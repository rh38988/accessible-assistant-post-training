# Reviews for batch fx8, round 2 (re-review of revised examples). Independent reviewer.
# Sources reviewed in order: Chrome 188842; Gmail 15433283 and 15621070; Apple 118226 and 108330; Google accessibility 6006961.

PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}


def sc(steps=2, ask=2, con=2, act=2, plain=2, real=2):
    return {"steps": steps, "ask_or_answer": ask, "constraints": con, "actionable": act, "plain": plain, "realistic_user": real}


def keep(id_, ra, covered=None):
    return {
        "id": id_, "required_actions": ra, "covered": covered or [True] * len(ra), "needs_clarification": False,
        "gates": PASS, "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": "",
    }


REVIEWS = [
    keep("tr104-e", ["Type @bookmarks in the address bar, then press Tab or Space (critical)",
                     "Type a keyword from the site's name (critical)",
                     "Click the bookmark in the list (critical)",
                     "Alternative: click Search bookmarks in the suggestions",
                     "Alternative: More > Bookmarks and lists > Bookmark Manager, then click the bookmark"]),
    keep("tr105-r", ["Go to Gmail; on the left click More, then Manage subscriptions (critical)",
                     "Find the store in the list (critical)",
                     "To the right of the store's entry, click Unsubscribe (critical)",
                     "Note: emails may keep arriving for a few days"]),
    keep("tr108-e", ["Open Control Center: swipe up from the bottom edge (Home button model) (critical)",
                     "Tap Portrait Orientation Lock to lock the screen (critical)",
                     "Close Control Center: tap the top of the screen or press the Home button",
                     "To turn sideways again: open Control Center, make sure the lock is off, close it, turn the iPhone",
                     "Some apps do not rotate, even with the lock off"]),
    keep("tr108-r", ["Open Control Center: swipe down from the top-right corner (critical)",
                     "Tap Portrait Orientation Lock (critical)",
                     "Close Control Center"]),
    keep("tr109-r", ["Say the page gives only Settings > Display & touch > Auto-rotate screen (critical)",
                     "Say that the steps do not confirm another place for this setting on the user's phone",
                     "Direct the user to the Disability Support team contact page for more accessibility help"]),
]
