#!/bin/bash
# LoRA SFT job for TACC Lonestar6. Submit from the repo root on the login node:
#     sbatch slurm/train_sft.slurm
# Override the data or run name without editing:
#     sbatch --export=ALL,TRAIN_FILE=data/train/all.jsonl,RUN_NAME=full-v1 slurm/train_sft.slurm
#
# Billing reminder: every job is billed at least the minimum, so test small
# things interactively (idev) and submit real runs as batch jobs.

#SBATCH -J sft-lora
#SBATCH -o slurm/logs/%x-%j.out
#SBATCH -e slurm/logs/%x-%j.err
#SBATCH -p gpu-a100-small       # 1 A100; check queue names with `sinfo` if this fails
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 01:00:00
#SBATCH -A CDA26008

set -euo pipefail

# ---- Settings (override with --export) ----
TRAIN_FILE=${TRAIN_FILE:-data/pilot/sample.jsonl}
RUN_NAME=${RUN_NAME:-pilot}
VENV=${VENV:-$WORK/inf385t/venv}
OUT_DIR=$WORK/accessible-assistant/adapters/$RUN_NAME

# ---- Environment ----
source "$VENV/bin/activate"
export HF_HOME=$WORK/hf_cache      # same cache the login-node download used
export HF_HUB_OFFLINE=1            # fail fast instead of downloading on a compute node
mkdir -p slurm/logs "$OUT_DIR"

echo "Job $SLURM_JOB_ID on $(hostname) at $(date)"
nvidia-smi --query-gpu=name,memory.total --format=csv
python scripts/validate_data.py --kind train $TRAIN_FILE

python training/train_sft.py \
    --train-file $TRAIN_FILE \
    --output-dir "$OUT_DIR"

echo "Finished at $(date). Adapter: $OUT_DIR"
