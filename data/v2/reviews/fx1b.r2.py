REVIEWS = [
    {
        "id": "tr009-e",
        "required_actions": [
            "Open Settings > Wi-Fi: make sure Wi-Fi is on and the network shows a blue checkmark",
            "Make sure Airplane Mode is off (critical)",
            "In Wi-Fi settings, make sure Connectivity Assist is off (critical)",
            "Uninstall VPN/security software if installed, restart iPhone, test; contact VPN manager/provider if needed",
            "Check other devices can connect to the same Wi-Fi",
            "Unplug router and cable modem, plug back in",
            "If other devices also cannot get online, contact the internet service provider",
            "Do not use Reset Network Settings (user constraint; it removes saved Wi-Fi networks and passwords)",
        ],
        "covered": [False, True, True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Skips the page's first check (Settings > Wi-Fi, Wi-Fi on, blue checkmark next to the network), so the reply never gives a clear starting point or tells the user what they should see. Step 3 'Tap Wi-Fi' is also a separate action inside a step about Connectivity Assist. Constraint (no Reset Network Settings) is handled correctly.",
        "fix": "Insert a new first step: 'Open **Settings**, then tap **Wi-Fi**. Make sure Wi-Fi is on and your network has a blue checkmark next to its name.' Then step 2 Airplane Mode (return to **Settings**), step 3 'In the **Wi-Fi** settings, make sure **Connectivity Assist** is off. If it looks dimmed, restart your iPhone.' Keep the remaining steps and the Reset Network Settings warning unchanged.",
    },
]
