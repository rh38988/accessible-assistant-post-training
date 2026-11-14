#!/usr/bin/env python3
"""Validate one reviewer file and save it as JSON Lines.

    python3 data/v2/tools/check_review.py <batch> <round>

Reads   data/v2/reviews/<batch>.r<round>.py    (defines REVIEWS, see REVIEWER_INSTRUCTIONS_v1.md)
Writes  data/v2/reviews/<batch>.r<round>.jsonl

Round 1 must cover every example in data/v2/cand/<batch>.jsonl. Later rounds
must cover the ids listed in data/v2/reviews/<batch>.r<round>.todo.json.
Exit code 1 on errors. Standard library only.
"""
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
V2 = REPO / "data" / "v2"
SCORES = ("steps", "ask_or_answer", "constraints", "actionable", "plain", "realistic_user")
GATES = ("source", "safety", "duplicate")


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    batch, rnd = sys.argv[1], int(sys.argv[2])
    path = V2 / "reviews" / f"{batch}.r{rnd}.py"
    spec = importlib.util.spec_from_file_location("rev", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    reviews = mod.REVIEWS

    todo = V2 / "reviews" / f"{batch}.r{rnd}.todo.json"
    if todo.exists():
        expected = set(json.load(open(todo, encoding="utf-8")))
    else:
        expected = {json.loads(line)["id"] for line in open(V2 / "cand" / f"{batch}.jsonl", encoding="utf-8") if line.strip()}

    errors, seen = [], set()
    for i, r in enumerate(reviews):
        rid = r.get("id", f"#{i}")
        if rid in seen:
            errors.append(f"{rid}: reviewed twice")
        seen.add(rid)
        if rid not in expected:
            errors.append(f"{rid}: not an example in this batch (or not due this round)")
            continue
        for k in ("required_actions", "covered", "needs_clarification", "gates", "unsupported_claims", "scores",
                  "decision", "reasons", "fix"):
            if k not in r:
                errors.append(f"{rid}: missing field '{k}'")
        if errors and errors[-1].startswith(f"{rid}: missing"):
            continue
        if len(r["required_actions"]) != len(r["covered"]) or not all(isinstance(c, bool) for c in r["covered"]):
            errors.append(f"{rid}: 'covered' must be True/False values, one per required action")
        g, s = r["gates"], r["scores"]
        if set(g) != set(GATES) or any(v not in ("pass", "fail", "unverified") for v in g.values()):
            errors.append(f"{rid}: gates must be {GATES} with values pass/fail (source may be unverified)")
            continue
        if set(s) != set(SCORES) or any(v not in (0, 1, 2, "NA") for v in s.values()):
            errors.append(f"{rid}: scores must be {SCORES} with values 0, 1, 2 or 'NA'")
            continue
        clean = all(v == "pass" for v in g.values()) and all(v in (2, "NA") for v in s.values()) and all(r["covered"])
        d = r["decision"]
        if d not in ("keep", "revise", "reject"):
            errors.append(f"{rid}: decision must be keep, revise, or reject")
        elif d == "keep" and not clean:
            errors.append(f"{rid}: 'keep' needs all gates pass, all scores 2 or NA, and all required actions covered")
        elif d != "keep" and clean:
            errors.append(f"{rid}: decision is '{d}' but nothing is marked wrong; lower the score or gate that explains it")
        if d != "keep" and not str(r["reasons"]).strip():
            errors.append(f"{rid}: reasons are required unless the decision is keep")
        if d == "revise" and not str(r["fix"]).strip():
            errors.append(f"{rid}: a 'fix' instruction is required for revise")
        if g["source"] == "fail" and not r["unsupported_claims"]:
            errors.append(f"{rid}: source gate failed but no unsupported claim is quoted")
    for rid in sorted(expected - seen):
        errors.append(f"{rid}: no review record")

    print(f"{batch} round {rnd}: {len(reviews)} reviews, decisions {dict(Counter(r.get('decision') for r in reviews))}")
    if errors:
        print(f"\n{len(errors)} ERROR(S) to fix:")
        for e in errors[:80]:
            print("  " + e)
        sys.exit(1)
    with open(V2 / "reviews" / f"{batch}.r{rnd}.jsonl", "w", encoding="utf-8") as f:
        for r in reviews:
            f.write(json.dumps({**r, "batch": batch, "round": rnd}, ensure_ascii=False) + "\n")
    print("OK")


if __name__ == "__main__":
    main()
