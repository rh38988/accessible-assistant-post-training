# Review round 2, batch ny2a. Page: https://support.apple.com/en-us/102578 (Mail on iPhone, cannot send or receive)
# Required actions derived from the page before judging:
#  1 Make sure the iPhone is connected to the internet
#  2 Check the email provider's status page or contact the provider for an outage
#  3 Sign in to the provider's website to check email address and password
#  4 Settings > Apps > Mail > Mail Accounts > Fetch New Data; Automatically, Manually, or a schedule
#  5 Ask the provider about two-step verification or other security features; may need a special password
#  6 Contact provider or system administrator if a username or password error remains
#  7 Last resort: confirm all email is saved elsewhere, then Settings > Apps > Mail > Mail Accounts > tap account > Delete Account, then add the account again

REVIEWS = []

REVIEWS += [
    {
        "id": "tr134-a",
        "required_actions": [
            "Connected to internet (non-critical)",
            "Provider outage check (non-critical)",
            "Sign in to provider website to check email address and password (non-critical)",
            "Settings > Apps > Mail > Mail Accounts > Fetch New Data, with Automatically, Manually, or schedule (critical)",
            "Ask provider about two-step verification or special password (non-critical)",
            "Contact provider or administrator if error remains (non-critical)",
            "Last resort: confirm email saved elsewhere, then Mail Accounts > account > Delete Account, then add again (critical for this step)",
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
        "id": "tr134-d",
        "required_actions": [
            "Connected to internet (non-critical)",
            "Provider outage check (non-critical)",
            "Sign in to provider website to check email address and password (non-critical)",
            "Settings > Apps > Mail > Mail Accounts > Fetch New Data, with Automatically, Manually, or schedule (critical)",
            "Ask provider about two-step verification or special password (non-critical)",
            "Contact provider or administrator if a username or password error remains (non-critical)",
        ],
        "covered": [True, True, True, True, False, False],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "S1 = 1: the page's security step is missing (two-step verification or special password). The reply ends without any step to contact the provider if sign-in still fails.",
        "fix": "After step 3 (or as a new step after step 3), add: 'Ask your provider whether two-step verification or another security feature is turned on. If it is, you may need a special password from them to use email on your iPhone.' At the end of the reply add: 'If it still does not work, contact your email provider or system administrator.' Keep all other steps unchanged.",
    },
    {
        "id": "tr134-e",
        "required_actions": [
            "Connected to internet (non-critical)",
            "Provider outage check (non-critical)",
            "Settings > Apps > Mail > Mail Accounts > Fetch New Data, with Automatically, Manually, or schedule (critical)",
            "Sign in to provider website to check email address and password (non-critical)",
            "Ask provider about two-step verification or special password (non-critical)",
            "Ask provider to confirm account settings (non-critical)",
            "Contact provider or administrator if error remains (non-critical)",
            "Last resort account removal (excluded by the user's constraint; the reply must not steer toward it)",
        ],
        "covered": [True, True, True, True, True, True, False, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
        "decision": "revise",
        "reasons": "S5 = 1: the closing sentence says 'Deleting the account is the last step on the list', but the list has no deletion step (its last item is the provider account check). S1 = 1: no step to contact the provider if sign-in still fails.",
        "fix": "Replace the closing sentence 'Deleting the account is the last step on the list, and it can remove emails already downloaded to the phone, so you can leave it alone for now.' with: 'Removing the account is not on this list. It can delete emails already downloaded to the phone, so do not remove it unless you have first confirmed on your provider's website that all your email is saved somewhere else.' Add to the end of the numbered list (as step 7): 'If none of these work, contact your email provider.'",
    },
]

# Page: https://support.apple.com/en-us/118433 (text messages and photos will not send or arrive on iPhone)
# Required actions derived from the page before judging:
#  1 Check the network connection (cellular or Wi-Fi) (non-critical)
#  2 Tap the red exclamation point, then tap Try Again (critical for Not Delivered)
#  3 Tap the red exclamation point again, then tap Send as Text Message; messaging rates may apply (critical for Not Delivered fallback)
#  4 Storage: make sure there is enough free space to receive images and videos (non-critical)
#  5 Settings > Apps > Messages; turn on Send Photo Previews or Low Quality Image Mode (non-critical)
#  6 Carrier attachment size limits on SMS or MMS; ask carrier whether it supports MMS, RCS, or SMS for the plan (non-critical)
#  7 Restart the iPhone (non-critical)
#  8 Confirm the correct phone number or email address (non-critical)
#  9 Contact Apple Support if you still cannot send or receive iMessages (non-critical)
# 10 Blue bubbles are iMessages; green bubbles are RCS, SMS, or MMS and require a text-messaging plan (informational)

REVIEWS += [
    {
        "id": "tr135-c",
        "required_actions": [
            "Enough storage to receive pictures and videos (non-critical)",
            "Settings > Apps > Messages; turn on Send Photo Previews or Low Quality Image Mode (non-critical)",
            "Ask carrier whether it supports MMS for the plan; carrier may limit attachment size (non-critical)",
            "Restart the iPhone (non-critical)",
        ],
        "covered": [True, True, True, False],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'and these settings help with that' -> the page lists Send Photo Previews and Low Quality Image Mode under 'Lower-quality sending', separately from 'Carrier limits'; it does not say these settings address carrier size limits",
        ],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "One unsupported causal claim about the photo settings and carrier limits. S1 = 1: the page's restart step is not in the reply.",
        "fix": "Delete the sentence 'Some carriers limit the size of attachments on regular text messages, and these settings help with that.' Replace it with: 'Some carriers limit the size of picture messages. Turning on Send Photo Previews or Low Quality Image Mode makes pictures you send use lower quality.' Add a step after step 4 (or before the carrier line): 'Restart your iPhone.' Keep all other text.",
    },
    {
        "id": "tr135-e",
        "required_actions": [
            "Check the network connection (non-critical)",
            "Tap the red exclamation point, then tap Try Again (critical)",
            "Restart the iPhone (non-critical)",
            "Tap the red exclamation point, then tap Send as Text Message; messaging rates may apply (non-critical, the user does not want charges)",
            "Confirm the phone number or email address is correct (non-critical)",
            "Contact Apple Support for blue bubble (iMessage) problems (non-critical)",
        ],
        "covered": [True, True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "S4 = 1: 'Send as Text Message is another option' gives no starting point. The page's path is to tap the red exclamation point again, then tap Send as Text Message.",
        "fix": "Replace 'If it still will not send, **Send as Text Message** is another option, but messaging rates may apply.' with: 'If it still will not send, tap the red exclamation point again, then tap **Send as Text Message**. Messaging rates may apply.' Keep the rest of the reply unchanged, including the sentence about contacting Apple Support.",
    },
]

# Page: https://support.apple.com/en-us/120000 (iPhone No Service or SOS), with https://support.apple.com/en-us/118575 (Software Update)
# Required actions derived from the pages before judging:
#  1 Settings > Airplane Mode on for at least 15 seconds, then off (critical)
#  2 Restart the iPhone (non-critical)
#  3 Contact the carrier: account active and in good standing; in coverage with no outage; device not blocked; right data plan (critical)
#  4 Plug in and connect to Wi-Fi; Settings > General > Software Update; Download and Install if shown (non-critical)
#  5 Carrier settings update: connect to Wi-Fi, Settings > General > About; update carrier settings option if shown (non-critical)
#  6 SOS means emergency calls only through other networks (informational; available in Australia, Canada, and the United States)
#  7 Apple service through its support site if carrier finds no account or network issue and a hardware problem is suspected (non-critical)
#  8 Dual SIM, data roaming, LTE, and IMEI items are conditional on device or travel (not required for this user)

REVIEWS += [
    {
        "id": "tr136-a",
        "required_actions": [
            "Airplane Mode on for at least 15 seconds, then off (critical)",
            "Restart the iPhone (non-critical)",
            "Contact the carrier: account active, coverage with no outage, device not blocked, right data plan (critical)",
            "Plug in and connect to Wi-Fi; Settings > General > Software Update; Download and Install (non-critical)",
            "Carrier settings update: Wi-Fi, Settings > General > About, update carrier settings if shown (non-critical)",
        ],
        "covered": [True, True, True, True, False],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "S1 = 1: the carrier settings update check (Settings > General > About) from the Apple page is not in the reply.",
        "fix": "After step 7 (Download and Install), add two steps: 'Connect to Wi-Fi. Open **Settings**, tap **General**, then tap **About**.' and 'If an update is available, you will see an option to update your carrier settings. Tap it.' Keep all other steps unchanged.",
    },
    {
        "id": "tr136-d",
        "required_actions": [
            "Airplane Mode on for at least 15 seconds, then off (critical)",
            "Restart the iPhone (non-critical)",
            "Contact the carrier to check account and coverage (critical)",
            "Plug in and connect to Wi-Fi; Settings > General > Software Update; Download and Install (non-critical)",
            "Carrier settings update: Wi-Fi, Settings > General > About, update carrier settings if shown (non-critical)",
        ],
        "covered": [True, True, True, True, False],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "S1 = 1: the carrier settings update check (Settings > General > About) is not in the reply.",
        "fix": "After step 5 (Software Update), add two steps: 'Connect to Wi-Fi. Open **Settings**, tap **General**, then tap **About**.' and 'If an update is available, you will see an option to update your carrier settings. Tap it.' Keep all other steps unchanged.",
    },
    {
        "id": "tr136-e",
        "required_actions": [
            "Connect to Wi-Fi; Settings > General > About; update carrier settings if shown (non-critical)",
            "Airplane Mode on for at least 15 seconds, then off (critical)",
            "Contact the carrier: account, coverage, device not blocked (critical)",
            "Plug in; Settings > General > Software Update; Download and Install (non-critical)",
            "Restart deferred by user constraint; the reply says it can be done later (non-critical)",
        ],
        "covered": [True, True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'This may pause your download, so you may prefer to do it after the download finishes.' -> the page does not say that Airplane Mode pauses a download; this is an added claim",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "G1 fail: one unsupported claim about what Airplane Mode does to the download. Otherwise the steps match the page and respect the user's no-restart limit.",
        "fix": "Delete the sentence 'This may pause your download, so you may prefer to do it after the download finishes.' Keep the rest of step 3 as written. Make no other change.",
    },
    {
        "id": "tr136-r",
        "required_actions": [
            "Contact the carrier: account active and in good standing, coverage with no outage, device not blocked, right data plan (critical)",
            "Plug in and connect to Wi-Fi; Settings > General > Software Update; Download and Install (non-critical)",
            "Carrier settings update: Settings > General > About; update carrier settings if shown (non-critical)",
            "If the carrier finds no account or network issue and a hardware problem is suspected, get service through Apple's support site (non-critical)",
        ],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "keep",
        "reasons": "",
        "fix": "",
    },
]

# Page: https://support.apple.com/en-us/118431 (iPhone temperature warning)
# Required actions derived from the page before judging (the warning text is an image and not quoted):
#  1 Turn off the device (critical per the page)
#  2 Move the device to a cooler environment, away from direct sunlight (non-critical)
#  3 Allow the device to cool down (critical per the page)
#  4 An iPhone showing this message might still be able to make emergency calls (informational)

REVIEWS += [
    {
        "id": "tr138-e",
        "required_actions": [
            "Turn off the device (critical per the page)",
            "Move the device to a cooler environment, away from direct sunlight (non-critical)",
            "Allow the device to cool down (critical per the page)",
        ],
        "covered": [True, True, True],
        "needs_clarification": False,
        "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 1, "actionable": 2, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "S3 = 1: the user said not to turn the phone off. The reply still tells them it 'may be safer to turn it off', which pushes against that limit without a clear way to keep the phone on. Safety is not at risk, so the fix is to state the page's steps and the trade-off plainly.",
        "fix": "Replace the reply's first two sentences ('The usual steps ... cool it. The closest option is this:') with: 'Apple's steps for this warning are to turn the iPhone off, move it to a cooler place away from direct sunlight, and let it cool down. Turning it off is the step that helps most.' Keep step 1 ('Move your iPhone to a cooler place, away from direct sunlight.') as the only step for keeping it on, and state it as: 'If you keep it on, move it to a cooler place away from direct sunlight.' Replace 'it may be safer to turn it off and let it cool, or ask the hospital for another number to call' with 'If the call is important, ask the hospital for another number to call.' Keep 'Apple says to let the iPhone cool down before using it again'.",
    },
]

# Page: https://support.apple.com/en-us/101619 (fix wrong date or time on iPhone), with https://support.apple.com/en-us/118575 (Software Update)
# Required actions derived from the pages before judging:
#  1 Connect to the internet (non-critical)
#  2 Install the latest software update: Settings > General > Software Update > Download and Install (non-critical)
#  3 Settings > General > Date & Time > turn on Set Time Automatically (critical)
#  4 If the message says updated time zone information is available, restart the iPhone (non-critical)
#  5 Settings > Privacy & Security > Location Services > scroll to bottom > System Services > turn on Setting Time Zone (critical when time zone is wrong)
#  6 Manual setting: turn off Set Automatically, then Time Zone or tap the date (conditional)
#  7 Gray or locked setting: Screen Time passcode or corporate profile with device restrictions; ask whoever set it up or manages the phone (critical when gray)
#  8 Not all carriers or countries offer the option (informational)

REVIEWS += [
    {
        "id": "tr139-a",
        "required_actions": [
            "Connect to the internet (non-critical)",
            "Install the latest software update (Settings > General > Software Update > Download and Install) (non-critical)",
            "Settings > General > Date & Time > turn on Set Time Automatically (critical)",
            "Restart if the updated time zone information message appears (non-critical)",
            "Privacy & Security > Location Services > System Services > turn on Setting Time Zone (critical when time zone is wrong)",
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
        "id": "tr139-d",
        "required_actions": [
            "Connect to the internet (non-critical)",
            "Install the latest software update (Settings > General > Software Update > Download and Install) (non-critical)",
            "Settings > General > Date & Time > turn on Set Time Automatically (critical)",
            "Restart if the updated time zone information message appears (non-critical)",
            "Privacy & Security > Location Services > System Services > turn on Setting Time Zone (critical when time zone is wrong)",
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
        "id": "tr139-r",
        "required_actions": [
            "Gray switch: a Screen Time passcode may be set; ask whoever set it up (critical when gray)",
            "Gray switch: a corporate profile with device restrictions may be installed; ask whoever manages it (critical when gray)",
            "Some carriers or countries do not offer the option; set the time by hand (non-critical)",
            "Manual setting: Settings > General > Date & Time > turn off Set Automatically; then tap Time Zone and enter a city, or tap the date (non-critical)",
        ],
        "covered": [True, True, True, True],
        "needs_clarification": False,
        "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": [
            "'or enter the passcode if you know it' -> the page does not say that entering a Screen Time passcode unlocks the Date & Time setting",
        ],
        "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
        "decision": "revise",
        "reasons": "G1 fail: the passcode-entry instruction is not on the page. S4 = 1: the manual path ends at 'Then tap Time Zone, or tap the date' without saying what to do next (the page says to enter a city in the time zone you need). The reply also calls the switch 'Set Automatically' in the manual step but 'Set Time Automatically' earlier in the thread, with no note that they are the same setting.",
        "fix": "In item 1, delete 'or enter the passcode if you know it'. Keep 'Ask the person who set it up.' In item 3, change 'Then tap **Time Zone**, or tap the date.' to: 'Then tap **Time Zone** and enter a city in the time zone you need, or tap the date to change the date and time.' Add after 'if **Set Automatically** is not locked, turn it off.': '(This is the same setting as **Set Time Automatically** shown earlier.)'",
    },
]
