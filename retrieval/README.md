# Retrieval

Owner: **Data Lead** (owns the source documents)

`bm25.py` is a small keyword retriever used by two conditions:

- `rag`: accessibility prompt + retrieved docs (baseline 3)
- `sft_rag`: fine-tuned model + the **same** retrieved docs

Both conditions get identical retrieved text, so any difference between them comes from training, not from the documents.

## Adding documents

1. Save each support page as a `.md` or `.txt` file in `docs/`.
2. Put two header lines at the top:
   ```
   Source: <url>
   Accessed: YYYY-MM-DD
   ```
3. Paste the relevant text below (instructions only, no menus or ads).
4. Delete the `sample_*.md` placeholder files once real documents are in.

## Try it

```bash
python retrieval/bm25.py "how do I make text bigger on iphone"
```
