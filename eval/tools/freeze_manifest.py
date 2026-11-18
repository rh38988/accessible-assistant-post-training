#!/usr/bin/env python3
"""Write a freeze manifest: SHA-256 and size of every file that must not change before
the new responses are generated (rubric, decision rule, scenarios, per-scenario prep,
judge script, retrieval documents, conditions file ...).

Usage:
  python freeze_manifest.py --files ..\\rubric_v4.md ..\\decision_v4_rule.md <scenarios.jsonl> ^
      <scenario_prep.json> run_llm_judge.py <judge_docs.json> --judge-model gpt-5.6-luna ^
      --seed 42 --runs 2 --out ..\\freeze_manifest.json

`approved` is always written as false. The researcher sets it to true by hand (and fills
`approved_by`) after reading the files; nobody else should. Re-run and compare the hashes
before generation and again before judging to show nothing changed.
"""
import argparse, datetime, hashlib, json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--files", nargs="+", required=True)
ap.add_argument("--judge-model", default="")
ap.add_argument("--judge-provider", default="")
ap.add_argument("--seed", type=int, default=None)
ap.add_argument("--runs", type=int, default=None)
ap.add_argument("--note", default="")
ap.add_argument("--out", required=True)
a = ap.parse_args()

files = {}
for f in a.files:
    p = Path(f)
    files[p.name] = {"path": str(p), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size}
manifest = {
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "files": files,
    "judge": {"model": a.judge_model, "provider": a.judge_provider, "seed": a.seed, "runs": a.runs},
    "note": a.note,
    "approved": False,
    "approved_by": None,
    "approved_at": None,
}
Path(a.out).write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(manifest, indent=1, ensure_ascii=False))
