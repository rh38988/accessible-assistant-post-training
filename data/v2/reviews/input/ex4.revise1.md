# Revision list: batch ex4, after review round 1 (36 examples)

Edit ONLY these examples in data/v2/specs/ex4.py, then rebuild.

## tr048-d
- reasons: Final reply has two lead-ins that say the same thing: 'One helpful option on iPhone is to silence calls from numbers you don't know.' followed by 'iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail.'
- fix requested: In the final reply keep 'Thanks.' then go straight into the single sentence 'iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.' Delete the sentence 'One helpful option on iPhone is to silence calls from numbers you don't know.' Keep the steps and closing paragraphs unchanged.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/111106

## tr049-a
- reasons: Two claims are not on the cited page.
- fix requested: Replace 'Tap the **More options** menu (three dots).' with 'Tap **More options**.' (no icon description). Replace 'Filtered calls won't ring or notify you, but they still appear in your call history.' with 'You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.' Do not say filtered calls do not ring.
- unsupported claims: 'Filtered calls won't ring or notify you' -> page only says you don't get missed call or voicemail notifications; it does not say filtered calls do not ring | 'Tap the More options menu (three dots)' -> page labels the control only 'More options'/'More'; it does not describe it as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

## tr049-b
- reasons: Final reply asks two questions ('iPhone or Android?' and 'If it's Android, which brand?'); a missing-info reply must be ONE question with no extra.
- fix requested: Reply with one question only, e.g. 'I can help with that. Is your phone an **iPhone** or an **Android** phone?' Then make the opening turn of tr049-d match the new wording (its first assistant turn is a copy), and have tr049-d's user answer fit (e.g. 'Android, a Google Pixel 7a').
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

## tr049-c
- reasons: Unsupported claims (user specifically wants calls not to ring, so the 'won't ring' promise matters). Also two lead-ins that overlap: 'Since your phone already labels them, you just need to turn on filtering:' then 'The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.'
- fix requested: Replace 'Tap the **More options** menu (three dots).' with 'Tap **More options**.' (no icon description). Replace 'Filtered calls won't ring or notify you, but they still appear in your call history.' with 'You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.' Do not say filtered calls do not ring. Keep one lead-in only: 'Since your phone already labels them, you just need to turn on **Filter spam calls**. It takes about a minute.' and delete 'The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.' Do not promise that the calls will stop ringing; say filtered calls are handled by the filter and you will not get missed call or voicemail notifications.
- unsupported claims: 'Filtered calls won't ring or notify you' -> page only says you don't get missed call or voicemail notifications; it does not say filtered calls do not ring | 'Tap the More options menu (three dots)' -> page labels the control only 'More options'/'More'; it does not describe it as three dots
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

## tr049-d
- reasons: Unsupported claims, and the lead-in repeats itself ('The Pixel has a built-in spam filter.' then 'The Phone app on your Pixel can filter spam calls.').
- fix requested: Replace 'Tap the **More options** menu (three dots).' with 'Tap **More options**.' (no icon description). Replace 'Filtered calls won't ring or notify you, but they still appear in your call history.' with 'You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.' Do not say filtered calls do not ring. Keep 'Thanks.' plus one lead-in sentence ('The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.') and delete 'The Pixel has a built-in spam filter.'
- unsupported claims: 'Filtered calls won't ring or notify you' -> page only says you don't get missed call or voicemail notifications; it does not say filtered calls do not ring | 'Tap the More options menu (three dots)' -> page labels the control only 'More options'/'More'; it does not describe it as three dots
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

## tr050-b
- reasons: Asks a second question ('about how old is it?') that does not change the steps. Only the phone type is needed.
- fix requested: Reply with one short question: 'That's annoying. Is your phone an **iPhone** or an **Android** phone?' Update the opening turn of tr050-d to match, and let the user answer just 'iPhone' or keep the age as optional extra info.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101575

## tr050-c
- reasons: Two questions ('Do you want to check your battery's health?' and 'is your phone an iPhone or an Android phone?'). The user already said 'battery health', so the first question is unnecessary.
- fix requested: Reply with one question: 'Sure. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101575

## tr051-a
- reasons: One unsupported claim.
- fix requested: Replace 'All three will get the message, and when anyone replies, everyone in the group sees it.' with 'All three will get your message.' (or: 'You'll see your group in the Messages list.' only if kept to what the page says). Remove the claim about everyone seeing replies.
- unsupported claims: 'when anyone replies, everyone in the group sees it' -> not stated on the page; the page says group SMS replies are sent as individual texts that recipients cannot see, so this is not true for every group
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr051-c
- reasons: Unsupported claim, and two overlapping lead-ins: 'A group text will send it to all three at once, so no one gets left out. Here's how:' then 'You can start a group text. It takes about a minute.'
- fix requested: Replace 'All three will get the message, and when anyone replies, everyone in the group sees it.' with 'All three will get your message.' (or: 'You'll see your group in the Messages list.' only if kept to what the page says). Remove the claim about everyone seeing replies. Also delete the second lead-in 'You can start a group text. It takes about a minute.' and keep 'A group text will send it to all three at once, so no one gets left out. It takes about a minute. Here's how:'
- unsupported claims: 'when anyone replies, everyone in the group sees it' -> not stated on the page; the page says group SMS replies are sent as individual texts that recipients cannot see, so this is not true for every group
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr051-d
- reasons: One unsupported claim in the final reply.
- fix requested: Replace 'All three will get the message, and when anyone replies, everyone in the group sees it.' with 'All three will get your message.' (or: 'You'll see your group in the Messages list.' only if kept to what the page says). Remove the claim about everyone seeing replies.
- unsupported claims: 'when anyone replies, everyone in the group sees it' -> not stated on the page; the page says group SMS replies are sent as individual texts that recipients cannot see, so this is not true for every group
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr052-a
- reasons: Two details are not on the cited page.
- fix requested: In step 1 write 'Click **More** at the top right of Chrome.' (no 'three dots'). In step 4 write 'Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.' (no percentages).
- unsupported claims: 'Click the **More** menu (three dots)' -> page calls it the More icon/button and does not describe it as three dots | 'choose a bigger number, like **125%** or **150%**' -> page lists no specific zoom percentages
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr052-c
- reasons: Two questions in one reply (one site vs every site, and which browser). Only the browser changes the steps.
- fix requested: Reply with one question: 'Sure. Which web browser do you use, such as **Chrome**, **Edge**, or **Safari**?' Update the follow-up user turn accordingly if needed.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr052-d
- reasons: Unsupported details, and the lead-in is said twice: 'Chrome lets you set a bigger size for every website.' then 'You can change Chrome's default zoom so every website opens bigger.'
- fix requested: In step 1 write 'Click **More** at the top right of Chrome.' (no 'three dots'). In step 4 write 'Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.' (no percentages). Keep 'Thanks.' plus one lead-in sentence only ('You can change Chrome's default zoom so every website opens bigger. It takes about a minute.') and delete 'Chrome lets you set a bigger size for every website.'
- unsupported claims: 'Click the **More** menu (three dots)' -> page calls it the More icon/button and does not describe it as three dots | 'choose a bigger number, like **125%** or **150%**' -> page lists no specific zoom percentages
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr054-b
- reasons: Two questions (iPhone or Android? And does your daughter have an iPhone or Android?).
- fix requested: Ask ONE question that covers both, for example: 'That's a nice way to give her peace of mind. Do you and your daughter both use **iPhones**?' Update the opening turn of tr054-d to match, and make its user answer fit (e.g. 'Yes, we both have iPhones').
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/105104

## tr054-c
- reasons: Asks two things ('Who would you like to share your location with' and iPhone or Android). Who the person is does not change the steps.
- fix requested: Ask only: 'Sure. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/105104

## tr055-a
- reasons: Two small details are not on the cited page.
- fix requested: In step 2 drop 'at the top' ('Tap your **profile picture or initial**.'). Delete the sentence 'Your son can then see where you are in Google Maps.' and end the steps with 'Your location will be shared for the time you picked.' only if you want a closing line.
- unsupported claims: 'Tap your profile picture or initial at the top' -> page gives no position ('at the top') | 'Your son can then see where you are in Google Maps.' -> page text does not say where the recipient sees the location
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

## tr055-b
- reasons: Two questions (iPhone or Android? And does your son use Gmail?).
- fix requested: Ask ONE question: 'That's a good safety idea. Is your phone an **iPhone** or an **Android** phone?' Update the opening turn of tr055-d and its user answer to match (e.g. 'Android').
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

## tr055-c
- reasons: Unsupported details, and two lead-ins that overlap: 'Yes, then he won't have to wait for your text. Here's how:' then 'Here's how. It takes about two minutes. ...'
- fix requested: In step 2 drop 'at the top' ('Tap your **profile picture or initial**.'). Delete the sentence 'Your son can then see where you are in Google Maps.' and end the steps with 'Your location will be shared for the time you picked.' only if you want a closing line. Remove the second 'Here's how.' so the reply reads: 'Yes, then he won't have to wait for your text. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.' then the steps.
- unsupported claims: 'Tap your profile picture or initial at the top' -> page gives no position ('at the top') | 'Your son can then see where you are in Google Maps.' -> page text does not say where the recipient sees the location
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

## tr055-d
- reasons: Unsupported details. Also the user said the son uses Gmail, yet the reply keeps the 'If he doesn't use Gmail, you can share a link' paragraph (steps for a case the user ruled out), and the intro says 'Here's how.' after 'Google Maps can do this.'
- fix requested: In step 2 drop 'at the top' ('Tap your **profile picture or initial**.'). Delete the sentence 'Your son can then see where you are in Google Maps.' and end the steps with 'Your location will be shared for the time you picked.' only if you want a closing line. Delete the sentence 'If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours.' (keep 'Only share your location with people you trust.'). Change 'Great. Google Maps can do this. Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.' to 'Great. Google Maps can do this. It takes about two minutes, and your son's Gmail address needs to be saved in your contacts.'
- unsupported claims: 'Tap your profile picture or initial at the top' -> page gives no position ('at the top') | 'Your son can then see where you are in Google Maps.' -> page text does not say where the recipient sees the location
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

## tr056-a
- reasons: Several details are not on the cited page.
- fix requested: Step 3: 'Type **WhatsApp** to search.' (no 'search button'). Step 5: say 'rest your finger on the **Touch ID** button'. Replace the closing line with 'When it's done, you'll see **Open** instead of **Get**.' Delete the 'Tip' paragraph (or support it with an official Apple page on avoiding fake apps if one is found).
- unsupported claims: 'tap the search button' -> page mentions only the Search tab, not a search button | 'the button changes to **Open** and the app appears on your Home Screen' -> page does not say the app appears on the Home Screen | 'Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.' -> page gives no such advice (and says nothing about verifying apps) | 'rest your finger on the Home button' -> page says the Touch ID button
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102590

## tr056-b
- reasons: Two questions (iPhone or Android? And which app?). The app name does not change the steps.
- fix requested: Ask ONE question: 'I can walk you through it. Is your phone an **iPhone** or an **Android** phone?' Update tr056-d's first assistant turn and the user answer to match (e.g. 'iPhone, I want WhatsApp' is fine as extra info).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102590

## tr056-c
- reasons: Asks which app, which does not change the steps. The one detail that matters is the phone type, because 'app store' alone does not say iPhone vs Android (Android uses the Play Store).
- fix requested: Ask ONE question: 'Sure. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102590

## tr056-d
- reasons: Unsupported details in the final reply.
- fix requested: Step 3: 'Type **WhatsApp** to search.' (no 'search button'). Step 5: say 'rest your finger on the **Touch ID** button'. Replace the closing line with 'When it's done, you'll see **Open** instead of **Get**.' Delete the 'Tip' paragraph (or support it with an official Apple page on avoiding fake apps if one is found).
- unsupported claims: 'tap the search button' -> page mentions only the Search tab, not a search button | 'the button changes to **Open** and the app appears on your Home Screen' -> page does not say the app appears on the Home Screen | 'Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.' -> page gives no such advice (and says nothing about verifying apps) | 'rest your finger on the Home button' -> page says the Touch ID button
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102590

## tr057-a
- reasons: Four claims are not supported by the cited page.
- fix requested: Add https://support.google.com/googleplay/answer/113409 as a second source. Step 2: 'Search for the app by name, or browse.' (no 'search bar'). Step 3: 'Tap the app, then check the star ratings and the number of downloads under its title.' (delete 'name and maker'). Step 5: either delete it, or re-source it from https://support.google.com/android/answer/9079646 (Find, open & close apps on Android) after confirming the wording there. Last line: 'It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.' Delete the 'links in texts or emails' sentence.
- unsupported claims: 'Tap the search bar and type the app's name.' -> cited page only says 'Find an app you want'; no search bar is named (https://support.google.com/googleplay/answer/113409 says 'Search or browse for content') | 'Check that the name and maker are what you expected.' -> page says check star ratings and number of downloads; nothing about the maker | 'When it's finished, open the app from the Play Store or find it with your other apps.' -> page gives no steps for opening the app after install | 'Avoid installing apps from links in texts or emails.' -> page does not mention links in texts or emails (it only warns about unknown sources)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9457058?hl=en

## tr057-b
- reasons: Two questions (iPhone or Android? And which app?). The app name does not change the steps.
- fix requested: Ask ONE question: 'I can help. Is your phone an **iPhone** or an **Android** phone?' Update tr057-d's first assistant turn to match; the user answer can stay 'Android. It's the app for my doctor's office.'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9457058?hl=en

## tr057-c
- reasons: Four claims are not supported by the cited page.
- fix requested: Add https://support.google.com/googleplay/answer/113409 as a second source. Step 2: 'Search for the app by name, or browse.' (no 'search bar'). Step 3: 'Tap the app, then check the star ratings and the number of downloads under its title.' (delete 'name and maker'). Step 5: either delete it, or re-source it from https://support.google.com/android/answer/9079646 (Find, open & close apps on Android) after confirming the wording there. Last line: 'It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.' Delete the 'links in texts or emails' sentence.
- unsupported claims: 'Tap the search bar and type the app's name.' -> cited page only says 'Find an app you want'; no search bar is named (https://support.google.com/googleplay/answer/113409 says 'Search or browse for content') | 'Check that the name and maker are what you expected.' -> page says check star ratings and number of downloads; nothing about the maker | 'When it's finished, open the app from the Play Store or find it with your other apps.' -> page gives no steps for opening the app after install | 'Avoid installing apps from links in texts or emails.' -> page does not mention links in texts or emails (it only warns about unknown sources)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9457058?hl=en

## tr057-d
- reasons: Four claims are not supported by the cited page.
- fix requested: Add https://support.google.com/googleplay/answer/113409 as a second source. Step 2: 'Search for the app by name, or browse.' (no 'search bar'). Step 3: 'Tap the app, then check the star ratings and the number of downloads under its title.' (delete 'name and maker'). Step 5: either delete it, or re-source it from https://support.google.com/android/answer/9079646 (Find, open & close apps on Android) after confirming the wording there. Last line: 'It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.' Delete the 'links in texts or emails' sentence.
- unsupported claims: 'Tap the search bar and type the app's name.' -> cited page only says 'Find an app you want'; no search bar is named (https://support.google.com/googleplay/answer/113409 says 'Search or browse for content') | 'Check that the name and maker are what you expected.' -> page says check star ratings and number of downloads; nothing about the maker | 'When it's finished, open the app from the Play Store or find it with your other apps.' -> page gives no steps for opening the app after install | 'Avoid installing apps from links in texts or emails.' -> page does not mention links in texts or emails (it only warns about unknown sources)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9457058?hl=en

## tr058-a
- reasons: One unsupported claim.
- fix requested: Delete the sentence 'If you might want it later, you can download it again from the App Store.' Keep 'Deleting an app also removes its data from your phone.' (supported by 108429: Delete 'removes the app and its related data').
- unsupported claims: 'If you might want it later, you can download it again from the App Store.' -> neither cited page says apps can be downloaded again
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101550 ; https://support.apple.com/en-us/108429

## tr059-a
- reasons: Label does not match the page.
- fix requested: Change step 3 to 'Tap **Manage apps & devices**.' (plural, as on the page).
- unsupported claims: 'Tap **Manage apps & device**.' -> page label is 'Manage apps & devices' (plural)
- required actions missing from the reply: Some preinstalled apps cannot be deleted; they may only be turned off (13627571)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

## tr059-c
- reasons: Label mismatch. Also two overlapping lead-ins: 'You can remove most of them. ... most apps can be removed like this:' then 'You can remove it through the Play Store. It takes about a minute.'
- fix requested: Change step 3 to 'Tap **Manage apps & devices**.' (plural, as on the page). Delete the second lead-in 'You can remove it through the Play Store. It takes about a minute.' and end the first with 'most apps can be removed through the **Play Store** like this. It takes about a minute:'
- unsupported claims: 'Tap **Manage apps & device**.' -> page label is 'Manage apps & devices' (plural)
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

## tr059-d
- reasons: Label does not match the page.
- fix requested: Change step 3 to 'Tap **Manage apps & devices**.' (plural, as on the page).
- unsupported claims: 'Tap **Manage apps & device**.' -> page label is 'Manage apps & devices' (plural)
- required actions missing from the reply: Some preinstalled apps cannot be deleted; they may only be turned off (13627571)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

## tr060-a
- reasons: Two details are not on the cited page.
- fix requested: Step 5: 'Click **More** next to it, then click **Uninstall**.' (no 'three dots'). Step 6: 'Follow any directions that appear on the screen.' (no 'Confirm').
- unsupported claims: 'Click the **three dots** next to it' -> page shows a More icon and names it More; it does not describe three dots | 'Confirm, and follow any instructions that appear.' -> page describes no separate confirm step in Settings, only 'follow the directions on the screen'
- required actions missing from the reply: Control Panel > Programs > Programs and Features, right-click the program, Uninstall (alternative; for apps Settings cannot remove)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

## tr060-c
- reasons: Unsupported details. The user asked 'Settings or Control Panel?' and the reply names Control Panel > Programs and Features but gives no steps for it.
- fix requested: Step 5: 'Click **More** next to it, then click **Uninstall**.' (no 'three dots'). Step 6: 'Follow any directions that appear on the screen.' (no 'Confirm'). Add a short 'If PhotoEasy is not in the list' block with the page's Control Panel steps: search for **Control Panel** on the taskbar and open it; go to **Programs**, then **Programs and Features**; right-click the program and choose **Uninstall** (or **Uninstall/Change**); follow the directions on the screen. Keep the total reply short.
- unsupported claims: 'Click the **three dots** next to it' -> page shows a More icon and names it More; it does not describe three dots | 'Confirm, and follow any instructions that appear.' -> page describes no separate confirm step in Settings, only 'follow the directions on the screen'
- required actions missing from the reply: Control Panel > Programs > Programs and Features, right-click the program, Uninstall (alternative; for apps Settings cannot remove)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

## tr060-d
- reasons: Two details are not on the cited page.
- fix requested: Step 5: 'Click **More** next to it, then click **Uninstall**.' (no 'three dots'). Step 6: 'Follow any directions that appear on the screen.' (no 'Confirm').
- unsupported claims: 'Click the **three dots** next to it' -> page shows a More icon and names it More; it does not describe three dots | 'Confirm, and follow any instructions that appear.' -> page describes no separate confirm step in Settings, only 'follow the directions on the screen'
- required actions missing from the reply: Control Panel > Programs > Programs and Features, right-click the program, Uninstall (alternative; for apps Settings cannot remove)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

## tr061-a
- reasons: Several details are not on the cited page.
- fix requested: Step 4: 'You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.' (remove 'At the top', 'Below that', 'see what it would remove'). Step 5: 'Tap an app's name, then choose to offload or delete it. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.' (no bold button names, no 'reinstall'). Delete the final sentence about offloading being a safe place to start.
- unsupported claims: '**Offload App** removes the app ... **Delete App** removes the app and its data.' -> page names the actions 'Offload the app' / 'Delete the app', not buttons labelled 'Offload App' / 'Delete App' | 'so nothing is lost if you reinstall it' -> page does not mention reinstalling | 'Offloading apps you rarely use is a safe place to start.' -> page does not call offloading safe or recommend it first | 'At the top, look at the recommendations ... Below that is a list of your apps.' -> page gives no positions, only that the screen shows recommendations and a list of apps | 'Tap one to see what it would remove' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108429

## tr061-d
- reasons: Several details are not on the cited page.
- fix requested: Step 4: 'You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.' (remove 'At the top', 'Below that', 'see what it would remove'). Step 5: 'Tap an app's name, then choose to offload or delete it. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.' (no bold button names, no 'reinstall'). Delete the final sentence about offloading being a safe place to start.
- unsupported claims: '**Offload App** removes the app ... **Delete App** removes the app and its data.' -> page names the actions 'Offload the app' / 'Delete the app', not buttons labelled 'Offload App' / 'Delete App' | 'so nothing is lost if you reinstall it' -> page does not mention reinstalling | 'Offloading apps you rarely use is a safe place to start.' -> page does not call offloading safe or recommend it first | 'At the top, look at the recommendations ... Below that is a list of your apps.' -> page gives no positions, only that the screen shows recommendations and a list of apps | 'Tap one to see what it would remove' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108429
