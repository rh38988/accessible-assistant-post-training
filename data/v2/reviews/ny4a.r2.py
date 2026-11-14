G_OK = {"source": "pass", "safety": "pass", "duplicate": "pass"}
S_OK = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}


def R(id, acts, nc=False, scores=None, decision="keep", reasons="", fix="", unsupported=None, cov=None, gates=None):
    sc = dict(S_OK)
    if scores:
        sc.update(scores)
    if not acts:
        sc["steps"] = "NA"
    g = dict(G_OK)
    if gates:
        g.update(gates)
    return {
        "id": id,
        "required_actions": acts,
        "covered": cov if cov is not None else [True] * len(acts),
        "needs_clarification": nc,
        "gates": g,
        "unsupported_claims": unsupported or [],
        "scores": sc,
        "decision": decision,
        "reasons": reasons,
        "fix": fix,
    }


REVIEWS = [
    R("tr161-a", [
        "Swipe down with two fingers from the top right corner (critical)",
        "Tap the Settings icon (critical)",
        "Tap Software update or System updates (critical)",
        "Tap Download and install, Check for system updates, or Check for software updates; Download now if shown (critical)",
        "When the download finishes, follow the on-screen prompts to install (critical)",
    ]),
    R("tr161-c", [
        "Make sure Smart Switch is installed on the computer (critical)",
        "Connect the Galaxy with the USB cable from the box; use a USB adapter on some PCs (critical)",
        "Open Smart Switch and let it detect the phone (critical)",
        "If an update is available, select Update and follow the prompts (critical)",
        "Keep the cable connected and do not use the phone until it finishes; the phone restarts (critical)",
    ]),
    R("tr164-a", [
        "Swipe down from the top right to open the Quick settings panel (critical)",
        "Tap the Flashlight icon to turn the light on (critical)",
        "Tap the Flashlight icon again to turn it off",
    ]),
    R("tr166-e", [
        "Press the watch Home button, swipe to and tap Samsung Find (critical)",
        "If asked, tap Continue and allow the permissions (critical)",
        "Select the phone (critical)",
        "Tap the Ring icon (critical)",
        "Stop the ringing with Dismiss on the phone or Stop on the watch (critical)",
        "Watch connected to the phone by Bluetooth, or Wi-Fi/LTE (critical)",
        "The phone must be turned on and have a network connection",
        "If the watch cannot find the phone, use the SmartThings Find or Samsung Find website",
    ], cov=[True, True, True, True, True, True, False, True],
       scores={"steps": 1}, decision="revise",
       reasons="Reply omits the page's requirement that the phone must be turned on and have a network connection for the watch to locate it; the page says 'The phone must be turned on' and 'It also needs a stable network connection'. This is a non-critical precondition, so S1 is 1. The page also lists a Samsung account and Lost device protection remote controls as prerequisites; they do not change the steps, so they are not required here.",
       fix="In the closing paragraph, add one sentence directly after 'The watch must be connected to the phone by Bluetooth, Wi-Fi, or LTE.': 'The phone must be turned on and have a network connection.' Change nothing else, including the steps and the website fallback."),
]
