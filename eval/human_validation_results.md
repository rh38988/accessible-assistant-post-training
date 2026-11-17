# Human validation of the LLM judge

Setup: 10 responses (2 per condition, 10 scenarios), condition hidden from the rater. One rater (Cian-Rong) scored them with rubric_v2_FROZEN.md. The judge scores come from the 2-run judge output on the same responses (judge_results_v2_per_response.csv). Files: human_validation_ratings.csv, human_validation_key_DO_NOT_OPEN.csv.

## Agreement per dimension (judge run 1 / run 2)

| Dimension | n | Exact | Within 1 | Quadratic weighted kappa | Mean human | Mean judge |
|---|---|---|---|---|---|---|
| Clarity | 10 | 6 / 7 | 9 / 10 | 0.51 / 0.74 | 1.70 | 1.20 / 1.40 |
| Actionability | 10 | 5 / 6 | 10 / 10 | 0.53 / 0.44 | 1.20 | 1.10 / 1.20 |
| Completeness | 9 | 7 / 7 | 9 / 9 | undefined (judge gave 0 on all 9) | 0.22 | 0.00 |
| Correctness | 9 | 7 / 7 | 8 / 8 | 0.67 / 0.67 | 1.00 | 0.67 |

NA items (H09 completeness and correctness for the judge) are excluded from those dimensions.

## Findings

- Direction: the judge is equal to or stricter than the human on every dimension (mean difference: clarity -0.40, actionability -0.05, completeness -0.22, correctness -0.33, averaging the two runs).
- Completeness: agreement is high (7/9), but this is mostly because both give 0 to almost every response. The two cases where the human gave 1 (H04, H08) were scored 0 by the judge. Completeness cannot separate conditions well for either scorer.
- Actionability: lowest agreement. Largest disagreements on H02 (human 1, judge 2 on both runs) and H06 (human 1, judge 2 on run 1).
- Judge run-to-run differences affect agreement (clarity kappa 0.51 vs 0.74), so a single judge run is not stable on clarity.
- The human rater also revised H01 before the final record (first 2, 2, 2, NA, then 2, 1, 0, 2).

## Limits

Ten responses and one human rater. Kappa values on 9 to 10 items are very imprecise. No second human rater, so human-human agreement is unknown. The human rater also knew the rubric's design. Treat the judge as roughly consistent with the human on correctness and clarity, less reliable on actionability, and not informative on completeness.

## Actionability re-rated with the v4 check A2 (post-hoc)

The rater re-scored actionability of the 8 English items using the rubric v4 definition of A2 (a step must name something the user will see on the screen). Clarity, completeness and correctness scores are unchanged. The v2 human scores are kept in the `actionability` column; the re-rated scores are in `actionability_v4`. Changed items: H05 (1 to 2) and H06 (1 to 2).

| Comparison (8 items) | Exact run 1 / run 2 | Within 1 | Quadratic weighted kappa run 1 / run 2 | Mean human | Mean judge |
|---|---|---|---|---|---|
| v2 human vs v2 judge | 4 / 6 | 8 / 8 | 0.30 / 0.47 | 1.38 | 1.38 |
| v4 human vs v4 judge | 5 / 3 | 8 / 8 | 0.54 / 0.23 | 1.62 | 1.25 |

Reading: agreement on actionability does not improve under v4. Exact agreement is 4 and 6 of 8 under v2, 5 and 3 of 8 under v4, and the two v4 judge runs disagree with each other on 2 of 8 items (H02 and H05), so the judge's own run-to-run noise is as large as the effect of the definition change. With 8 items and one human rater this cannot show that v4 is better or worse. The judge is stricter than the human under v4 (1.25 vs 1.62).
