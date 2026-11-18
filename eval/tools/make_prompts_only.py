#!/usr/bin/env python3
"""Make the prompts-only file that is given to the model owner.

Keeps only scenario_id and the conversation (`prompt`). Drops expected_elements,
clarification_required, risk_level, source_url, scenario_type and every other label, so the
router and generator cannot see evaluation labels.

  python make_prompts_only.py --scenarios eval_v2.jsonl --out eval_v2_prompts_only.jsonl
"""
import argparse, json

ap = argparse.ArgumentParser()
ap.add_argument("--scenarios", required=True)
ap.add_argument("--out", required=True)
a = ap.parse_args()
n = 0
with open(a.scenarios, encoding="utf-8") as f, open(a.out, "w", encoding="utf-8") as g:
    for line in f:
        if not line.strip():
            continue
        s = json.loads(line)
        g.write(json.dumps({"scenario_id": s["id"], "prompt": s["prompt"]}, ensure_ascii=False) + "\n")
        n += 1
print(f"wrote {n} prompts to {a.out}")
