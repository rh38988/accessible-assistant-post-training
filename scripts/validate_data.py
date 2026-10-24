"""Check training examples or eval scenarios against the project schema.

Usage:
    python scripts/validate_data.py --kind train data/pilot/*.jsonl
    python scripts/validate_data.py --kind scenario eval/scenarios/*.jsonl

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
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Fields every record needs, for each kind of file.
REQUIRED = {
    "train": ["id", "messages", "specification", "category", "platform",
              "language", "sensitive", "sources", "author", "reviewed"],
    "scenario": ["id", "turns", "specification", "category", "platform",
                 "language", "sensitive"],
}


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
    if msgs[-1].get("role") != must_end_with:
        errors.append(f"{where}: last message must be '{must_end_with}'")


def check_record(rec, kind, errors, where):
    missing = [f for f in REQUIRED[kind] if f not in rec]
    if missing:
        errors.append(f"{where}: missing fields {missing}")
        return

    if rec["specification"] not in SPECIFICATIONS:
        errors.append(f"{where}: specification must be one of {sorted(SPECIFICATIONS)}")
    if rec["category"] not in CATEGORIES:
        errors.append(f"{where}: category must be one of {sorted(CATEGORIES)}")
    if rec["language"] not in LANGUAGES:
        errors.append(f"{where}: language must be one of {sorted(LANGUAGES)}")
    if not isinstance(rec["sensitive"], bool):
        errors.append(f"{where}: sensitive must be true or false")

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
    else:
        # Scenarios end with the user turn the model must answer.
        check_conversation(rec["turns"], "user", errors, where)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=["train", "scenario"], required=True)
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    errors, seen_ids = [], set()
    spec_counts, cat_counts, lang_counts = Counter(), Counter(), Counter()
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
                rid = rec.get("id")
                if rid in seen_ids:
                    errors.append(f"{where}: duplicate id '{rid}'")
                seen_ids.add(rid)
                check_record(rec, args.kind, errors, where)
                spec_counts[rec.get("specification")] += 1
                cat_counts[rec.get("category")] += 1
                lang_counts[rec.get("language")] += 1
                n_sensitive += rec.get("sensitive") is True
                n_unreviewed += args.kind == "train" and rec.get("reviewed") is False

    # Summary helps the team keep the training and eval mixes aligned.
    print(f"Records: {total}")
    if total:
        under = spec_counts["underspecified"]
        print(f"Underspecified: {under} ({under / total:.0%})  target is about 40%")
        print(f"Categories: {dict(cat_counts)}")
        print(f"Languages: {dict(lang_counts)}")
        print(f"Sensitive: {n_sensitive}")
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
