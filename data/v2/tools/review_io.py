#!/usr/bin/env python3
"""Prepare reviewer inputs and revision work lists.

    python3 data/v2/tools/review_io.py render <batch> [round]
        Writes data/v2/reviews/input/<batch>.r<round>.md : the examples a reviewer must
        check in that round (all of them in round 1; only the revised ones later).
        Generator notes are NOT included, so the reviewer stays independent.

    python3 data/v2/tools/review_io.py todo <batch> <round_just_finished>
        Reads the latest decisions and writes, for the examples marked 'revise':
          data/v2/reviews/input/<batch>.revise<round>.md   (what to fix, for the reviser)
          data/v2/reviews/<batch>.r<round+1>.todo.json     (ids due for re-review)
        Also saves a snapshot of the batch before revision in data/v2/snapshots/.
        Examples a person already reviewed (reviewed: true) are never auto-revised.

    python3 data/v2/tools/review_io.py status
        Decision counts for every batch, using the latest round per example.
"""
import json
import shutil
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"


def load_cand(batch):
    recs = [json.loads(line) for line in open(V2 / "cand" / f"{batch}.jsonl", encoding="utf-8") if line.strip()]
    meta = json.load(open(V2 / "cand" / f"{batch}.meta.json", encoding="utf-8"))
    return recs, meta


def latest_reviews(batch):
    """id -> latest review record (highest round)."""
    out = {}
    for path in sorted((V2 / "reviews").glob(f"{batch}.r*.jsonl"), key=lambda p: int(p.stem.split(".r")[-1])):
        for line in open(path, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                out[r["id"]] = r
    return out


def show(rec, m):
    lines = [f"## {rec['id']}",
             f"- scenario: {m['scenario']} | style: {rec['style']} | specification: {rec['specification']} | platform: {rec['platform']}",
             f"- task: {m['task']} ({m['task_platform']}) | sensitive: {rec['sensitive']} | reviewed by a person: {rec['reviewed']}",
             "- sources: " + " ; ".join(s["url"] for s in rec["sources"]), ""]
    for msg in rec["messages"]:
        lines += [f"**{msg['role'].upper()}:**", msg["content"], ""]
    return lines


def render(batch, rnd):
    recs, meta = load_cand(batch)
    todo = V2 / "reviews" / f"{batch}.r{rnd}.todo.json"
    if todo.exists():
        ids = set(json.load(open(todo, encoding="utf-8")))
        recs = [r for r in recs if r["id"] in ids]
    out = [f"# Review input: batch {batch}, round {rnd} ({len(recs)} examples)", ""]
    for rec in recs:
        out += show(rec, meta[rec["id"]])
    path = V2 / "reviews" / "input" / f"{batch}.r{rnd}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"{path.relative_to(REPO)}: {len(recs)} examples")


def todo(batch, rnd):
    recs, meta = load_cand(batch)
    by_id = {r["id"]: r for r in recs}
    reviews = latest_reviews(batch)
    due = [rid for rid, r in reviews.items()
           if r["decision"] == "revise" and r["round"] == rnd and rid in by_id and not by_id[rid]["reviewed"]]
    snap = V2 / "snapshots" / f"{batch}.before_revise{rnd}.jsonl"
    snap.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(V2 / "cand" / f"{batch}.jsonl", snap)
    out = [f"# Revision list: batch {batch}, after review round {rnd} ({len(due)} examples)", "",
           f"Edit ONLY these examples in data/v2/specs/{batch}.py, then rebuild.", ""]
    for rid in due:
        r = reviews[rid]
        out += [f"## {rid}", f"- reasons: {r['reasons']}", f"- fix requested: {r['fix']}"]
        if r["unsupported_claims"]:
            out.append("- unsupported claims: " + " | ".join(r["unsupported_claims"]))
        missing = [a for a, c in zip(r["required_actions"], r["covered"]) if not c]
        if missing:
            out.append("- required actions missing from the reply: " + " | ".join(missing))
        low = {k: v for k, v in r["scores"].items() if v not in (2, "NA")}
        bad = {k: v for k, v in r["gates"].items() if v != "pass"}
        out += [f"- low scores: {low} | gates not passed: {bad}",
                "- sources: " + " ; ".join(s["url"] for s in by_id[rid]["sources"]), ""]
    (V2 / "reviews" / "input").mkdir(parents=True, exist_ok=True)
    (V2 / "reviews" / "input" / f"{batch}.revise{rnd}.md").write_text("\n".join(out), encoding="utf-8")
    json.dump(due, open(V2 / "reviews" / f"{batch}.r{rnd + 1}.todo.json", "w", encoding="utf-8"))
    print(f"{batch}: {len(due)} to revise after round {rnd}")


def status():
    total = Counter()
    for path in sorted((V2 / "cand").glob("*.jsonl")):
        batch = path.stem
        recs, _ = load_cand(batch)
        reviews = latest_reviews(batch)
        c = Counter(reviews[r["id"]]["decision"] if r["id"] in reviews else "unreviewed" for r in recs)
        rounds = max([r["round"] for r in reviews.values()], default=0)
        total.update(c)
        print(f"{batch:6s} n={len(recs):3d} round={rounds} {dict(c)}")
    print("TOTAL", sum(total.values()), dict(total))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "render":
        render(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    elif cmd == "todo":
        todo(sys.argv[2], int(sys.argv[3]))
    elif cmd == "status":
        status()
    else:
        sys.exit(__doc__)
