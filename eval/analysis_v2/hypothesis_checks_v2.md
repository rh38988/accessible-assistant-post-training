# Checking the three hypotheses behind the v2 judge results

Date: 2026-11-16. **Exploratory, post hoc.** Rubric v2 stays frozen; nothing here rescores anything. All numbers are reproduced by `analyze_hypotheses_v2.py` from the judge files on this branch, the saved model outputs (branch `share-rag-evidence-20261116`, `eval/outputs/`), and the training data (branch `data-v2`). The one hand judgment is in `rag_missing_vs_notes_v2.csv`.

Caveats that apply to everything below: 15 scenarios; one judge model; the RAG and v6 settings were developed on these same 15 scenarios (the v6 summary lists checklist, action-plan and verified v2 to v6 runs), so they are development results, not held-out results.

## A better completeness number from the same judge output

Completeness (0 to 2) needs every key action present, and most scenarios have 3 or more, so nearly every response scores 0. The judge's `missing_key_actions` field gives the share of key actions covered, which does separate the conditions:

| Condition | Key actions covered |
|---|---|
| original | 11% |
| prompt | 16% |
| SFT v2 | 13% |
| SFT v2 + RAG | 32% |
| v6 | 39% |

Suggest reporting this next to the frozen completeness score, labeled as a post hoc measure.

## Hypothesis 1: "The 3B model writes short, generic answers, so it misses steps"

**Partly supported, and part of the cause is the training data.**

- On the 10 scenarios that need an answer (not a question), median length is 225 words for the original model, 135 for prompt, about 60 for SFT v2 and SFT v2 + RAG, and 48 for v6. The training data's median reply is 72 words, so the trained model is a little shorter than its data, not much shorter.
- Length alone does not explain the misses: the original model writes the most and still covers only 11% of key actions.
- What the trained models leave out most is saying how to tell it worked. Judge check A2 ("says what the user should see, or how to tell it worked") fails in 67% of SFT v2, 87% of RAG and 83% of v6 judgments.
- The training data rarely shows this: 38% of training replies say what the user should see, and 15% say what to do if a step doesn't work (approximate, by pattern matching).

## Hypothesis 2: "The model treats retrieved steps as background, not as a list to follow"

**Supported.** For SFT v2 + RAG, 36 key actions were missed in both judge runs. Checked by hand against the notes that were actually retrieved:

| In the retrieved notes? | Count |
|---|---|
| yes | 19 |
| partly | 10 |
| no (retrieval or corpus gap) | 3 |
| not a document fact (explain a term, format, ask a question) | 4 |

So about 80% of the missed actions were fully or partly in front of the model. Example, EVAL-PHONE-005: the retrieved note says to pick the iPhone's hotspot from the laptop's Wi-Fi list and enter the password shown on the phone; the answer instead sends the user to an invented `findiphone.apple.com/hotspot`.

A likely reason: SFT v2 was trained on prompts that contain only the conversation, never retrieved notes, so it never practiced answering from them. Two scenarios (COMM-001, SAFE-005) also retrieved off-topic notes.

The hand check is one rater's judgment (Claude) and should be confirmed by a team member.

## Hypothesis 3: "v6 has more steps, but bundles actions, which costs actionability"

**Partly supported.**

- Check A1 (one action per step) fails in 43% of v6 judgments vs 27% for plain RAG.
- v6 also covers more key actions (39% vs 32%), so the bundling comes with more content.
- v6's own checker does separate good from bad answers: the 8 it accepted cover 55% of key actions, the 7 it rejected cover 22%. The rejected answers were still used, because the retry limit was 1 and there was no fallback.
- The checker is not always right: it rejected SAFE-002 for 1-800-633-4227 and ReportFraud.ftc.gov, which the scenario's key actions ask for.

## What this suggests

1. Inference change, no retraining (implemented in `eval/v7/`): have the model write each verified step from the v6 action plan one at a time, so none can be dropped and each step holds one action; return the router's clarifying question word for word.
2. Data change, for a future SFT round: include retrieved notes in some training prompts, and add "what you'll see" and "if you don't see it" lines where the source supports them.
3. Write more held-out scenarios from `eval/tasks/eval_tasks.csv` before claiming any RAG variant is better, since all variants were tuned on these 15.
