# Reviews for batch ex4, round 1
def R(id, ra, cov, nc, src, saf, dup, unsup, st, ao, co, ac, pl, ru, dec, reasons="", fix=""):
    return {
        "id": id, "required_actions": ra, "covered": cov, "needs_clarification": nc,
        "gates": {"source": src, "safety": saf, "duplicate": dup},
        "unsupported_claims": unsup,
        "scores": {"steps": st, "ask_or_answer": ao, "constraints": co, "actionable": ac, "plain": pl, "realistic_user": ru},
        "decision": dec, "reasons": reasons, "fix": fix,
    }

P = "pass"
REVIEWS = []

# ---- page 111106 (tr048) ----
_ra48 = ["Open Settings, tap Apps, tap Phone (critical)", "Scroll to Screen Unknown Callers (critical)", "Select Silence (critical)"]
REVIEWS += [
    R("tr048-a", _ra48, [True]*3, False, P, P, P, [], 2, 2, 2, 2, 2, 2, "keep"),
    R("tr048-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr048-c", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr048-d", _ra48, [True]*3, False, P, P, P, [], 2, 2, 2, 2, 1, 2, "revise",
      "Final reply has two lead-ins that say the same thing: 'One helpful option on iPhone is to silence calls from numbers you don't know.' followed by 'iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail.'",
      "In the final reply keep 'Thanks.' then go straight into the single sentence 'iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.' Delete the sentence 'One helpful option on iPhone is to silence calls from numbers you don't know.' Keep the steps and closing paragraphs unchanged."),
]

# ---- page 3459196 (tr049) ----
_ra49 = ["Open the Phone app (critical)", "Tap More options, then Settings, then Caller ID and spam (critical)", "Make sure See caller ID & spam is on", "Turn on Filter spam calls (critical)", "If Filter spam calls is not shown, device uses Call Screen (spam autoblocking is an option there)"]
_u49 = ["'Filtered calls won't ring or notify you' -> page only says you don't get missed call or voicemail notifications; it does not say filtered calls do not ring",
        "'Tap the More options menu (three dots)' -> page labels the control only 'More options'/'More'; it does not describe it as three dots"]
_fx49 = ("Replace 'Tap the **More options** menu (three dots).' with 'Tap **More options**.' (no icon description). "
         "Replace 'Filtered calls won't ring or notify you, but they still appear in your call history.' with 'You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.' "
         "Do not say filtered calls do not ring.")
REVIEWS += [
    R("tr049-a", _ra49, [True]*5, False, "fail", P, P, _u49, 2, 2, 2, 2, 2, 2, "revise",
      "Two claims are not on the cited page.", _fx49),
    R("tr049-b", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Final reply asks two questions ('iPhone or Android?' and 'If it's Android, which brand?'); a missing-info reply must be ONE question with no extra.",
      "Reply with one question only, e.g. 'I can help with that. Is your phone an **iPhone** or an **Android** phone?' Then make the opening turn of tr049-d match the new wording (its first assistant turn is a copy), and have tr049-d's user answer fit (e.g. 'Android, a Google Pixel 7a')."),
    R("tr049-c", _ra49, [True]*5, False, "fail", P, P, _u49, 2, 2, 2, 2, 1, 2, "revise",
      "Unsupported claims (user specifically wants calls not to ring, so the 'won't ring' promise matters). Also two lead-ins that overlap: 'Since your phone already labels them, you just need to turn on filtering:' then 'The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.'",
      _fx49 + " Keep one lead-in only: 'Since your phone already labels them, you just need to turn on **Filter spam calls**. It takes about a minute.' and delete 'The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.' Do not promise that the calls will stop ringing; say filtered calls are handled by the filter and you will not get missed call or voicemail notifications."),
    R("tr049-d", _ra49, [True]*5, False, "fail", P, P, _u49, 2, 2, 2, 2, 1, 2, "revise",
      "Unsupported claims, and the lead-in repeats itself ('The Pixel has a built-in spam filter.' then 'The Phone app on your Pixel can filter spam calls.').",
      _fx49 + " Keep 'Thanks.' plus one lead-in sentence ('The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.') and delete 'The Pixel has a built-in spam filter.'"),
]

# ---- page 101575 (tr050) ----
_ra50 = ["Open Settings, tap Battery (critical)", "Tap Battery Health (critical)", "Read Maximum Capacity (relative to when new; lower means fewer hours between charges)", "Know that the 'significantly degraded' message is not a safety issue and service/replacement is available"]
REVIEWS += [
    R("tr050-a", _ra50, [True]*4, False, P, P, P, [], 2, 2, 2, 2, 2, 2, "keep"),
    R("tr050-b", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Asks a second question ('about how old is it?') that does not change the steps. Only the phone type is needed.",
      "Reply with one short question: 'That's annoying. Is your phone an **iPhone** or an **Android** phone?' Update the opening turn of tr050-d to match, and let the user answer just 'iPhone' or keep the age as optional extra info."),
    R("tr050-c", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Two questions ('Do you want to check your battery's health?' and 'is your phone an iPhone or an Android phone?'). The user already said 'battery health', so the first question is unnecessary.",
      "Reply with one question: 'Sure. Is your phone an **iPhone** or an **Android** phone?'"),
    R("tr050-d", _ra50, [True]*4, False, P, P, P, [], 2, 2, 2, 2, 2, 2, "keep"),
]

# ---- page 118236 (tr051) ----
_ra51 = ["Open Messages (critical)", "Tap the Compose button (square and pencil) (critical)", "Enter the names or tap the Add (plus) button to pick from contacts (critical)", "Type the message", "Tap the Send button (up arrow) (critical)", "For group MMS, turn on MMS Messaging in Settings > Messages (optional note)"]
_u51 = ["'when anyone replies, everyone in the group sees it' -> not stated on the page; the page says group SMS replies are sent as individual texts that recipients cannot see, so this is not true for every group"]
_fx51 = "Replace 'All three will get the message, and when anyone replies, everyone in the group sees it.' with 'All three will get your message.' (or: 'You'll see your group in the Messages list.' only if kept to what the page says). Remove the claim about everyone seeing replies."
REVIEWS += [
    R("tr051-a", _ra51, [True]*6, False, "fail", P, P, _u51, 2, 2, 2, 2, 2, 2, "revise", "One unsupported claim.", _fx51),
    R("tr051-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep",
      "Already read by a person; I found no change needed."),
    R("tr051-c", _ra51, [True]*6, False, "fail", P, P, _u51, 2, 2, 2, 2, 1, 2, "revise",
      "Unsupported claim, and two overlapping lead-ins: 'A group text will send it to all three at once, so no one gets left out. Here's how:' then 'You can start a group text. It takes about a minute.'",
      _fx51 + " Also delete the second lead-in 'You can start a group text. It takes about a minute.' and keep 'A group text will send it to all three at once, so no one gets left out. It takes about a minute. Here's how:'"),
    R("tr051-d", _ra51, [True]*6, False, "fail", P, P, _u51, 2, 2, 2, 2, 2, 2, "revise", "One unsupported claim in the final reply.", _fx51),
]

# ---- page 96810 (tr052) ----
_ra52 = ["Open Chrome", "Select the More icon at top right, then Settings (critical)", "Select Appearance (critical)", "Find Page zoom and choose a zoom level from its drop-down (critical)", "Single page: Ctrl and + (Windows) or Command and + (Mac)"]
_u52 = ["'Click the **More** menu (three dots)' -> page calls it the More icon/button and does not describe it as three dots",
        "'choose a bigger number, like **125%** or **150%**' -> page lists no specific zoom percentages"]
_fx52 = "In step 1 write 'Click **More** at the top right of Chrome.' (no 'three dots'). In step 4 write 'Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.' (no percentages)."
REVIEWS += [
    R("tr052-a", _ra52, [True]*5, False, "fail", P, P, _u52, 2, 2, 2, 2, 2, 2, "revise", "Two details are not on the cited page.", _fx52),
    R("tr052-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr052-c", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Two questions in one reply (one site vs every site, and which browser). Only the browser changes the steps.",
      "Reply with one question: 'Sure. Which web browser do you use, such as **Chrome**, **Edge**, or **Safari**?' Update the follow-up user turn accordingly if needed."),
    R("tr052-d", _ra52, [True]*5, False, "fail", P, P, _u52, 2, 2, 2, 2, 1, 2, "revise",
      "Unsupported details, and the lead-in is said twice: 'Chrome lets you set a bigger size for every website.' then 'You can change Chrome's default zoom so every website opens bigger.'",
      _fx52 + " Keep 'Thanks.' plus one lead-in sentence only ('You can change Chrome's default zoom so every website opens bigger. It takes about a minute.') and delete 'Chrome lets you set a bigger size for every website.'"),
]

# ---- page 105104 (tr054) ----
_ra54 = ["Open Find My (critical)", "Tap the Me tab and make sure Share My Location is on (critical)", "Tap the People tab (critical)", "Tap Add (plus icon), then Share My Location (critical)", "Choose the person to share with (critical)", "Choose how long to share (an hour, until end of day, indefinitely, or custom) (critical)", "Requirement: both people need an iPhone with iOS 15 or later"]
REVIEWS += [
    R("tr054-a", _ra54, [True]*7, False, P, P, P, [], 2, 2, 2, 2, 2, 2, "keep"),
    R("tr054-b", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Two questions (iPhone or Android? And does your daughter have an iPhone or Android?).",
      "Ask ONE question that covers both, for example: 'That's a nice way to give her peace of mind. Do you and your daughter both use **iPhones**?' Update the opening turn of tr054-d to match, and make its user answer fit (e.g. 'Yes, we both have iPhones')."),
    R("tr054-c", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Asks two things ('Who would you like to share your location with' and iPhone or Android). Who the person is does not change the steps.",
      "Ask only: 'Sure. Is your phone an **iPhone** or an **Android** phone?'"),
    R("tr054-d", _ra54, [True]*7, False, "fail", P, P,
      ["'6. Tap **Send**.' -> the page does not describe a Send button in the Find My steps"],
      2, 2, 2, 2, 2, 2, "revise",
      "Unsupported Send step (example was marked reviewed by a person, so list for the Data Lead). Earlier assistant turn asks two questions (style only; fix with tr054-b).",
      "Delete step 6 ('Tap **Send**.') and renumber. Step 5 can read 'Choose your daughter.' as in tr054-a; step 6 then becomes the duration choice."),
]

# ---- page 15437054 (tr055) ----
_ra55 = ["Open Google Maps (signed in to Google Account) (critical)", "Tap profile picture or initial, then Location sharing, then New share (critical)", "Choose how long to share (critical)", "Tap the person's profile; allow contacts access if prompted (critical)", "Tap Share (critical)", "Requirement: person's Gmail address saved in Google Contacts; recipient needs Gmail", "No Gmail: copy a link, which works up to 24 hours"]
_u55 = ["'Tap your profile picture or initial at the top' -> page gives no position ('at the top')",
        "'Your son can then see where you are in Google Maps.' -> page text does not say where the recipient sees the location"]
_fx55 = "In step 2 drop 'at the top' ('Tap your **profile picture or initial**.'). Delete the sentence 'Your son can then see where you are in Google Maps.' and end the steps with 'Your location will be shared for the time you picked.' only if you want a closing line."
REVIEWS += [
    R("tr055-a", _ra55, [True]*7, False, "fail", P, P, _u55, 2, 2, 2, 2, 2, 2, "revise", "Two small details are not on the cited page.", _fx55),
    R("tr055-b", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Two questions (iPhone or Android? And does your son use Gmail?).",
      "Ask ONE question: 'That's a good safety idea. Is your phone an **iPhone** or an **Android** phone?' Update the opening turn of tr055-d and its user answer to match (e.g. 'Android')."),
    R("tr055-c", _ra55, [True]*7, False, "fail", P, P, _u55, 2, 2, 2, 2, 1, 2, "revise",
      "Unsupported details, and two lead-ins that overlap: 'Yes, then he won't have to wait for your text. Here's how:' then 'Here's how. It takes about two minutes. ...'",
      _fx55 + " Remove the second 'Here's how.' so the reply reads: 'Yes, then he won't have to wait for your text. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.' then the steps."),
    R("tr055-d", _ra55, [True]*7, False, "fail", P, P, _u55, 2, 2, 2, 2, 1, 2, "revise",
      "Unsupported details. Also the user said the son uses Gmail, yet the reply keeps the 'If he doesn't use Gmail, you can share a link' paragraph (steps for a case the user ruled out), and the intro says 'Here's how.' after 'Google Maps can do this.'",
      _fx55 + " Delete the sentence 'If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours.' (keep 'Only share your location with people you trust.'). Change 'Great. Google Maps can do this. Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.' to 'Great. Google Maps can do this. It takes about two minutes, and your son's Gmail address needs to be saved in your contacts.'"),
]

# ---- page 102590 (tr056) ----
_ra56 = ["Open the App Store (critical)", "Tap the Search tab and look for the app (critical)", "Tap Get (or the price) next to the app (critical)", "Complete it by double-clicking the side button; Face ID glance or Touch ID finger; may need Apple Account password (critical)", "If it shows Open, the app is already downloaded"]
_u56 = ["'tap the search button' -> page mentions only the Search tab, not a search button",
        "'the button changes to **Open** and the app appears on your Home Screen' -> page does not say the app appears on the Home Screen",
        "'Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.' -> page gives no such advice (and says nothing about verifying apps)",
        "'rest your finger on the Home button' -> page says the Touch ID button"]
_fx56 = ("Step 3: 'Type **WhatsApp** to search.' (no 'search button'). Step 5: say 'rest your finger on the **Touch ID** button'. "
         "Replace the closing line with 'When it's done, you'll see **Open** instead of **Get**.' Delete the 'Tip' paragraph (or support it with an official Apple page on avoiding fake apps if one is found).")
REVIEWS += [
    R("tr056-a", _ra56, [True]*5, False, "fail", P, P, _u56, 2, 2, 2, 2, 2, 2, "revise", "Several details are not on the cited page.", _fx56),
    R("tr056-b", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Two questions (iPhone or Android? And which app?). The app name does not change the steps.",
      "Ask ONE question: 'I can walk you through it. Is your phone an **iPhone** or an **Android** phone?' Update tr056-d's first assistant turn and the user answer to match (e.g. 'iPhone, I want WhatsApp' is fine as extra info)."),
    R("tr056-c", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Asks which app, which does not change the steps. The one detail that matters is the phone type, because 'app store' alone does not say iPhone vs Android (Android uses the Play Store).",
      "Ask ONE question: 'Sure. Is your phone an **iPhone** or an **Android** phone?'"),
    R("tr056-d", _ra56, [True]*5, False, "fail", P, P, _u56, 2, 2, 2, 2, 2, 2, "revise", "Unsupported details in the final reply.", _fx56),
]

# ---- page 9457058 (tr057) ----
_ra57 = ["Open the Play Store app (critical)", "Find the app you want (search or browse) (critical)", "Check the star ratings and number of downloads under the app's title", "Tap Install (no-charge apps) or the price (critical)", "Safety: get apps from Google Play; Play Protect checks for harmful apps; unknown sources put the phone and information at risk"]
_u57 = ["'Tap the search bar and type the app's name.' -> cited page only says 'Find an app you want'; no search bar is named (https://support.google.com/googleplay/answer/113409 says 'Search or browse for content')",
        "'Check that the name and maker are what you expected.' -> page says check star ratings and number of downloads; nothing about the maker",
        "'When it's finished, open the app from the Play Store or find it with your other apps.' -> page gives no steps for opening the app after install",
        "'Avoid installing apps from links in texts or emails.' -> page does not mention links in texts or emails (it only warns about unknown sources)"]
_fx57 = ("Add https://support.google.com/googleplay/answer/113409 as a second source. Step 2: 'Search for the app by name, or browse.' (no 'search bar'). "
         "Step 3: 'Tap the app, then check the star ratings and the number of downloads under its title.' (delete 'name and maker'). "
         "Step 5: either delete it, or re-source it from https://support.google.com/android/answer/9079646 (Find, open & close apps on Android) after confirming the wording there. "
         "Last line: 'It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.' Delete the 'links in texts or emails' sentence.")
REVIEWS += [
    R("tr057-a", _ra57, [True]*5, False, "fail", P, P, _u57, 2, 2, 2, 2, 2, 2, "revise", "Four claims are not supported by the cited page.", _fx57),
    R("tr057-b", [], [], True, P, P, P, [], "NA", 1, 2, 2, 2, 2, "revise",
      "Two questions (iPhone or Android? And which app?). The app name does not change the steps.",
      "Ask ONE question: 'I can help. Is your phone an **iPhone** or an **Android** phone?' Update tr057-d's first assistant turn to match; the user answer can stay 'Android. It's the app for my doctor's office.'"),
    R("tr057-c", _ra57, [True]*5, False, "fail", P, P, _u57, 2, 2, 2, 2, 2, 2, "revise", "Four claims are not supported by the cited page.", _fx57),
    R("tr057-d", _ra57, [True]*5, False, "fail", P, P, _u57, 2, 2, 2, 2, 2, 2, "revise", "Four claims are not supported by the cited page.", _fx57),
]

# ---- pages 101550 + 108429 (tr058) ----
_ra58 = ["Touch and hold the app (critical)", "Tap Remove App (critical)", "Tap Delete App, then Delete to confirm (critical)", "If apps jiggle: tap the minus icon at the app's upper-left, Delete App, Delete, then Done at the top (critical for that case)", "Deleting does not cancel in-app subscriptions; cancel unneeded ones first", "Delete removes the app and its related data (108429)"]
_u58 = ["'If you might want it later, you can download it again from the App Store.' -> neither cited page says apps can be downloaded again"]
_fx58 = "Delete the sentence 'If you might want it later, you can download it again from the App Store.' Keep 'Deleting an app also removes its data from your phone.' (supported by 108429: Delete 'removes the app and its related data')."
REVIEWS += [
    R("tr058-a", _ra58, [True]*6, False, "fail", P, P, _u58, 2, 2, 2, 2, 2, 2, "revise", "One unsupported claim.", _fx58),
    R("tr058-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr058-c", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr058-d", _ra58, [True]*6, False, "fail", P, P, _u58, 2, 2, 2, 2, 2, 2, "revise",
      "One unsupported claim in the final reply (example was marked reviewed by a person, so list for the Data Lead).", _fx58),
]

# ---- pages 13627402 / 7431795 / 13627571 (tr059) ----
_ra59 = ["Open the Play Store app (critical)", "Tap the Profile icon at the top right (critical)", "Tap Manage apps & devices, then Manage (critical)", "Select the app to remove (critical)", "Tap Uninstall (critical)", "Purchased apps can be reinstalled without paying again", "Some preinstalled apps cannot be deleted; they may only be turned off (13627571)"]
_u59 = ["'Tap **Manage apps & device**.' -> page label is 'Manage apps & devices' (plural)"]
_fx59 = "Change step 3 to 'Tap **Manage apps & devices**.' (plural, as on the page)."
REVIEWS += [
    R("tr059-a", _ra59, [True]*6 + [False], False, "fail", P, P, _u59, 2, 2, 2, 2, 2, 2, "revise", "Label does not match the page.", _fx59),
    R("tr059-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr059-c", _ra59, [True]*7, False, "fail", P, P, _u59, 2, 2, 2, 2, 1, 2, "revise",
      "Label mismatch. Also two overlapping lead-ins: 'You can remove most of them. ... most apps can be removed like this:' then 'You can remove it through the Play Store. It takes about a minute.'",
      _fx59 + " Delete the second lead-in 'You can remove it through the Play Store. It takes about a minute.' and end the first with 'most apps can be removed through the **Play Store** like this. It takes about a minute:'"),
    R("tr059-d", _ra59, [True]*6 + [False], False, "fail", P, P, _u59, 2, 2, 2, 2, 2, 2, "revise", "Label does not match the page.", _fx59),
]

# ---- page 4b55f974 Microsoft (tr060) ----
_ra60 = ["Open Start, then Settings, then Apps, then Installed apps (critical)", "Find the app, select More, then Uninstall (critical)", "Follow the directions on the screen", "Start > All apps, right-click the app, select Uninstall (alternative)", "Control Panel > Programs > Programs and Features, right-click the program, Uninstall (alternative; for apps Settings cannot remove)"]
_u60 = ["'Click the **three dots** next to it' -> page shows a More icon and names it More; it does not describe three dots",
        "'Confirm, and follow any instructions that appear.' -> page describes no separate confirm step in Settings, only 'follow the directions on the screen'"]
_fx60 = "Step 5: 'Click **More** next to it, then click **Uninstall**.' (no 'three dots'). Step 6: 'Follow any directions that appear on the screen.' (no 'Confirm')."
REVIEWS += [
    R("tr060-a", _ra60, [True, True, True, True, False], False, "fail", P, P, _u60, 2, 2, 2, 2, 2, 2, "revise", "Two details are not on the cited page.", _fx60),
    R("tr060-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr060-c", _ra60, [True, True, True, True, False], False, "fail", P, P, _u60, 1, 2, 2, 2, 2, 2, "revise",
      "Unsupported details. The user asked 'Settings or Control Panel?' and the reply names Control Panel > Programs and Features but gives no steps for it.",
      _fx60 + " Add a short 'If PhotoEasy is not in the list' block with the page's Control Panel steps: search for **Control Panel** on the taskbar and open it; go to **Programs**, then **Programs and Features**; right-click the program and choose **Uninstall** (or **Uninstall/Change**); follow the directions on the screen. Keep the total reply short."),
    R("tr060-d", _ra60, [True, True, True, True, False], False, "fail", P, P, _u60, 2, 2, 2, 2, 2, 2, "revise", "Two details are not on the cited page.", _fx60),
]

# ---- page 108429 (tr061) ----
_ra61 = ["Open Settings, tap General (critical)", "Tap iPhone Storage ([device] Storage) (critical)", "Look at the recommendations and the list of apps with their storage usage (critical)", "Tap an app's name for details; offload or delete the app (critical)", "Offload keeps documents and data; Delete removes the app and its related data"]
_u61 = ["'**Offload App** removes the app ... **Delete App** removes the app and its data.' -> page names the actions 'Offload the app' / 'Delete the app', not buttons labelled 'Offload App' / 'Delete App'",
        "'so nothing is lost if you reinstall it' -> page does not mention reinstalling",
        "'Offloading apps you rarely use is a safe place to start.' -> page does not call offloading safe or recommend it first",
        "'At the top, look at the recommendations ... Below that is a list of your apps.' -> page gives no positions, only that the screen shows recommendations and a list of apps",
        "'Tap one to see what it would remove' -> not on the page"]
_fx61 = ("Step 4: 'You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.' (remove 'At the top', 'Below that', 'see what it would remove'). "
         "Step 5: 'Tap an app's name, then choose to offload or delete it. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.' (no bold button names, no 'reinstall'). Delete the final sentence about offloading being a safe place to start.")
REVIEWS += [
    R("tr061-a", _ra61, [True]*5, False, "fail", P, P, _u61, 2, 2, 2, 2, 2, 2, "revise", "Several details are not on the cited page.", _fx61),
    R("tr061-b", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr061-c", [], [], True, P, P, P, [], "NA", 2, 2, 2, 2, 2, "keep"),
    R("tr061-d", _ra61, [True]*5, False, "fail", P, P, _u61, 2, 2, 2, 2, 2, 2, "revise", "Several details are not on the cited page.", _fx61),
]
