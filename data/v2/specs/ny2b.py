TASKS = [
    {
        "task_id": "TR-141",
        "task_type": "voicemail",
        "task": "Set up and listen to voicemail",
        "platform": "iPhone",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Apple Support: iPhone User Guide, Set up voicemail / Check voicemail", "url": "https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0"},
        "source_notes": """Set up (Visual Voicemail, select carriers/countries): 1. In the Phone app tap Voicemail, then tap Set Up Now (you see this the first time you tap Voicemail). 2. Create a voicemail password. 3. Choose a greeting, Default or Custom. If Custom, you can record a new greeting.
Listen: Siri works too ("Do I have any new voicemail?", "Play the voicemail from Eliza"). Or: 1. Tap Voicemail, then tap a message. Visual Voicemail shows a list of messages. A badge on the Voicemail icon shows how many messages you haven't heard. 2. Choose an action: Play (tap the Play button; messages stay saved until you delete them or your carrier erases them), Share (Share button), Delete (Delete button; some carriers permanently erase deleted messages; messages may be deleted if you change SIM card).
Recover deleted: tap Deleted Messages, tap the message, tap Undelete.
If Visual Voicemail isn't available: On your iPhone tap Voicemail, then follow the on-screen instructions. From another phone: call your own mobile number, press * or # (depending on carrier) to skip your greeting, then enter your voicemail password.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I set up voicemail on my iPhone?",
                 """Here is how to set up voicemail on your iPhone.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap **Set Up Now**.
4. Create a voicemail password.
5. Choose a greeting, either **Default** or **Custom**.
6. If you picked **Custom**, record your new greeting.

If you do not see **Set Up Now**, your phone may not offer Visual Voicemail. Tap **Voicemail** and follow the instructions on the screen.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My daughter set up my iPhone last year and voicemail is already working. There is a little red number on the Voicemail icon at the bottom of the Phone app and I think someone left me a message but I have never listened to one on this phone. How do I hear it? I would like to delete it afterward too.",
                 """The red number shows how many messages you have not heard yet. Here is how to listen and delete.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap the message you want.
4. Tap the **Play** button.
5. When it is done, tap the **Delete** button to remove it.

Messages stay saved until you delete them. If you delete one by mistake, tap **Deleted Messages**, tap the message, then tap **Undelete**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "Can you help me set up voicemail on my phone?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Can you help me set up voicemail on my phone?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "It's an iPhone.",
                 """Thank you. Here is how to set up voicemail on an iPhone.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap **Set Up Now**.
4. Create a voicemail password.
5. Choose a greeting, either **Default** or **Custom**.
6. If you picked **Custom**, record your new greeting.

If you do not see **Set Up Now**, tap **Voicemail** and follow the instructions on the screen.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "sources": [{"title": 'Apple Support: iPhone User Guide, Set up voicemail / Check voicemail', "url": 'https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0', "accessed": "2026-11-13"}, {"title": 'Apple Support: iPhone User Guide, Turn on and activate Siri', "url": 'https://support.apple.com/guide/iphone/turn-on-and-activate-siri-iph83aad8922/ios', "accessed": "2026-11-13"}],
             "messages": [
                 "I have an iPhone and my fingers shake so I really struggle to tap the little buttons in the Phone app. Is there any way to find out if I have new voicemail without tapping through all the screens? I can talk to the phone fine.",
                 """Yes, you can ask Siri instead of tapping. Use your voice:

1. Say "Hey Siri" to wake Siri.
2. Then say something like "Do I have any new voicemail?"
3. Or say "Play the voicemail from" and then the name of the person, for example "Play the voicemail from Eliza."

Siri will answer or play the message for you. If Siri does not answer when you say "Hey Siri", that phrase may not be turned on yet. Someone can help you open **Settings**, tap **Siri**, and tap **Turn On Siri**. If you ever want to tap instead, open the **Phone** app, tap **Voicemail**, then tap a message and tap the **Play** button.

If voicemail was never set up on this phone, ask a helper to open the **Phone** app, tap **Voicemail**, tap **Set Up Now**, create a voicemail password, and choose a greeting.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone keeps saying I have no voicemail greeting. Please walk me through setting up my voicemail.",
                 """Here is how to set up voicemail on your iPhone.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap **Set Up Now**.
4. Create a voicemail password.
5. Choose a greeting, either **Default** or **Custom**.
6. If you picked **Custom**, record your new greeting.

If you do not see **Set Up Now**, tap **Voicemail** and follow the instructions on the screen.""",
                 "I tapped Voicemail but there is no Set Up Now button. It just shows something different.",
                 """That can happen when your phone does not offer Visual Voicemail. Try this.

1. Open the **Phone** app and tap **Voicemail**.
2. Follow the instructions on the screen.

Or you can use another phone.

1. Call your own mobile number.
2. When your greeting plays, press * or #, depending on your carrier, to skip it.
3. Enter your voicemail password.""",
             ]},
        ],
    },
    {
        "task_id": "TR-142",
        "task_type": "call_forwarding",
        "task": "Forward calls to another number",
        "platform": "iPhone",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Apple Support: iPhone User Guide, Set up call forwarding on iPhone", "url": "https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios"},
        "source_notes": """Meta: In Phone on iPhone, set up call forwarding (on GSM networks).
Steps: 1. Open Settings, tap Apps, then tap Phone. 2. Tap Call Forwarding, then turn on Call Forwarding. A Call Forwarding icon appears in the status bar while it is active. 3. Tap Forward To, enter the number to forward calls to, then tap Back. If iPhone has Dual SIM, choose a line (below SIMs).
Notes: applies if you have cellular service on a GSM network; if you use a CDMA network, contact your carrier. You must be in range of the cellular network when you set up forwarding, or calls won't forward. The page does not explain how to turn forwarding off.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I forward my iPhone calls to my husband's phone number?",
                 """Here is how to forward your calls on an iPhone.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To**.
7. Type in your husband's phone number.
8. Tap **Back**.

You will see a Call Forwarding icon at the top of the screen while it is on. Your phone must be in range of the cellular network when you do this, or calls will not forward.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I'm going on a cruise next week and I will not have my iPhone with me, it is staying at home with the charger. My son said I can send calls to his number so I don't miss anything from the doctor's office. My iPhone has two SIMs in it because I travel for work. Please tell me what to do.",
                 """Yes, you can forward your calls to your son's number. Set it up before you leave.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Because your iPhone has Dual SIM, choose a line under **SIMs**.
7. Tap **Forward To**.
8. Type in your son's number.
9. Tap **Back**.

A Call Forwarding icon shows at the top of the screen while it is on. Your phone must be in range of the cellular network when you set it up, or calls will not forward. If your phone service uses a CDMA network, ask your carrier for setup information.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I need my calls to go to my sister's number for a week. How?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I need my calls to go to my sister's number for a week. How?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone",
                 """Thank you. Here is how to forward calls on an iPhone.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To**.
7. Type in your sister's number.
8. Tap **Back**.

A Call Forwarding icon shows at the top of the screen while it is on.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone is on a CDMA network, my grandson told me that's the kind of service I have. I would like to send calls to my neighbor's number while I'm in the hospital. Can you give me the steps for that?",
                 """The iPhone steps for call forwarding are for phones on a GSM network. Since your service is CDMA, please contact your carrier and ask them to set up call forwarding for you.

If your carrier tells you that you are on a GSM network, the steps are these.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding** and turn it on.
5. Tap **Forward To**, type your neighbor's number, then tap **Back**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Please help me make my iPhone send my calls to my cell number at my cabin.",
                 """Here is how to forward your calls on an iPhone.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To**.
7. Type in the number.
8. Tap **Back**.

You will see a Call Forwarding icon at the top of the screen while it is on.""",
                 "I did all that but when my friend called me it didn't go to the other number. What went wrong?",
                 """Two things are worth checking.

1. Your phone must be in range of the cellular network when you set up forwarding. If it was not, calls will not forward. Move to a spot with signal and set it up again.
2. Call forwarding works on a GSM network. If your phone uses a CDMA network, contact your carrier.""",
             ]},
        ],
    },
    {
        "task_id": "TR-143",
        "task_type": "flash_alerts",
        "task": "Make the light flash for alerts",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Get LED flash alerts on your iPhone or iPad", "url": "https://support.apple.com/en-us/111774"},
        "source_notes": """Steps: 1. Open Settings, go to Accessibility, then select Audio/Visual. 2. Turn on LED Flash for Alerts. 3. Optional: to keep the flash from blinking in silent mode, turn off Flash on Silent. Leave it on if you want flashes in silent mode.
What you see: the LED flash next to the camera lens blinks when your device is locked and you get a notification. Can help if you might miss audible alerts.
Condition: LED Flash for Alerts works only when your device is locked.
Page does not mention phone calls specifically and has no troubleshooting steps beyond: setting on, device locked, Flash on Silent set the way you want.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have trouble hearing my iPhone. Can I make the little light on the back flash when I get an alert?",
                 """Yes, your iPhone can blink its light for alerts.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

After that, the light next to the camera lens blinks when you get a notification. This only works while the phone is locked.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I work in a loud garage all day and my iPhone is always on silent so it doesn't buzz off my workbench. My wife says I miss her messages. I've heard there is a setting where the flashlight blinks. I want it to blink even though the phone is on silent. I'm on an iPhone. What should I do?",
                 """Yes, there is a setting for that.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.
5. Make sure **Flash on Silent** is turned on.

With both on, the light next to the camera lens blinks when you get a notification, even in silent mode. It only blinks while the phone is locked.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "My hearing isn't good. Is there a way to have a light blink on my phone instead of a sound?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My hearing isn't good. Is there a way to have a light blink on my phone instead of a sound?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "It is an iPhone",
                 """Thank you. On an iPhone, you can make the light blink for alerts.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

The light next to the camera lens will then blink when you get a notification. This only works while the phone is locked.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I want my iPhone light to blink for alerts, but at church and at night I put my phone on silent and I do NOT want it blinking then. I only want the light when the phone isn't on silent. It's an iPhone.",
                 """You can do that.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.
5. Turn off **Flash on Silent**.

Now the light blinks for notifications, but not while your phone is in silent mode. It only blinks while the phone is locked.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Is there a setting to make my iPhone's flash blink when something comes in? I keep missing things.",
                 """Yes, there is.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

The light next to the camera lens blinks when you get a notification while the phone is locked.""",
                 "I turned it on but I was holding the phone and reading it, and the light never blinked when a message came.",
                 """That is expected. **LED Flash for Alerts** only works when your phone is locked.

1. Put the phone down and lock it.
2. Wait for the next notification. The light next to the camera lens should blink.

If you are still not seeing it, go back to **Settings**, **Accessibility**, **Audio/Visual** and check that **LED Flash for Alerts** is on.""",
             ]},
        ],
    },
    {
        "task_id": "TR-144",
        "task_type": "find_model",
        "task": "Find the model number of the iPhone to identify which model it is",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Find the model number of your iPhone, iPad, or iPod touch", "url": "https://support.apple.com/en-us/106343"},
        "source_notes": """From 106343. In Settings: 1. Open Settings and tap General. 2. Tap About. 3. To the right of Model Number you find the part number. Tap it to reveal the model number.
On the device, by model: iPhone 7 or earlier: check the back of the device. iPhone 8 or later with a SIM tray: remove the SIM tray and look in the slot, in bright overhead light; the model number is on the upper side (the side with the display). iPhone without a SIM tray: look in the USB-C or Lightning connector, in bright overhead light, on the upper side (the side with the display).
Not covered by 106343: prefix meanings, A-number, what appears after tap beyond the model number.
Supplement from the companion page 108044 (Identify your iPhone model): model numbers begin with A followed by four digits; match the number to the entry for the model in Apple's iPhone model list; the same model can have different numbers by region. Page does not give how to remove the SIM tray, so do not describe how.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How can I find out which model my iPhone is? I'm trying to sell it.",
                 """You can find the model number in Settings.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. The part number is shown to its right.
5. Tap that part number and it changes to the model number.

Use that number when you sell the phone.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I found my old iPhone 7 in a drawer, the one my late husband used. The battery is dead and I don't have the right charger so I can't turn it on. A repair shop asked me for the model number. Is there a way to see it without turning it on?",
                 """Yes. On an iPhone 7 or earlier, the model number is on the back of the phone.

1. Turn the phone over so the back faces you.
2. Look at the writing on the back and find the model number.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "What model is my phone? The store wants to know.",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "What model is my phone? The store wants to know.",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iphone",
                 """Thank you. Here is how to find the model number on an iPhone.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. A part number is shown to its right.
5. Tap that part number and it changes to the model number.

You can tell the store that number.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I forgot the passcode on my iPhone 8 so I can't open Settings, and I do not want to try guessing it. It has a SIM tray on the side. Can I still find the model number some other way?",
                 """Yes. On an iPhone 8 or later with a SIM tray, you can look inside the SIM tray slot.

1. Remove the SIM tray from the side of the phone.
2. Hold the tray slot under bright overhead light and look inside the slot.
3. Look on the upper side of the slot, the side with the display. The model number is there.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Please show me where the model number is on my iPhone, I need it for an insurance form.",
                 """You can find it in Settings.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. A part number is shown to its right.
5. Tap that part number and it changes to the model number.""",
                 "I got to About and Model Number but the number there is a long one that doesn't look like what the insurance form wants.",
                 """That long number is the part number. Tap it once.

1. On the **About** screen, find **Model Number**.
2. Tap the number to the right of it.
3. It changes to the model number. Use that one on the form.""",
             ]},
        ],
    },
    {
        "task_id": "TR-145",
        "task_type": "scan_document",
        "task": "Scan a paper document with the phone",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: How to scan documents on your iPhone or iPad", "url": "https://support.apple.com/en-us/108963"},
        "source_notes": """Scan in Notes: 1. Open Notes, then select a note or create a new one. 2. Tap the Attachment button (paperclip icon), then tap Scan Documents. 3. Place the document in view of the camera. (On iOS 26 you can also choose options such as flash or an image filter.) 4. Auto: if the device is in Auto mode, the document scans automatically. Manual: to capture the scan yourself, tap the Shutter button or press a Volume button. Then drag the corners to fit the page and tap Keep Scan. 5. Tap Done, or add more scans to the document.
To start a scan from an open note: tap the More button (ellipsis icon), then tap Scan.
Use Files: 1. In the Files app tap the More button (ellipsis icon). 2. Tap Scan Documents. 3. Place the document in view of the camera (iOS 26: flash or image filter options). 4. Auto or manual capture as above; drag the corners to fit the page, tap Keep Scan. 5. Tap Done, or add more scans. 6. Choose a location, then tap Save.
Page has no troubleshooting section and does not say how to switch between Auto and Manual. Page does not name Retake, crop or share buttons.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I scan a paper form with my iPhone so I can email it?",
                 """You can scan it in the Notes app.

1. Open **Notes**.
2. Open a note, or start a new one.
3. Tap the paperclip button.
4. Tap **Scan Documents**.
5. Hold the phone so the paper is in view of the camera. If your phone is in Auto mode, it scans by itself.
6. Tap **Done**.

If the paper has more pages, scan them before you tap **Done**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I never use the Notes app on my iPhone, I only know the Files app because my grandson put my tax papers in there. I have a letter from the county on my kitchen table that I want to scan and keep in Files. How do I do that? I want it saved in a folder, not floating around.",
                 """You can scan it right inside the Files app.

1. Open **Files**.
2. Tap the **More** button, the three dots.
3. Tap **Scan Documents**.
4. Hold the phone so the letter is in view of the camera. In Auto mode it scans by itself.
5. Tap **Done**, or scan more pages first.
6. Choose the folder where you want it.
7. Tap **Save**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i scan a paper with my phone",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "how do i scan a paper with my phone",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "its an iphone",
                 """Thank you. On an iPhone you can scan in the Notes app.

1. Open **Notes**.
2. Open a note, or start a new one.
3. Tap the paperclip button.
4. Tap **Scan Documents**.
5. Hold the phone so the paper is in view of the camera. In Auto mode it scans by itself.
6. Tap **Done**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an iPhone. When I scan, the phone grabs the picture too fast before I have the paper lined up. I want to be the one who decides when it takes the picture. How do I scan a bill in Notes that way?",
                 """You can capture the scan yourself.

1. Open **Notes**, then open a note or start a new one.
2. Tap the paperclip button.
3. Tap **Scan Documents**.
4. Line up the bill in view of the camera.
5. Tap the Shutter button, or press a Volume button, when you are ready.
6. Drag the corners so they fit the page.
7. Tap **Keep Scan**.
8. Tap **Done**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone needs to scan my lease papers. Can you tell me how in the Notes app?",
                 """Here is how to scan in Notes.

1. Open **Notes**.
2. Open a note, or start a new one.
3. Tap the paperclip button.
4. Tap **Scan Documents**.
5. Hold the phone so the paper is in view of the camera. In Auto mode it scans by itself.
6. Tap **Done**.""",
                 "I pointed it at the paper but it never scanned by itself. It just keeps showing the camera.",
                 """Then capture it yourself.

1. With the paper in view, tap the Shutter button, or press a Volume button.
2. Drag the corners so they fit the page.
3. Tap **Keep Scan**.
4. Tap **Done**, or scan more pages first.""",
             ]},
        ],
    },
    {
        "task_id": "TR-146",
        "task_type": "home_screen_organize",
        "task": "Move apps and organize the Home Screen",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Move apps and create folders on your iPhone, iPad, or iPod touch", "url": "https://support.apple.com/en-us/108307"},
        "source_notes": """Organize apps: 1. Touch and hold any app until options appear, then tap Edit Home Screen. 2. Drag the app to a new spot, such as the Dock at the bottom of the screen. 3. Save your changes: on iPhone X and later tap Done; on iPhone 8 and earlier press the Home button.
Move an app to another page: 1. Touch and hold an app until the apps jiggle. 2. Drag the app to the right edge of the screen. A new page may take a second to appear. 3. The dots above the Dock show your current page. If there are dots to the right of the bright dot, drag the app toward that side to reach the next page. Otherwise swipe left to view the apps on that page. 4. If there are no dots to the right of the bright dot, dragging an app to that side creates a new page.
Create a folder: 1. Touch and hold an app until the apps jiggle. 2. Drag one app onto another app to create the folder. 3. Drag more apps into the folder.
Rename a folder: touch and hold the folder until the quick actions menu appears, tap Rename, type the name, tap Done.
Notes: deleting a page: move all apps to another Home Screen; a page with no apps is deleted. iOS 16 and later: Search appears at the bottom instead of the page dots until you scroll through your Home Screen pages. Page does not explain how to delete a folder.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I move the Weather app to the bottom row of my iPhone so it's easier to reach? I have an iPhone 14.",
                 """Here is how to move an app on your iPhone.

1. Touch and hold the Weather app until a menu appears.
2. Tap **Edit Home Screen**.
3. Drag the app to its new spot, such as the Dock at the bottom of the screen.
4. Tap **Done** to save your change.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone 8 has so many apps on the first page that I can't find anything. I want the Camera app moved over to the second page of my Home Screen. I am afraid of messing something up. The phone has the round Home button at the bottom. What do I do exactly?",
                 """Here is how to move the Camera app to another page.

1. Touch and hold the Camera app until the apps jiggle.
2. Drag the app to the right edge of the screen. A new page may take a second to appear.
3. Let go of the app when it is on the page you want.
4. Press the Home button to save your changes.

If you do not see dots to the right of the bright dot above the Dock, dragging to the right edge makes a new page.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "The apps on my phone are all in a mess. How do I put them where I want?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "The apps on my phone are all in a mess. How do I put them where I want?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone, a newer one with no home button",
                 """Thank you. Here is how to move apps on your iPhone.

1. Touch and hold any app until a menu appears.
2. Tap **Edit Home Screen**.
3. Drag the app to its new spot.
4. Repeat for any other apps you want to move.
5. Tap **Done** to save your changes.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an iPhone and I have six card game apps all over my screen. I do NOT want to delete any of them, I just want them together in one place. Is there a way to group them?",
                 """Yes, you can put them in a folder. Nothing gets deleted.

1. Touch and hold one of the game apps until the apps jiggle.
2. Drag it onto another game app. This makes a folder.
3. Drag each of the other game apps into the folder.

To give the folder a name, touch and hold the folder until a menu appears, tap **Rename**, type the name, then tap **Done**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Can you tell me how to get my Photos app onto a different page of my iPhone Home Screen? I'm on an iPhone with Face ID.",
                 """Here is how to move Photos to another page.

1. Touch and hold the Photos app until the apps jiggle.
2. Drag the app to the right edge of the screen.
3. Let go when you are on the page you want.
4. Tap **Done** to save your change.""",
                 "I dragged it to the right edge but nothing happened, the page didn't change.",
                 """Try this.

1. Keep holding the app at the right edge for a second. A new page may take a moment to appear.
2. Look at the dots above the Dock. If there are dots to the right of the bright dot, keep dragging toward that side to reach the next page.
3. If there are no dots to the right, dragging to that side makes a new page.""",
             ]},
        ],
    },
]
