#!/usr/bin/env python3
"""Build and check one train_v2 candidate batch.

    python3 data/v2/tools/build_v2.py <batch>

Reads   data/v2/specs/<batch>.py     (defines TASKS, see GENERATION_SPEC_v1.md)
Writes  data/v2/cand/<batch>.jsonl   (training records, existing schema)
        data/v2/cand/<batch>.meta.json (scenario, task type, source per id)

Prints errors (must be fixed) and warnings (double-check). Exit code 1 on errors.
Standard library only.
"""
import csv
import difflib
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"
sys.path.insert(0, str(REPO))
from scripts.validate_data import STYLES, CATEGORIES, check_record  # noqa: E402

ACCESSED = "2026-11-13"
MAX_CHARS = 2200          # whole conversation; stands in for the 768-token cap
SCENARIOS = {"direct", "direct_messy", "missing_info", "followup", "constraint",
             "failure_recovery", "already_acted", "helper", "prevention"}
MULTI_TURN_OK = {"followup", "failure_recovery"}


def norm(text):
    return re.sub(r"[^a-z0-9 ]", "", text.lower())


def similar(a, b):
    """Similarity of two normalized strings, with a cheap pre-filter."""
    if not a or not b:
        return 0.0
    if abs(len(a) - len(b)) > 0.4 * max(len(a), len(b)):
        return 0.0
    m = difflib.SequenceMatcher(None, a, b)
    if m.quick_ratio() < 0.7:
        return 0.0
    return m.ratio()


def load_spec(batch):
    path = V2 / "specs" / f"{batch}.py"
    spec = importlib.util.spec_from_file_location(f"spec_{batch}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TASKS


def build_records(batch, tasks, errors):
    records, meta = [], {}
    for ti, t in enumerate(tasks):
        where = f"task[{ti}] {t.get('task_id', '?')}"
        missing = [k for k in ("task_id", "task_type", "task", "platform", "category", "sensitive", "source", "examples")
                   if k not in t]
        if missing:
            errors.append(f"{where}: missing keys {missing}")
            continue
        if not re.fullmatch(r"TR-\d{3}", str(t["task_id"])):
            errors.append(f"{where}: task_id must look like TR-117")
            continue
        if t["category"] not in CATEGORIES:
            errors.append(f"{where}: category must be one of {sorted(CATEGORIES)}")
        if not isinstance(t["sensitive"], bool):
            errors.append(f"{where}: sensitive must be True or False")
        src = t["source"]
        if not (isinstance(src, dict) and str(src.get("url", "")).startswith("https://") and src.get("title")):
            errors.append(f"{where}: source needs a title and an https url")
            continue
        n = int(t["task_id"].split("-")[1])
        seen_suffix = set()
        for ei, ex in enumerate(t["examples"]):
            w = f"{where} example[{ei}] {ex.get('suffix', '?')}"
            miss = [k for k in ("suffix", "scenario", "style", "specification", "platform", "messages") if k not in ex]
            if miss:
                errors.append(f"{w}: missing keys {miss}")
                continue
            if ex["suffix"] in seen_suffix:
                errors.append(f"{w}: duplicate suffix in this task")
            seen_suffix.add(ex["suffix"])
            msgs = ex["messages"]
            if not (isinstance(msgs, list) and len(msgs) >= 2 and len(msgs) % 2 == 0
                    and all(isinstance(m, str) and m.strip() for m in msgs)):
                errors.append(f"{w}: messages must be an even-length list of non-empty strings (user, assistant, ...)")
                continue
            existing = bool(ex.get("existing"))
            if not existing and not str(t.get("source_notes", "")).strip():
                errors.append(f"{where}: source_notes is required for new examples")
            style = ex["style"]
            inspired = ex.get("inspired_by") or (
                "OATS" if style in ("verbose", "over_specified", "incomplete")
                else "GrandGuard" if t["sensitive"] else "original")
            rec = {
                "id": ex.get("id") or f"tr{n:03d}-{ex['suffix']}",
                "messages": [{"role": "user" if i % 2 == 0 else "assistant", "content": m.strip()}
                             for i, m in enumerate(msgs)],
                "specification": ex["specification"],
                "category": t["category"],
                "platform": ex["platform"],
                "language": "en",
                "sensitive": t["sensitive"],
                "sources": ex.get("sources") or [{"title": src["title"], "url": src["url"], "accessed": ACCESSED}],
                "task_id": t["task_id"],
                "inspired_by": inspired,
                "style": style,
                "author": ex.get("author", "claude-draft"),
                "reviewed": bool(ex.get("reviewed", False)),
            }
            records.append(rec)
            meta[rec["id"]] = {"batch": batch, "scenario": ex["scenario"], "task_type": t["task_type"],
                               "task": t["task"], "task_platform": t["platform"], "source_url": src["url"],
                               "existing": existing}
    return records, meta


def check(batch, records, meta, errors, warnings):
    eval_types = {r["task_type"] for r in csv.DictReader(open(REPO / "eval/tasks/eval_tasks.csv", encoding="utf-8"))}
    eval_prompts = []
    for line in open(REPO / "eval/scenarios/eval_v1.jsonl", encoding="utf-8"):
        if line.strip():
            e = json.loads(line)
            eval_prompts.append((e["id"], norm(e["prompt"][0]["content"])))

    # Everything already built in other batches, for id and near-duplicate checks.
    others = []
    for path in sorted((V2 / "cand").glob("*.jsonl")):
        if path.stem == batch:
            continue
        for line in open(path, encoding="utf-8"):
            if line.strip():
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue      # another batch is being written right now; skip the partial line
                others.append((r["id"], r["task_id"], norm(r["messages"][0]["content"]), len(r["messages"])))
    other_ids = {o[0] for o in others}

    seen = set()
    mine = []
    for rec in records:
        rid, m = rec["id"], meta[rec["id"]]
        new = not m["existing"]
        soft = errors if new else warnings          # style rules are warnings for existing drafts
        if rid in seen or rid in other_ids:
            errors.append(f"{rid}: duplicate id")
        seen.add(rid)
        check_record(rec, "train", errors, rid)
        if m["task_type"] in eval_types:
            errors.append(f"{rid}: task_type '{m['task_type']}' is a held-out evaluation task type")
        scen, msgs = m["scenario"], rec["messages"]
        final = msgs[-1]["content"]
        if scen not in SCENARIOS:
            errors.append(f"{rid}: scenario must be one of {sorted(SCENARIOS)}")
        if rec["style"] not in STYLES:
            errors.append(f"{rid}: style must be one of {sorted(STYLES)}")
        want = "underspecified" if scen == "missing_info" else "fully_specified"
        if rec["specification"] != want:
            errors.append(f"{rid}: scenario '{scen}' needs specification '{want}'")
        total = sum(len(x["content"]) for x in msgs)
        if total > MAX_CHARS:
            errors.append(f"{rid}: conversation is {total} characters; the cap is {MAX_CHARS}")
        if any(ch in x["content"] for x in msgs for ch in "—–"):
            soft.append(f"{rid}: contains an em dash or en dash")
        if scen == "missing_info":
            if final.count("?") != 1:
                soft.append(f"{rid}: a missing-information reply must have exactly one question mark (has {final.count('?')})")
            if re.search(r"(^|\n)\s*1\.", final):
                soft.append(f"{rid}: a missing-information reply must not contain steps")
            if len(final.split()) > 50:
                soft.append(f"{rid}: clarifying reply is {len(final.split())} words; keep it under 50")
            if len(msgs) != 2:
                errors.append(f"{rid}: missing_info must be exactly 2 messages")
        else:
            if final.rstrip().endswith("?"):
                soft.append(f"{rid}: the reply ends with a question; answers must not end by asking")
            if len(final.split()) < 25:
                warnings.append(f"{rid}: reply is very short ({len(final.split())} words)")
            if len(final.split()) > 260:
                warnings.append(f"{rid}: reply is long ({len(final.split())} words)")
            if not rec["sensitive"] and not re.search(r"(^|\n)\s*1\.", final) and scen != "failure_recovery":
                warnings.append(f"{rid}: no numbered steps in the reply")
        if scen == "followup" and len(msgs) != 4:
            errors.append(f"{rid}: followup must be exactly 4 messages")
        if scen == "failure_recovery" and len(msgs) < 4:
            errors.append(f"{rid}: failure_recovery must be multi-turn (at least 4 messages)")
        if len(msgs) > 2 and scen not in MULTI_TURN_OK and scen != "already_acted":
            warnings.append(f"{rid}: {len(msgs)} messages for scenario '{scen}'")
        if "http" in final and new:
            warnings.append(f"{rid}: reply contains a web address; make sure it appears in the source")
        mine.append((rid, rec["task_id"], norm(msgs[0]["content"]), len(msgs), scen, new))

    # Near-duplicate opening messages.
    for i, (rid, task, text, nmsg, scen, new) in enumerate(mine):
        soft = errors if new else warnings
        for eid, etext in eval_prompts:
            if similar(text, etext) >= 0.7:
                errors.append(f"{rid}: opening is too similar to an evaluation prompt ({eid})")
        pool = [(o[0], o[1], o[2], o[3], None) for o in others] + [(x[0], x[1], x[2], x[3], x[4]) for x in mine[:i]]
        for oid, otask, otext, on, oscen in pool:
            s = similar(text, otext)
            if otask == task:
                by_design = (scen == "followup" or oscen == "followup") if new else (nmsg >= 4 or on >= 4)
                if s >= 0.8 and not by_design:
                    soft.append(f"{rid}: opening is too similar to {oid} in the same task ({s:.2f}); make it clearly different")
            elif s >= 0.85:
                soft.append(f"{rid}: opening is nearly the same as {oid} from another task ({s:.2f})")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    batch = sys.argv[1]
    errors, warnings = [], []
    tasks = load_spec(batch)
    records, meta = build_records(batch, tasks, errors)
    if records:
        check(batch, records, meta, errors, warnings)
    out = V2 / "cand"
    out.mkdir(parents=True, exist_ok=True)
    with open(out / f"{batch}.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    json.dump(meta, open(out / f"{batch}.meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{batch}: {len(tasks)} tasks, {len(records)} examples -> data/v2/cand/{batch}.jsonl")
    if records:
        sizes = sorted(sum(len(x["content"]) for x in r["messages"]) for r in records)
        print(f"  conversation length in characters: median {sizes[len(sizes) // 2]}, longest {sizes[-1]} (cap {MAX_CHARS})")
        per_task = {}
        for r in records:
            per_task[r["task_id"]] = per_task.get(r["task_id"], 0) + 1
        print("  examples per task: " + ", ".join(f"{k}:{v}" for k, v in sorted(per_task.items())))
    for w in warnings:
        print("  warning:", w)
    if errors:
        print(f"\n{len(errors)} ERROR(S) to fix:")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
