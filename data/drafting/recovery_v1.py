"""Draft failure-recovery examples by extending existing verified examples.

Each recovery example = an existing example's conversation + a user turn
reporting that something went wrong + an assistant reply that helps recover.
The earlier turns are copied from the source example, so the first answer
stays identical to the one already in the dataset.

Run from the repo root:
    python data/drafting/recovery_v1.py
Writes data/train/recovery_v1.jsonl
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
ACCESSED = "2026-10-24"


def load(path):
    return {r["id"]: r for r in map(json.loads, open(REPO / path, encoding="utf-8"))}


pilot = load("data/pilot/pilot_v1.jsonl")
b01 = load("data/train/batch_01.jsonl")
b02 = load("data/train/batch_02.jsonl")

RECOVERY = [
    {
        "base": b01["tr021-a"], "id": "tr021-r",
        "extra_sources": [],
        "user": "I made it really big and now some of the buttons are cut off and hard to tap.",
        "reply": """That can happen when the text is set very large. Let's make it a little smaller so the buttons fit again.

1. Open **Settings**.
2. Tap **Display & Brightness**, then **Text Size**.
   If you used **Larger Text** instead, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**.
3. Drag the slider **one step to the left**.
4. Go back to the app and check the buttons.

Repeat until the buttons fit on the screen and the text is still easy for you to read.""",
    },
    {
        "base": pilot["pilot-007"], "id": "tr007-r",
        "extra_sources": [],  # base example already cites the Wi-Fi troubleshooting page
        "user": "I don't see SmithHome in the list at all.",
        "reply": """Let's check a few things. Try them in order, and stop as soon as **SmithHome** appears in the list.

1. **Check the internet box.** Make sure your daughter's router is plugged in and its lights are on. Ask her whether other phones in the house can connect.
2. **Move closer** to the router, then look at the list again.
3. **Check Airplane Mode.** In **Settings**, make sure **Airplane Mode** is turned off.
4. **Restart your iPhone**, then open **Settings** and **Wi-Fi** again.
5. **Restart the router.** Unplug the router and the modem, then plug them back in. Ask your daughter first, because this turns off the internet for everyone in the house for a few minutes.

If SmithHome still doesn't show up, tell me which network names you do see.""",
    },
    {
        "base": b02["tr041-a"], "id": "tr041-r",
        "extra_sources": [],
        "user": "Oh no. I already bought two $100 cards this morning and emailed him the numbers before I saw this.",
        "reply": """I'm sorry this happened. This scam fools a lot of careful people. Acting quickly gives you the best chance of getting money back.

1. **Contact the gift card company right away.** Tell them the cards were used in a scam and ask for your money back. Sometimes they can freeze money that hasn't been spent yet. The FTC's gift card scam page lists contact information for major gift card companies.
2. **Keep the cards and the store receipt.** You'll need them when you report it.
3. **Report the scam** at **ReportFraud.ftc.gov**.
4. **Don't reply** to the email, and don't buy more cards, even if you're asked again.
5. **Tell your church office**, so they can warn other members.

Do you have the cards and the receipt with you? If so, we can look at step 1 together.""",
    },
]


def build(spec):
    base = spec["base"]
    sources = list(base["sources"]) + [
        {"title": t, "url": u, "accessed": ACCESSED} for t, u in spec["extra_sources"]
    ]
    return {
        **{k: v for k, v in base.items() if k not in ("id", "messages", "sources", "style", "inspired_by")},
        "id": spec["id"],
        "messages": base["messages"] + [
            {"role": "user", "content": spec["user"]},
            {"role": "assistant", "content": spec["reply"]},
        ],
        "specification": "fully_specified",
        "sources": sources,
        "inspired_by": "original",
        "style": "failure_recovery",
        "author": "claude-draft",
        "reviewed": False,
    }


out = REPO / "data/train/recovery_v1.jsonl"
with open(out, "w", encoding="utf-8") as f:
    for spec in RECOVERY:
        f.write(json.dumps(build(spec), ensure_ascii=False) + "\n")
print(f"wrote {len(RECOVERY)} examples to {out.relative_to(REPO)}")
