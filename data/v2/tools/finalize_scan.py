#!/usr/bin/env python3
"""Turn the raw rule-scan output into the final issue list.

    python3 data/v2/tools/finalize_scan.py

Reads data/v2/rule_scan/out/part_01..19.jsonl (Haiku agents, text only) and writes
data/v2/RULE_SCAN_v2.2.csv. Three changes to the raw agent flags:

1. Timing claims (R13) are found by one fixed text search instead of by the agents,
   because the agents applied that rule unevenly. Agent R13 flags whose quote is a
   timing phrase are replaced by the search result.
2. Examples that still contain a sentence removed by a v2.1 or v2.2 fix are added
   (source = same_text_as_fix). Only the matches listed in SAME_TEXT were kept; the
   other matches were shared harmless sentences (for example the device question).
3. Every high-severity flag was checked by hand against the reply and, where needed,
   the official page (2026-11-16). Result in check_status; see HIGH_CHECKS.
"""
import csv
import json
import re
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]

TIMING = re.compile(
    r"[^.\n]*\btakes?\s+(?:only\s+|just\s+)?(?:about|around|less than|under|a few|a couple of|a|an|one|two|three|five|ten)"
    r"\s+(?:\w+\s+)?(?:seconds?|minutes?)\b[^.\n]*", re.I)

SAME_TEXT = {  # id: (fixed example it repeats, what to change)
    "tr050-d": ("tr050-a", "Same reply as tr050-a before v2.2. Apply the same fix: remove 'It takes a minute', explain Maximum Capacity in plain words, and replace the warranty line with the page's wording."),
    "tr062-a": ("tr062-d", "Same generic reply as tr062-d before v2.2. Say photos should be removed with Delete from device after checking backup, since regular Delete also removes the backed-up copy."),
    "tr038-a": ("tr038-c", "Contains 'It usually takes a few minutes.', removed from tr038-c in v2.1. Delete it."),
    "tr038-d": ("tr038-c", "Contains 'It usually takes a few minutes.', removed from tr038-c in v2.1. Delete it."),
    "tr049-d": ("tr049-a", "Contains 'It takes about a minute to turn on.', removed from tr049-a in v2.1. Delete it."),
    "tr097-a": ("tr049-a", "Contains 'It takes about a minute to turn on.', removed from tr049-a in v2.1. Delete it."),
    "tr097-d": ("tr049-a", "Contains 'It takes about a minute to turn on.', removed from tr049-a in v2.1. Delete it."),
}

OK, LOWER, NOT = "checked: confirmed", "checked: confirmed, lowered to medium", "checked: not a problem"
HIGH_CHECKS = {  # (id, rule): (status, note)
    ("tr010-c", "R10"): (OK, "Library computer; add a step to sign out and not save the password in the browser."),
    ("tr050-d", "R9"): (NOT, "Apple 101575: 'This message doesn't indicate a safety issue.' See same_text_as_fix tr050-a instead."),
    ("tr059-e", "R12"): (LOWER, "Plausible (game progress could be lost) but not stated on the Play page; needs a source."),
    ("tr062-a", "R12"): (OK, "Same problem as tr062-d."),
    ("tr078-r", "R9"): (NOT, "Apple 105072: 'If you turn off Emergency Calls & SOS, your Medical ID information will not be shared.'"),
    ("tr090-r", "R2"): (LOWER, "Bank and email are changed in step 2 and email is called most important; only the order is off."),
    ("tr120-c", "R11"): (LOWER, "'Do not pay' could be read as the real power bill; scope it to the crypto demand and suggest calling the number on a real bill."),
    ("tr120-c", "R9"): (NOT, "FTC crypto page: 'Only scammers demand payment in cryptocurrency.'"),
    ("tr120-g", "R9"): (NOT, "FTC crypto page: 'Only scammers demand payment in cryptocurrency.'"),
    ("tr120-e", "R2"): (OK, "Reporting to the exchange used is on the FTC page; make it an early, unconditional step and say crypto payments usually can't be reversed."),
    ("tr124-e", "R12"): (NOT, "Apple 102610: 'Deleting or uninstalling an app doesn't remove any documents or other files that you created with the app.'"),
    ("tr125-c", "R12"): (LOWER, "Deleting Downloads files without checking them first; user wants to keep family pictures."),
    ("tr147-e", "R12"): (LOWER, "Really R1: the user asked not to be told to reset, and the reply mentions a full erase."),
    ("tr152-e", "R9"): (LOWER, "Google 9061432 supports 'can't view your report' and 'past replies aren't sent'. Not supported: 'Your name and phone number are not linked'; the page says your country code and a copy to your carrier may be sent."),
    ("tr158-a", "R9"): (LOWER, "Google 15146908 says the lock 'may activate' if someone grabs the phone and runs, bikes, or drives away, and may not trigger in some cases. 'Locks automatically' overstates it."),
    ("tr158-d", "R9"): (LOWER, "Same as tr158-a."),
    ("tr173-a", "R12"): (OK, "Large or unused files and Files synced to the cloud can hold the user's own files; add a check before removing them."),
    ("tr173-e", "R12"): (OK, "Cut moves the only copy of family photos; safer to Copy, check they open on the USB drive, then delete from the PC."),
    ("tr197-a", "R12"): (OK, "Permanent delete with no download-first step (tr197-e shows the safer version)."),
    ("tr197-d", "R12"): (OK, "Same as tr197-a."),
    ("tr214-a", "R9"): (LOWER, "The 30-day dispute condition is already in step 3; the remaining issue is U.S.-only framing (same as tr214-g)."),
    ("tr214-c", "R9"): (OK, "Same frequency-rule simplification Shirley fixed in tr214-g."),
    ("tr214-r", "R9"): (LOWER, "The 30-day condition is already in step 2; remaining issue is U.S.-only framing (same as tr214-g)."),
    ("tr218-a", "R11"): (OK, "Delete comes before report (same as tr218-e)."),
    ("tr218-c", "R11"): (OK, "Delete comes before report (same as tr218-e)."),
    ("tr218-f", "R11"): (OK, "Delete comes before report (same as tr218-e)."),
    ("tr218-g", "R11"): (OK, "Delete comes before report (same as tr218-e)."),
    ("tr218-a", "R9"): (OK, "'All talk' (same as tr218-e)."),
    ("tr218-c", "R9"): (OK, "'All talk' (same as tr218-e)."),
    ("tr218-f", "R9"): (OK, "'All talk' (same as tr218-e)."),
    ("tr218-g", "R9"): (OK, "'All talk' (same as tr218-e)."),
    ("tr219-a", "R9"): (NOT, "FTC public Wi-Fi page: 'connecting through a public Wi-Fi network is usually safe.'"),
    ("tr221-a", "R9"): (LOWER, "Says 'In one FTC case' and then 'usually'; drop 'usually'."),
    ("tr221-r", "R2"): (OK, "Already paid $1,800; add asking the card company or bank to reverse the charge (FTC 'What To Do if You Were Scammed')."),
    ("tr223-r", "R2"): (OK, "Gift cards already sent; add contacting the gift card company right away (FTC 'What To Do if You Were Scammed')."),
    ("tr224-r", "R2"): (OK, "Wire already sent; add contacting the wire transfer company or bank to ask for a reversal (FTC 'What To Do if You Were Scammed')."),
}

FIELDS = ["id", "task_id", "rule", "severity", "found_by", "check_status", "quote", "reason", "suggestion",
          "needs_source_check", "note"]


def main():
    recs = {json.loads(l)["id"]: json.loads(l) for l in open(V2 / "train_v2_en.jsonl", encoding="utf-8")}
    spot = {r["id"] for r in csv.DictReader(open(V2 / "spot_check_v2.csv", encoding="utf-8-sig"))}
    scope = [i for i in recs if i not in spot]

    rows = []
    for p in sorted((V2 / "rule_scan/out").glob("part_*.jsonl")):
        if p.name == "part_00.jsonl":  # calibration run on the 50 spot-checked examples
            continue
        for line in open(p, encoding="utf-8"):
            r = json.loads(line)
            for f in r["flags"]:
                if f["rule"] == "R13" and TIMING.search(f["quote"]):
                    continue  # replaced by the text search below
                status, note = HIGH_CHECKS.get((r["id"], f["rule"]), ("not checked", ""))
                sev = f["severity"]
                if status in (LOWER,):
                    sev = "medium"
                rows.append({"id": r["id"], "task_id": recs[r["id"]]["task_id"], "rule": f["rule"], "severity": sev,
                             "found_by": "agent", "check_status": status, "quote": f["quote"], "reason": f["reason"],
                             "suggestion": f["suggestion"], "needs_source_check": f["needs_source_check"], "note": note})

    for i in scope:
        reply = recs[i]["messages"][-1]["content"]
        m = TIMING.search(reply)
        if m and re.search(r"a few seconds", m.group(0), re.I):
            m = None  # rough timing, allowed by the rules
        if m and i in SAME_TEXT and "takes" in SAME_TEXT[i][1]:
            m = None  # already listed under same_text_as_fix
        if m:
            rows.append({"id": i, "task_id": recs[i]["task_id"], "rule": "R13", "severity": "low",
                         "found_by": "text_search", "check_status": "not checked", "quote": m.group(0).strip(),
                         "reason": "A time estimate for the task is stated as fact.",
                         "suggestion": "Delete the time estimate unless the official page gives it.",
                         "needs_source_check": True, "note": ""})

    for i, (fid, sugg) in SAME_TEXT.items():
        rows.append({"id": i, "task_id": recs[i]["task_id"], "rule": "SAME", "severity": "medium" if i in ("tr050-d", "tr062-a") else "low",
                     "found_by": f"same_text_as_fix:{fid}", "check_status": "checked: confirmed", "quote": "",
                     "reason": f"Still contains text that was fixed in {fid}.", "suggestion": sugg,
                     "needs_source_check": False, "note": ""})

    order = {"high": 0, "medium": 1, "low": 2}
    rows.sort(key=lambda x: (x["check_status"] == "checked: not a problem", order[x["severity"]], x["rule"], x["id"]))
    with open(V2 / "RULE_SCAN_v2.2.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    live = [r for r in rows if r["check_status"] != "checked: not a problem"]
    by_sev = {s: len({r["id"] for r in live if r["severity"] == s}) for s in order}
    print(f"examples scanned: {len(scope)} | flags: {len(rows)} ({len(rows) - len(live)} checked and dismissed)")
    print(f"examples with a live flag: {len({r['id'] for r in live})} | by worst severity: ", end="")
    worst = {}
    for r in live:
        worst[r["id"]] = min(worst.get(r["id"], 9), order[r["severity"]])
    print({s: sum(1 for v in worst.values() if v == n) for s, n in order.items()})
    print("timing flags (text search):", sum(r["found_by"] == "text_search" for r in rows))
    print("high flags confirmed:", sum(r["severity"] == "high" and r["check_status"] == OK for r in rows))
    missing = [k for k in HIGH_CHECKS if not any(r["id"] == k[0] and r["rule"] == k[1] for r in rows)]
    print("HIGH_CHECKS keys not matched:", missing)


if __name__ == "__main__":
    main()
