#!/usr/bin/env python3
"""Export the existing English drafts into v2 spec files (specs/ex1.py ... exN.py).

    python3 data/v2/tools/export_spec.py <number_of_groups>

Original ids, authors, review flags, and sources are preserved, so the v2
pipeline can review and revise the old drafts the same way as new examples.
Chinese drafts are left out of this round.
"""
import csv
import glob
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"


def q(s):
    """Readable Python literal for a string."""
    if '"""' in s or "\\" in s or s.endswith('"') or "\n" not in s:
        return repr(s)
    return '"""' + s + '"""'


def scenario(rec):
    n, spec, style = len(rec["messages"]), rec["specification"], rec["style"]
    if spec == "underspecified":
        return "missing_info"
    if n >= 4:
        return "failure_recovery" if style == "failure_recovery" else "followup"
    return "direct" if style == "plain" else "direct_messy"


def main():
    groups = int(sys.argv[1])
    tasks = {r["task_id"]: r for r in csv.DictReader(open(REPO / "data/tasks/train_tasks.csv", encoding="utf-8"))}
    recs = []
    for f in [REPO / "data/pilot/pilot_v1.jsonl"] + sorted(glob.glob(str(REPO / "data/train/*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                if r["language"] == "en":
                    recs.append(r)
    by_task = {}
    for r in recs:
        by_task.setdefault(r["task_id"], []).append(r)
    ids = sorted(by_task)
    size = -(-len(ids) // groups)
    for g in range(groups):
        chunk = ids[g * size:(g + 1) * size]
        if not chunk:
            continue
        lines = [f'"""Existing English drafts, group {g + 1}. Exported by export_spec.py; ids and provenance preserved."""',
                 "TASKS = ["]
        for tid in chunk:
            t, exs = tasks[tid], by_task[tid]
            src = exs[0]["sources"][0]
            lines += ["    {",
                      f'        "task_id": {tid!r}, "task_type": {t["task_type"]!r}, "task": {t["task"]!r},',
                      f'        "platform": {t["platform"]!r}, "category": {t["category"]!r}, "sensitive": {t["sensitive"] == "True"},',
                      f'        "source": {{"title": {src["title"]!r}, "url": {src["url"]!r}}},',
                      '        "examples": [']
            for r in exs:
                suffix = r["id"].split("-")[-1] if r["id"].startswith("tr") else "p"
                lines += ["            {",
                          f'                "existing": True, "id": {r["id"]!r}, "suffix": {suffix!r}, "scenario": {scenario(r)!r},',
                          f'                "style": {r["style"]!r}, "specification": {r["specification"]!r}, "platform": {r["platform"]!r},',
                          f'                "author": {r["author"]!r}, "reviewed": {r["reviewed"]!r}, "inspired_by": {r.get("inspired_by")!r},',
                          f'                "sources": {r["sources"]!r},',
                          '                "messages": [']
                for m in r["messages"]:
                    lines.append("                    " + q(m["content"]) + ",")
                lines += ["                ],", "            },"]
            lines += ["        ],", "    },"]
        lines.append("]")
        path = V2 / "specs" / f"ex{g + 1}.py"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{path.relative_to(REPO)}: {len(chunk)} tasks, {sum(len(by_task[i]) for i in chunk)} examples")


if __name__ == "__main__":
    main()
