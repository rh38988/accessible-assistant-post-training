"""Generate model responses for one experimental condition.

Owner: Training Lead runs it; Evaluation Lead uses the outputs.

Five conditions (see README):
    prompt   : accessibility system prompt                      (baseline 1)
    fewshot  : system prompt + demonstrations                   (baseline 2)
    rag      : system prompt + retrieved docs                   (baseline 3)
    sft      : fine-tuned model, no system prompt               (post-trained)
    sft_rag  : fine-tuned model + the same retrieved docs       (post-trained + retrieval)

Every condition answers the SAME scenarios. For multi-turn scenarios the
earlier turns are fixed; the model only writes the final reply.
Decoding is greedy (no sampling), so reruns give the same output.

Example:
    python eval/generate.py --condition rag \
        --scenarios eval/scenarios/sample.jsonl \
        --out eval/outputs/rag.jsonl

    python eval/generate.py --condition sft --adapter $WORK/accessible-assistant/adapters/pilot \
        --scenarios eval/scenarios/sample.jsonl --out eval/outputs/sft.jsonl
"""
import argparse
import json
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from retrieval.bm25 import BM25Retriever, format_context  # noqa: E402

CONDITIONS = {
    #           system prompt?  demos?  retrieval?  adapter?
    "prompt":  dict(system=True,  fewshot=False, rag=False, adapter=False),
    "fewshot": dict(system=True,  fewshot=True,  rag=False, adapter=False),
    "rag":     dict(system=True,  fewshot=False, rag=True,  adapter=False),
    "sft":     dict(system=False, fewshot=False, rag=False, adapter=True),
    "sft_rag": dict(system=False, fewshot=False, rag=True,  adapter=True),
}

RAG_HEADER = (
    "Reference documentation (may be incomplete or out of date; "
    "use it only if it matches the user's device and situation):"
)


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def build_messages(scenario, cond, system_prompt, demos, retriever, top_k):
    """Assemble the exact chat the model sees for one scenario."""
    system_parts, retrieved = [], []
    if cond["system"]:
        system_parts.append(system_prompt)
    if cond["rag"]:
        # Query with everything the user has said so far.
        query = " ".join(t["content"] for t in scenario["turns"] if t["role"] == "user")
        retrieved = retriever.search(query, k=top_k)
        if retrieved:
            system_parts.append(RAG_HEADER + "\n\n" + format_context(retrieved))

    messages = []
    if system_parts:
        messages.append({"role": "system", "content": "\n\n".join(system_parts)})
    if cond["fewshot"]:
        for d in demos:
            messages.extend(d["messages"])
    messages.extend(scenario["turns"])
    return messages, [r["doc"] for r in retrieved]


def build_all(args):
    """Build every prompt first (no GPU needed). Use --dry-run to inspect them."""
    cond = CONDITIONS[args.condition]
    system_prompt = Path(args.system_prompt).read_text(encoding="utf-8").strip()
    demos = load_jsonl(args.demos) if cond["fewshot"] else []
    retriever = BM25Retriever(args.docs) if cond["rag"] else None
    built = []
    for sc in load_jsonl(args.scenarios):
        messages, docs = build_messages(sc, cond, system_prompt, demos, retriever, args.top_k)
        built.append((sc, messages, docs))
    return built


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--condition", choices=CONDITIONS, required=True)
    p.add_argument("--scenarios", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
    p.add_argument("--adapter", help="LoRA adapter folder (required for sft and sft_rag)")
    p.add_argument("--system-prompt", default=str(REPO / "eval/prompts/system_prompt.txt"))
    p.add_argument("--demos", default=str(REPO / "eval/prompts/demonstrations.jsonl"))
    p.add_argument("--docs", default=str(REPO / "retrieval/docs"))
    p.add_argument("--top-k", type=int, default=3)
    p.add_argument("--max-new-tokens", type=int, default=768)
    p.add_argument("--dry-run", action="store_true", help="Print the prompts and exit, no model loaded")
    args = p.parse_args()

    cond = CONDITIONS[args.condition]
    if cond["adapter"] and not args.adapter and not args.dry_run:
        p.error(f"--adapter is required for condition '{args.condition}'")

    built = build_all(args)
    if args.dry_run:
        for sc, messages, docs in built:
            print(f"=== {sc['id']}  retrieved={docs}")
            print(json.dumps(messages, ensure_ascii=False, indent=2))
        return

    # Heavy imports only when actually generating.
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
    dtype = torch.bfloat16 if use_bf16 else torch.float32
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=dtype).to(device)
    if cond["adapter"]:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, args.adapter)
    model.eval()

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as out:
        for i, (sc, messages, docs) in enumerate(built, start=1):
            # add_generation_prompt=True appends the "assistant:" marker so the
            # model writes the next reply.
            inputs = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
            ).to(device)
            with torch.no_grad():
                output = model.generate(
                    **inputs, max_new_tokens=args.max_new_tokens, do_sample=False
                )
            # Keep only the newly generated tokens, not the prompt.
            new_tokens = output[0][inputs["input_ids"].shape[1]:]
            response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
            out.write(json.dumps({
                "scenario_id": sc["id"],
                "condition": args.condition,
                "response": response,
                "retrieved_docs": docs,
                "model": args.model,
                "adapter": args.adapter,
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            }, ensure_ascii=False) + "\n")
            print(f"[{i}/{len(built)}] {sc['id']} done")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
