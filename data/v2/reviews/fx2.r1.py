# Reviews for batch fx2, round 1
S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
OK = {"source": "pass", "safety": "pass", "duplicate": "pass"}


def keep(id, req, nc=False, scores=None, gates=None):
    return {
        "id": id,
        "required_actions": req,
        "covered": [True] * len(req),
        "needs_clarification": nc,
        "gates": dict(gates or OK),
        "unsupported_claims": [],
        "scores": dict(scores or S2),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    }


FAMILY = [
    "Resist the urge to act immediately (critical)",
    "Do not wire money, pay by gift card, or send cash (critical)",
    "Call the relative at a number you know to be genuine (critical)",
    "Check the story with another trusted family member, even if told to keep it secret",
    "Report to the FTC at www.ftc.gov/complaint",
]
CODE = [
    "Never give the verification code to anyone (critical)",
    "Don't engage: hang up, block the number, stop texting",
    "If worried, contact bank/credit union/investment advisor directly using a trusted number (statement or app)",
    "Never use a number the caller gave",
    "Report at ReportFraud.ftc.gov",
]
PAY = [
    "Treat a seller who says you can only pay one way (bank transfer, wire, crypto, payment app, gift card) as probably a scammer (critical)",
    "Never send money to someone who insists on one payment method (critical)",
    "Look the seller up online with words like review, scam, complaint",
    "Pay by credit card when possible (more protections, can dispute charges)",
    "Report at ReportFraud.ftc.gov",
]

REVIEWS = []
REVIEWS += [
    keep("tr014-c", FAMILY),
    keep("tr014-e", FAMILY),
    keep("tr014-r", ["Report the fraud to the FTC at www.ftc.gov/complaint (critical; page gives no recovery steps)", "Do not send more money / do not wire, gift card, or cash again", "Tell another trusted family member"]),
    keep("tr014-f", FAMILY),
    keep("tr014-g", ["Know the signs: family member emergency, stock lines, accomplice doctor/lawyer/police, money immediately by wire/gift card (critical)", "Don't act right away", "Call relative on a genuine number", "Check with another family member", "Family agreement: no one calls with emergency wire/gift card/cash request", "Report at www.ftc.gov/complaint"]),
    keep("tr015-c", CODE),
    keep("tr015-e", CODE),
    keep("tr015-r", ["Contact bank/credit union directly using a trusted number (critical; page gives no specific steps for an already-shared code)", "Never use the number the caller gave", "Don't engage, block, stop texting", "Report at ReportFraud.ftc.gov"]),
    keep("tr015-f", CODE),
    keep("tr015-g", CODE + ["Explain how the scam works (pose as trusted person, code lets them log in and move money)"]),
    keep("tr016-d", PAY, scores=S2),
    keep("tr016-c", PAY),
    {
        "id": "tr016-e",
        "required_actions": PAY,
        "covered": [True, True, True, True, False],
        "needs_clarification": False,
        "gates": dict(OK),
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 1, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "User said they cannot use a credit card, but step 3 still leads with 'Paying by credit card is safest', which pushes the one option the user ruled out. The opening 'Please be careful' is soft for a seller who says a payment app is the only way; the page says such a seller is probably a scammer and to never send money that way. The reply does not use the 'only way' wording or the ReportFraud report step.",
        "fix": "Start with 'Please don't pay this seller with Zelle.' Say that a seller who says you can only pay with a payment app is probably a scammer, and that the tickets going fast is the kind of pressure scammers use (keep this general, no new facts). Keep step 1 (never send money to anyone who says you can only pay one specific way, whatever reason they give) and step 2 (search the seller's name with review, scam, complaint). Replace step 3 with: 'The FTC suggests a credit card when possible because it lets you dispute charges. Since you can't use one, the safe choice is to skip a seller who insists on a payment app.' Add: 'You can report the seller at ReportFraud.ftc.gov.' Source: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay. Keep the ftc.gov/scams line if wanted (the page names ftc.gov/scams).",
    },
    keep("tr016-r", ["Don't wait: contact the company you used to send the money right away (critical)", "Tell them it was fraud", "Ask whether they can stop or reverse the transaction and return the money", "Report at ReportFraud.ftc.gov"]),
    keep("tr016-g", PAY),
]

# ---- page: Apple 102453 / Google 11183305 / Apple 105103
REVIEWS += [
    keep("tr021-e", [
        "Open Settings and tap Accessibility (critical)",
        "Tap Display & Text Size (critical)",
        "Tap Larger Text (critical)",
        "Drag the slider to the preferred size (critical)",
    ]),
    keep("tr022-e", [
        "Open Settings, search and select Font size, drag the slider (adds the Font Size tile to Quick Settings) (critical)",
        "Swipe down from the top of the screen to open Quick Settings",
        "Tap Font Size",
        "Tap Increase or Decrease, or drag the percentage slider",
    ]),
    keep("tr022-r", [
        "Open Settings, search for and select Font size (critical)",
        "Tap Reset settings to return to defaults, or drag the slider back to a smaller size (critical)",
    ]),
    {
        "id": "tr024-e",
        "required_actions": [
            "Explain that the buttons change media volume while using videos/music/games and ringer volume only when not using other apps (critical)",
            "Stop using other apps (leave the video app)",
            "Press volume up/down to adjust the ringer volume (critical)",
        ],
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'Press the **volume up** button on the side of the phone' -> the Apple page does not say where the volume buttons are; remove the location.",
        ],
        "scores": dict(S2),
        "decision": "revise",
        "reasons": "Only issue is the button location, which the page does not state. Everything else matches the page (media vs ringer volume behavior, Silent mode vibrate).",
        "fix": "In step 2 change to 'Press the **volume up** button a few times.' (drop 'on the side of the phone'). Keep everything else. Source: https://support.apple.com/en-us/105103.",
    },
    {
        "id": "tr024-r",
        "required_actions": [
            "Recognize orange means Silent mode, which vibrates for calls (critical)",
            "Turn off Silent mode by flipping the Ring/Silent switch so orange is not showing (critical)",
            "Press volume up to raise the ringer volume (when no other app is in use)",
            "Newer models (iPhone 15 Pro and later, no switch): the Action button turns Silent mode on or off by default",
            "Favorite contacts still ring in Silent mode",
        ],
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'Find the small **Ring/Silent switch** above the volume buttons.' -> the page does not say where the switch is or that it is small; the page text and image alt text give no location.",
        ],
        "scores": dict(S2),
        "decision": "revise",
        "reasons": "The switch location ('small', 'above the volume buttons') is not on the page. The user already said they see orange on the side of the phone, so the location can be tied to that instead.",
        "fix": "Step 1 should read: 'Find the **Ring/Silent switch**, where you see the orange.' Drop 'small' and 'above the volume buttons'. Keep steps 2 and 3 and the Action button paragraph. Do not add a press-and-hold instruction for the Action button; the page does not give one. Source: https://support.apple.com/en-us/105103.",
    },
]

# ---- page: Google 9082609 / Apple 108066 / Google 9075928
REVIEWS += [
    {
        "id": "tr025-e",
        "required_actions": [
            "Press a volume button (critical)",
            "At the right, tap the Down arrow (older Android) (critical)",
            "Choose the volume type Ring (critical)",
            "Slide the Ring level to the wanted loudness",
        ],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'Tap the **Down arrow** that appears next to the slider.' -> the page says only 'At the right, tap the Down arrow'; it does not say next to the slider.",
            "'Slide it to the right to make the ring louder.' -> the page gives no slide direction for the older-version steps.",
        ],
        "scores": dict(S2),
        "decision": "revise",
        "reasons": "Two small unsupported details: the arrow position wording and the slide direction. The user described a slider plus a small arrow, so the reply may refer to the arrow they already see.",
        "fix": "Step 2: 'At the right, tap the **Down arrow**.' Step 4: 'Slide the **Ring** level to where you want it.' (no direction). Keep the closing line about Media, Ring, and Alarm. Source: https://support.google.com/android/answer/9082609?hl=en.",
    },
    {
        "id": "tr025-r",
        "required_actions": [
            "Press a volume button (critical)",
            "At the right, tap the Down arrow (older Android) (critical)",
            "Choose Ring (critical)",
            "Slide the Ring level to the wanted loudness",
        ],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'Slide it to the right to make it louder.' -> the page gives no slide direction for the older-version steps.",
        ],
        "scores": dict(S2),
        "decision": "revise",
        "reasons": "Final reply is right about the Down arrow and Ring, but adds a slide direction that the page does not state. Step 3 'Choose Ring' and step 4 are also described by the page only as choosing the volume type.",
        "fix": "Step 4: 'Slide the **Ring** level to where you want it.' (remove 'to the right to make it louder'). Optionally add 'At the right' to step 2 ('At the right, tap the **Down arrow**.'), matching the page. Source: https://support.google.com/android/answer/9082609?hl=en.",
    },
    keep("tr026-e", [
        "Open Settings and tap Cellular (critical)",
        "With two SIMs, select the line you want (work line) (critical)",
        "Tap Wi-Fi Calling",
        "Turn on Wi-Fi Calling on This Phone (critical)",
        "Tap Enable (critical)",
        "Enter/confirm emergency address if asked; carrier must offer Wi-Fi Calling",
    ]),
    {
        "id": "tr026-r",
        "required_actions": [
            "Check that the carrier offers Wi-Fi Calling and the iPhone has the latest software",
            "Open Settings > Cellular, select the line if multiple SIMs, tap Wi-Fi Calling and make sure it is on",
            "Restart the iPhone",
            "Connect to a different Wi-Fi network (not all networks work)",
            "Turn Wi-Fi Calling off and on again (wait about two minutes between steps)",
            "If still not working, contact the carrier (critical)",
        ],
        "covered": [True, False, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'3. If it still won't turn on, contact your carrier. 4. If your carrier can't fix it, restart your iPhone, try a different Wi-Fi network, and then turn Wi-Fi Calling off and on again.' -> the page lists restart, different Wi-Fi network, and off/on as the troubleshooting sequence, and says to contact the carrier if it still can't be turned on afterward. The reply puts the carrier before the restart and invents an 'if your carrier can't fix it' condition.",
        ],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Order is wrong against the page and step 4 packs three actions into one. The check that Wi-Fi Calling is on in Settings > Cellular (the page's first troubleshooting step) and the wait between steps are missing.",
        "fix": "Rewrite the final reply as: 'Let's try these in order.' 1. Check that your carrier offers Wi-Fi Calling and that your iPhone software is up to date. 2. Open **Settings**, tap **Cellular**, tap **Wi-Fi Calling**, and make sure **Wi-Fi Calling on This iPhone** is on. 3. Restart your iPhone. 4. Connect to a different Wi-Fi network, because some networks don't work with Wi-Fi Calling. 5. Turn Wi-Fi Calling off, then on again. Then: 'Wait about two minutes between steps. If it still won't turn on, contact your carrier.' Keep each step to one action. Source: https://support.apple.com/en-us/108066 (page also lists General > Transfer or Reset iPhone > Reset > Reset Network Settings as a last step; leave it out for simplicity or add it as step 6).",
    },
    keep("tr027-e", [
        "Open the screen to capture",
        "Press and hold the Power button for a few seconds (critical)",
        "Tap Screenshot (critical)",
        "Preview appears at bottom left; if nothing, see phone maker's support site",
    ]),
    keep("tr027-r", [
        "Open the Photos app (critical)",
        "Tap Collections",
        "Tap On this device, then Screenshots (critical)",
        "Tap Share to send it",
        "No Photos app (older Android): Gallery > Album view > Screenshots folder",
    ]),
]

# ---- page: Microsoft Snipping Tool / Google 9075847 / Microsoft Wi-Fi
REVIEWS += [
    keep("tr028-e", [
        "Select Start, enter snipping tool, select Snipping Tool (critical)",
        "Select Snipping Mode, then Rectangle (critical)",
        "Select New (critical)",
        "Select the rectangular area to capture",
        "Snip is automatically saved to the Screenshots folder",
    ]),
    {
        "id": "tr028-r",
        "required_actions": [
            "Know that snips are automatically saved to the Screenshots folder (critical)",
            "Open the Screenshots folder (needs a starting point such as File Explorer > Pictures > Screenshots) (critical)",
            "Optional: Save as, choose a location and name, then Save",
            "Optional: See More > Settings to change where snips are saved",
        ],
        "covered": [True, False, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "The user asked how to find the picture, but step 1 says only 'Look in your Screenshots folder' with no way to open that folder. The cited Snipping Tool page does not give the path; another Microsoft page does.",
        "fix": "Replace step 1 with: 'Open **File Explorer** from the taskbar.' Add step 2: 'On the left side, select the **Pictures** folder, then select **Screenshots**.' Keep the Save as step (select **Save as** in Snipping Tool, choose a location and a name, then select **Save**) as step 3 and the See More > Settings line. Add a second source: https://support.microsoft.com/en-us/windows/experience/keyboard-shortcut-for-print-screen (says: open File Explorer from the taskbar, select the Pictures folder, then Screenshots).",
    },
    {
        "id": "tr030-e",
        "required_actions": [
            "Open Settings; tap Network & internet, then Internet (critical)",
            "Scroll to the bottom of the list and tap Add network (critical)",
            "Enter the network name (SSID) and the security details (critical)",
            "Tap Advanced options; under Hidden Network select Yes (critical)",
            "Tap Save (critical)",
            "Once connected it is labeled Saved and reconnects automatically nearby",
        ],
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": dict(OK),
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 1, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "The user says the son gave him the name and the password, but step 5 says only 'Enter the security details if asked', which does not tell him the password goes there; it also makes the step sound optional. The page says to provide the security details with the name.",
        "fix": "Change step 5 to: 'Enter the security details your son gave you, including the password.' Keep all other steps and the closing Saved line. Source: https://support.google.com/android/answer/9075847?hl=en.",
    },
    {
        "id": "tr030-r",
        "required_actions": [
            "Open Settings; tap Network & internet, then Internet",
            "Scroll to the bottom of the list and tap Add network (critical)",
            "Enter the network name (SSID) and security details (critical)",
            "Tap Advanced options; under Hidden Network select Yes (critical)",
            "Tap Save (critical)",
        ],
        "covered": [False, True, True, False, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'Wait a few seconds for the list to reload.' -> not on the page.",
        ],
        "scores": {"steps": 0, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "For a network that is not listed the page requires choosing Hidden Network = Yes under Advanced options (critical), and entering security details (the password). The final reply leaves both out, so the steps would not connect to a hidden network. It also starts from 'Add network' without the path and adds an unsupported 'wait a few seconds' step.",
        "fix": "Rewrite the final reply: 'Her network may be hidden. Ask her for the network name and the password.' 1. Open **Settings**, tap **Network & internet**, then **Internet**. 2. Scroll to the bottom of the list and tap **Add network**. 3. Type the network name, then enter the security details (the password). 4. Tap **Advanced options**, and under **Hidden Network** select **Yes**. 5. Tap **Save**. Remove 'Wait a few seconds for the list to reload.' Source: https://support.google.com/android/answer/9075847?hl=en.",
    },
    keep("tr031-e", [
        "Select the Network, Sound, or Battery icons on the taskbar (critical)",
        "Select Manage Wi-Fi connections in the Wi-Fi quick setting (critical)",
        "Choose the network and select Connect (critical)",
        "Enter the password and select Next (critical)",
    ]),
    keep("tr031-r", [
        "Open Manage Wi-Fi connections from the taskbar quick settings (critical)",
        "Select the Refresh network list button in the lower right (critical)",
        "Select the network and select Connect",
    ]),
]
