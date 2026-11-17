# Source, generation, review, and human-check records

Keep training JSONL, source/generation provenance, AI reviews, and human spot checks as separate files. Never overwrite rejected or pre-revision candidates; append a new candidate/version and link it through `correction_history`. These formats describe deliverables for Ryan's later 500-example batch. The two demonstration records have provenance but **no AI acceptance review** and `reviewed:false`.

## One provenance row per final training ID

Use `DEMONSTRATION_PROVENANCE.jsonl` as a working example. Required keys:

```json
{
  "id": "gsft-0001",
  "task_id": "TR-104",
  "task_group": "bookmark_site",
  "source_group": "google_chrome_bookmarks_computer",
  "content_sha256": "64 lowercase hex characters",
  "eligibility": "cleared_for_training",
  "generation": {
    "method": "writer/model and version",
    "model": "model ID or null for human writing",
    "prompt_version": "rag-system-v1",
    "candidate_id": "gsft-0001-v3"
  },
  "inference_template": {
    "builder": "eval.generate_rag.build_messages",
    "condition": "sft_v2_rag",
    "decision": {"mode": "answer", "question": ""},
    "decision_basis": "source-based reason why the stated user facts permit an answer",
    "accessibility": "",
    "source_conversation": [{"role": "user", "content": "original user request"}],
    "sections": [{"platform": "Chrome on a computer", "app": "Chrome", "text": "exact source-checked passage sent to the prompt builder"}],
    "section_ref_ids": ["chrome-bookmark-current"]
  },
  "source_refs": [{
    "ref_id": "chrome-bookmark-current",
    "organization": "Google",
    "title": "official page title",
    "url": "https://official.example/path",
    "access_date": "YYYY-MM-DD",
    "page_update_date": null,
    "section": "named page section",
    "applicability": "device/app/version and any conditions",
    "verified_excerpt": "short exact source anchor",
    "model_visible_text": "exact section text included in the ANSWER system message",
    "extraction_method": "how the official page was read and checked"
  }],
  "correction_history": [{
    "from_candidate": "gsft-0001-v2",
    "to_candidate": "gsft-0001-v3",
    "reason": "specific documented defect",
    "changed_fields": ["messages"],
    "review_id": "review-gsft-0001-v2"
  }]
}
```

The example URL above is **schema illustration only**, never a source to use. In actual rows, use a real official URL and preserve its original query parameters if applicable. For ANSWER, each `section_ref_id` maps a section to one `source_ref`; the section's exact `text` equals `source_ref.model_visible_text` and appears in the **system** message produced by the existing builder. For CLARIFY, `sections` and `section_ref_ids` are empty because the builder places the supplied clarification question without procedural references; source evidence still belongs in provenance. The source page itself must substantiate the paraphrase and answer or clarification basis. Record uncertainty or inaccessible pages as unresolved; do not accept examples from an unreadable source. Keep source groups and task groups stable across variants so split checks operate at group level.

Compute `content_sha256` over the exact final `messages` array, encoded as UTF-8 JSON with `ensure_ascii=False`, `sort_keys=True`, `separators=(',', ':')`:

```python
hashlib.sha256(json.dumps(record['messages'], ensure_ascii=False,
    sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
```

The full JSONL file also needs a byte-level SHA256 and manifest with count, accepted IDs, source/task groups, tokenizer revision, prompt version, and input file hashes. Content hashes must be recalculated after any edit. The two demonstrations' saved `decision: answer` values are template fixtures; the current router does not yet support their task groups. Production `decision_basis` must explain the ANSWER/CLARIFY choice from the user conversation and checked source applicability, independently of the target answer. A later runtime router should reproduce an appropriate decision for live RAG use; its current coverage is not a prerequisite for drafting candidates.

## Separate AI review row for every accepted example

One accepted final candidate must have one independent AI review row with this minimum shape; failed earlier reviews remain in review history. A corrected hash alone never implies acceptance.

```json
{
  "review_id": "review-gsft-0001-v3",
  "id": "gsft-0001",
  "candidate_id": "gsft-0001-v3",
  "conversation_sha256": "exact final messages hash from above",
  "reviewer_model": "separate AI reviewer model and version",
  "reviewer_prompt_sha256": "SHA256 of the reviewer prompt/version",
  "reviewed_at": "ISO-8601 timestamp",
  "source_checks": [{
    "ref_id": "chrome-bookmark-current",
    "official_url": "real official URL",
    "access_date": "YYYY-MM-DD",
    "applicability_confirmed": true,
    "source_accessible": true,
    "finding": "how page supports or fails the candidate"
  }],
  "required_actions": [{
    "action": "source-supported operation and condition",
    "source_ref_id": "chrome-bookmark-current",
    "critical": true,
    "covered_in_target": true
  }],
  "checks": {
    "factual_steps_labels_contacts_claims": "pass|fail|unverified",
    "necessary_action_coverage": "pass|fail",
    "explicit_constraints_and_completed_state": "pass|fail",
    "clarification_decision": "pass|fail",
    "no_invented_history_or_unsupported_content": "pass|fail",
    "one_action_per_step": "pass|fail",
    "brevity_without_omission": "pass|fail",
    "safety": "pass|fail"
  },
  "decision": "keep|revise|reject",
  "findings": ["precise issue or empty list"],
  "correction_required": "specific edit or empty string"
}
```

`keep` requires source accessibility, every relevant check passing, and every critical action covered. For a genuine clarification, `required_actions` may be empty, but the reviewer must verify that the missing device/app/version *actually changes the instructions* and that the reply asks one concise question with no guessed steps. For a safety task, protective action cannot be delayed behind a question. Every concrete phone number, URL, label, menu path, time limit, and claim needs relevant official passage support. The reviewer must inspect earlier assistant turns in multi-turn examples for factual or safety errors. The reviewer cannot write the candidate it reviews. AI review does **not** set the existing `reviewed` flag to `true`; that flag means a second team member checked the record under the old schema.

## Ryan's human spot-check log

Ryan should select **at least 50 of the 500 final IDs** across scenario types, task families, platforms, source groups, sensitive cases, and any AI-review edge cases. Record each row in a new batch-specific human log, with columns:

```text
id,conversation_sha256,reviewer,reviewed_at,sampling_reason,source_refs,verdict,findings,proposed_correction,resolution,corrected_candidate_id,corrected_content_sha256,followup_review_id
```

Fill `id` and exact hash before review; fill `findings` and `resolution` even for `keep` (`none` / `kept unchanged`). A changed target requires a new candidate hash, independent AI re-review, and a link to that re-review before acceptance. Keep Ryan's original `data/v2/spot_check_v2.csv` intact as historical evidence for the prior dataset; its 15 completed checks cannot count as human verification of these new 500. Do not invent spot-check IDs or outcomes before Ryan reviews them. Report AI-reviewed count and human-checked count separately.
