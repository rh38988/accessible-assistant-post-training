# Independent reviewer agent: grounded SFT candidates (grounded-review-v1)

You did not write these candidates and must not edit them. Base folder: `/home/claude/gsft/integration/grounded_sft_handoff/` (below, `H/`). Your task message gives a batch name and round N.

Do not open anything under `eval/`, any `judge` file, `H/work/drafts/`, or `H/work/cards/`. Use only the review input file below and the official pages. Do not create, update or delete scheduled tasks or triggers. Make no tool calls unrelated to this task. Do not write report files. Never use em dashes.

## Input

`H/work/reviews/input/<batch>.r<N>.md` (build it if missing: `python3 H/work/tools/review_io.py render <batch> <N>`). For each candidate it shows the ID, candidate ID, conversation hash, behavior, the user turns and any earlier assistant turn, the routing decision and its basis, the passages the model sees, and the source references. The final reply comes last, after a line `TARGET (read only after step 2)`.

## For each candidate, in order

1. **Sources.** WebFetch each cited official URL yourself. Check the named section, the platform/version applicability, the excerpt, and every label, step, contact, number and claim in the model-visible passage. If a claim seems absent, fetch again with a narrower question before calling it unsupported. Passages may paraphrase the page (the writer's fetch tool summarizes), but every claim must be on the page. Confirm the verified_excerpt with a fetch asking for the exact words; if it differs, put the page's exact words in that ref's `finding` (a card fix, not by itself a reason to revise). If a page cannot be read, the source is unverified and the decision cannot be keep.
2. **Required actions, before reading the target.** From the user turns and the applicable passage only, list the necessary actions and conditions. Mark actions the user already completed. Mark inapplicable or distractor passages. For clarify, decide whether the missing device/app really changes the steps.
3. **Target.** Now read it and check:
   - every critical action covered, none the user already did repeated without reason;
   - answer vs one question is right; a clarify target is exactly the routed question;
   - explicit user constraints respected;
   - nothing invented: no steps, labels, paths, web addresses, phone numbers, durations, guarantees or claims beyond the applicable passage and official page;
   - one understandable action per step; plain words; no unexplained technical terms; brief without dropping actions;
   - safety: protective action first, contacts only where the passage gives them for that purpose;
   - for multiturn: the earlier assistant turn is correct, and the target makes sense from the user turns alone;
   - English only, no em dashes.

## Output

Write `H/work/reviews/<batch>.r<N>.jsonl`, one JSON object per candidate, in input order:

```json
{"review_id": "review-<candidate_id>", "id": "...", "candidate_id": "...", "conversation_sha256": "copy from input",
 "reviewer_model": "claude-haiku-5-5", "reviewed_at": "2026-11-17T00:00:00Z",
 "source_checks": [{"ref_id": "...", "official_url": "...", "access_date": "2026-11-17",
   "applicability_confirmed": true, "source_accessible": true, "finding": "what the page supports or not"}],
 "required_actions": [{"action": "...", "source_ref_id": "...", "critical": true, "covered_in_target": true}],
 "checks": {"factual_steps_labels_contacts_claims": "pass", "necessary_action_coverage": "pass",
   "explicit_constraints_and_completed_state": "pass", "clarification_decision": "pass",
   "no_invented_history_or_unsupported_content": "pass", "one_action_per_step": "pass",
   "brevity_without_omission": "pass", "safety": "pass"},
 "decision": "keep", "findings": [], "correction_required": ""}
```

- `source_checks`: one entry per source reference listed for the candidate (every ref_id, including distractors).
- `decision`: keep only if every check passes, every source is accessible and applicable, and every critical action is covered. Then `findings` is empty and `correction_required` is "".
- revise: quote each problem in `findings` and give the exact fix in `correction_required`.
- reject: the task or source can't support a good example; say why.
- Check values: "pass", "fail" or "unverified".

Then run `python3 H/work/tools/review_io.py check <batch> <N>` and fix your file until it prints OK. Reply with one line: `<batch> r<N>: K keep, R revise, J reject, checker OK`.
