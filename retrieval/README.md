# Retrieval

Owner: **Data Lead** (owns the source documents)

`bm25.py` is a small keyword retriever used by two conditions:

- `rag`: accessibility prompt + retrieved docs (baseline 3)
- `sft_rag`: fine-tuned model + the **same** retrieved docs

Both conditions get identical retrieved text, so any difference between them comes from training, not from the documents.

## What the corpus needs to cover

Retrieval is used at **evaluation** time (`rag` and `sft_rag`), so the docs must cover the **eval tasks** in `eval/tasks/eval_tasks.csv`. The current docs mostly cover pilot training tasks, so add summaries for the eval tasks before running the RAG conditions. Adding eval-task docs here is fine: they are never used for training.

## Adding documents

1. Save each support page as a `.md` or `.txt` file in `docs/`.
2. Put two header lines at the top:
   ```
   Source: <url>
   Accessed: YYYY-MM-DD
   ```
3. Below the header, **summarize the steps in your own words**. Don't paste the page: support pages are copyrighted, and short summaries also retrieve better.
4. Keep exact menu and button names (e.g. **Display & Brightness**); those need to match the screen.

## Try it

```bash
python retrieval/bm25.py "how do I make text bigger on iphone"
```
