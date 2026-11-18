# Grounded SFT checkpoint development handoff — 2026-11-18

## Scope and status

**Ready for offline evaluation, with no epoch selected.** This comparison uses the 13 English user conversations in `eval/scenarios/eval_v1.jsonl`; the two Traditional Chinese conversations were left out. The reserved final test set was not opened or run. No expected elements, evaluation labels, rubric scores, or earlier answers were sent to retrieval, routing, or the model.

The [shared plan](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.shared-plan.json) was built once from only each scenario's ID and user-role conversation. It freezes one `HybridRetriever(k=3)` result, one routing decision, and one ordinary SFT v2 + RAG model input per case. All four conditions use those same 13 input-message and rendered-input SHA256 values, corpus manifest SHA256 `98ba12590680b3f0576083c84187a5570e234111c0f658b38b5b986cafa0e501`, cached Qwen2.5-3B-Instruct revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`, bf16/SDPA on CUDA, seed 42, and greedy `max_new_tokens=768` (`do_sample=False`). Prompt input lengths range from 193 to 630 tokens. There is no checklist, action-plan, realization, or checker prompt.

The ordinary generation path sends two messages: system instructions plus retrieved reference passages for ANSWER (or the router's exact question for CLARIFY), then the joined user turns. The model generates every response, including all clarifications. The router supplies the **decision and question**, not a response emitted directly to the user. Each output row records `response_origin=model_generated`, `router_decision`, `router_question` where applicable, and whether the response exactly matches that question. There are eight ANSWER and five CLARIFY cases.

## Baseline reuse

The 15-row [`dev-sft-v2-rag-20261115.jsonl`](../../../eval/outputs/dev-sft-v2-rag-20261115.jsonl) was reduced to the same 13 English IDs in a **new** baseline file. Reuse was allowed only after exact comparison of the current shared plan with the saved baseline plan: scenario-file hash, corpus hash, model/revision, adapter path, decoding settings, routing decisions, complete retrieved passages, and model-visible messages all matched for the 13 IDs. Each prior response's prompt hash, evidence hash, route, 768-token setting, and adapter path also matched. The original SFT v2 adapter's current weights hash (`7331fb9a7d5f0b947a4ddd88602b37ea80256d5c888a21ce2a2037c526aa06fb`) matches its completed training receipt; the old baseline plan recorded its path but did not separately record the adapter-weight hash. The baseline response text and token counts were copied, not regenerated.

## Files for the evaluation owner

| Condition | Response file | Adapter identity | Responses | Total generated tokens | Longest | 768-token hits |
|---|---|---|---:|---:|---:|---:|
| Original SFT v2 | [`sft-v2.jsonl`](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.sft-v2.jsonl) | completed 981-example adapter | 13 | 872 | 167 | 0 |
| Grounded epoch 1 | [`grounded-ep1.jsonl`](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.grounded-ep1.jsonl) | `checkpoint-250` | 13 | 863 | 202 | 0 |
| Grounded epoch 2 | [`grounded-ep2.jsonl`](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.grounded-ep2.jsonl) | `checkpoint-500` | 13 | 665 | 117 | 0 |
| Grounded epoch 3 | [`grounded-ep3.jsonl`](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.grounded-ep3.jsonl) | `checkpoint-750` | 13 | 747 | 142 | 0 |

The [side-by-side CSV](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.comparison.csv) contains the four response texts and token counts per scenario, the route and router question, and the shared input/evidence hashes. The [machine-readable summary](../../../eval/outputs/grounded-sft-dev13-20261118-9e4dbed2.summary.json) records the full adapter-weight SHA256 values, scenario IDs, source hashes, settings, length-limit hits, and each output's SHA256. The shared plan includes the actual retrieved passages and model-visible messages. New files were used throughout; the 2026-11-15 outputs were preserved.

All 52 outputs ended with EOS. The original SFT v2 responses exactly match the router question in four of five CLARIFY cases; each grounded checkpoint matches in five of five. Relative to the original baseline, each grounded checkpoint has nine response-text differences (the eight ANSWER cases plus one CLARIFY case). These are descriptive comparisons, **not** quality scores or evidence that one epoch is best. The evaluation owner should review source-grounded action coverage, explicit user constraints, unsupported instructions, safety, and clarification behavior using the existing development rubric, keeping ANSWER and CLARIFY cases separate. The checkpoint comparison should remain a development decision; do not use the reserved final test set to choose an epoch.

## Reproduction and verification

The controlled runner is [`eval/compare_grounded_sft_dev.py`](../../../eval/compare_grounded_sft_dev.py). It uses `eval.generate_rag.prepare` and `eval.generate.generation_kwargs`; it loads one adapter from the base model per condition and reads the frozen plan during generation. It refuses to overwrite a plan, partial output, or final output. The 13-case plan and all four output files were checked for identical scenario order, route, prompt hash, rendered-input hash, evidence hash, corpus hash, and input-token count. All generated token counts are at most 768, and no output has `hit_length_limit=true`. The baseline reuse decision and exact comparison reasons are in the shared plan.

One preparation attempt failed before writing a plan because this Transformers build tried an online model-metadata request during cached-tokenizer loading. The successful preparation and all three GPU generations ran with `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`; the failed attempt did not create an output. A second preparation attempt exposed a read helper that expected scenario records; that helper was corrected before the successful plan was written. Logs of these attempts and generation runs are in this receiving directory.

No model retraining, paid judge, evaluation scoring, frozen-test modification, commit, or push occurred.
