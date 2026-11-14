# Reviews for batch ex5, round 1. Independent reviewer.
# Sources fetched with WebFetch on 2026-11-13 (all 13 URLs readable; extra checks on a few claims).

S_ALL2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}
SRC_FAIL = {"source": "fail", "safety": "pass", "duplicate": "pass"}


def s(**kw):
    d = dict(S_ALL2)
    d.update(kw)
    return d


def clar(id, decision="keep", ask=2, reasons="", fix=""):
    return {
        "id": id, "required_actions": [], "covered": [], "needs_clarification": True,
        "gates": dict(PASS), "unsupported_claims": [],
        "scores": s(steps="NA", ask_or_answer=ask),
        "decision": decision, "reasons": reasons, "fix": fix,
    }


REVIEWS = []

# ---------- tr062: Free up storage (Android) support.google.com/android/answer/7431795 ----------
RA_62 = [
    "Open Settings and tap Storage (critical)",
    "Tap Free up space (critical)",
    "Scroll to a category and tap Select files; if the category is not listed, tap Browse (critical)",
    "Select the files to delete (critical)",
    "Tap Move files to Trash (critical)",
    "Optional: delete phone copies of photos already backed up in Google Photos",
    "Optional: uninstall unused apps (can be reinstalled without paying again)",
]
UNSUP_62 = ["'Tap **Storage**. You'll see which kinds of files use the most space.' -> the page only says 'Tap Storage' then 'Select a category'; it does not say what the user sees or that files are shown by size"]
FIX_62 = ("In step 2 delete the sentence \"You'll see which kinds of files use the most space.\" (page only says: Settings > Storage > Free up space, then scroll to a category and tap Select files; if the category isn't listed, tap Browse). "
          "Optionally add 'If you don't see the category, tap **Browse**.' after step 4.")
REVIEWS.append({
    "id": "tr062-a", "required_actions": RA_62, "covered": [True] * 7, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_62, "scores": s(),
    "decision": "revise", "reasons": "Unsupported 'what you will see' cue after tapping Storage.", "fix": FIX_62,
})
REVIEWS.append(clar("tr062-b"))
REVIEWS.append(clar("tr062-c"))
REVIEWS.append({
    "id": "tr062-d", "required_actions": RA_62, "covered": [True] * 7, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_62, "scores": s(plain=1),
    "decision": "revise",
    "reasons": "Unsupported 'what you will see' cue. The same hedge is said twice (lead-in 'Samsung menus can look a little different, so tell me if something doesn't match' and closing 'Menu names vary between phones ... Tell me what you see if something doesn't match').",
    "fix": FIX_62 + " Also keep the Samsung hedge only once: delete either the lead-in sentence or the closing paragraph.",
})

# ---------- tr063: Flashlight (iPhone) support.apple.com/en-us/105001 ----------
RA_63 = [
    "Open Control Center: pull down from top-right corner (Face ID) or swipe up from bottom edge (Home button) (critical)",
    "Tap the flashlight icon to turn on, tap again to turn off (critical)",
    "Lock Screen: press and hold the Flashlight button in the bottom-left corner",
    "Siri: say 'Hey Siri, turn on my flashlight'",
]
REVIEWS.append({
    "id": "tr063-a", "required_actions": RA_63, "covered": [True] * 4, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(),
    "decision": "keep", "reasons": "", "fix": "",
})
REVIEWS.append(clar(
    "tr063-b", "revise", ask=1,
    reasons="Two questions ('Do you mean the flashlight?' and 'Is your phone an iPhone or an Android phone?'). The 'do you mean flashlight' check is not needed to choose the steps.",
    fix="Replace the reply with one question only, for example: 'I can help with the flashlight. Is your phone an **iPhone** or an **Android** phone?' (one question mark). The first assistant turn of tr063-d is identical and must be changed the same way, with the user's follow-up adjusted to 'iPhone'."))
REVIEWS.append(clar("tr063-c"))
REVIEWS.append({
    "id": "tr063-d", "required_actions": RA_63, "covered": [True] * 4, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(),
    "decision": "keep", "reasons": "", "fix": "",
})

# ---------- tr064: Flashlight (Android) support.google.com/android/answer/9083864 ----------
# The cited page is 'Change settings quickly on your Android phone'. Two fetches: no mention of Flashlight, no pencil icon.
UNSUP_64 = [
    "'Tap **Flashlight**. A dimmed icon means it's off.' -> the page never mentions a Flashlight quick setting (no text, caption or alt text); only generic 'Dimmed settings are off'",
    "'Tap the **edit** icon (a pencil).' -> the page says 'tap Edit' with an image that has no alt text; no pencil is described",
    "'find **Flashlight**, and tap **Add**' -> the page says to find the setting you want and tap Add; Flashlight is not named",
]
RA_64 = [
    "Swipe down from the top of the screen; swipe down again to see all Quick Settings (critical)",
    "Tap the setting's icon to turn it on or off; dimmed means off (critical)",
    "Missing setting: swipe down twice, tap Edit, scroll to the setting and tap Add, drag to arrange",
]
REVIEWS.append({
    "id": "tr064-a", "required_actions": RA_64, "covered": [True] * 3, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_64, "scores": s(),
    "decision": "reject",
    "reasons": "The cited page is about changing Quick Settings in general and never mentions the flashlight. I searched support.google.com for an official Android flashlight page and found none, so the task cannot be sourced.",
    "fix": "",
})
REVIEWS.append(clar("tr064-b"))
REVIEWS.append({
    "id": "tr064-c", "required_actions": RA_64, "covered": [True] * 3, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_64, "scores": s(plain=1),
    "decision": "reject",
    "reasons": "Same source problem as tr064-a (flashlight not on the cited page). Also the lead-in is pasted twice ('...you can add it:' then 'Here's the quickest way.').",
    "fix": "",
})
REVIEWS.append({
    "id": "tr064-d", "required_actions": RA_64, "covered": [True] * 3, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_64, "scores": s(),
    "decision": "reject",
    "reasons": "Same source problem as tr064-a (flashlight not on the cited page).",
    "fix": "",
})

# ---------- tr066: Set an alarm (iPhone) support.apple.com/en-us/118444 ----------
RA_66 = [
    "Open the Clock app and tap the Alarms tab (critical)",
    "Tap the Add button (critical)",
    "Set the time (critical)",
    "Optional: Repeat for recurring alarms",
    "Tap Done when creating a new alarm (Save is only for editing an existing alarm) (critical)",
    "Silent mode and Do Not Disturb do not affect the alarm sound",
    "If too quiet: Settings > Sounds & Haptics, drag the Ringtone and Alerts slider",
    "If it only vibrates: the alarm's Sound may be None; choose a sound",
]
COV_66 = [True, True, True, True, False, True, True, True]
UNSUP_66 = [
    "'Tap **Alarms** at the bottom.' -> page says only 'tap the Alarms tab'; no position given",
    "'Tap the **plus (+)** button.' -> page says 'Tap the Add button'; the icon has no alt text or description",
    "'Tap **Save** (on some versions, **Done**).' -> page says tap Done when creating an alarm; Save appears only when editing an existing alarm",
]
FIX_66 = ("Rewrite the steps to match the page: 1. Open the **Clock** app, then tap the **Alarms** tab. 2. Tap the **Add** button. 3. Set the time to 6:30 AM. 4. (optional) Tap **Repeat** to choose days. 5. Tap **Done**. "
          "Remove 'at the bottom', '(+)' and 'Save (on some versions, Done)'. Keep the Silent/Do Not Disturb, Sounds & Haptics > Ringtone and Alerts, and Sound/None lines.")
REVIEWS.append({
    "id": "tr066-a", "required_actions": RA_66, "covered": COV_66, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_66, "scores": s(steps=1),
    "decision": "revise", "reasons": "Wrong finishing button and two unsupported UI descriptions.", "fix": FIX_66,
})
REVIEWS.append(clar(
    "tr066-b", "revise", ask=1,
    reasons="Asks two things (phone type AND wake-up time). The time does not change the steps, so it should not be asked first.",
    fix="Ask only: 'Sure. Is your phone an **iPhone** or an **Android** phone?' Update tr066-d's first assistant turn the same way and change the user's follow-up there to 'iPhone' (the final reply can then ask nothing, or the time can be left out)."))
REVIEWS.append({
    "id": "tr066-c", "required_actions": RA_66, "covered": COV_66, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_66, "scores": s(steps=1, plain=1),
    "decision": "revise",
    "reasons": "Wrong finishing button and unsupported UI descriptions. Lead-in is pasted twice ('Here's how to make sure you're up at 6:30:' then 'Here's how. It takes about a minute.'). The user needs a single wake-up tomorrow, so the 'If you want it every day' step is not needed.",
    "fix": FIX_66 + " Use one lead-in sentence only, and make the Repeat step optional ('Only if you want it to repeat, tap Repeat').",
})
REVIEWS.append({
    "id": "tr066-d", "required_actions": RA_66, "covered": COV_66, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_66, "scores": s(steps=1, plain=1),
    "decision": "revise",
    "reasons": "Wrong finishing button and unsupported UI descriptions. Lead-in is pasted twice ('Here's how to set it for 6:30.' then 'Here's how. It takes about a minute.'). Earlier turn asks two questions, which should be changed to one (see tr066-b).",
    "fix": FIX_66 + " Use one lead-in sentence only.",
})

# ---------- tr067: Set an alarm (Android Clock) support.google.com/android/answer/2840926 ----------
RA_67 = [
    "Open the Clock app (critical)",
    "Tap Alarm (critical)",
    "Tap Add (critical)",
    "Set the time: analog = drag hour hand then minute hand, digital = enter hour and minutes; choose AM or PM (critical)",
    "Tap OK (critical)",
    "Keep alarm volume above 30%",
    "Leave at least 5 minutes between alarms",
]
REVIEWS.append({
    "id": "tr067-a", "required_actions": RA_67, "covered": [True] * 7, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(),
    "decision": "keep", "reasons": "", "fix": "",
})
REVIEWS.append(clar("tr067-b"))
REVIEWS.append(clar(
    "tr067-c", "revise", ask=1,
    reasons="Asks two questions (7 AM or PM, and phone type). AM/PM does not change the steps, and there are two question marks.",
    fix="Ask only: 'Sure. Is your phone an **iPhone** or an **Android** phone?' (one question mark)."))
REVIEWS.append({
    "id": "tr067-d", "required_actions": RA_67, "covered": [True] * 7, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(),
    "decision": "keep", "reasons": "", "fix": "",
})

# ---------- tr068: Pair hearing aids (iPhone) support.apple.com/en-us/108780 ----------
RA_68 = [
    "Make sure iOS is up to date (critical)",
    "Put the hearing aids in pairing mode (battery door open/close, off/on, or remove from charger; user guide has specifics) (critical)",
    "Open Settings > Accessibility > Hearing Devices (critical)",
    "Tap Pair MFi Hearing Device, follow the onscreen instructions, select the device, tap Pair (critical)",
    "If Pair MFi Hearing Device is not shown: tap the hearing device's name under Hearing Devices, then Pair",
]
UNSUP_68 = [
    "'Your audiologist can also help.' -> the page does not mention audiologists; it points to the hearing device's user guide, the manufacturer's app, and the vendor",
]
FIX_68 = ("(1) Replace 'Your audiologist can also help.' with page-supported help: 'If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.' "
          "(2) Split step 6 into two steps: '6. Tap **Pair MFi Hearing Device** and follow the steps on the screen. 7. Select your hearing aids, then tap **Pair**.' Then add: 'If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.'")
REVIEWS.append({
    "id": "tr068-a", "required_actions": RA_68, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_68, "scores": s(actionable=1),
    "decision": "revise", "reasons": "Unsupported audiologist referral; step 6 bundles two branches plus the Pair tap in one step.", "fix": FIX_68,
})
REVIEWS.append(clar("tr068-b"))
REVIEWS.append({
    "id": "tr068-c", "required_actions": RA_68, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_68, "scores": s(actionable=1, plain=1),
    "decision": "revise",
    "reasons": "Unsupported audiologist referral; step 6 bundles actions. Lead-in is pasted twice ('Here's how to connect them:' then 'Here's how to pair them. It takes a few minutes.').",
    "fix": FIX_68 + " Also use a single lead-in sentence.",
})
REVIEWS.append({
    "id": "tr068-d", "required_actions": RA_68, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_68, "scores": s(actionable=1),
    "decision": "revise", "reasons": "Unsupported audiologist referral; step 6 bundles two branches plus the Pair tap in one step.", "fix": FIX_68,
})

# ---------- tr069: Pair Bluetooth headphones (Android) support.google.com/android/answer/9417604 ----------
RA_69 = [
    "Make the headphones discoverable / ready to pair, following their instructions (critical; NOT on the cited page, see https://support.google.com/android/answer/9769184?hl=en)",
    "Pull down from the top edge of the screen (critical)",
    "Touch and hold the Bluetooth icon (critical)",
    "Tap Pair new device (critical)",
    "Tap the name of the headphones (critical)",
    "Follow the on-screen instructions (critical)",
    "If there is no 'Pair new device': check under Available devices, or tap More then Refresh",
    "If asked for a passcode and you don't have it, try 0000 or 1234",
]
UNSUP_69 = [
    "'Put your headphones in **pairing mode**. Each brand does this differently, so check the instructions that came with them.' -> the cited page has no text about pairing mode or the accessory's instructions",
    "'If your headphones don't appear, check under **Available devices**, or tap **More** and then **Refresh**.' -> the page gives this only for when the 'Pair new device' option is missing, not for when the headphones don't show up",
]
FIX_69 = ("Add a second source https://support.google.com/android/answer/9769184?hl=en (it says 'Check that your accessory is discoverable and ready to pair' and 'Follow the instructions that came with your accessory'). "
          "Reword step 1: 'Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.' (avoid the unsourced claim that brands differ). "
          "Reword troubleshooting: 'If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.' Keep the 0000/1234 line.")
REVIEWS.append({
    "id": "tr069-a", "required_actions": RA_69, "covered": [False] + [True] * 7, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_69, "scores": s(),
    "decision": "revise", "reasons": "Pairing-mode step and the Refresh troubleshooting line are not supported by the cited page as worded.", "fix": FIX_69,
})
REVIEWS.append(clar("tr069-b"))
REVIEWS.append(clar(
    "tr069-c", "revise", ask=1,
    reasons="Two questions (what won't connect, and iPhone or Android). Two question marks.",
    fix="Ask one question only: 'It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else?'"))
REVIEWS.append({
    "id": "tr069-d", "required_actions": RA_69, "covered": [False] + [True] * 7, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_69, "scores": s(),
    "decision": "revise", "reasons": "Pairing-mode step and the Refresh troubleshooting line are not supported by the cited page as worded.", "fix": FIX_69,
})

# ---------- tr070: Low Power Mode (iPhone) support.apple.com/en-us/101604 ----------
RA_70 = [
    "Control Center: swipe down from the top-right corner, tap the battery icon (critical)",
    "Or Settings > Battery; iPhone 15 and later: Power Mode > Low Power Mode; iPhone 14 and earlier: turn on Low Power Mode (critical)",
    "Battery icon turns yellow when on",
    "Turns off automatically when charged to 80% or higher",
]
UNSUP_70A = ["'It turns off by itself once you charge above 80%.' -> page says 'When you charge the device to 80% or higher'"]
REVIEWS.append({
    "id": "tr070-a", "required_actions": RA_70, "covered": [True] * 4, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_70A, "scores": s(),
    "decision": "revise", "reasons": "Number stated differently from the page.",
    "fix": "Change the last sentence to 'It turns off by itself once the battery is charged to 80% or higher.'",
})
REVIEWS.append(clar("tr070-b"))
REVIEWS.append(clar("tr070-c"))
REVIEWS.append({
    "id": "tr070-d", "required_actions": RA_70, "covered": [True] * 4, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_70A, "scores": s(plain=1),
    "decision": "revise",
    "reasons": "Number stated differently from the page. The user said iPhone 14 but the reply still gives the 'iPhone 15 and newer' branch and the 'older iPhones' branch.",
    "fix": "Change the last sentence to 'It turns off by itself once the battery is charged to 80% or higher.' In Settings step 3 say only: 'Turn on **Low Power Mode**.' (iPhone 14 and earlier: Settings > Battery > Low Power Mode) and drop the iPhone 15 branch.",
})

# ---------- tr071: Battery Saver (Android) support.google.com/android/answer/7664692 ----------
RA_71 = [
    "Open the Settings app (critical)",
    "Tap Battery, then Battery Saver (critical)",
    "Choose a schedule for Battery Saver, or have it turn off automatically",
    "Dark theme and limited background activity while on",
    "Some phones use another name such as low power mode",
]
UNSUP_71 = ["'Tap **Battery Saver** and turn it on.' -> the page's step 3 is 'Choose a schedule for battery saver mode or automatically turn it off'; it names no on/off switch, so 'turn it on' is not supported"]
FIX_71 = ("Make step 3 match the page: 'Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.' If the writer wants an explicit 'turn it on' step, add a second official Google/Android page that names the switch and cite it. "
          "Keep the dark-theme/background and 'some phones call it low power mode' lines.")
REVIEWS.append({
    "id": "tr071-a", "required_actions": RA_71, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_71, "scores": s(),
    "decision": "revise", "reasons": "'Turn it on' step is not on the cited page.", "fix": FIX_71,
})
REVIEWS.append(clar("tr071-b"))
REVIEWS.append({
    "id": "tr071-c", "required_actions": RA_71, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_71, "scores": s(plain=1),
    "decision": "revise",
    "reasons": "'Turn it on' step is not on the cited page. Lead-in is pasted twice ('Here's how to turn it on. Menu names on Samsung phones can differ a little:' then 'Here's how. It takes less than a minute.').",
    "fix": FIX_71 + " Use a single lead-in sentence that includes the Samsung hedge.",
})
REVIEWS.append({
    "id": "tr071-d", "required_actions": RA_71, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_71, "scores": s(),
    "decision": "revise", "reasons": "'Turn it on' step is not on the cited page.", "fix": FIX_71,
})

# ---------- tr072: Update apps (iPhone) support.apple.com/en-us/102629 ----------
RA_72 = [
    "Open the App Store (critical)",
    "Tap your profile picture or My Account button at the top (critical)",
    "Tap App Updates (critical)",
    "Tap Update next to one app, or Update All (critical)",
    "Automatic updates: Settings > Apps > App Store > turn App Updates on",
]
REVIEWS.append({
    "id": "tr072-a", "required_actions": RA_72, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(),
    "decision": "keep", "reasons": "", "fix": "",
})
REVIEWS.append(clar("tr072-b"))
REVIEWS.append(clar("tr072-c"))
REVIEWS.append({
    "id": "tr072-d", "required_actions": RA_72, "covered": [True] * 5, "needs_clarification": False,
    "gates": dict(SRC_FAIL),
    "unsupported_claims": ["'Open the App Store from your Home Screen, not from a link in a message' -> not on the cited page (nothing about links in messages)"],
    "scores": s(plain=1),
    "decision": "revise",
    "reasons": "Added safety tip is not on the cited page (the intent is good, but nothing may be added from memory). The lead-in ends with 'then:' and is followed by a second lead-in ('Here's how to update them all at once.'), and 'Open the App Store' is said twice.",
    "fix": "Delete 'Open the App Store from your Home Screen, not from a link in a message, then:' (or support it with a second Apple page). Use one lead-in: 'Thanks. Here's how to update your banking app.' Then step 1 'Open the **App Store**', and in step 4 stress tapping **Update** next to the banking app, with **Update All** as the alternative.",
})

# ---------- tr073: Magnification (Android) support.google.com/accessibility/android/answer/6006949 ----------
RA_73 = [
    "Open Settings > Accessibility > Magnification (critical)",
    "Turn on Magnification shortcut (critical)",
    "Optional: choose the shortcut: Accessibility button, Hold volume keys (press and hold both volume keys), or Triple-tap screen",
    "Start with the shortcut, then tap anywhere on the screen except the keyboard or navigation bar (critical)",
    "Drag with two fingers to move around; pinch with two fingers to change zoom",
    "Use the shortcut again to stop",
    "Zoom goes up to 8x",
]
COV_73 = [True, True, True, False, True, True, True]
UNSUP_73 = ["'**pressing both volume keys**' -> the page's option is 'Hold volume keys' ('Press and hold both volume keys')"]
FIX_73 = ("(1) In the shortcut list say 'pressing and holding both volume keys' (page label: Hold volume keys). "
          "(2) In 'Use it', after 'Start magnification with your shortcut' add a step: 'Tap anywhere on the screen, except the keyboard or the navigation bar.' (the page requires this for full-screen zoom; with Triple-tap the triple-tap itself starts it). "
          "Then keep pinch, two-finger drag, and use the shortcut again to stop.")
REVIEWS.append({
    "id": "tr073-a", "required_actions": RA_73, "covered": COV_73, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_73, "scores": s(steps=1),
    "decision": "revise", "reasons": "Missing the 'tap the screen' step needed to start full-screen zoom; volume-key option misworded.", "fix": FIX_73,
})
REVIEWS.append(clar("tr073-b"))
REVIEWS.append({
    "id": "tr073-c", "required_actions": RA_73, "covered": COV_73, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_73, "scores": s(steps=1),
    "decision": "revise", "reasons": "Missing the 'tap the screen' step needed to start full-screen zoom; volume-key option misworded.", "fix": FIX_73,
})
REVIEWS.append({
    "id": "tr073-d", "required_actions": RA_73, "covered": COV_73, "needs_clarification": False,
    "gates": dict(SRC_FAIL), "unsupported_claims": UNSUP_73, "scores": s(steps=1),
    "decision": "revise", "reasons": "Missing the 'tap the screen' step needed to start full-screen zoom; volume-key option misworded.", "fix": FIX_73,
})

# ---------- tr074: Find a lost iPhone support.apple.com/en-us/101593 ----------
RA_74 = [
    "On another trusted Apple device signed in with the Apple Account, open Find My and go to the Devices tab (critical)",
    "Or on a computer go to icloud.com/find and look under All Devices (critical)",
    "Select the iPhone to locate it (critical)",
    "Use Play Sound to find it nearby",
    "Family Sharing: the iPhone can appear on a family member's device in Find My > Devices",
    "Lost Mode: Find My > Devices > select iPhone > More > scroll to Lost Mode > (optional contact number and message) > Activate; on icloud.com mark as lost; if asked for a verification code select Find Devices",
    "Apple never contacts you to say the iPhone was found; never share passcode, passwords, or codes",
]
COV_74 = [True, True, True, True, True, False, True]
FIX_74_LM = ("Add the Lost Mode steps from the page: 'Open **Find My**, tap **Devices**, select your iPhone, tap **More**, scroll down and turn on **Lost Mode**. You can add a phone number and a message, then tap **Activate**.' "
             "Also say how to play a sound: 'Tap your iPhone and use **Play Sound**.' On a computer: 'If you're asked for a verification code, select **Find Devices** instead.' Keep the scam warning (it is supported). Stay under the 2,200 character cap.")
REVIEWS.append({
    "id": "tr074-a", "required_actions": RA_74, "covered": COV_74, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(steps=1),
    "decision": "revise", "reasons": "Lost Mode (the protective action) is only named, with no steps to turn it on; Play Sound path also not given.", "fix": FIX_74_LM,
})
REVIEWS.append(clar(
    "tr074-b", "revise", ask=1,
    reasons="Two questions (iPhone or Android, and whether another device is available). The second does not change the steps because both device and computer options are given.",
    fix="Keep the empathy line and ask one question only: 'I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?' Update tr074-d's first assistant turn to match."))
REVIEWS.append({
    "id": "tr074-c", "required_actions": RA_74, "covered": COV_74, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(steps=1),
    "decision": "revise", "reasons": "Lost Mode (the protective action) is only named, with no steps to turn it on; Play Sound path also not given.", "fix": FIX_74_LM,
})
REVIEWS.append({
    "id": "tr074-d", "required_actions": RA_74, "covered": COV_74, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(steps=1, constraints=1, plain=1),
    "decision": "revise",
    "reasons": "Lost Mode steps missing. The user said they are on a laptop, yet the reply says 'Good, your laptop will work.' and then repeats 'You'll need another device or a computer.' and still gives the Option 1 steps for another Apple device.",
    "fix": FIX_74_LM + " Because the user is on a laptop, give only the computer steps (icloud.com/find, sign in with the Apple Account, All Devices) and drop Option 1; remove the repeated 'You'll need another device or a computer.' Earlier turn has two questions; change it as in tr074-b.",
})

# ---------- tr075: Find a lost Android phone support.google.com/accounts/answer/6160491 ----------
RA_75 = [
    "On another Android phone/tablet open Find Hub, or on any browser go to google.com/android/find (critical)",
    "Sign in (tap Continue as [name] if the lost phone is the device) (critical)",
    "Select the lost phone from the device list (critical)",
    "If prompted, enter the phone's lock screen PIN (Android 9 and up)",
    "Check the map; tap Find nearby within 10 meters",
    "Play sound: rings at full volume for 5 minutes even on silent",
    "Mark as lost: locks the phone, adds contact info and a message, then tap Mark as lost again to confirm",
    "Factory reset: Settings in Find Hub > Factory reset; deletes all data and the phone no longer appears in Find Hub",
    "Phone must have power, mobile data or Wi-Fi, a signed-in Google Account, and Find Hub on",
]
COV_75 = [True, True, True, False, True, True, False, True, True]
FIX_75 = ("Add the missing actions from the page: after selecting the phone, 'If asked, enter your lock screen PIN or password' (page: the phone's lock screen PIN); under Mark as lost add 'add a message and phone number, then tap **Mark as lost** again to confirm.' "
          "Keep the Play sound / Factory reset text (supported).")
REVIEWS.append({
    "id": "tr075-a", "required_actions": RA_75, "covered": COV_75, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(steps=1),
    "decision": "revise", "reasons": "Missing the PIN prompt and the confirm tap for Mark as lost (the protective action).", "fix": FIX_75,
})
REVIEWS.append(clar(
    "tr075-b", "revise", ask=1,
    reasons="Two questions with two question marks (iPhone or Android, and whether a computer or another phone is available). The second does not change the steps.",
    fix="Ask one question only: 'Let's try to find it. Is it an **iPhone** or an **Android** phone?' Update tr075-d's first assistant turn to match."))
REVIEWS.append(clar(
    "tr075-c", "revise", ask=1,
    reasons="One question mark but two asks (phone type, and whether a computer or another phone is available). The second does not change the steps.",
    fix="Ask one question only: 'I'm sorry, let's try to find it. Is it an **iPhone** or an **Android** phone?'"))
REVIEWS.append({
    "id": "tr075-d", "required_actions": RA_75, "covered": COV_75, "needs_clarification": False,
    "gates": dict(PASS), "unsupported_claims": [], "scores": s(steps=1, constraints=1),
    "decision": "revise",
    "reasons": "Missing the PIN prompt and the confirm tap for Mark as lost. The user will use their husband's phone, whose type is unknown, but the steps cover only an Android phone or a computer.",
    "fix": FIX_75 + " Add: 'If your husband's phone isn't an Android phone, open a web browser on it and go to **google.com/android/find**' (page: without an Android device, use a browser). Earlier turn has two questions; change it as in tr075-b.",
})
