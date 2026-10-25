"""core_tasks_v1: group training tasks into core tasks, and pick the checkpoint verify list.

A core task is one user goal. It groups existing training tasks (task_ids) by
task_type, so no example changes. Device and communication core tasks are
goals covered on 2+ platforms, which is where "which device are you using?"
matters. Online-safety core tasks group scams by the decision the user faces.

Every expected result and common failure below is taken from a source page
already cited by the examples in that core task.

Run from the repo root:
    python scripts/core_tasks.py
Writes:
    data/tasks/core_tasks_v1.csv        (machine-readable)
    data/tasks/core_tasks_v1.md         (readable summary + source list)
    data/tasks/checkpoint_verify_v1.csv (examples to hand-verify for the checkpoint)
"""
import csv
import glob
import json
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

CORE_TASKS = [
    # ---------------- A. Device Basics ----------------
    dict(id="CT-01", family="Device Basics", name="Make text bigger", risk="low",
         types=["text_size"],
         expected="Text appears larger right away; the sample text changes as the slider moves.",
         failure="Very large text can make buttons hard to tap; some Android apps ignore the font size setting."),
    dict(id="CT-02", family="Device Basics", name="Install software and app updates", risk="low",
         types=["software_update"],
         expected="The update installs (the device may restart) and Settings shows the device or app is up to date.",
         failure="A 'not enough space' message stops the update; menu names differ by phone maker."),
    dict(id="CT-03", family="Device Basics", name="Make the phone ring louder", risk="low",
         types=["ring_volume"],
         expected="Incoming calls ring loud enough to hear.",
         failure="The iPhone is in Silent mode (orange switch or Action button), so it only vibrates."),
    dict(id="CT-04", family="Device Basics", name="Turn off notifications from an app or chat", risk="low",
         types=["app_notifications_off"],
         expected="Alerts from that app or chat stop; the app itself keeps working.",
         failure="In LINE, @mentions can still notify after a chat is muted; Android menu names vary."),
    dict(id="CT-05", family="Device Basics", name="Delete an app", risk="low",
         types=["delete_app"],
         expected="The app's icon disappears; it can be reinstalled later.",
         failure="On iPhone the icons start to jiggle instead of showing a menu (use the minus sign, then Done)."),
    dict(id="CT-06", family="Device Basics", name="Take a screenshot", risk="low",
         types=["screenshot"],
         expected="A small preview appears and the screenshot is saved to Photos or the Screenshots folder.",
         failure="The two-button press doesn't register; on Windows, Print Screen only copies to the clipboard."),
    dict(id="CT-07", family="Device Basics", name="Connect to Wi-Fi", risk="low",
         types=["wifi_connect"],
         expected="A checkmark appears next to the network and the Wi-Fi symbol shows at the top of the screen.",
         failure="The network doesn't appear in the list, or the password is rejected."),
    # ---------------- B. Communication ----------------
    dict(id="CT-08", family="Communication", name="Add a contact or LINE friend", risk="low",
         types=["add_contact"],
         expected="The person appears in Contacts or the LINE friends list.",
         failure="LINE phone-number search finds nothing because the person hasn't allowed being added by phone number."),
    dict(id="CT-09", family="Communication", name="Block a caller or sender", risk="low",
         types=["block_number"],
         expected="Calls or messages from that person stop; they are not notified.",
         failure="On iPhone a blocked caller can still leave a voicemail (without a notification)."),
    dict(id="CT-10", family="Communication", name="Start a group chat", risk="low",
         types=["group_text"],
         expected="One message reaches everyone, and everyone sees the replies.",
         failure="An iPhone group with Android users won't send unless MMS Messaging is on; in LINE, people must be friends first."),
    dict(id="CT-11", family="Communication", name="Share location with family", risk="medium",
         types=["share_location"],
         expected="The family member can see the user's location in Find My or Google Maps.",
         failure="Google Maps sharing needs the recipient's Gmail address (otherwise use a link); Find My needs iOS 15 or later on both phones."),
    dict(id="CT-12", family="Communication", name="Attach a photo to an email", risk="low",
         types=["email_attach"],
         expected="The attachment's name appears in the message before sending.",
         failure="Files over 25 MB are added as a Google Drive link instead of an attachment."),
    # ---------------- C. Online Safety ----------------
    dict(id="CT-13", family="Online Safety", name="Someone claiming to be family or a friend asks for money", risk="high",
         types=["family_emergency_scam", "impersonation_borrow_money"],
         expected="The user pauses, calls the person at a number they already have, and doesn't send money.",
         failure="The voice sounds real (voice cloning), or money or codes were already sent."),
    dict(id="CT-14", family="Online Safety", name="Someone claiming to be an authority calls", risk="high",
         types=["government_impersonation"],
         expected="The user hangs up and checks with the agency using its official number.",
         failure="The user already shared a Social Security number or bank details (see IdentityTheft.gov / 165)."),
    dict(id="CT-15", family="Online Safety", name="Check or report a suspicious message or link", risk="high",
         types=["package_text_scam", "phishing_email", "report_spam_text", "verification_code_scam", "report_scam"],
         expected="The user doesn't click, checks through the official site or number, and reports it (7726, ReportFraud.ftc.gov, or 165).",
         failure="The user already clicked and entered card details or a code."),
    dict(id="CT-16", family="Online Safety", name="Unusual payment request", risk="high",
         types=["gift_card_scam", "romance_scam", "investment_scam", "online_shopping_scam", "online_payment_safety"],
         expected="The user refuses gift cards, wire transfers, crypto, or private transfers, and talks to someone they trust.",
         failure="The user already paid: contact the gift card company or bank right away and report it."),
    dict(id="CT-17", family="Online Safety", name="Protect an account", risk="high",
         types=["account_password_reset", "two_step_verification", "strong_passwords", "account_security"],
         expected="The account has a strong, unique password and 2-step verification turned on.",
         failure="Account recovery doesn't work right away (try again in a few days); never share codes with anyone."),
]

# One existing draft per core task, mixing variants (a/b/c/d) and languages,
# plus the 3 failure-recovery drafts. Variant d also shows clarification
# (its first assistant turn asks a question).
CHECKPOINT = [
    ("CT-01", "tr022-c"), ("CT-02", "tr033-b"), ("CT-03", "tr101-a"), ("CT-04", "tr032-a"),
    ("CT-05", "tr058-d"), ("CT-06", "tr027-c"), ("CT-07", "tr031-a"), ("CT-08", "tr044-d"),
    ("CT-09", "tr045-c"), ("CT-10", "tr051-b"), ("CT-11", "tr054-d"), ("CT-12", "tr037-a"),
    ("CT-13", "tr112-c"), ("CT-14", "tr089-c"), ("CT-15", "tr040-d"), ("CT-16", "tr088-a"),
    ("CT-17", "tr085-b"),
    ("CT-01", "tr021-r"), ("CT-07", "tr007-r"), ("CT-16", "tr041-r"),
]


def variant_label(ex):
    if ex.get("style") == "failure_recovery":
        return "failure_recovery"
    turns = len(ex["messages"])
    if turns > 2:
        return "multi_turn_clarify"
    if ex["specification"] == "underspecified":
        return "incomplete_request"
    return "complete_request" if ex.get("style") == "plain" else f"complete_request ({ex.get('style')})"


def main():
    tasks = list(csv.DictReader(open(REPO / "data/tasks/train_tasks.csv", encoding="utf-8")))
    examples = {}
    files = {}
    for p in [REPO / "data/pilot/pilot_v1.jsonl"] + sorted(Path(x) for x in glob.glob(str(REPO / "data/train/*.jsonl"))):
        for line in open(p, encoding="utf-8"):
            ex = json.loads(line)
            examples[ex["id"]] = ex
            files[ex["id"]] = str(p.relative_to(REPO))

    by_type = defaultdict(list)
    for t in tasks:
        by_type[t["task_type"]].append(t)
    ex_by_task = defaultdict(list)
    for ex in examples.values():
        ex_by_task[ex["task_id"]].append(ex)

    # ---- core_tasks_v1.csv ----
    used_types = set()
    rows = []
    for ct in CORE_TASKS:
        tids = [t["task_id"] for ty in ct["types"] for t in by_type[ty]]
        assert tids, f"{ct['id']}: no tasks for {ct['types']}"
        used_types.update(ct["types"])
        exs = [e for tid in tids for e in ex_by_task[tid]]
        plats = sorted({t["platform"] for ty in ct["types"] for t in by_type[ty]})
        langs = sorted({e["language"] for e in exs})
        srcs = {}
        for e in exs:
            for s in e["sources"]:
                srcs[s["url"]] = s["title"]
        rows.append({
            "core_task_id": ct["id"], "family": ct["family"], "core_task": ct["name"],
            "risk_level": ct["risk"], "task_types": ";".join(ct["types"]), "task_ids": ";".join(tids),
            "platforms": "; ".join(plats), "languages": ";".join(langs), "n_examples": len(exs),
            "expected_result": ct["expected"], "common_failure": ct["failure"],
            "source_urls": " ".join(srcs), "_sources": srcs,
        })

    out = REPO / "data/tasks"
    fields = [k for k in rows[0] if not k.startswith("_")]
    with open(out / "core_tasks_v1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    # ---- checkpoint_verify_v1.csv ----
    ct_ids = {ct["id"] for ct in CORE_TASKS}
    ct_of_task = {tid: r["core_task_id"] for r in rows for tid in r["task_ids"].split(";")}
    vrows = []
    for ct_id, ex_id in CHECKPOINT:
        ex = examples[ex_id]
        assert ct_id in ct_ids and ct_of_task.get(ex["task_id"]) == ct_id, (ct_id, ex_id)
        vrows.append({
            "example_id": ex_id, "core_task_id": ct_id, "file": files[ex_id],
            "variant": variant_label(ex), "language": ex["language"],
            "sensitive": ex["sensitive"], "source_urls": " ".join(s["url"] for s in ex["sources"]),
            "reviewer": "", "steps_match_source": "", "edited": "", "reviewed_on": "", "notes": "",
        })
    with open(out / "checkpoint_verify_v1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(vrows[0]))
        w.writeheader()
        w.writerows(vrows)

    # ---- core_tasks_v1.md ----
    fam_order = ["Device Basics", "Communication", "Online Safety"]
    md = ["# core_tasks_v1", "",
          "Generated by `scripts/core_tasks.py`. A core task is one user goal; it groups existing",
          "training tasks (task_ids), so no examples were changed.", "",
          "| Family | Core tasks | Examples |", "|---|---|---|"]
    for fam in fam_order:
        fr = [r for r in rows if r["family"] == fam]
        md.append(f"| {fam} | {len(fr)} | {sum(r['n_examples'] for r in fr)} |")
    md.append(f"| **Total** | **{len(rows)}** | **{sum(r['n_examples'] for r in rows)}** |")
    for fam in fam_order:
        md += ["", f"## {fam}", ""]
        for r in (r for r in rows if r["family"] == fam):
            md += [f"### {r['core_task_id']} {r['core_task']}",
                   f"- **Risk level:** {r['risk_level']}",
                   f"- **Platforms:** {r['platforms']} ({r['languages']}; {r['n_examples']} examples)",
                   f"- **Task IDs:** {r['task_ids'].replace(';', ', ')}",
                   f"- **Expected result:** {r['expected_result']}",
                   f"- **Common failure:** {r['common_failure']}",
                   "- **Sources:**"]
            md += [f"  - [{title}]({url})" for url, title in r["_sources"].items()]
            md.append("")
    vc = Counter(v["variant"].split(" (")[0] for v in vrows)
    md += ["## Checkpoint verify list", "",
           f"`checkpoint_verify_v1.csv` lists {len(vrows)} examples: one per core task plus "
           f"{vc['failure_recovery']} failure-recovery drafts.", "",
           "| Variant | Count |", "|---|---|"]
    md += [f"| {k} | {n} |" for k, n in sorted(vc.items())]
    md += ["", f"Languages: {dict(Counter(v['language'] for v in vrows))}", "",
           "For each example: check the steps against the cited source (on a real device if possible),",
           "edit the wording, set `reviewed: true` in the JSONL, and fill in the CSV columns.", "",
           "## Extended pool", "",
           f"{len(set(by_type) - used_types)} other task types stay as a draft pool for Phase 2."]
    (out / "core_tasks_v1.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"{len(rows)} core tasks, {sum(r['n_examples'] for r in rows)} examples in core tasks")
    for fam in fam_order:
        fr = [r for r in rows if r["family"] == fam]
        print(f"  {fam}: {len(fr)} tasks, {sum(r['n_examples'] for r in fr)} examples")
    print(f"verify list: {len(vrows)} examples, variants {dict(vc)}")
    print(f"extended pool: {len(set(by_type) - used_types)} task types")


if __name__ == "__main__":
    main()
