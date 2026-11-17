#!/usr/bin/env python3
"""Post hoc checks of the three hypotheses in judge_results_v2_summary.md.

Exploratory: rubric v2 is frozen and is not changed here. Every number comes from
files already produced by the judge run, the saved model outputs, and the training data.

    python eval/analysis_v2/analyze_hypotheses_v2.py \
        --outputs-dir <share-rag-evidence-20261116 checkout>/eval/outputs \
        --train <data-v2 checkout>/data/v2/versions/train_v2_en.v2.0.jsonl

Inputs from this branch: eval/scenarios/eval_v1.jsonl, eval/scenario_prep_v2.json,
eval/judge_results_v2_per_response.csv, eval/judge_out/judge_raw.jsonl,
eval/analysis_v2/rag_missing_vs_notes_v2.csv (hand judgment, see that file).
"""
import argparse
import csv
import json
import re
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
COND = {"original": "original", "prompt": "prompt", "sft_v2": "SFT v2", "sft_v2_rag": "SFT v2 + RAG",
        "sft_v2_rag_v6": "v6"}
FILES = {"original": "eval_v1-original.jsonl", "prompt": "eval_v1-prompt.jsonl",
         "sft_v2": "dev-sft-v2-fd4787c4a7e34e73a46019b345216f4d.jsonl",
         "sft_v2_rag": "dev-sft-v2-rag-20261115.jsonl",
         "sft_v2_rag_v6": "dev-sft-v2-rag-verified-action-plan-v6-20261115.jsonl"}
CHECKS = ["C1", "C2", "C3", "A1", "A2", "A3", "A4"]
# Training-data patterns (regular expressions, so counts are approximate).
SEE = re.compile(r"(you(?:'ll| will| should)? see|should (?:now )?(?:see|show|appear|turn)|will (?:show|appear|turn|change)"
                 r"|appears?\b|shows? (?:up|a|the|that)|turns? (?:blue|green|gray|grey|on)|that means|you can tell|is now (?:on|off))", re.I)
FALL = re.compile(r"(if you (?:don't|do not|can't|cannot) (?:see|find)|if (?:it|that|this) (?:doesn't|does not|didn't|still)"
                  r"|if (?:the|that) (?:option|button|setting) (?:isn't|is not)|tell me what you see|if nothing)", re.I)
STEP = re.compile(r"(?m)^\s*\d+\.\s")


def jl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def kid(x):
    return str(x).split(":")[0].strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outputs-dir", required=True)
    ap.add_argument("--train", required=True)
    a = ap.parse_args()

    scen = {s["id"]: s for s in jl(EVAL / "scenarios/eval_v1.jsonl")}
    prep = json.load(open(EVAL / "scenario_prep_v2.json", encoding="utf-8"))
    rows = list(csv.DictReader(open(EVAL / "judge_results_v2_per_response.csv", encoding="utf-8-sig")))
    raw = {(r["blind_id"], r["run"]): (r["parsed"] or {}) for r in jl(EVAL / "judge_out/judge_raw.jsonl")}
    resp = {(r["scenario_id"], c): r["response"] for c, f in FILES.items() for r in jl(Path(a.outputs_dir) / f)}
    answer_ids = [s for s in scen if not scen[s]["clarification_required"]]

    print("## 1. Length (answer scenarios only, n=%d)" % len(answer_ids))
    print("| Condition | Median words | Median numbered steps |\n|---|---|---|")
    for c in FILES:
        w = [len(resp[(s, c)].split()) for s in answer_ids]
        n = [len(STEP.findall(resp[(s, c)])) for s in answer_ids]
        print(f"| {COND[c]} | {st.median(w):.0f} | {st.median(n):.0f} |")

    fails, njudg, cover = defaultdict(Counter), Counter(), defaultdict(list)
    for r in rows:
        c, nk = r["condition"], len(prep[r["scenario_id"]]["key_actions"])
        for run in (1, 2):
            p = raw.get((r["blind_id"], run), {})
            njudg[c] += 1
            for grp in ("clarity_checks", "actionability_checks"):
                for k, v in (p.get(grp) or {}).items():
                    if v is False:
                        fails[c][k] += 1
            cover[c].append(1 - len({kid(x) for x in (p.get("missing_key_actions") or [])}) / nk)
    print("\n## 2. Judge check failures (share of judgments, 2 runs x 15) and key-action coverage")
    print("| Condition | " + " | ".join(CHECKS) + " | Key actions covered |\n|---|" + "---|" * (len(CHECKS) + 1))
    for c in FILES:
        print(f"| {COND[c]} | " + " | ".join(f"{fails[c][k] / njudg[c]:.0%}" for k in CHECKS)
              + f" | {st.mean(cover[c]):.0%} |")

    tr = jl(a.train)
    fin = [r["messages"][-1]["content"] for r in tr]
    clar = [len(STEP.findall(t)) == 0 and t.strip().endswith("?") for t in fin]
    ans = [t for t, q in zip(fin, clar) if not q]
    print(f"\n## 3. Training data ({a.train.split('/')[-1]}, {len(tr)} examples, {len(ans)} non-question replies)")
    print(f"- Median words {st.median(len(t.split()) for t in ans):.0f}, median numbered steps {st.median(len(STEP.findall(t)) for t in ans):.0f}")
    print(f"- Says what the user should see or how to tell it worked: {sum(bool(SEE.search(t)) for t in ans) / len(ans):.0%}")
    print(f"- Gives an 'if you don't see it / if it doesn't work' fallback: {sum(bool(FALL.search(t)) for t in ans) / len(ans):.0%}")
    print("- Prompts with retrieved notes: 0 (the training prompts contain only the conversation)")

    hand = list(csv.DictReader(open(EVAL / "analysis_v2/rag_missing_vs_notes_v2.csv", encoding="utf-8")))
    cnt = Counter(h["in_retrieved_notes"] for h in hand)
    print(f"\n## 4. SFT v2 + RAG: key actions missed in both judge runs ({len(hand)}) vs the retrieved notes (hand check)")
    for k in ("yes", "partly", "no", "not a document fact"):
        print(f"- {k}: {cnt[k]}")

    v6 = {r["scenario_id"]: r for r in jl(Path(a.outputs_dir) / FILES["sft_v2_rag_v6"])}
    acc = defaultdict(list)
    for r in rows:
        if r["condition"] != "sft_v2_rag_v6":
            continue
        nk = len(prep[r["scenario_id"]]["key_actions"])
        c = [1 - len({kid(x) for x in (raw.get((r["blind_id"], k), {}).get("missing_key_actions") or [])}) / nk for k in (1, 2)]
        acc[bool(v6[r["scenario_id"]]["accepted"])].append(st.mean(c))
    print("\n## 5. v6 checker result vs judge key-action coverage")
    for k in (True, False):
        print(f"- checker {'accepted' if k else 'rejected (still shipped)'}: n={len(acc[k])}, coverage {st.mean(acc[k]):.0%}")


if __name__ == "__main__":
    main()
