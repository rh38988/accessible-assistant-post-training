"""Build a blinded, shuffled rating sheet from model outputs.

Owner: Evaluation Lead

Reads every eval/outputs/*.jsonl file, gives each response a random item id,
shuffles them, and writes two files:

    eval/ratings/rating_sheet.csv   -> give a copy to each rater
    eval/ratings/key.csv            -> item_id to condition; DO NOT share with raters
                                       (git-ignored; keep a private backup)

Raters see the conversation and the response, never the condition.

Example:
    python eval/make_rating_sheet.py --scenarios eval/scenarios/sample.jsonl
"""
import argparse
import csv
import json
import random
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Rating columns raters fill in. 1 = pass/yes, 0 = fail/no, NA = not applicable.
CORE = ["clarity", "actionability", "completeness", "correctness"]
EXTRA = ["asked_clarification", "chunking", "expectation_setting", "failure_recovery"]


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def format_conversation(turns):
    return "\n\n".join(f"{t['role'].upper()}: {t['content']}" for t in turns)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scenarios", required=True)
    p.add_argument("--outputs", default=str(REPO / "eval/outputs"))
    p.add_argument("--ratings-dir", default=str(REPO / "eval/ratings"))
    p.add_argument("--seed", type=int, default=2026)
    args = p.parse_args()

    scenarios = {s["id"]: s for s in load_jsonl(args.scenarios)}
    items = []
    for path in sorted(Path(args.outputs).glob("*.jsonl")):
        for row in load_jsonl(path):
            items.append(row)
    if not items:
        raise SystemExit(f"No outputs found in {args.outputs}")

    rng = random.Random(args.seed)
    rng.shuffle(items)  # random order so raters can't infer the condition from position

    out_dir = Path(args.ratings_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    sheet_path, key_path = out_dir / "rating_sheet.csv", out_dir / "key.csv"

    with open(sheet_path, "w", newline="", encoding="utf-8") as sf, \
         open(key_path, "w", newline="", encoding="utf-8") as kf:
        sheet = csv.writer(sf)
        key = csv.writer(kf)
        sheet.writerow(["item_id", "conversation", "response", "notes_for_raters"] + CORE + EXTRA + ["comment"])
        key.writerow(["item_id", "scenario_id", "condition"])
        for n, row in enumerate(items, start=1):
            item_id = f"item-{n:04d}"
            sc = scenarios[row["scenario_id"]]
            sheet.writerow([
                item_id,
                format_conversation(sc["turns"]),
                row["response"],
                sc.get("notes_for_raters", ""),
            ] + [""] * (len(CORE) + len(EXTRA) + 1))
            key.writerow([item_id, row["scenario_id"], row["condition"]])

    print(f"{len(items)} items")
    print(f"Rating sheet: {sheet_path}  (copy to ratings_<rater>.csv for each rater)")
    print(f"Key (keep private): {key_path}")


if __name__ == "__main__":
    main()
