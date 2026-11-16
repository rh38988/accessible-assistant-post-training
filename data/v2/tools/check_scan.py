#!/usr/bin/env python3
"""Check one rule-scan output part, or merge all parts into a CSV.

    python3 data/v2/tools/check_scan.py 07        # check part 07
    python3 data/v2/tools/check_scan.py --merge   # write data/v2/RULE_SCAN_v2.2.csv
"""
import csv
import json
import sys
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
SCAN = V2 / "rule_scan"
RULES = {f"R{i}" for i in range(1, 15)}
SEV = {"high", "medium", "low"}
FIELDS = ["rule", "severity", "quote", "reason", "suggestion", "needs_source_check"]


def check(part):
    ids = json.load(open(SCAN / f"input/part_{part}.ids.json"))
    out = SCAN / f"out/part_{part}.jsonl"
    errs = []
    if not out.exists():
        return [f"missing {out}"], []
    rows = []
    for n, line in enumerate(open(out, encoding="utf-8"), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"line {n}: bad JSON ({e})")
            continue
        rows.append(r)
        if not isinstance(r.get("flags"), list):
            errs.append(f"line {n}: flags must be a list")
            continue
        if len(r["flags"]) > 3:
            errs.append(f"{r.get('id')}: more than 3 flags")
        for f in r["flags"]:
            missing = [k for k in FIELDS if k not in f]
            if missing:
                errs.append(f"{r.get('id')}: flag missing {missing}")
            if f.get("rule") not in RULES:
                errs.append(f"{r.get('id')}: unknown rule {f.get('rule')}")
            if f.get("severity") not in SEV:
                errs.append(f"{r.get('id')}: bad severity {f.get('severity')}")
            if not isinstance(f.get("needs_source_check"), bool):
                errs.append(f"{r.get('id')}: needs_source_check must be true or false")
            if any("—" in str(f.get(k, "")) for k in ("reason", "suggestion")):
                errs.append(f"{r.get('id')}: em dash in reason or suggestion")
    got = [r.get("id") for r in rows]
    if got != ids:
        miss = [i for i in ids if i not in got]
        extra = [i for i in got if i not in ids]
        errs.append(f"ids do not match input order (missing {miss[:5]}, extra {extra[:5]}, count {len(got)} vs {len(ids)})")
    return errs, rows


def merge():
    recs = {json.loads(l)["id"]: json.loads(l) for l in open(V2 / "train_v2_en.jsonl", encoding="utf-8")}
    parts = sorted(p.name[5:7] for p in (SCAN / "input").glob("part_*.ids.json") if p.name[5:7] != "00")  # 00 = calibration
    out_rows, bad, checked = [], [], 0
    for part in parts:
        errs, rows = check(part)
        if errs:
            bad.append((part, errs[:3]))
            continue
        checked += len(rows)
        for r in rows:
            for f in r["flags"]:
                out_rows.append({"id": r["id"], "task_id": recs[r["id"]]["task_id"], **{k: f[k] for k in FIELDS}})
    order = {"high": 0, "medium": 1, "low": 2}
    out_rows.sort(key=lambda x: (order[x["severity"]], x["rule"], x["id"]))
    with open(V2 / "RULE_SCAN_v2.2.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "task_id"] + FIELDS)
        w.writeheader()
        w.writerows(out_rows)
    print(f"parts OK: {len(parts) - len(bad)}/{len(parts)} | examples checked: {checked} | flags: {len(out_rows)} "
          f"| flagged examples: {len({r['id'] for r in out_rows})}")
    for part, errs in bad:
        print("BAD", part, errs)


if __name__ == "__main__":
    if sys.argv[1:] == ["--merge"]:
        merge()
    else:
        errs, rows = check(sys.argv[1])
        print("\n".join(errs) if errs else f"OK ({len(rows)} examples, {sum(len(r['flags']) for r in rows)} flags)")
