#!/usr/bin/env python3
"""Compare v7 with v6 (and plain RAG) after v7 has been judged with the frozen rubric v2.

    python eval/v7/compare_v7.py --v7-judge-out eval/judge_out_v7

Reads the first judge run (eval/judge_out/) for v6 and SFT v2 + RAG, and the separate v7
judge run. All conditions are computed the same way here:
- dimension means exclude NA;
- "overall" = mean of a response's non-NA dimension scores, averaged over the judge runs,
  then over scenarios (this differs slightly from the summary's "Overall" for the SFT
  conditions, so compare conditions within this table only);
- key-action coverage = share of the scenario's key actions not listed as missing.
Exploratory: 15 development scenarios, which v6 and v7 were both tuned on.
"""
import argparse
import csv
import json
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
DIMS = ("clarity", "actionability", "completeness", "correctness")


def load(judge_dir):
    key = {r["blind_id"]: r for r in csv.DictReader(open(Path(judge_dir) / "key_condition_DO_NOT_SHOW_JUDGE.csv", encoding="utf-8-sig"))}
    out = defaultdict(list)  # (condition, scenario) -> list of parsed judgments
    for line in open(Path(judge_dir) / "judge_raw.jsonl", encoding="utf-8"):
        r = json.loads(line)
        k = key[r["blind_id"]]
        if r.get("parsed"):
            out[(k["condition"], k["scenario_id"])].append(r["parsed"])
    return out


def num(x):
    return x if isinstance(x, (int, float)) else None


def summarize(judg, cond, prep):
    sids = sorted({s for c, s in judg if c == cond})
    dim = {d: [] for d in DIMS}
    overall, cover, a1, a2, invented, clar = {}, {}, [], [], 0, defaultdict(int)
    for s in sids:
        js = judg[(cond, s)]
        per_run = []
        for p in js:
            sc = p.get("scores") or {}
            vals = [num(sc.get(d)) for d in DIMS]
            for d, v in zip(DIMS, vals):
                if v is not None:
                    dim[d].append(v)
            if any(v is not None for v in vals):
                per_run.append(st.mean(v for v in vals if v is not None))
            ac = p.get("actionability_checks") or {}
            a1.append(ac.get("A1") is False)
            a2.append(ac.get("A2") is False)
            clar[p.get("clarification_behavior", "")] += 1
        overall[s] = st.mean(per_run) if per_run else None
        nk = len(prep[s]["key_actions"])
        cover[s] = st.mean(1 - len({str(x).split(":")[0].strip() for x in (p.get("missing_key_actions") or [])}) / nk for p in js)
        invented += any((p.get("invented_content") or {}).get("present") for p in js)
    return {"n": len(sids), **{d: st.mean(v) if v else float("nan") for d, v in dim.items()},
            "overall": overall, "coverage": cover, "A1_fail": sum(a1) / len(a1), "A2_fail": sum(a2) / len(a2),
            "invented": invented, "clarification": dict(clar)}


def paired(a, b, seed=42, reps=5000):
    ids = sorted(set(a) & set(b))
    d = [b[i] - a[i] for i in ids if a[i] is not None and b[i] is not None]
    rng = random.Random(seed)
    boots = sorted(st.mean(rng.choice(d) for _ in d) for _ in range(reps))
    return st.mean(d), boots[int(0.025 * reps)], boots[int(0.975 * reps)], sum(x > 0 for x in d), sum(x < 0 for x in d), sum(x == 0 for x in d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v7-judge-out", required=True)
    ap.add_argument("--first-judge-out", default=str(EVAL / "judge_out"))
    a = ap.parse_args()
    prep = json.load(open(EVAL / "scenario_prep_v2.json", encoding="utf-8"))
    first, v7 = load(a.first_judge_out), load(a.v7_judge_out)
    res = {"SFT v2 + RAG": summarize(first, "sft_v2_rag", prep), "v6": summarize(first, "sft_v2_rag_v6", prep),
           "v7": summarize(v7, "sft_v2_rag_v7", prep)}
    print("| Condition | Clarity | Actionability | Completeness | Correctness | Overall | Key actions covered | A1 fails | A2 fails | Invented (of 15) |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for name, r in res.items():
        ov = st.mean(v for v in r["overall"].values() if v is not None)
        print(f"| {name} | {r['clarity']:.2f} | {r['actionability']:.2f} | {r['completeness']:.2f} | {r['correctness']:.2f} | "
              f"{ov:.2f} | {st.mean(r['coverage'].values()):.0%} | {r['A1_fail']:.0%} | {r['A2_fail']:.0%} | {r['invented']} |")
    print("\nPaired by scenario (v7 minus other): mean, 95% bootstrap interval, better / worse / tie")
    for other in ("v6", "SFT v2 + RAG"):
        for metric in ("overall", "coverage"):
            m, lo, hi, w, l, t = paired(res[other][metric], res["v7"][metric])
            print(f"- v7 - {other}, {metric}: {m:+.2f} [{lo:+.2f}, {hi:+.2f}], {w} / {l} / {t}")
    print("\nClarification behavior (judgments):", {k: r["clarification"] for k, r in res.items()})


if __name__ == "__main__":
    main()
