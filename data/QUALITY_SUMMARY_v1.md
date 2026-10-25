# Data Quality-Check Summary (checkpoint, 10/28)

Owner: Data Lead (Ryan Hsieh) · Status as of 2026-10-25

## 1. Status at a glance

| Item | Count |
|---|---|
| Core tasks defined (`tasks/core_tasks_v1.md`) | **17** in 3 families |
| Training examples **human-verified** (`reviewed: true`) | **20** |
| Draft examples still awaiting review | 387 |
| Distinct official source pages (verified set / all data) | 24 / 112 |
| Validator errors (schema, roles, sources, dates) | 0 |
| Task-type overlap between training and eval | 0 |

### Verified set coverage

| Family | Core tasks | Verified examples |
|---|---|---|
| Device Basics | 7 | 9 |
| Communication | 5 | 5 |
| Online Safety | 5 | 6 |

| Conversation type | Count |
|---|---|
| Complete request | 8 (3 written in a verbose, OATS-style voice) |
| Incomplete request (model should ask one question) | 5 |
| Multi-turn clarification | 4 |
| Failure recovery | 3 |

- Every core task has at least one verified example.
- Languages: 17 English, 3 Traditional Chinese (LINE notifications, adding a LINE friend, LINE money-borrowing scam).
- 7 of the 20 are sensitive tasks (scams, accounts, location sharing).

## 2. Sources

Every example cites at least one official page, with an access date (2026-10-24). The verified set draws on:

| Publisher | Pages |
|---|---|
| Apple Support | 9 |
| Google Help (Android, Gmail, Google Account) | 6 |
| FTC Consumer Advice | 4 |
| LINE 說明中心 | 2 |
| Microsoft Support | 1 |
| Taiwan police / National Police Agency (165) | 2 |

Rules we followed:
- Steps and button names come from the cited page, not from memory.
- zh-TW examples use only LINE and Taiwan police / 165 pages, because those show the exact Chinese labels. Apple and Google pages returned English labels even in Chinese.
- If no readable official page could be found for a task, the task was swapped for one that could be verified, instead of being written from memory.
- The full source list per core task is in `tasks/core_tasks_v1.md`.

## 3. How quality was checked

Three stages, in order:

1. **Drafting from sources.** Examples were drafted by an AI model (Claude) from summaries of the cited pages. User messages follow the task types and phrasing styles of OATS, ElderBench, and GrandGuard, but are written fresh, not copied.
2. **AI pre-check.** Two independent Claude agents, which did not write the drafts, fetched every cited page and checked each of the 20 examples claim by claim, plus the target behaviors.
   - Result: 3 pass, 16 pass with notes, **1 fail**, no unsafe advice.
   - The failure (deleting an iPhone app skipped the **Delete App** tap) and 4 other confirmed issues were fixed before human review.
   - Full findings: `tasks/checkpoint_ai_precheck_v1.json`
3. **Human verification.** The Data Lead reviewed all 20 examples one by one against the cited pages, deciding on every suggested edit.
   - **5 approved as is, 15 edited.**
   - Each decision is logged in `tasks/checkpoint_verify_v1.csv` (reviewer, date, what changed, why).

### What the human review changed

| Type of change | Examples |
|---|---|
| Wording tightened (one intro line instead of two) | 5 |
| Steps split so each has one action | 4 |
| One clarifying question instead of two | 2 |
| Safety additions (pop-up warning, report to FTC, contact bank, photo of receipt) | 5 |
| UI accuracy (button names, locations, conditions) | 6 |

### Errors caught across both checks

- **Wrong steps:** iPhone app deletion skipped a tap (AI pre-check); "restart your iPhone" given as a general Wi-Fi fix, when Apple says to restart only if the Wi-Fi switch is gray (human review).
- **Unsupported claims removed:** "the person can still open" a Google Drive link; replaced with the sourced 25 MB rule.
- **Safety gap closed:** the LINE money-borrowing example now tells the user to call 165 right away if money was already sent.

## 4. Known limitations (be upfront about these)

- **Reviewer additions without a source.** 9 of the 20 examples contain at least one statement the cited page doesn't make, such as "contact your bank" or "press and hold the Action button". Each is labeled in the CSV `notes` column as a reviewer addition or judgment.
- **Not yet tested on a device.** Five UI details still need a real device:
  - Action button: press vs. press and hold (tr101-a)
  - LINE add-friend button: 「加入」 vs 「加入好友」 (tr044-d)
  - **Block Contact** confirm button (tr045-c)
  - Find My: type name, then **Send** (tr054-d)
  - Gmail Attach icon described as a paperclip (tr037-a)
- **One human reviewer.** Agreement between two reviewers hasn't been measured yet.
- **AI-drafted data.** The drafts came from an AI model and were then verified. This should be disclosed in the report, and the team should confirm it fits the course and model-provider rules.
- **Interfaces change.** Steps reflect the official pages as of 2026-10-24 and may go out of date.
- **Team perspective.** Like the evaluation, this review measures response quality as judged by the team, not usability for older adults.

## 5. Next phase: expanding the dataset

Target for the first full pilot: **about 60 to 70 verified examples** (17 core tasks × about 4 conversation types).

1. **Verify from the draft pool.** The 17 core tasks already have 207 drafts (5 to 22 per core task). Pick 3 more per core task to reach about 4 each.
2. **Add failure-recovery examples.** Only 3 exist. Draft one per core task, following the same pattern (extend an existing example).
3. **Decide on recap.** If the team adds recap as a target behavior, draft recap examples and add it to the rubric.
4. **Second reviewer.** Have another team member independently review about 10 of the verified examples, to report agreement.
5. **Device pass.** Test the open UI details above, and add a `device_tested` column to the CSV.
6. **Keep the process.** Draft from sources, AI pre-check, then human verification, with every decision logged.

Only after the LoRA pipeline works on this set do we expand toward the larger proposal scale, using the remaining 43 task types in the draft pool.

## Files

- `tasks/core_tasks_v1.md` / `.csv`: core tasks, expected results, common failures, risk levels, sources
- `tasks/checkpoint_verify_v1.csv`: the 20 verified examples and every review decision
- `tasks/checkpoint_ai_precheck_v1.json`: AI pre-check findings
- `train/*.jsonl`, `pilot/pilot_v1.jsonl`: the data (verified examples have `reviewed: true`)
