G_OK = {"source": "pass", "safety": "pass", "duplicate": "pass"}
S_OK = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}


def R(id, acts, nc=False, scores=None, decision="keep", reasons="", fix="", unsupported=None, cov=None):
    sc = dict(S_OK)
    if scores:
        sc.update(scores)
    if not acts:
        sc["steps"] = "NA"
    return {
        "id": id,
        "required_actions": acts,
        "covered": cov if cov is not None else [True] * len(acts),
        "needs_clarification": nc,
        "gates": dict(G_OK),
        "unsupported_claims": unsupported or [],
        "scores": sc,
        "decision": decision,
        "reasons": reasons,
        "fix": fix,
    }


SHOT = ["Press Power/Side and Volume Down together, then release (critical)", "Screen flashes to confirm the capture"]
SHOT_FIND = ["Open Gallery, tap Albums tab, then Screenshots folder (critical)", "Or open My Files, tap Images"]
UPD = ["Swipe down with two fingers from top-right corner, tap Settings icon (critical)", "Tap Software update or System updates (critical)", "Tap Download and install / Check for system updates / Check for software updates; Download now on some devices (critical)", "When download finishes, follow the on-screen prompts to install (critical)"]
WIFI = ["Open Settings, tap Connections (critical)", "Tap Wi-Fi (critical)", "If Wi-Fi is off, tap the toggle to turn it on", "Tap the network name (critical)", "Enter the password and tap Connect (critical)", "Success cue: name under Current network with Connected below it"]
BLK_RECENT = ["Phone app, Recents tab, select the number (critical)", "Tap the menu icon (three lines with three dots), then Block (critical)", "Confirm with Block (critical)"]
FLASH = ["Swipe down from top right to open Quick settings panel (critical)", "Tap the Flashlight icon to turn on (critical)", "Tap the Flashlight icon again to turn off"]
EASY = ["Open Settings app (critical)", "Go to Display (critical)", "Tap Easy Mode (critical)", "Use the switch to turn it on (or off) (critical)"]
LOST = ["In a web browser open SmartThings Find or Samsung Find website and sign in with Samsung account (critical)", "Find the device in the list on the left (critical)", "Select the device to see its position on the map (critical)", "Phone must be on and have a network connection; otherwise only last known location"]

REVIEWS = [
    R("tr160-a", SHOT),
    R("tr160-c", ["Take a standard screenshot first (Power/Side + Volume Down, release) (critical)", "Tap the Scroll capture icon (two downward arrows) (critical)"]),
    R("tr160-b", [], nc=True),
    R("tr160-d", SHOT),
    R("tr160-e", ["Swipe down from top right with two fingers to open Quick panel (critical)", "Tap the gear icon, Settings (critical)", "Go to Advanced features (critical)", "Tap the Palm swipe to capture switch (critical)", "Swipe edge of hand across screen to capture (critical)", "Optional: voice commands Hey Bixby/Hey Google, take a screenshot"]),
    R("tr160-r", SHOT_FIND),
    R("tr161-a", UPD, scores={"plain": 1}, decision="revise",
      reasons="Closing line repeats what step 3 already says, so the reply says the same thing twice; this is extra text a learner would copy.",
      fix="Delete the last line 'If the name is different on your phone, look for **System updates** instead.' Step 3 already says 'On some phones it is called **System updates**.' Change nothing else."),
    R("tr161-c", ["Have Smart Switch installed on the computer (page: 'a computer that has Smart Switch installed'; page links samsung.com/us/support/owners/app/smart-switch) (critical)", "Connect the Galaxy with the USB cable from the box (adapter for some PCs) (critical)", "Open Smart Switch and let it detect the device (critical)", "If an update is available select Update and follow the prompts (critical)", "Keep cable connected, do not use the device until finished; it restarts"], cov=[False, True, True, True, True],
      scores={"steps": 1}, decision="revise",
      reasons="Reply never says Smart Switch must already be installed on the laptop. This user only uses the laptop for email, so step 2 'Open Smart Switch' would not work for them and they are not told what to do.",
      fix="Add a first step before plugging in: 'Make sure the Smart Switch program is installed on your computer. If it is not, you can get it from Samsung's Smart Switch page: https://www.samsung.com/us/support/owners/app/smart-switch'. Then keep the existing steps 1-3 (renumbered) and the closing note. Keep it short."),
    R("tr161-b", [], nc=True),
    R("tr161-d", UPD),
    R("tr161-e", ["Settings, Software update or System updates (critical)", "Tap Last update, then All changes (critical)", "Update on the phone: Download and install (or Download now) (critical)", "Follow on-screen prompts after download", "Phone cannot be used during update, including emergency calls"]),
    R("tr161-r", ["In Settings look for System updates in place of Software update (critical)", "Tap Download and install, Check for system updates, or Check for software updates depending on carrier (critical)", "Tap Download now if shown"]),
    R("tr162-a", WIFI),
    R("tr162-c", WIFI),
    R("tr162-b", [], nc=True),
    R("tr162-d", WIFI),
    R("tr162-e", ["Password is usually on a sticker on the router", *WIFI[:5], WIFI[5]]),
    R("tr162-r", ["Tap the network name again, tap the eye icon next to password to see it (critical)", "Fix typos and tap Connect (critical)", "If still failing, Settings > Connections, turn the Wi-Fi switch off, wait, turn on"]),
    R("tr163-a", BLK_RECENT),
    R("tr163-c", ["Open Contacts and tap the contact (critical)", "Tap More, then Block contact (critical)", "Confirm with Block (critical)"]),
    R("tr163-b", [], nc=True),
    R("tr163-d", BLK_RECENT),
    R("tr163-e", ["Open Samsung Messages and select the conversation (critical)", "Press and hold the conversation, tap More, then Block (critical)", "Confirm with Block (critical)"]),
    R("tr163-r", ["Phone app, More options (three dots), Settings (critical)", "Tap Block numbers (critical)", "Type the number and tap Add (plus sign) (critical)"]),
    R("tr164-a", FLASH, scores={"actionable": 2}, decision="revise",
      reasons="One cue is not on the cited page.",
      fix="Delete the last line 'The icon looks highlighted while the light is on.' The page does not describe how the icon looks when on. Keep 'The light comes on.' in step 2 as the cue.",
      unsupported=["'The icon looks highlighted while the light is on.' -> the page does not describe the icon's appearance when on"]),
    R("tr164-c", ["Swipe down from top right to open Quick settings panel (critical)", "Tap and hold the Flashlight icon (critical)", "Tap the switch to turn the light on (critical)", "Adjust the slider for brightness (critical)", "Slider is grayed out until the flashlight is turned on"]),
    R("tr164-b", [], nc=True),
    R("tr164-d", FLASH),
    R("tr164-e", FLASH),
    R("tr164-r", ["Swipe left in the Quick settings panel to find the Flashlight icon (critical)", "Tap the Flashlight icon"]),
    R("tr165-a", EASY),
    R("tr165-c", EASY),
    R("tr165-b", [], nc=True),
    R("tr165-d", EASY),
    R("tr165-e", ["Open Settings app (critical)", "Go to Display (critical)", "Tap Easy Mode (critical)", "Turn the switch off (critical)"]),
    R("tr165-r", ["Restart the device and try again (critical)", "Re-check Settings, Display, Easy Mode switch is on", "Causes: outdated software, glitch, low storage"]),
    R("tr166-a", LOST),
    R("tr166-c", ["Open SmartThings Find or Samsung Find website, sign in (critical)", "Select the device (critical)", "Select Ring, then Start (critical)", "Rings one minute even on silent or vibrate", "Stop with Stop on website or Dismiss on phone"]),
    R("tr166-b", [], nc=True),
    R("tr166-d", LOST),
    R("tr166-e", ["Press the watch Home button, swipe to and tap Samsung Find (critical)", "Tap Continue and allow the permissions (critical)", "Select the phone (critical)", "Tap the Ring icon (critical)", "Stop with Dismiss on phone or Stop on watch", "Watch must be connected by Bluetooth, or Wi-Fi/LTE", "If watch cannot locate it, use the website"],
      cov=[True, False, True, True, False, True, True], scores={"steps": 1}, decision="revise",
      reasons="Page's watch procedure has a Continue/allow permissions step that is missing, and the reply never says how to stop the ringing, which matters for someone who finds the phone by sound.",
      fix="After 'Open **Samsung Find**' (say 'swipe to and tap **Samsung Find**'), add a step: 'If asked, tap **Continue** and allow the permissions.' After the Ring step add: 'To stop the ringing, swipe **Dismiss** on the phone, or tap **Stop** on the watch.' Keep the closing note about Bluetooth, Wi-Fi or LTE and the website fallback."),
    R("tr166-r", ["Understand the map shows only last known location when phone is off (critical)", "Go to the last known spot and look", "If still missing contact the carrier to locate or suspend", "If stolen, do not go to the location; inform the authorities (critical)"]),
]

for _r in REVIEWS:
    if _r["id"] == "tr164-a":
        _r["gates"]["source"] = "fail"
