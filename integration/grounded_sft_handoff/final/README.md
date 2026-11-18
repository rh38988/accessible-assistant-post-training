# Grounded SFT 500 (rag-system-v1)

Ryan's 500 English, official-source-grounded training examples, built for Shirley's handoff (`../HANDOFF_TO_RYAN.md`). Every record uses the exact `rag-system-v1` template from `../prompt_contract.py`.

## Files

| File | What it is |
|---|---|
| `grounded_sft_500.jsonl` | 500 training records |
| `grounded_sft_500.provenance.jsonl` | one row per id: official URL, section, applicability, verified anchor, exact model-visible passage, decision basis, correction chain |
| `grounded_sft_500.ai_reviews.jsonl` | the independent `keep` review bound to each final content hash |
| `grounded_sft_500.human_spot_checks.csv` | Ryan's sheet: 55 sampled ids with hashes; outcomes not filled yet |
| `grounded_sft_500.task_clearance_request.csv` | 95 task groups for the evaluation owner to clear |
| `grounded_sft_500.manifest.json` | counts, file hashes, every id and hash, exclusions, input hashes |

## Gates

| Gate | Status |
|---|---|
| Schema, English, prompt rebuild, provenance hashes, source mapping, train_v2.1 overlap, eval task types | Pass (Shirley's validator up to the tokenizer step) |
| Independent AI review per final hash | Pass: 500 of 500 `keep`. Simulated with eligibility set to cleared, `--require-ai-review` passes |
| Token length (max 1,028) | Not run here: needs the cached Qwen tokenizer revision `aa8e725...` |
| Evaluation-owner task clearance | Pending: `disposition` blank for all 95 groups |
| Ryan's human spot checks (at least 50) | Pending: 55 ids selected, 0 checked |

Eligibility stays `pending_eval_owner_clearance` until the evaluation owner fills the clearance file.

## Counts

- Behavior: 200 direct, 125 clarify, 100 constraint, 75 multiturn
- Tags: 120 safety, 117 distractor, 183 conditional
- 95 task groups (at most 7 each), 213 source groups
- Category: 272 technical_support, 142 online_services, 86 communication
- Authors: 498 drafted by Claude Haiku writer agents, 2 by the main session; reviews by separate Claude Haiku reviewer agents that never saw their own work

## How it was made

1. Allocation of 95 task groups (`../work/allocation_v1.csv`), avoiding the 15 blocked development task types.
2. Writer agents read each official page and wrote a source card, then drafted candidates (`../work/AGENT_GSFT_WRITER.md`).
3. Independent reviewers re-read every cited page, listed required actions before reading the target, and decided keep, revise or reject (`../work/AGENT_GSFT_REVIEWER.md`).
4. Revisers applied corrections as new versions, never editing old ones (`../work/AGENT_GSFT_REVISER.md`); each version was reviewed again. Up to 5 rounds.
5. `../work/tools/assemble_gsft.py` picked the final 500.

502 candidates were drafted. Excluded: `gsft-romance_scam-02` (still `revise` after 4 rounds) and `gsft-account_password_reset-01` (kept, but over the direct target).

## Things to know

- **Passages are close paraphrases.** The fetch tool returns page summaries and only short exact quotes, so `model_visible_text` follows the page closely but is not always word for word. Each claim was checked against the live page by an independent reviewer. `verified_excerpt` is the short exact anchor.
- **Source addresses.** For 135 example-source pairs the reviewer read the same official page at another address (often a regional Apple page or a reordered Google URL). Provenance records the address actually read, with the card's address in `card_url`.
- **Wording overlap warnings (12, for manual review).** 9 are multiturn examples whose opening question resembles a train_v2 user turn; their final question differs. 3 single-turn clarify prompts are close paraphrases of train_v2 user turns: `gsft-bookmark_site-03`, `gsft-brightness-03`, `gsft-ring_volume-03`. Kept because the format and target differ; reword and re-review them if the team wants zero overlap.
- **Dev overlap notes.** `wifi_connect`, `video_captions`, `bluetooth_pair` and `crypto_investment_scam` are near the development set; flagged in the clearance request.

## Full validation (on a machine with the Qwen tokenizer cached)

```bash
python integration/grounded_sft_handoff/validate_grounded.py \
  integration/grounded_sft_handoff/final/grounded_sft_500.jsonl \
  --provenance integration/grounded_sft_handoff/final/grounded_sft_500.provenance.jsonl \
  --reviews integration/grounded_sft_handoff/final/grounded_sft_500.ai_reviews.jsonl \
  --against data/v2/versions/train_v2_en.v2.1.jsonl --expected-count 500
```

After the evaluation owner fills the clearance file and eligibility is set to `cleared_for_training`, add `--require-ai-review --task-clearance <filled csv> --require-task-clearance`.
