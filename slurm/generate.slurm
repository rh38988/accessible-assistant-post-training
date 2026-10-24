#!/bin/bash
# Generate responses for all five conditions on Lonestar6. Submit from the repo root:
#     sbatch --export=ALL,ADAPTER=$WORK/accessible-assistant/adapters/pilot slurm/generate.slurm
# Run only some conditions:
#     sbatch --export=ALL,CONDITIONS="prompt fewshot rag" slurm/generate.slurm

#SBATCH -J generate
#SBATCH -o slurm/logs/%x-%j.out
#SBATCH -e slurm/logs/%x-%j.err
#SBATCH -p gpu-a100-small
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 01:00:00
#SBATCH -A CDA26008

set -euo pipefail

SCENARIOS=${SCENARIOS:-eval/scenarios/sample.jsonl}
CONDITIONS=${CONDITIONS:-"prompt fewshot rag sft sft_rag"}
ADAPTER=${ADAPTER:-}
VENV=${VENV:-$WORK/inf385t/venv}

source "$VENV/bin/activate"
export HF_HOME=$WORK/hf_cache
export HF_HUB_OFFLINE=1
mkdir -p slurm/logs eval/outputs

python scripts/validate_data.py --kind scenario $SCENARIOS

for COND in $CONDITIONS; do
    echo "=== $COND ==="
    EXTRA=""
    if [[ $COND == sft* ]]; then
        if [[ -z "$ADAPTER" ]]; then
            echo "Skipping $COND: set ADAPTER=<path>"
            continue
        fi
        EXTRA="--adapter $ADAPTER"
    fi
    python eval/generate.py --condition $COND --scenarios $SCENARIOS \
        --out eval/outputs/$COND.jsonl $EXTRA
done

echo "Done at $(date)"
