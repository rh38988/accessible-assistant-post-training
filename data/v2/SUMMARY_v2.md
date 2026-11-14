# train_v2 (English) summary

Frozen file: `data/v2/train_v2_en.jsonl` | 575 examples | sha256 `3b8b41a02e13c31f3c69920206e511f329cd47c1166de1d02963ed9d444e19de`

Label for reports: **AI-screened, with human spot checks.**

## Funnel

| Stage | Count |
|---|---|
| Candidates reviewed | 1204 (348 existing English drafts, 856 new) |
| Kept by the independent AI review | 563 |
| Rejected by the reviewer | 5 |
| Flagged for revision, not yet resolved | 348 |
| Dropped by code checks (duplicates, length, overlap) | 0 |
| Not reviewed | 276 |
| Kept but held in reserve | 0 |
| **Final training set** | **575** (132 from existing drafts, 443 new) |

Text changed during revision: 29 of the final examples.
Human-reviewed examples in the final set: 17.

## Distribution of the final set

| Scenario | Count | Share |
|---|---|---|
| missing information | 205 | 36% |
| direct | 146 | 25% |
| constraint | 112 | 19% |
| failure recovery | 112 | 19% |

| Category | Count |
|---|---|
| technical_support | 420 |
| communication | 96 |
| online_services | 59 |

- Sensitive (safety, accounts, privacy): 93
- Multi-turn: 171
- Tasks: 152 | task types: 79 | official pages: 149
- Longest conversation: 1950 characters (cap 2200)
