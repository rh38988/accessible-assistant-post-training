# Reviewer file for batch ny3a, round 1.
S = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}

def rec(id, acts, cov=None, clar=False, src="pass", unsup=None, sc=None, dec="keep", reasons="", fix=""):
    scores = dict(S)
    if sc:
        scores.update(sc)
    if clar:
        acts, cov = [], []
        scores["steps"] = "NA"
    if cov is None:
        cov = [True] * len(acts)
    return {
        "id": id, "required_actions": acts, "covered": cov, "needs_clarification": clar,
        "gates": {"source": src, "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": unsup or [], "scores": scores,
        "decision": dec, "reasons": reasons, "fix": fix,
    }

FROZEN = ["Hold the power button about 60 seconds to restart when frozen with screen on (critical)", "If it keeps happening: Settings > System > Software update and follow prompts"]
CHARGE = ["Remove the case", "Make sure cable is firmly seated at both ends; clear dust or lint from port", "Try a different cable or adapter; test outlet",
          "Plug in and wait one minute; battery icon means off and charging", "Press and hold Power 5-7 seconds (critical)"]
NET_A = ["Restart the phone", "Settings > Network & internet or Connections: switch between Wi-Fi and mobile data", "Airplane mode on, wait 10 seconds, off", "Restart router: unplug, lights out, wait 30 s, plug in, wait 30 s", "Contact provider if it persists"]
TXT = ["Update Google Messages", "Check SIM inserted properly", "Set Google Messages as default texting app", "Check plan or credit covers texts", "Confirm signal", "Turn off airplane mode", "Confirm carrier supports SMS, MMS, or RCS"]
GRP = ["Open Google Messages", "Tap Start chat, then Create group (critical)", "Choose contacts", "Tap Next", "Write and send"]
SPAM = ["Open Google Messages, touch and hold the conversation (critical)", "Tap Block, then Report spam, then OK (critical)"]
SRC2 = "Add a second source https://support.google.com/messages/answer/16287429 (Create RCS groups), which has the labels Start chat, Create group, Next. The cited page 9367099 does not contain them."

REVIEWS = [
 rec("tr147-a", FROZEN),
 rec("tr147-c", FROZEN),
 rec("tr147-b", [], clar=True),
 rec("tr147-d", FROZEN),
 rec("tr147-e", FROZEN),
 rec("tr147-r", ["Settings > System > Software update, follow prompts", "Check storage in Settings; less than 10% free can cause problems", "Restart after each step"]),
 rec("tr148-a", CHARGE),
 rec("tr148-c", ["Plug into working outlet with firm cable", "Press and hold Power 5-7 s", "A fully drained phone may show nothing for up to 25 minutes (critical)", "After 25 minutes with no response get repair or support"]),
 rec("tr148-b", [], clar=True),
 rec("tr148-d", CHARGE),
 rec("tr148-e", ["Remove the case", "Test cable and adapter on another device", "Seat cable firmly; clear port", "Test outlet with another device", "Plug in and wait one minute; battery icon means off and charging", "Press and hold Power 5-7 s (critical)"],
     cov=[True, True, True, True, False, True],
     sc={"steps": 1, "actionable": 1}, dec="revise",
     reasons="The one-minute wait and the battery-icon cue are replaced by 'Charge for a few minutes', so the user is not told what to look for.",
     fix="Replace step 6 with two steps: 'Plug it in and wait one minute. A battery icon on the screen means the phone is off and charging.' then 'Press and hold the **Power** button for 5 to 7 seconds.' Keep the no-new-cable constraint."),
 rec("tr148-r", ["Press and hold Power about 35 seconds to reboot (critical)", "Wait about 2 minutes", "Call the phone from another phone or use Find Hub", "If it rings but screen blank, contact authorized repair center"]),
 rec("tr149-a", NET_A),
 rec("tr149-c", ["Settings > Network & internet or Connections > Wi-Fi, turn on", "Look at Wi-Fi symbol; if missing or no bars move closer", "Restart router (lights out, 30 s, plug in, 30 s)", "Contact internet provider if it persists"]),
 rec("tr149-b", [], clar=True),
 rec("tr149-d", ["Restart the phone", "Settings > Network & internet or Connections > Mobile data or Cellular data", "Turn on; if on, off and on", "Look for 2G/3G/4G/H beside signal bars", "If none, out of coverage; move or go outside", "Contact provider if it persists"]),
 rec("tr149-e", ["Restart the phone", "Switch Wi-Fi off/mobile data on, then mobile data off/Wi-Fi on, test each (critical)", "Airplane mode on, 10 s, off", "Settings > Wi-Fi turn on; check symbol, move closer if no bars", "Router restart not possible (constraint); ask network host"],
     cov=[True, False, True, True, True],
     sc={"steps": 1, "actionable": 1}, dec="revise",
     reasons="Step 3 turns Wi-Fi off and mobile data on, but the reply never turns Wi-Fi back on before step 5 asks the user to check the Wi-Fi symbol. The user is trying to get online at the sister's house through Wi-Fi, so they would end with Wi-Fi off.",
     fix="In step 3 say: 'Turn Wi-Fi off and mobile data on, and see if things load. Then turn mobile data off and Wi-Fi on, and check again.' In step 5 begin with 'Make sure **Wi-Fi** is on, then look at the Wi-Fi symbol at the top of the screen.' Keep the rest."),
 rec("tr149-r", ["If Wi-Fi symbol missing or no bars filled, may be out of range; move closer to router and try again"]),
 rec("tr150-a", TXT),
 rec("tr150-c", ["Delete the contact and add again", "Check whether you blocked them", "Verify the phone number", "Check country code such as +1 for US numbers"]),
 rec("tr150-b", [], clar=True),
 rec("tr150-d", ["Make sure you have a data connection", "In Settings app reset APN settings to default", "Make sure MMS mass text is off", "Profile picture or Initials (top right) > Messages settings > Advanced > Group messaging, tap Send an MMS reply to all recipients (group MMS)"],
     sc={"actionable": 1, "plain": 1}, dec="revise",
     reasons="Step 2 uses the jargon 'APN settings' with no explanation and no starting point or cue; a low-confidence user cannot act on it. The page itself gives no path, so the reply should say so.",
     fix="Reword step 2 to: 'In your phone's **Settings** app, find the **APN** settings (the settings your phone uses to send picture messages) and choose to reset them to default. The exact menu names are a little different on each phone.' Keep the other steps."),
 rec("tr150-e", TXT, ),
 rec("tr150-r", ["Explain that the message means the carrier does not currently support RCS", "Confirm carrier supports SMS, MMS, or RCS"]),
 rec("tr151-a", GRP, src="fail", unsup=["'Tap **Start chat**, then tap **Create group**' and 'Tap **Next**' -> not on the cited page 9367099 (it only says 'Start a new conversation'); supported by 16287429"],
     dec="revise", reasons="Reply is correct but its key labels are not on the cited page.", fix=SRC2),
 rec("tr151-c", GRP, src="fail", unsup=["'Tap **Start chat**, then tap **Create group**' and 'Tap **Next**' -> not on the cited page 9367099; supported by 16287429"],
     dec="revise", reasons="Labels not on the cited page.", fix=SRC2),
 rec("tr151-b", [], clar=True),
 rec("tr151-d", GRP, src="fail", unsup=["'Tap **Start chat**, then tap **Create group**' and 'Tap **Next**' -> not on the cited page 9367099; supported by 16287429"],
     dec="revise", reasons="Labels not on the cited page.", fix=SRC2),
 rec("tr151-e", ["Profile picture or initials > Messages settings > Advanced > Group messaging", "Choose mass text as default (critical)", "Start chat > Create group, pick members, Next", "Write and send"],
     src="fail", sc={"actionable": 1},
     unsup=["'At the top right, tap your **profile picture** or **initials**' -> 9367099 says only 'Tap your profile photo or icon' (top right is on 9077245)", "'tap **Start chat**, then **Create group** ... tap **Next**' -> not on 9367099; supported by 16287429"],
     dec="revise", reasons="Labels and the top-right position are not on the cited page; step 5 bundles go back, start chat, create group, pick members and Next in one step.",
     fix=SRC2 + " Also add https://support.google.com/messages/answer/9077245 for the 'top right' profile picture position. Split step 5 into separate steps: 'Go back to the main screen.', 'Tap **Start chat**, then **Create group**.', 'Pick your choir members, then tap **Next**.'"),
 rec("tr151-r", ["Profile picture or initials > Messages settings > Advanced > Group messaging", "Tap Send an MMS reply to all recipients (group MMS) (critical)"],
     src="fail", unsup=["'at the top right, tap your **profile picture** or **initials**' -> not on cited 9367099 (it is on 9077245)", "Earlier turn 'Tap **Start chat**, then tap **Create group**' and '**Next**' -> not on 9367099; supported by 16287429"],
     dec="revise", reasons="Top-right position and the earlier-turn labels are not on the cited page.",
     fix=SRC2 + " Also add https://support.google.com/messages/answer/9077245 for the 'top right' profile picture position."),
 rec("tr152-a", SPAM),
 rec("tr152-c", ["Tap More options", "Tap Details", "Tap Block & report spam, then OK (critical)"]),
 rec("tr152-b", [], clar=True),
 rec("tr152-d", SPAM),
 rec("tr152-e", SPAM + ["Explain what is and is not shared with Google and that the spammer cannot see the report"]),
 rec("tr152-r", ["Explain that a Spam reporting conversation may be created and sends a copy of the number and most recent text to the carrier", "It may automatically go to Spam & blocked"]),
 rec("tr153-a", ["Swipe down from top of screen", "Tap Voicemail"]),
 rec("tr153-c", ["Open Phone app", "At the bottom tap Dialpad", "Touch and hold 1"]),
 rec("tr153-b", [], clar=True),
 rec("tr153-d", ["Open Phone app", "More options (top right) > Settings > Voicemail", "Turn on Visual voicemail (critical)", "Tap Voicemail at bottom to listen", "Not every carrier offers it"]),
 rec("tr153-e", ["Notification: swipe down, tap Voicemail", "Or Phone app > Dialpad > touch and hold 1"]),
 rec("tr153-r", ["If Voicemail is not found, call voicemail: Phone app > Dialpad > touch and hold 1", "Visual voicemail not offered by every carrier"]),
]
