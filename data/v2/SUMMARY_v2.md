# train_v2 (English) summary

Frozen file: `data/v2/train_v2_en.jsonl` | 1000 examples | sha256 `fec4686554ac8b8873f1a7e6c41acc5b71c5ef5eadb881302f1b184dc8662119`

Label for reports: **AI-screened, with human spot checks.**

## Funnel

| Stage | Count |
|---|---|
| Candidates reviewed | 1204 (348 existing English drafts, 856 new) |
| Kept by the independent AI review | 1045 |
| Rejected by the reviewer | 41 |
| Flagged for revision, not yet resolved | 70 |
| Dropped by code checks (duplicates, length, overlap) | 0 |
| Not reviewed | 36 |
| Kept but held in reserve | 57 |
| **Final training set** | **1000** (280 from existing drafts, 720 new) |

Text changed during revision: 341 of the final examples.
Human-reviewed examples in the final set: 17.

## Distribution of the final set

| Scenario | Count | Share |
|---|---|---|
| direct | 335 | 34% |
| missing information | 328 | 33% |
| constraint | 170 | 17% |
| failure recovery | 167 | 17% |

| Category | Count |
|---|---|
| technical_support | 642 |
| online_services | 190 |
| communication | 168 |

- Sensitive (safety, accounts, privacy): 227
- Multi-turn: 303
- Tasks: 194 | task types: 99 | official pages: 209
- Longest conversation: 1858 characters (cap 2200)
