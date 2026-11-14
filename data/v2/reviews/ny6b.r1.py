# Reviews for batch ny6b, round 1. Independent reviewer.

PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}


def sc(steps=2, ask=2, con=2, act=2, plain=2, real=2):
    return {"steps": steps, "ask_or_answer": ask, "constraints": con, "actionable": act, "plain": plain, "realistic_user": real}


def keep(id, ra, cov=None, clar=False, scores=None):
    return {"id": id, "required_actions": ra, "covered": cov if cov is not None else [True] * len(ra),
            "needs_clarification": clar, "gates": dict(PASS), "unsupported_claims": [],
            "scores": scores or sc(), "decision": "keep", "reasons": "", "fix": ""}


def ask(id):
    return keep(id, [], [], True, sc(steps="NA"))


REVIEWS = []

# ---- page 1: chrome 3220216 ----
BLOCK_RA = ["Open Chrome, select More, then Settings (critical)", "Select Privacy and security, Site Settings, Notifications (critical)",
            "Next to Not allowed to send notifications, select Add (critical)", "Enter the site's web address (critical)", "Select Add (critical)"]
REVIEWS += [
    keep("tr193-a", BLOCK_RA),
    keep("tr193-c", ["Select the Settings icon in the Get notifications? message (critical)", "Select Don't allow (critical)"]),
    ask("tr193-b"),
    keep("tr193-d", BLOCK_RA),
    {"id": "tr193-e",
     "required_actions": ["Open Chrome, More, Settings (critical)", "Privacy and security, Site Settings, Notifications (critical)",
                          "Choose the default option 'Allow quieter notification prompts' / 'Allow sites to ask to send notifications' (critical)",
                          "Select Use quieter messaging (critical)", "Expect a bell icon next to the site address instead of the pop-up"],
     "covered": [True, True, True, True, True], "needs_clarification": False, "gates": dict(PASS), "unsupported_claims": [],
     "scores": sc(act=1), "decision": "revise",
     "reasons": "Step 3 'choose the option that lets sites ask for notifications' gives no on-screen label, so the user cannot tell which option to pick.",
     "fix": "Rewrite step 3 to use the page's wording: 'Select **Allow quieter notification prompts**, then choose the option that allows sites to ask to send notifications.' Keep step 4 (**Use quieter messaging**) and the closing bell-icon sentence."},
    {"id": "tr193-r",
     "required_actions": ["Select Privacy and security, Site Settings, Pop-ups and redirects (critical)",
                          "Under Allowed to send pop-ups and use redirects, find the site (critical)",
                          "To the right of the site select More, then Block (critical)",
                          "If the site is not listed, select Add next to Not allowed to send pop-ups or use redirects, enter the address, select Add"],
     "covered": [True, True, True, False], "needs_clarification": False, "gates": dict(PASS), "unsupported_claims": [],
     "scores": sc(steps=1), "decision": "revise",
     "reasons": "Final reply only handles the case where the site is already in the Allowed list; a site that is not listed leaves the user stuck. Page gives the alternative.",
     "fix": "Add a line after step 3: 'If you do not see the site in that list, select **Add** next to **Not allowed to send pop-ups or use redirects**, type the site's web address, then select **Add**.' Also say step 3 starts after the user selects More to the right of the site's name."},
]

# ---- page 2: chrome 10538231 ----
LC_RA = ["Open Chrome, select More, then Settings (critical)", "Select Accessibility (critical)", "Turn Live Caption on (critical)"]
REVIEWS += [
    keep("tr194-a", LC_RA),
    {"id": "tr194-c",
     "required_actions": LC_RA + ["Next to Manage languages, select Add languages and choose Spanish (critical)",
                                  "Next to Preferred caption language, open the dropdown and choose Spanish (critical)"],
     "covered": [True] * 5, "needs_clarification": False, "gates": dict(PASS),
     "unsupported_claims": ["'open the down arrow and choose Spanish' -> page says 'open the dropdown'; no 'down arrow' is described"],
     "scores": sc(act=1), "decision": "revise",
     "reasons": "Step 4 bundles adding the language and choosing it in one step, and step 5 describes the control as a 'down arrow', which the page does not say.",
     "fix": "Change step 5 to: 'Next to **Preferred caption language**, open the dropdown and choose **Spanish**.' Optionally split step 4 into 'Next to **Manage languages**, select **Add languages**' and 'Choose **Spanish**. Chrome downloads the language pack by itself.'"},
    ask("tr194-b"),
    keep("tr194-d", LC_RA),
    keep("tr194-e", LC_RA[:2] + ["Linux: select Captions (critical)", "Turn Live Caption on (critical)", "Drag the bubble to move it; arrow in the bubble collapses or expands captions"]),
    keep("tr194-r", ["Turn up the video volume so Live Caption can pick up the sound (critical)"]),
]

# ---- page 3: accounts 3067630 ----
SO_RA = ["Go to myaccount.google.com (critical)", "Select Security & sign-in (critical)", "In the Your devices panel, select Manage all devices (critical)",
         "Select the device, then select Sign out (critical)"]
REVIEWS += [
    keep("tr195-a", SO_RA + ["Same device name listed more than once: sign out of every entry with that name"]),
    keep("tr195-c", SO_RA),
    ask("tr195-b"),
    keep("tr195-d", SO_RA),
    keep("tr195-e", SO_RA),
    keep("tr195-r", ["Entries with the same name may be one device or several; sign out of every session with that name (critical)"]),
]

# ---- page 4: accounts 183723 ----
RP_RA = ["Go to myaccount.google.com (critical)", "Select Security & sign-in (critical)", "Under How you sign in to Google, select Recovery phone (critical)",
         "Follow the on-screen steps (critical)", "Phone tips: gets texts, only yours, carried regularly, not Google Voice"]
REVIEWS += [
    keep("tr196-a", RP_RA),
    keep("tr196-c", ["Go to myaccount.google.com (critical)", "Select Security & sign-in (critical)", "Under How you sign in to Google, select Recovery email (critical)",
                     "Follow the on-screen steps (critical)", "Use an address you use regularly, different from the sign-in email"]),
    ask("tr196-b"),
    keep("tr196-d", RP_RA[:4]),
    keep("tr196-e", ["Say recovery info cannot be added while locked out or in account recovery (critical)", "After getting back in: myaccount.google.com, Security & sign-in, Recovery phone, follow the steps (critical)"]),
    keep("tr196-r", ["Try again from a device you normally use to sign in (critical)", "Or from a location where you normally sign in", "Or the following week from the device you are using now"]),
]

# ---- page 5: googleone 9776477 ----
SM_RA = ["Go to one.google.com and click Storage (critical)", "Select Clean up space (critical)", "Choose a category or service under Clean up suggested items or Clean up by service (critical)",
         "Check the files to remove (critical)", "Click Delete at top right (critical)", "Read the consent wording and check the box (critical)", "Click Permanently delete (critical)"]
REVIEWS += [
    keep("tr197-a", SM_RA + ["Storage total can take 48-72 hours to update"]),
    keep("tr197-c", ["Open Google One app, tap Storage, then Free up account storage (critical)", "Under Clean up other items, tap WhatsApp (critical)", "Tap Delete backup (critical)",
                     "Deleting a backup does not turn off future backups"]),
    ask("tr197-b"),
    keep("tr197-d", SM_RA),
    {"id": "tr197-e",
     "required_actions": ["Go to one.google.com and click Storage (critical)", "Select Clean up space (critical)", "Choose Google Photos under Clean up by service (critical)",
                          "Check the photos (critical)", "Click Download to save copies first (critical)", "Click Delete at top right (critical)",
                          "Read the consent wording and check the box (critical)", "For Photos click Move to trash (critical)"],
     "covered": [True, True, True, True, True, True, False, True], "needs_clarification": False, "gates": dict(PASS), "unsupported_claims": [],
     "scores": sc(steps=1), "decision": "revise",
     "reasons": "Reply skips the page's step 'Read the consent wording, then check the box' between Delete and Move to trash. The user is careful not to lose photos, so the order matters too.",
     "fix": "Replace step 6 with two steps: '6. Click **Delete** at the top right.' '7. Read the wording that appears, check the box to continue, then click **Move to trash**.' Keep Download (step 5) before Delete so copies are saved first."},
    {"id": "tr197-r",
     "required_actions": ["Wait up to 48-72 hours for the storage total to update after a large deletion (critical)",
                          "If still at quota: automatic backup may be refilling the space with queued photos and videos unless it is turned off (critical)"],
     "covered": [True, True], "needs_clarification": False, "gates": dict(PASS),
     "unsupported_claims": ["'Check your **Google Photos** backup settings.' -> page does not name Google Photos in that sentence and gives no place or steps for turning automatic backup off"],
     "scores": sc(act=1), "decision": "revise",
     "reasons": "Last line points to 'Google Photos backup settings' with no location or step, and the page does not give one; the user cannot act on it.",
     "fix": "Replace the last two sentences with: 'If it is still full after that, automatic backup may be filling the space again. Photos and videos waiting to be backed up are added to the free space unless automatic backup is turned off.' Do not name a settings screen; the page gives none (it only links to 'Learn more about Google Photos back ups')."},
]

# ---- page 6: maps 144339 ----
DIR_RA = ["Open Google Maps on the computer and click Directions (critical)", "Enter a starting point and destination (critical)", "Choose a mode (Driving/Transit/Walking) (critical)",
          "Best route is blue, others gray; select a route to choose it", "Click Details under the route to see the steps"]
REVIEWS += [
    keep("tr198-a", DIR_RA, cov=[True, True, True, True, True]),
    {"id": "tr198-c",
     "required_actions": DIR_RA[:3] + ["Click Details under the route", "Print: click the printer icon, choose Print including maps or Print text only, click Print (critical, user's stated goal; on a different page)"],
     "covered": [True, True, True, True, False], "needs_clarification": False, "gates": dict(PASS), "unsupported_claims": [],
     "scores": sc(steps=0, con=0), "decision": "revise",
     "reasons": "The user said they want to print the route. The reply gives walking directions only and never mentions printing, so a stated goal is dropped. The cited page does not cover printing.",
     "fix": "Add a second source https://support.google.com/maps/answer/7101463 (Share, send or print directions from Google Maps, Computer). After step 3 add: '4. Pick the route you want. 5. Click the **printer** icon. 6. Choose **Print including maps** or **Print text only**. 7. Click **Print**.' Keep the Details line optional."},
    ask("tr198-b"),
    keep("tr198-d", DIR_RA[:3] + ["Click Details under the route"]),
    {"id": "tr198-e",
     "required_actions": ["Click Directions, enter start and destination (critical)", "Choose Driving", "Choose Options (critical)", "Check the box for Tolls (critical)"],
     "covered": [True, True, True, True], "needs_clarification": False, "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'Under **Avoid tolls & highways**, check **Tolls**.' -> page says 'Avoid tolls & highways' is only a section heading in the article, not a label on screen; the checkbox labels are Tolls and Highways"],
     "scores": sc(act=1), "decision": "revise",
     "reasons": "Step 5 sends the user to look for a heading that is not on the screen.",
     "fix": "Change step 5 to: 'Check the box next to **Tolls**.' Do not mention 'Avoid tolls & highways'."},
    keep("tr198-r", ["Transit only shows where the local transit agency has added route info to Google Maps (critical)", "Can still choose Driving or Walking"]),
]
