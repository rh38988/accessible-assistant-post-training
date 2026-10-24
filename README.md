# Post-Training a Small Language Model for Accessible Digital Assistance

LoRA supervised fine-tuning of **Qwen2.5-3B-Instruct** so that clear, step-by-step, low-jargon tech help (for older adults and other less tech-confident users) becomes the model's default behavior, without needing a detailed prompt.

## Research question

Does post-training beat strong prompting baselines at giving accessible tech guidance?

**Primary metric:** % of responses rated *acceptable* (passes all four core criteria: clarity, actionability, completeness, factual correctness).

**Decision rule:** post-training is justified only if a post-trained condition beats the strongest prompting baseline by **at least 10 percentage points** with a **paired McNemar test p < 0.05**.

**Clarification is scored both ways:** guessing when the request is missing details, and asking when it isn't.

## Conditions

| Condition | What it is |
|---|---|
| `prompt` | Accessibility system prompt (baseline 1) |
| `fewshot` | Prompt + demonstrations (baseline 2) |
| `rag` | Prompt + retrieved support docs (baseline 3) |
| `sft` | LoRA fine-tuned model, no system prompt |
| `sft_rag` | Fine-tuned model + the same retrieved docs |

## Repository layout

```
data/            training examples (JSONL) and schema         -> Data Lead
  pilot/         first ~50 examples
  train/         full set (~1,000)
retrieval/       BM25 retriever + support docs                -> Data Lead
training/        LoRA SFT script                              -> Training Lead
eval/            scenarios, prompts, generation, rating, analysis -> Evaluation Lead
slurm/           Lonestar6 batch jobs                         -> Training Lead
scripts/         data validator, model download
```

Each folder has its own README with details.

## Setup

### Lonestar6 (TACC)

On the **login node** (`login1.ls6` prompt):

```bash
cd $WORK
git clone https://github.com/rh38988/accessible-assistant-post-training.git
cd accessible-assistant-post-training

# Reuse the course venv (already has torch + transformers), add the rest
source $WORK/inf385t/venv/bin/activate
pip install -r requirements.txt

# Download the base model once, on the login node
export HF_HOME=$WORK/hf_cache
python scripts/download_model.py
```

Then submit jobs from the repo root:

```bash
sbatch slurm/train_sft.slurm                         # pilot training run
sbatch --export=ALL,ADAPTER=$WORK/accessible-assistant/adapters/pilot slurm/generate.slurm
squeue -u $USER                                       # check status
```

### Local (laptop)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install torch && pip install -r requirements.txt
```

The data validator, retriever, rating-sheet builder, and analysis script use only the Python standard library, so they run without installing anything.

## Workflow

1. **Data:** write examples in `data/pilot/`, then `python scripts/validate_data.py --kind train data/pilot/*.jsonl`
2. **Scenarios:** write held-out scenarios in `eval/scenarios/`, validate with `--kind scenario`
3. **Inspect prompts:** `python eval/generate.py --condition rag --scenarios eval/scenarios/sample.jsonl --out /dev/null --dry-run`
4. **Train:** `sbatch slurm/train_sft.slurm`
5. **Generate:** `sbatch slurm/generate.slurm` (all five conditions)
6. **Rate:** `python eval/make_rating_sheet.py --scenarios ...`, two raters fill in copies
7. **Analyze:** `python eval/analyze.py ...` (see `eval/README.md`)

## Team conventions

- Validate data before every commit.
- Don't commit model weights, adapters, or `eval/ratings/key*.csv` (already in `.gitignore`).
- Everything under `sample*` is a placeholder. Replace it with real, cited material before experiments.
- Sensitive tasks (payments, passwords, privacy, scams, account recovery) need a second reviewer.

## References

- Yang, A., et al. (2025). Qwen2.5 Technical Report. arXiv:2412.15115.
- Hu, E. J., et al. (2022). LoRA: Low-Rank Adaptation of Large Language Models. ICLR.
- Ko, E. G., Nanayakkara, S., & Huff, E. W., Jr. (2025). Empowering Older Adults through GenAI Literacy. CHI EA.
- Hugging Face [PEFT](https://github.com/huggingface/peft) and [TRL](https://github.com/huggingface/trl)
