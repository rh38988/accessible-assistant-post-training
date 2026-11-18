#!/usr/bin/env python3
"""Audit a judge run (run_llm_judge.py output folder).

Checks (a judge score is only a signal; these checks look for broken or contradictory output):
  Q1  every quote in `evidence` appears word for word in the response (whitespace and
      quote marks normalised)
  Q2  completeness = 2 but missing_key_actions is not empty
  Q3  completeness = 0 or 1 but missing_key_actions is empty
  Q4  constraint_violation is true but correctness is above 0
  Q5  completeness is NA but the scenario does not require clarification
  Q6  every expected (blind_id, run) was parsed, ids are unique, scores are 0/1/2/NA
Writes a markdown report and a CSV of flagged rows. Does not change any score.

Example:
  python check_judge_quotes.py --judge-out ..\\judge_out_v4 --scenarios <eval_v1.jsonl> ^
      --outputs-dir <outputs folder> --conditions-json <conditions.json> --prep ..\\scenario_prep_v2.json ^
      --expected-runs 2 --out-md ..\\judge_audit.md --out-csv ..\\judge_audit_flags.csv
"""
import argparse, csv, json, re


def norm(t):
    t = re.sub(r"[‘’`“”\"'\\\\]", "", str(t))
    t = re.sub(r"[*_#>]+", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge-out", required=True)
    ap.add_argument("--scenarios", required=True)
    ap.add_argument("--outputs-dir", required=True)
    ap.add_argument("--conditions-json", required=True)
    ap.add_argument("--prep", required=True)
    ap.add_argument("--expected-runs", type=int, default=2)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--out-csv", required=True)
    a = ap.parse_args()

    scen = {s["id"]: s for s in load_jsonl(a.scenarios)}
    conds = json.load(open(a.conditions_json, encoding="utf-8"))
    resp = {}
    for c, fn in conds.items():
        for r in load_jsonl(f"{a.outputs_dir}/{fn}"):
            resp[(c, r["scenario_id"])] = r.get("response", r.get("response_text", ""))
    key = {r["blind_id"]: r for r in csv.DictReader(open(f"{a.judge_out}/key_condition_DO_NOT_SHOW_JUDGE.csv", encoding="utf-8-sig"))}

    flags, n_quotes, n_found, n_rows, bad_schema = [], 0, 0, 0, 0
    seen, failed = set(), 0
    for l in open(f"{a.judge_out}/judge_raw.jsonl", encoding="utf-8"):
        r = json.loads(l)
        ident = (r["blind_id"], r["run"])
        if ident in seen:
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q6 duplicate", "detail": ""}); continue
        seen.add(ident)
        p = r.get("parsed")
        if not p:
            failed += 1
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q6 unparsed", "detail": str(r.get("error"))[:120]}); continue
        n_rows += 1
        k = key[r["blind_id"]]
        text = norm(resp.get((k["condition"], k["scenario_id"]), ""))
        sc = p["scores"]
        if any(sc.get(d) not in (0, 1, 2, "NA", "0", "1", "2") for d in ("clarity", "actionability", "completeness", "correctness")):
            bad_schema += 1
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q6 bad score value", "detail": json.dumps(sc)})
        for q in p.get("evidence") or []:
            q = norm(q)
            if not q:
                continue
            n_quotes += 1
            # a quote with "..." is checked piece by piece; very short pieces are ignored
            parts = [x.strip(" .,;:") for x in re.split(r"\.{3,}|…", q)]
            parts = [x for x in parts if len(x) >= 8] or [q]
            if all(x in text for x in parts):
                n_found += 1
            else:
                flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q1 quote not in response", "detail": q[:140]})
        miss = p.get("missing_key_actions") or []
        comp = sc.get("completeness")
        if str(comp) == "2" and miss:
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q2 completeness 2 with missing", "detail": str(miss)})
        if str(comp) in ("0", "1") and not miss:
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q3 completeness<2 with none missing", "detail": ""})
        if (p.get("constraint_violation") or {}).get("violated") and str(sc.get("correctness")) not in ("0",):
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q4 constraint violated, correctness>0", "detail": str(sc.get("correctness"))})
        if comp == "NA" and not scen[k["scenario_id"]]["clarification_required"]:
            flags.append({"blind_id": r["blind_id"], "run": r["run"], "check": "Q5 NA without clarification required", "detail": k["scenario_id"]})

    expected = len(key) * a.expected_runs
    md = ["# Judge audit", "",
          f"Parsed judge calls: {n_rows} of {expected} expected ({len(key)} responses x {a.expected_runs} runs); unparsed: {failed}.",
          f"Evidence quotes found word for word in the response: {n_found} of {n_quotes}"
          + (f" ({100*n_found/n_quotes:.0f}%)." if n_quotes else "."),
          f"Rows with a score outside 0/1/2/NA: {bad_schema}.", "",
          "| Check | Flags |", "|---|---|"]
    from collections import Counter
    cnt = Counter(f["check"] for f in flags)
    for c in sorted(cnt):
        md.append(f"| {c} | {cnt[c]} |")
    if not cnt:
        md.append("| none | 0 |")
    md += ["", "Flags are for human review; nothing was changed. A quote that is not found may be a paraphrase "
           "or a quote from the scenario or documents, so check it before treating it as an error."]
    open(a.out_md, "w", encoding="utf-8").write("\n".join(md) + "\n")
    with open(a.out_csv, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["blind_id", "run", "check", "detail"])
        w.writeheader(); w.writerows(flags)
    print("\n".join(md))


if __name__ == "__main__":
    main()
