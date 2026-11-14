S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
G = {"source": "pass", "safety": "pass", "duplicate": "pass"}


def sc(**kw):
    d = dict(S2)
    d.update(kw)
    return d


def ask(id_):
    return {
        "id": id_, "required_actions": [], "covered": [], "needs_clarification": True,
        "gates": dict(G), "unsupported_claims": [],
        "scores": sc(steps="NA"), "decision": "keep", "reasons": "", "fix": "",
    }


VM_SET = ["Tap Voicemail (critical)", "Tap Set Up Now (critical)", "Create a voicemail password (critical)",
          "Choose a greeting, Default or Custom (critical)", "If Custom, record a new greeting"]
VM_LISTEN = ["Tap Voicemail (critical)", "Tap a message (critical)", "Tap the Play button (critical)", "Tap the Delete button to delete"]
FWD = ["Settings > Apps > Phone (critical)", "Tap Call Forwarding, turn on Call Forwarding (critical)",
       "If Dual SIM, choose a line (below SIMs) BEFORE Forward To", "Tap Forward To, enter the number (critical)", "Tap Back (critical)"]
LED = ["Settings > Accessibility > Audio/Visual (critical)", "Switch on LED Flash for Alerts (critical)"]
MOD = ["Settings > General > About (critical)", "Find Model Number, tap the part number to show the model number (critical)"]
SCAN_N = ["Open Notes, open or create a note (critical)", "Tap Attachment (paperclip) button, then Scan Documents (critical)",
          "Position document in camera view (critical)", "Auto mode scans itself; or tap Shutter button / press a Volume button, drag corners, tap Keep Scan",
          "Tap Done or add more scans (critical)"]

REVIEWS = [
    {"id": "tr141-a", "required_actions": VM_SET, "covered": [True] * 5, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr141-c", "required_actions": VM_LISTEN, "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    ask("tr141-b"),
    {"id": "tr141-d", "required_actions": VM_SET, "covered": [True] * 5, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr141-e", "required_actions": ["Use Siri: ask 'Do I have any new voicemail?' / 'Play the voicemail from <name>'",
                                           "Know how to start Siri (the page assumes Siri is already listening)"],
     "covered": [True, False], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [],
     "scores": sc(actionable=1), "decision": "revise",
     "reasons": "User cannot tap well; the reply says 'ask Siri' but never says how to start Siri, so there is no clear starting point. The cited voicemail page does not say how to activate Siri.",
     "fix": "Add a first step telling the user how to wake Siri hands-free, taken from https://support.apple.com/guide/iphone/turn-on-and-activate-siri-iph83aad8922/ios (for example saying 'Hey Siri', only as that page states it, and noting that Siri must be turned on in settings if it does not answer). Add that URL as a second source. Keep the two example phrases exactly as they are."},
    {"id": "tr141-r", "required_actions": ["Tap Voicemail and follow the instructions on the screen (critical)", "From another phone, dial your own mobile number",
                                           "Press * or # (depending on carrier) to skip the greeting", "Enter your voicemail password"],
     "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},

    {"id": "tr142-a", "required_actions": FWD, "covered": [True, True, True, True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr142-c", "required_actions": FWD, "covered": [True, True, False, True, True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'6. Tap Forward To and type in your son's number. 7. Because your iPhone has two SIMs, choose the line you want to forward. 8. Tap Back.' -> the page puts the Dual SIM line choice (below SIMs) right after turning on Call Forwarding and BEFORE tapping Forward To; the reply puts it after."],
     "scores": sc(steps=1, actionable=1), "decision": "revise",
     "reasons": "Dual SIM step is in the wrong order, and step 6 bundles tapping Forward To with typing the number.",
     "fix": "Reorder: 5 Turn on Call Forwarding; 6 Because your iPhone has Dual SIM, choose a line (below SIMs); 7 Tap Forward To; 8 Type your son's number; 9 Tap Back. Keep the range note and the status-bar icon sentence. Optionally add one short line that call forwarding works on GSM networks only (page: contact your carrier if CDMA)."},
    ask("tr142-b"),
    {"id": "tr142-d", "required_actions": FWD, "covered": [True, True, True, True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr142-e", "required_actions": ["Say forwarding works on GSM networks; if CDMA, contact carrier (critical)", "If GSM: Settings > Apps > Phone > Call Forwarding on",
                                           "Tap Forward To, enter number, tap Back"],
     "covered": [True, True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr142-r", "required_actions": ["Be in range of the cellular network when setting forwarding; redo if not (critical)", "Works on GSM; if CDMA contact carrier"],
     "covered": [True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},

    {"id": "tr143-a", "required_actions": LED, "covered": [True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr143-c", "required_actions": LED + ["Keep Flash on Silent on so it blinks on silent"], "covered": [True, True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    ask("tr143-b"),
    {"id": "tr143-d", "required_actions": LED, "covered": [True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr143-e", "required_actions": LED + ["Turn off Flash on Silent"], "covered": [True, True, True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr143-r", "required_actions": ["Explain flash only works when iPhone is locked (critical)", "Let the phone lock, then wait for a notification",
                                           "Check LED Flash for Alerts is on in Settings > Accessibility > Audio/Visual"],
     "covered": [True, True, True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'Press the side button to lock the phone' -> the cited page never says how to lock the phone or names the side button."],
     "scores": sc(), "decision": "revise",
     "reasons": "One unsupported control instruction.",
     "fix": "In step 1 delete 'Press the side button to lock the phone, or'. Use only: 'Put the phone down and let the screen go dark so it is locked.'"},

    {"id": "tr144-a", "required_actions": MOD, "covered": [True, True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'The model number starts with the letter A and four digits.' -> page does not describe the format.",
                            "'You can match it against Apple's list of iPhone models to see which model you have.' -> not stated on the cited page."],
     "scores": sc(), "decision": "revise", "reasons": "Two unsupported closing claims.",
     "fix": "Delete both closing sentences. End after step 5, optionally with 'Use that number when you sell the phone.'"},
    {"id": "tr144-c", "required_actions": ["iPhone 7 or earlier: find the model number on the back of the device (critical)"], "covered": [True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'The model number starts with the letter A and four digits.' -> not on the page.",
                            "'You do not need to turn the phone on.' -> page does not say this."],
     "scores": sc(), "decision": "revise", "reasons": "Unsupported format claim and unsupported statement about not turning the phone on.",
     "fix": "Delete both sentences. Answer: 'Yes. On an iPhone 7 or earlier, the model number is on the back of the phone.' then steps 1 and 2 as written. The user can see this is the back-of-phone method without needing it turned on; you may say 'This method looks at the back of the phone itself' only if you keep it to that."},
    ask("tr144-b"),
    {"id": "tr144-d", "required_actions": MOD, "covered": [True, True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'The model number starts with the letter A and four digits.' -> page does not describe the format."],
     "scores": sc(), "decision": "revise", "reasons": "Unsupported format claim.",
     "fix": "Replace the last paragraph with 'You can tell the store that number.' Remove the sentence about the letter A and four digits."},
    {"id": "tr144-e", "required_actions": ["iPhone 8 or later with SIM tray: remove the SIM tray and look in the slot (critical)", "Be in bright overhead light",
                                           "Model number is on the upper side, the side with the display (critical)"],
     "covered": [True, True, True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'The model number starts with the letter A and four digits.' -> page does not describe the format.",
                            "'Yes, you do not need to unlock the phone.' -> page does not state this."],
     "scores": sc(), "decision": "revise", "reasons": "Unsupported format claim; unlock statement not on page.",
     "fix": "Delete the letter A sentence. Change the opening to 'Yes. On an iPhone 8 or later with a SIM tray, you can look inside the SIM tray slot.' Keep the three steps. Optionally say step 2 means 'a place with bright light overhead'."},
    {"id": "tr144-r", "required_actions": ["Tap the part number next to Model Number to show the model number (critical)"], "covered": [True], "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},

    {"id": "tr145-a", "required_actions": SCAN_N, "covered": [True] * 5, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr145-c", "required_actions": ["Files: tap More button (three dots) (critical)", "Tap Scan Documents (critical)", "Position document; Auto scans itself",
                                           "Tap Done or add more scans (critical)", "Choose a location (critical)", "Tap Save (critical)"],
     "covered": [True] * 6, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    ask("tr145-b"),
    {"id": "tr145-d", "required_actions": SCAN_N, "covered": [True] * 5, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr145-e", "required_actions": SCAN_N[:3] + ["Tap Shutter button or press a Volume button (critical)", "Drag corners to fit the page", "Tap Keep Scan (critical)", "Tap Done (critical)"],
     "covered": [True] * 7, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr145-r", "required_actions": ["Tap Shutter button or press a Volume button (critical)", "Drag corners to fit", "Tap Keep Scan (critical)", "Tap Done or add more scans"],
     "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},

    {"id": "tr146-a", "required_actions": ["Press and hold the app until options appear (critical)", "Tap Edit Home Screen (critical)", "Drag to new spot such as the Dock (critical)", "iPhone X and later: tap Done (critical)"],
     "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr146-c", "required_actions": ["Press and hold until apps jiggle", "Drag to right edge, wait a moment (critical)", "If no dots to the right, dragging makes a new page", "iPhone 8: press Home button to save (critical)"],
     "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    ask("tr146-b"),
    {"id": "tr146-d", "required_actions": ["Press and hold app until options appear", "Tap Edit Home Screen", "Drag app to new spot", "iPhone X and later: tap Done"],
     "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr146-e", "required_actions": ["Press and hold app until apps jiggle", "Drag one app onto another to create a folder (critical)", "Drag more apps into the folder (critical)", "Optional rename: press and hold folder, Rename, type, Done"],
     "covered": [True] * 4, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr146-r", "required_actions": ["Wait a moment at the right edge for the new page", "Check dots above the Dock; if dots to the right, drag toward that edge", "If no dots to the right, dragging to the right edge makes a new page"],
     "covered": [True] * 3, "needs_clarification": False,
     "gates": dict(G), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
]
