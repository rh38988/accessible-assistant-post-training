# Round 2 review of batch ex5 (re-review of revised examples). Written page by page.
REVIEWS = []

# Source A: https://support.google.com/android/answer/7431795?hl=en (free up storage)
REVIEWS += [
    {
        "id": "tr062-a",
        "required_actions": [
            "Open the Settings app (critical)",
            "Tap Storage (critical)",
            "Tap Free up space (critical)",
            "Scroll to a category and tap Select files, or Browse if the category is not listed (critical)",
            "Select the files you don't need (critical)",
            "Tap Move files to Trash (critical)",
        ],
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr062-d",
        "required_actions": [
            "Open the Settings app (critical)",
            "Tap Storage (critical)",
            "Tap Free up space (critical)",
            "Scroll to a category and tap Select files, or Browse if the category is not listed (critical)",
            "Select the files you don't need (critical)",
            "Tap Move files to Trash (critical)",
        ],
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source B: https://support.apple.com/en-us/105001 (flashlight)
REVIEWS += [
    {
        "id": "tr063-b",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source C: https://support.apple.com/en-us/118444 (alarm, iPhone)
_ALARM_ACTIONS = [
    "Open the Clock app, then tap the Alarms tab (critical)",
    "Tap the Add button (critical)",
    "Set the time (critical)",
    "Only if repeating, tap Repeat and choose the days",
    "Tap Done (critical)",
]
REVIEWS += [
    {
        "id": "tr066-a",
        "required_actions": _ALARM_ACTIONS,
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr066-b",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr066-c",
        "required_actions": _ALARM_ACTIONS,
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr066-d",
        "required_actions": _ALARM_ACTIONS,
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source D: https://support.google.com/android/answer/2840926?hl=en (Android Clock alarm)
REVIEWS += [
    {
        "id": "tr067-c",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source E: https://support.apple.com/en-us/108780 (hearing aids, iPhone)
_HEAR_ACTIONS = [
    "Make sure the iPhone has the latest iOS update (critical)",
    "Put the hearing aids in pairing mode (critical)",
    "Open Settings, tap Accessibility, then tap Hearing Devices (critical)",
    "Tap Pair MFi Hearing Device and follow the steps on screen (critical)",
    "Select the hearing aids and tap Pair (critical)",
]
_HEAR_COVERED = [True, True, True, True, True]
REVIEWS += [
    {
        "id": "tr068-a",
        "required_actions": _HEAR_ACTIONS,
        "covered": _HEAR_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr068-c",
        "required_actions": _HEAR_ACTIONS,
        "covered": _HEAR_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr068-d",
        "required_actions": _HEAR_ACTIONS,
        "covered": _HEAR_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source F: https://support.google.com/android/answer/9417604?hl=en and .../9769184?hl=en (Bluetooth pairing, Android)
_BT_ACTIONS = [
    "Turn on the headphones and make them discoverable or ready to pair (critical)",
    "Swipe down from the top of the screen (critical)",
    "Press and hold the Bluetooth icon (critical)",
    "Tap Pair new device (critical)",
    "Tap the headphones' name (critical)",
    "Enter 0000 or 1234 if asked for a code (only if asked)",
]
_BT_COVERED = [True, True, True, True, True, True]
REVIEWS += [
    {
        "id": "tr069-a",
        "required_actions": _BT_ACTIONS,
        "covered": _BT_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr069-c",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr069-d",
        "required_actions": _BT_ACTIONS,
        "covered": _BT_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source G: https://support.apple.com/en-us/101604 (Low Power Mode, iPhone)
_LPM_ACTIONS = [
    "Open Settings (critical)",
    "Tap Battery (critical)",
    "Turn on Low Power Mode, via Power Mode on iPhone 15 and newer (critical)",
]
_LPM_COVERED = [True, True, True]
REVIEWS += [
    {
        "id": "tr070-a",
        "required_actions": _LPM_ACTIONS,
        "covered": _LPM_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr070-d",
        "required_actions": _LPM_ACTIONS,
        "covered": _LPM_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source H: https://support.google.com/android/answer/7664692?hl=en (Battery Saver, Android)
_BS_ACTIONS = [
    "Open the Settings app (critical)",
    "Tap Battery (critical)",
    "Tap Battery Saver (critical)",
    "Choose a schedule for Battery Saver, or the option that turns it off automatically (critical)",
]
_BS_COVERED = [True, True, True, True]
REVIEWS += [
    {
        "id": "tr071-a",
        "required_actions": _BS_ACTIONS,
        "covered": _BS_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr071-c",
        "required_actions": _BS_ACTIONS,
        "covered": _BS_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr071-d",
        "required_actions": _BS_ACTIONS,
        "covered": _BS_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source I: https://support.apple.com/en-us/102629 (update apps, iPhone)
REVIEWS += [
    {
        "id": "tr072-d",
        "required_actions": [
            "Open the App Store (critical)",
            "Tap the profile picture or account icon at the top (critical)",
            "Tap App Updates (critical)",
            "Tap Update next to the banking app (critical)",
        ],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source J: https://support.google.com/accessibility/android/answer/6006949?hl=en (Magnification, Android)
_MAG_ACTIONS = [
    "Open Settings, tap Accessibility, then tap Magnification (critical)",
    "Turn on the Magnification shortcut (critical)",
    "Start magnification with the shortcut (critical)",
    "Tap anywhere on the screen, except the keyboard or navigation bar (critical)",
    "Pinch with two fingers to zoom, and drag with two fingers to move (critical)",
    "Use the shortcut again to stop (critical)",
]
_MAG_COVERED = [True, True, True, True, True, True]
REVIEWS += [
    {
        "id": "tr073-a",
        "required_actions": _MAG_ACTIONS,
        "covered": _MAG_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr073-c",
        "required_actions": _MAG_ACTIONS,
        "covered": _MAG_COVERED,
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "\"Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time.\" -> the page says nothing about how apps look or about text size or layout when magnification is off; it only says the shortcut stops magnification. Only the part 'you use the shortcut to turn it on and off' is supported.",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "The opening claim that magnification leaves how the app looks unchanged the rest of the time is not on the page (the page does not discuss app appearance or text size when magnification is off).",
        "fix": "Replace the first sentence of the reply (\"Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time.\") with a sentence that uses only supported facts, for example: \"Magnification can help with that. It zooms in on the whole screen, and you turn it on and off with your shortcut.\" Keep the rest of the reply unchanged.",
    },
    {
        "id": "tr073-d",
        "required_actions": _MAG_ACTIONS,
        "covered": _MAG_COVERED,
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source K: https://support.apple.com/en-us/101593 (Find My, lost iPhone)
_FM_ACTIONS = [
    "Open the Find My app on another Apple device and tap Devices (critical)",
    "Select the lost iPhone (critical)",
    "Tap More, then turn on Lost Mode (critical)",
    "Follow the steps on screen to add a phone number and message, then tap Activate (critical)",
    "On a computer, go to icloud.com/find and sign in with the Apple Account (critical)",
    "Select the iPhone under All Devices, then play a sound or mark it as lost (critical)",
    "Safety: Apple never calls or texts to say the iPhone was found; never share a passcode or code (critical)",
]
_FM_COVERED = [True, True, True, True, True, True, True]
_FM_FIX_MAP = (
    "Change \"Select your iPhone to see it on a map.\" to \"Select your iPhone to locate it.\" "
    "The page only says Find My can be used to locate devices; it does not describe a map. "
    "Keep every other step as it is."
)
REVIEWS += [
    {
        "id": "tr074-a",
        "required_actions": _FM_ACTIONS,
        "covered": _FM_COVERED,
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "\"Select your iPhone to see it on a map.\" -> the page does not mention a map or describe what the screen shows after a device is selected; it only says to use Find My to locate devices.",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Unsupported description of what the user sees after selecting the iPhone (a map).",
        "fix": _FM_FIX_MAP,
    },
    {
        "id": "tr074-b",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr074-c",
        "required_actions": _FM_ACTIONS,
        "covered": _FM_COVERED,
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "\"Select your iPhone to see it on a map.\" -> the page does not mention a map or describe what the screen shows after a device is selected; it only says to use Find My to locate devices.",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Unsupported description of what the user sees after selecting the iPhone (a map).",
        "fix": _FM_FIX_MAP,
    },
    {
        "id": "tr074-d",
        "required_actions": [
            "On a computer, go to icloud.com/find and sign in with the Apple Account (critical)",
            "Select the iPhone under All Devices (critical)",
            "Play a sound or mark the iPhone as lost (critical)",
            "Safety: Apple never calls or texts to say the iPhone was found; never share a passcode or code (critical)",
        ],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Source L: https://support.google.com/accounts/answer/6160491?hl=en (Find Hub, Android lost phone)
_FH_ACTIONS = [
    "On another Android phone, open the Find Hub app, or on a computer go to google.com/android/find (critical)",
    "Sign in with the Google Account (critical)",
    "Select the lost phone (critical)",
    "If asked, enter the lock screen PIN (critical when asked)",
    "Choose Play sound, Mark as lost, or Factory reset as needed (non-critical)",
]
_FH_COVERED = [True, True, True, True, True]
_FH_FIX_CONDITION = (
    "Replace \"It works if your phone is on and connected to the internet.\" with "
    "\"It works best when your phone is on and connected. If its current location can't be found, "
    "Find Hub may show its last known location.\" The page lists the power and connection conditions only "
    "for securing or erasing the phone, not for locating it."
)
_FH_FIX_PIN = (
    "Replace \"enter your lock screen PIN or password\" with \"enter your lock screen PIN\", and add "
    "\"If the phone has no PIN, or runs Android 8 or lower, you may be asked for your Google password.\""
)
_FH_UNSUPPORTED = [
    "\"It works if your phone is on and connected to the internet.\" -> the page lists power and a data or Wi-Fi connection only as conditions for securing or erasing; for locating it gives no such condition and mentions last known location instead.",
    "\"If asked, enter your lock screen PIN or password.\" -> the page says the lock screen PIN is requested (Android 9 or higher); a Google password is requested only when the phone has no PIN or runs Android 8 or lower. The reply does not say this.",
]
REVIEWS += [
    {
        "id": "tr075-a",
        "required_actions": _FH_ACTIONS,
        "covered": _FH_COVERED,
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": _FH_UNSUPPORTED,
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "The locating condition is taken from the page's securing or erasing checklist, and the PIN or password prompt is mislabelled.",
        "fix": _FH_FIX_CONDITION + " " + _FH_FIX_PIN + " Keep every other sentence unchanged.",
    },
    {
        "id": "tr075-b",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr075-c",
        "required_actions": [],
        "covered": [],
        "needs_clarification": True,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr075-d",
        "required_actions": _FH_ACTIONS,
        "covered": _FH_COVERED,
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": _FH_UNSUPPORTED,
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "The locating condition is taken from the page's securing or erasing checklist, and the PIN or password prompt is mislabelled.",
        "fix": _FH_FIX_CONDITION + " " + _FH_FIX_PIN + " Keep every other sentence unchanged.",
    },
]
