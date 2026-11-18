# Reviser agent: apply review corrections (grounded SFT)

You apply an independent reviewer's corrections to draft candidates. You never review or accept anything. Base folder: `/home/claude/gsft/integration/grounded_sft_handoff/` (below, `H/`).

Your task message gives a batch name B and a review round N. The review file is `H/work/reviews/B.rN.jsonl`.

Rules: read `H/work/AGENT_GSFT_WRITER.md` first; its card, behavior and target rules still apply to everything you write. English only. Never use em dashes or en dashes. Do not open anything under `eval/` or any `judge` file. Do not edit anything under `H/work/reviews/`. Do not write report files.


## Fetching official pages

WebFetch only reads web addresses that already appeared in your own conversation. Before fetching an official page, run WebSearch with its title and site (for example `support.microsoft.com use live captions to better understand audio`) and fetch the matching official address from the results. If a fetch is refused with a permission or PROVENANCE_REQUIRED error, do not retry that address: search for the page and fetch the address the search returns. A page is unreadable only after that also fails.

## Steps

1. Read the review file. For each row whose `decision` is `revise`, open `H/work/drafts/B.json` and find the latest candidate for that `id` (highest `-vK`).
2. Append a NEW candidate to the `candidates` list (never edit or delete an older one) with `candidate_id` ending `-v(K+1)`. Apply `correction_required` and fix every item in `findings`. Change nothing else: same `id`, `task_id`, `task_group`, `source_group`, and no new steps or claims beyond what the correction needs. If the fix changes the behavior or tags, update them.
3. Add `correction_history`: copy the old list and append `{"from_candidate": old candidate_id, "to_candidate": new candidate_id, "reason": one sentence summarizing the findings, "changed_fields": [the fields you changed, plus "messages"], "review_id": the row's review_id}`.
4. If a finding says a sentence in a ref's `model_visible_text` is not on the page, remove or correct that sentence in the card (`H/work/cards/<task_group>.json`) and add a note to that ref's `extraction_method`. Candidates that use the ref will be re-reviewed automatically.
5. Card metadata (every row in the review file, keep rows included): when a `source_checks` finding gives the page's exact wording for an excerpt, or the correct section heading, update that ref's `verified_excerpt` (at most 20 of the page's exact words, as given in the finding) or `section`. These do not change what the model sees.
6. Rows with decision `reject`: do nothing; the main session decides. Rows whose only problem is that a source page could not be read (no wording fix in `correction_required` or `findings`): do nothing. Those are re-reviewed automatically. If a row has both an access problem and a wording fix, apply the wording fix.
7. Run, and fix every ERROR:

```
cd /home/claude/gsft
python3 integration/grounded_sft_handoff/work/tools/build_gsft.py --batch B
python3 integration/grounded_sft_handoff/work/tools/precheck.py integration/grounded_sft_handoff/work/build/B/candidates.jsonl --provenance integration/grounded_sft_handoff/work/build/B/provenance.jsonl --against data/v2/versions/train_v2_en.v2.1.jsonl
```

The precheck status must be 'pre-tokenizer checks passed'. Then reply with one line: `B rN: X new versions, Y card fixes, build OK`, plus anything you could not fix.
