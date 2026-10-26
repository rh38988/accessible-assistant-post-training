"""PROPOSED (not yet approved) adapter: schema_v1 -> the field names the current pipeline reads.

Why: eval/generate.py, eval/make_rating_sheet.py, eval/analyze.py and scripts/validate_data.py read
`turns`, `specification`, `sensitive`, `category`, `language`, `notes_for_raters`. schema_v1 uses
`prompt`, `clarification_required`, `risk_level`, `task_family`, `expected_elements`.

This script NEVER edits eval_v1.jsonl. It writes a derived, throw-away file that the unmodified
scripts can read. eval_v1.jsonl stays the single source of truth.

Usage:
    python eval/tools/schema_v1_adapter.py eval/scenarios/eval_v1.jsonl eval/scenarios/eval_v1.repo_compat.jsonl
Then (unmodified scripts):
    python scripts/validate_data.py --kind scenario eval/scenarios/eval_v1.repo_compat.jsonl
    python eval/generate.py --condition prompt --scenarios eval/scenarios/eval_v1.repo_compat.jsonl --out /dev/null --dry-run

Mapping decisions (need team approval, see eval/schema_compat_note_v1.md):
    prompt                  -> turns
    clarification_required  -> specification  (true = underspecified, false = fully_specified)
    task_family             -> category       (Smartphone Basics -> technical_support,
                                               Communication -> communication,
                                               Online Safety and Scam Prevention -> online_services)
    risk_level              -> sensitive      (low = false, medium/high = true)
    (CJK in any user turn)  -> language       (zh-TW, otherwise en)
    expected_elements       -> notes_for_raters (joined text; rating sheet shows it to raters, never to the model)
    id, platform            -> unchanged
Every other schema_v1 field (split, task, device, scenario_type, source_url, access_date) is dropped from the copy.
"""
import json, re, sys

CATEGORY = {
    "Smartphone Basics": "technical_support",
    "Communication": "communication",
    "Online Safety and Scam Prevention": "online_services",
}
CJK = re.compile(r"[一-鿿]")


def to_repo_format(r):
    user_text = " ".join(m["content"] for m in r["prompt"] if m["role"] == "user")
    return {
        "id": r["id"],
        "turns": r["prompt"],
        "specification": "underspecified" if r["clarification_required"] else "fully_specified",
        "category": CATEGORY[r["task_family"]],
        "platform": r["platform"],
        "language": "zh-TW" if CJK.search(user_text) else "en",
        "sensitive": r["risk_level"] != "low",
        "notes_for_raters": "Expected elements: " + " | ".join(r["expected_elements"]),
    }


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    n = 0
    with open(src, encoding="utf-8") as f, open(dst, "w", encoding="utf-8", newline="\n") as out:
        for line in f:
            if line.strip():
                out.write(json.dumps(to_repo_format(json.loads(line)), ensure_ascii=False) + "\n")
                n += 1
    print(f"converted {n} records -> {dst}")
