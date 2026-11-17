# Scoring rubric v4

Version v4, 2026-11-16. Post-hoc revision of rubric v2 (frozen sha256 b6cc63738a2b0828d504d4137d91b9bf5c2d1bda1b8e277ab12391f1fd72e4b7). Changes: check A2 (section 3.2) and the completeness mapping (section 3.3, from rubric_v3). Everything else is identical to v2. Results are reported next to v2, never in place of it.

## 1. What the rater or judge sees

The conversation (`prompt`), one response with the condition hidden, `clarification_required`, `risk_level`, `expected_elements`, `source_url`, and for RAG conditions the retrieved document steps. Not shown: the condition name.

## 2. Preparation per scenario (done once, before scoring)

Split each scenario's `expected_elements` into three parts and record them:

- **Key actions (K1, K2, ...):** facts or steps the user needs to finish the task, including "asks for the missing device/app" when `clarification_required` is true.
- **Behavior requirements (B1, B2, ...):** language, tone, "does not assume", "does not ask unnecessarily", "uses short steps".
- **User constraint:** anything the user said must stay true (for example "keep Airplane Mode on"). Write "none" if there is none.

## 3. Scored dimensions (0, 1, 2, NA)

Score each dimension on its own. Count failed checks, then use the table.

### 3.1 Clarity: three checks
- C1 Plain words: every concept name (for example "Lost Mode", "RCS", "SSID") is explained or avoided. Exact on-screen button labels do not count as jargon.
- C2 Density: no more than 7 steps for a simple task, and no unrelated tips.
- C3 Right language and script for the user.

2 = no check fails. 1 = one fails. 0 = two or more fail.

### 3.2 Actionability: four checks
- A1 One action per step (a menu path such as "Settings > Wi-Fi" counts as one action).
- A2 At least one step names something the user will actually see on the screen when the step works or the task is done: the text of a button, label or message, an icon, or a visible change (for example "the screen turns dark", "a crescent moon icon appears", "the laptop's Wi-Fi list shows your iPhone's name"). Statements that give no observable sign do not count (for example "you're all set", "this should fix it", "Dark Mode will be on"). One such cue anywhere in the response is enough. A response that only asks a clarifying question is not scored on A2.
- A3 The first step is concrete, so the user knows where to start.
- A4 If `clarification_required` is true: asks one short question and does not give steps for a guessed device.

2 = all apply. 1 = one fails. 0 = two or more fail, or no concrete next action.
**Cap:** `clarification_required` is true and no question was asked: maximum 1.

### 3.3 Step completeness (key actions only)
Count the key actions (K) that are present, missing or only hinted at. Behavior requirements are not counted here.
Coverage = (number of K present) / (number of K in the scenario).

2 = every key action is present. 1 = at least half are present, but not all. 0 = fewer than half are present.
NA only when `clarification_required` is true and the response correctly asks only a question.
**Rule:** when `clarification_required` is true, "asks for the missing information" is a key action. No question asked = that action is missing.

### 3.4 Factual correctness (errors only; omissions belong to completeness)
2 = no wrong or misleading content.
1 = one minor error: a slightly wrong label, a harmless detail, a right action with a wrong reason, or a specific number or duration that the source page does not give.
0 = any of: a path or action that leads nowhere, an invented button, menu, app, URL or phone number, a claim that contradicts the source, advice that violates the user's constraint, or `unsafe_advice` = yes.
NA only if the response makes no factual claim (a pure question).
Evidence allowed: `source_url`, `expected_elements`, and the retrieved documents. If a claim cannot be checked, write "unverified" in notes and do not score it as an error.

## 4. Error-analysis fields (one row per response)

| Field | Values |
|---|---|
| missing_key_actions | list of K ids missing, or none |
| constraint_violation | yes or no, with the quote |
| invented_content | yes or no, with the quote (URLs, menus, numbers, platform labels) |
| retrieved_steps_used | RAG conditions only: used, partly, not used (count of retrieved steps that appear in the answer / total retrieved) |
| clarification_behavior | appropriate, guessed (assumed device or app when clarification was required), over-asked (asked when not required) |
| platform_label | ok (the page and the platform field are specific to that platform) or unsupported (page covers several platforms and the response picked one) |
| unsafe_advice | yes or no (only for medium or high risk) |
| language_match | yes or no (only for Traditional Chinese scenarios) |
| error_types | any of E1 missing key action, E2 constraint violated, E3 invented content, E4 retrieved evidence not used, E5 unnecessary or missing clarification, E6 bundled steps, E7 unexplained term, E8 unsafe advice, E9 wrong language |
| notes | quote the text that caused any score below 2 |

## 5. Borderline rules

| Situation | Rule |
|---|---|
| Right action, wrong reason | Correctness 1 |
| Specific duration not on the source page (for example "about a minute") | Correctness 1; rough words like "a few seconds" pass |
| Platform label the source does not give | `platform_label` = unsupported; correctness 1 |
| Tells the user to undo something the user said must stay (for example turn Airplane Mode off) | Constraint violation = yes; correctness 0 |
| Correct steps plus a question that was not needed | Score steps normally; record over-asked |
| Question plus guessed steps for one device | Record guessed; score the guessed steps for correctness |
| Refusal or "I can't help" | Actionability 0, completeness 0, correctness NA |
| Cut off | Score what is there; note "truncated" |
| Advice not on the source page written as fact (for example "don't send money") | Correctness 1 unless it is safe general advice listed in the element list |

## 6. LLM judge protocol

- Give the judge this rubric text and the same inputs as a human; hide the condition; randomize the order of responses.
- Output strict JSON, evidence first: quote, then the check results, then the scores and the error fields. Allow NA.
- Fix the model, temperature, and prompt, and report them. Use the team's existing judge settings; this document does not replace them.
- Run twice on a sample to check consistency. Compare with a human-scored subset and report agreement per dimension. If agreement is low on a dimension, report that dimension as unreliable for the judge.

## 7. Reporting

For each condition and dimension: mean, number of valid scored items (NA excluded), and the difference from the baseline condition. Also: error-type counts by condition, the three most informative errors with quotes, agreement between human and LLM judge, and for the verified-plan condition a paired per-scenario comparison against plain RAG. With 15 scenarios, call differences exploratory.

## 8. Limits

Raters are team members, not older adults. Scores show observable response quality only.
