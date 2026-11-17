# Output of analyze_hypotheses_v2.py (2026-11-16)

## 1. Length (answer scenarios only, n=10)
| Condition | Median words | Median numbered steps |
|---|---|---|
| original | 225 | 6 |
| prompt | 135 | 4 |
| SFT v2 | 61 | 3 |
| SFT v2 + RAG | 60 | 3 |
| v6 | 48 | 4 |

## 2. Judge check failures (share of judgments, 2 runs x 15) and key-action coverage
| Condition | C1 | C2 | C3 | A1 | A2 | A3 | A4 | Key actions covered |
|---|---|---|---|---|---|---|---|---|
| original | 73% | 80% | 7% | 67% | 63% | 17% | 33% | 11% |
| prompt | 23% | 37% | 0% | 73% | 27% | 0% | 33% | 16% |
| SFT v2 | 30% | 17% | 0% | 23% | 67% | 0% | 10% | 13% |
| SFT v2 + RAG | 7% | 17% | 0% | 27% | 87% | 7% | 3% | 32% |
| v6 | 23% | 7% | 0% | 43% | 83% | 0% | 0% | 39% |

## 3. Training data (train_v2_en.v2.0.jsonl, 1000 examples, 845 non-question replies)
- Median words 72, median numbered steps 4
- Says what the user should see or how to tell it worked: 38%
- Gives an 'if you don't see it / if it doesn't work' fallback: 15%
- Prompts with retrieved notes: 0 (the training prompts contain only the conversation)

## 4. SFT v2 + RAG: key actions missed in both judge runs (36) vs the retrieved notes (hand check)
- yes: 19
- partly: 10
- no: 3
- not a document fact: 4

## 5. v6 checker result vs judge key-action coverage
- checker accepted: n=8, coverage 55%
- checker rejected (still shipped): n=7, coverage 22%
