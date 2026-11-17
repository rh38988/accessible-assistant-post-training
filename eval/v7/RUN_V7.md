# v7: one model call per verified step (inference change only)

Why: the v2 judge run showed that about 80% of the key actions SFT v2 + RAG missed were fully or partly in its retrieved notes, and that v6's checker rejected 7 of 15 answers that were still used. See `eval/analysis_v2/hypothesis_checks_v2.md`.

What changes from v6: nothing in retrieval, routing, the action plan, the base model, the adapter, or greedy decoding. Only the answer writing:

| Route | v6 | v7 |
|---|---|---|
| clarify | model writes the question | the router's question, word for word |
| answer with an action plan | one call with the whole plan; checker; 1 retry; used even if rejected | one short call per plan action ("rewrite this one instruction as one step"), plus an opening sentence and, if a retrieved sentence says how to tell it worked, one sentence about that; a fixed closing line |
| no plan / insufficient | one call | same one call |

Each model-written piece is checked (`grounded_steps.validate`): too long, a web address or number not in the plan or source, a dropped button name, wrong language. A failed piece is replaced by the plan's text (English) or the official source sentence (Traditional Chinese), so no verified step can be lost. Simplified characters are converted to Traditional with a small table. Every replacement is logged in the `.checks.jsonl` file.

Known limits: the closing line ("If something on your screen doesn't match these steps, tell me what you see") is the same for every answer with on-screen steps; plan text used as a fallback is plainer than ideal; tuned on the same 15 development scenarios as v6.

## 1. Generate (needs the v6 adapter and a GPU; Josh)

From the repository root, with the files from branch `share-rag-evidence-20261116` in `eval/outputs/`:

```powershell
$P = "eval/outputs/dev-sft-v2-rag-verified-action-plan-v6-20261115"
# check the prompts first, no model loaded
.\.venv\Scripts\python.exe -B eval/v7/generate_v7.py --v6-plan "$P.plan.json" --v6-outputs "$P.jsonl" --dry-run
# real run: 48 short model calls in total
.\.venv\Scripts\python.exe -B eval/v7/generate_v7.py --v6-plan "$P.plan.json" --v6-outputs "$P.jsonl" `
    --adapter "checkpoints/train-v2-ready-981-3ep-resume-9cf18be227b34b869f9ace4af7b56563" `
    --out eval/outputs/dev-sft-v2-rag-v7-20261116.jsonl
```

Writes the responses, `.checks.jsonl` (which pieces fell back and why) and `.summary.json` (hashes). Tests without a model: `python -m unittest eval/v7/test_grounded_steps.py -v`.

## 2. Judge (frozen rubric v2, same judge settings; whoever holds JUDGE_API_KEY)

```powershell
.\.venv\Scripts\python.exe -B eval/tools/run_llm_judge.py --eval-dir eval --rubric eval/rubric_v2_FROZEN.md `
    --prep eval/scenario_prep_v2.json --docs eval/judge_docs.json `
    --conditions sft_v2_rag_v7 --runs 2 --out eval/judge_out_v7
```

`--conditions` is new; without it the runner judges the original five, as before. v6 and plain RAG are not re-judged: their first-run judgments are reused.

## 3. Compare

```powershell
.\.venv\Scripts\python.exe -B eval/v7/compare_v7.py --v7-judge-out eval/judge_out_v7
```

Prints dimension means, overall, key-action coverage, A1/A2 failure rates, invented content, and paired v7-vs-v6 and v7-vs-RAG differences with bootstrap intervals. Report it as exploratory (15 development scenarios).
