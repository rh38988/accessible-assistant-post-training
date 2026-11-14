# Reviews for batch ny6b, round 2 (re-review of revised examples). Independent reviewer.
# Page 1 done: https://support.google.com/chrome/answer/3220216

REVIEWS = []

# ---- page 1: chrome 3220216 ----
# Source steps: Open Chrome, More, Settings; Privacy and security, Site Settings, Notifications;
# under Notifications choose "Allow quieter notification prompts", turn on "Allow sites to ask to send notifications",
# then select "Use quieter messaging". Bell icon next to the website's address; "no pop-up prompt will show".
# Pop-ups and redirects: Privacy and security, Site Settings, Pop-ups and redirects; Add next to
# "Not allowed to send pop-ups or use redirects" when the site is not listed; More, then Block for a listed site.
REVIEWS += [
    {
        "id": "tr193-e",
        "required_actions": [
            "Open Chrome, select More, then Settings (critical)",
            "Select Privacy and security, then Site Settings, then Notifications (critical)",
            "Select Allow quieter notification prompts (critical)",
            "Turn on Allow sites to ask to send notifications (critical)",
            "Select Use quieter messaging (critical)",
        ],
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr193-r",
        "required_actions": [
            "Open Privacy and security, then Site Settings, then Pop-ups and redirects (critical)",
            "Find the site under Allowed to send pop-ups and use redirects; if listed, select More, then Block (critical)",
            "If not listed, select Add next to Not allowed to send pop-ups or use redirects, type the web address, select Add (critical)",
        ],
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# ---- page 2: chrome 10538231 (Live Caption) ----
# Source steps: Open Chrome; More, Settings, Accessibility; turn Live Caption on.
# "If you want to get Live Captions in a language other than English": next to "Manage languages" select
# "Add languages" ("This will automatically download language packs."); next to "Preferred caption language"
# select the "Down arrow" icon, then your preferred language. Captions "appear in a bubble that you can drag".
# Spanish is named on this page only in the Live Translate section (Chromebook Plus), not in the Live Caption steps.
REVIEWS += [
    {
        "id": "tr194-c",
        "required_actions": [
            "Open Chrome, select More, then Settings, then Accessibility (critical)",
            "Turn Live Caption on (critical)",
            "Next to Manage languages, select Add languages (critical)",
            "Next to Preferred caption language, select the Down arrow (critical)",
            "Choose the caption language from the list (critical)",
        ],
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'Choose Spanish.' (step 5) and 'Choose Spanish.' (step 7) -> the page does not say Spanish can be chosen for Live Caption captions; it names Spanish only in the Live Translate section (Chromebook Plus devices). The request for Spanish captions is therefore not supported by the cited page.",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 1, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "Source gate fails: the reply promises Spanish captions, but the page only says 'a language other than English' and does not list Spanish for Live Caption. Constraint score is 1 because the user's stated goal (Spanish captions) is not confirmed by the source. Steps 1 to 4 and 'the Down arrow' wording are supported (the page says 'Down arrow icon'), so no change is needed there.",
        "fix": "In the opening line, replace 'Yes, Chrome can do that.' with 'Chrome can show captions in a language other than English.' Replace step 5 'Choose Spanish. Chrome downloads the language pack by itself.' with 'Choose the language you want from the list. Chrome downloads the language pack by itself.' Replace step 7 'Choose Spanish.' with 'Choose the same language.' Keep step 6 'Next to Preferred caption language, select the down arrow.' Add one sentence after the steps: 'This page does not say whether Spanish is in the list, so if it is not there, Live Caption may not support Spanish.' Do not cite Live Translate for Spanish captions.",
    },
]

# ---- page 3: googleone 9776477 (Storage Manager) ----
# Source steps: one.google.com, Storage, Clean up space, Clean up by service (or Clean up suggested items),
# select files; for Google Photos "download copies first by clicking Download"; click Delete at top right;
# "Read the consent wording to confirm", "Check the box to continue"; for Photos click "Move to trash".
# Permanently delete for other services. Update timing: "up to 48-72 hours" after deleting many files.
# "If after 48-72 hours you still are at quota, you might have files ... set to back up automatically."
# "unless automatic back up is turned off". Page gives NO steps for Google Photos backup settings.
REVIEWS += [
    {
        "id": "tr197-e",
        "required_actions": [
            "Go to one.google.com and click Storage (critical)",
            "Select Clean up space (critical)",
            "Under Clean up by service, choose Google Photos (critical)",
            "Select the photos to remove (critical)",
            "Click Download to keep copies first (critical, from the user's constraint)",
            "Click Delete at the top right (critical)",
            "Read the consent wording and check the box to continue (critical)",
            "Click Move to trash (critical)",
        ],
        "covered": [True, True, True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr197-r",
        "required_actions": [
            "Go to one.google.com, click Storage, select Clean up space (critical)",
            "Select the files, click Delete, check the box, click Permanently delete (critical)",
            "Wait 48 to 72 hours for the total to update, then check the storage again (critical)",
            "If still full, check which files are set to back up automatically and turn off automatic backup (critical)",
        ],
        "covered": [True, True, True, False],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "The 48 to 72 hour wait and the automatic backup explanation are supported by the page. But the final turn ends on an explanation with no next action: it does not tell the user what to do if the storage is still full after the wait, and it names no place to check or turn off automatic backup. The page gives no steps for that, so the reply cannot give them from this source.",
        "fix": "Replace the last paragraph of the final assistant turn with: 'If it is still full after 48 to 72 hours, some photos and videos may be set to back up automatically. Automatic backup can be turned off, and then files waiting to be backed up will stop using the free space.' Keep the sentence 'The total can take 48 to 72 hours to update after a large deletion, so please wait that long first.' Do not name Google Photos backup settings or give steps to find them unless a source page gives them. To give a location, add the Google Photos backup help article linked from https://support.google.com/googleone/answer/9776477 as a second source and cite its steps.",
    },
]

# ---- page 4: maps 144339 (directions, Options, Tolls) and page 5: maps 7101463 (print directions) ----
# Source steps: Directions; enter starting point and destination; Walking or Driving icon; "Choose Options";
# "Check the box next to 'Tolls' or 'Highways'" (section "Avoid tolls & highways"); "Under the route you want, click Details".
# Printing (7101463): Directions; enter destination; choose a route; click the "Print" icon; choose "Print including maps"
# or "Print text only"; click "Print". The page does not say where the Print icon is.
REVIEWS += [
    {
        "id": "tr198-c",
        "required_actions": [
            "Open Google Maps in the browser and click Directions (critical)",
            "Enter the starting point and the destination (critical)",
            "Choose Walking (critical)",
            "Choose the route (critical)",
            "Click the Print icon (critical)",
            "Choose Print including maps or Print text only (critical)",
            "Click Print (critical)",
        ],
        "covered": [True, True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
    {
        "id": "tr198-e",
        "required_actions": [
            "Open Google Maps in the browser and click Directions (critical)",
            "Enter a starting point and a destination (critical)",
            "Choose Driving (critical)",
            "Choose Options (critical)",
            "Check the box next to Tolls (critical)",
        ],
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]
