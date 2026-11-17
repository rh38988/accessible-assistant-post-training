# Scoring rubric v3 (post-hoc revision of rubric v2, completeness only)

Date: 2026-11-16. rubric_v2_FROZEN.md (sha256 `b6cc63738a2b0828d504d4137d91b9bf5c2d1bda1b8e277ab12391f1fd72e4b7`) stays the primary result and is not changed. rubric_v3 is reported next to it, never in place of it.

## Reason for the revision

On the completeness dimension, the v2 mapping (0 missing = 2, 1 missing = 1, 2 or more missing = 0) cannot separate a response that misses two key actions from one that misses five. Almost every response scored 0, so the dimension had too little resolution to compare conditions. v3 changes only the rule that turns the list of missing key actions into a score. The list of missing key actions itself is unchanged.

## What is unchanged

Everything in rubric_v2_FROZEN.md except section 3.3: the inputs, the per-scenario preparation (key actions K, behavior requirements B, user constraint), clarity, actionability, factual correctness, the error fields, the borderline rules, and the judge protocol.

## 3.3 Step completeness (v3)

Count the key actions (K) that are present, missing or only hinted at, exactly as in v2. Behavior requirements are not counted.

Coverage = (number of K present) / (number of K in the scenario).

- 2 = every key action is present (coverage 100%).
- 1 = at least half are present, but not all (coverage 50% to 99%).
- 0 = fewer than half are present (coverage below 50%).
- NA = only when `clarification_required` is true and the response correctly asks only a question.

**Rule:** when `clarification_required` is true, "asks for the missing information" is a key action. No question asked = that action is missing.

## Reporting

Report v2 and v3 completeness side by side, with the mean key-action coverage. State that v3 is a post-hoc revision made after the v2 results were seen, and that the threshold (one half) is a natural cut point, not tuned to any condition.
