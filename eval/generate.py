"""Generate the final reply to each native schema_v1 scenario.

Conditions: original (base model), prompt (base + accessibility system prompt),
and sft (base + LoRA adapter). Only role/content messages from `prompt` enter
the model; evaluation metadata is never part of the chat. Earlier turns stay
fixed and decoding is greedy, with the same response budget for every condition.

Inspect prompts without loading a tokenizer or model or writing output:
    python eval/generate.py --condition original --dry-run
    python eval/generate.py --condition prompt --dry-run
    python eval/generate.py --condition sft --adapter checkpoints/pilot --dry-run
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from scripts.validate_data import check_record  # noqa: E402

CONDITIONS = {
    "original": dict(system=False, adapter=False),
    "prompt": dict(system=True, adapter=False),
    "sft": dict(system=False, adapter=True),
}


def load_jsonl(path):
    """Validate native schema_v1 records without converting their fields."""
    scenarios, errors, seen_ids = [], [], set()
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            where = f"{path}:{line_no}"
            if not line.strip():
                errors.append(f"{where}: blank scenario line")
                continue
            try:
                scenario = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{where}: invalid JSON ({exc})")
                continue
            check_record(scenario, "scenario", errors, where)
            if isinstance(scenario, dict) and isinstance(scenario.get("id"), str):
                if scenario["id"] in seen_ids:
                    errors.append(f"{where}: duplicate id '{scenario['id']}'")
                seen_ids.add(scenario["id"])
            scenarios.append(scenario)
    if not scenarios:
        errors.append(f"{path}: no scenarios")
    if errors:
        raise ValueError("\n".join(errors))
    return scenarios


def build_messages(scenario, condition, system_prompt=""):
    """Copy only role/content, preserving every turn and its exact ordering."""
    messages = []
    if CONDITIONS[condition]["system"]:
        if not system_prompt.strip():
            raise ValueError("Accessibility system prompt must not be empty")
        messages.append({"role": "system", "content": system_prompt})
    messages.extend({"role": m["role"], "content": m["content"]} for m in scenario["prompt"])
    return messages


def build_all(args):
    """Build every prompt first (no GPU needed). Use --dry-run to inspect them."""
    cond = CONDITIONS[args.condition]
    system_prompt = Path(args.system_prompt).read_text(encoding="utf-8").strip() if cond["system"] else ""
    return [(sc["id"], build_messages(sc, args.condition, system_prompt))
            for sc in load_jsonl(args.scenarios)]


def generation_kwargs(max_new_tokens):
    """One greedy decoding configuration shared by all three conditions."""
    return {"max_new_tokens": max_new_tokens, "do_sample": False}


def response_record(scenario_id, condition, adapter, response):
    return {
        "scenario_id": scenario_id,
        "condition": condition,
        "adapter": adapter if CONDITIONS[condition]["adapter"] else None,
        "response": response,
    }


def parse_args(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--condition", choices=CONDITIONS, required=True)
    p.add_argument("--scenarios", default=str(REPO / "eval/scenarios/eval_v1.jsonl"))
    p.add_argument("--out", help="Response JSONL path (required unless --dry-run)")
    p.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
    p.add_argument("--adapter", help="LoRA adapter folder (required for sft, including dry-run)")
    p.add_argument("--system-prompt", default=str(REPO / "eval/prompts/system_prompt.txt"))
    p.add_argument("--max-new-tokens", type=int, default=768)
    p.add_argument("--dry-run", action="store_true", help="Print the prompts and exit, no model loaded")
    args = p.parse_args(argv)

    cond = CONDITIONS[args.condition]
    if cond["adapter"] and not args.adapter:
        p.error(f"--adapter is required for condition '{args.condition}'")
    if args.adapter and not cond["adapter"]:
        p.error("--adapter is only valid for condition 'sft'")
    if not args.out and not args.dry_run:
        p.error("--out is required unless --dry-run is set")
    if args.max_new_tokens <= 0:
        p.error("--max-new-tokens must be positive")
    return args


def main(argv=None):
    # Keep Traditional Chinese prompts readable when stdout is redirected on Windows.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args(argv)
    cond = CONDITIONS[args.condition]
    try:
        built = build_all(args)
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc
    decoding = generation_kwargs(args.max_new_tokens)
    if args.dry_run:
        for scenario_id, messages in built:
            print(json.dumps({
                "scenario_id": scenario_id,
                "condition": args.condition,
                "adapter": args.adapter if cond["adapter"] else None,
                "model": args.model,
                **decoding,
                "message_count": len(messages),
                "roles": [m["role"] for m in messages],
                "messages": messages,
            }, ensure_ascii=False))
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
        for i, (scenario_id, messages) in enumerate(built, start=1):
            # add_generation_prompt=True appends the "assistant:" marker so the
            # model writes the next reply.
            inputs = tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
            ).to(device)
            with torch.no_grad():
                output = model.generate(**inputs, **decoding)
            # Keep only the newly generated tokens, not the prompt.
            new_tokens = output[0][inputs["input_ids"].shape[1]:]
            response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
            out.write(json.dumps(response_record(
                scenario_id, args.condition, args.adapter, response
            ), ensure_ascii=False) + "\n")
            print(f"[{i}/{len(built)}] {scenario_id} done")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
