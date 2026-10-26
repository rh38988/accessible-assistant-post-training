# schema_v1 compatibility note (for Shirley and the team)

2026-10-26. **Short answer: the current pipeline cannot load `eval/scenarios/eval_v1.jsonl` as it stands.** Nothing in the shared repo was modified. The proposals below are untested against the real scripts except where stated.

## 1. What was run, and what was only read

| Item | Status |
|---|---|
| `scripts/validate_data.py --kind scenario` on `eval_v1.jsonl` | **Executed** on a verbatim copy of the file as read from `main`. Result: 15 errors, every record `missing fields ['turns', 'specification', 'category', 'language', 'sensitive']` (the validator then returns early, so it never looks at `prompt`). |
| Field accesses in `generate.py`, `make_rating_sheet.py`, `analyze.py` | **Simulated** (the exact lookups, not the scripts). `scenario["turns"]` and `scenarios[s]["specification"]` and `["sensitive"]` raise `KeyError`. `sc.get("notes_for_raters", "")` does not fail, it silently returns an empty string. |
| `generate.py --dry-run`, `make_rating_sheet.py`, `analyze.py` themselves | **Not executed** (no checkout). Conclusions come from reading their code. |
| Adapter output through the validator | **Executed.** The converted copy passes (`Records: 15 … OK: no errors`). |

## 2. Exact incompatibilities

| File (path in repo) | Reads | schema_v1 has | Effect on `eval_v1.jsonl` |
|---|---|---|---|
| `scripts/validate_data.py` (`REQUIRED["scenario"]`, `check_record`) | `turns`, `specification`, `category`, `language`, `sensitive` | `prompt`, `clarification_required`, `task_family`, `risk_level`; no `language` | Fails with "missing fields". Also `--kind` only accepts `train` or `scenario`. |
| `eval/generate.py` (`build_messages`, `build_all`) | `scenario["turns"]` (messages sent to the model; the RAG query joins user turns) | `prompt` | `KeyError: 'turns'`. Only `turns` is sent to the model, so `expected_elements` would **not** leak into the prompt once mapped. |
| `eval/make_rating_sheet.py` | `sc["turns"]`, `sc.get("notes_for_raters")` | `prompt`, `expected_elements` | `KeyError: 'turns'`. Raters would otherwise get an empty notes column. |
| `eval/analyze.py` | `scenarios[s]["specification"]` (guess and over-clarification rates), `scenarios[s]["sensitive"]` (sensitive-task acceptable rate) | `clarification_required`, `risk_level` | `KeyError`. |
| `slurm/generate.slurm` | Runs `python scripts/validate_data.py --kind scenario $SCENARIOS` under `set -euo pipefail`, and defaults `SCENARIOS` to `eval/scenarios/sample.jsonl` | n/a | The job **aborts** at validation on a schema_v1 file. The default points at `sample.jsonl`, whose `sc-0002` is a training task. |
| `eval/README.md`, `data/README.md` | Describe `turns`, `notes_for_raters`, 40% underspecified | n/a | Documentation drift only. |

## 3. Minimal proposed approach (needs approval)

Keep `eval_v1.jsonl` as the only source of truth in schema_v1. Add one small, one-way adapter so that the **unmodified** scripts can read a derived copy.

Delivered, not yet in the repo: `eval/tools/schema_v1_adapter.py`.

| schema_v1 field | Derived field | Rule |
|---|---|---|
| `prompt` | `turns` | copied |
| `clarification_required` | `specification` | true gives `underspecified`, false gives `fully_specified` |
| `task_family` | `category` | Smartphone Basics gives `technical_support`; Communication gives `communication`; Online Safety and Scam Prevention gives `online_services` |
| `risk_level` | `sensitive` | `low` gives false; `medium` or `high` gives true |
| user-turn text | `language` | `zh-TW` if any CJK character, else `en` |
| `expected_elements` | `notes_for_raters` | joined into one string |
| `id`, `platform` | same | copied |

Derived counts on `eval_v1.jsonl` (checked): `underspecified` 5, `fully_specified` 10; `sensitive` true 5, false 10; `zh-TW` 2, `en` 13.

Commands for Shirley (from the repo root, after the files are merged; not executed on the real scripts):

```bash
python eval/tools/validate_eval_v1.py eval/scenarios/eval_v1.jsonl                       # schema_v1 check (executed here, passes)
python eval/tools/schema_v1_adapter.py eval/scenarios/eval_v1.jsonl eval/scenarios/eval_v1.repo_compat.jsonl
python scripts/validate_data.py --kind scenario eval/scenarios/eval_v1.repo_compat.jsonl   # executed here on a verbatim copy, passes
python eval/generate.py --condition prompt --scenarios eval/scenarios/eval_v1.repo_compat.jsonl --out /dev/null --dry-run   # NOT executed: check prompts first
sbatch --export=ALL,SCENARIOS=eval/scenarios/eval_v1.repo_compat.jsonl,CONDITIONS="prompt fewshot rag" slurm/generate.slurm
```

Keep `eval_v1.repo_compat.jsonl` out of version control (or mark it generated). It is a derived file.

## 4. What must change before the baseline run

1. **Pass the converted file**, not `eval_v1.jsonl`, to `generate.py`, `make_rating_sheet.py` and `analyze.py` (all three read `--scenarios`).
2. **Do not run the default `SCENARIOS`** in `slurm/generate.slurm`. It points at `sample.jsonl` and would score a training task.
3. **`make_rating_sheet.py` shows `notes_for_raters` to raters.** With the adapter, that column now holds the `expected_elements`. Raters seeing them is intended. The model never sees them (`generate.py` sends only `turns`).
4. **RAG baseline (`rag`, `sft_rag`) needs docs for these 15 tasks** in `retrieval/docs/` (Data Lead). The current docs cover training topics (`retrieval/README.md`), so `rag` would retrieve unrelated text.
5. **Rating-sheet integrity:** `make_rating_sheet.py` overwrites `key.csv` each run and reads every file in `eval/outputs/`. Run it once, only after all five condition outputs exist, and back up `key.csv` privately.
6. **Language field:** analysis by language (zh-TW vs en) is only possible through the adapter's derived `language`. `schema_v1` itself carries none.

## 5. Questions for team approval

1. May the repo gain `eval/tools/schema_v1_adapter.py` and `eval/tools/validate_eval_v1.py`, or should the existing scripts be updated to read schema_v1 natively (a larger change to Training Lead and Data Lead files)?
2. Is the mapping in section 3 acceptable, especially `risk_level` to `sensitive` (medium counts as sensitive) and `task_family` to `category`?
3. Should schema_v1 gain a `language` field? Without it, zh-TW cannot be reported from the primary file.
4. Should the README target of 40% underspecified be applied to the eval set? It is 33% here (5 of 15) by design.
5. Is it acceptable to show `expected_elements` to raters? It replaces `notes_for_raters`.
6. Who updates `eval/README.md` and `data/README.md` so they stop describing `turns`?

## 6. Repository write access

I had no checkout and no credentials, so **no branch was created and nothing was committed**. When you are ready, from a clone:

```bash
git checkout -b eval/eval-v1-schema-v1
# copy in: eval/scenarios/eval_v1.jsonl, eval/overlap_report_v1.md, eval/eval_v1_review.md,
#          eval/schema_compat_note_v1.md, eval/tools/*.py
python eval/tools/validate_eval_v1.py eval/scenarios/eval_v1.jsonl
git add eval/ && git commit -m "Add eval_v1 (schema_v1, 15 pilot scenarios) and reports"
git push -u origin eval/eval-v1-schema-v1
```
