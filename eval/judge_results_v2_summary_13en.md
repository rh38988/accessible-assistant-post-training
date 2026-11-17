# Final judge results, 13 English scenarios (65 responses)

The two Traditional Chinese scenarios (EVAL-COMM-005, EVAL-SAFE-004) are excluded because the training data is English only. Same judge, same frozen rubric_v2, 2 runs each; means of the two runs, NA excluded. The 15-scenario results remain in judge_results_v2_summary.md.

| Condition | Clarity | Actionability | Completeness | Correctness | Overall |
|---|---|---|---|---|---|
| original | 0.31 (n=13) | 0.46 (n=13) | 0.08 (n=13) | 0.23 (n=13) | 0.27 |
| prompt | 1.42 (n=13) | 0.73 (n=13) | 0.19 (n=13) | 0.31 (n=13) | 0.66 |
| sft_v2 | 1.58 (n=13) | 1.08 (n=13) | 0.23 (n=13) | 0.44 (n=9) | 0.83 |
| sft_v2_rag | 1.81 (n=13) | 0.88 (n=13) | 0.10 (n=10) | 1.25 (n=8) | 1.01 |
| sft_v2_rag_v6 | 1.73 (n=13) | 0.73 (n=13) | 0.38 (n=12) | 1.56 (n=9) | 1.10 |

## Paired differences (per-scenario mean of the four dimensions, 13 scenarios, bootstrap 95% interval)

| Comparison | Mean diff | 95% interval | better / worse / tie |
|---|---|---|---|
| sft_v2 - original | +0.62 | [0.39, 0.87] | 11 / 1 / 1 |
| sft_v2 - prompt | +0.23 | [-0.01, 0.52] | 5 / 5 / 3 |
| sft_v2_rag - original | +0.84 | [0.58, 1.07] | 12 / 0 / 1 |
| sft_v2_rag - sft_v2 | +0.21 | [-0.04, 0.48] | 8 / 4 / 1 |
| sft_v2_rag_v6 - sft_v2_rag | -0.01 | [-0.28, 0.25] | 5 / 5 / 3 |
| sft_v2_rag_v6 - original | +0.83 | [0.68, 0.99] | 13 / 0 / 0 |

## Run-1 flags

| Condition | Constraint violated | Invented content | Clarification behavior (run 1) |
|---|---|---|---|
| original | 2 | 7 | guessed 5, appropriate 8 |
| prompt | 0 | 8 | guessed 4, appropriate 8, over-asked 1 |
| sft_v2 | 1 | 5 | appropriate 11, guessed 2 |
| sft_v2_rag | 0 | 2 | appropriate 13 |
| sft_v2_rag_v6 | 0 | 3 | appropriate 13 |

## Human validation without the two Chinese items (8 items: H02, H04, H05, H06, H07, H08, H09, H10)

| Dimension | n | Exact run1 / run2 | Within 1 run1 / run2 | Mean human | Mean judge run1 / run2 |
|---|---|---|---|---|---|
| clarity | 8 | 5 / 5 | 8 / 8 | 1.62 | 1.25 / 1.25 |
| actionability | 8 | 4 / 6 | 8 / 8 | 1.38 | 1.38 / 1.38 |
| completeness | 7 | 5 / 5 | 7 / 7 | 0.29 | 0.00 / 0.00 |
| correctness | 7 | 6 / 6 | 7 / 7 | 1.00 | 0.86 / 0.86 |
