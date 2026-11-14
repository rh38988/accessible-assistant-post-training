# Reviews for batch fx8, round 1. Independent reviewer. All source pages readable via WebFetch.
# Extra official pages found: Apple 108330 (Control Center), Gmail 15621070 (Manage subscriptions),
# Google accessibility 7641084 (Disability Support link on the cited page).

PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}
SRCF = {"source": "fail", "safety": "pass", "duplicate": "pass"}


def sc(steps=2, ask=2, con=2, act=2, plain=2, real=2):
    return {"steps": steps, "ask_or_answer": ask, "constraints": con, "actionable": act, "plain": plain, "realistic_user": real}


def keep(id_, ra, covered=None):
    return {
        "id": id_, "required_actions": ra, "covered": covered or [True] * len(ra), "needs_clarification": False,
        "gates": PASS, "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": "",
    }


REVIEWS = [
    {
        "id": "tr104-e",
        "required_actions": ["Type @bookmarks in the address bar and press Tab or Space (or select Search bookmarks) (critical)",
                             "Enter keywords (critical)", "Choose the result (critical)",
                             "Alternative: More > Bookmarks and lists > Bookmark Manager, select the bookmark"],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": SRCF,
        "unsupported_claims": ["'Click the address bar at the top.' -> the page never says where the address bar is"],
        "scores": sc(),
        "decision": "revise",
        "reasons": "Method and the user's no-bar constraint are right and the Search bookmarks and Bookmark Manager lines are supported. Only the position 'at the top' is unsupported.",
        "fix": "Step 2: change to 'Click the address bar.' Nothing else needs to change.",
    },
    keep("tr104-r", ["Click More, then Bookmarks and lists, then Show bookmarks bar (critical)",
                     "Click the bookmark in the bar to open it", "Or More > Bookmarks and lists > Bookmark Manager"]),
    keep("tr105-e", ["Go to Gmail and open the email (critical)", "Click Unsubscribe next to the sender's name (critical)",
                     "Click Unsubscribe in the pop-up (critical)", "Go to website means finish on the sender's site",
                     "May take a few days to stop"]),
    {
        "id": "tr105-r",
        "required_actions": ["Go to Gmail; on the left click More, then Manage subscriptions (critical)",
                             "Find the store's active subscriptions there (critical)",
                             "Click Unsubscribe to the right of the store's sender entry (critical)",
                             "Note: sender may take a few days to process"],
        "covered": [True, True, False, False],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": sc(steps=1, act=1),
        "decision": "revise",
        "reasons": "The final reply stops at 'Check it for the store's other lists' and never tells the user what to do next (click Unsubscribe next to the store). The cited page does not describe the Manage subscriptions screen; the linked Gmail page does.",
        "fix": "Add a second source https://support.google.com/mail/answer/15621070?hl=en&co=GENIE.Platform%3DDesktop . Replace step 4 with: '4. Find the store in the list. To the right of its name, click **Unsubscribe**.' Add a last line: 'It can take a few days for the emails to stop.' Keep the explanation about other mailing lists.",
    },
    keep("tr106-e", ["Say deleted drafts can't be recovered from Trash (critical)", "Go to Gmail; On the left click More, then Trash",
                     "Check the box next to the message", "At the top click Move to", "Choose Inbox", "Deleted emails stay 30 days"]),
    keep("tr106-r", ["On the left click More, then Trash", "Messages are removed permanently after 30 days / Delete forever / Empty Trash now",
                     "Deleted drafts can't be recovered from Trash"]),
    keep("tr107-e", ["Open Gmail on the computer", "Select one or more emails (critical)", "At the top click Report spam (critical)",
                     "Google receives a copy of the email"]),
    keep("tr107-r", ["Open Gmail", "On the left click More, then Spam (critical)", "Check the box next to the email (critical)",
                     "At the top click Not spam (critical)"]),
    {
        "id": "tr108-e",
        "required_actions": ["Open Control Center (Home button model: swipe up from the bottom edge) (critical)",
                             "Tap Portrait Orientation Lock to lock (critical)", "Close Control Center",
                             "To turn sideways again: make sure the lock is off, then turn the iPhone",
                             "Some apps don't support rotation"],
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": SRCF,
        "unsupported_claims": ["'Swipe up from the bottom edge of the screen to open **Control Center**.' -> the cited page (118226) covers only models without a Home button and says nothing about the swipe up. It is correct per https://support.apple.com/en-us/108330 , which is not cited."],
        "scores": sc(),
        "decision": "revise",
        "reasons": "The user has an iPhone 8 (Home button). The key gesture is not on the cited page. The reply is right, but needs the second source.",
        "fix": "Add the second source https://support.apple.com/en-us/108330 (Home button models: swipe up from the bottom edge of any screen to open Control Center; tap the screen... close by tapping the top of the screen or pressing the Home button). No text change is needed, but optionally make 'Close Control Center' say 'Tap the top of the screen or press the Home button to close it.'",
    },
    {
        "id": "tr108-r",
        "required_actions": ["Swipe down from the top-right corner to open Control Center (critical)",
                             "Tap Portrait Orientation Lock (critical)", "Close Control Center"],
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": SRCF,
        "unsupported_claims": ["'Control Center opens from the corner, not the middle of the top edge.' -> the cited page says only 'swipe down from the top-right corner'. The warning about the top-center is on https://support.apple.com/en-us/108330 , not cited."],
        "scores": sc(),
        "decision": "revise",
        "reasons": "Steps correct for iPhone 13; the 'not the middle' explanation needs the Control Center page as a second source.",
        "fix": "Add the second source https://support.apple.com/en-us/108330 (it says swiping near the top-center may open Notification Center instead). No text change is needed.",
    },
    keep("tr109-e", ["Open Settings", "Go to Display & touch", "Select Auto-rotate screen to turn it off",
                     "TalkBack requires auto-rotate off"]),
    {
        "id": "tr109-r",
        "required_actions": ["Say the page gives only Settings > Display & touch > Auto-rotate screen", "Direct to the Disability Support team for more accessibility help"],
        "covered": [True, True],
        "needs_clarification": False,
        "gates": PASS,
        "unsupported_claims": [],
        "scores": sc(act=1),
        "decision": "revise",
        "reasons": "Honest and supported, but 'contact the Disability Support team' leaves a low-confidence user with no way to do it. The cited page links the contact page.",
        "fix": "Keep the text and add the contact page from the cited page: 'You can reach the Disability Support team here: https://support.google.com/accessibility/answer/7641084'. Optionally say 'Tell me what you see in Settings and I'll try to help.'",
    },
    keep("tr110-e", ["Press and quickly release volume up", "Press and quickly release volume down",
                     "Press and hold the side button until the Apple logo (may take longer than 10 seconds)",
                     "If it won't turn on, charge one hour; then service"]),
    keep("tr110-r", ["iPhone 7: hold the side button and volume down until Apple logo", "If it won't turn on, charge for one hour then try again",
                     "Might need service"]),
    keep("tr111-e", ["Check cable and adapter for damage; don't use damaged ones", "Wall outlet; check connections or try a different outlet",
                     "Clear debris from the charging port and plug in firmly", "Charge half an hour",
                     "Force restart (volume up, volume down, hold side button until Apple logo)", "Charge another half hour",
                     "Might need service"]),
    keep("tr111-r", ["Connect the iPhone directly to the charger, no adapters", "Clear debris from the charging port", "Restart the iPhone",
                     "Try a different USB cable or charger", "Make sure iOS is the latest version", "Might need service"]),
]
