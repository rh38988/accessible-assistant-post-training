#!/usr/bin/env python3
"""Assemble the frozen train_v2 English set from reviewed candidates.

    python3 data/v2/tools/assemble.py [--target 1000] [--seed 42]

Keeps an example only if its latest independent review says `keep`
(examples a person already reviewed are kept and listed if the AI reviewer
disagreed). Then runs the code checks, enforces at most 6 examples per task,
selects the target number, and writes:

    data/v2/train_v2_en.jsonl              frozen training file (existing schema)
    data/v2/train_v2_en.manifest.json      version, file hash, per-example hashes
    data/v2/train_v2_index.csv             one row per candidate: decision and provenance
    data/v2/train_v2_reserve.jsonl         kept examples beyond the target
    data/v2/spot_check_v2.csv              random sample for the human spot check
    data/v2/SUMMARY_v2.md                  funnel and distribution
"""
import argparse
import csv
import difflib
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"
sys.path.insert(0, str(REPO))
from scripts.validate_data import check_record  # noqa: E402

MAX_CHARS = 2200
PER_TASK_CAP = 6
BUCKET = {"direct": "direct", "direct_messy": "direct", "helper": "direct", "prevention": "direct",
          "missing_info": "missing information", "followup": "missing information",
          "constraint": "constraint", "failure_recovery": "failure recovery", "already_acted": "failure recovery"}


def norm(text):
    return re.sub(r"[^a-z0-9 ]", "", text.lower())


def sha(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def load():
    recs, meta, reviews, rounds = {}, {}, {}, Counter()
    for path in sorted((V2 / "cand").glob("*.jsonl")):
        for line in open(path, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                recs[r["id"]] = r
        meta.update(json.load(open(path.with_suffix("").with_suffix(".meta.json"), encoding="utf-8")))
    files = sorted((V2 / "reviews").glob("*.r*.jsonl"), key=lambda p: int(p.stem.split(".r")[-1]))
    for path in files:
        for line in open(path, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                reviews[r["id"]] = r
                rounds[r["id"]] = max(rounds[r["id"]], r["round"])
    return recs, meta, reviews, rounds


def revised_ids():
    """Ids whose text changed between the first snapshot and the current candidate file."""
    first = {}
    for path in sorted((V2 / "snapshots").glob("*.before_revise*.jsonl")):
        for line in open(path, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                first.setdefault(r["id"], r["messages"])
    return first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--spot", type=int, default=50)
    ap.add_argument("--rebuild-frozen", action="store_true",
                    help="overwrite a frozen version (drops human fixes made after the AI review)")
    args = ap.parse_args()
    rng = random.Random(args.seed)

    # Guard: v2.1 and later carry human fixes made directly on the frozen file
    # (see data/v2/human_fixes/ and tools/apply_human_fixes.py). Rebuilding from the
    # review records would silently undo them.
    man_path = V2 / "train_v2_en.manifest.json"
    if man_path.exists() and not args.rebuild_frozen:
        version = json.load(open(man_path, encoding="utf-8")).get("version", "")
        if not version.endswith("-interim"):
            sys.exit(f"train_v2_en is frozen at {version}; not overwriting. "
                     "To change it, edit data/v2/human_fixes/ and run tools/apply_human_fixes.py.")

    recs, meta, reviews, rounds = load()
    first_text = revised_ids()
    eval_types = {r["task_type"] for r in csv.DictReader(open(REPO / "eval/tasks/eval_tasks.csv", encoding="utf-8"))}
    eval_prompts = [norm(json.loads(l)["prompt"][0]["content"])
                    for l in open(REPO / "eval/scenarios/eval_v1.jsonl", encoding="utf-8") if l.strip()]

    status, why = {}, {}
    for rid, rec in recs.items():
        rv = reviews.get(rid)
        if rv is None:
            status[rid], why[rid] = "not_reviewed", "no review record"
        elif rv["decision"] == "keep":
            status[rid] = "keep"
        elif rec["reviewed"]:
            status[rid], why[rid] = "keep", "human-reviewed; AI reviewer flagged: " + rv["reasons"]
        elif rv["decision"] == "reject":
            status[rid], why[rid] = "rejected", rv["reasons"]
        else:
            status[rid], why[rid] = "dropped_unresolved", rv["reasons"]

    # Code checks on the kept examples.
    kept = [rid for rid in recs if status[rid] == "keep"]
    seen_pair, seen_open = {}, []
    for rid in kept:
        rec, m = recs[rid], meta[rid]
        errs = []
        check_record(rec, "train", errs, rid)
        text = norm(rec["messages"][0]["content"])
        if errs:
            status[rid], why[rid] = "dropped_code_check", "; ".join(errs)
        elif sum(len(x["content"]) for x in rec["messages"]) > MAX_CHARS:
            status[rid], why[rid] = "dropped_code_check", "over the length cap"
        elif m["task_type"] in eval_types:
            status[rid], why[rid] = "dropped_code_check", "held-out evaluation task type"
        elif any(difflib.SequenceMatcher(None, text, e).ratio() >= 0.7 for e in eval_prompts):
            status[rid], why[rid] = "dropped_code_check", "too similar to an evaluation prompt"
        else:
            pair = (text, norm(rec["messages"][-1]["content"]), len(rec["messages"]))
            if pair in seen_pair:
                status[rid], why[rid] = "dropped_code_check", f"exact duplicate of {seen_pair[pair]}"
                continue
            seen_pair[pair] = rid
            dup = None
            for oid, otask, otext in seen_open:
                if otask != rec["task_id"] and abs(len(otext) - len(text)) <= 0.3 * max(len(otext), len(text), 1):
                    sm = difflib.SequenceMatcher(None, text, otext)
                    if sm.quick_ratio() >= 0.9 and sm.ratio() >= 0.9:
                        dup = oid
                        break
            if dup and not rec["reviewed"]:
                status[rid], why[rid] = "dropped_code_check", f"near-duplicate opening of {dup} (another task)"
            else:
                seen_open.append((rid, rec["task_id"], text))

    # At most PER_TASK_CAP per task; prefer human-reviewed, then one per scenario.
    by_task = defaultdict(list)
    for rid in recs:
        if status[rid] == "keep":
            by_task[recs[rid]["task_id"]].append(rid)
    for task, ids in by_task.items():
        if len(ids) > PER_TASK_CAP:
            ids.sort(key=lambda i: (not recs[i]["reviewed"], i))
            chosen, scen_seen = [], set()
            for i in ids:
                if meta[i]["scenario"] not in scen_seen and len(chosen) < PER_TASK_CAP:
                    chosen.append(i)
                    scen_seen.add(meta[i]["scenario"])
            for i in ids:
                if i not in chosen and len(chosen) < PER_TASK_CAP:
                    chosen.append(i)
            for i in ids:
                if i not in chosen:
                    status[i], why[i] = "reserve", "over the per-task cap"

    # Select the target number: trim the fullest scenario buckets first, never human-reviewed ones.
    kept = [rid for rid in recs if status[rid] == "keep"]
    extra = len(kept) - args.target
    if extra > 0:
        pool = defaultdict(list)
        for rid in kept:
            if not recs[rid]["reviewed"]:
                pool[meta[rid]["scenario"]].append(rid)
        for ids in pool.values():
            rng.shuffle(ids)
        counts = Counter(meta[rid]["scenario"] for rid in kept)
        while extra > 0:
            scen = max((s for s in pool if pool[s]), key=lambda s: counts[s])
            rid = pool[scen].pop()
            status[rid], why[rid] = "reserve", "kept, but beyond the target size"
            counts[scen] -= 1
            extra -= 1

    final = sorted((rid for rid in recs if status[rid] == "keep"),
                   key=lambda i: (recs[i]["task_id"], i))
    reserve = sorted(rid for rid in recs if status[rid] == "reserve")

    # Write outputs.
    out = V2 / "train_v2_en.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for rid in final:
            f.write(json.dumps(recs[rid], ensure_ascii=False) + "\n")
    with open(V2 / "train_v2_reserve.jsonl", "w", encoding="utf-8") as f:
        for rid in reserve:
            f.write(json.dumps(recs[rid], ensure_ascii=False) + "\n")
    file_hash = hashlib.sha256(out.read_bytes()).hexdigest()
    manifest = {"name": "train_v2_en", "version": "v2.0-interim", "created": "2026-11-13", "language": "en",
                "count": len(final), "file": "data/v2/train_v2_en.jsonl", "sha256": file_hash,
                "label": "AI-screened, with human spot checks",
                "human_reviewed_count": sum(recs[i]["reviewed"] for i in final),
                "examples": [{"id": i, "sha256": sha(recs[i])} for i in final]}
    json.dump(manifest, open(V2 / "train_v2_en.manifest.json", "w", encoding="utf-8"), indent=1)

    with open(V2 / "train_v2_index.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "final_status", "task_id", "task_type", "task_platform", "scenario", "style", "specification",
                    "sensitive", "origin", "human_reviewed", "ai_decision", "review_rounds", "text_revised",
                    "source_url", "batch", "note"])
        for rid in sorted(recs, key=lambda i: (recs[i]["task_id"], i)):
            rec, m, rv = recs[rid], meta[rid], reviews.get(rid, {})
            changed = rid in first_text and first_text[rid] != rec["messages"]
            w.writerow([rid, "train_v2" if status[rid] == "keep" else status[rid], rec["task_id"], m["task_type"],
                        m["task_platform"], m["scenario"], rec["style"], rec["specification"], rec["sensitive"],
                        "existing_draft" if m["existing"] else "new_v2", rec["reviewed"], rv.get("decision", ""),
                        rounds.get(rid, 0), changed, m["source_url"], m["batch"], why.get(rid, "")])

    # Spot-check sample, stratified by scenario bucket and sensitivity.
    cand = [i for i in final if not recs[i]["reviewed"]]
    strata = defaultdict(list)
    for i in cand:
        strata[(BUCKET[meta[i]["scenario"]], recs[i]["sensitive"])].append(i)
    sample = []
    keys = sorted(strata)
    for k in keys:
        rng.shuffle(strata[k])
    while len(sample) < min(args.spot, len(cand)):
        for k in keys:
            if strata[k] and len(sample) < args.spot:
                sample.append(strata[k].pop())
    spot_path = V2 / "spot_check_v2.csv"
    if spot_path.exists():
        spot_path = V2 / "spot_check_v2.new.csv"  # never overwrite a filled-in spot check
    with open(spot_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "task", "platform", "scenario", "sensitive", "source_url",
                    "reviewer", "steps_match_source", "decision", "notes"])
        for i in sorted(sample):
            w.writerow([i, meta[i]["task"], meta[i]["task_platform"], meta[i]["scenario"], recs[i]["sensitive"],
                        meta[i]["source_url"], "", "", "", ""])

    # Summary.
    st = Counter(status.values())
    origin = Counter(("existing" if meta[i]["existing"] else "new") for i in recs)
    fin_origin = Counter(("existing" if meta[i]["existing"] else "new") for i in final)
    scen = Counter(BUCKET[meta[i]["scenario"]] for i in final)
    fam = Counter(recs[i]["category"] for i in final)
    lines = ["# train_v2 (English) summary", "",
             f"Frozen file: `data/v2/train_v2_en.jsonl` | {len(final)} examples | sha256 `{file_hash}`", "",
             "Label for reports: **AI-screened, with human spot checks.**", "",
             "## Funnel", "", "| Stage | Count |", "|---|---|",
             f"| Candidates reviewed | {len(recs)} ({origin['existing']} existing English drafts, {origin['new']} new) |",
             f"| Kept by the independent AI review | {sum(1 for i in recs if reviews.get(i, {}).get('decision') == 'keep')} |",
             f"| Rejected by the reviewer | {st['rejected']} |",
             f"| Flagged for revision, not yet resolved | {st['dropped_unresolved']} |",
             f"| Dropped by code checks (duplicates, length, overlap) | {st['dropped_code_check']} |",
             f"| Not reviewed | {st['not_reviewed']} |",
             f"| Kept but held in reserve | {st['reserve']} |",
             f"| **Final training set** | **{len(final)}** ({fin_origin['existing']} from existing drafts, {fin_origin['new']} new) |", "",
             f"Text changed during revision: {sum(1 for i in final if i in first_text and first_text[i] != recs[i]['messages'])} of the final examples.",
             f"Human-reviewed examples in the final set: {sum(recs[i]['reviewed'] for i in final)}.", "",
             "## Distribution of the final set", "",
             "| Scenario | Count | Share |", "|---|---|---|"]
    for k, v in scen.most_common():
        lines.append(f"| {k} | {v} | {v / max(len(final), 1):.0%} |")
    lines += ["", "| Category | Count |", "|---|---|"] + [f"| {k} | {v} |" for k, v in fam.most_common()]
    lines += ["", f"- Sensitive (safety, accounts, privacy): {sum(recs[i]['sensitive'] for i in final)}",
              f"- Multi-turn: {sum(len(recs[i]['messages']) > 2 for i in final)}",
              f"- Tasks: {len({recs[i]['task_id'] for i in final})} | task types: {len({meta[i]['task_type'] for i in final})} | official pages: {len({s['url'] for i in final for s in recs[i]['sources']})}",
              f"- Longest conversation: {max(sum(len(x['content']) for x in recs[i]['messages']) for i in final) if final else 0} characters (cap {MAX_CHARS})",
              ""]
    (V2 / "SUMMARY_v2.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print("status:", dict(st))


if __name__ == "__main__":
    main()
