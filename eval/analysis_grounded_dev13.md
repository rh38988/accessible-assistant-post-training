# Judge analysis: ../judge_out_grounded_dev13

Responses scored: 26 (13 scenarios x 2 conditions), runs per response: 2. Failed or unparsed judge calls: 0. Excluded scenarios: none.

## Means (runs averaged per scenario, NA excluded)

| Condition | Clarity | Actionability | Completeness | Correctness | Overall | Key-action coverage |
|---|---|---|---|---|---|---|
| sft_v2_rag | 1.73 (n=13) | 1.27 (n=13) | 0.41 (n=11) | 1.25 (n=8) | 1.25 | 35% |
| grounded_ep3_rag | 1.62 (n=13) | 1.23 (n=13) | 0.55 (n=10) | 1.06 (n=8) | 1.28 | 38% |

## Paired differences (candidate - baseline; per-scenario overall score; bootstrap 95% interval)

| Baseline | Candidate | Mean difference | 95% interval | Better / worse / tie | Clear? |
|---|---|---|---|---|---|
| sft_v2_rag | grounded_ep3_rag | +0.03 | [-0.31, 0.41] | 4 / 6 / 3 | no (interval contains 0) |

## Flags (counts over response-runs)

| Condition | Constraint violated | Invented content | Unsafe advice (yes) | Clarification: appropriate / guessed / over-asked | Unverified claims (total) |
|---|---|---|---|---|---|
| sft_v2_rag | 0 | 5 | 0 | 26 / 0 / 0 | 25 |
| grounded_ep3_rag | 2 | 2 | 0 | 26 / 0 / 0 | 8 |

## Judge run-to-run agreement (exact match, pairs where both runs gave a number)

- clarity: 23 / 26 (88%)
- actionability: 25 / 26 (96%)
- completeness: 14 / 18 (78%)
- correctness: 13 / 16 (81%)

Differences between conditions are exploratory when the number of scenarios is small. Judge reruns of a whole batch can move a condition mean by about 0.3, so smaller differences should not be interpreted.
