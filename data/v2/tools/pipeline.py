#!/usr/bin/env python3
"""Show where every batch stands and what to launch next (idempotent).

    python3 data/v2/tools/pipeline.py            # prepare inputs, print pending actions, mark them launched
    python3 data/v2/tools/pipeline.py --dry      # print only
    python3 data/v2/tools/pipeline.py --reset    # forget 'launched' marks for unfinished stages (after an interruption)

Stages per batch: WRITE -> REVIEW 1 -> REVISE 1 -> REVIEW 2 -> REVISE 2 -> REVIEW 3 -> DONE
"""
import json, subprocess, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"
MARK = V2 / "reviews" / ".launched"
MAX_ROUND = 3
sys.path.insert(0, str(V2 / "tools"))
import review_io  # noqa: E402


def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], cwd=REPO, capture_output=True, text=True)


def main():
    dry, reset = "--dry" in sys.argv, "--reset" in sys.argv
    MARK.mkdir(parents=True, exist_ok=True)
    batches = sorted({p.stem for p in (V2 / "assignments").glob("*.md")} | {p.stem for p in (V2 / "specs").glob("*.py")})
    actions, done, totals = [], 0, Counter()
    for b in batches:
        has_assign = (V2 / "assignments" / f"{b}.md").exists()
        gen_done = (V2 / "reports" / f"{b}.gen.md").exists() or not has_assign
        if not gen_done or not (V2 / "specs" / f"{b}.py").exists():
            actions.append(("WRITE", b, 0)); continue
        built = run(V2 / "tools" / "build_v2.py", b)
        if built.returncode != 0:
            actions.append(("WRITE", b, 0)); print(f"  {b}: builder errors, needs the writer again"); continue
        recs, _ = review_io.load_cand(b)
        by_id = {r["id"]: r for r in recs}
        reviews = review_io.latest_reviews(b)
        rounds = sorted(int(p.stem.split(".r")[-1]) for p in (V2 / "reviews").glob(f"{b}.r*.jsonl"))
        n = rounds[-1] if rounds else 0
        totals.update(reviews[i]["decision"] if i in reviews else "unreviewed" for i in by_id)
        if n == 0:
            if not dry: review_io.render(b, 1)
            actions.append(("REVIEW", b, 1)); continue
        due = [i for i, r in reviews.items() if r["decision"] == "revise" and i in by_id and not by_id[i]["reviewed"]]
        if not due or n >= MAX_ROUND:
            done += 1; continue
        if not (V2 / "reports" / f"{b}.revise{n}.md").exists():
            if not dry and not (V2 / "reviews" / f"{b}.r{n + 1}.todo.json").exists(): review_io.todo(b, n)
            actions.append(("REVISE", b, n))
        else:
            if not dry: review_io.render(b, n + 1)
            actions.append(("REVIEW", b, n + 1))
    pending = []
    for kind, b, n in actions:
        m = MARK / f"{b}.{kind}{n}"
        if reset and m.exists(): m.unlink()
        if m.exists():
            print(f"  running: {kind} {b} {n or ''}")
        else:
            pending.append((kind, b, n))
            if not dry and "--no-mark" not in sys.argv: m.write_text("launched")
    print(f"batches: {len(batches)} | done: {done} | decisions so far: {dict(totals)}")
    for kind, b, n in pending:
        size = len(review_io.load_cand(b)[0]) if (V2 / "cand" / f"{b}.jsonl").exists() else 0
        print(f"LAUNCH {kind} {b} {n or ''} ({size} examples)")
    if not actions: print("ALL DONE: run assemble.py")


if __name__ == "__main__":
    main()
