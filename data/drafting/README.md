# Drafting specs (train v1)

These files were used to **draft** `data/train/batch_0*.jsonl`. They are kept for transparency, so anyone can see exactly how each example was produced.

- `sources.py`: every official page used, with title and URL (all accessed 2026-10-24)
- `batch_0*.py`: one spec per training task (TR-021 to TR-116)
- `build.py`: expands each spec into 4 examples

```bash
python data/drafting/build.py . batch_01 batch_02 batch_03 batch_04 batch_05   # run from repo root
```

## How one spec becomes 4 examples

| Suffix | Conversation | Label |
|---|---|---|
| `-a` | fully specified question -> steps | fully_specified |
| `-b` | vague question -> one clarifying question | underspecified |
| `-c` | OATS-style message (verbose, over-specified, incomplete) -> steps, or a clarifying question if it can't be answered | depends |
| `-d` | vague question -> clarify -> user answers -> steps | fully_specified |

Examples `-a`, `-c` (when answerable), and `-d` share the same steps on purpose, so the instructions for a task stay consistent. Reviewers may reword them to add variety.

## After review starts

**Edit the JSONL files directly.** Do not rerun `build.py` once anyone has edited the JSONL, or those edits will be overwritten.
