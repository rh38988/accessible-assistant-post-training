# Evaluation

Owner: **Evaluation Lead** (scenarios, rubric, ratings, analysis)

## Pipeline

```
scenarios/*.jsonl ──> generate.py (x5 conditions) ──> outputs/*.jsonl
                                                          │
                                       make_rating_sheet.py (blinded, shuffled)
                                                          │
                          rater 1 + rater 2 fill in ratings_<name>.csv
                                                          │
                              (discuss disagreements -> adjudicated.csv)
                                                          │
                                                   analyze.py
```

## Scenario schema

Same fields as training examples, except `turns` replaces `messages` and **ends with a user turn** (the one the model answers). Add `notes_for_raters` to say what a good answer looks like.

```bash
python scripts/validate_data.py --kind scenario eval/scenarios/sample.jsonl
```

- About 40% `underspecified`, matching the training data
- Multi-turn: earlier turns are fixed, so every condition answers the same context
- Never reuse a training task as a scenario

## Conditions

| Condition | System prompt | Demonstrations | Retrieved docs | LoRA adapter |
|---|---|---|---|---|
| `prompt` | yes | | | |
| `fewshot` | yes | yes | | |
| `rag` | yes | | yes | |
| `sft` | | | | yes |
| `sft_rag` | | | yes | yes |

`rag` and `sft_rag` receive identical retrieved text. In `sft_rag` the docs are the only content of the system message, which slightly differs from training (no system message); note this when interpreting results.

Check exactly what each condition sends, without a GPU:

```bash
python eval/generate.py --condition rag --scenarios eval/scenarios/sample.jsonl --out /dev/null --dry-run
```

## Rubric

Each rater fills in every column with `1` (yes/pass), `0` (no/fail), or `NA`.

| Column | Type | Meaning |
|---|---|---|
| `clarity` | core | Plain language, easy to follow |
| `actionability` | core | The person could actually do it from these steps |
| `completeness` | core | No missing steps |
| `correctness` | core | Steps are accurate for the stated platform (check the source) |
| `asked_clarification` | measured | Did the response ask the user a question? (yes/no, not good/bad) |
| `chunking` | target | One action per step |
| `expectation_setting` | target | Says what to expect (what they'll see, how long) |
| `failure_recovery` | target | Says what to do if something goes wrong |

- **Acceptable** = all four core columns are 1. Core columns cannot be NA.
- If a response only asks a clarifying question, rate the core columns on whether the question is clear, appropriate, and enough to move forward.
- Rate blind: never open `ratings/key.csv`.

## Analysis

```bash
python eval/analyze.py --scenarios eval/scenarios/<file>.jsonl \
    --key eval/ratings/key.csv \
    --ratings eval/ratings/ratings_<rater1>.csv eval/ratings/ratings_<rater2>.csv \
    --adjudicated eval/ratings/adjudicated.csv \
    --baseline rag --candidates sft sft_rag --out-json eval/results.json
```

Reports, per condition: acceptable rate, guess rate (didn't ask when it should), over-clarification rate (asked when it shouldn't), sensitive-task acceptable rate, target behaviors, Cohen's kappa, and the decision rule (difference of at least 10 points and McNemar p < 0.05).

`adjudicated.csv` columns: `item_id, acceptable, asked_clarification`, one row per item the raters disagreed on.
