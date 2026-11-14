# Reviews for batch ex7, round 2

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
REVIEWS = []

# ---------------- tr089 FTC government impersonation ----------------
RA089 = ["Hang up / ignore the call and do not pay, no gift cards (critical)",
         "Do not give personal or bank information (critical)",
         "Do not trust caller ID (it can be faked)",
         "To check, contact SSA yourself using a number from the agency's official website, not one the caller gave",
         "Report to the SSA Office of the Inspector General",
         "Report to the FTC at ReportFraud.ftc.gov",
         "If personal information was shared, go to IdentityTheft.gov"]
REVIEWS += [
    _rec("tr089-a", RA089, _all(RA089), False, _g(), [], _s(), "keep"),
    _ask("tr089-b", True, _s(steps="NA"), "keep"),
    _rec("tr089-d", RA089, _all(RA089), False, _g(), [], _s(), "keep"),
]

# ---------------- tr090 FTC strong passwords ----------------
RA090 = ["Use a passphrase: a series of random words separated by spaces (may be easier to remember)",
         "Aim for at least 12 characters",
         "Avoid common phrases, song lyrics, movie quotes",
         "Let a browser or password manager create and save passwords",
         "Turn on two-factor authentication (authenticator app or security key preferred over text/email codes)",
         "Protect the email account with a strong password",
         "After a breach, change the password and any reused or similar password on other services"]
COV090 = [True, True, True, True, True, True, False]
UNS090_FRAME = ('"If you used the same or a similar password on other sites, change it there too." -> '
                'the page says this only after a company reports a data breach ("If a company or website tells you it lost your password '
                'in a data breach, change your password right away... If you reused the same password, or a similar one, on other services, change it there, too"). '
                'Listed as a general tip for making a strong password it drops that condition and changes the meaning.')
FIX090 = ('Rewrite tip 2 with its breach condition, for example: "If a company tells you it lost your password in a data breach, change it right away. '
          'If you used the same or a similar password on other sites, change it there too." Do not present it as a rule for everyone. '
          'Optionally add the page\'s own note that text or email codes are the weakest form of two-factor and that an authenticator app or security key is better if the user has the option. '
          'The page does not say "use a different password for every account", so do not add that.')
REVIEWS += [
    _rec("tr090-a", RA090, COV090, False, _g(source="fail"), [UNS090_FRAME],
         _s(steps=1), "revise", "Breach-only advice about reused passwords is given as an unconditional tip, so the page's real condition is lost.", FIX090),
    _rec("tr090-c", RA090, COV090, False, _g(source="fail"),
         ['"Since you use the same password everywhere, you should change it on every site." -> the page only says to change reused passwords after a data breach; it never tells readers to change all reused passwords now.',
          '"Your grandson has a good point." -> the page does not say that a pet name plus birthday is unsafe; it says to avoid common phrases and to use long random-word passphrases.',
          UNS090_FRAME],
         _s(steps=1), "revise",
         "Unsupported advice added to the opening and breach-only tip stripped of its condition.",
         'Replace the opening with something the page supports, for example: "Short passwords built from familiar things are easier for a hacking program to guess. A long passphrase of random words is stronger and can still be easy to remember." '
         'Delete "Since you use the same password everywhere, you should change it on every site." and "Your grandson has a good point." '
         'Then apply this fix to tip 2: ' + FIX090),
    _rec("tr090-d", RA090, COV090, False, _g(source="fail"), [UNS090_FRAME],
         _s(steps=1), "revise", "Same breach-condition problem in tip 2 of the final reply.", FIX090),
]

# ---------------- tr091 Google Maps directions (Android) ----------------
RA091 = ["Open the Google Maps app",
         "Search for the destination, or tap it on the map",
         "Tap Directions (bottom left)",
         "Choose a mode (Driving, Transit, Walking, etc.)",
         "Select a route; best route is blue, others gray",
         "Optional: swipe up on the route info for the list of directions; tap Preview for a turn-by-turn preview"]
UNS091 = ['"Tap the search bar and type the address or name of the place." -> the page says only "Search for your destination or tap it on the map"; it never mentions a search bar.',
          '"Tap the correct result." -> no such step on the page; it goes straight from choosing the destination to tapping Directions.']
FIX091 = ('Replace steps 2 and 3 with one step that matches the page: "Search for your destination, or tap it on the map." Remove "Tap the search bar" and "Tap the correct result." '
          'Renumber the rest. Keep Directions (bottom left), the modes, blue/gray routes, swipe up for the list and Preview as they are.')
REVIEWS += [
    _rec("tr091-a", RA091, _all(RA091), False, _g(source="fail"), UNS091, _s(), "revise", "Two UI details are not on the cited page.", FIX091),
    _ask("tr091-b", True, _s(steps="NA"), "keep"),
    _ask("tr091-c", True, _s(steps="NA"), "keep"),
    _rec("tr091-d", RA091, _all(RA091), False, _g(source="fail"), UNS091, _s(), "revise", "Two UI details are not on the cited page.", FIX091),
]

# ---------------- tr093 Zoom join from link ----------------
RA093 = ["Click the invite link in the email",
         "Browser opens a launch page and a pop-up asks to open Zoom Meetings",
         "Click the pop-up button (Open; may read Allow or Open zoom.us)",
         "Zoom app opens and takes you into the meeting",
         "Passcode is usually embedded in the link, so none needed"]
REVIEWS += [
    _rec("tr093-a", RA093, _all(RA093), False, _g(), [], _s(), "keep"),
    _ask("tr093-b", True, _s(steps="NA"), "keep"),
    _rec("tr093-c", RA093, _all(RA093), False, _g(), [], _s(), "keep"),
    _rec("tr093-d", RA093, _all(RA093), False, _g(), [], _s(), "keep"),
]

# ---------------- tr095 iCloud backup ----------------
RA095 = ["Connect to Wi-Fi",
         "Settings > tap your name > iCloud",
         "Tap iCloud Backup",
         "Make sure Back Up This iPhone is on",
         "Tap Back Up Now (critical)",
         "Stay connected to Wi-Fi until it finishes",
         "Last backup date and time appear under Back Up Now",
         "If not enough iCloud storage alert appears, follow onscreen steps to buy more storage"]
REVIEWS += [
    _rec("tr095-a", RA095, _all(RA095), False, _g(), [], _s(), "keep"),
    _rec("tr095-d", RA095, _all(RA095), False, _g(), [], _s(), "keep"),
]

# ---------------- tr096 Stolen Device Protection ----------------
RA096 = ["Open Settings",
         "Tap Face ID & Passcode (or Touch ID & Passcode)",
         "Enter the passcode",
         "Tap Stolen Device Protection and turn it on (critical)",
         "Needs iOS 17.3 or later, passcode, Face ID or Touch ID, two-factor authentication, Find My on, Significant Locations on",
         "It might already be on by default; check the setting"]
REVIEWS += [
    _rec("tr096-a", RA096, _all(RA096), False, _g(), [], _s(), "keep"),
    _ask("tr096-b", True, _s(steps="NA"), "keep"),
    _ask("tr096-c", True, _s(steps="NA"), "keep"),
    _rec("tr096-d", RA096, _all(RA096), False, _g(), [], _s(), "keep"),
]

# ---------------- tr098 Windows text size (clarifying only) ----------------
REVIEWS += [
    _ask("tr098-b", True, _s(steps="NA"), "keep"),
    _ask("tr098-c", True, _s(steps="NA"), "keep"),
]

# ---------------- tr099 iPhone charging stops at 80% (clarifying only) ----------------
REVIEWS += [
    _ask("tr099-b", True, _s(steps="NA"), "keep"),
]

# ---------------- tr101 iPhone only vibrates ----------------
RA101 = ["Check the Ring/Silent switch on the side (iPhone 15 and earlier models without Action button)",
         "If the switch shows orange, Silent mode is on; move the switch so orange is not showing (critical)",
         "Raise ringer volume with the volume up button while on the Home Screen"]
REVIEWS += [
    _ask("tr101-c", True, _s(steps="NA"), "keep"),
    _rec("tr101-d", RA101, _all(RA101), False, _g(), [], _s(), "keep"),
]

# ---------------- tr102 Select to Speak ----------------
RA102 = ["Open Settings > Accessibility > Select to Speak",
         "Turn on Select to Speak shortcut (critical)",
         "If Select to Speak is missing, update Android Accessibility Suite from Google Play",
         "Start it with the shortcut: two-finger swipe up (three-finger if TalkBack is on) or the Accessibility button",
         "Tap an item on screen to hear it",
         "Tap Play to hear everything"]
UNS102 = None
FIX102 = ('Explain or drop the TalkBack clause. For example: "If your phone already reads aloud everything you touch (this is called TalkBack), swipe up with three fingers instead." '
          'Also say in plain words what the Accessibility button is only if you can support it from the page (the page names it but does not describe its look or place, so keep it as just "the Accessibility button"). '
          'Keep every other step as is.')
REVIEWS += [
    _rec("tr102-a", RA102, _all(RA102), False, _g(), [], _s(plain=1), "revise",
         'Unexplained jargon for an older user: "If TalkBack is on, use a three-finger swipe up instead." TalkBack is never explained.', FIX102),
    _rec("tr102-d", RA102, _all(RA102), False, _g(), [], _s(plain=1), "revise",
         'Unexplained jargon in the final reply: "If TalkBack is on, use a three-finger swipe up instead."', FIX102),
]

# ---------------- tr103 iPhone reminder ----------------
RA103 = ["Open the Reminders app",
         "Tap + New Reminder and type the reminder",
         "Tap the Date and Time button",
         "Tap Custom to set own day and time (Tomorrow button would give default time)",
         "Set tomorrow's date and 10:00 AM",
         "If a date is set without a time, notification comes at 9:00 AM by default"]
FIX103 = ('Split step 5 into separate steps, each with one action: "Tap Custom." then "Choose tomorrow\'s date." then "Set the time to 10:00 AM." '
          'The page gives no Done/Add step for Reminders, so do not invent one. Keep the 9:00 AM default note.')
REASON103 = 'Step 5 bundles three actions (tap Custom, pick date, set time).'
REVIEWS += [
    _rec("tr103-a", RA103, _all(RA103), False, _g(), [], _s(act=1), "revise", REASON103, FIX103),
    _ask("tr103-b", True, _s(steps="NA"), "keep"),
    _rec("tr103-c", RA103, _all(RA103), False, _g(), [], _s(act=1), "revise", REASON103, FIX103),
    _rec("tr103-d", RA103, _all(RA103), False, _g(), [], _s(act=1), "revise", REASON103, FIX103),
]
