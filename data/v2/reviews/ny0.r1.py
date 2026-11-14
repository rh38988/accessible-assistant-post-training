S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
OK = {"source": "pass", "safety": "pass", "duplicate": "pass"}
ASK = {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}


def R(id, req, cov=None, gates=None, unsup=None, scores=None, decision="keep", reasons="", fix="", nc=False):
    return {
        "id": id,
        "required_actions": req,
        "covered": cov if cov is not None else [True] * len(req),
        "needs_clarification": nc,
        "gates": gates or dict(OK),
        "unsupported_claims": unsup or [],
        "scores": scores or dict(S2),
        "decision": decision,
        "reasons": reasons,
        "fix": fix,
    }


FULL = ["Press and release Shift-Command-3 together (critical)", "Click the corner thumbnail to edit if it appears", "Otherwise find it on the desktop"]
CRYPTO_STOP = ["Do not pay or send crypto (critical)", "Do not click links", "Report at ReportFraud.ftc.gov"]
BK = ["Open Settings", "Tap Google, then All services", "Under Backup and restore tap Backup", "Tap Back up now"]
AUTO = ["Open Settings", "Tap Google services, then All services", "Choose Photos & videos and/or Device data", "Turn Backup on", "On appears below; can take up to 24 hours"]

REVIEWS = [
    R("tr117-a", FULL),
    R("tr117-c",
      ["Press Shift-Command-4 (critical)", "Pointer becomes crosshair", "Click and hold, drag over the area", "Release to capture", "Esc cancels"],
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'The picture is saved on your desktop unless a small picture appears in the corner' -> page: the thumbnail may appear and you can click it to edit 'or wait for the file to save to the desktop'; the file is saved to the desktop either way"],
      scores={"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
      decision="revise",
      reasons="The sentence suggests nothing is saved to the desktop when a thumbnail appears, which contradicts the source and could make the user think the screenshot is lost.",
      fix="Replace with: 'A small picture may appear in the corner of the screen. You can click it to edit the screenshot, or wait and the screenshot is saved on your desktop.'"),
    R("tr117-b", [], [], scores=ASK, nc=True),
    R("tr117-d", FULL),
    R("tr117-e", ["Press and release Control-Shift-Command-3 (critical)", "Control adds copy to Clipboard instead of saving a file", "Optional: Control-click thumbnail > Save to Clipboard"]),
    R("tr117-r", ["Screenshot was saved on the desktop", "Look for a file named Screen Shot with date and time", "Shift-Command-5 > Options > show floating thumbnail"]),
    R("tr118-a", AUTO),
    R("tr118-c", BK + ["Covers apps, contacts, call history, settings, texts; photos via Google Photos", "Work phone cannot back up"]),
    R("tr118-b", [], [], scores=ASK, nc=True),
    R("tr118-d", BK + ["Work phone cannot back up"]),
    R("tr118-e", AUTO[:2] + ["Choose only Photos & videos, leave Device data off"] + AUTO[3:]),
    R("tr118-r", ["Wait; backup can take up to 24 hours", "Check Backup is on and Device data chosen", "On appears below when saved"]),
    R("tr119-c", ["Select the Microsoft Store icon on the taskbar (or Start > Microsoft Store)", "Choose Gaming", "Show all to see more"]),
    R("tr119-b", [], [], scores=ASK, nc=True),
    R("tr119-e", ["Open Microsoft Store from the taskbar", "Select More info next to account picture", "Select My Library", "Select the Download icon next to the app", "Order history for apps not installed"],
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'with no new purchase' -> page does not say reinstalling is free of charge",
             "'Make sure you are signed in with the same Microsoft account you used before.' -> not on the page"],
      decision="revise",
      reasons="Two assurances are added from memory. The steps themselves match the page.",
      fix="Change the opening to 'You can look for it in your Library and download it again.' Delete the sentence 'Make sure you are signed in with the same Microsoft account you used before.' Keep steps 1 to 5 and the Order history line."),
    R("tr120-a", CRYPTO_STOP + ["Search the name with review, scam, complaint"]),
    R("tr120-c", CRYPTO_STOP),
    R("tr120-e", ["Do not add more money (critical)", "Stop clicking her links", "Report at ReportFraud.ftc.gov, sec.gov/tcr, CFTC.gov/complaint", "Contact the exchange if crypto sent"]),
    R("tr120-r", ["Do not send more", "Contact the exchange", "Report at ReportFraud.ftc.gov, CFTC.gov/complaint, sec.gov/tcr, ic3.gov/Home/FileComplaint", "Crypto usually not reversible"]),
    R("tr120-f", ["Ask her not to send anything or click links", "Search name and coin with review, scam, complaint", "Report at ReportFraud.ftc.gov", "Contact the exchange if already sent"]),
    R("tr120-g", ["Warning signs: guaranteed profits, unexpected contact, love interest advice, vague explanations", "Do not click unexpected links", "Search name and crypto with review, scam, complaint", "Report at ReportFraud.ftc.gov"]),
]
