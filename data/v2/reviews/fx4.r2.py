S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
P = {"source": "pass", "safety": "pass", "duplicate": "pass"}
REVIEWS = [
    {
        "id": "tr050-r",
        "required_actions": [
            "Explain: on iPhone XR the message 'Unable to verify this iPhone has a genuine Apple battery' means Apple cannot verify the battery as genuine, so the shown battery health info may be inaccurate (critical)",
            "To have the battery checked, use the page's 'get service' link (Apple's service page: getsupport.apple.com) (critical)",
        ],
        "covered": [True, True],
        "needs_clarification": False,
        "gates": dict(P),
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 1, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Step 2 'Get service for the battery through Apple Support, Apple's support website, to have it checked' is garbled and gives no clear starting point; the page's wording is 'To have your battery checked, get service' linking to getsupport.apple.com. Step 1 'Don't rely on the numbers shown there' is not an action.",
        "fix": "Replace the two steps with one clear action: '1. To have the battery checked, go to **getsupport.apple.com** and choose the battery service option (this is the 'get service' link on Apple's battery page).' Drop the phrase 'Apple Support, Apple's support website'. Keep the opening explanation that the numbers on that screen may not be accurate. Source: https://support.apple.com/en-us/101575 (link: https://getsupport.apple.com/?caller=kbase&PRKEYS=PF9&category_id=SC0999&symptom_id=23306).",
    },
    {
        "id": "tr051-r",
        "required_actions": [
            "If no MMS Messaging option appears under Settings > Messages, contact your carrier (critical)",
            "Ask the carrier whether your plan supports Group MMS Messaging (critical)",
        ],
        "covered": [True, True],
        "needs_clarification": False,
        "gates": dict(P),
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
        "decision": "revise",
        "reasons": "'group MMS' is used unexplained in the final reply and the carrier action has no 'what you will hear' cue; the reply is terse for an anxious user who just saw nothing arrive for the Android cousin.",
        "fix": "Reword the final reply in plain words, e.g. 'That setting is needed to send group messages to a phone that is not an iPhone. If your iPhone does not show it, your phone company has to turn it on. 1. Call or contact your phone carrier. 2. Ask: 'Does my plan support Group MMS Messaging?' (that is the name for group picture-and-text messages to non-iPhones).' Keep it short. Source: https://support.apple.com/en-us/118236 ('If you don't see an option to turn on MMS Messaging, contact your carrier').",
    },
    {
        "id": "tr056-r",
        "required_actions": [
            "Check whether Content & Privacy Restrictions is turned on; set Installing Apps to Allow under iTunes & App Store Purchases (critical)",
            "If App Store still not found, swipe down from the middle of the Home Screen and search for it with Spotlight",
        ],
        "covered": [True, True],
        "needs_clarification": False,
        "gates": dict(P),
        "unsupported_claims": [
            "\"If you did not set this up, ask the person who manages your phone.\" -> not on the page (harmless general advice, but unsupported)",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Step 3 'Adjust your iTunes & App Store Purchases settings' gives no starting point (where to open it); the cited page gives no Settings path and its linked article no longer uses these labels. Order is also reversed from the page (page: restrictions first, then Spotlight).",
        "fix": "Fetch Apple's current Screen Time guide for blocking/allowing app installs (e.g. https://support.apple.com/guide/iphone/block-apps-app-downloads-websites-purchases-iph3ff83f3b1/ios, section on preventing app installs) and add it as a second source; then write the exact Settings path (Settings > Screen Time > Content & Privacy Restrictions > ... > Installing Apps > Allow) only if that page shows it, one action per step, in the page's order (restrictions check first, Spotlight search as the fallback). If the path cannot be confirmed, reject this example. Remove or soften 'ask the person who manages your phone'.",
    },
    {
        "id": "tr057-r",
        "required_actions": [
            "Explain that a price instead of Install means a paid app; Install is for no-charge apps",
            "Either tap the price for a paid app, or choose a free app showing Install",
        ],
        "covered": [True, True],
        "needs_clarification": False,
        "gates": dict(P),
        "unsupported_claims": [],
        "scores": dict(S2),
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]
