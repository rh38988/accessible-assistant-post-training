# Overlap check: eval_v1 (15 scenarios) vs training data v2.0 / v2.1 / v2.2 and reserve

Date: 2026-11-16. Data read from branch `data-v2` (commit 80a4cfb) and `eval` (eval_v1.jsonl). Read-only.

Method: for every training example, compare the user turns with the user turns of each eval scenario. Normalised text (lowercase, punctuation removed). Also compare source URLs.

| Training file | Examples | Exact user-text match | Near match (similarity 0.8 or more) | Same source URL as an eval scenario |
|---|---|---|---|---|
| v2.0 | 1000 | 0 | 0 | 0 |
| v2.1 | 1000 | 0 | 0 | 0 |
| v2.2 | 1000 | 0 | 0 | 0 |
| reserve | 57 | 0 | 0 | 0 |

Shared 5-word phrases: the most shared phrases are generic ("how do i turn on", "how do i do that"). The highest pair (tr206-a vs EVAL-COMM-003) shares only "I'm in a Zoom meeting on my", then asks a different question (captions vs muted microphone). Not an overlap.

Limits: the check covers wording and source URL, not meaning. Chinese examples are not in the English training file. The adapter used for the evaluated SFT v2 is named `train-v2-ready-981-3ep-resume-...`; the exact training file for that adapter has not been confirmed.
