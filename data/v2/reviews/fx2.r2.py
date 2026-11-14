S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
G = {"source": "pass", "safety": "pass", "duplicate": "pass"}


def sc(**kw):
    d = dict(S2)
    d.update(kw)
    return d


def keep(id, ra):
    return {"id": id, "required_actions": ra, "covered": [True] * len(ra), "needs_clarification": False,
            "gates": dict(G), "unsupported_claims": [], "scores": dict(S2), "decision": "keep", "reasons": "", "fix": ""}


REVIEWS = [
    {
        "id": "tr016-e",
        "required_actions": ["Do not send money to anyone who insists on one specific payment method (critical)",
                             "Search the seller's name with words like review, scam, complaint",
                             "Credit card is advised for dispute protection (user cannot use one)",
                             "Report scams at ReportFraud.ftc.gov", "More advice at ftc.gov/scams"],
        "covered": [True, True, True, True, True], "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": ["'Tickets going fast is the kind of pressure scammers use.' -> the FTC page says nothing about pressure or urgency tactics; its only time-related advice is 'Don't delay if you paid a scammer.'"],
        "scores": sc(),
        "decision": "revise",
        "reasons": "One sentence is not on the cited page (urgency or pressure claim). Everything else is supported and the protective action comes first.",
        "fix": "Delete the sentence 'Tickets going fast is the kind of pressure scammers use.' Optionally keep the opening as: 'A seller who says you can only pay with a payment app is probably a scammer.' (the page says anyone who says you can only pay in one of these ways is probably a scammer). Do not add other claims about urgency.",
    },
    keep("tr024-e", ["Buttons change media volume while using music, video or games",
                     "When no other app is in use, the buttons adjust the ringer volume", "Mention the Silent mode check"]),
    {
        "id": "tr024-r",
        "required_actions": ["Recognize orange on the side as Silent mode (phone vibrates for calls)", "Flip the Ring/Silent switch so orange is not showing (critical)",
                             "Press volume up with no other app in use"],
        "covered": [True, True, True], "needs_clarification": False, "gates": dict(G),
        "unsupported_claims": [],
        "scores": sc(plain=1),
        "decision": "revise",
        "reasons": "The user already described an orange mark on the side, so the switch applies. The last paragraph ('If you have an iPhone 15 Pro or a newer model, there is no switch. The Action button toggles Silent mode...') is about other models and gives no way to use the Action button (the page gives no gesture). It adds clutter for a low-confidence user. The page also never says outright that newer models 'have no switch'. The favorites line is not needed for this fix.",
        "fix": "Delete the final paragraph about iPhone 15 Pro, newer models and favorite contacts. Keep steps 1 to 3 and the first sentence about orange meaning Silent mode.",
    },
    keep("tr025-e", ["Press a volume button", "Tap the Down arrow on the right", "Choose Ring", "Slide the Ring level"]),
    keep("tr025-r", ["Press a volume button", "Tap the Down arrow on the right (older Android)", "Choose Ring", "Slide the Ring level"]),
    {
        "id": "tr026-r",
        "required_actions": ["Check the carrier supports Wi-Fi Calling and the iPhone has the latest software before troubleshooting",
                             "Confirm Settings > Cellular > Wi-Fi Calling is on", "Restart the iPhone",
                             "Connect to a different Wi-Fi network (not all networks support it)", "Turn Wi-Fi Calling off, then on",
                             "Settings > General > Transfer or Reset iPhone > Reset > Reset Network Settings",
                             "Pause about two minutes between steps", "If still failing and the carrier supports it, contact the carrier"],
        "covered": [True, True, True, True, True, False, True, True], "needs_clarification": False, "gates": dict(G),
        "unsupported_claims": [],
        "scores": sc(steps=1, actionable=1),
        "decision": "revise",
        "reasons": "The page's last troubleshooting step (Reset Network Settings) is missing. Step 1 bundles two separate checks (carrier support and software update) with no way to do either.",
        "fix": "Split step 1 into: 'Make sure your carrier offers Wi-Fi Calling (the carrier can confirm).' and 'Make sure your iPhone has the latest software.' Add a step after 'turn off, then on': 'Open Settings, tap General, tap Transfer or Reset iPhone, tap Reset, then tap Reset Network Settings.' (Do not add warnings about what it erases; the page gives none. Optionally say it is the last thing to try.) Keep the two-minute wait and the carrier line.",
    },
    keep("tr028-r", ["Open File Explorer from the taskbar", "Select Pictures in the left pane, then Screenshots (critical)",
                     "Optional: Save as, choose location and name, Save", "Optional: See More > Settings to change save location"]),
    keep("tr030-e", ["Settings > Network & internet > Internet", "Scroll to the bottom and tap Add network", "Enter network name and security details",
                     "Advanced options > Hidden Network > Yes", "Tap Save (critical)"]),
    {
        "id": "tr030-r",
        "required_actions": ["If the network should be nearby, wait for the list to refresh",
                             "Otherwise scroll to the bottom of the list and tap Add network", "Enter the network name and security details",
                             "Advanced options > Hidden Network > Yes", "Tap Save (critical)"],
        "covered": [False, True, True, True, True], "needs_clarification": False, "gates": dict(G),
        "unsupported_claims": [],
        "scores": sc(steps=1),
        "decision": "revise",
        "reasons": "The page says to wait for the list to refresh first if the network should be in range. The reply goes straight to Add network when the user says her network is not listed.",
        "fix": "Before the current step 1, add a step: 'Wait a few seconds for the list of networks to refresh. If her network still is not listed, it may be hidden.' Then continue with the existing steps (Add network, name and password, Hidden Network, Save). Keep 'Ask her for the network name and the password.'",
    },
]
