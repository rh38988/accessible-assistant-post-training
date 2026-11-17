#!/usr/bin/env python3
"""Compare actionability under rubric v2 and v4 (both runs, 13 English scenarios).
Usage: python analyze_actionability_v4.py --v2 ..\\judge_out --v4 ..\\judge_out_v4 --out ..\\actionability_v4_summary.md
Reads judge_raw.jsonl and key_condition_DO_NOT_SHOW_JUDGE.csv from each folder."""
import argparse, csv, json
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("--v2", required=True); ap.add_argument("--v4", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
DROP = {"EVAL-COMM-005", "EVAL-SAFE-004"}
CONS = ["original", "prompt", "sft_v2", "sft_v2_rag", "sft_v2_rag_v6"]

def load(d):
    key = {r["blind_id"]: r for r in csv.DictReader(open(f"{d}/key_condition_DO_NOT_SHOW_JUDGE.csv", encoding="utf-8-sig"))}
    out = {}
    for l in open(f"{d}/judge_raw.jsonl", encoding="utf-8"):
        r = json.loads(l)
        if not r["parsed"]: continue
        k = key[r["blind_id"]]
        if k["scenario_id"] in DROP: continue
        s = r["parsed"]["scores"]["actionability"]
        a2 = r["parsed"].get("actionability_checks", {}).get("A2")
        out[(k["condition"], k["scenario_id"], r["run"])] = (None if s == "NA" else float(s), a2)
    return out

v2, v4 = load(a.v2), load(a.v4)
lines = ["# Actionability under rubric v2 vs v4 (13 English scenarios)", "",
         "v4 changes check A2 only. Judge, model, seed and both runs as in v2. Other dimensions are not re-scored here.", "",
         "| Condition | v2 actionability | v4 actionability | A2 fails v2 | A2 fails v4 |", "|---|---|---|---|---|"]
def mean_by_scen(d, c):
    m = {}
    for (cc, sid, run), (s, _) in d.items():
        if cc == c and s is not None: m.setdefault(sid, []).append(s)
    return {k: np.mean(v) for k, v in m.items()}
def a2fail(d, c):
    v = [x[1] for (cc, _, _), x in d.items() if cc == c and x[1] is not None]
    return f"{100*sum(1 for x in v if x is False)/len(v):.0f}%" if v else "n/a"
for c in CONS:
    m2, m4 = mean_by_scen(v2, c), mean_by_scen(v4, c)
    lines.append(f"| {c} | {np.mean(list(m2.values())):.2f} | {np.mean(list(m4.values())):.2f} | {a2fail(v2, c)} | {a2fail(v4, c)} |")
same = [v2[k][0] == v4[k][0] for k in v2 if k in v4 and v2[k][0] is not None and v4[k][0] is not None]
lines += ["", f"Response-run level: {sum(same)}/{len(same)} actionability scores unchanged between v2 and v4."]
open(a.out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
