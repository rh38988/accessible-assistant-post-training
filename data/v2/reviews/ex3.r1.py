# Reviews for batch ex3, round 1 (written page by page)
REVIEWS = []

# ---- Page: https://support.google.com/android/answer/7680439 (tr033) ----
_A33 = ["Connect to Wi-Fi and charge battery to at least 75% first",
        "Open Settings, tap System, tap Software updates (or tap the update notification and its update button)",
        "Follow the on-screen prompts to download and install",
        "Expect restart: Pixel installs in background and takes effect after next restart; other Android devices usually restart on their own"]
REVIEWS += [
    {"id": "tr033-a", "required_actions": _A33, "covered": [True, True, True, True],
     "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'On some phones this is called **System update** or is in a different spot.' -> the page never names 'System update' as an alternative label; it only says update controls sit under System > Software updates and that schedules vary by manufacturer."],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Unsupported alternative label 'System update'.",
     "fix": "In step 3 delete 'or System update'. Keep only a general hedge such as 'Names can be a little different on some phones.' Optionally add the source cue that the update status appears on that screen (page: 'The update status appears there')."},
    {"id": "tr033-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'Real updates come from your phone's Settings.' -> not on the page, and it contradicts the page, which says a real update can also arrive as a notification that you open and tap its update button.",
                            "'they fix problems and help keep your phone secure' -> page supports security updates only; 'fix problems' is not stated."],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Reviewed by a person, but the claim 'Real updates come from your phone's Settings' is unsupported and partly contradicts the source (notifications are a valid route). For the Data Lead's list.",
     "fix": "Replace the middle paragraph with a supported, safe line, e.g. 'Updates are usually a good idea because they help keep your phone secure. If the message appeared on a website or in a text with a link, don't tap it.' Remove the sentence 'Real updates come from your phone's Settings.' Keep the single iPhone-or-Android question."},
    {"id": "tr033-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr033-d", "required_actions": _A33, "covered": [True, True, True, True],
     "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'On some phones this is called **System update** or is in a different spot.' -> 'System update' is not on the page."],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Unsupported label 'System update'. Final reply has a doubled lead-in ('Otherwise, follow these steps.' then 'Here's how to check for an update.').",
     "fix": "Delete 'or System update' from step 3 (use a general hedge only). Remove the second lead-in 'Here's how to check for an update.' so the reply reads: 'Thanks. If you still see the update notification, you can tap it, then tap its update button. Otherwise, before you start, connect to Wi-Fi and charge the battery to at least 75%. 1. ...'. The notification tap is supported (page: open the notification and tap its update button)."},
]

# ---- Page: https://support.microsoft.com/.../install-windows-updates (tr034) ----
_A34 = ["Select Start, then Settings, then Windows Update (critical)",
        "Select 'Check for Windows updates' (critical)",
        "If updates are available, select 'Download & install' (critical)",
        "If prompted, restart the device to apply the updates"]
_U34 = "'Click **Check for updates**.' -> the page's button is 'Check for Windows updates'."
REVIEWS += [
    {"id": "tr034-a", "required_actions": _A34, "covered": [True, True, True, True],
     "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": [_U34],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Wrong button label in step 4.",
     "fix": "Change step 4 to 'Click **Check for Windows updates**.' Optional: for the error-message line, a second source exists, 'Troubleshoot problems updating Windows' (linked from the cited page); keep the line as a general 'tell me what it says'."},
    {"id": "tr034-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr034-c", "required_actions": _A34, "covered": [True, True, True, True],
     "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": [_U34],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Wrong button label. Doubled lead-in ('Sure, here's the path:' then 'Here's how to check...'). User said they are comfortable with Settings and only want to know where to go, but the reply keeps the beginner-style explanations.",
     "fix": "Change step 4 to 'Click **Check for Windows updates**.' Use one lead-in only. Shorten for this user: 'Sure. Go to **Start**, then **Settings**, then **Windows Update**, and click **Check for Windows updates**. If it finds updates, click **Download & install**. If Windows asks you to restart, do that to finish.' (keep numbered steps only if the writer prefers; drop the Windows-logo explanation and the long lead-in)."},
    {"id": "tr034-d", "required_actions": _A34, "covered": [True, True, True, True],
     "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": [_U34],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Wrong button label. Doubled lead-in ('Thanks. Here's how to install the updates.' then 'Here's how to check for updates and install them.').",
     "fix": "Change step 4 to 'Click **Check for Windows updates**.' Remove one of the two lead-in sentences, e.g. start 'Thanks. Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.'"},
]

# ---- Page: https://support.google.com/photos/answer/6193313 (tr035) ----
_A35 = ["Open the Google Photos app (critical)",
        "Sign in to your Google Account (critical)",
        "Tap your Profile picture or Initial at the top right (critical)",
        "Tap Photos settings, then Backup (critical)",
        "Turn on Backup (critical)",
        "Have a good internet connection; Wi-Fi works best (non-critical)"]
_C35 = [True, True, True, True, True, False]
_F35 = ("Add a short line before the steps: 'Use Wi-Fi if you can, because it works best.' (page: 'You need a good internet connection. Wi-Fi works best.') "
        "After step 6 add a what-you-see cue from the page: 'At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**.'")
REVIEWS += [
    {"id": "tr035-a", "required_actions": _A35, "covered": _C35, "needs_clarification": False,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Missing the internet/Wi-Fi requirement (non-critical); no cue for what the user will see after turning Backup on although the page gives one.",
     "fix": _F35},
    {"id": "tr035-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr035-c", "required_actions": _A35, "covered": _C35, "needs_clarification": False,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Missing Wi-Fi/internet line; no what-you-see cue; doubled lead-in ('Google Photos can save a copy online:' then 'You can use the Google Photos app to save copies...').",
     "fix": "Keep the sympathetic opening, then use only one lead-in, e.g. 'I'm sorry about those pictures. Let's make sure your new ones are kept safe. You can use the **Google Photos** app to save copies of your photos to your Google Account.' Delete the line 'Google Photos can save a copy online:'. " + _F35},
    {"id": "tr035-d", "required_actions": _A35, "covered": _C35, "needs_clarification": False,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Missing Wi-Fi/internet line; no what-you-see cue; doubled lead-in ('On Android, Google Photos can do this for you.' then 'You can use the Google Photos app to save copies...').",
     "fix": "Merge into one lead-in: 'Great. On Android you can use the **Google Photos** app to save copies of your photos to your Google Account.' " + _F35},
]

# ---- Page: https://support.microsoft.com/.../add-or-install-a-printer-in-windows (tr036) ----
_A36 = ["Turn the printer on; plug in cable if wired; wireless/network printer must be on the same network as the PC (critical)",
        "Start > Settings > Bluetooth & devices > Printers & scanners (critical)",
        "Check whether the printer is already in the installed list; if so you are finished (non-critical)",
        "If not listed, select Add a printer & scanner, then Add device (critical)",
        "Wait a few minutes for the list to fill (critical)",
        "Select Add Device next to your printer (Windows may add it without this click) (critical)",
        "If not listed: 'The printer that I want isn't listed', then 'Add a new device manually' (non-critical)"]
_C36 = [True, True, False, True, True, True, True]
_U36 = ["'It takes about five minutes.' -> page gives no total time; it only says wait 'a few minutes' for the list to populate.",
        "'Some printers install by themselves after step 4.' -> page says a wired printer often installs automatically once connected and powered on, i.e. BEFORE opening Printers & scanners; placement after step 4 is wrong."]
_F36 = ("Replace 'It takes about five minutes.' with 'It can take a few minutes.' Add a step after opening Printers & scanners: 'Look at the list of printers. If your printer is already there, you're finished.' "
        "Move 'Some printers install by themselves' to the First section: 'Some printers, especially ones with a cable, install by themselves once they are plugged in and on. Check the list first.' "
        "Number the later steps accordingly. Optional second source for problems: 'Fix printer connection and printing problems in Windows' (linked from the cited page).")
REVIEWS += [
    {"id": "tr036-a", "required_actions": _A36, "covered": _C36, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U36,
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Unsupported time estimate, misplaced auto-install statement, and the 'already listed? you're finished' check is missing.",
     "fix": _F36},
    {"id": "tr036-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr036-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Clarifying reply asks two questions (two question marks): what the printer won't do, and what it prints from.",
     "fix": "Ask ONE question with one question mark, e.g. 'It looks like your message got cut off. What happens when you try to set up the new printer: does it not **turn on**, not **connect**, or not **print**?' Do not add the second question about computer or phone."},
    {"id": "tr036-d", "required_actions": _A36, "covered": _C36, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U36,
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Unsupported time estimate, misplaced auto-install statement, missing 'already listed' check, and doubled lead-in ('Great, here's how to add it...' then 'Here's how to add your new printer.').",
     "fix": _F36 + " Also keep only one lead-in: 'Great, here's how to add the printer to your Windows 11 laptop.'"},
]

# ---- Page: https://support.google.com/mail/answer/6584 (tr037) ----
_A37 = ["Open the Gmail app (critical)", "Tap Compose at the bottom right (critical)",
        "Tap Attach at the top right (critical)", "Choose the type in the menu, e.g. Photos (critical)",
        "Pick the photo(s); up to five at a time (critical)"]
REVIEWS += [
    {"id": "tr037-a", "required_actions": _A37, "covered": [True]*5, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'It looks like a **paperclip**.' -> the page only labels the icon 'Attach' (alt text 'Attach'); no paperclip description.",
                            "'tap the close icon (**X**)' -> the page says tap 'Close' to the right of the attachment name; it does not describe an X.",
                            "'Files over 25 MB are added as a Google Drive link instead.' -> page: for personal Gmail accounts the limit is 25 MB and if the attachment is over the limit Gmail removes it and adds a Drive link; stating it per file and for all accounts is imprecise."],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Reviewed by a person, but icon descriptions (paperclip, X) are not supported by the page. For the Data Lead's list.",
     "fix": "Step 3: 'Tap **Attach** at the top right.' (delete 'It looks like a paperclip'). Removal line: 'tap **Close** to the right of its name.' Limit line: 'If the attachments are over 25 MB (personal Gmail accounts), Gmail adds them as a Google Drive link instead.'"},
    {"id": "tr037-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "The clarifying reply bundles two questions in one sentence (phone or computer, and which email app).",
     "fix": "Ask one question only, e.g. 'I can help. Which email app are you using, for example **Gmail** on your phone?'"},
    {"id": "tr037-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Two questions: what to attach, and where.",
     "fix": "Ask one question: 'Happy to help. **Where do you want to attach something**: in an email, in a text message, or somewhere else?' Remove the 'what would you like to attach' question."},
    {"id": "tr037-d", "required_actions": _A37, "covered": [True]*5, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'Very large files are added as a Google Drive link instead, which the person can still open.' -> 'which the person can still open' is not on the page, and 'the person' is odd phrasing; page says over the limit (25 MB for personal Gmail) the attachment is removed and added as a Drive link.",
                            "'tap the close icon (**X**)' -> the page says tap 'Close'; no X described."],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Unsupported claims in the closing paragraph; doubled lead-in ('Thanks, here's how in the Gmail app.' then 'Here's how.').",
     "fix": "Use one lead-in: 'Thanks, here's how in the Gmail app. It takes about a minute.' Change the last paragraph to: 'If you added the wrong photo, tap **Close** to the right of its name to remove it. If the attachments are over 25 MB, Gmail adds them as a Google Drive link instead.'"},
]

# ---- Page: https://support.google.com/accounts/answer/7682439 (tr038) ----
_A38 = ["Start recovery with the link 'Follow the steps to recover your Google Account or Gmail' (accounts.google.com/signin/recovery) (critical)",
        "Answer the questions that confirm the account is yours, as accurately as you can; wrong guesses do not end the process (critical)",
        "When prompted, reset the password to a strong one not used with this account before (critical)",
        "Never share passwords or verification codes; Google does not help with sign-in by phone (safety)",
        "If recovery info was changed, it can take up to 7 days; try again after a few days (non-critical)"]
_C38 = [False, True, True, True, True]
_U38 = ["'Go to Google's **account recovery** page.' -> gives no link or address, so a low-confidence user has no starting point; the page links to accounts.google.com/signin/recovery.",
        "'Enter the details it asks for, starting with your Gmail address.' -> 'starting with your Gmail address' is not on the page; it only says you will be asked questions to confirm the account is yours."]
_F38 = ("Step 1: 'Go to **accounts.google.com/signin/recovery** (Google's account recovery page).' "
        "Step 2: delete 'starting with your Gmail address'; say 'Answer the questions it asks to show the account is yours. Answer as accurately as you can; if you're not sure, give your best guess. Wrong guesses don't end the process.' "
        "Last line: 'If you recently changed your recovery info, it can take up to 7 days to take effect, so try again after a few days.'")
REVIEWS += [
    {"id": "tr038-a", "required_actions": _A38, "covered": _C38, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U38,
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "No link to the recovery page (no starting point); unsupported 'starting with your Gmail address'.",
     "fix": _F38},
    {"id": "tr038-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Asks two things (which email, and what is going wrong).",
     "fix": "Ask one question: 'That's stressful, but it can usually be fixed. **Which email do you use**, for example Gmail, which ends in @gmail.com?' Remove the 'what's going wrong' question."},
    {"id": "tr038-c", "required_actions": _A38, "covered": _C38, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U38,
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "No link to the recovery page; unsupported 'starting with your Gmail address'; doubled lead-in ('You can reset the password:' then 'You can get back in through Google's account recovery.').",
     "fix": _F38 + " Use one lead-in only: 'That happens a lot when a phone stays signed in for years. You can get back in through Google's account recovery.'"},
    {"id": "tr038-d", "required_actions": _A38, "covered": _C38, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U38,
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "No link to the recovery page; unsupported 'starting with your Gmail address'; doubled lead-in ('Thanks. You can reset it through Google's account recovery.' then 'You can get back in through Google's account recovery.').",
     "fix": _F38 + " Use one lead-in only: 'Thanks. You can get back in through Google's account recovery.'"},
]

# ---- Page: https://consumer.ftc.gov/.../scammers-use-ai-enhance-their-family-emergency-schemes (tr039) ----
_A39 = ["Do not trust the voice; call the person who supposedly contacted you to verify (critical)",
        "Use a phone number you know is theirs, not one from the call (critical)",
        "If you can't reach them, contact them through another family member or their friends (critical)",
        "Know the red flag: scammers want payment in hard-to-recover ways: wire money, cryptocurrency, gift cards (critical)",
        "Report the scam to the FTC at ReportFraud.ftc.gov (non-critical)"]
_U39 = ["'**Hang up.** You don't need to argue or explain.' -> the page never says to hang up (only 'Call the person who supposedly contacted you and verify the story').",
        "'**Warning signs of this scam:** an urgent emergency, pressure to act fast...' -> the page does not list urgency or pressure as warning signs; its warning sign is payment by wire, crypto, or gift card."]
_F39 = ("Remove the 'Hang up' step and start the list with the sourced action: '1. **Don't trust the voice**, even if it sounds like her. Call your granddaughter on a phone number you know is hers, not a number from the call.' "
        "Then '2. If you can't reach her, try another family member or her friends.' In the warning-signs line keep only the payment red flag: 'Scammers ask you to pay in ways that make it hard to get your money back: wire money, cryptocurrency, or gift cards.' Remove 'an urgent emergency, pressure to act fast'. "
        "No second official source for 'hang up' was found; do not add it. Keep 'don't send any money yet' first.")
REVIEWS += [
    {"id": "tr039-a", "required_actions": _A39, "covered": [True]*5, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U39,
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Two claims not on the cited page ('Hang up'; urgency/pressure as warning signs).", "fix": _F39},
    {"id": "tr039-b", "required_actions": [], "covered": [], "needs_clarification": False,
     "gates": {"source": "pass", "safety": "fail", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 0, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "The user already said someone called asking for money for the granddaughter. Verification steps do not depend on how the money was to be sent, so no clarification is needed. The reply delays the protective action behind a question and has no 'don't send money' line (G2). It also asks two things in one sentence.",
     "fix": "Lead with the protective action, as tr041-b does, then ask ONE question: 'I'm glad you asked before doing anything. **Please don't send any money yet.** Have you already sent anything, or are you still deciding?' Do not ask about the payment method and do not give steps in this reply (this keeps the missing-info shape)."},
    {"id": "tr039-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Compound clarifying question (what the caller said, and whether they asked for money or personal information). Also no light protective line while the situation is unknown.",
     "fix": "Ask one question: 'I'm happy to help you figure it out. Please don't send money or share any codes or personal details until we check. **What did the caller say?**'"},
    {"id": "tr039-d", "required_actions": _A39, "covered": [True]*5, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U39,
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Same unsupported claims in the final reply ('Hang up'; urgency/pressure as warning signs). Earlier assistant turn asks two things (style only).", "fix": _F39},
]

# ---- Page: https://consumer.ftc.gov/.../think-text-message-usps-it-could-be-scam (tr040) ----
_A40 = ["Do not give information or click any link in the message (critical)",
        "To check a real delivery, go to the online retail site or account you ordered from, not the link in the text (critical)",
        "Report the text with the messaging app's report-junk/spam option (critical)",
        "If there is no report option, forward the message to 7726 (critical)",
        "Optionally tell the FTC at ReportFraud.ftc.gov (non-critical)"]
_U40_DEL = "'4. Then delete it.' -> the page gives no advice to delete the message."
_U40_BANK = "'If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.' -> the page says nothing about contacting a bank or card company; it only warns that payments and entered details go to the scammer."
_F40 = ("Delete step 4 ('Then delete it.'). Replace the last paragraph with a non-instructional offer: 'If you already clicked the link or typed in any information, tell me and we'll look at what to do next.' (do not give bank or card steps, they are not on the page). "
        "Step 3: 'Report the text. Use your messaging app's report junk or spam option. If there isn't one, forward the text to **7726**. You can also tell the FTC at **ReportFraud.ftc.gov**.'")
REVIEWS += [
    {"id": "tr040-a", "required_actions": _A40, "covered": [True, True, True, True, False], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U40_DEL, _U40_BANK],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Unsupported 'delete it' step and bank advice; optional ReportFraud.ftc.gov report missing.",
     "fix": _F40},
    {"id": "tr040-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "fail", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Scam-safety reply asks a question without first giving the protective action (G2: protective action must not wait behind a question). tr040-c does include it.",
     "fix": "Add a protective line before the single question: 'Let's check it together. For now, **please don't click any link or give any information** in that text. **What does the text ask you to do?**' Keep it to one question; the examples after the question are optional."},
    {"id": "tr040-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Two questions (two question marks): 'Do you mean ... a link in it?' and 'What does the text ask you to do?'",
     "fix": "Keep the protective line and ask one question: 'If you got a text that looks like it's from USPS with a link in it, please **don't click the link** yet. **What does the text ask you to do?**'"},
    {"id": "tr040-d", "required_actions": _A40, "covered": [True]*5, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'A small fee plus a link is a very common sign of a scam' -> the page mentions no fee amount or redelivery charge; it lists lures like 'unpaid postage, a missed delivery' and says if you pay the money goes to the scammer.",
                            _U40_DEL, _U40_BANK],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Reviewed by a person, but the final reply has the unsupported 'delete it' step, bank advice, and a fee claim not on the page. For the Data Lead's list.",
     "fix": "Open with: 'Thanks. A text about a missed delivery or unpaid postage with a link is a common scam lure, and if you pay, the money goes to the scammer.' Then apply this: " + _F40 + " (the ReportFraud.ftc.gov sentence is already in step 3, keep it)."},
]

# ---- Page: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams (tr041) ----
_A41 = ["Do not buy the gift cards: no real business or government agency demands gift card payment (critical)",
        "Check with the person who supposedly asked, using a number you already know (critical)",
        "If cards were already given: report to the gift card company right away (critical)",
        "Ask the company for your money back and whether it can freeze the funds (critical)",
        "Keep the gift card and store receipt; give the card number and receipt to the company (critical)",
        "Report to the FTC at ReportFraud.ftc.gov (non-critical)",
        "Contact info for gift card companies is on the FTC page; if not listed, check the card or search online for the issuer (non-critical)"]
_U41 = "'Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers' -> the page says no real business or government agency will ask; it does not say people you know never do (it warns scammers pose as friends or relatives and says to contact them to check)."
_F41 = ("Change the sentence to: 'Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know.' "
        "In the 'already bought' section add: 'Give the company the card number and the receipt.' and 'The FTC's gift card scam page lists phone numbers for major gift card companies. If yours isn't listed, look on the card or search online for the company that issued it.'")
REVIEWS += [
    {"id": "tr041-a", "required_actions": _A41, "covered": [True, True, True, True, False, True, False], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U41],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Overbroad claim 'people you know don't ask'; missing 'give the card number and receipt to the company' and how to find the company's contact details.",
     "fix": _F41},
    {"id": "tr041-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Protective line comes first (good), but the reply asks two questions: who is asking, and whether cards were already bought or sent.",
     "fix": "Keep the first two sentences, then ask only: '**Have you already bought or sent any gift cards?**' Drop 'Who is asking'."},
    {"id": "tr041-c", "required_actions": _A41, "covered": [True, True, True, True, False, True, False], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "fail", "duplicate": "pass"}, "unsupported_claims": [_U41],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 1, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "The user says a friend ALREADY bought cards; the urgent protective steps (contact the gift card company right away) are placed at the very end, after the 'don't buy' steps meant for someone who has not acted (G2 order). The 'already bought' bullets are written to 'you', not the friend. Plus the overbroad 'people you know' claim and missing items.",
     "fix": "Open with: 'You're not being rude by checking, and a real pastor would understand. Your friend should act first: she should **contact the gift card company right away**, tell them the cards were used in a scam, ask for the money back, and ask if they can freeze it. She should give them the card numbers and receipt, and report it at ReportFraud.ftc.gov.' Then give the 'for you' steps (don't buy, check with the pastor on a number you already have). " + _F41},
    {"id": "tr041-d", "required_actions": _A41, "covered": [True, True, True, True, False, True, False], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U41],
     "scores": {"steps": 1, "ask_or_answer": 2, "constraints": 1, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Overbroad 'people you know' claim; 'Here's what to do:' appears twice; the user said they have bought nothing, yet the reply keeps the long 'If you already bought cards' section (extra text, ignores the user's answer); missing items.",
     "fix": "Remove the first 'Here's what to do:' and the whole 'If you already bought cards and shared the numbers' section (replace with one line: 'If you ever do share card numbers, tell me right away and call the gift card company.'). " + _F41},
    {"id": "tr041-r", "required_actions": ["Contact the gift card company right away (critical)", "Tell them it was a scam and ask for money back; ask whether the funds can be frozen (critical)",
                                           "Keep the cards and store receipt; give card number and receipt to the company (critical)", "Report to the FTC at ReportFraud.ftc.gov (non-critical)",
                                           "Find the company's contact info on the FTC page, or on the card / online if not listed (non-critical)"],
     "covered": [True, True, True, True, True], "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'take a photo of both' -> not on the page.",
                            "'**Tell your church office**, so they can warn other members, and let your pastor know his email may have been hacked.' -> not on the page; the hacked-email claim is a guess.",
                            "Earlier assistant turn: 'people you know don't ask to be paid with gift card numbers' -> overbroad, see tr041-a."],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Reviewed by a person, but the final reply has steps not on the page (photo, church office, 'pastor's email may have been hacked'), and the earlier turn has the overbroad claim. For the Data Lead's list.",
     "fix": "Step 2: delete 'and take a photo of both'; say 'Keep the cards and the store receipt. The company will want the card numbers and the receipt.' Step 5: replace with 'Check with your pastor by calling a phone number you already have, to make sure the email was not really from him.' Delete the church-office and 'hacked' wording. In the earlier turn apply the _F41 sentence change (remove 'people you know')."},
]

# ---- Page: https://support.apple.com/en-us/108380 (tr042) ----
_A42 = ["Open Settings and tap your name (critical)", "Tap Family, then tap Continue (critical)",
        "Follow the onscreen instructions to create the group and invite family members (critical)",
        "To invite later: Settings > Family > Add Member button > Invite Others (adult, or child who already has a Child Account) (critical)",
        "Complete the remaining prompts (parental controls, location sharing, etc.) (non-critical)",
        "Invitee accepts on their own device (email/text invitation or Settings) (non-critical)",
        "Resend: Settings > Family > tap the person's name > Resend Invitation (non-critical)"]
_C42 = [True, False, True, True, True, True, True]
_U42 = ["'tap the **add member** button (it has a plus sign)' -> the page calls it the 'Add Member' button and shows an icon, but never describes a plus sign.",
        "'tap **your name** at the top' -> 'at the top' is not stated on the page."]
_F42 = ("Step 2: 'Tap **Family**, then tap **Continue**.' Step 1: delete 'at the top'. Step 5: 'Tap the **Add Member** button.' (delete the plus-sign description). "
        "Do not repeat 'Settings, then Family' as a new first step after step 3 if the writer merges the group setup and invitation (page: the onscreen steps create the group and invite family members).")
REVIEWS += [
    {"id": "tr042-a", "required_actions": _A42, "covered": _C42, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U42,
     "scores": {"steps": 0, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "The 'Continue' tap after Family is missing, which is a required step for creating the group; plus-sign and 'at the top' claims are not on the page.",
     "fix": _F42},
    {"id": "tr042-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Two questions (what to share, and iPhone or Android).",
     "fix": "Ask one question: 'There are a few ways to do that. Is your phone an **iPhone** or an **Android** phone?' Remove the 'what would you like to share' question."},
    {"id": "tr042-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr042-d", "required_actions": _A42, "covered": _C42, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U42,
     "scores": {"steps": 0, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Missing the 'Continue' tap after Family; plus-sign and 'at the top' claims not on the page. Earlier assistant turn asks two things (style only).",
     "fix": _F42},
]

# ---- Page: https://support.google.com/contacts/answer/1069522 (tr043) ----
_A43 = ["Open the Contacts app (critical)", "Tap the Add icon at the bottom right (critical)",
        "Enter the contact's name and phone number (critical)", "Tap Save (critical)"]
_U43 = "'Now the name will show up when the office calls you' -> not on the page (it says nothing about caller display); in the follow-up example the user never mentioned a doctor's office."
REVIEWS += [
    {"id": "tr043-a", "required_actions": _A43, "covered": [True]*4, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U43.split(' ->')[0] + " -> not on the page, which says nothing about how calls are displayed."],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Unsupported claim about caller display.",
     "fix": "Change the closing sentence to 'Now you can find the number in Contacts.' (delete 'the name will show up when the office calls you')."},
    {"id": "tr043-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr043-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr043-d", "required_actions": _A43, "covered": [True]*4, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U43],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 1, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Unsupported caller-display claim, and it assumes a doctor's office although the user only asked how to save a phone number.",
     "fix": "Change the closing sentence to 'Now you can find the number in Contacts.' Keep 'Dr. Smith's Office' only as an example name ('Type a name, like **Mom** or **Dr. Smith's Office**.') and remove any wording that assumes the number is an office."},
]

# ---- Page: https://support.apple.com/en-us/111104 (tr045) ----
_A45 = ["Open the Phone app and tap Recents (critical)",
        "Tap the number you want to block (in Classic view tap the Info button instead) (critical)",
        "Scroll down and tap Block Caller (critical)"]
_U45_CONF = "'5. Confirm if asked.' -> the page's Phone-app steps have no confirmation step."
_U45_I = "'a small **\"i\"** in a circle' -> the page says 'Info button' (Classic view) and does not describe its look."
_F45 = ("Delete step 5. In step 3 say: 'Tap the number. (In Classic view, tap the **Info** button next to it instead.)' "
        "Everything else (Recents, Block Caller, caller not told, voicemail saved with no notification) matches the page.")
REVIEWS += [
    {"id": "tr045-a", "required_actions": _A45, "covered": [True]*3, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U45_CONF, _U45_I],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Invented confirmation step; unsupported icon look.", "fix": _F45},
    {"id": "tr045-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr045-c", "required_actions": _A45, "covered": [True]*3, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"},
     "unsupported_claims": ["'5. If a message asks you to confirm, tap **Block Contact**.' -> on the page 'Block Contact' appears only in the iOS 26 Settings flow, not the Phone app steps.", _U45_I],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Reviewed by a person, but step 5 ('Block Contact') is not part of the Phone-app steps on the page, and the icon description is unsupported. For the Data Lead's list.",
     "fix": _F45},
    {"id": "tr045-d", "required_actions": _A45, "covered": [True]*3, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [_U45_CONF, _U45_I],
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 1, "realistic_user": 2},
     "decision": "revise",
     "reasons": "Invented confirmation step; unsupported icon look; doubled lead-in ('Here's how to block it on your iPhone.' then 'You can block that number from your list of recent calls.').",
     "fix": _F45 + " Use one lead-in: 'Thanks. You can block that number from your list of recent calls.'"},
]

# ---- Page: https://support.google.com/phoneapp/answer/6325463 (tr046) ----
_A46 = ["Open the Phone app (critical)", "Tap More, then Call history (critical)",
        "Tap a call from the number you want to block (critical)", "Tap Block / report spam (critical)"]
_U46 = ["'Tap the **More** menu (three dots)' -> the page only labels the icon 'More' (alt text 'More'); 'three dots' is not stated.",
        "'5. Confirm if asked.' -> the page gives no confirmation step after Block / report spam."]
_F46 = "Step 2: 'Tap **More**, then choose **Call history**.' (delete 'three dots'). Delete step 5. Keep the line about visual voicemail and the hedge about the Phone app looking different."
REVIEWS += [
    {"id": "tr046-a", "required_actions": _A46, "covered": [True]*4, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U46,
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Unsupported 'three dots' and invented confirmation step.", "fix": _F46},
    {"id": "tr046-b", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "keep", "reasons": "", "fix": ""},
    {"id": "tr046-c", "required_actions": [], "covered": [], "needs_clarification": True,
     "gates": {"source": "pass", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": [],
     "scores": {"steps": "NA", "ask_or_answer": 1, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Two questions (calling or texting, and iPhone or Android).",
     "fix": "Ask one question: 'Sure, I can help you block it. Is your phone an **iPhone** or an **Android** phone?'"},
    {"id": "tr046-d", "required_actions": _A46, "covered": [True]*4, "needs_clarification": False,
     "gates": {"source": "fail", "safety": "pass", "duplicate": "pass"}, "unsupported_claims": _U46,
     "scores": {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
     "decision": "revise", "reasons": "Unsupported 'three dots' and invented confirmation step.", "fix": _F46},
]
