"""Expand task specs into 4 training examples each and write data/train/*.jsonl.

Each spec produces:
  a  fully specified, plain:    [user full] -> steps
  b  underspecified:            [user under] -> clarify
  c  OATS-style variant:        [styled] -> (opener + steps) or (styled clarify)
  d  multi-turn:                [user under, clarify, answer] -> (d_open + steps)
"""
import csv
import importlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from sources import SOURCES  # noqa: E402

REPO = Path(sys.argv[1])
CHUNKS = sys.argv[2:]
ACCESSED = "2026-10-24"

tasks = {r["task_id"]: r for r in csv.DictReader(open(REPO / "data/tasks/train_tasks.csv", encoding="utf-8"))}


def u(t):
    return {"role": "user", "content": t}


def a(t):
    return {"role": "assistant", "content": t}


def build(spec):
    t = tasks[spec["id"]]
    lang = t["language"]
    sources = [{"title": SOURCES[k][0], "url": SOURCES[k][1], "accessed": ACCESSED} for k in spec["src"]]
    base = {
        "category": t["category"],
        "language": lang,
        "sensitive": t["sensitive"] == "True",
        "sources": sources,
        "task_id": t["task_id"],
        "author": "claude-draft",
        "reviewed": False,
    }
    plat = t["platform"]
    under_plat = spec.get("under_platform", "unknown")
    steps = spec["steps"].strip()
    n = int(t["task_id"].split("-")[1])
    out = []

    def add(suffix, messages, spec_label, platform, inspired, style):
        out.append({"id": f"tr{n:03d}-{suffix}", "messages": messages, "specification": spec_label,
                    "platform": platform, "inspired_by": inspired, "style": style, **base})

    insp = spec.get("inspired", "original")
    add("a", [u(spec["full"]), a(steps)], "fully_specified", plat, insp, "plain")
    add("b", [u(spec["under"]), a(spec["clarify"])], "underspecified", under_plat, insp, "under_specified")
    if spec["styled_full"]:
        add("c", [u(spec["styled"]), a(spec["styled_open"].strip() + "\n\n" + steps)],
            "fully_specified", plat, "OATS", spec["style"])
    else:
        add("c", [u(spec["styled"]), a(spec["styled_reply"])],
            "underspecified", under_plat, "OATS", spec["style"])
    add("d", [u(spec["under"]), a(spec["clarify"]), u(spec["answer"]), a(spec["d_open"].strip() + "\n\n" + steps)],
        "fully_specified", plat, insp, "under_specified")
    return out


def main():
    out_dir = REPO / "data/train"
    out_dir.mkdir(parents=True, exist_ok=True)
    for chunk in CHUNKS:
        mod = importlib.import_module(chunk)
        rows = [ex for spec in mod.SPECS for ex in build(spec)]
        path = out_dir / f"{chunk}.jsonl"
        with open(path, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{chunk}: {len(mod.SPECS)} tasks -> {len(rows)} examples -> {path.relative_to(REPO)}")


main()
