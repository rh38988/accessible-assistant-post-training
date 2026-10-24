"""Analyze human ratings: acceptable rate, clarification errors, agreement, McNemar.

Owner: Evaluation Lead

Implements the decision rule in the proposal:
    Primary metric: % of responses "acceptable" = passes all four core criteria.
    Post-training is justified only if a post-trained condition beats the
    strongest prompting baseline by >= 10 percentage points AND the paired
    McNemar test gives p < 0.05.

How two raters are combined into one label per item:
    1. If adjudicated.csv has the item, use that.
    2. Otherwise, if both raters agree, use their answer.
    3. Otherwise the item is UNRESOLVED. Results are then marked PROVISIONAL:
       "acceptable" needs both raters to say yes (conservative), and
       "asked_clarification" counts if either rater said yes.
    Resolve all disagreements by discussion before reporting final numbers.

Standard library only. Example:
    python eval/analyze.py --scenarios eval/scenarios/sample.jsonl \
        --key eval/ratings/key.csv \
        --ratings eval/ratings/ratings_alice.csv eval/ratings/ratings_bob.csv \
        --baseline rag --candidates sft sft_rag
"""
import argparse
import csv
import json
from collections import defaultdict
from math import comb

CORE = ["clarity", "actionability", "completeness", "correctness"]
TARGET = ["chunking", "expectation_setting", "failure_recovery"]
THRESHOLD_PP = 10.0
ALPHA = 0.05


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def to_bit(value, item_id, col):
    v = str(value).strip().upper()
    if v in {"1", "Y", "YES", "TRUE"}:
        return 1
    if v in {"0", "N", "NO", "FALSE"}:
        return 0
    if v in {"NA", "N/A", ""}:
        return None
    raise ValueError(f"{item_id}: '{col}' has value '{value}'; use 1, 0, or NA")


def rater_labels(row):
    """One rater's judgments for one item."""
    iid = row["item_id"]
    core = [to_bit(row[c], iid, c) for c in CORE]
    if None in core:
        raise ValueError(f"{iid}: core criteria must be 1 or 0, not blank or NA")
    return {
        "acceptable": int(all(core)),
        "asked": to_bit(row["asked_clarification"], iid, "asked_clarification"),
        **{t: to_bit(row.get(t, "NA"), iid, t) for t in TARGET},
    }


def cohens_kappa(pairs):
    """Agreement between two raters on a yes/no label, corrected for chance."""
    pairs = [(a, b) for a, b in pairs if a is not None and b is not None]
    n = len(pairs)
    if n == 0:
        return None
    observed = sum(a == b for a, b in pairs) / n
    p_a = sum(a for a, _ in pairs) / n
    p_b = sum(b for _, b in pairs) / n
    expected = p_a * p_b + (1 - p_a) * (1 - p_b)
    return None if expected == 1 else (observed - expected) / (1 - expected)


def mcnemar_exact(b, c):
    """Exact two-sided McNemar test.

    b = scenarios where only the candidate was acceptable,
    c = scenarios where only the baseline was acceptable.
    Scenarios where both agree carry no information about the difference.
    Under "no difference", each discordant scenario is a coin flip.
    """
    n = b + c
    if n == 0:
        return 1.0
    tail = sum(comb(n, k) for k in range(min(b, c) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def pct(x):
    return "n/a" if x is None else f"{100 * x:.1f}%"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scenarios", required=True)
    p.add_argument("--key", required=True)
    p.add_argument("--ratings", nargs=2, required=True, help="Two rater CSVs")
    p.add_argument("--adjudicated", help="CSV with item_id, acceptable, asked_clarification")
    p.add_argument("--baseline", default="rag", help="Strongest prompting baseline")
    p.add_argument("--candidates", nargs="+", default=["sft", "sft_rag"])
    p.add_argument("--out-json", help="Optional path to save the summary")
    args = p.parse_args()

    scenarios = {s["id"]: s for s in load_jsonl(args.scenarios)}
    key = {r["item_id"]: r for r in read_csv(args.key)}
    raters = [{r["item_id"]: rater_labels(r) for r in read_csv(path)} for path in args.ratings]
    adjudicated = {}
    if args.adjudicated:
        for r in read_csv(args.adjudicated):
            adjudicated[r["item_id"]] = {
                "acceptable": to_bit(r["acceptable"], r["item_id"], "acceptable"),
                "asked": to_bit(r["asked_clarification"], r["item_id"], "asked_clarification"),
            }

    # ---- Agreement ----
    shared = sorted(set(raters[0]) & set(raters[1]))
    missing = set(key) - set(shared)
    if missing:
        print(f"WARNING: {len(missing)} items are not rated by both raters; they are skipped.")
    kappa_acc = cohens_kappa([(raters[0][i]["acceptable"], raters[1][i]["acceptable"]) for i in shared])
    kappa_ask = cohens_kappa([(raters[0][i]["asked"], raters[1][i]["asked"]) for i in shared])

    # ---- Final label per item ----
    final, unresolved = {}, []
    for i in shared:
        r1, r2 = raters[0][i], raters[1][i]
        if i in adjudicated:
            final[i] = adjudicated[i]
            continue
        if r1["acceptable"] != r2["acceptable"] or r1["asked"] != r2["asked"]:
            unresolved.append(i)
        final[i] = {
            "acceptable": int(r1["acceptable"] and r2["acceptable"]),
            "asked": int(bool(r1["asked"]) or bool(r2["asked"])),
        }

    # ---- Per-condition metrics ----
    by_cond = defaultdict(list)
    for i, label in final.items():
        sid, cond = key[i]["scenario_id"], key[i]["condition"]
        by_cond[cond].append((sid, i, label))

    summary = {"kappa_acceptable": kappa_acc, "kappa_asked": kappa_ask,
               "unresolved_items": len(unresolved), "conditions": {}, "comparisons": []}

    print("\n## Results by condition\n")
    print("| Condition | n | Acceptable | Guessed when should ask | Asked when unnecessary | Sensitive acceptable |")
    print("|---|---|---|---|---|---|")
    for cond in sorted(by_cond):
        rows = by_cond[cond]
        n = len(rows)
        acc = sum(l["acceptable"] for _, _, l in rows) / n
        under = [l for s, _, l in rows if scenarios[s]["specification"] == "underspecified"]
        full = [l for s, _, l in rows if scenarios[s]["specification"] == "fully_specified"]
        sens = [l for s, _, l in rows if scenarios[s]["sensitive"]]
        guess = sum(1 - l["asked"] for l in under) / len(under) if under else None
        over = sum(l["asked"] for l in full) / len(full) if full else None
        sens_acc = sum(l["acceptable"] for l in sens) / len(sens) if sens else None
        # Target behaviors: average of both raters, ignoring NA.
        target = {}
        for t in TARGET:
            vals = [raters[k][i][t] for _, i, _ in rows for k in (0, 1) if raters[k][i][t] is not None]
            target[t] = sum(vals) / len(vals) if vals else None
        summary["conditions"][cond] = {"n": n, "acceptable": acc, "guess_rate": guess,
                                       "over_clarification_rate": over,
                                       "sensitive_acceptable": sens_acc, **target}
        print(f"| {cond} | {n} | {pct(acc)} | {pct(guess)} | {pct(over)} | {pct(sens_acc)} |")

    print("\n## Target behaviors (share of responses rated yes, NA excluded)\n")
    print("| Condition | " + " | ".join(TARGET) + " |")
    print("|---|" + "---|" * len(TARGET))
    for cond in sorted(by_cond):
        c = summary["conditions"][cond]
        print(f"| {cond} | " + " | ".join(pct(c[t]) for t in TARGET) + " |")

    # ---- Decision rule: paired McNemar vs. baseline ----
    print(f"\n## Decision rule (vs. baseline '{args.baseline}')\n")
    base = {s: l["acceptable"] for s, _, l in by_cond.get(args.baseline, [])}
    if not base:
        print(f"No ratings for baseline '{args.baseline}'.")
    for cand in args.candidates:
        cand_map = {s: l["acceptable"] for s, _, l in by_cond.get(cand, [])}
        paired = sorted(set(base) & set(cand_map))
        if not paired:
            print(f"- {cand}: no paired scenarios")
            continue
        b = sum(cand_map[s] == 1 and base[s] == 0 for s in paired)
        c = sum(cand_map[s] == 0 and base[s] == 1 for s in paired)
        diff = 100 * (b - c) / len(paired)
        pval = mcnemar_exact(b, c)
        passes = diff >= THRESHOLD_PP and pval < ALPHA
        verdict = "MEETS threshold" if passes else "does NOT meet threshold"
        print(f"- {cand} vs {args.baseline}: n={len(paired)}, difference = {diff:+.1f} pp, "
              f"only-{cand} = {b}, only-{args.baseline} = {c}, McNemar p = {pval:.4f} -> {verdict}")
        summary["comparisons"].append({"candidate": cand, "baseline": args.baseline, "n": len(paired),
                                       "diff_pp": diff, "b": b, "c": c, "p": pval, "passes": passes})

    print("\n## Rater agreement\n")
    print(f"- Cohen's kappa, acceptable: {'n/a' if kappa_acc is None else f'{kappa_acc:.2f}'}")
    print(f"- Cohen's kappa, asked clarification: {'n/a' if kappa_ask is None else f'{kappa_ask:.2f}'}")
    if unresolved:
        print(f"\nPROVISIONAL: {len(unresolved)} items have rater disagreements without adjudication:")
        print("  " + ", ".join(unresolved[:20]) + (" ..." if len(unresolved) > 20 else ""))

    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        print(f"\nSaved summary to {args.out_json}")


if __name__ == "__main__":
    main()
