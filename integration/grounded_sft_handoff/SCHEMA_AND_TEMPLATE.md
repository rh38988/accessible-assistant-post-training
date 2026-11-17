# Grounded SFT schema and model-visible template

## Chosen format: `rag-system-v1`

The target is the ordinary SFT v2 + RAG prompt from `eval/generate_sft_rag_dev.py` with no checklist. Its exact message builder is `eval.generate_rag.build_messages()` in the development checkout. Ryan's sharing branch carries [prompt_contract.py](prompt_contract.py), a portable copy verified against that builder; see [INFERENCE_ALIGNMENT.md](INFERENCE_ALIGNMENT.md). This is an explicit training format for this new batch, not a change to the saved evaluation prompts.

Each UTF-8 JSONL record keeps the existing train fields `id`, `messages`, `specification`, `category`, `platform`, `language`, `sensitive`, `sources`, `author`, and `reviewed`, plus `task_id`, `task_group`, `source_group`, and `prompt_format: "rag-system-v1"`. For this format, `messages` has **exactly three real chat roles**:

```json
[
  {"role":"system","content":"<exact build_messages() system content>"},
  {"role":"user","content":"<user_only_query(source_conversation)>"},
  {"role":"assistant","content":"<final target answer or router question>"}
]
```

`training.train_sft.to_prompt_completion()` passes `messages[:-1]` as the prompt and the final assistant turn as completion. The loader already preserves a supplied system message; `scripts/validate_data.py` now permits this three-message shape only when the explicit `prompt_format` is present. Legacy user/assistant records remain on their old schema path. There are no textual `System:` role labels in a user message.

## What goes in each role

**System, ANSWER:** The unchanged `RULES` from `eval/generate_rag.py`, its `Routing: answer from compatible evidence` instruction, and a canonical JSON array of relevant and deliberately marked inapplicable sections. Each section contributes `platform`, `app`, and the complete model-visible `instructions` text. Source URLs and document IDs stay in metadata and provenance; they are not part of this established prompt. The official passage text itself is present in the system message.

**System, CLARIFY:** The same `RULES`, `Routing: clarify`, and one question justified by the missing user fact and checked source applicability. The current inference builder does **not** supply procedural references on this route. Official sources and applicability remain in provenance to justify the question. At runtime, routing must supply an appropriate question; current router coverage of new task groups is separate work. Never fabricate an ANSWER passage to force a clarification example into a grounded-answer format.

**User:** The existing `user_only_query()` joins all user turns from the source conversation with `\n\n` in order. Explicit constraints, device/app facts, and already completed actions must be stated by the user. Earlier assistant turns are **not** in this inference prompt. For a multi-turn record, preserve the full source conversation in provenance, but write the final target so it depends only on the joined user turns and source instructions. A vague update such as “I did what you said” is insufficient if the completed action is not stated.

**Plan:** None in this chosen mode. V7 and v8 system plans are development-only for selected intents; v8 was not promoted. Do not put target-derived checklists or actions into the model input. Conditions supported by an official source remain in section text.

## Actual Qwen/TRL rendering

The pinned cached tokenizer is `Qwen/Qwen2.5-3B-Instruct` revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`. Because the record has an explicit system message, Qwen does **not** insert its default system line. For ANSWER, the generation prompt renders as:

```text
<|im_start|>system
<RULES, routing instruction, canonical JSON source sections><|im_end|>
<|im_start|>user
<joined user turns><|im_end|>
<|im_start|>assistant
```

Training renders the same prefix followed by `<final target><|im_end|>`. The actual collator masks the system and user prefix with `-100`; the supervised span includes the final assistant role header, target text, and end marker. `MODEL_VISIBLE_RENDERINGS.txt` contains the exact tokenizer renderings for both demonstrations, and `VALIDATION_RESULTS.json` records message equality, token-prefix equality, before-truncation lengths, and labels. No silent truncation is allowed: the entire system/history/target sequence must fit `--max-length 1028`. Generation `--max-new-tokens 768` is a separate output budget.

The demo source pages and their exact model-visible section text are in `DEMONSTRATION_PROVENANCE.jsonl`. For production records, provenance must include `inference_template.source_conversation`, `decision`, `sections`, and `section_ref_ids` so the validator can rebuild the two prompt messages with the portable contract tested against the development builder.
