# train_v2 handoff (Data Lead: Ryan Hsieh)

Status 2026-11-13: **frozen, 1,000 examples, English only (v2.0, "AI-screened, with human spot checks").** 17 examples were human-read; spot_check_v2.csv lists 50 more for you to read. 57 reserve examples are in train_v2_reserve.jsonl.

## Files
- `data/v2/train_v2_en.jsonl`: training file (existing schema; `training/train_sft.py` reads `messages` and trains on the last assistant turn)
- `data/v2/train_v2_en.manifest.json`: version, file SHA-256, per-example hashes
- `data/v2/SUMMARY_v2.md`: count funnel and distribution
- `data/v2/train_v2_index.csv`: every candidate with its decision, review rounds, source, and reason
- `data/v2/reviews/*.jsonl`: AI review records (required actions, gates, scores, evidence), kept separate from the training answers
- `data/v2/spot_check_v2.csv`: 50 stratified examples for the human spot check
- `data/v2/DATA_RUBRIC_v1.md`, `GENERATION_SPEC_v1.md`, `REVIEWER_INSTRUCTIONS_v1.md`: how the data was made and judged

## Run
```bash
python scripts/validate_data.py --kind train data/v2/train_v2_en.jsonl
sbatch --export=ALL,TRAIN_FILE=data/v2/train_v2_en.jsonl slurm/train_sft.slurm   # or pass --train-file to training/train_sft.py
python data/v2/tools/assemble.py --target 1000   # rebuild the frozen set from the review records
```

## How to describe it
"AI-screened, with human spot checks." Each example cites an official page; an independent reviewer agent checked it against that page with the rubric; flagged examples were revised and re-checked (at most two rounds). Only 17 examples were read in full by a person (the earlier verified set). The 3 Traditional Chinese verified examples are not in this English-only round.

## Open items
- Human spot check of `spot_check_v2.csv` (Ryan), then report the pass rate.
- 768-token cap was enforced as 2,200 characters; confirm with the Qwen tokenizer.
- Topics dropped because their official pages block automated reading: WhatsApp, Facebook (one older Facebook pilot task has a single example).

## Human spot check log (Ryan, 2026-11-13)
- 10 examples human-annotated so far, recorded in `spot_check_v2.csv` (reviewer = Ryan): keep tr012-e, tr014-r, tr025-e, tr035-e, tr040-e; fix tr028-r, tr038-c, tr048-a, tr048-d, tr049-a.
- The 5 fixes are not yet applied to `train_v2_en.jsonl`. The frozen file is unchanged.
- Target is 15 to 20 spot-checked examples across families, so 5 to 10 more are needed.
