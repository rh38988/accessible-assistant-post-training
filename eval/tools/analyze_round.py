#!/usr/bin/env python3
"""Analyze one judge run (run_llm_judge.py output folder).

Produces, per condition: mean of each dimension (two runs averaged, NA excluded, n listed),
overall score, key-action coverage, flag counts; paired differences with a bootstrap 95%
interval; judge run-to-run agreement. Writes a markdown report and a per-response CSV.

Example (round 1, 13 English scenarios):
  python analyze_round.py --judge-out ..\\judge_out_v4 --prep ..\\scenario_prep_v2.json \\
      --exclude EVAL-COMM-005,EVAL-SAFE-004 \\
      --pairs original:sft_v2,prompt:sft_v2,original:sft_v2_rag,sft_v2:sft_v2_rag,sft_v2_rag:sft_v2_rag_v6,original:sft_v2_rag_v6 \\
      --out-md ..\\analysis.md --out-csv ..\\analysis_per_response.csv

Pairs are written baseline:candidate (difference = candidate - baseline). Fix the list of
pairs BEFORE looking at results (see decision_v4_rule.md).
"""
import argparse, csv, json, re
from collections import Counter
import numpy as np

DIMS = ["clarity", "actionability", "completeness", "correctness"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge-out", required=True)
    ap.add_argument("--prep", required=True)
    ap.add_argument("--exclude", default="", help="comma-separated scenario ids to leave out")
    ap.add_argument("--pairs", default="", help="baseline:candidate,baseline:candidate,...")
    ap.add_argument("--order", default="", help="comma-separated condition order for the tables")
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--out-csv", required=True)
    ap.add_argument("--boot", type=int, default=2000)
    a = ap.parse_args()

    prep = json.load(open(a.prep, encoding="utf-8"))
    drop = {x for x in a.exclude.split(",") if x}
    key = {r["blind_id"]: r for r in csv.DictReader(open(f"{a.judge_out}/key_condition_DO_NOT_SHOW_JUDGE.csv", encoding="utf-8-sig"))}

    rows = []  # one per response-run
    failed = 0
    for l in open(f"{a.judge_out}/judge_raw.jsonl", encoding="utf-8"):
        r = json.loads(l)
        p = r.get("parsed")
        if not p:
            failed += 1
            continue
        k = key[r["blind_id"]]
        if k["scenario_id"] in drop:
            continue
        nk = len(prep[k["scenario_id"]]["key_actions"])
        miss = {m for m in re.findall(r"K\d+", json.dumps(p.get("missing_key_actions", []))) if int(m[1:]) <= nk}
        sc = p["scores"]
        rows.append({
            "blind_id": r["blind_id"], "run": r["run"], "scenario_id": k["scenario_id"], "condition": k["condition"],
            **{d: (None if sc[d] == "NA" else float(sc[d])) for d in DIMS},
            "n_key": nk, "n_missing": len(miss),
            "coverage": None if sc["completeness"] == "NA" else 1 - len(miss) / nk,
            "constraint_violated": bool((p.get("constraint_violation") or {}).get("violated")),
            "invented": bool((p.get("invented_content") or {}).get("present")),
            "unsafe": p.get("unsafe_advice"),
            "clarification": p.get("clarification_behavior"),
            "unverified": len(p.get("unverified_claims") or []),
        })
    conds = [c for c in a.order.split(",") if c] or sorted({r["condition"] for r in rows})
    sids = sorted({r["scenario_id"] for r in rows})

    with open(a.out_csv, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    def scen_mean(c, d):
        out = {}
        for s in sids:
            v = [r[d] for r in rows if r["condition"] == c and r["scenario_id"] == s and r[d] is not None]
            if v: out[s] = float(np.mean(v))
        return out

    md = [f"# Judge analysis: {a.judge_out}", "",
          f"Responses scored: {len({(r['condition'], r['scenario_id']) for r in rows})} "
          f"({len(sids)} scenarios x {len(conds)} conditions), runs per response: {len({r['run'] for r in rows})}. "
          f"Failed or unparsed judge calls: {failed}. Excluded scenarios: {sorted(drop) or 'none'}.", "",
          "## Means (runs averaged per scenario, NA excluded)", "",
          "| Condition | Clarity | Actionability | Completeness | Correctness | Overall | Key-action coverage |", "|---|---|---|---|---|---|---|"]
    per_over = {}
    for c in conds:
        cells, parts = [], {}
        for d in DIMS:
            m = scen_mean(c, d); parts[d] = m
            cells.append(f"{np.mean(list(m.values())):.2f} (n={len(m)})" if m else "n/a")
        per_over[c] = {s: float(np.mean([parts[d][s] for d in DIMS if s in parts[d]])) for s in sids if any(s in parts[d] for d in DIMS)}
        cov = scen_mean(c, "coverage")
        md.append(f"| {c} | " + " | ".join(cells) + f" | {np.mean(list(per_over[c].values())):.2f} | "
                  + (f"{100*np.mean(list(cov.values())):.0f}%" if cov else "n/a") + " |")

    if a.pairs:
        md += ["", "## Paired differences (candidate - baseline; per-scenario overall score; bootstrap 95% interval)", "",
               "| Baseline | Candidate | Mean difference | 95% interval | Better / worse / tie | Clear? |", "|---|---|---|---|---|---|"]
        for pair in a.pairs.split(","):
            b, c = pair.split(":")
            ids = sorted(set(per_over[b]) & set(per_over[c]))
            df = np.array([per_over[c][s] - per_over[b][s] for s in ids])
            bs = [np.random.default_rng(i).choice(df, len(df)).mean() for i in range(a.boot)]
            lo, hi = np.percentile(bs, 2.5), np.percentile(bs, 97.5)
            clear = "yes" if (lo > 0 or hi < 0) else "no (interval contains 0)"
            md.append(f"| {b} | {c} | {df.mean():+.2f} | [{lo:.2f}, {hi:.2f}] | {int((df>0).sum())} / {int((df<0).sum())} / {int((df==0).sum())} | {clear} |")

    md += ["", "## Flags (counts over response-runs)", "",
           "| Condition | Constraint violated | Invented content | Unsafe advice (yes) | Clarification: appropriate / guessed / over-asked | Unverified claims (total) |", "|---|---|---|---|---|---|"]
    for c in conds:
        rs = [r for r in rows if r["condition"] == c]
        cl = Counter(r["clarification"] for r in rs)
        md.append(f"| {c} | {sum(r['constraint_violated'] for r in rs)} | {sum(r['invented'] for r in rs)} | "
                  f"{sum(1 for r in rs if r['unsafe'] == 'yes')} | {cl.get('appropriate',0)} / {cl.get('guessed',0)} / {cl.get('over-asked',0)} | {sum(r['unverified'] for r in rs)} |")

    md += ["", "## Judge run-to-run agreement (exact match, pairs where both runs gave a number)", ""]
    by = {}
    for r in rows:
        by.setdefault((r["condition"], r["scenario_id"]), {})[r["run"]] = r
    for d in DIMS:
        pr = [(v[1][d], v[2][d]) for v in by.values() if 1 in v and 2 in v and v[1][d] is not None and v[2][d] is not None]
        if pr: md.append(f"- {d}: {sum(x == y for x, y in pr)} / {len(pr)} ({100*sum(x == y for x, y in pr)/len(pr):.0f}%)")
    md += ["", "Differences between conditions are exploratory when the number of scenarios is small. "
           "Judge reruns of a whole batch can move a condition mean by about 0.3, so smaller differences should not be interpreted."]
    open(a.out_md, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
