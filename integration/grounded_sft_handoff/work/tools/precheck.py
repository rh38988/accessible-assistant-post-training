#!/usr/bin/env python3
"""Run Shirley's validate_grounded.py checks that do not need the Qwen tokenizer.

This workspace cannot reach Hugging Face, so torch/datasets/peft/transformers/trl are
replaced by empty stand-ins only to import the validator. Every check before its
tokenizer step runs unchanged (schema, English, prompt rebuild, provenance hashes,
source mapping, eval task types, clearance, overlap with v2.1, AI-review binding).
The token-length and label-mask checks must still be run on a machine with the cached
tokenizer, using the command in HANDOFF_TO_RYAN.md.

    python3 integration/grounded_sft_handoff/work/tools/precheck.py <candidates.jsonl> --provenance <prov.jsonl> [validator args]
"""
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
class _Unavailable:
    """Importable placeholder; any real use raises ImportError (the tokenizer step)."""
    def __init__(self, name):
        self._name = name
    def __getattr__(self, attr):
        if attr.startswith("__"):
            raise AttributeError(attr)
        raise ImportError(f"{self._name}.{attr} unavailable here")
    def __call__(self, *a, **k):
        raise ImportError(f"{self._name} unavailable here")


for name in ("torch", "datasets", "peft", "transformers", "trl", "trl.trainer", "trl.trainer.sft_trainer"):
    mod = types.ModuleType(name)
    mod.__path__ = []
    mod.__getattr__ = lambda attr, _n=name: _Unavailable(f"{_n}.{attr}") if not attr.startswith("__") else (_ for _ in ()).throw(AttributeError(attr))
    sys.modules[name] = mod

import argparse  # noqa: E402
import json  # noqa: E402
from integration.grounded_sft_handoff import validate_grounded as vg  # noqa: E402


def main():
    sys.argv[0] = "validate_grounded.py"
    parser_args = sys.argv[1:]
    ns = argparse.Namespace(provenance=None, reviews=None, require_ai_review=False, expected_count=None,
                            max_length=1028, against=None, eval_task_types=ROOT / "eval/tasks/eval_tasks.csv",
                            task_clearance=None, require_task_clearance=False, report=None)
    it = iter(parser_args)
    ns.file = Path(next(it))
    for arg in it:
        key = arg.lstrip("-").replace("-", "_")
        if key in ("require_ai_review", "require_task_clearance"):
            setattr(ns, key, True)
        elif key == "against":
            ns.against = [Path(next(it))]
        elif key == "expected_count":
            ns.expected_count = int(next(it))
        else:
            setattr(ns, key, Path(next(it)))
    try:
        result = vg.validate(ns)
    except (ImportError, FileNotFoundError) as e:
        if isinstance(e, FileNotFoundError) and "tokenizer" not in str(e):
            raise
        print(json.dumps({"status": "pre-tokenizer checks passed",
                          "note": f"stopped at the tokenizer step ({e}); run the full validator where the Qwen tokenizer is cached"}))
        return 0
    print(json.dumps({k: v for k, v in result.items() if k in ("status", "count", "errors", "warnings")}, indent=1)[:6000])
    return 1 if result.get("status") == "failed" else 0


if __name__ == "__main__":
    sys.exit(main())
