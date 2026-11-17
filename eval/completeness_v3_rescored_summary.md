# Completeness rescored with rubric v3 (post-hoc), 13 English scenarios

rubric_v3 changes only the completeness mapping (see rubric_v3.md). The judge's K-level judgments (which key actions are missing) are unchanged; only the rule that turns them into a score is new. Computed from judge_out/judge_raw.jsonl, both runs, NA excluded, then averaged per scenario. The v2 column is the frozen primary result.

| Condition | v2 completeness | v3 completeness | Mean key-action coverage | n scored |
|---|---|---|---|---|
| original | 0.08 | 0.08 | 13% | 13 |
| prompt | 0.19 | 0.12 | 18% | 13 |
| sft_v2 | 0.23 | 0.27 | 11% | 13 |
| sft_v2_rag | 0.10 | 0.30 | 29% | 10 |
| sft_v2_rag_v6 | 0.38 | 0.46 | 37% | 12 |

## v3 score distribution (counts of response-runs, 13 scenarios)

| Condition | 0 | 1 | 2 | NA |
|---|---|---|---|---|
| original | 24 | 2 | 0 | 0 |
| prompt | 23 | 3 | 0 | 0 |
| sft_v2 | 21 | 3 | 1 | 1 |
| sft_v2_rag | 14 | 5 | 0 | 7 |
| sft_v2_rag_v6 | 14 | 7 | 1 | 4 |

## Run-to-run agreement of completeness (13 scenarios, response level, NA pairs excluded)

- v2: exact 55/57
- v3: exact 54/57

## Paired v3 completeness differences (scenarios scored in both conditions)

| Comparison | Mean diff | 95% bootstrap interval | better / worse / tie |
|---|---|---|---|
| sft_v2 - original | +0.19 | [-0.12, 0.58] (n=13) | 3 / 1 / 9 |
| sft_v2 - prompt | +0.15 | [-0.15, 0.58] (n=13) | 3 / 2 / 8 |
| sft_v2_rag - sft_v2 | +0.15 | [0.00, 0.35] (n=10) | 2 / 0 / 8 |
| sft_v2_rag_v6 - sft_v2_rag | +0.15 | [-0.25, 0.55] (n=10) | 2 / 1 / 7 |
| sft_v2_rag_v6 - original | +0.38 | [0.08, 0.71] (n=12) | 4 / 0 / 8 |
