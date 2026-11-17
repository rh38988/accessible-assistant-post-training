#!/usr/bin/env python3
"""Build rag-system-v1 candidates and provenance from source cards and drafts.

    python3 integration/grounded_sft_handoff/work/tools/build_gsft.py [--batch NAME]

Inputs (written by writer agents, never by reviewers):
  work/cards/<task_group>.json   source cards: one entry per checked official passage
  work/drafts/<batch>.json       candidates: conversation, route, section refs, target

Outputs:
  work/build/candidates.jsonl    training-format records (latest version of each id)
  work/build/provenance.jsonl    one provenance row per id (RECORD_FORMATS.md)
  work/build/build_report.json   counts, hashes, errors and warnings

The system and user messages are built only by prompt_contract.build_messages, so writers
never type the grounding rules. Exit code 1 if any candidate has an error.
"""
import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
HANDOFF = WORK.parent
ROOT = HANDOFF.parents[1]
sys.path.insert(0, str(ROOT))
from integration.grounded_sft_handoff.prompt_contract import build_messages, user_only_query  # noqa: E402
from scripts.validate_data import check_record  # noqa: E402

BEHAVIORS = {"direct", "clarify", "constraint", "multiturn"}
TAGS = {"safety", "distractor", "conditional"}
STYLES = {"plain", "verbose", "over_specified", "under_specified", "incomplete", "failure_recovery"}
CJK = re.compile(r"[　-鿿＀-￯]")
DASH = re.compile("[–—]")
CARD_KEYS = ("ref_id", "organization", "title", "url", "access_date", "section", "applicability",
             "verified_excerpt", "model_visible_text", "platform", "app", "extraction_method")
MAX_PER_GROUP = 8


def sha_messages(messages):
    return hashlib.sha256(json.dumps(messages, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def load_cards(errors, warnings):
    refs, groups = {}, {}
    for p in sorted((WORK / "cards").glob("*.json")):
        card = json.load(open(p, encoding="utf-8"))
        groups[card["task_group"]] = card
        for r in card["source_refs"]:
            missing = [k for k in CARD_KEYS if not r.get(k)]
            if missing:
                errors.append(f"card {p.name} {r.get('ref_id')}: missing {missing}")
            if not str(r.get("url", "")).startswith("https://"):
                errors.append(f"card {p.name} {r.get('ref_id')}: URL must be https")
            if r.get("ref_id") in refs:
                errors.append(f"card {p.name}: duplicate ref_id {r.get('ref_id')}")
            if CJK.search(r.get("model_visible_text", "")):
                errors.append(f"card {p.name} {r.get('ref_id')}: model-visible text must be English")
            if re.search(r'["\\\n]', r.get("model_visible_text", "")):
                # The builder JSON-escapes passages, so these would not appear verbatim in the
                # system message and validate_grounded.py would reject the mapping.
                warnings.append(f"card {p.name} {r.get('ref_id')}: double quote, backslash or line break; it cannot be used as an answer passage")
            refs[r["ref_id"]] = {**r, "_group": card["task_group"]}
    return refs, groups


def load_drafts(batch):
    latest = {}
    for p in sorted((WORK / "drafts").glob("*.json")):
        if batch and p.stem != batch:
            continue
        for c in json.load(open(p, encoding="utf-8"))["candidates"]:
            c["_file"] = p.name
            v = int(c["candidate_id"].rsplit("-v", 1)[1])
            if c["id"] not in latest or v > latest[c["id"]][0]:
                latest[c["id"]] = (v, c)
    return [c for _, c in latest.values()]


def build_one(c, refs, errors, warnings):
    cid = c.get("id", "?")
    def err(msg): errors.append(f"{cid}: {msg}")
    def warn(msg): warnings.append(f"{cid}: {msg}")

    for k in ("id", "candidate_id", "task_id", "task_group", "source_group", "behavior", "category", "platform",
              "sensitive", "style", "source_conversation", "decision", "decision_basis", "source_ref_ids", "target"):
        if k not in c:
            err(f"missing {k}")
            return None
    if not c["candidate_id"].startswith(cid + "-v"):
        err("candidate_id must be <id>-v<N>")
    if c["behavior"] not in BEHAVIORS:
        err(f"behavior must be one of {sorted(BEHAVIORS)}")
    if not set(c.get("tags", [])) <= TAGS:
        err(f"tags must be within {sorted(TAGS)}")
    if c["style"] not in STYLES:
        err(f"style must be one of {sorted(STYLES)}")
    conv, decision, target = c["source_conversation"], c["decision"], c["target"].strip()
    mode = decision.get("mode")

    text_all = " ".join(t["content"] for t in conv) + " " + target + " " + decision.get("question", "")
    if CJK.search(text_all):
        err("English only: CJK characters found")
    if DASH.search(target) or any(DASH.search(t["content"]) for t in conv):
        err("no em or en dashes in conversation or target")
    if not conv or conv[0]["role"] != "user" or conv[-1]["role"] != "user":
        err("source conversation must start and end with a user turn")
    roles = [t["role"] for t in conv]
    if any(a == b for a, b in zip(roles, roles[1:])):
        err("source conversation roles must alternate")
    users = [t for t in conv if t["role"] == "user"]
    if c["behavior"] == "multiturn":
        if len(users) < 2 or "assistant" not in roles:
            err("multiturn needs at least user, assistant, user")
    elif len(conv) != 1:
        err("non-multiturn candidates have exactly one user turn")

    missing_refs = [r for r in c["source_ref_ids"] if r not in refs]
    if missing_refs:
        err(f"unknown source_ref_ids {missing_refs}")
        return None
    used = [refs[r] for r in c["source_ref_ids"]]
    if any(r["_group"] != c["task_group"] for r in used):
        warn("uses a source card from another task group")

    if mode == "clarify":
        if c["behavior"] != "clarify":
            err("clarify route only for behavior clarify")
        q = decision.get("question", "").strip()
        if not q or q.count("?") != 1 or not q.endswith("?"):
            err("clarify question must be one question ending with ?")
        if target != q:
            err("clarify target must equal the routed question exactly")
        if c.get("section_ref_ids"):
            err("clarify must not include section_ref_ids")
        if len(used) < 2:
            err("clarify needs at least two source refs showing the procedure differs")
        sections = []
        if c.get("sensitive") and "safety" in c.get("tags", []):
            err("safety cases must not be clarify-only")
    elif mode == "answer":
        if c["behavior"] == "clarify":
            err("behavior clarify needs the clarify route")
        if c.get("section_ref_ids") is not None and c["section_ref_ids"] != c["source_ref_ids"]:
            err("for answer, section_ref_ids must equal source_ref_ids")
        sections = [{"platform": r["platform"], "app": r["app"], "text": r["model_visible_text"]} for r in used]
        if "distractor" in c.get("tags", []) and len(used) < 2:
            err("distractor tag needs a second (inapplicable) passage")
        if not re.search(r"(?m)^\s*1\.\s", target) and c["behavior"] != "clarify":
            warn("answer has no numbered steps")
    else:
        err("decision.mode must be answer or clarify")
        return None

    try:
        prompt = build_messages(user_only_query(conv), {"mode": mode, "question": decision.get("question", "")},
                                sections, accessibility="")
    except ValueError as e:
        err(str(e))
        return None
    messages = prompt + [{"role": "assistant", "content": target}]
    if mode == "answer" and any(sec["text"] not in messages[0]["content"] for sec in sections):
        err("a passage does not appear verbatim in the system message")
    chars = sum(len(m["content"]) for m in messages)
    if chars / 3.2 > 900:
        warn(f"long: about {int(chars / 3.2)} tokens by character estimate (limit 1028, exact check needs the Qwen tokenizer)")

    sources, seen = [], set()
    for r in used:
        if r["url"] not in seen:
            seen.add(r["url"])
            sources.append({"title": r["title"], "url": r["url"], "accessed": r["access_date"]})
    record = {"id": cid, "messages": messages,
              "specification": "underspecified" if mode == "clarify" else "fully_specified",
              "category": c["category"], "platform": c["platform"], "language": "en",
              "sensitive": bool(c["sensitive"]), "sources": sources, "task_id": c["task_id"],
              "task_group": c["task_group"], "source_group": c["source_group"], "style": c["style"],
              "author": "claude-haiku-writer-gsft", "reviewed": False, "prompt_format": "rag-system-v1"}
    errs = []
    check_record(record, "train", errs, cid)
    for e in errs:
        err(e)
    digest = sha_messages(messages)
    prov = {
        "id": cid, "task_id": c["task_id"], "task_group": c["task_group"], "source_group": c["source_group"],
        "content_sha256": digest, "eligibility": "pending_eval_owner_clearance",
        "behavior": c["behavior"], "tags": sorted(c.get("tags", [])),
        "generation": {"method": "Claude Haiku writer agent, work/AGENT_GSFT_WRITER.md", "model": "claude-haiku-5-5",
                       "prompt_version": "rag-system-v1", "candidate_id": c["candidate_id"], "draft_file": c["_file"]},
        "inference_template": {"builder": "eval.generate_rag.build_messages", "condition": "sft_v2_rag",
                               "decision": {"mode": mode, "question": decision.get("question", "") if mode == "clarify" else ""},
                               "decision_basis": c["decision_basis"], "accessibility": "",
                               "source_conversation": conv, "sections": sections,
                               "section_ref_ids": c["source_ref_ids"] if mode == "answer" else []},
        "source_refs": [{k: r[k] for k in ("ref_id", "organization", "title", "url", "access_date", "page_update_date",
                                           "section", "applicability", "verified_excerpt", "model_visible_text",
                                           "extraction_method") if k in r} for r in used],
        "author_note": c.get("author_note", ""),
        "correction_history": c.get("correction_history", []),
    }
    return record, prov


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch")
    a = ap.parse_args()
    errors, warnings = [], []
    refs, groups = load_cards(errors, warnings)
    cands = load_drafts(a.batch)
    records, provs = [], []
    for c in sorted(cands, key=lambda c: c["id"]):
        out = build_one(c, refs, errors, warnings)
        if out:
            records.append(out[0])
            provs.append(out[1])
    per_group = collections.Counter(r["task_group"] for r in records)
    for g, n in per_group.items():
        if n > MAX_PER_GROUP:
            warnings.append(f"group {g}: {n} candidates (at most {MAX_PER_GROUP} can be accepted)")
    ids = [r["id"] for r in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate ids")
    build = WORK / "build"
    build.mkdir(exist_ok=True)
    with open(build / "candidates.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(build / "provenance.jsonl", "w", encoding="utf-8") as f:
        for p in provs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    report = {"candidates": len(records), "groups": len(per_group),
              "behavior": dict(collections.Counter(p["behavior"] for p in provs)),
              "tags": dict(collections.Counter(t for p in provs for t in p["tags"])),
              "per_group": dict(per_group), "errors": errors, "warnings": warnings,
              "hashes": {p["id"]: p["content_sha256"] for p in provs}}
    json.dump(report, open(build / "build_report.json", "w", encoding="utf-8"), indent=1)
    print(f"candidates {len(records)} | groups {len(per_group)} | behavior {report['behavior']} | tags {report['tags']}")
    print(f"errors {len(errors)} | warnings {len(warnings)}")
    for e in errors[:40]:
        print("ERROR", e)
    for w in warnings[:20]:
        print("warn", w)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
