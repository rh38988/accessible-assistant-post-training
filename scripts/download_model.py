"""Download the base model into the Hugging Face cache.

Run this on the TACC LOGIN node (compute nodes may not have internet):

    export HF_HOME=$WORK/hf_cache
    python scripts/download_model.py

Why HF_HOME and not cache_dir: snapshot_download and from_pretrained both
read HF_HOME and use the same hub/ layout under it. Passing an explicit
cache_dir in one place but not the other can make the job look for files in
a different layout and re-download. Set HF_HOME once, use it everywhere.
"""
import argparse
import os

from huggingface_hub import snapshot_download

parser = argparse.ArgumentParser()
parser.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
args = parser.parse_args()

if "HF_HOME" not in os.environ:
    print("Warning: HF_HOME is not set; using the default ~/.cache/huggingface")

path = snapshot_download(repo_id=args.model)
print(f"Downloaded {args.model} to {path}")
