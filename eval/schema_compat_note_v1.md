# schema_v1 migration history

On 2026-10-26, a conversion adapter was proposed to bridge schema_v1 and the legacy evaluation fields.

Native schema_v1 support replaced that adapter in `eval/generate.py` and `scripts/validate_data.py --kind scenario`. The obsolete `eval/tools/schema_v1_adapter.py` file has been removed. Generation and validation read `eval/scenarios/eval_v1.jsonl` directly; no compatibility file is needed.

The active generation conditions are `original`, `prompt`, and `sft`. See [the evaluation README](README.md) for current validation and dry-run instructions.

`eval/make_rating_sheet.py` and `eval/analyze.py` still need native schema_v1 support. The regression test in `eval/test_generate.py` continues to prevent generation from importing the removed adapter.
