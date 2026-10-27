"""Standalone schema_v1 checker for eval/scenarios/eval_v1.jsonl (standard library only).
Usage: python eval/tools/validate_eval_v1.py eval/scenarios/eval_v1.jsonl
"""
import json, re, sys
from collections import Counter

FIELDS = ["id","split","task_family","task","platform","device","scenario_type","source_url",
          "access_date","risk_level","prompt","clarification_required","expected_elements"]
FAMILIES = {"Smartphone Basics": 5, "Communication": 5, "Online Safety and Scam Prevention": 5}
RISK = {"low", "medium", "high"}
FORBIDDEN = {"completion", "response", "answer", "output", "messages", "turns", "language", "author",
             "reviewed", "task_id", "sources", "category", "specification", "sensitive", "notes_for_raters"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL = re.compile(r"^https://[^\s]+$")
PLACEHOLDER = re.compile(r"example\.com|\.\.\.|TODO|placeholder|xxx", re.I)

path = sys.argv[1]
errs, recs, checks = [], [], {}
raw = open(path, encoding="utf-8").read()
lines = raw.split("\n")
if lines and lines[-1] == "": lines = lines[:-1]
for i, line in enumerate(lines, 1):
    if not line.strip():
        errs.append(f"line {i}: blank line"); continue
    try: recs.append(json.loads(line))
    except json.JSONDecodeError as e: errs.append(f"line {i}: invalid JSON ({e})")

def chk(name, ok):
    checks[name] = bool(ok)
    if not ok: errs.append(f"CHECK FAILED: {name}")

chk("1. exactly 15 JSON objects", len(recs) == 15 and all(isinstance(r, dict) for r in recs))
chk("2. valid JSONL (one object per non-blank line, no parse errors)", len(recs) == len(lines) and not any("invalid JSON" in e or "blank" in e for e in errs))
chk("3. all 13 required fields present in every record", all(all(f in r for f in FIELDS) for r in recs))
chk("4. no unexpected top-level fields (exactly the 13)", all(list(r.keys()) == FIELDS or set(r.keys()) == set(FIELDS) for r in recs))
fam = Counter(r.get("task_family") for r in recs)
chk("5. five scenarios per task family (exact family strings)", dict(fam) == FAMILIES)
ids = [r.get("id") for r in recs]
chk("6. all IDs unique", len(set(ids)) == len(ids))
chk("7. every split == 'evaluation'", all(r.get("split") == "evaluation" for r in recs))
chk("8. clarification_required is a JSON boolean", all(type(r.get("clarification_required")) is bool for r in recs))
chk("9. expected_elements is a list of 3-6 non-empty strings", all(isinstance(r.get("expected_elements"), list) and 3 <= len(r["expected_elements"]) <= 6 and all(isinstance(x, str) and x.strip() for x in r["expected_elements"]) for r in recs))
def prompt_ok(p):
    if not isinstance(p, list) or not p: return False
    for i, m in enumerate(p):
        if not isinstance(m, dict) or set(m) != {"role", "content"}: return False
        if m["role"] != ("user" if i % 2 == 0 else "assistant"): return False
        if not isinstance(m["content"], str) or not m["content"].strip(): return False
    return p[0]["role"] == "user" and p[-1]["role"] == "user"
chk("10. every prompt is a role/content array that alternates, starts and ends with user", all(prompt_ok(r.get("prompt")) for r in recs))
chk("11. no completion/response/answer or other forbidden fields", not any(set(r) & FORBIDDEN for r in recs))
chk("extra: risk_level in {low, medium, high}", all(r.get("risk_level") in RISK for r in recs))
chk("extra: access_date is YYYY-MM-DD", all(DATE.match(str(r.get("access_date"))) for r in recs))
chk("extra: source_url is https and has no placeholder text", all(URL.match(str(r.get("source_url"))) and not PLACEHOLDER.search(str(r.get("source_url"))) for r in recs))
chk("extra: platform/device/task/scenario_type are non-empty strings", all(all(isinstance(r.get(k), str) and r[k].strip() for k in ("platform","device","task","scenario_type")) for r in recs))
chk("extra: at least 2 zh-TW (CJK) prompts", sum(any(re.search(r"[一-鿿]", m["content"]) for m in r["prompt"]) for r in recs) >= 2)
chk("extra: at least 1 multi-turn prompt", any(len(r["prompt"]) > 1 for r in recs))
chk("extra: expected_elements text never appears inside prompt", all(not any(e in m["content"] for e in r["expected_elements"] for m in r["prompt"]) for r in recs))

print(f"File: {path}\nRecords: {len(recs)}")
print("Task families:", dict(fam))
print("scenario_type:", dict(Counter(r.get("scenario_type") for r in recs)))
print("clarification_required true:", sum(r.get("clarification_required") is True for r in recs), "of", len(recs))
print("risk_level:", dict(Counter(r.get("risk_level") for r in recs)))
print("multi-turn:", [r["id"] for r in recs if len(r["prompt"]) > 1])
print()
for k, v in checks.items(): print(("PASS  " if v else "FAIL  ") + k)
print("\n" + ("ALL CHECKS PASSED" if not errs else f"{len(errs)} problem(s):\n  " + "\n  ".join(errs)))
sys.exit(1 if errs else 0)
