"""Check training examples or eval scenarios against the project schema.

Usage:
    python scripts/validate_data.py --kind train data/pilot/*.jsonl
    python scripts/validate_data.py --kind scenario eval/scenarios/eval_v1.jsonl

Exits with code 1 if any file has errors, so it can be used before commits.
Standard library only, so it runs anywhere (laptop, TACC login node).
"""
import argparse
import json
import re
import sys
from collections import Counter

SPECIFICATIONS = {"underspecified", "fully_specified"}
CATEGORIES = {"communication", "online_services", "technical_support"}
LANGUAGES = {"en", "zh-TW"}
# Optional provenance fields (see data/README.md).
INSPIRED_BY = {"OATS", "ElderBench", "GrandGuard", "original"}
STYLES = {"plain", "verbose", "over_specified", "under_specified", "incomplete", "failure_recovery"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Fields every record needs, for each kind of file.
REQUIRED = {
    "train": ["id", "messages", "specification", "category", "platform",
              "language", "sensitive", "sources", "author", "reviewed"],
    "scenario": ["id", "split", "task_family", "task", "platform", "device",
                 "scenario_type", "source_url", "access_date", "risk_level",
                 "prompt", "clarification_required", "expected_elements"],
}
TASK_FAMILIES = {"Smartphone Basics", "Communication", "Online Safety and Scam Prevention"}


def check_conversation(msgs, must_end_with, errors, where):
    """Roles must alternate user/assistant, start with user, end as required."""
    if not isinstance(msgs, list) or not msgs:
        errors.append(f"{where}: conversation must be a non-empty list")
        return
    for i, m in enumerate(msgs):
        expected = "user" if i % 2 == 0 else "assistant"
        if not isinstance(m, dict) or set(m) != {"role", "content"}:
            errors.append(f"{where}: message {i} must have exactly 'role' and 'content'")
            continue
        if m["role"] != expected:
            errors.append(f"{where}: message {i} role is '{m['role']}', expected '{expected}'")
        if not isinstance(m["content"], str) or not m["content"].strip():
            errors.append(f"{where}: message {i} has empty content")
    if not isinstance(msgs[-1], dict) or msgs[-1].get("role") != must_end_with:
        errors.append(f"{where}: last message must be '{must_end_with}'")


def check_schema_v1(rec, errors, where):
    """Validate evaluation fields directly; never map them to training fields."""
    unexpected = sorted(set(rec) - set(REQUIRED["scenario"]))
    if unexpected:
        errors.append(f"{where}: unexpected schema_v1 fields {unexpected}")
    if rec["split"] != "evaluation":
        errors.append(f"{where}: split must be 'evaluation'")
    if not isinstance(rec["task_family"], str) or rec["task_family"] not in TASK_FAMILIES:
        errors.append(f"{where}: invalid task_family")
    for field in ("task", "platform", "device", "scenario_type"):
        if not isinstance(rec[field], str) or not rec[field].strip():
            errors.append(f"{where}: {field} must be a non-empty string")
    url = rec["source_url"]
    if (not isinstance(url, str) or not re.fullmatch(r"https://[^\s]+", url)
            or re.search(r"example\.com|\.\.\.|TODO|placeholder|xxx", url, re.I)):
        errors.append(f"{where}: source_url must be an HTTPS URL without placeholders")
    if not DATE_RE.fullmatch(str(rec["access_date"])):
        errors.append(f"{where}: access_date must be YYYY-MM-DD")
    if rec["risk_level"] not in ("low", "medium", "high"):
        errors.append(f"{where}: risk_level must be low, medium, or high")
    if not isinstance(rec["clarification_required"], bool):
        errors.append(f"{where}: clarification_required must be true or false")
    elements = rec["expected_elements"]
    if (not isinstance(elements, list) or not 3 <= len(elements) <= 6
            or not all(isinstance(e, str) and e.strip() for e in elements)):
        errors.append(f"{where}: expected_elements must contain 3-6 non-empty strings")
    check_conversation(rec["prompt"], "user", errors, where)


def check_record(rec, kind, errors, where):
    if not isinstance(rec, dict):
        errors.append(f"{where}: record must be a JSON object")
        return
    missing = [f for f in REQUIRED[kind] if f not in rec]
    if missing:
        errors.append(f"{where}: missing fields {missing}")
        return
    if not isinstance(rec["id"], str) or not rec["id"].strip():
        errors.append(f"{where}: id must be a non-empty string")
    if kind == "scenario":
        check_schema_v1(rec, errors, where)
        return

    if rec["specification"] not in SPECIFICATIONS:
        errors.append(f"{where}: specification must be one of {sorted(SPECIFICATIONS)}")
    if rec["category"] not in CATEGORIES:
        errors.append(f"{where}: category must be one of {sorted(CATEGORIES)}")
    if rec["language"] not in LANGUAGES:
        errors.append(f"{where}: language must be one of {sorted(LANGUAGES)}")
    if not isinstance(rec["sensitive"], bool):
        errors.append(f"{where}: sensitive must be true or false")
    if "inspired_by" in rec and rec["inspired_by"] not in INSPIRED_BY:
        errors.append(f"{where}: inspired_by must be one of {sorted(INSPIRED_BY)}")
    if "style" in rec and rec["style"] not in STYLES:
        errors.append(f"{where}: style must be one of {sorted(STYLES)}")

    if kind == "train":
        # Training examples end with the assistant reply we want to teach.
        check_conversation(rec["messages"], "assistant", errors, where)
        if not isinstance(rec["reviewed"], bool):
            errors.append(f"{where}: reviewed must be true or false")
        sources = rec["sources"]
        if not isinstance(sources, list) or not sources:
            errors.append(f"{where}: at least one source is required")
        else:
            for j, s in enumerate(sources):
                if not all(k in s for k in ("title", "url", "accessed")):
                    errors.append(f"{where}: source {j} needs title, url, accessed")
                elif not DATE_RE.match(str(s["accessed"])):
                    errors.append(f"{where}: source {j} accessed date must be YYYY-MM-DD")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=["train", "scenario"], required=True)
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    errors, seen_ids = [], set()
    spec_counts, cat_counts, lang_counts, insp_counts = Counter(), Counter(), Counter(), Counter()
    family_counts, risk_counts = Counter(), Counter()
    n_clarification = n_multiturn = 0
    n_sensitive = n_unreviewed = total = 0

    for path in args.files:
        with open(path, encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                if not line.strip():
                    continue
                where = f"{path}:{line_no}"
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError as e:
                    errors.append(f"{where}: invalid JSON ({e})")
                    continue
                total += 1
                check_record(rec, args.kind, errors, where)
                if not isinstance(rec, dict):
                    continue
                rid = rec.get("id")
                if isinstance(rid, str):
                    if rid in seen_ids:
                        errors.append(f"{where}: duplicate id '{rid}'")
                    seen_ids.add(rid)
                if args.kind == "scenario":
                    for field, counts in (("task_family", family_counts), ("risk_level", risk_counts)):
                        value = rec.get(field)
                        counts[value if isinstance(value, str) else "<invalid>"] += 1
                    n_clarification += rec.get("clarification_required") is True
                    n_multiturn += isinstance(rec.get("prompt"), list) and len(rec["prompt"]) > 1
                    continue
                spec_counts[rec.get("specification")] += 1
                cat_counts[rec.get("category")] += 1
                lang_counts[rec.get("language")] += 1
                if "inspired_by" in rec:
                    insp_counts[rec["inspired_by"]] += 1
                n_sensitive += rec.get("sensitive") is True
                n_unreviewed += args.kind == "train" and rec.get("reviewed") is False

    # Summary helps the team keep the training and eval mixes aligned.
    print(f"Records: {total}")
    if total and args.kind == "scenario":
        print(f"Task families: {dict(family_counts)}")
        print(f"Risk levels: {dict(risk_counts)}")
        print(f"Clarification required: {n_clarification}")
        print(f"Multi-turn: {n_multiturn}")
    elif total:
        under = spec_counts["underspecified"]
        print(f"Underspecified: {under} ({under / total:.0%})  target is about 40%")
        print(f"Categories: {dict(cat_counts)}")
        print(f"Languages: {dict(lang_counts)}")
        print(f"Sensitive: {n_sensitive}")
        if insp_counts:
            print(f"Inspired by: {dict(insp_counts)}")
        if args.kind == "train":
            print(f"Not yet reviewed: {n_unreviewed}")

    if errors:
        print(f"\n{len(errors)} error(s):")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("\nOK: no errors")


if __name__ == "__main__":
    main()
