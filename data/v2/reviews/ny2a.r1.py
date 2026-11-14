# Reviewer file for batch ny2a, round 1.
S = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}

def rec(id, acts, cov=None, clar=False, src="pass", unsup=None, sc=None, dec="keep", reasons="", fix="", gates=None):
    scores = dict(S)
    if sc:
        scores.update(sc)
    if clar:
        acts, cov = [], []
        scores["steps"] = "NA"
    if cov is None:
        cov = [True] * len(acts)
    g = {"source": src, "safety": "pass", "duplicate": "pass"}
    if gates:
        g.update(gates)
    return {
        "id": id, "required_actions": acts, "covered": cov, "needs_clarification": clar,
        "gates": g, "unsupported_claims": unsup or [], "scores": scores,
        "decision": dec, "reasons": reasons, "fix": fix,
    }

UPDATE_URL = "https://support.apple.com/en-us/118575"
MAIL_RECV = ["Make sure the iPhone is connected to the internet", "Check the provider's status page or contact provider about an outage",
             "Sign in to the provider's website to check email address and password", "Settings > Apps > Mail > Mail Accounts > Fetch New Data, choose a setting (critical for not receiving)",
             "Ask provider about two-step verification or other security, may need special password"]
TXT_FAIL = ["Check network connection", "Tap red exclamation point, tap Try Again (critical)", "If still fails, tap red exclamation point again, tap Send as Text Message (rates may apply)",
            "Restart iPhone", "Confirm correct phone number or email for the contact", "Contact carrier if SMS/MMS still fails"]
NOSVC = ["Settings: turn on Airplane Mode at least 15 seconds, then off (critical)", "Restart iPhone (critical)", "Contact carrier: account active, coverage/outage, device not blocked, correct data plan (critical)",
         "Update to the latest iOS"]
SENS = ["Restart iPhone", "Clean screen, free of debris or water", "Unplug accessories from charging port; if screen works, try different outlet, cable, charger", "Remove case and screen protector", "If still failing, set up service with Apple"]
HOT = ["Turn off the iPhone (critical)", "Move it somewhere cooler, away from direct sunlight (critical)", "Let it cool down before using it again (critical)"]
TIME_AUTO = ["Connect to internet", "Install latest software updates", "Settings > General > Date & Time > turn on Set Time Automatically (critical)",
             "If message says updated time zone info available, restart iPhone", "Settings > Privacy & Security > Location Services > System Services > Setting Time Zone on"]
TIME_MAN = ["Settings > General > Date & Time (critical)", "Turn off Set Automatically (critical)", "Tap Time Zone and enter a city, or tap the date to change date and time (critical)"]

PROT = "Add a one-line addition only; keep everything else."
R = []

R.append(rec("tr134-a", MAIL_RECV + ["Account removal is a last resort: confirm all mail is on provider website first, then Settings > Apps > Mail > Mail Accounts > tap account > Delete Account, add again"],
  cov=[True, True, True, False, True, True], sc={"steps": 1, "actionable": 1, "plain": 1}, dec="revise",
  reasons="Fetch New Data (Settings > Apps > Mail > Mail Accounts > Fetch New Data) is missing. The single 'stop when your email works' list of 9 steps mixes checks with a destructive account removal; step 5 is a worry rather than an action, and Delete Account is presented as just another step in the middle of a flat list. Page warns downloaded emails might be removed. Too long and risky for a low-confidence user.",
  fix="Rewrite as two short groups. Group 1 (try first, stop when it works): internet; provider status page or contact provider; sign in to provider website to check address and password; ask provider about two-step verification / special password; Settings > Apps > Mail > Mail Accounts > Fetch New Data, choose Automatically or Manually or a schedule. Group 2, clearly labeled 'last resort, only if nothing above works': warn that removing the account can delete emails already saved on the phone, so first sign in to the provider website on a computer and confirm all email is there or saved elsewhere; then Settings > Apps > Mail > Mail Accounts > tap the account > Delete Account; then add the account again. Keep 'If that does not help, contact your email provider.'"))

R.append(rec("tr134-c", ["Outbox instructions (not on the page)"], cov=[False], src="fail",
  unsup=["'an email that did not go out waits in the Outbox' -> page has no Outbox content",
         "'Open Mail and go to your list of mailboxes. Tap Outbox... If there is no Outbox, your email was sent.' -> not on page; the last claim is also a guess about sent status",
         "'Check that your daughter's address is correct. Tap Send.' -> not on page"],
  sc={"steps": 0}, dec="reject",
  reasons="Entire answer is from memory. The cited page (support.apple.com/en-us/102578) has no Outbox steps. The user question (where is the unsent note) cannot be answered from this source.",
  fix="Reject. If a replacement is wanted, write a different direct_messy scenario that the page does support (for example, mail will not send or get new email, user names the error about a wrong password; answer: sign in to provider website, contact provider, ask about two-step verification)."))

R.append(rec("tr134-b", [], clar=True))

R.append(rec("tr134-d", MAIL_RECV, cov=[True, True, False, True, False], sc={"steps": 1, "actionable": 1}, dec="revise",
  reasons="For mail not coming in, the page also says to sign in to the provider website to check address and password; this is missing. Step 6 'Choose a setting such as Automatically or Manually, or pick a schedule' gives no clear choice for a user whose mail is not arriving. The closing note about charging and Wi-Fi is supported (iOS 11 and later) and useful.",
  fix="Add a step after the outage check: 'In a web browser, sign in to your provider's website to confirm your email address and password.' Change the last step to name one concrete choice, e.g. 'Tap **Automatically** (or **Manually**, or pick a schedule)' and tell the user what they will see: the chosen option is shown with a check. If you cannot support the check mark, only say 'tap the one you want'. Keep the Automatically note."))

R.append(rec("tr134-e", MAIL_RECV, cov=[True, True, True, False, True], sc={"steps": 1}, dec="revise",
  reasons="Reply keeps the constraint (no account deletion) and is supported, but omits Settings > Apps > Mail > Mail Accounts > Fetch New Data, a check the user can do themselves without deleting anything and that bears on 'gets nothing new'.",
  fix="Add after step 2: 'Open **Settings**, then tap **Apps**. Tap **Mail**, then **Mail Accounts**, then **Fetch New Data**. Choose **Automatically**, **Manually**, or a schedule.' Renumber. Keep the closing note about deletion."))

R.append(rec("tr134-r", ["Contact provider or system administrator about the username/password error (critical)", "Ask about two-step verification or other security; may need special password", "Confirm account settings"]))

R.append(rec("tr135-a", TXT_FAIL[:3] + ["Contact carrier if still failing"]))

R.append(rec("tr135-c", ["Make sure there is enough storage to receive pictures and videos", "Settings > Apps > Messages", "Turn on Send Photo Previews or Low Quality Image Mode", "Ask carrier whether it supports MMS (attachment size limits)"],
  cov=[True, True, True, False], sc={"steps": 1, "actionable": 1}, dec="revise",
  reasons="'Make sure your iPhone has enough storage' gives no way to do it and no starting point (the page gives none either). The user also says received pictures do not show up, and the page's carrier check (ask the carrier whether it supports MMS) is missing. 'Turn on Send Photo Previews or Low Quality Image Mode' leaves the user to guess which one.",
  fix="Keep steps 2 and 3. Reword step 4 to 'Look for **Send Photo Previews** or **Low Quality Image Mode** and turn on whichever one you see.' Change step 1 into a plain sentence in the lead-in ('Pictures need free space on the iPhone, so delete things you no longer need if it is full') only if you can support it; otherwise keep it as 'Make sure your iPhone has enough storage to receive pictures and videos.' Add a last line: 'If pictures still will not go through, ask your carrier whether it supports MMS (picture messages) for your plan.'"))

R.append(rec("tr135-b", [], clar=True))

R.append(rec("tr135-d", ["Settings > Apps > Messages > Send & Receive (critical)", "Choose the phone number or email address to use", "If the number does not appear, link iPhone number to Apple Account or set up Text Message Forwarding"]))

R.append(rec("tr135-e", ["Check network connection", "Tap red exclamation point, then Try Again (critical)", "Avoid Send as Text Message since rates may apply (constraint)", "Restart iPhone", "Confirm correct number/email for the contact"],
  cov=[True, True, True, False, False],
  unsup=["'the only other choice is Send as Text Message' -> page also lists restarting the iPhone and confirming the contact's phone number or email; contacting the carrier is for SMS/MMS, and Apple Support is the page's contact for iMessage"],
  sc={"steps": 1}, dec="revise",
  reasons="'The only other choice' is wrong per the page; restart and correct-contact-number checks (no charge) are omitted, which matter for this user. 'Contact your carrier' for an iMessage failure: page says contact Apple Support for iMessage and carrier for SMS/MMS.",
  fix="Replace the closing paragraph: add two steps after Try Again, 'Restart your iPhone.' and 'Check that your neighbor's phone number or email address is correct in the contact.' Then say 'If it still will not send, **Send as Text Message** is another option, but messaging rates may apply. If you do not want that, contact Apple Support for blue-bubble (iMessage) problems.' Remove 'the only other choice' and 'contact your carrier'."))

R.append(rec("tr135-r", ["Restart iPhone", "Confirm correct number/email for the contact", "Check Wi-Fi or cellular data", "Contact carrier if SMS still fails"]))

R.append(rec("tr136-a", NOSVC + ["Contact carrier checks"], cov=[True, True, True, True, True], sc={"actionable": 1}, dec="revise",
  reasons="Step 6 'Update your iPhone to the latest iOS' has no starting point, and the step list puts the update after a phone call to the carrier. Page order: Airplane Mode, restart, contact carrier, update iOS, so order is fine, but a low-confidence user needs the path.",
  fix="Expand step 6 using the second official page https://support.apple.com/en-us/118575 : 'Plug in your iPhone and connect to Wi-Fi. Open **Settings**, tap **General**, tap **Software Update**. If an update is available, tap **Download and Install** and follow the instructions on the screen.' Keep the rest. Optionally also add the page's carrier settings step (connect to Wi-Fi, Settings > General > About, update carrier settings if offered)."))

R.append(rec("tr136-c", ["Settings > Cellular (or Cellular Data)", "Turn on Cellular Data", "Tap Cellular Data Options", "Turn on Data Roaming (critical)", "If still no service: Airplane Mode, restart, carrier"]))

R.append(rec("tr136-b", [], clar=True))

R.append(rec("tr136-d", NOSVC, cov=[True, True, True, False], sc={"steps": 1}, dec="revise",
  reasons="The SOS explanation and the emergency-call countries are supported. Missing the page's 'Update iOS to the latest version' action; also no mention that the first three steps go in this order and what to do if still SOS.",
  fix="Add a step 5: 'If it still says SOS, update your iPhone: plug it in and connect to Wi-Fi, open **Settings**, tap **General**, tap **Software Update**, and if an update is shown tap **Download and Install**.' Add https://support.apple.com/en-us/118575 as a second source for this step."))

R.append(rec("tr136-e", ["Airplane Mode 15 seconds then off (no restart per constraint)", "Contact carrier checks", "Update iOS", "Check carrier settings update: Wi-Fi, Settings > General > About"],
  cov=[True, True, False, True], sc={"steps": 1, "constraints": 1}, dec="revise",
  reasons="Update iOS is omitted (the user's 'download' may be that update). Turning on Airplane Mode can interrupt the Wi-Fi download the user is waiting on, and the reply does not warn about that or put the Wi-Fi-based carrier settings check first. Step 4 does not tell the user what they see if no update appears.",
  fix="Put the Wi-Fi step first: connect to Wi-Fi, Settings > General > About, if an update is offered tap to update carrier settings. Then Airplane Mode (add: 'this may pause your download, so you may prefer to do it after the download finishes'). Then carrier. Add the iOS update step with the Settings > General > Software Update > Download and Install path from https://support.apple.com/en-us/118575 as second source. Add 'If no update shows, nothing more to do here' for step 4."))

R.append(rec("tr136-r", ["Contact carrier checks (critical)", "Update iOS", "Check carrier settings update (Wi-Fi, General > About)", "If carrier confirms all fine and hardware is suspected, get service from Apple"],
  cov=[True, True, False, False],
  unsup=["'If you still see No Service after that, contact your carrier again.' -> page sends the user to Apple service when the carrier confirms account and network are fine and a hardware problem is suspected"],
  sc={"steps": 1, "actionable": 1}, dec="revise",
  reasons="'Update your iPhone to the latest iOS' has no path; carrier settings update is missing; last step loops back to the carrier instead of the page's hardware/service step.",
  fix="Step 2: add path 'Plug in and connect to Wi-Fi, open Settings > General > Software Update, tap Download and Install' (second source https://support.apple.com/en-us/118575). Add a step for carrier settings (Wi-Fi, Settings > General > About, update if offered). Replace step 3 with 'If your carrier says your account and network are fine and you think the phone itself has a problem, get service from Apple.'"))

R.append(rec("tr137-a", SENS))
R.append(rec("tr137-c", SENS))
R.append(rec("tr137-b", [], clar=True))
R.append(rec("tr137-d", SENS))
R.append(rec("tr137-e", SENS[:3] + ["Remove case/screen protector only if needed (constraint)", "Service with Apple"]))
R.append(rec("tr137-r", ["Try a different outlet", "Try a different cable", "Try a different charger", "If still failing, set up service with Apple"]))

R.append(rec("tr138-a", HOT + ["Emergency calls may still work"]))
R.append(rec("tr138-c", HOT + ["Avoid long GPS navigation in sun/heat; do not leave phone in a hot car"]))
R.append(rec("tr138-b", [], clar=True))
R.append(rec("tr138-d", ["Know that setup, restore, update, wireless charging, camera, video streaming make it warm and it cools afterwards", "No warning means it can keep being used", "If a warning appears: turn off, cooler place, let cool"]))

R.append(rec("tr138-e", ["Move to a cooler place away from direct sunlight (critical)", "Let it cool before use (critical)", "Turn off the iPhone (page step; user declines)"],
  cov=[True, True, False],
  unsup=["'An iPhone showing the warning screen might still be able to make emergency calls.' -> page-supported, but irrelevant to an incoming hospital call and may mislead the user into thinking the phone can still receive it"],
  sc={"plain": 1, "actionable": 1}, dec="revise",
  reasons="The honest opening is good. But 'Let it cool down before you use it again' collides with the user waiting for a call, and the emergency-calls sentence answers a different question (making, not receiving, calls).",
  fix="Keep the opening and step 1. Replace step 2 and the last paragraph with: 'While the warning is showing, Apple says to let the iPhone cool down before using it, so I cannot promise it will work for your call. If the call is important, it may be safer to turn it off and let it cool, or ask the hospital for another number to call.' Remove the emergency-calls sentence (or say plainly it is about making emergency calls only)."))

R.append(rec("tr138-r", ["Move to a cooler place away from direct sunlight", "Wait for normal temperature; Charging On Hold resumes automatically"]))

R.append(rec("tr139-a", TIME_AUTO, cov=[True, False, True, False, True], sc={"steps": 1}, dec="revise",
  reasons="Page lists installing the latest software updates before turning on Set Time Automatically, and restarting if a message says updated time zone information is available; both are missing.",
  fix="Add after step 1: 'Install the latest iPhone update if one is waiting (Settings > General > Software Update > Download and Install; second source https://support.apple.com/en-us/118575).' Add after the Set Time Automatically step: 'If a message says updated time zone information is available, restart your iPhone.'"))

R.append(rec("tr139-c", TIME_MAN))
R.append(rec("tr139-b", [], clar=True))

R.append(rec("tr139-d", TIME_AUTO, cov=[True, False, True, True, False], sc={"steps": 1}, dec="revise",
  reasons="Missing the page's step to install the latest software updates; the user's problem is both date and time wrong, and the Setting Time Zone location step is also omitted (non-critical).",
  fix="Add after step 1: 'Install the latest iPhone update if one is waiting (Settings > General > Software Update > Download and Install; second source https://support.apple.com/en-us/118575).' Optionally add the Privacy & Security > Location Services > System Services > Setting Time Zone step."))

R.append(rec("tr139-e", TIME_MAN))

R.append(rec("tr139-r", ["Explain why the switch is dimmed: Screen Time passcode, work profile with restrictions, carrier or country/region", "Give a next action for each reason"],
  cov=[True, False], sc={"steps": 1, "actionable": 1}, dec="revise",
  reasons="Reasons are supported, but the reply ends with no action: the user is left with a list of causes and no next step.",
  fix="After each reason add a short action the page supports in spirit: Screen Time passcode, ask the person who set it up (or enter the Screen Time passcode if you know it); work profile, ask your workplace's IT help; carrier/country, you cannot turn it on, set the time by hand instead (Settings > General > Date & Time, if the Set Automatically switch is not locked, turn it off, then Time Zone or tap the date). Keep it short and do not add steps the page does not give."))

R.append(rec("tr140-a", ["Open Settings", "Tap Display & Brightness", "Drag the slider right for brighter (left for dimmer)"]))
R.append(rec("tr140-c", ["iPhone 8 or earlier: swipe up from bottom edge", "Drag brightness bar down for dimmer"]))
R.append(rec("tr140-b", [], clar=True))
R.append(rec("tr140-d", ["iPhone X or later: swipe down from top-right corner; iPhone 8 or earlier: swipe up from bottom edge", "Drag brightness bar up for brighter"]))
R.append(rec("tr140-e", ["Settings > Accessibility > Display & Text Size > Auto-Brightness off", "Settings > Display & Brightness, drag slider"]))
R.append(rec("tr140-r", ["If warm, display dims and top brightness lowered until it cools", "Auto-Brightness off then on: Settings > Accessibility > Display & Text Size > Auto-Brightness"]))

REVIEWS = R
