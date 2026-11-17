# Selected inference contract for grounded SFT

## Decision

Use the ordinary **SFT v2 + RAG answer/clarification prompt** in `eval/generate_sft_rag_dev.py` with `checklist=False`. That runner attaches the SFT v2 adapter and reuses `eval.generate_rag.prepare()` / `build_messages()`; its 15-case baseline was saved as `eval/outputs/dev-sft-v2-rag-20261115.jsonl`. The development runner is not on Ryan's remote `data-v2` branch. [prompt_contract.py](prompt_contract.py) is a portable snapshot of the selected message builder and user-turn join, tested for exact output equality against the development code. This is a **handoff design target**, not evidence that the experimental CLI is a production service.

The checklist, v7 action-plan, and v8 realization modes append additional system content. The local v8 report says **do not promote v8** because final-answer reliability did not improve consistently. The new 500 therefore target the ordinary RAG message contract; they do not train on a plan that is unavailable for most new task groups. The historical experiment prompts and outputs remain untouched.

## Exact model input

`build_messages(user_text, decision, sections, accessibility='')` returns exactly two messages:

| Route | System message | User message | Plan/constraints |
| --- | --- | --- | --- |
| ANSWER | Verbatim `RULES`, then `Routing: answer from compatible evidence. Reference instructions:`, then canonical JSON of `[{"platform": ..., "app": ..., "instructions": section.text}, ...]`. Source URLs and document IDs are absent. | `user_only_query(source_conversation)`: all user-turn text joined by two newlines in order. | No structured plan. Explicit constraints and completed actions must be stated in the user turns; source conditions are in section text. |
| CLARIFY | Verbatim `RULES`, then `Routing: clarify. Return only this question:`, then the supplied clarification question. No procedural sections are supplied to the model. | The same joined user-turn text. | For candidate drafting, justify the question from the user request and checked sources, not from the target answer. Runtime routing must later supply an equivalent decision. |
| INSUFFICIENT | Verbatim `RULES`, then `Routing: insufficient evidence. Do not give procedural instructions.` | The same joined user-turn text. | No source-backed procedure is available. |

The 500-example acceptance format covers ANSWER and genuine CLARIFY cases. An INSUFFICIENT route is a source gap to resolve, not an accepted training example to use as a count filler.

The generation tokenizer uses `apply_chat_template(messages, add_generation_prompt=True)`, so it ends with `<|im_start|>assistant\n`. Training adds the final assistant message as the completion. The exact train prefix is the two inference messages, without moving references into the user role. TRL supervises the final assistant header, answer, and closing marker; the system and user tokens are masked. `MODEL_VISIBLE_RENDERINGS.txt` shows both renderings and their SHA256 values.

This mode **drops previous assistant turns** before prompting: `retrieval.audit.user_only_query()` selects user turns only. A multi-turn training example may retain the source conversation in provenance, but its model-visible user message must contain only the joined user turns. If a previous assistant step matters, the user's later turn must state what they did or know; the target cannot depend on an unseen assistant turn. Do not insert textual role labels to simulate history.

For ANSWER records, each provenance `sections[].text` is the exact passage sent through the builder, and `section_ref_ids` maps those sections to official-source provenance. For CLARIFY, source evidence can justify the routing decision in provenance, but the model-visible prompt contains the router's question and no reference instructions, matching inference.

## Demonstration comparison and routing limit

The two revised demonstrations are template fixtures for the ANSWER branch. Their training `messages[:-1]` equal the output of the existing `build_messages()` for the saved source conversation, sections, and route decision. The full Qwen training rendering begins with the exact generation rendering; the only added text is the final assistant target and closing marker. `validate_grounded.py` checks this with the cached tokenizer and actual TRL collator. Neither fixture has a paid/independent AI acceptance review or frozen-test task clearance.

**The current router does not support these new task groups.** With the demos' user text and source-section fixtures, `retrieval.routing.route()` returns `clarify` for both `bookmark_site` and `mouse_pointer_size`, with the generic question “Which device and app are you using, and what would you like to do?” It classifies their intent as unknown, despite the Chrome/Windows facts in the requests. The official source pages are not in the active RAG corpus either. The saved `decision: answer` in demo provenance is explicitly a *template fixture*, not a claim that live retrieval/routing will make that decision.

Thus the **message-template mismatch is resolved**, while end-to-end inference for these examples and 500 diverse task groups remains unverified. Ryan can select training-eligible tasks, verify their official documents, decide whether each user request needs an answer or clarification from that evidence, and draft candidates with the unchanged `build_messages()` contract. An accepted candidate needs an independent review and frozen-test task-group clearance. The retrieval/routing owner can develop broader task coverage in parallel; it must be tested before using this dataset to claim live RAG performance. Do not hardcode the two demos, convert the evaluation-informed active corpus wholesale, or treat the source-checked demonstrations as deployed RAG coverage.
