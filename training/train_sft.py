"""LoRA supervised fine-tuning (SFT) of Qwen2.5-3B-Instruct.

Owner: Training Lead

What this script does, step by step:
1. Loads training examples (schema in data/README.md).
2. Converts each example into a "prompt" (all messages except the last) and
   a "completion" (the last assistant message).
3. Trains LoRA adapters with TRL's SFTTrainer. With prompt-completion data,
   TRL computes the loss ONLY on the completion tokens, so the model learns
   to write the reply, not to copy the user's message.
4. Saves the LoRA adapter (a few hundred MB at most, not the full model).

No system message is added: the Qwen chat template then inserts its own
default system line, and generate.py does the same for the `sft` condition,
so training and evaluation see the same format.

Example (pilot run):
    python training/train_sft.py \
        --train-file data/pilot/sample.jsonl \
        --output-dir $WORK/accessible-assistant/adapters/pilot
"""
import argparse
import json
import random
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTConfig, SFTTrainer


def load_jsonl(paths):
    rows = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            rows.extend(json.loads(line) for line in f if line.strip())
    return rows


def to_prompt_completion(example):
    """Split a conversation into context (prompt) and the reply to learn (completion)."""
    messages = example["messages"]
    return {"prompt": messages[:-1], "completion": [messages[-1]]}


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--train-file", nargs="+", required=True, help="One or more .jsonl files")
    p.add_argument("--output-dir", required=True)
    p.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
    # Validation split is only for watching the loss during training.
    # The real held-out evaluation uses eval/scenarios/, never these examples.
    p.add_argument("--val-fraction", type=float, default=0.1)
    p.add_argument("--epochs", type=float, default=3)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--grad-accum", type=int, default=4, help="Effective batch = batch-size x grad-accum")
    p.add_argument("--max-length", type=int, default=2048, help="Longer examples are truncated")
    # LoRA settings: r = adapter rank (capacity), alpha = scaling, dropout = regularization.
    p.add_argument("--lora-r", type=int, default=16)
    p.add_argument("--lora-alpha", type=int, default=32)
    p.add_argument("--lora-dropout", type=float, default=0.05)
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def main():
    args = parse_args()
    random.seed(args.seed)

    # ---- Data ----
    examples = load_jsonl(args.train_file)
    random.shuffle(examples)
    n_val = int(len(examples) * args.val_fraction)
    val_rows = [to_prompt_completion(e) for e in examples[:n_val]]
    train_rows = [to_prompt_completion(e) for e in examples[n_val:]]
    print(f"Train examples: {len(train_rows)}  Validation examples: {len(val_rows)}")
    train_ds = Dataset.from_list(train_rows)
    val_ds = Dataset.from_list(val_rows) if val_rows else None

    # ---- Model ----
    # bf16 halves memory and is supported on A100s. Fall back to fp32 elsewhere.
    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    dtype = torch.bfloat16 if use_bf16 else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype)

    # LoRA: freeze the base model and train small low-rank matrices added to
    # every linear layer ("all-linear"). Only these adapters are saved.
    lora = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules="all-linear",
        task_type="CAUSAL_LM",
    )

    config = SFTConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        max_length=args.max_length,
        completion_only_loss=True,      # loss on the reply only (see docstring)
        gradient_checkpointing=True,    # trades some speed for much less GPU memory
        bf16=use_bf16,
        logging_steps=5,
        eval_strategy="epoch" if val_ds is not None else "no",
        save_strategy="epoch",
        save_total_limit=1,
        report_to="none",
        seed=args.seed,
    )

    trainer = SFTTrainer(
        model=model,
        args=config,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        processing_class=tokenizer,
        peft_config=lora,
    )
    trainer.train()

    # ---- Save ----
    trainer.save_model(args.output_dir)  # saves the LoRA adapter + config
    tokenizer.save_pretrained(args.output_dir)
    Path(args.output_dir, "train_args.json").write_text(json.dumps(vars(args), indent=2))
    print(f"Saved adapter to {args.output_dir}")


if __name__ == "__main__":
    main()
