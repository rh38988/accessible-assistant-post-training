#!/usr/bin/env python3
"""Review plumbing for grounded SFT candidates.

    python3 review_io.py render <batch> <N>   # write reviews/input/<batch>.r<N>.md for candidates needing review
    python3 review_io.py check  <batch> <N>   # validate reviews/<batch>.r<N>.jsonl against current hashes
    python3 review_io.py status               # latest review per id, across all batches

Run build_gsft.py first: hashes come from build/provenance.jsonl. A review counts only
for the exact conversation hash it names; an edited candidate needs a new review.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
ROOT_GIT = Path(__file__).resolve().parents[4]
REVIEWER_DOC = WORK / "AGENT_GSFT_REVIEWER.md"
CHECKS = ["factual_steps_labels_contacts_claims", "necessary_action_coverage",
          "explicit_constraints_and_completed_state", "clarification_decision",
          "no_invented_history_or_unsupported_content", "one_action_per_step",
          "brevity_without_omission", "safety"]


def jl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def build(batch=None):
    d = WORK / "build" / batch if batch and (WORK / "build" / batch).exists() else WORK / "build"
    recs = {r["id"]: r for r in jl(d / "candidates.jsonl")}
    prov = {p["id"]: p for p in jl(d / "provenance.jsonl")}
    return recs, prov


def all_reviews():
    out = {}
    for p in sorted((WORK / "reviews").glob("*.r*.jsonl")):
        for r in jl(p):
            out[(r["id"], r["conversation_sha256"])] = r
    return out


def current_review(done, prov, i):
    """The review for this id's exact hash AND current candidate version. A new version
    whose model-visible messages did not change (e.g. only the earlier assistant turn)
    still needs a fresh review."""
    r = done.get((i, prov[i]["content_sha256"]))
    if not r or r.get("candidate_id") != prov[i]["generation"]["candidate_id"]:
        return None
    # A review that could not read a source page is not a verdict: review again.
    if any(sc.get("source_accessible") is not True for sc in r.get("source_checks") or []):
        return None
    return r


def batch_ids(prov, batch):
    return [i for i, p in prov.items() if p["generation"]["draft_file"] == f"{batch}.json"]


REDO = set()  # ids to re-review even if their hash has a review (set with --redo a,b)


def render(batch, n):
    recs, prov = build(batch)
    done = all_reviews()
    ids = [i for i in batch_ids(prov, batch) if not current_review(done, prov, i) or i in REDO]
    lines = [f"# Review input: {batch}, round {n} ({len(ids)} candidates)\n"]
    for i in ids:
        p, t = prov[i], prov[i]["inference_template"]
        lines += [f"## {i}", f"- candidate_id: {p['generation']['candidate_id']}",
                  f"- conversation_sha256: {p['content_sha256']}",
                  f"- task_group: {p['task_group']} | behavior: {p['behavior']} | tags: {', '.join(p['tags']) or 'none'}",
                  f"- route: {t['decision']['mode']}" + (f" | routed question: {t['decision']['question']}" if t['decision']['mode'] == 'clarify' else ""),
                  f"- decision basis (writer's): {t['decision_basis']}", "", "Conversation (the model sees only the user turns, joined):"]
        for turn in t["source_conversation"]:
            lines.append(f"> **{turn['role']}:** " + turn["content"].replace("\n", "\n> "))
        lines.append("")
        if t["sections"]:
            lines.append("Passages the model sees (in this order):")
            for s, rid in zip(t["sections"], t["section_ref_ids"]):
                lines.append(f"- [{rid}] platform: {s['platform']} | app: {s['app']}\n  > {s['text']}")
        else:
            lines.append("Passages the model sees: none (clarify route)")
        lines.append("\nSource references to check:")
        for r in p["source_refs"]:
            lines.append(f"- {r['ref_id']}: {r['organization']}, \"{r['title']}\" <{r['url']}> | section: {r['section']} "
                         f"| applicability: {r['applicability']} | excerpt: \"{r['verified_excerpt']}\"")
        lines += ["", "TARGET (read only after step 2)", "", "> " + recs[i]["messages"][-1]["content"].replace("\n", "\n> "), "", "---", ""]
    out = WORK / f"reviews/input/{batch}.r{n}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    json.dump(ids, open(out.with_suffix(".ids.json"), "w"))
    print(f"wrote {out} ({len(ids)} candidates)")


def check(batch, n):
    recs, prov = build(batch)
    ids = json.load(open(WORK / f"reviews/input/{batch}.r{n}.ids.json"))
    path = WORK / f"reviews/{batch}.r{n}.jsonl"
    errs = []
    rows = jl(path) if path.exists() else []
    if [r.get("id") for r in rows] != ids:
        errs.append(f"need one row per candidate in input order; got {[r.get('id') for r in rows][:5]}... expected {ids[:5]}...")
    prompt_sha = hashlib.sha256(REVIEWER_DOC.read_bytes()).hexdigest()
    for r in rows:
        i = r.get("id")
        p = prov.get(i)
        if not p:
            errs.append(f"{i}: unknown id")
            continue
        if r.get("conversation_sha256") != p["content_sha256"]:
            errs.append(f"{i}: conversation_sha256 does not match the current candidate")
        if r.get("candidate_id") != p["generation"]["candidate_id"]:
            errs.append(f"{i}: candidate_id should be {p['generation']['candidate_id']}")
        for k in ("review_id", "reviewer_model", "reviewed_at", "source_checks", "required_actions", "checks", "decision"):
            if k not in r:
                errs.append(f"{i}: missing {k}")
        if r.get("decision") not in ("keep", "revise", "reject"):
            errs.append(f"{i}: decision must be keep, revise or reject")
        checks = r.get("checks") or {}
        bad = [c for c in CHECKS if checks.get(c) not in ("pass", "fail", "unverified")]
        if bad:
            errs.append(f"{i}: checks need pass/fail/unverified for {bad}")
        refs = [x["ref_id"] for x in p["source_refs"]]
        got = [s.get("ref_id") for s in r.get("source_checks") or []]
        if sorted(got) != sorted(refs):
            errs.append(f"{i}: source_checks must cover exactly {refs}")
        if r.get("decision") == "keep":
            if any(checks.get(c) != "pass" for c in CHECKS):
                errs.append(f"{i}: keep needs every check = pass")
            if r.get("findings") or r.get("correction_required"):
                errs.append(f"{i}: keep needs empty findings and correction_required")
            if any(s.get("source_accessible") is not True or s.get("applicability_confirmed") is not True
                   or not s.get("finding") for s in r.get("source_checks") or []):
                errs.append(f"{i}: keep needs every source accessible and applicable, with a finding")
            if any(a.get("critical") and not a.get("covered_in_target") for a in r.get("required_actions") or []):
                errs.append(f"{i}: keep with an uncovered critical action")
        elif not r.get("findings"):
            errs.append(f"{i}: revise/reject needs findings")
        r["reviewer_prompt_sha256"] = prompt_sha
    if errs:
        print("\n".join(errs[:40]))
        sys.exit(1)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"OK {batch} r{n}: {dict(Counter(r['decision'] for r in rows))}")


def status():
    recs, prov = build()
    done = all_reviews()
    st = Counter()
    for i, p in prov.items():
        r = current_review(done, prov, i)
        st[r["decision"] if r else "not reviewed"] += 1
    print(dict(st))


def stamp(batch, n, rev):
    """Add reviewer_prompt_sha256 to rows of a review file whose batch-wide check never passed
    (for example because other rows in it were superseded). Each stamped row must still bind to
    the current candidate and pass every per-row check; the hash is of the reviewer document as
    it was at git revision `rev`, the version the reviewer actually followed."""
    import subprocess
    doc = subprocess.run(["git", "show", f"{rev}:{REVIEWER_DOC.relative_to(ROOT_GIT)}"], cwd=ROOT_GIT,
                         capture_output=True, check=True).stdout
    prompt_sha = hashlib.sha256(doc).hexdigest()
    recs, prov = build()
    path = WORK / f"reviews/{batch}.r{n}.jsonl"
    rows = jl(path)
    stamped = 0
    for r in rows:
        i, p = r.get("id"), prov.get(r.get("id"))
        if r.get("reviewer_prompt_sha256") or not p:
            continue
        if r.get("conversation_sha256") != p["content_sha256"] or r.get("candidate_id") != p["generation"]["candidate_id"]:
            continue  # superseded by a later version; leave as historical record
        checks = r.get("checks") or {}
        refs = sorted(x["ref_id"] for x in p["source_refs"])
        ok = (sorted(s.get("ref_id") for s in r.get("source_checks") or []) == refs and
              all(k in r for k in ("review_id", "reviewer_model", "reviewed_at", "required_actions", "decision")))
        if r.get("decision") == "keep":
            ok = ok and all(checks.get(c) == "pass" for c in CHECKS) and not r.get("findings") \
                and not r.get("correction_required") \
                and all(s.get("source_accessible") is True and s.get("applicability_confirmed") is True and s.get("finding")
                        for s in r["source_checks"]) \
                and not any(a.get("critical") and not a.get("covered_in_target") for a in r["required_actions"])
        if ok:
            r["reviewer_prompt_sha256"] = prompt_sha
            stamped += 1
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"stamped {stamped} rows of {batch} r{n} with the reviewer document at {rev} ({prompt_sha[:12]})")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "render":
        if "--redo" in sys.argv:
            REDO.update(sys.argv[sys.argv.index("--redo") + 1].split(","))
        render(sys.argv[2], int(sys.argv[3]))
    elif cmd == "stamp":
        stamp(sys.argv[2], int(sys.argv[3]), sys.argv[4])
    elif cmd == "check":
        check(sys.argv[2], int(sys.argv[3]))
    else:
        status()
