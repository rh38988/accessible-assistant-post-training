# Note to Cian-Rong: review rules and spot-check results (from Ryan, 2026-11-13)

## What I need from you
1. Sign off on the pilot (10 to 20 examples through the reviewer). I scaled to 1,000 before this sign-off, so please check the review results now.
2. Confirm or change these rules that the reviewer used:
   - Specific durations not on the source page ("about a minute", "about five minutes") fail. Rough words like "a few seconds" pass.
   - Bundled steps (one step holding separate actions) score S4 = 1.
   - Unexplained feature names (for example "Lost Mode", "RCS", "MMS group chat") score S5 = 1 in plain-language checks.
   - Round 3 is final, so rejects at round 3 cannot be revised.
3. Decide how to score a reply that adds a platform label the page doesn't give (for example "On Windows,").

## Numbers
- Frozen training file: 1,000 examples, v2.1 (`data/v2/train_v2_en.jsonl`).
- Human spot check: 15 examples checked by Ryan (8 keep, 7 fixed). Decisions are in `data/v2/spot_check_v2.csv`.
- Reserve: 57 examples. Rejected in review: 41. Flagged and unresolved: 70. Not reviewed: 36.
- Unreadable source: Facebook help pages (blocked by robots). The pilot-017 example there was rejected.

## Patterns from the spot check
- Unsupported durations (for example "about a minute") and claims the page doesn't make.
- Advice the page doesn't give, like "don't send money", written as fact.
- Steps that bundle two actions.

Please reply with your decisions on items 1 to 3 so I can update the rules and the notes.
