# Reviews for batch ex6, round 1. Independent reviewer.
S_ALL2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
PASS = {"source": "pass", "safety": "pass", "duplicate": "pass"}
SRC_FAIL = {"source": "fail", "safety": "pass", "duplicate": "pass"}


def s(**kw):
    d = dict(S_ALL2)
    d.update(kw)
    return d


def rec(id, ra, cov, nc, gates, uns, sc, dec, reasons="", fix=""):
    return {"id": id, "required_actions": ra, "covered": cov, "needs_clarification": nc, "gates": gates,
            "unsupported_claims": uns, "scores": sc, "decision": dec, "reasons": reasons, "fix": fix}


REVIEWS = []

# ---------- tr076: QR iPhone (support.apple.com/en-us/102680) ----------
RA_076 = [
    "Open the Camera app (critical)",
    "Hold the iPhone so the QR code appears on screen (critical)",
    "Tap the link that appears to open the content (critical)",
    "Alternative: open Control Center and tap Scan Code (the button must have been added via Add a Control)",
]
FIX_076_DUP = ("Remove the pasted lead-in. Start the reply with 'That square is a QR code, and your iPhone can read it with the Camera app.' "
               "then go straight to the numbered steps. Do not repeat 'Your iPhone camera can read QR codes. It takes a few seconds.' "
               "Also change the Control Center line to 'If you don't see **Scan Code** in Control Center, touch and hold the background of Control Center, tap **Add a Control**, then tap **Scan Code**.' or drop the Control Center line.")
REVIEWS += [
    rec("tr076-a", RA_076, [True, True, True, True], False, PASS, [], s(), "keep"),
    rec("tr076-b", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr076-c", RA_076, [True, True, True, True], False, PASS, [],
        s(plain=1), "revise",
        "Lead-in is pasted twice: 'Next time, try this:' followed by 'Your iPhone camera can read QR codes. It takes a few seconds.' right after 'your iPhone can read it with the camera.' Also tells the user 'The restaurant's menu will open' although it is a statement, fine; main issue is the duplicated intro.",
        FIX_076_DUP),
    rec("tr076-d", RA_076, [True, True, True, True], False, PASS, [],
        s(plain=1, realistic_user=2), "revise",
        "Final reply says 'The restaurant's menu will open' and 'ones printed on the restaurant's own menu or table' but this user never mentioned a restaurant; carried over from tr076-a. Also 'Thanks.' then 'Your iPhone camera can read QR codes' is slightly repetitive.",
        "Replace 'The restaurant's menu will open.' with 'The page or app that the code is for will open.' and replace the last line with 'Only open QR codes you trust, like ones printed by a business you know.' Keep the rest."),
]

# ---------- tr077: QR Android (support.google.com/camerafromgoogle/answer/12033278) ----------
RA_077 = [
    "Open Camera from Google (critical)",
    "Use QR mode (tap QR) or the default photo mode; scanning does not work in portrait or video mode (critical)",
    "Point the camera at the QR code (critical)",
    "Tap the banner that appears to open the page/app (critical)",
]
RA_077_PIXEL = [
    "Launch Camera (critical)",
    "If scanning is not working: tap the Settings icon, More settings, then make sure Camera scan suggestions is on",
    "Aim the lens at the whole code; no photo needed (critical)",
    "Wait for a bubble or link to appear (critical)",
    "Tap the link to open it (critical)",
    "Alternative: swipe down for Quick Settings and tap Scan QR code",
]
REVIEWS += [
    rec("tr077-a", RA_077, [True, True, True, True], False, PASS, [], s(), "keep"),
    rec("tr077-b", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr077-c", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions (two question marks): 'Is the QR code not scanning, or is it opening something you didn't expect? And is your phone an iPhone or an Android phone?'",
        "Replace with exactly one question and no steps: 'It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?'"),
    rec("tr077-d", RA_077_PIXEL, [False, False, True, False, True, False], False, SRC_FAIL,
        ["'Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.' -> this is from the Camera from Google page, which says Pixel Camera users should use the separate Pixel help page; the Pixel page has no photo/QR mode step",
         "'When a banner appears on the screen, tap it' -> Pixel page says a bubble or link appears",
         "'These steps are for Google's Camera app... Other phone brands work in a similar way' -> user named a Pixel, so these steps are not the Pixel steps"],
        s(steps=1, constraints=1), "revise",
        "The user said Pixel. The cited page explicitly sends Pixel Camera users to a different Help Center, so the Pixel-specific steps are not from the cited source.",
        "Add source https://support.google.com/pixelphone/answer/16561572?hl=en and rewrite the final reply for a Pixel: 1 Open the **Camera** app. 2 Point the lens at the code so the whole code is on the screen (no need to take a photo). 3 Wait a moment for a bubble or link to appear, then tap it. Then: 'If nothing appears, tap the **Settings** icon in Camera, tap **More settings**, and make sure **Camera scan suggestions** is on.' Optionally add: 'You can also swipe down from the top and tap **Scan QR code**.' Drop the 'Google's Camera app / other brands' paragraph and the photo/portrait/video mode lines."),
]

# ---------- tr078: Medical ID iPhone (support.apple.com/en-us/105072) ----------
RA_078 = [
    "Open Health and select the Summary tab (critical)",
    "Tap your profile picture in the upper corner (critical)",
    "Tap Medical ID (critical)",
    "Turn on Show When Locked so it is available from the Lock Screen (critical)",
    "Tap Edit or Add beside a field such as Allergies and enter details (critical)",
    "Tap Done (critical)",
    "Emergency contacts: Edit next to Emergency Contacts, plus button next to Add Emergency Contact, choose a contact, enter relationship, tap Done",
]
UNSUP_078 = [
    "'Tap **Summary** at the bottom.' -> page says only 'select the Summary tab'; 'at the bottom' is not on the page",
    "'Tap **Edit**.' (separate step before Show When Locked) -> page does not list a separate Edit step before Show When Locked; Edit appears beside a field/Emergency Contacts",
]
FIX_078 = ("Change step 2 to 'Tap **Summary**.' and step 3 to 'Tap your **profile picture** in the upper corner.' Remove the standalone step 'Tap **Edit**' before Show When Locked (page order is: Medical ID, turn on Show When Locked, then tap Edit or Add beside a field such as Allergies and type, then Done). "
           "At the end of the emergency contacts paragraph add 'Then tap **Done**.' and change 'tap the **plus** button' to 'tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you.' Keep the privacy line.")
REVIEWS += [
    rec("tr078-a", RA_078, [True, True, True, True, True, True, False], False, SRC_FAIL, UNSUP_078, s(steps=1), "revise",
        "Emergency contacts part ends without the final Done; two small unsupported details (position of Summary, separate Edit step).", FIX_078),
    rec("tr078-b", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr078-c", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr078-d", RA_078, [True, True, True, True, True, True, False], False, SRC_FAIL, UNSUP_078, s(steps=1), "revise",
        "Same problems as tr078-a in the final reply.", FIX_078),
]

# ---------- tr079: emergency info Android (support.google.com/android/answer/9319337) ----------
RA_079 = [
    "Open the Safety app (critical)",
    "Sign in to your Google Account (critical)",
    "Tap Your info (critical)",
    "Medical information: tap Medical information, then an item such as allergies or medications to update it (critical)",
    "Emergency contacts: tap Emergency contacts, then Add contact, choose an existing contact (critical)",
    "Lock screen access: tap Emergency info access, then Show when locked (critical)",
]
REVIEWS += [
    rec("tr079-a", RA_079, [True] * 6, False, PASS, [], s(), "keep"),
    rec("tr079-b", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr079-c", RA_079, [True] * 6, False, PASS, [], s(), "keep"),
    rec("tr079-d", RA_079, [True] * 6, False, PASS, [], s(), "keep"),
]

# ---------- tr080: app notifications iPhone (support.apple.com/en-us/120681) ----------
RA_080 = [
    "Open Settings and tap Apps (critical)",
    "Tap the app (critical)",
    "Tap Notifications (critical)",
    "Switch Allow Notifications off (critical)",
    "If Notifications does not appear, the app may not be able to send notifications",
]
UNSUP_080 = ["'it means the app can't send notifications' -> page says only that the app 'may not be able to send notifications at all'"]
FIX_080 = "Change the last line to 'If you don't see **Notifications** for that app, the app may not be able to send notifications.' Leave everything else unchanged."
REVIEWS += [
    rec("tr080-a", RA_080, [True] * 5, False, SRC_FAIL, UNSUP_080, s(), "revise",
        "One overstated claim, stronger than the page.", FIX_080),
    rec("tr080-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions in one reply ('Which app is sending them...? And is your phone an iPhone or an Android phone?'). The app name does not change the steps; only the phone type does.",
        "Replace with exactly one question and no steps: 'I can help with that. Is your phone an **iPhone** or an **Android** phone?'"),
    rec("tr080-c", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions ('popping up too often, or stopped showing up?' and 'which app is it?') and neither asks for the phone type, which is what changes the steps; the user message is too cut off to know the problem.",
        "Replace with exactly one question and no steps: 'It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?'"),
    rec("tr080-d", RA_080, [True] * 5, False, SRC_FAIL, UNSUP_080, s(), "revise",
        "Same overstated claim in the final reply. (Earlier assistant turn asks two questions; style only.)", FIX_080),
]

# ---------- tr081: app notifications Android (support.google.com/android/answer/9079661) ----------
RA_081 = [
    "Option 1: Open Settings (critical)",
    "Tap Notifications, then App notifications (some phones: Apps & notifications)",
    "Find the app under Most recent; for more apps open the dropdown and tap All apps",
    "Tap the app and turn its notifications off (critical)",
    "Option 2: swipe down from top; touch and hold the notification; tap the Settings icon; turn off All notifications",
    "Menu names can vary by phone",
]
UNSUP_081 = ["'open the menu at the top and choose all apps' -> page says 'open the dropdown and tap All apps' under 'Most recent'; 'menu at the top' is not on the page"]
FIX_081 = "In Option 1 step 3 replace 'open the menu at the top and choose all apps' with 'open the dropdown and tap **All apps**'. Leave everything else unchanged."
REVIEWS += [
    rec("tr081-a", RA_081, [True] * 6, False, SRC_FAIL, UNSUP_081, s(), "revise", "One unsupported position/label detail.", FIX_081),
    rec("tr081-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions in one reply ('Which app is it, and is your phone an iPhone or an Android phone?'). The app name does not change the steps.",
        "Replace with exactly one question and no steps: 'Yes, you can turn off an app's notifications. Is your phone an **iPhone** or an **Android** phone?'"),
    rec("tr081-c", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions (alerts from an app vs emails or texts, and iPhone vs Android).",
        "Replace with exactly one question and no steps: 'That sounds tiring. Is your phone an **iPhone** or an **Android** phone?'"),
    rec("tr081-d", RA_081, [True] * 6, False, SRC_FAIL, UNSUP_081, s(), "revise",
        "Same unsupported detail in the final reply.", FIX_081),
]

# ---------- tr082: zoom Chrome desktop (support.google.com/chrome/answer/96810) ----------
RA_082 = [
    "Open Chrome on the computer",
    "At the top right, click More (critical)",
    "Next to Zoom, click Zoom in (+) to enlarge or Zoom out to shrink (critical)",
    "Keyboard: Ctrl and + (Command and + on Mac) larger; Ctrl and - smaller",
    "Default zoom for all pages: More > Settings > Appearance > Page zoom, pick an option",
]
UNSUP_082 = ["'the **More** menu (three dots) at the top right' -> page says 'At the top right, click More' and does not describe the icon as three dots"]
FIX_082 = ("Replace 'Click the **More** menu (three dots) at the top right of Chrome.' with 'At the top right of Chrome, click **More**.' "
           "In the last paragraph make it 'click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.' Leave everything else unchanged.")
REVIEWS += [
    rec("tr082-a", RA_082, [True] * 5, False, SRC_FAIL, UNSUP_082, s(), "revise", "Unsupported icon description.", FIX_082),
    rec("tr082-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions (device type, then browser).",
        "Replace with exactly one question and no steps: 'I can help you make them bigger. Are you on a **computer**, a **phone**, or a **tablet**?'"),
    rec("tr082-c", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "The question asked ('just this page or every website') does not change the steps (the reply can give both); the missing detail that does change them is whether this is Chrome on a computer or on a phone/tablet.",
        "Replace with exactly one question and no steps: 'Sure. Are you using Chrome on a **computer**, a **phone**, or a **tablet**?'"),
    rec("tr082-d", RA_082, [True] * 5, False, SRC_FAIL, UNSUP_082, s(), "revise", "Same unsupported icon description in the final reply.", FIX_082),
]

# ---------- tr083: find downloads Windows 11 (support.microsoft.com ... find-my-downloads-in-windows-10) ----------
RA_083 = [
    "Open File Explorer (taskbar, Start menu, or Windows logo key + E) (critical)",
    "In Windows 11 (22H2 and later), click Downloads, pinned under Quick access in the left pane (critical)",
    "If Downloads is missing: select Home, select the Up arrow, right-click Downloads, choose Pin to Quick access",
    "Note: in Windows 11 22H2 and later, known folders no longer appear under This PC",
]
UNSUP_083 = [
    "'You can also find it under **This PC**.' -> contradicted: the page says that in Windows 11 22H2 and later the known folders no longer appear under This PC",
    "'If the folder is sorted by date, your newest download will be near the top.' -> page does not describe sorting",
    "'Click the folder icon on the taskbar' -> page says only 'select it on the taskbar'; the icon is not described",
]
FIX_083 = ("Step 1: 'Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.' Step 2: 'In the list on the left, click **Downloads** (under **Quick access**).' "
           "Delete 'You can also find it under This PC.' Replace step 3 with 'Your downloaded file should be in the list.' (no sorting claim). Optionally add: 'If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.' "
           "Fix the closing line so it matches the user's file.")
REVIEWS += [
    rec("tr083-a", RA_083, [True, True, False, False], False, SRC_FAIL, UNSUP_083, s(steps=1, plain=2), "revise",
        "Contradicts the page on This PC; unsupported sorting claim.", FIX_083),
    rec("tr083-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions ('computer or phone?' and 'Windows or a Mac?').",
        "Replace with exactly one question and no steps: 'Let's find it. Is this on a **Windows computer**, a **Mac**, or a **phone**?'"),
    rec("tr083-c", RA_083, [True, True, False, False], False, SRC_FAIL, UNSUP_083, s(steps=1, plain=1), "revise",
        "Same source problems as tr083-a. Lead-in pasted twice ('It's most likely in your Downloads folder. Here's how to find it:' then 'Files you download usually go to your Downloads folder. Here's how to find it.'). Step 3 says 'your form' and the closing line says 'what the form is called' but the user is looking for an insurance card PDF.",
        FIX_083 + " Also delete the duplicated lead-in (keep only 'It's most likely in your **Downloads** folder. Here's how to find it.') and say 'your insurance card PDF' instead of 'your form'."),
    rec("tr083-d", RA_083, [True, True, False, False], False, SRC_FAIL, UNSUP_083, s(steps=1, plain=2), "revise",
        "Same source problems as tr083-a. Also 'Look for your form' but the user said only 'something I downloaded'.",
        FIX_083 + " Replace 'your form' with 'your file'."),
]

# ---------- tr084: bigger mouse pointer Windows 11 (support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see) ----------
RA_084 = [
    "Select the Start button, then Settings (critical)",
    "Select Accessibility (critical)",
    "Select Mouse pointer & touch (critical)",
    "Choose the pointer size/color options that work best for you (critical)",
]
UNSUP_084 = ["'You can also change the **style** or color' -> page says you can change the color and size of the pointer; 'style' is not named"]
FIX_084 = "Replace step 5 with 'You can also change the pointer's **color** so it stands out more.' (remove 'style'). Leave everything else unchanged."
REVIEWS += [
    rec("tr084-a", RA_084, [True] * 4, False, SRC_FAIL, UNSUP_084, s(), "revise", "One unsupported option name.", FIX_084),
    rec("tr084-b", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr084-c", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr084-d", RA_084, [True] * 4, False, SRC_FAIL, UNSUP_084, s(), "revise", "Same unsupported option name in the final reply.", FIX_084),
]

# ---------- tr085: 2-Step Verification (support.google.com/accounts/answer/185839 ; 7682439) ----------
RA_085 = [
    "Go to myaccount.google.com and open your Google Account (critical)",
    "Select Security & sign-in (critical)",
    "Under How you sign in to Google, select Turn on 2-Step Verification (critical)",
    "Follow the on-screen steps (critical)",
    "Never share verification codes; Google won't call to ask for a code",
    "Work/school accounts: steps may not work; contact your administrator",
]
UNSUP_085 = [
    "'Google may ask you to confirm with your phone when you sign in on a new device.' -> page says Google chooses the second step and mentions phone prompts, but nothing about 'a new device'",
    "'**Never share these codes with anyone**' -> 'these codes' has no antecedent (no code has been mentioned); page says 'Don't share verification codes with anyone, because scammers may try to take over your account. Google won't call you to ask for a code.'",
]
FIX_085 = ("Replace 'After it's on, Google may ask you to confirm with your phone when you sign in on a new device.' with 'After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.' "
           "Replace 'Never share these codes with anyone, even if they say they're from Google.' with 'Never share a verification code with anyone. Google will not call you to ask for one.' Leave the work/school line.")
REVIEWS += [
    rec("tr085-a", RA_085, [True] * 6, False, SRC_FAIL, UNSUP_085, s(plain=1), "revise", "One unsupported detail and a dangling 'these codes'.", FIX_085),
    rec("tr085-b", [], [], True, PASS, [], s(steps="NA"), "keep", "Already read by a person; I agree."),
    rec("tr085-c", [], [], True, PASS, [], s(steps="NA"), "keep"),
    rec("tr085-d", RA_085, [True] * 6, False, SRC_FAIL, UNSUP_085, s(plain=1), "revise", "Same issues in the final reply. (Earlier turn asks two questions; style only.)", FIX_085),
]

# ---------- tr086: phishing email (consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams) ----------
RA_086 = [
    "Do not click links or open attachments (critical)",
    "Contact the company using a phone number or website you know is real, not the email's information (critical)",
    "Forward the email to the Anti-Phishing Working Group at reportphishing@apwg.org",
    "Report it at ReportFraud.ftc.gov, then delete the message",
    "Warning signs: story about a billing/account problem, link to click, generic greeting, company logo",
    "If you clicked a link/opened an attachment: update security software, run a scan; if you gave personal info, go to IdentityTheft.gov",
]
UNSUP_086 = [
    "'the link can lead to a fake website that steals your password' -> page says the link may contain malware; it does not describe a fake website that steals a password",
    "'call your bank using the number on the **back of your card**' -> page says use 'a phone number or website you know is real'; the card is not mentioned",
    "'If you already clicked and typed your password, call your bank right away and change your password.' -> page says nothing like this; for a clicked link it says update security software and run a scan, and if you gave information go to IdentityTheft.gov",
]
FIX_086 = ("Change the second sentence to 'These emails often look real, even with the bank's logo, but a link can carry malware.' "
           "Change step 2 to 'To check your account, contact your bank using a phone number or website you already know is real, not anything from the email.' "
           "Replace the last line with 'If you already clicked a link or opened an attachment, update your computer's security software, run a scan, and remove anything it finds. If you gave out personal information, go to **IdentityTheft.gov** for next steps.'")
REVIEWS += [
    rec("tr086-a", RA_086, [True, True, True, True, True, False], False, SRC_FAIL, UNSUP_086, s(steps=1), "revise",
        "Three unsupported claims; the 'already clicked' advice is not what the page says.", FIX_086),
    rec("tr086-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions in one ('Who does the email say it's from, and what is it asking you to do?').",
        "Keep 'Good thinking to check first. Please don't click anything yet.' then ask exactly one question: '**Who does the email say it's from?**'"),
    rec("tr086-c", [], [], True, {"source": "pass", "safety": "fail", "duplicate": "pass"}, [], s(steps="NA"), "revise",
        "Scam safety: the protective instruction comes after the question ('Who does the email say it's from? And please don't click any links...').",
        "Reorder to put the protective line first: 'It looks like your message got cut off. Please don't click any links in it until we check. **Who does the email say it's from?**'"),
    rec("tr086-d", RA_086, [True, True, True, True, True, False], False, SRC_FAIL, UNSUP_086, s(steps=1), "revise",
        "Same unsupported claims in the final reply.", FIX_086),
]

# ---------- tr087: report spam texts (consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages) ----------
RA_087 = [
    "Report it in the messaging app you use (report junk/spam) (critical)",
    "Forward the message to 7726 (SPAM) so the provider can spot and block similar messages (critical)",
    "Report it to the FTC at ReportFraud.ftc.gov (critical)",
    "Don't click links or reply",
    "Legitimate companies won't ask for account information by text; contact the company using a number or website you know is real",
    "Optional: use the phone's spam filter, the carrier's blocking tools or a call-blocking app",
]
UNSUP_087 = ["'Then delete the text.' -> the page does not tell you to delete the message"]
FIX_087 = "Delete the line 'Then delete the text.' Leave everything else unchanged."
REVIEWS += [
    rec("tr087-a", RA_087, [True, True, True, True, True, False], False, SRC_FAIL, UNSUP_087, s(), "revise", "One unsupported step.", FIX_087),
    rec("tr087-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions (report/block/both, and iPhone/Android).",
        "Replace with exactly one question and no steps: 'There are a couple of things you can do about junk texts. Is your phone an **iPhone** or an **Android** phone?'"),
    rec("tr087-c", RA_087, [True, True, True, True, True, False], False, SRC_FAIL, UNSUP_087, s(plain=1), "revise",
        "Lead-in repeated: 'Reporting them helps your phone company block more of these:' then 'Reporting spam texts helps your phone company block similar messages. Here's how.' Also the unsupported 'Then delete the text.'",
        FIX_087 + " Also delete the second lead-in sentence ('Reporting spam texts helps ... Here's how.') and keep only 'Good for you for not clicking. Reporting them helps your wireless provider block more of these. Here's how:'"),
    rec("tr087-d", RA_087, [True, True, True, True, True, False], False, SRC_FAIL, UNSUP_087, s(), "revise",
        "Unsupported 'Then delete the text.' in the final reply.", FIX_087),
]

# ---------- tr088: online friend asks for money (consumer.ftc.gov/articles/what-know-about-romance-scams) ----------
RA_088 = [
    "Do not send money or gifts to someone you haven't met in person (critical)",
    "Stop communicating with the person (critical)",
    "Talk with a trusted friend or family member",
    "Reverse image search the profile photo / search the person's job plus 'scammer'",
    "Report at ReportFraud.ftc.gov and notify the dating site or app where you met",
    "If money was already sent: contact the bank or payment company immediately and ask for a refund",
]
UNSUP_088 = ["'Strong feelings grow quickly through lots of messages.' -> page says trust is built through frequent chats and then they ask for money; nothing about feelings growing quickly"]
FIX_088 = ("Replace that warning sign with 'After lots of friendly messages, they ask for money for emergencies, travel, or fees.' "
           "Change step 4 to 'Stop talking to him, then report it at **ReportFraud.ftc.gov** and to the website or app where you met.' (the page says stop communicating right away, not only if it is a scam). Leave the rest.")
REVIEWS += [
    rec("tr088-a", RA_088, [True, True, True, True, True, True], False, SRC_FAIL, UNSUP_088, s(), "revise",
        "One unsupported claim; stop-contact step is conditional ('If it's a scam') though the page says to stop right away. Marked reviewed by a person, so listed for the Data Lead.", FIX_088),
    rec("tr088-b", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions, and no protective advice before asking; a money request to an online friend is a scam-risk topic.",
        "Reply with the protective line first and one question: 'I'm glad you asked first. Please don't send any money or gift cards yet. **Have you met this person in person?**'"),
    rec("tr088-c", [], [], True, PASS, [], s(steps="NA", ask_or_answer=1), "revise",
        "Two questions ('What kind of help is he asking for? And have the two of you met in person?') with no protective line first.",
        "Reply: 'Thank you for trusting me with this. Please don't send money or gift cards to someone you haven't met in person. **What kind of help is he asking for?**'"),
    rec("tr088-d", RA_088, [True, True, True, True, True, True], False, SRC_FAIL, UNSUP_088, s(), "revise",
        "Same unsupported claim and conditional stop-contact step in the final reply. (Earlier turn asks two questions; style only.)", FIX_088),
]
