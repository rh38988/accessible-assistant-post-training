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
3. Below the header, **summarize the steps in your own words**. Don't paste the page: support pages are copyrighted, and short summaries also retrieve better.
4. Keep exact menu and button names (e.g. **Display & Brightness**); those need to match the screen.

## Try it

```bash
python retrieval/bm25.py "how do I make text bigger on iphone"
```
