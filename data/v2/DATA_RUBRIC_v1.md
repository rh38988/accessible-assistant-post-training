# Training data rubric v1 (English, train_v2)

Owner: Data Lead (Ryan Hsieh). Status: used for the train_v2 screening run on 2026-11-13.
Cian-Rong owns the quality checklist in the team plan; this version is the working rubric until hers replaces it.

The assistant reply in each example is what the model learns to copy, so the bar is higher than the evaluation rubric: an example is kept only when nothing needs fixing.

## 1. Gates (any fail means the example is not kept)

| Gate | Pass when |
|---|---|
| G1 Source | Every concrete step, button or menu name, number, and policy statement is supported by the cited official page. Nothing is added from memory. |
| G2 Safety | No risky advice (sharing codes or passwords, paying, installing remote-access software, calling back a number the caller gave). For scams and money, the protective action comes first. |
| G3 No leakage or copies | Not similar to an evaluation question. Not a reworded copy of another kept example. |
| G4 Format | Valid schema, English, roles alternate, full conversation within the length cap (768 tokens; estimated as 2,200 characters). |

G3 and G4 are checked by code (`tools/build_v2.py`, `tools/assemble.py`). G1 and G2 are checked by the independent reviewer.

## 2. Scores (0, 1, 2, or NA)

| # | Dimension | 2 means |
|---|---|---|
| S1 | Required steps | The reviewer lists the required actions from the source first. All of them appear in the reply. 1 = one non-critical action missing. 0 = a critical action missing. NA for a reply that is only a clarifying question. |
| S2 | Ask or answer | If a detail that changes the steps is missing, the reply is one short question with no guessed steps. If the information is sufficient, the reply answers directly and asks nothing first. |
| S3 | Constraints kept | The reply respects everything the user said: device, goal, and limits such as "without turning it off". |
| S4 | Actionable | Clear starting point, one action per step, says what the user should see. |
| S5 | Plain language | Everyday words, on-screen labels shown exactly and explained, length fits the task. |
| S6 | Realistic user | The user message sounds like a real low-confidence user, and the scenario label matches the content. |

## 3. Decision

- **keep**: all gates pass and every score is 2 (or NA).
- **revise**: the problem can be fixed from the source. At most two revise-and-re-review rounds.
- **reject**: the source cannot support the example, the example is unsafe, it duplicates another example, or it still fails after two rounds.

Each review record stores: the required actions, which ones are covered, unsupported claims (quoted), gate results, scores, decision, reasons, and the fix that was requested. Review records are stored in `reviews/`, separate from the training answers.

## 4. Set-level rules

- At most 6 examples per task (one official page), each a different scenario type.
- Scenario types: direct, direct with a messy request, missing information (ask), follow-up after the user answers, user constraint, failure recovery. Safety tasks use: direct, second story, pressure tactic or constraint, already acted, asking for a relative, prevention.
- Task types never overlap with `eval/tasks/eval_tasks.csv`.
- Wording: the data is "AI-screened, with human spot checks". Only examples a person actually read are marked `reviewed: true`.
