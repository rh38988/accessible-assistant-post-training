#!/usr/bin/env python3
"""Check the response files from the model owner before any judge call.

Checks:
  I1  every condition file has every scenario exactly once, no extras, no empty response
  I2  expected number of responses (conditions x scenarios)
  I3  no Chinese characters in a response to an English scenario (and no English-only reply to a zh scenario is NOT checked)
  I4  no truncation (field `truncated` true, or response ids listed in <file>.summary.json hit_length_limit_ids)
  I5  RAG conditions (name contains 'rag') carry retrieval.document_ids when they answered
  I6  response_id values (if present) are unique
  I7  leakage: the model-input log(s) and the prompts-only file contain none of the evaluation labels
      (expected_elements text, clarification_required, notes_for_raters)
Writes a markdown report. Exit code 1 if any check fails.

Example:
  python check_inputs.py --scenarios <scenarios.jsonl> --outputs-dir <folder> --conditions-json <conditions.json> ^
      --model-inputs <model_inputs.jsonl> --prompts-file <prompts_only.jsonl> --out-md ..\\input_check.md
"""
import argparse, json, re, sys
from pathlib import Path

CJK = re.compile(r"[㐀-鿿]")


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9㐀-鿿 ]", " ", str(t).lower())).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenarios", required=True)
    ap.add_argument("--outputs-dir", required=True)
    ap.add_argument("--conditions-json", required=True)
    ap.add_argument("--expected-conditions", type=int, default=0, help="default: number of conditions in the json")
    ap.add_argument("--exclude", default="", help="scenario ids to ignore")
    ap.add_argument("--model-inputs", nargs="*", default=[], help="jsonl or text files logging what the model/router actually received")
    ap.add_argument("--prompts-file", nargs="*", default=[], help="prompts-only file(s) given to the model owner")
    ap.add_argument("--out-md", required=True)
    a = ap.parse_args()

    drop = {x for x in a.exclude.split(",") if x}
    scen = {s["id"]: s for s in load_jsonl(a.scenarios) if s["id"] not in drop}
    conds = json.load(open(a.conditions_json, encoding="utf-8"))
    n_expected = a.expected_conditions or len(conds)
    problems, notes = [], []

    if len(conds) != n_expected:
        problems.append(f"I2 {len(conds)} conditions in the json, expected {n_expected}")
    total = 0
    for c, fn in conds.items():
        p = Path(a.outputs_dir) / fn
        if not p.exists():
            problems.append(f"I1 missing file for {c}: {fn}"); continue
        rows = [r for r in load_jsonl(p) if r["scenario_id"] not in drop]
        total += len(rows)
        ids = [r["scenario_id"] for r in rows]
        for s in scen:
            n = ids.count(s)
            if n != 1:
                problems.append(f"I1 {c}: scenario {s} appears {n} times")
        for s in set(ids) - set(scen):
            problems.append(f"I1 {c}: unknown scenario {s}")
        rid = [r.get("response_id") for r in rows if r.get("response_id")]
        if len(rid) != len(set(rid)):
            problems.append(f"I6 {c}: duplicate response_id")
        summ = p.with_suffix(".summary.json")
        limit_ids = set()
        if summ.exists():
            limit_ids = set(json.load(open(summ, encoding="utf-8")).get("hit_length_limit_ids", []))
        for r in rows:
            text = r.get("response", r.get("response_text", ""))
            sid = r["scenario_id"]
            if not str(text).strip():
                problems.append(f"I1 {c}/{sid}: empty response")
            zh = bool(CJK.search(json.dumps(scen[sid]["prompt"], ensure_ascii=False))) if sid in scen else False
            if not zh and CJK.search(text):
                problems.append(f"I3 {c}/{sid}: Chinese characters in an English scenario")
            if r.get("truncated") is True or sid in limit_ids:
                problems.append(f"I4 {c}/{sid}: truncated or hit the length limit")
            if "rag" in c.lower() and not (r.get("retrieval") or {}).get("document_ids"):
                notes.append(f"I5 {c}/{sid}: no retrieval.document_ids (fine only if the router chose to clarify)")
    if total != n_expected * len(scen):
        problems.append(f"I2 {total} responses found, expected {n_expected} x {len(scen)} = {n_expected*len(scen)}")

    labels = ["expected_elements", "clarification_required", "notes_for_raters"]
    snippets = {}
    for sid, s in scen.items():
        snippets[sid] = [norm(e)[:60] for e in s.get("expected_elements", []) if len(norm(e)) >= 25]
    for f in list(a.model_inputs) + list(a.prompts_file):
        txt = Path(f).read_text(encoding="utf-8", errors="replace")
        low = txt.lower()
        for lab in labels:
            if lab in low:
                problems.append(f"I7 {Path(f).name}: contains the label '{lab}'")
        nt = norm(txt)
        for sid, sn in snippets.items():
            for x in sn:
                if x and x in nt:
                    problems.append(f"I7 {Path(f).name}: contains text of an expected element of {sid}: '{x[:40]}...'")
    if not (a.model_inputs or a.prompts_file):
        notes.append("I7 not checked: no --model-inputs or --prompts-file given (ask the model owner for the log of real model inputs)")

    md = ["# Input check", "",
          f"Scenarios: {len(scen)}. Conditions: {len(conds)}. Responses found: {total}. Expected: {n_expected*len(scen)}.", "",
          f"**Result: {'FAIL' if problems else 'PASS'}** ({len(problems)} problems, {len(notes)} notes)", ""]
    if problems:
        md += ["## Problems", ""] + [f"- {p}" for p in problems] + [""]
    if notes:
        md += ["## Notes", ""] + [f"- {n}" for n in notes] + [""]
    Path(a.out_md).write_text("\n".join(md), encoding="utf-8")
    print("\n".join(md))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
