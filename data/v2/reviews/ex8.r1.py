# Reviews for batch ex8, round 1. Independent reviewer.
# Sources fetched with WebFetch on 2026-11-13 (all 9 URLs readable).

S_ALL2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}
SRC_FAIL = {"source": "fail", "safety": "pass", "duplicate": "pass"}


def s(**kw):
    d = dict(S_ALL2)
    d.update(kw)
    return d


# ---------- Task tr104: Chrome bookmark (support.google.com/chrome/answer/188842) ----------
RA_104 = [
    "Go to the page you want to save (critical)",
    "Click the Bookmark icon to the right of the address bar (critical)",
    "To open it later: select it in the bookmarks bar; turn the bar on with More > Bookmarks and lists > Show bookmarks bar",
    "Or: More > Bookmarks and lists > Bookmark Manager (or type @bookmarks in the address bar) and select the bookmark",
]
UNSUP_104 = [
    "'the **More** menu (three dots)' -> the page says only 'At the top right, select More'; it never describes the icon as three dots",
    "'If you see the **bookmarks bar** under the address bar' -> the page does not say where the bar appears ('below'/'under' do not occur on the page)",
]
FIX_104 = ("In 'To find it later', replace 'If you see the **bookmarks bar** under the address bar, click the bookmark there.' "
           "with 'If the **bookmarks bar** is showing, click the bookmark there.' and replace 'click the **More** menu (three dots)' "
           "with 'click **More** at the top right'. Leave everything else unchanged.")
ASK_104 = ("Replace the reply with exactly one question and no steps: 'You can bookmark it. Which browser are you using, like "
           "**Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?'")

# ---------- Task tr105: Gmail unsubscribe (support.google.com/mail/answer/15433283) ----------
RA_105 = [
    "Go to Gmail at mail.google.com on a computer",
    "Open an email from the sender (critical)",
    "Next to the sender's name, click Unsubscribe (critical)",
    "In the pop-up, click Unsubscribe or Go to website (critical)",
    "Optional: on the left click More > Manage subscriptions to see all subscriptions",
    "Expect it may take a few days for the emails to stop",
]
UNSUP_105 = [
    "'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' "
    "-> the cited unsubscribe page gives no such warning; and the Gmail spam page (1366858) says a suspicious message should be reported "
    "as phishing, not spam, so 'report it as spam' is also not the official advice",
]
FIX_105_CORE = (
    "(1) Split step 1 into two steps: '1. Go to **mail.google.com**.' and '2. Open an email from the sender.' and renumber the rest. "
    "(2) Delete 'Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it.' "
    "Add https://support.google.com/mail/answer/1366858 as a second source and put in its place: "
    "'If you're not sure an email is from a sender you trust, don't reply or open any links in it.' "
    "Keep 'It can take a few days for the emails to stop.'"
)
ASK_105 = ("Replace the reply with one question (one question mark): 'There are a few ways. Which email do you use, like **Gmail**, "
           "and are the emails from **stores or newsletters** you signed up for, or from **strangers**?'")

# ---------- Task tr106: Gmail recover deleted (support.google.com/mail/answer/7401) ----------
RA_106 = [
    "Go to Gmail on a computer",
    "On the left, click More, then Trash (critical)",
    "Check the box next to the message (critical)",
    "At the top, click Move to (critical)",
    "Choose Inbox (critical)",
    "Know that messages can be recovered only up to 30 days after deletion",
]

# ---------- Task tr107: Gmail report spam (support.google.com/mail/answer/1366858) ----------
RA_107 = [
    "Open Gmail in a browser on the computer",
    "Select the email(s) (critical)",
    "At the top, click Report spam (critical)",
]
ASK_107 = ("Replace the reply with one question: 'I can help. Which email do you use, like **Gmail**, and are you on a "
           "**computer** or a **phone**?'")

# ---------- Task tr108: iPhone rotation lock (support.apple.com 118226 + 105001) ----------
RA_108 = [
    "Open Control Center: Face ID iPhone swipe down from the top-right corner; Home button iPhone swipe up from the bottom (critical)",
    "Tap the Portrait Orientation Lock button (critical)",
    "Close Control Center",
]
UNSUP_108 = [
    "'It has a **lock** icon.' -> neither page describes the button's look in text (118226 only has image alt text 'Lock Rotation switch button')",
]
FIX_108_CORE = "Delete the sentence 'It has a **lock** icon.' from step 2. Leave the rest unchanged."

# ---------- Task tr109: Android auto-rotate (support.google.com/accessibility/android/answer/6006961) ----------
RA_109 = [
    "Open the Settings app (critical)",
    "Tap Display & touch (critical)",
    "Select Auto-rotate screen to turn it off (critical)",
]

# ---------- Task tr110: force restart iPhone (support.apple.com/en-us/116940) ----------
RA_110_ALL = [
    "Face ID iPhone: press and quickly release volume up (critical)",
    "Face ID iPhone: press and quickly release volume down (critical)",
    "Face ID iPhone: press and hold the side button until the Apple logo appears, may take longer than 10 seconds (critical)",
    "iPhone 7/7 Plus: hold side button and volume down together until the Apple logo",
    "iPhone 6s and earlier: hold Home button and side or top button until the Apple logo (around 10 seconds)",
    "If it doesn't turn on, charge for one hour and try again",
]
RA_110_FACEID = RA_110_ALL[:3] + [RA_110_ALL[5]]

# ---------- Task tr111: iPhone won't charge (support.apple.com/en-ca/108805) ----------
RA_111 = [
    "Plug into a power source: computer, power accessory, or wall power outlet",
    "Restart the iPhone",
    "Check the charging cable and USB adapter for damage; don't use damaged accessories",
    "Use a wall power outlet with firm connections, or try a different outlet",
    "Remove debris from the charging port and plug the cable in firmly (critical)",
    "Let it charge for half an hour (critical)",
    "If it still won't power on or shows a battery icon, force restart with the model-specific buttons (critical)",
    "Let it charge for another half hour",
    "If it still won't power on or charge, it might need service",
]
COV_111 = [True, False, True, True, True, True, True, True, True]
UNSUP_111 = [
    "'Plug into a wall outlet instead of a computer or power strip.' -> the page lists 'Computer' as an acceptable power source in its "
    "first step and never mentions a power strip; the wall-outlet advice is a later step about firm connections",
]
FIX_111_CORE = (
    "Rewrite the numbered list to follow the page: "
    "1. '**Restart your iPhone.**' "
    "2. '**Check the cable and adapter** for damage, like breaks or bent prongs. Don't use a damaged one.' "
    "3. '**Plug into a wall outlet** and make sure the cable, adapter, and outlet are firmly connected, or try a different outlet.' "
    "4. keep the charging-port step as is. "
    "5. '**Leave it charging for half an hour.**' "
    "6. 'If it still won't turn on or only shows a battery picture, **force restart** it. On an iPhone 8 or later: press and quickly "
    "release **volume up**, press and quickly release **volume down**, then press and hold the **side button** until you see the "
    "**Apple logo**. On an older iPhone, tell me the model and I'll give you those steps.' (put each button press on its own line) "
    "7. '**Charge it for another half hour.**' "
    "Delete 'instead of a computer or power strip'. Keep the service line and the 80% note. Stay under the 2,200-character cap."
)


REVIEWS = [
    # ---------------- tr104 ----------------
    {
        "id": "tr104-a",
        "required_actions": RA_104,
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_104,
        "scores": s(),
        "decision": "revise",
        "reasons": "Steps are right, but two details are added from memory: the More icon described as three dots, and the bar's location 'under the address bar'.",
        "fix": FIX_104,
    },
    {
        "id": "tr104-b",
        "required_actions": ["Ask ONE question to learn the browser and device (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions (two question marks).",
        "fix": ASK_104,
    },
    {
        "id": "tr104-c",
        "required_actions": ["Ask ONE question to learn the browser and device (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "Two questions (bookmark vs save a copy, then browser). It also does not ask computer or phone, which changes the steps.",
        "fix": "Replace the reply with exactly one question: 'Sure. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?'",
    },
    {
        "id": "tr104-d",
        "required_actions": RA_104,
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_104,
        "scores": s(),
        "decision": "revise",
        "reasons": "The final reply repeats tr104-a, including the same two unsupported details. The first assistant turn asks two questions.",
        "fix": FIX_104 + " Also replace the first assistant turn with the revised tr104-b question: 'You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?'",
    },
    # ---------------- tr105 ----------------
    {
        "id": "tr105-a",
        "required_actions": RA_105,
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_105,
        "scores": s(actionable=1),
        "decision": "revise",
        "reasons": "Adds a safety warning that is not on the cited page and differs from Gmail's official advice (suspicious mail should be reported as phishing). Step 1 holds two actions.",
        "fix": FIX_105_CORE,
    },
    {
        "id": "tr105-b",
        "required_actions": ["Ask ONE question to learn the email service and the kind of emails (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": ASK_105,
    },
    {
        "id": "tr105-c",
        "required_actions": RA_105,
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_105,
        "scores": s(actionable=1, plain=1),
        "decision": "revise",
        "reasons": "Same unsupported warning and two-action step 1 as tr105-a. The intro is pasted twice: 'Unsubscribing will stop new ones from piling up:' followed by a second intro, 'Gmail can unsubscribe you in a couple of clicks.'",
        "fix": "Replace the first two lines with: 'That's a lot of clutter. Unsubscribing stops new ones from piling up, and Gmail can do it in a couple of clicks per sender.' Then: " + FIX_105_CORE,
    },
    {
        "id": "tr105-d",
        "required_actions": RA_105,
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_105,
        "scores": s(actionable=1),
        "decision": "revise",
        "reasons": "The final reply has the same unsupported warning and two-action step 1 as tr105-a. The first assistant turn asks two questions.",
        "fix": FIX_105_CORE + " Also replace the first assistant turn with the revised tr105-b question: 'There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?'",
    },
    # ---------------- tr106 ----------------
    {
        "id": "tr106-a",
        "required_actions": RA_106,
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr106-b",
        "required_actions": ["Ask ONE question to learn what was deleted and on which device or app (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "Two question marks: '(an email, a photo, a file?)' and '...device or app?'",
        "fix": "Replace the reply with: 'Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?' (one question mark).",
    },
    {
        "id": "tr106-c",
        "required_actions": ["Ask ONE question to learn the email service and device (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": "Replace the reply with: 'It looks like your message got cut off. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?'",
    },
    {
        "id": "tr106-d",
        "required_actions": RA_106,
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "Final reply is correct. Note: the first assistant turn is the tr106-b question (two question marks); if tr106-b is revised, update this opening to match.",
        "fix": "",
    },
    # ---------------- tr107 ----------------
    {
        "id": "tr107-a",
        "required_actions": RA_107,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr107-b",
        "required_actions": ["Ask ONE question to learn the email service and device (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": ASK_107,
    },
    {
        "id": "tr107-c",
        "required_actions": ["Ask ONE question to learn whether it is spam email, texts, or calls (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA"),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr107-d",
        "required_actions": RA_107,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "Final reply is correct. Note: the first assistant turn is the tr107-b question (two questions); if tr107-b is revised, update this opening to match.",
        "fix": "",
    },
    # ---------------- tr108 ----------------
    {
        "id": "tr108-a",
        "required_actions": RA_108,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_108,
        "scores": s(),
        "decision": "revise",
        "reasons": "Describes the button as having a lock icon, which the cited pages do not say in text.",
        "fix": FIX_108_CORE,
    },
    {
        "id": "tr108-b",
        "required_actions": ["Ask ONE question to learn iPhone or Android (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA"),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr108-c",
        "required_actions": RA_108,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_108,
        "scores": s(plain=1),
        "decision": "revise",
        "reasons": "Has the same unsupported lock-icon sentence. The intro is pasted twice: 'You can stop that by locking the screen upright:' and then 'You can lock the screen so it stays upright.'",
        "fix": "Replace the first two lines with: 'That sounds annoying. You can lock the screen so it stays upright. It takes a few seconds.' " + FIX_108_CORE,
    },
    {
        "id": "tr108-d",
        "required_actions": RA_108,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_108,
        "scores": s(),
        "decision": "revise",
        "reasons": "The final reply has the same unsupported lock-icon sentence as tr108-a.",
        "fix": FIX_108_CORE,
    },
    # ---------------- tr109 ----------------
    {
        "id": "tr109-a",
        "required_actions": RA_109,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "Steps match the page exactly. 'Menu names can be a little different on some phones' is not on the page; I accepted it as a hedge that asks the user to report back, not as a factual step.",
        "fix": "",
    },
    {
        "id": "tr109-b",
        "required_actions": ["Ask ONE question to learn iPhone or Android (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA"),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr109-c",
        "required_actions": ["Ask ONE question to learn the goal (stop vs allow rotation) and iPhone or Android (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": "Replace the reply with: 'Sure. Is it an **iPhone** or an **Android** phone, and do you want the screen to **stop turning sideways**, or to **turn sideways** when it won't?' (one question mark).",
    },
    {
        "id": "tr109-d",
        "required_actions": RA_109,
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "Same final reply as tr109-a. I accepted the menu-name hedge, as in tr109-a.",
        "fix": "",
    },
    # ---------------- tr110 ----------------
    {
        "id": "tr110-a",
        "required_actions": RA_110_ALL,
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(),
        "decision": "keep",
        "reasons": "The model is unknown, but the reply gives every branch, labeled by visible features as the page does, so no question is needed.",
        "fix": "",
    },
    {
        "id": "tr110-b",
        "required_actions": ["Ask ONE question to learn iPhone or Android and whether it has a Home button (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": "Replace the reply with: 'Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?' (one question mark).",
    },
    {
        "id": "tr110-c",
        "required_actions": RA_110_FACEID,
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": [
            "'An iPhone 14 has Face ID' -> page 116940 names no Face ID models (only the headings 'iPhone with Face ID' / 'iPhone with Home Button')",
        ],
        "scores": s(plain=1),
        "decision": "revise",
        "reasons": "The model claim is not on the cited page. The user gave the model, yet the reply still says 'The steps depend on your model' and lists the iPhone 7 and 6s steps. That is extra text, and the intro is pasted twice.",
        "fix": ("Add https://support.apple.com/en-ca/108805 as a second source; it gives the volume up / volume down / side button "
                "sequence for 'iPhone 8 or later'. Replace 'That's frustrating. An iPhone 14 has Face ID, so use the first set of steps:' "
                "and 'You can **force restart** it. The steps depend on your model.' and the '**iPhone with Face ID (no Home button):**' header "
                "with one line: 'That's frustrating. You can **force restart** it. On an iPhone 14, do this:'. Keep the three numbered steps. "
                "Delete the '**iPhone 7:**' and '**iPhone 6s or older ...**' lines. Keep 'If it still won't turn on, charge it for an hour and try again.'"),
    },
    {
        "id": "tr110-d",
        "required_actions": RA_110_FACEID,
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(plain=1),
        "decision": "revise",
        "reasons": "The user said there is no Home button, yet the reply says 'The steps depend on your model' and lists the iPhone 7 and 6s steps, which is extra text. The first assistant turn asks two questions.",
        "fix": ("Replace 'Thanks. For your iPhone 12, use the first set of steps.', 'You can **force restart** it. The steps depend on your model.' "
                "and the '**iPhone with Face ID (no Home button):**' header with one line: 'Thanks. Since your iPhone has no Home button, "
                "**force restart** it like this:'. Keep the three numbered steps. Delete the '**iPhone 7:**' and '**iPhone 6s or older ...**' lines. "
                "Keep the charge-for-an-hour line. Also replace the first assistant turn with the revised tr110-b question."),
    },
    # ---------------- tr111 ----------------
    {
        "id": "tr111-a",
        "required_actions": RA_111,
        "covered": COV_111,
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_111,
        "scores": s(steps=1, actionable=1),
        "decision": "revise",
        "reasons": "The wall-outlet step contradicts the page (a computer is a listed power source) and adds a power strip. The 'Restart your iPhone' step is missing. 'force restart it' gives no button steps, though the page gives them.",
        "fix": FIX_111_CORE,
    },
    {
        "id": "tr111-b",
        "required_actions": ["Ask ONE question to learn iPhone or Android and the kind of charging problem (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": "Replace the reply with: 'Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?' (one question mark).",
    },
    {
        "id": "tr111-c",
        "required_actions": ["Ask ONE question to learn the problem and the phone type (critical)"],
        "covered": [True],
        "needs_clarification": True,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=1),
        "decision": "revise",
        "reasons": "A clarification is needed, but the reply asks two questions.",
        "fix": "Replace the reply with: 'It looks like your message got cut off. Is your phone **not charging**, and is it an **iPhone** or an **Android** phone?' (one question mark).",
    },
    {
        "id": "tr111-d",
        "required_actions": RA_111,
        "covered": COV_111,
        "needs_clarification": False,
        "gates": SRC_FAIL,
        "unsupported_claims": UNSUP_111,
        "scores": s(steps=1, actionable=1, plain=1),
        "decision": "revise",
        "reasons": "Same problems as tr111-a. The intro is also pasted twice: 'Thanks. Let's go through some checks.' then 'Let's go through a few checks.' The first assistant turn asks two questions.",
        "fix": ("Replace 'Thanks. Let's go through some checks.' and the next line with: 'Thanks. Let's go through a few checks. This can take up to an hour, mostly waiting.' "
                + FIX_111_CORE + " Also replace the first assistant turn with the revised tr111-b question."),
    },
]
