#!/bin/bash
# Generate original, prompt, and sft responses on Lonestar6. Submit from the repo root:
#     sbatch --export=ALL,ADAPTER=$WORK/accessible-assistant/adapters/pilot slurm/generate.slurm
# Run only some conditions:
#     sbatch --export=ALL,CONDITIONS="original prompt" slurm/generate.slurm

#SBATCH -J generate
#SBATCH -o slurm/logs/%x-%j.out
#SBATCH -e slurm/logs/%x-%j.err
#SBATCH -p gpu-a100-small
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 01:00:00
#SBATCH -A CDA26008

set -euo pipefail

SCENARIOS=${SCENARIOS:-eval/scenarios/eval_v1.jsonl}
CONDITIONS=${CONDITIONS:-"original prompt sft"}
MAX_NEW_TOKENS=${MAX_NEW_TOKENS:-768}
ADAPTER=${ADAPTER:-}
VENV=${VENV:-$WORK/inf385t/venv}

# Check the requested conditions before starting any model generation.
for COND in $CONDITIONS; do
    case "$COND" in
        original|prompt) ;;
        sft)
            if [[ -z "$ADAPTER" ]]; then
                echo "sft requires ADAPTER=<path>" >&2
                exit 1
            fi
            ;;
        *) echo "Unknown condition: $COND" >&2; exit 1 ;;
    esac
done

source "$VENV/bin/activate"
export HF_HOME=$WORK/hf_cache
export HF_HUB_OFFLINE=1
mkdir -p slurm/logs eval/outputs

python scripts/validate_data.py --kind scenario "$SCENARIOS"

for COND in $CONDITIONS; do
    echo "=== $COND ==="
    EXTRA=()
    if [[ $COND == sft ]]; then
        EXTRA=(--adapter "$ADAPTER")
    fi
    python eval/generate.py --condition "$COND" --scenarios "$SCENARIOS" \
        --max-new-tokens "$MAX_NEW_TOKENS" \
        --out "eval/outputs/$COND.jsonl" "${EXTRA[@]}"
done

echo "Done at $(date)"
