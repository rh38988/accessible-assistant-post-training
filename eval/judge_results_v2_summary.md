# Final comparison: LLM judge results (rubric v2)

15 held-out scenarios x 5 conditions = 75 responses. Each response judged twice; scores are the average of the two runs. NA scores are excluded, so n differs by dimension. Source files: `judge_out/judge_raw.jsonl`, `judge_results_v2_per_response.csv`.

**Judge setup.** Model `gpt-5.6-luna` through Portkey (`@30845-fall26-openai`). The model did not accept a temperature setting, so the default was used; seed 42 was sent. Rubric: `rubric_v2_FROZEN.md` (sha256 `b6cc6373...72e4b7`). Judge saw the conversation, the response, key actions (K), behavior requirements (B), the user constraint, the source URL, and for RAG conditions the retrieved notes. Condition names were hidden and order was shuffled (seed 42).

## 1. Mean score (0-2) by condition

| Condition | Clarity | Actionability | Completeness | Correctness | Overall |
|---|---|---|---|---|---|
| original | 0.40 | 0.47 | 0.07 | 0.20 | 0.28 |
| prompt | 1.40 | 0.70 | 0.17 | 0.37 | 0.66 |
| SFT v2 | 1.57 | 1.00 | 0.20 | 0.41 | 0.82 |
| SFT v2 + RAG | 1.77 | 0.77 | 0.08 | 1.20 | 0.98 |
| SFT v2 + RAG + checks (v6) | 1.70 | 0.77 | 0.32 | 1.55 | 1.06 |

Valid n per cell is 15, except correctness (SFT v2 11, RAG 10, v6 11) and completeness (RAG 12, v6 14), where pure clarifying questions were scored NA. **Correctness and completeness means are therefore not computed on the same items across conditions**: conditions that ask more questions score on fewer, easier items.

Overall mean with 95% bootstrap interval over scenarios: original 0.28 [0.20, 0.36]; prompt 0.66 [0.56, 0.75]; SFT v2 0.82 [0.69, 0.97]; RAG 0.98 [0.81, 1.18]; v6 1.06 [0.96, 1.17].

## 2. Paired differences (same scenario, overall score)

| Comparison | Mean difference | 95% interval | Better / worse / tie (of 15) |
|---|---|---|---|
| SFT v2 - original | +0.56 | [0.35, 0.80] | 12 / 1 / 2 |
| SFT v2 - prompt | +0.19 | [-0.04, 0.44] | 6 / 6 / 3 |
| SFT v2 + RAG - SFT v2 | +0.19 | [-0.03, 0.42] | 9 / 5 / 1 |
| SFT v2 + RAG - original | +0.76 | [0.52, 0.99] | 14 / 0 / 1 |
| v6 - SFT v2 + RAG | +0.04 | [-0.18, 0.27] | 7 / 5 / 3 |
| v6 - original | +0.80 | [0.67, 0.95] | 15 / 0 / 0 |

Supported: every trained or retrieval-augmented condition beats the original model. Not supported: any ranking among SFT v2, RAG and v6 (intervals include 0). v6 vs plain RAG: 7 better, 5 worse, 3 tied.

## 3. Behaviors that matter for the task

**Asked a clarifying question where one was required (5 scenarios; both judge runs agree):** original 0/5, prompt 0/5 (one split), SFT v2 3/5, SFT v2 + RAG 5/5, v6 5/5. Over-asking when not required: 1 of 50 responses (RAG, either run).

**Violated the user's constraint (either run, of 15):** original 2 (PHONE-004, SAFE-001), SFT v2 2 (PHONE-004, SAFE-001), prompt 0, RAG 0, v6 0.

**Invented content flagged (either run, of 15):** original 8, prompt 9, SFT v2 6, RAG 4, v6 3. Examples: an invented hotspot URL (`findiphone.apple.com/hotspot`, RAG, PHONE-005) and a garbled URL (SFT v2, SAFE-002).

**Unsafe advice flagged (either run, of 15):** original 3, prompt 2, SFT v2 3, RAG 1, v6 1. For RAG the flag is SAFE-004 (it added a US agency for a Taiwan scam and a vague "stop paying bills").

**Retrieved steps used in the answer (RAG; judge's rating):** RAG: used 0, partly 8, not used 5, runs disagree 2. v6: used 1, partly 6, not used 5, runs disagree 3.

## 4. Error types (derived from structured judge fields; a response counts if flagged in at least one run; of 15)

| Error type | original | prompt | SFT v2 | RAG | v6 |
|---|---|---|---|---|---|
| E1 missing key action | 15 | 15 | 14 | 14 | 14 |
| E2 constraint violated | 2 | 0 | 2 | 0 | 0 |
| E3 invented content | 8 | 9 | 6 | 4 | 3 |
| E4 retrieved evidence not used or only partly | 0 | 0 | 1 | 15 | 14 |
| E5 clarification problem (guessed or over-asked) | 5 | 5 | 2 | 1 | 0 |
| E6 bundled steps | 12 | 12 | 5 | 4 | 8 |
| E7 unexplained term | 12 | 5 | 6 | 2 | 5 |
| E8 unsafe advice | 3 | 2 | 3 | 1 | 1 |
| E9 wrong language | 1 | 0 | 0 | 0 | 0 |

The judge's own `error_types` list was unreliable (it sometimes listed all nine codes), so it was not used.

## 5. What the errors say about the next round

1. Missing key actions is the dominant failure for every condition (14 or 15 of 15). Completeness is near the floor for all conditions, so it separates conditions poorly.
2. Retrieved steps are rarely carried into the answer (E4 14 to 15 of 15), even when the right document is retrieved.
3. Asking for clarification now works with SFT v2 + RAG and v6 (5/5).
4. Constraint tracking is fixed in the RAG conditions (0 violations), but the answers still omit the steps that make the task complete.
5. v6 reduces invented content and clarification problems but increases bundled steps (8 vs 4).

## 6. Judge reliability (two runs per response)

| Dimension | n | Exact agreement | Within 1 point | Quadratic weighted kappa |
|---|---|---|---|---|
| Clarity | 75 | 76% | 96% | 0.70 |
| Actionability | 75 | 72% | 100% | 0.67 |
| Completeness | 67 | 97% | 100% | 0.86 |
| Correctness | 61 | 84% | 97% | 0.82 |

Agreement between the two runs on structured fields (of 75): constraint violation 74, invented content 68, clarification behavior 75, retrieved-steps rating 69, set of missing key actions 66. Five responses were scored NA in one run and numeric in the other.

## 7. Limits

- The judge was not validated against human ratings on these outputs, and rubric v2 was not calibrated with a second human rater, so there is no human agreement figure.
- One judge model, no temperature control; two runs only.
- The earlier human pilot (5 scenarios, 3 conditions, rubric v1, older outputs) is not comparable with these numbers. The v2 judge is much stricter than the v1 human pilot (original: about 0.28 overall here versus about 1.2 there).
- 15 scenarios; intervals are bootstrap over scenarios. Differences among SFT v2, RAG and v6 are not reliable.
- Retrieved notes are source-checked paraphrases, not the full official pages. The v6 checker's own result was 8 of 15 accepted.
- Raters are team members, not older adults.
