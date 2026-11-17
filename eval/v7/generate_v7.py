#!/usr/bin/env python3
"""Generate the v7 condition (SFT v2 + RAG, one model call per verified step).

Reuses v6's saved retrieval, routing and action plans, so only the answer-writing step
changes. Same base model, adapter and greedy decoding as v6.

    # see every prompt, no model needed
    python eval/v7/generate_v7.py --v6-plan <v6 plan.json> --v6-outputs <v6 responses .jsonl> --dry-run
    # compose answers from plan text only, no model (for checking the format; do NOT judge this)
    python eval/v7/generate_v7.py --v6-plan ... --v6-outputs ... --stub --out eval/outputs/v7-stub.jsonl
    # real run (GPU, same adapter as v6)
    python eval/v7/generate_v7.py --v6-plan ... --v6-outputs ... --adapter <checkpoint> \
        --out eval/outputs/dev-sft-v2-rag-v7-20261116.jsonl
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grounded_steps import build_answer  # noqa: E402

CONDITION = "sft_v2_rag_v7"


def jl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--v6-plan", required=True, help="dev-sft-v2-rag-verified-action-plan-v6-20261115.plan.json")
    ap.add_argument("--v6-outputs", required=True, help="dev-sft-v2-rag-verified-action-plan-v6-20261115.jsonl (for the retrieval field)")
    ap.add_argument("--model", default="Qwen/Qwen2.5-3B-Instruct")
    ap.add_argument("--adapter", help="same LoRA checkpoint as v6")
    ap.add_argument("--out")
    ap.add_argument("--dry-run", action="store_true", help="print the prompts each scenario would send; no model")
    ap.add_argument("--stub", action="store_true", help="no model: every model call fails validation, so plan text is used")
    a = ap.parse_args(argv)
    if not (a.dry_run or a.stub) and not a.adapter:
        ap.error("--adapter is required for a real run")
    if not a.dry_run and not a.out:
        ap.error("--out is required")

    plan = json.load(open(a.v6_plan, encoding="utf-8"))
    v6 = {r["scenario_id"]: r for r in jl(a.v6_outputs)}

    if a.dry_run or a.stub:
        log = []

        def generate(messages, max_new_tokens):
            log.append({"max_new_tokens": max_new_tokens, "messages": messages})
            return ""
    else:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from peft import PeftModel
        use_bf16 = torch.cuda.is_available() and torch.cuda.is_bf16_supported()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tok = AutoTokenizer.from_pretrained(a.model, revision=plan.get("model_revision"))
        model = AutoModelForCausalLM.from_pretrained(a.model, revision=plan.get("model_revision"),
                                                     torch_dtype=torch.bfloat16 if use_bf16 else torch.float32).to(device)
        model = PeftModel.from_pretrained(model, a.adapter).eval()

        def generate(messages, max_new_tokens):
            inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt",
                                             return_dict=True).to(device)
            with torch.no_grad():
                out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
            return tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()

    records, checks = [], []
    for row in plan["rows"]:
        sid = row["scenario_id"]
        request = row["query"]
        if a.dry_run:
            log.clear()
        response, check = build_answer(row, request, generate, row["model_messages"])
        if a.dry_run:
            print(json.dumps({"scenario_id": sid, "method": check["method"], "calls": log}, ensure_ascii=False))
            continue
        records.append({"scenario_id": sid, "condition": CONDITION + ("_stub" if a.stub else ""),
                        "adapter": None if a.stub else a.adapter, "response": response,
                        "retrieval": v6[sid].get("retrieval"), "generation": {"model_calls": check["calls"]}})
        checks.append({"scenario_id": sid, **check})
        print(f"{sid}: {check['method']}, calls {check['calls']}, fallbacks {check.get('fallbacks', 0)}")
    if a.dry_run:
        return

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    chk = out.with_suffix(".checks.jsonl")
    with open(chk, "w", encoding="utf-8") as f:
        for c in checks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    summary = {"condition": CONDITION, "stub": a.stub, "model": a.model, "model_revision": plan.get("model_revision"),
               "adapter": a.adapter, "decoding": "greedy", "v6_plan_sha256": sha(a.v6_plan),
               "v6_outputs_sha256": sha(a.v6_outputs), "output_sha256": sha(out), "checks_sha256": sha(chk),
               "scenarios": len(records), "model_calls": sum(c["calls"] for c in checks),
               "step_fallbacks": sum(c.get("fallbacks", 0) for c in checks)}
    json.dump(summary, open(out.with_suffix(".summary.json"), "w", encoding="utf-8"), indent=1)
    print(f"Wrote {out} ({len(records)} scenarios)")


if __name__ == "__main__":
    main()
