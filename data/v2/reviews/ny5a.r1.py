G = {"source": "pass", "safety": "pass", "duplicate": "pass"}
S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
SNA = dict(S2, steps="NA")

def keep(id, ra, nc=False, clar=False):
    return {"id": id, "required_actions": [] if clar else ra, "covered": [] if clar else [True] * len(ra),
            "needs_clarification": nc, "gates": dict(G), "unsupported_claims": [],
            "scores": dict(SNA if clar else S2), "decision": "keep", "reasons": "", "fix": ""}

def rev(id, ra, cov, claims, scores, reasons, fix, source="pass"):
    sc = dict(S2); sc.update(scores)
    g = dict(G); g["source"] = source
    return {"id": id, "required_actions": ra, "covered": cov, "needs_clarification": False, "gates": g,
            "unsupported_claims": claims, "scores": sc, "decision": "revise", "reasons": reasons, "fix": fix}

CLEAN = ["Start > Settings > System > Storage > Cleanup recommendations (critical)",
         "Review groups Temporary files, Large or unused files, Files synced to the cloud, Unused apps",
         "Tick items to remove (critical)", "Select Clean up for each section (critical)"]
PREV = ["Start > Settings > System > Storage > Cleanup recommendations (critical)",
        "Find previous version of Windows listed as a system file (only if upgraded fewer than 10 days ago) (critical)",
        "Select it and Clean up (critical)", "Warn it removes Windows.old and cannot be undone"]
MOVE = ["Connect the external drive", "Open File Explorer, select the files", "Select Cut on the ribbon (critical)",
        "Go to the drive and select Paste (critical)"]
BIGF = ["File Explorer, open Downloads/Videos/Music/Pictures", "View > Details", "Right-click empty area > Sort by > Size",
        "Delete unneeded files", "Empty the Recycle Bin"]
ES_Q = ["Select Battery icon in notification area (critical)", "Select Energy saver quick setting (critical)"]
ES_AUTO = ["Start > Settings > System > Power & battery (critical)", "Expand Energy saver",
           "Next to 'Turn energy saver on when battery level is at' choose a level (critical)"]
ES_ALWAYS = ["Start > Settings > System > Power & battery (critical)", "Expand Energy saver",
             "Set 'Always use energy saver' to On (critical)"]
BT_ON = "Make sure Bluetooth is turned on before pairing (page: 'Bluetooth needs to be turned on')"
BTQ = [BT_ON, "Put device in discoverable/pairing mode (critical)", "Select Network, Sound, or Battery icon on taskbar (critical)",
       "Select chevron on Bluetooth quick setting (Manage Bluetooth devices) (critical)",
       "Under New devices select the device; scroll Your devices if not visible (critical)", "Follow prompts, select Done (critical)"]
BTFIX = "Add a first step: 'Make sure Bluetooth is turned on.' It can be one short line using the page's own route, for example: Select the Network, Sound, or Battery icon near the clock and check the Bluetooth tile is on (or Start > Settings > Bluetooth & devices and set Bluetooth to On). Keep the other steps unchanged."
NOT = ["Start > Settings > System > Notifications (critical)", "Under 'Notifications from apps and other senders' select the app (critical)"]
MAG = ["Windows key + Plus sign turns Magnifier on (critical)", "Windows key + Plus again zooms in", "Windows key + Minus zooms out", "Windows key + Esc turns Magnifier off"]
LC = ["Windows logo key + Ctrl + L (critical)", "Accept consent prompt on first use", "Download language files if prompted"]
BR = ["Select Network icon at right end of taskbar (critical)", "Drag the Brightness slider (critical)"]

REVIEWS = [
 keep("tr173-a", CLEAN + ["Optional: File Explorer > This PC > Devices and drives shows free space"]),
 rev("tr173-c", PREV, [True]*4, [], {}, "", "", ) if False else keep("tr173-c", PREV),
 keep("tr173-b", [], nc=True, clar=True),
 keep("tr173-d", CLEAN),
 rev("tr173-e", MOVE, [True]*4,
     ["'Yes, you can move them to the USB drive and keep them safe' -> the page never says a USB drive keeps files safe and does not mention backups; Cut and Paste to one USB leaves a single copy"],
     {}, "G1 unsupported 'keep them safe' claim about the USB drive. It overpromises for family photos.",
     "Change the opening to 'Yes, you can move them to the USB drive instead of deleting them:' and remove 'keep them safe'. Keep the six steps. Keep the closing note but base it on the page wording: you can still use the files when the drive is connected, but they will not take up space on the PC.",
     source="fail"),
 keep("tr173-r", BIGF),
 keep("tr174-a", ES_Q),
 keep("tr174-c", ES_AUTO),
 keep("tr174-b", [], nc=True, clar=True),
 keep("tr174-d", ES_Q),
 keep("tr174-e", ES_ALWAYS),
 rev("tr174-r", ["Alternative route: Start > Settings > System > Power & battery > expand Energy saver > set Always use energy saver to On",
                 "Restart the PC", "Start > Settings > System > Troubleshoot > Other troubleshooters > Run next to Power"],
     [False, True, True], [],
     {"steps": 1},
     "The reply skips the page's Settings route for turning Energy saver on. The restart and Power troubleshooter appear on the page only under 'If battery life is still poor', so they should not be the only fix offered for the quick setting not working.",
     "Make step 1 the Settings route: Start, then Settings; System, then Power & battery; expand Energy saver; set Always use energy saver to On. Then keep the restart and Power troubleshooter steps as a second try ('If that does not help, restart the laptop, then ... next to Power select Run'). Keep to about five steps."),
 rev("tr175-a", BTQ, [False] + [True]*5, [], {"steps": 1},
     "Prerequisite 'Bluetooth needs to be turned on' is missing (non-critical).", BTFIX),
 rev("tr175-c", ["Bluetooth on", "Make printer discoverable", "Start > Settings (critical)", "Bluetooth & devices > Printers & scanners (critical)",
                 "Next to Add a printer or scanner select Add device (critical)", "Wait while Windows searches (can take a few minutes)", "Select Add device next to the printer (critical)"],
     [False, True, True, True, True, True, True],
     ["'A blinking light usually means it is ready to be found.' -> not on the page (the page does not mention a blinking light); it is from memory and can be wrong for some printers"],
     {"steps": 1}, "G1 unsupported claim about blinking light; Bluetooth-on prerequisite missing.",
     "Delete the sentence 'A blinking light usually means it is ready to be found.' and open with something like 'Here is how to add it:'. Keep step 1 (printer discoverable, see its manual). Add the line 'Make sure Bluetooth is turned on.' as a step before the Settings steps (Start > Settings > Bluetooth & devices, and check the Bluetooth switch is On).",
     source="fail"),
 keep("tr175-b", [], nc=True, clar=True),
 rev("tr175-d", BTQ, [False] + [True]*5, [], {"steps": 1},
     "Prerequisite 'Bluetooth needs to be turned on' is missing (non-critical).", BTFIX),
 rev("tr175-e", BTQ, [False] + [True]*5, [], {"steps": 1},
     "Prerequisite 'Bluetooth needs to be turned on' is missing (non-critical). The taskbar-only constraint is otherwise respected.",
     BTFIX + " Do not send the user into the Settings app (they said it confuses them); the quick settings Bluetooth tile is enough."),
 rev("tr175-r", ["Put device in pairing mode again", "Look through Your devices as well as New devices", "Check Bluetooth is On",
                 "Set Bluetooth devices discovery to Advanced (page: device not displayed in list)", "Computer must have Bluetooth; USB Bluetooth adapter if not"],
     [True, True, True, False, True], [], {"steps": 1},
     "The page's tip for a device not shown in the list, setting Bluetooth devices discovery to Advanced, is missing.",
     "Add a step: 'Select Start, then Settings, then Bluetooth & devices, then Devices. Under Device settings, set Bluetooth devices discovery to Advanced.' This path is on the second official page https://support.microsoft.com/en-us/windows/hardware/bluetooth/fix-bluetooth-problems-in-windows ; add that URL as a second source. Keep the other steps."),
 keep("tr176-a", NOT + ["Switch off 'Turn notifications on or off' (critical)"]),
 keep("tr176-c", NOT + ["Switch off 'Turn notifications on or off' (critical)"]),
 keep("tr176-b", [], nc=True, clar=True),
 keep("tr176-d", NOT + ["Switch off 'Turn notifications on or off' (critical)"]),
 keep("tr176-e", NOT[:1] + ["Select Mail", "Switch off 'Play a sound' (critical)", "Leave 'Turn notifications on or off' on"]),
 keep("tr176-r", ["Open Notifications settings and select Mail", "Switch 'Turn notifications on or off' back on (critical)",
                  "Switch off 'Show notification banners' (critical)", "Switch off 'Play a sound' (critical)"]),
 rev("tr177-a", MAG[:2], [True, True],
     ["'Magnifier is already built into Windows.' -> the page does not say this"],
     {}, "G1 unsupported sentence. The steps themselves match the page.",
     "Delete 'Magnifier is already built into Windows.' and start with 'Yes. Use the keyboard:' (or similar). Keep the two steps.", source="fail"),
 keep("tr177-c", MAG),
 keep("tr177-b", [], nc=True, clar=True),
 keep("tr177-d", MAG[:3]),
 rev("tr177-e", ["Turn Magnifier on with Windows key + Plus if off", "Switch to Lens view with Ctrl + Alt + L", "Back to full screen with Ctrl + Alt + F"],
     [True, True, True],
     ["'Press Ctrl + Alt + L' and 'Ctrl + Alt + F' -> the cited page does not list Lens or Full screen shortcuts"],
     {}, "Cited page does not cover the Lens and Full screen shortcuts. They are correct on another official page.",
     "Keep the reply as is and add a second source: https://support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier (it lists Full screen Ctrl+Alt+F, Lens Ctrl+Alt+L, Windows key+Plus to turn on).", source="fail"),
 keep("tr177-r", MAG[2:]),
 rev("tr178-a", LC, [True]*3,
     ["'Captions then appear for the sound your computer plays.' -> page says only detected speech is captioned; music and applause are not reliably captioned"],
     {}, "G1 overstatement of what live captions show.",
     "Replace the last line with 'Captions then appear for speech in what your computer plays.' (or 'for the spoken words').", source="fail"),
 keep("tr178-c", ["Start > Settings (critical)", "Accessibility > Captions (critical)", "Turn on Live captions toggle (critical)", "Consent prompt / language files on first use"]),
 keep("tr178-b", [], nc=True, clar=True),
 keep("tr178-d", LC[:2] + ["Language files may download"]),
 keep("tr178-e", ["Select battery, network, or volume icon on taskbar (critical)", "Turn on Live captions (critical)", "Consent / language files on first use"]),
 rev("tr178-r", ["Live captions use the default sound output device", "Settings > System > Sound", "Change the default output device to the headset (critical)"],
     [True, True, False], [], {"steps": 1, "actionable": 1},
     "The page says to change the default output device in Settings > System > Sound. The reply only says to check it and never tells the user to change it.",
     "Add after step 3: 'If it is not the headset you are using, change the default output device to your headset.' Then say to play the video again and check that captions show. Keep the first two steps."),
 keep("tr179-a", BR),
 keep("tr179-c", ["Start > Settings (critical)", "System > Display (critical)", "Move Brightness slider left to dim (critical)"]),
 keep("tr179-b", [], nc=True, clar=True),
 keep("tr179-d", BR[:1] + ["Move Brightness slider right (critical)"]),
 keep("tr179-e", ["Start > Settings > System > Display (critical)", "Select Brightness (critical)", "Turn on the toggle for changing brightness automatically when lighting changes (critical)",
                  "Note only some PCs support it", "Slider can still fine-tune"]),
 keep("tr179-r", ["Explain slider may not appear on desktop with external monitor", "Use buttons on the monitor (critical)"]),
]
