# Reviews for batch fx5, round 1. Independent reviewer.
# Sources fetched with WebFetch on 2026-11-13 (all 13 URLs readable).
# Note: android/answer/9083864 is a generic Quick Settings page and never names the Flashlight tile.

S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}
SRCFAIL = {"source": "fail", "safety": "pass", "duplicate": "pass"}


def sc(**kw):
    d = dict(S2)
    d.update(kw)
    return d


def rec(id, ra, cov=None, gates=PASS, unsup=None, scores=None, decision="keep", reasons="", fix=""):
    return {
        "id": id,
        "required_actions": ra,
        "covered": cov if cov is not None else [True] * len(ra),
        "needs_clarification": False,
        "gates": gates,
        "unsupported_claims": unsup or [],
        "scores": scores or dict(S2),
        "decision": decision,
        "reasons": reasons,
        "fix": fix,
    }


RA_062A = ["Open Settings (critical)", "Storage > Free up space (critical)", "Tap the menu icon, then Settings (critical)", "Turn on Smart Storage (critical)"]
RA_062M = ["Open Settings", "Storage > Free up space (critical)", "Scroll to the category", "Tap Select files; if the category isn't listed, tap Browse (critical)", "Select files or select all", "Tap Move files to Trash (critical)"]
RA_063 = ["Say 'Hey Siri, turn on my flashlight' (critical)", "Say 'Hey Siri, turn off my flashlight' to turn it off"]
RA_063R = ["Home button model: swipe up from the bottom edge to open Control Center; Face ID model: swipe down from upper-right (critical)", "Tap Flashlight button (critical)", "If missing: Settings > Control Center, tap Flashlight in the list of available controls (critical)"]
RA_064 = ["Swipe down once for the first few settings, again for all", "Tap Edit", "Tap and drag the tile to where you want it (critical)", "Dimmed icon means off; tap again to turn off"]
RA_064R = ["Swipe down; swipe down again for all settings", "Tap the icon to turn on; dimmed = off", "If missing: swipe down twice, tap Edit, scroll to the available settings, tap Add (critical)"]
RA_066 = ["Open Clock, tap Alarms tab (critical)", "Tap Add (+) (critical)", "Set the time (critical)", "Tap Done (critical)", "Silent switch, Silent mode and Do Not Disturb do not affect alarm sound", "Volume: Settings > Sounds & Haptics > Ringtone and Alerts slider"]
RA_066R = ["Clock > Alarms > Edit (upper-left) (critical)", "Tap the alarm (critical)", "Tap Sound and choose a sound instead of None (critical)", "Tap Save"]
RA_067 = ["Open Clock, tap Alarm (critical)", "Tap Add (critical)", "Set the time and tap AM or PM (critical)", "Tap OK (critical)", "Tap the alarm block, then tap the days to repeat (critical)"]
RA_067R = ["Alarms too close together can cancel each other; leave at least a 5-minute gap (critical)", "Tap the second alarm's time to edit it, set it to a time 5+ minutes away, tap OK (critical)", "Or tap the alarm block and tap Delete"]
RA_068 = ["Check compatibility with the MFi list", "Update iPhone software", "Bring the hearing aids near the iPhone", "Rechargeable with no switch: remove from charger (critical)", "Settings > Accessibility > Hearing Devices (critical)", "Tap Pair MFi Hearing Device, follow screen steps (critical)", "Select the hearing aids, tap Pair (critical)", "If Pair MFi Hearing Device is not shown, tap the device name under Hearing Devices then Pair"]
RA_068R = ["Confirm compatibility and pairing mode (critical)", "Restart the iPhone (critical)", "If paired to another Apple device, unpair it there first (critical)", "Retry Settings > Accessibility > Hearing Devices"]
RA_069 = ["Pull down quick settings, confirm Bluetooth on (critical)", "Press and hold the Bluetooth tile (critical)", "Under Saved devices, choose the disconnected device (critical)", "Wait until it shows Connected"]
RA_069R = ["If Pair new device is missing, check under Available devices (critical)", "Or open the More menu and choose Refresh (critical)", "Pick the device name (critical)", "If a passcode is asked and you have none, try 0000 or 1234"]
RA_070 = ["Say 'Siri, turn on Low Power Mode' (critical)", "Battery icon turns yellow when on", "'Hey Siri, turn off Low Power Mode' to turn off", "Turns off automatically at 80% or higher"]
RA_070R = ["Low Power Mode turns off automatically when charged to 80% or higher (critical)", "Settings > Battery > Power Mode (iPhone 15 and later) (critical)", "Toggle Low Power Mode on (critical)", "Yellow battery icon"]
RA_071 = ["Settings > Battery > Battery Saver (critical)", "Choose a schedule for Battery Saver, or have it turn off automatically (critical)", "Effects: dark theme, limited background activity"]
RA_071R = ["Restart: hold power button about 30 seconds, tap Restart if shown (critical)", "Settings > System > Software update (critical)", "Play Store: profile icon > Manage apps & devices > update under Updates available (critical)", "Still trouble: carrier or manufacturer support site"]
RA_072 = ["Settings > Apps > App Store (critical)", "Turn off App Updates (critical)", "To update manually: App Store > profile photo/My Account > App Updates > Update / Update All"]
RA_072R = ["Tap the profile photo or My Account button near the top of the App Store (critical)", "Tap App Updates (critical)", "Tap Update or Update All (critical)"]
RA_073 = ["Settings > Accessibility > Magnification (critical)", "Magnification type: choose partial screen (critical)", "Turn on Magnification shortcut (critical)", "Start with the Accessibility button/icon (critical)", "Drag with two fingers to move the window, pinch to zoom", "Some steps need Android 13 or later"]
RA_073R = ["Settings > Accessibility > Magnification > Magnification shortcut (critical)", "Choose Accessibility button or Hold volume keys instead of Triple-tap screen (critical)", "How to start the new shortcut (tap the Accessibility icon, or hold both volume buttons)"]
RA_074 = ["Go to icloud.com/find and sign in (critical)", "Review devices under All Devices, tap the iPhone (critical)", "Play sound, mark as lost, or erase (erase is last resort, cannot be undone)", "If asked for a verification code, select the Find Devices button", "Apple never contacts you to say it was found; do not share codes (safety)"]
RA_074R = ["Use Find My / Lost Mode from a device that supports it (own trusted Apple device, Family Sharing, or icloud.com/find) (critical)", "Devices tab, select iPhone, tap More, scroll to Lost [Device], turn on Lost Mode (critical)", "Optionally add contact information", "Tap Activate (critical)", "Offline: shows online/in Lost Mode only when on and connected to Wi-Fi or cellular"]
RA_075 = ["Open Find Hub on another Android device, or go to google.com/android/find (critical)", "Sign in, select the lost phone (critical)", "Tap Mark as lost, then Next (critical)", "Add contact info and a message", "Tap Mark as lost again to confirm (critical)", "Do not use Factory reset (erases data)"]
RA_075R = ["Tap Play sound: rings at full volume for 5 minutes even if silent (critical)", "If within 10 meters, tap Find nearby; a shape fills in as you get closer (critical)", "Location accuracy: GPS roughly 20 meters, unreliable indoors"]

REVIEWS = [
    rec("tr062-e", RA_062A),
    rec("tr062-r", RA_062M, cov=[True, True, True, True, True, True], unsup=[
        "'That happens when a category is not listed the usual way.' -> the user said they DID find the category; the page only says 'If the category isn't listed, tap Browse', so the explanation does not match the user's report and the page never says where Browse appears"],
        scores=sc(actionable=1), decision="revise",
        reasons="The explanation misdescribes the user's situation and Browse has no stated location/cue.",
        fix="Replace 'That happens when a category is not listed the usual way. Try this instead:' with 'Your phone may show it a little differently. Try this instead:'. Keep the three steps, but change step 1 to 'On the **Free up space** screen, tap **Browse**.' only if you can keep it to what the page says; otherwise write 'Look for **Browse** and tap it.' Add one closing line: 'Menu names can differ a little between phones, and some steps need Android 14 or newer.'"),
    rec("tr063-e", RA_063),
    rec("tr063-r", RA_063R, unsup=[
        "'3. Add **Flashlight**.' -> the page says 'tap Flashlight in the list of available controls'; 'Add' is not a label on the page",
        "User message 'iPhone 11 here, the one with the round button at the bottom' -> the iPhone 11 has no Home button (Face ID), so the stated model contradicts the swipe-up steps"],
        scores=sc(actionable=1, realistic_user=1), decision="revise",
        reasons="User message contradicts itself (iPhone 11 vs round Home button); step 3 uses a label the page does not give.",
        fix="In the user's first message, change 'iPhone 11 here, the one with the round button at the bottom.' to 'iPhone SE here, the one with the round button at the bottom.' (a Home button model) and keep the swipe-up reply. In the final reply replace step 3 'Add **Flashlight**.' with 'In the list of controls, tap **Flashlight**.'"),
    rec("tr064-e", RA_064, unsup=[], reasons="", fix=""),
    rec("tr064-r", RA_064R),
    rec("tr066-e", RA_066),
    rec("tr066-r", RA_066R),
    rec("tr067-e", RA_067),
    rec("tr067-r", RA_067R),
    rec("tr068-e", RA_068, cov=[False, True, False, True, True, True, True, True], scores=sc(steps=1), decision="revise",
        reasons="Page says to bring the hearing devices near the iPhone before pairing; the reply omits it (non-critical).",
        fix="After step 2 ('Take both hearing aids **out of the charger**.') add the sentence 'Keep them close to your iPhone.' inside step 2, or as a new step before opening Settings. Do not add anything else."),
    rec("tr068-r", RA_068R),
    rec("tr069-e", RA_069),
    rec("tr069-r", RA_069R),
    rec("tr070-e", RA_070),
    rec("tr070-r", RA_070R),
    rec("tr071-e", RA_071, gates=SRCFAIL, unsup=[
        "'Yes, Battery Saver has a schedule.' / 'Choose a **Schedule** for when it should run.' -> the page says only 'Choose a schedule for battery saver mode or automatically turn it off'; it does not say you can set evening hours or a timetable, and 'Schedule' is not given as a label"],
        scores=sc(constraints=1), decision="revise",
        reasons="Overpromises an evening timetable and presents 'Schedule' as an on-screen label; the page gives no schedule options.",
        fix="Replace the opening line with 'Yes, Battery Saver lets you choose a schedule, or have it turn off automatically.' Replace step 4 with 'Look for the option to set a schedule or to turn it off automatically, and choose what fits you.' (no bold label). Add the hedge 'The choices can look a little different on some phones.' Keep the last paragraph about dark theme and slower apps."),
    rec("tr071-r", RA_071R),
    rec("tr072-e", RA_072),
    rec("tr072-r", RA_072R),
    rec("tr073-e", RA_073, cov=[True, True, True, True, True, True], unsup=[
        "'pick **Accessibility button** if you are asked how to start it' -> the page says to tap Magnification shortcut to pick a trigger; it never says you are asked",
        "'5. Tap the **Accessibility button**.' -> the page calls it the Accessibility icon at the bottom of the screen (position depends on navigation setup); no cue where it is"],
        scores=sc(actionable=1), decision="revise",
        reasons="Step 4 bundles two actions with an unsupported 'if you are asked'; step 5 gives no cue for where the button is.",
        fix="Split step 4 into: '4. Turn on **Magnification shortcut**.' and '5. Tap **Magnification shortcut** and choose **Accessibility button**.' Then '6. Tap the **Accessibility** icon at the bottom of the screen. Its exact spot depends on how your phone is set up.' Then '7. Drag with two fingers ... pinch ...'. Delete 'if you are asked how to start it'."),
    rec("tr073-r", RA_073R, cov=[True, True, False], scores=sc(actionable=1), decision="revise",
        reasons="After switching shortcuts the reply never says how to start magnification with the new one.",
        fix="After step 3 add a short line: 'With **Accessibility button**, tap the Accessibility icon at the bottom of the screen. With **Hold volume keys**, hold both volume buttons together.' Keep the rest."),
    rec("tr074-e", RA_074),
    rec("tr074-r", RA_074R, cov=[False, True, True, True, True], gates=SRCFAIL, unsup=[
        "'Open the **Find My** app and sign in with your Apple Account.' (on the wife's iPad) -> the page covers only your own signed-in trusted device, Family Sharing members' devices, and icloud.com/find; it does not describe signing in to Find My on someone else's iPad",
        "'scroll to the **Lost** section' -> the page says 'Lost [Device]' (e.g. Lost iPhone)"],
        scores=sc(steps=1), decision="revise",
        reasons="Signing in to the wife's iPad app is unsupported and could mix accounts; icloud.com/find is the page-supported route on someone else's device.",
        fix="Rewrite the first assistant turn to: 'Use the web browser on her iPad.' 1. Go to **icloud.com/find**. 2. Sign in with your Apple Account. 3. Open **All Devices** and tap your iPhone. 4. Choose to **mark it as lost**. (Mention you can also play a sound.) In the final reply, give the same icloud.com/find route for Lost Mode (page gives no button labels, so describe 'mark it as lost' in words) and drop 'scroll to the **Lost** section'. Alternatively, ask first whether her iPad is in your Family Sharing group, then use Find My > Devices > your iPhone > More > scroll to Lost iPhone > Lost Mode > Activate only if yes. Keep the offline explanation."),
    rec("tr075-e", RA_075),
    rec("tr075-r", RA_075R, cov=[True, True, False], unsup=[
        "'The location can be off by a few meters, especially indoors.' -> the page says GPS is accurate to roughly 20 meters and can be unreliable indoors or underground"],
        scores=sc(plain=1), decision="revise",
        reasons="Accuracy figure understated and contradicts the page (roughly 20 meters).",
        fix="Replace the first sentence with 'The location can be off by roughly 20 meters, and it is less reliable indoors.' Keep the three steps."),
]
