# Reviews for batch ex7, round 1

def _s(steps=2, ask=2, con=2, act=2, plain=2, real=2):
    return {"steps": steps, "ask_or_answer": ask, "constraints": con,
            "actionable": act, "plain": plain, "realistic_user": real}

def _g(source="pass", safety="pass", duplicate="pass"):
    return {"source": source, "safety": safety, "duplicate": duplicate}

def _rec(id, ra, cov, nc, gates, unsup, scores, decision, reasons="", fix=""):
    return {"id": id, "required_actions": ra, "covered": cov, "needs_clarification": nc,
            "gates": gates, "unsupported_claims": unsup, "scores": scores,
            "decision": decision, "reasons": reasons, "fix": fix}

def _ask(id, nc, scores, decision, reasons="", fix="", gates=None):
    return _rec(id, [], [], nc, gates or _g(), [], scores, decision, reasons, fix)

def _all(ra):
    return [True] * len(ra)

NASK = dict(steps="NA")

# ---------------- tr089 FTC government impersonation ----------------
RA089 = ["Hang up and do not pay, no gift cards (critical)",
         "Do not give personal or bank information (critical)",
         "Do not trust caller ID",
         "To check, contact SSA yourself at a number you know is correct, from its official website",
         "Report to the FTC at ReportFraud.ftc.gov",
         "Report to the Social Security Office of the Inspector General",
         "If personal information was shared, go to IdentityTheft.gov"]
FIX089_BEN = ('Delete the sentence "Your benefits are not being cut off." The FTC page does not say it. '
              'Keep only what the page says: the real Social Security Administration will not threaten you, will not suspend your Social Security number, and will not ask you to pay with gift cards.')

# ---------------- tr090 FTC passwords ----------------
RA090 = ["Make the password long, at least 12 characters",
         "Use a passphrase made of random words",
         "Avoid common phrases, song lyrics, movie quotes",
         "If you reused the same or a similar password on other services, change it there too",
         "Use a password manager or the browser to create and save passwords",
         "Turn on two-factor authentication",
         "Protect your email account with a strong password (reset links go to email)"]
UNSUP090 = [
    '"Use a different password for each account, so if one is stolen, the others stay safe." -> page has no standalone rule; it only says "If you reused the same password, or a similar one, on other services, change it there, too."',
    '"many web browsers have one built in" -> page says a web browser or mobile browser can create and save passwords; it does not say browsers have a built-in password manager.',
    '"Turn on two-step verification" -> page says "two-factor authentication" (and multi-factor); a different label.',
    '"easier to remember than a jumble of symbols" -> page only says "You may find it easier to use a passphrase"; no comparison with symbols.']
FIX090 = ('Rewrite the tips to match the FTC page: (1) keep "at least 12 characters" and the random-words passphrase, but say a passphrase "may be easier to remember" with no comparison to symbols; '
          '(2) replace the "different password for each account" item with "If you used the same or a similar password on other sites, change it there too"; '
          '(3) replace "many web browsers have one built in" with "A password manager, or your web browser, can create strong passwords and save them for you"; '
          '(4) say "two-factor authentication" instead of "two-step verification" and add what it does: a hacker who steals your password still cannot log in without another step. '
          'Keep the song lyrics/quotes tip (add movie quotes) and the email tip.')

# ---------------- tr091 Google Maps ----------------
RA091 = ["Open the Google Maps app",
         "Search for the destination",
         "Tap Directions at the bottom left (critical)",
         "Pick a travel mode",
         "Choose a route; best route is blue, others gray",
         "Optional: swipe up on the route panel for the list of steps, or tap Preview for a turn-by-turn preview"]
COV091 = [True, True, True, True, True, False]
UNSUP091 = [
    '"If you\'re starting from where you are now, Maps can give turn-by-turn directions as you go." -> not on the page. The page says your location is the default start, and Preview shows a turn-by-turn preview.',
    '"To see the list of turns before you leave, tap Preview." -> page: the directions list comes from swiping up on the route info panel; Preview is the turn-by-turn preview.']
FIX091 = ('Replace the last paragraph with only page-supported text: "To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap Preview." Delete the sentence about turn-by-turn directions "as you go". Keep steps 1 to 6 unchanged.')

# ---------------- tr093 Zoom ----------------
RA093 = ["Click the invite link in the email (or paste it into a browser) (critical)",
         "In the browser pop-up asking to open Zoom Meetings, click Open (may read Allow or Open zoom.us depending on browser) (critical)",
         "The Zoom app opens and takes you into the meeting",
         "If the link has the passcode embedded, no separate passcode is needed"]
UNSUP093 = [
    '"give yourself 5 to 10 minutes before the meeting starts" -> the page gives no early-join time.',
    '"it may say Open Zoom Meetings, Allow, or Open zoom.us" -> page: the button is "Open" and may read "Allow" or "Open zoom.us" depending on browser and device; "open Zoom Meetings" is the pop-up question, not a button label.',
    '"Your web browser will open a page asking if you want to open Zoom Meetings" -> page: the browser goes to a launch page where a pop-up asks whether to open Zoom Meetings.']
FIX093 = ('Delete "The first time, give yourself 5 to 10 minutes before the meeting starts." In step 2 say a small box (pop-up) asks whether to open Zoom Meetings. '
          'In step 3 say: click **Open**; depending on your browser the button may read **Allow** or **Open zoom.us**. Keep the passcode sentence and the "tell me what you see" line.')

# ---------------- tr095 iCloud backup ----------------
RA095 = ["Connect the iPhone to Wi-Fi",
         "Settings, tap your name, tap iCloud",
         "Tap iCloud Backup",
         "Confirm Back Up This iPhone is on",
         "Tap Back Up Now (critical)",
         "Keep the Wi-Fi connection until it finishes (critical)",
         "Check date and time of last backup under Back Up Now",
         "If an iCloud storage alert appears, follow the onscreen steps to buy more"]
UNSUP095 = ['"tap **your name** at the top" -> the page says only to tap your name; "at the top" is a position claim not on the page.']
FIX095 = 'In step 2 write "Open **Settings** and tap **your name**." (remove "at the top"). Everything else matches the Apple page.'

# ---------------- tr096 Stolen Device Protection ----------------
RA096 = ["Open Settings",
         "Tap Face ID & Passcode (or Touch ID & Passcode)",
         "Enter your passcode",
         "Tap Stolen Device Protection and turn it on (critical)",
         "Requirements: two-factor authentication, passcode, Face ID or Touch ID, Significant Locations on, Find My on, iOS 17.3 or later",
         "It may already be on by default"]
COV096 = [True, True, True, True, False, True]
FIX096 = 'In the last paragraph add the missing requirement from the Apple page: **iOS 17.3 or later** (for example "an iPhone updated to iOS 17.3 or later"). Keep the rest.'

# ---------------- tr097 Live Caption ----------------
RA097 = ["Press a volume button, tap More under the volume controls, tap Live Caption, then Done",
         "Or open Settings, Accessibility, Live Caption and turn it on",
         "Connect to Wi-Fi the first time so the language pack can download",
         "If it is missing, search for Live Caption in Settings"]

# ---------------- tr098 Windows text size ----------------
RA098 = ["Open Settings, Accessibility (Start then Settings, or Windows logo key + U)",
         "Select Text size (critical)",
         "Drag the Text size slider to the right",
         "Select Apply (critical)",
         "For images and apps bigger use Scale under Display"]

# ---------------- tr099 iPhone 80% ----------------
RA099 = ["Explain Optimized Battery Charging holds the charge at 80% during long charges",
         "Heat can limit charging above 80%; move to a cooler spot",
         "iPhone 15 and later: a charge limit can be changed to charge past 80%"]

# ---------------- tr101 Silent mode ----------------
RA101 = ["Check the Ring/Silent switch; orange means Silent mode is on (critical)",
         "Move the switch so orange no longer shows (critical)",
         "On Action button models, the Action button turns Silent mode on or off by default; it can be set to do something else",
         "Volume buttons adjust ringer volume"]

# ---------------- tr102 Select to Speak ----------------
RA102 = ["Open Settings, Accessibility, Select to Speak",
         "Turn on the Select to Speak shortcut (critical)",
         "If missing, update Android Accessibility Suite from Google Play",
         "Start it with a two-finger swipe up (three-finger if TalkBack is on) or the Accessibility button",
         "Tap an item to hear it",
         "Tap Play to hear everything"]
COV102 = [True, True, True, True, True, True]
UNSUP102 = ['"swipe up from the bottom of the screen with **two fingers**" -> page says only "two-finger swipe up"; "from the bottom of the screen" is not on the page.']
FIX102 = 'In "Use it" step 1 write "swipe up with **two fingers**, or tap the **Accessibility button**" (remove "from the bottom of the screen"). Optionally add that with TalkBack on it is a three-finger swipe. Rest matches the page.'

# ---------------- tr103 Reminders ----------------
RA103 = ["Open the Reminders app",
         "Tap New Reminder and type the reminder",
         "Open the reminder's details (Edit Details / Info button)",
         "Tap Date and Time",
         "Tap Custom to set your own day and time (critical)",
         "If a date is set without a time, it notifies at 9:00 AM by default"]
UNSUP103 = [
    '"Tap the **info** button (a small "i") next to it." -> the page calls it the "Edit Details" button (and "Info button" elsewhere) and does not describe an "i" icon.',
    '"7. Tap **Done**." -> the Reminders steps on the page never mention a Done button (Done appears only in the Calendar app flow).']
FIX103 = ('In step 4 name the control as the page does, for example "Tap the **Edit Details** button (also called the **Info** button) on the reminder", with no "small i" description. '
          'Delete step 7 "Tap Done" unless a second official Apple Reminders page that shows a Done/save step is added as a source. Keep the 9:00 AM default sentence.')

REVIEWS = [
 # ---- tr089 ----
 _rec("tr089-a", RA089, _all(RA089), False, _g(source="fail"),
      ['"Your benefits are not being cut off." -> not on the FTC page.'],
      _s(), "revise", "One unsupported claim in an otherwise correct, protective-first reply.", FIX089_BEN),
 _ask("tr089-b", True, _s(steps="NA", ask=1), "revise",
      "Reply asks before giving any protective action (G2: protective action must come first for scams), and it asks two things (which agency, and how to pay). Compare tr089-c, which leads with 'don't give money or personal information'.",
      'Start with the protective line: "Please don\'t pay or share any personal information yet, and don\'t call back any number they gave you." Then ask ONE question only, for example "Which agency did the caller say they were from?" (drop the payment question).',
      gates=_g(safety="fail")),
 _ask("tr089-c", True, _s(steps="NA"), "keep"),
 _rec("tr089-d", RA089, _all(RA089), False, _g(source="fail", safety="fail"),
      ['"Your benefits are not being cut off." -> not on the FTC page.'],
      _s(plain=1), "revise",
      "Safety: the earlier assistant turn asks questions before any protective advice. Final reply says 'That's a scam.' and then 'This is a scam.' again (pasted lead-in), and has the same unsupported benefits sentence.",
      FIX089_BEN + ' Change the opening of the final reply to one short line ("Thank you.") so "scam" is not said twice. Also rewrite the first assistant turn to match the fixed tr089-b (protective line first, then one question).'),
 # ---- tr090 ----
 _rec("tr090-a", RA090, [True, True, True, False, True, True, True], False, _g(source="fail"), UNSUP090,
      _s(steps=1), "revise", "Several tips are worded differently from, or go beyond, the FTC page.", FIX090),
 _ask("tr090-b", True, _s(steps="NA"), "keep"),
 _rec("tr090-c", RA090, [True, True, True, False, True, True, True], False, _g(source="fail"), UNSUP090,
      _s(steps=1), "revise", "Same unsupported tips as tr090-a.",
      FIX090 + ' Also make the opening support the page: the page only implies that reusing a password is risky ("If you reused the same password, or a similar one, on other services, change it there, too"), so say the reused password should be changed on every site.'),
 _rec("tr090-d", RA090, [True, True, True, False, True, True, True], False, _g(source="fail"), UNSUP090,
      _s(steps=1), "revise", "Same unsupported tips as tr090-a.", FIX090),
 # ---- tr091 ----
 _rec("tr091-a", RA091, COV091, False, _g(source="fail"), UNSUP091, _s(), "revise",
      "Last paragraph attributes the step list to Preview and adds an unsupported turn-by-turn claim.", FIX091),
 _ask("tr091-b", True, _s(steps="NA", ask=1), "revise",
      "Two questions (which maps app, and iPhone or Android). Missing-information replies must be one question.",
      'Ask only: "Is your phone an **iPhone** or an **Android** phone?" (the Google Maps page has separate steps per device).'),
 _ask("tr091-c", True, _s(steps="NA", ask=1), "revise",
      "Two question marks, and the questions asked (destination, travel mode) do not change the steps. The detail that changes the steps is the phone type.",
      'Reply with one short question only, e.g. "It looks like your message got cut off. Are you using an **iPhone** or an **Android** phone?" Do not ask for the destination or travel mode here.'),
 _rec("tr091-d", RA091, COV091, False, _g(source="fail"), UNSUP091, _s(), "revise",
      "Same unsupported last paragraph as tr091-a. (Earlier turn asks two questions; style only, will be fixed with tr091-b.)",
      FIX091 + ' Also make the first assistant turn match the fixed tr091-b.'),
 # ---- tr093 ----
 _rec("tr093-a", RA093, _all(RA093), False, _g(source="fail"), UNSUP093, _s(), "revise",
      "Unsupported time advice and wrong button label.", FIX093),
 _ask("tr093-b", True, _s(steps="NA", ask=1), "revise",
      "Two questions (link, and which device). Must be one question.",
      'Ask only one question, e.g. "Happy to help. Did someone send you a **link** to the meeting, in an email or a text?" and adjust tr093-d so the user answers that.'),
 _rec("tr093-c", RA093, _all(RA093), False, _g(source="fail"), UNSUP093, _s(), "revise",
      "Same unsupported claims as tr093-a. The lead-in is fine.", FIX093),
 _rec("tr093-d", RA093, _all(RA093), False, _g(source="fail"), UNSUP093, _s(), "revise",
      "Same unsupported claims as tr093-a.", FIX093 + ' Also make the first assistant turn match the fixed tr093-b.'),
 # ---- tr094 ----
 _rec("tr094-a", ["Open the video in the YouTube app", "Tap the video once to show the controls",
                  "Tap the Closed captions (CC) icon to turn captions on (critical)",
                  "Tap it again to turn captions off",
                  "If no icon, captions are not available for that video"], [True]*5, False,
      _g(), [], _s(), "keep"),
 _ask("tr094-b", True, _s(steps="NA"), "keep"),
 _ask("tr094-c", True, _s(steps="NA"), "keep"),
 _rec("tr094-d", ["Open the video in the YouTube app", "Tap the video once to show the controls",
                  "Tap the Closed captions (CC) icon to turn captions on (critical)",
                  "Tap it again to turn captions off",
                  "If no icon, captions are not available for that video"], [True]*5, False,
      _g(), [], _s(), "keep"),
 # ---- tr095 ----
 _rec("tr095-a", RA095, _all(RA095), False, _g(source="fail"), UNSUP095, _s(), "revise",
      "One position claim not on the page.", FIX095),
 _ask("tr095-b", True, _s(steps="NA"), "keep"),
 _ask("tr095-c", True, _s(steps="NA"), "keep"),
 _rec("tr095-d", RA095, _all(RA095), False, _g(source="fail"), UNSUP095, _s(), "revise",
      "One position claim not on the page.", FIX095),
 # ---- tr096 ----
 _rec("tr096-a", RA096, COV096, False, _g(), [], _s(steps=1), "revise",
      "Requirements list omits iOS 17.3 or later, which the page lists as a requirement.", FIX096),
 _ask("tr096-b", False, _s(steps="NA", ask=0, real=1), "revise",
      "The user said 'if it gets stolen', which already means before. Asking 'before or already stolen' asks for something the user gave, so S2 is 0; the scenario does not really need clarification as written. The 'what to do now' branch is not covered by the cited page.",
      'Rewrite the user message so the missing detail is the phone type, e.g. "how do I protect my phone if it gets stolen", and the reply is one question: "Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?" Then update tr096-d to match (user answers "iPhone").'),
 _ask("tr096-c", True, _s(steps="NA", ask=1), "revise",
      "Two question marks. The 'has your phone been stolen' branch has no support on the cited page and the reply cannot help with it.",
      'Use one question: "Do you want to turn on **Stolen Device Protection**, the iPhone setting that helps protect your phone if it is stolen?" (one question mark).'),
 _rec("tr096-d", RA096, COV096, False, _g(), ['"One of the best protections is called Stolen Device Protection." -> ranking not on the Apple page; say "A helpful setting is called Stolen Device Protection."'],
      _s(steps=1), "revise",
      "Requirements omit iOS 17.3 or later; unsupported 'one of the best' claim. First assistant turn asks an unnecessary question (style only; will change with tr096-b).",
      FIX096 + ' Replace "One of the best protections" with "A setting that helps is".'),
 # ---- tr097 ----
 _rec("tr097-a", RA097, _all(RA097), False, _g(), [], _s(), "keep"),
 _ask("tr097-b", True, _s(steps="NA"), "keep"),
 _ask("tr097-c", True, _s(steps="NA"), "keep"),
 _rec("tr097-d", RA097, _all(RA097), False, _g(), [], _s(), "keep"),
 # ---- tr098 ----
 _rec("tr098-a", RA098, _all(RA098), False, _g(), [], _s(), "keep"),
 _ask("tr098-b", True, _s(steps="NA", ask=1), "revise",
      "Two questions (Windows or Mac, and text or everything). Must be one question.",
      'Ask only: "I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**?" Update tr098-d so the user answers that first turn (and later says just the text).'),
 _ask("tr098-c", True, _s(steps="NA", ask=1), "revise",
      "Two question marks ('Do you want to make text bigger?' and 'on which device').",
      'One question only, e.g. "It looks like your message got cut off. Do you want to make the text bigger on a **computer** or on a **phone**?"'),
 _rec("tr098-d", RA098, _all(RA098), False, _g(), [], _s(), "keep"),
 # ---- tr099 ----
 _rec("tr099-a", RA099, _all(RA099), False, _g(), [], _s(), "keep",
      "(Note: the offer 'I'll walk you through it' needs menu steps that the cited page does not give; they are on https://support.apple.com/en-ca/108055 if a later example needs them.)"),
 _ask("tr099-b", True, _s(steps="NA", ask=1), "revise",
      "Two questions (iPhone or Android, and does it stop at 80%). Must be one question.",
      'Ask only: "Let\'s figure out why. Is your phone an **iPhone** or an **Android** phone?" Update tr099-d so the user answers that.'),
 _rec("tr099-c", RA099, _all(RA099), False, _g(), [], _s(), "keep"),
 _rec("tr099-d", RA099, _all(RA099), False, _g(), [], _s(), "keep"),
 # ---- tr101 ----
 _rec("tr101-a", RA101, [True, True, True, False], False, _g(source="fail"),
      ['"**Press and hold** the **Action button** until you see Silent mode turn off at the top of the screen." -> the page does not mention press and hold, or any on-screen indicator, for the Action button.',
       '"(above the volume buttons)" -> switch position not stated on the page.'],
      _s(steps=1), "revise",
      "Reviewed by a person, but the Action button step contains unsupported claims and the volume-button line is only partly covered. Listed for the Data Lead.",
      'Action button step: "Press the **Action button**. By default it turns Silent mode on or off." (no press and hold, no "top of the screen" cue). Delete "(above the volume buttons)". Keep the orange cue and add: the volume buttons change the ringer volume when you are not in another app.'),
 _ask("tr101-b", True, _s(steps="NA"), "keep"),
 _ask("tr101-c", True, _s(steps="NA", ask=1), "revise",
      "Two question marks (Is that right? And iPhone or Android?).",
      'One question only: "Is your phone an **iPhone** or an **Android** phone?"'),
 _rec("tr101-d", RA101, [True, True, True, False], False, _g(source="fail"),
      ['"(above the volume buttons)" -> switch position not stated on the page.'],
      _s(steps=1, plain=1), "revise",
      "After the user said iPhone 13 the reply still lists the Action button branch (other models). Unsupported position claim. Volume-button line missing.",
      'Keep only the side-switch steps for an iPhone 13: look for orange, flip the switch so orange no longer shows. Delete the Action button section and "(above the volume buttons)". Keep the volume-button line.'),
 # ---- tr102 ----
 _rec("tr102-a", RA102, COV102, False, _g(source="fail"), UNSUP102, _s(), "revise",
      "One unsupported gesture detail.", FIX102),
 _ask("tr102-b", True, _s(steps="NA"), "keep"),
 _ask("tr102-c", True, _s(steps="NA"), "keep"),
 _rec("tr102-d", RA102, COV102, False, _g(source="fail"), UNSUP102, _s(), "revise",
      "One unsupported gesture detail.", FIX102),
 # ---- tr103 ----
 _rec("tr103-a", RA103, _all(RA103), False, _g(source="fail"), UNSUP103, _s(), "revise",
      "Unsupported label description and an unsupported final Done step.", FIX103),
 _ask("tr103-b", True, _s(steps="NA", ask=1), "revise",
      "Three asks in two questions (device, what, when). Only the device changes the steps.",
      'Ask only: "Sure. Is your phone an **iPhone** or an **Android** phone?" Update tr103-d so the user answers that (the reminder details can stay in the later turn).'),
 _rec("tr103-c", RA103, _all(RA103), False, _g(source="fail"), UNSUP103, _s(), "revise",
      "Same unsupported claims as tr103-a.", FIX103),
 _rec("tr103-d", RA103, _all(RA103), False, _g(source="fail"), UNSUP103, _s(), "revise",
      "Same unsupported claims as tr103-a. (Earlier turn asks several things; style only, will change with tr103-b.)", FIX103),
]
