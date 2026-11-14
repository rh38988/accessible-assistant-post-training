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



NA = {"steps": "NA"}
DESK = ["Click the Show captions icon in the meeting toolbar (critical)", "If not visible: More > Show captions",
        "Captions appear above the toolbar (speaker name shown)",
        "If restricted: More > Request captions > Send; host/co-host approves"]
MOB = ["Tap More in the toolbar (critical)", "Tap Show CC (critical)", "Captions appear above meeting controls",
       "If restricted: More > Request captions > Send; host approves"]
R("tr206-a", DESK, [True] * 4, False)
R("tr206-c", MOB, [True] * 4, False)
R("tr206-d", MOB, [True] * 4, False)
R("tr206-e", ["Show captions icon, or More > Show captions (critical)", "Hover over captions and click the gear icon (critical)",
              "Click Caption settings; Accessibility panel opens on right (critical)", "Move Font size slider (critical)",
              "Changes only visible to the user", "If restricted: More > Request captions > Send; host approves"], [True] * 6, False)
R("tr206-r", ["Click Show captions icon, or More > Show captions", "If nothing: More > Request captions (critical)", "Click Send (critical)",
              "Host/co-host must approve", "If Request captions is absent, host may have disabled captions; ask the host"], [True] * 5, False)
