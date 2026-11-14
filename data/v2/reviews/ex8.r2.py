REVIEWS = []


def R(id, req, cov, clar, src="pass", safe="pass", dup="pass", unsup=None, scores=None, decision="keep", reasons="", fix=""):
    sc = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
    if scores:
        sc.update(scores)
    REVIEWS.append({
        "id": id, "required_actions": req, "covered": cov, "needs_clarification": clar,
        "gates": {"source": src, "safety": safe, "duplicate": dup},
        "unsupported_claims": unsup or [], "scores": sc,
        "decision": decision, "reasons": reasons, "fix": fix,
    })


# ---- Page: Chrome bookmark (188842)
BK = ["Go to the website (critical)", "Click the bookmark icon to the right of the address bar (critical)",
      "Find later: click bookmark on bookmarks bar, show via More > Bookmarks and lists > Show bookmarks bar", "Or More > Bookmarks and lists > Bookmark Manager"]
R("tr104-a", BK, [True] * 4, False)
NA = {"steps": "NA"}
R("tr104-b", [], [], True, scores=NA)
R("tr104-c", [], [], True, scores=NA)
R("tr104-d", BK, [True] * 4, False)

# ---- Page: Gmail unsubscribe (15433283 + 1366858)
UN = ["Go to mail.google.com", "Open an email from the sender", "Click Unsubscribe next to sender name (critical)",
      "Click Unsubscribe in the pop-up to confirm (critical)", "If 'Go to website' appears, unsubscribe on the sender's site",
      "More (left) > Manage subscriptions to see all", "May take a few days; do not reply/open links in suspicious email (1366858)"]
R("tr105-a", UN, [True] * 7, False)
R("tr105-b", [], [], True, scores=NA)
R("tr105-c", UN, [True] * 7, False)
R("tr105-d", UN, [True] * 7, False)

# ---- Page: Gmail restore deleted email (7401) and spam (1366858): clarifying replies only
R("tr106-b", [], [], True, scores=NA)
R("tr106-c", [], [], True, scores=NA)
R("tr107-b", [], [], True, scores=NA)

# ---- Page: Apple rotate screen (118226 + 105001)
LK = ["Open Control Center: swipe down from top-right (Face ID) / swipe up from bottom (Home button) (critical)",
      "Tap the Portrait Orientation Lock button (critical)", "Close Control Center", "Tap the same button again to allow rotation"]
R("tr108-a", LK, [True] * 4, False)
R("tr108-c", LK, [True] * 4, False)
R("tr108-d", LK, [True] * 4, False)
# ---- Android rotate (6006961): clarifying only
R("tr109-c", [], [], True, scores=NA)

# ---- Page: Apple force restart (116940 + 108805)
R("tr110-b", [], [], True, scores=NA)
FR = ["Press and quickly release volume up (critical)", "Press and quickly release volume down (critical)",
      "Press and hold the side button until the Apple logo appears, may take over 10 seconds (critical)",
      "If it still won't turn on, charge for an hour and try again"]
R("tr110-c", FR, [True] * 4, False)
R("tr110-d", FR, [True] * 4, False)

# ---- Page: Apple iPhone won't charge (108805)
CH = ["Restart the iPhone", "Check cable and adapter for damage; don't use damaged ones", "Use a wall outlet / check firm connections or try another outlet",
      "Remove debris from the charging port, plug in firmly", "Charge for half an hour",
      "If still won't turn on / battery icon: force restart (iPhone 8 or later: vol up, vol down, hold side until Apple logo) (critical)",
      "Charge another half hour", "If still failing, get service from Apple"]
R("tr111-a", CH, [True] * 8, False)
R("tr111-b", [], [], True, scores=NA)
R("tr111-c", [], [], True, scores=NA)
R("tr111-d", CH, [True] * 8, False, scores={"plain": 1},
  decision="revise",
  reasons="The user said the phone 'doesn't charge at all' (not stopping partway), yet the reply still ends with the 80% note, which answers the 'stop partway' case the user ruled out. Extra text the task does not need.",
  fix="In the final assistant reply, delete the last paragraph '**If it stops at 80%:** that's usually a battery-saving feature, not a problem.' Leave everything else unchanged (keep tr111-a as is, since that user did not say which problem).")
