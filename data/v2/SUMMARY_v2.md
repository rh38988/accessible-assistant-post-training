# train_v2 (English) summary

Frozen file: `data/v2/train_v2_en.jsonl` | 708 examples | sha256 `181469ace2a6af876cac7db897762f909d9d5773d42881ebca57ea676c98714d`

Label for reports: **AI-screened, with human spot checks.**

## Funnel

| Stage | Count |
|---|---|
| Candidates reviewed | 1204 (348 existing English drafts, 856 new) |
| Kept by the independent AI review | 696 |
| Rejected by the reviewer | 5 |
| Flagged for revision, not yet resolved | 335 |
| Dropped by code checks (duplicates, length, overlap) | 0 |
| Not reviewed | 156 |
| Kept but held in reserve | 0 |
| **Final training set** | **708** (153 from existing drafts, 555 new) |

Text changed during revision: 85 of the final examples.
Human-reviewed examples in the final set: 17.

## Distribution of the final set

| Scenario | Count | Share |
|---|---|---|
| missing information | 261 | 37% |
| direct | 183 | 26% |
| constraint | 132 | 19% |
| failure recovery | 132 | 19% |

| Category | Count |
|---|---|
| technical_support | 517 |
| communication | 104 |
| online_services | 87 |

- Sensitive (safety, accounts, privacy): 115
- Multi-turn: 214
- Tasks: 173 | task types: 84 | official pages: 174
- Longest conversation: 1858 characters (cap 2200)
