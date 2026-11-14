# Revision list: batch ex5, after review round 1 (31 examples)

Edit ONLY these examples in data/v2/specs/ex5.py, then rebuild.

## tr062-a
- reasons: Unsupported 'what you will see' cue after tapping Storage.
- fix requested: In step 2 delete the sentence "You'll see which kinds of files use the most space." (page only says: Settings > Storage > Free up space, then scroll to a category and tap Select files; if the category isn't listed, tap Browse). Optionally add 'If you don't see the category, tap **Browse**.' after step 4.
- unsupported claims: 'Tap **Storage**. You'll see which kinds of files use the most space.' -> the page only says 'Tap Storage' then 'Select a category'; it does not say what the user sees or that files are shown by size
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7431795?hl=en

## tr062-d
- reasons: Unsupported 'what you will see' cue. The same hedge is said twice (lead-in 'Samsung menus can look a little different, so tell me if something doesn't match' and closing 'Menu names vary between phones ... Tell me what you see if something doesn't match').
- fix requested: In step 2 delete the sentence "You'll see which kinds of files use the most space." (page only says: Settings > Storage > Free up space, then scroll to a category and tap Select files; if the category isn't listed, tap Browse). Optionally add 'If you don't see the category, tap **Browse**.' after step 4. Also keep the Samsung hedge only once: delete either the lead-in sentence or the closing paragraph.
- unsupported claims: 'Tap **Storage**. You'll see which kinds of files use the most space.' -> the page only says 'Tap Storage' then 'Select a category'; it does not say what the user sees or that files are shown by size
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7431795?hl=en

## tr063-b
- reasons: Two questions ('Do you mean the flashlight?' and 'Is your phone an iPhone or an Android phone?'). The 'do you mean flashlight' check is not needed to choose the steps.
- fix requested: Replace the reply with one question only, for example: 'I can help with the flashlight. Is your phone an **iPhone** or an **Android** phone?' (one question mark). The first assistant turn of tr063-d is identical and must be changed the same way, with the user's follow-up adjusted to 'iPhone'.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/105001

## tr066-a
- reasons: Wrong finishing button and two unsupported UI descriptions.
- fix requested: Rewrite the steps to match the page: 1. Open the **Clock** app, then tap the **Alarms** tab. 2. Tap the **Add** button. 3. Set the time to 6:30 AM. 4. (optional) Tap **Repeat** to choose days. 5. Tap **Done**. Remove 'at the bottom', '(+)' and 'Save (on some versions, Done)'. Keep the Silent/Do Not Disturb, Sounds & Haptics > Ringtone and Alerts, and Sound/None lines.
- unsupported claims: 'Tap **Alarms** at the bottom.' -> page says only 'tap the Alarms tab'; no position given | 'Tap the **plus (+)** button.' -> page says 'Tap the Add button'; the icon has no alt text or description | 'Tap **Save** (on some versions, **Done**).' -> page says tap Done when creating an alarm; Save appears only when editing an existing alarm
- required actions missing from the reply: Tap Done when creating a new alarm (Save is only for editing an existing alarm) (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118444

## tr066-b
- reasons: Asks two things (phone type AND wake-up time). The time does not change the steps, so it should not be asked first.
- fix requested: Ask only: 'Sure. Is your phone an **iPhone** or an **Android** phone?' Update tr066-d's first assistant turn the same way and change the user's follow-up there to 'iPhone' (the final reply can then ask nothing, or the time can be left out).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118444

## tr066-c
- reasons: Wrong finishing button and unsupported UI descriptions. Lead-in is pasted twice ('Here's how to make sure you're up at 6:30:' then 'Here's how. It takes about a minute.'). The user needs a single wake-up tomorrow, so the 'If you want it every day' step is not needed.
- fix requested: Rewrite the steps to match the page: 1. Open the **Clock** app, then tap the **Alarms** tab. 2. Tap the **Add** button. 3. Set the time to 6:30 AM. 4. (optional) Tap **Repeat** to choose days. 5. Tap **Done**. Remove 'at the bottom', '(+)' and 'Save (on some versions, Done)'. Keep the Silent/Do Not Disturb, Sounds & Haptics > Ringtone and Alerts, and Sound/None lines. Use one lead-in sentence only, and make the Repeat step optional ('Only if you want it to repeat, tap Repeat').
- unsupported claims: 'Tap **Alarms** at the bottom.' -> page says only 'tap the Alarms tab'; no position given | 'Tap the **plus (+)** button.' -> page says 'Tap the Add button'; the icon has no alt text or description | 'Tap **Save** (on some versions, **Done**).' -> page says tap Done when creating an alarm; Save appears only when editing an existing alarm
- required actions missing from the reply: Tap Done when creating a new alarm (Save is only for editing an existing alarm) (critical)
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118444

## tr066-d
- reasons: Wrong finishing button and unsupported UI descriptions. Lead-in is pasted twice ('Here's how to set it for 6:30.' then 'Here's how. It takes about a minute.'). Earlier turn asks two questions, which should be changed to one (see tr066-b).
- fix requested: Rewrite the steps to match the page: 1. Open the **Clock** app, then tap the **Alarms** tab. 2. Tap the **Add** button. 3. Set the time to 6:30 AM. 4. (optional) Tap **Repeat** to choose days. 5. Tap **Done**. Remove 'at the bottom', '(+)' and 'Save (on some versions, Done)'. Keep the Silent/Do Not Disturb, Sounds & Haptics > Ringtone and Alerts, and Sound/None lines. Use one lead-in sentence only.
- unsupported claims: 'Tap **Alarms** at the bottom.' -> page says only 'tap the Alarms tab'; no position given | 'Tap the **plus (+)** button.' -> page says 'Tap the Add button'; the icon has no alt text or description | 'Tap **Save** (on some versions, **Done**).' -> page says tap Done when creating an alarm; Save appears only when editing an existing alarm
- required actions missing from the reply: Tap Done when creating a new alarm (Save is only for editing an existing alarm) (critical)
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118444

## tr067-c
- reasons: Asks two questions (7 AM or PM, and phone type). AM/PM does not change the steps, and there are two question marks.
- fix requested: Ask only: 'Sure. Is your phone an **iPhone** or an **Android** phone?' (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/2840926?hl=en

## tr068-a
- reasons: Unsupported audiologist referral; step 6 bundles two branches plus the Pair tap in one step.
- fix requested: (1) Replace 'Your audiologist can also help.' with page-supported help: 'If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.' (2) Split step 6 into two steps: '6. Tap **Pair MFi Hearing Device** and follow the steps on the screen. 7. Select your hearing aids, then tap **Pair**.' Then add: 'If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.'
- unsupported claims: 'Your audiologist can also help.' -> the page does not mention audiologists; it points to the hearing device's user guide, the manufacturer's app, and the vendor
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108780

## tr068-c
- reasons: Unsupported audiologist referral; step 6 bundles actions. Lead-in is pasted twice ('Here's how to connect them:' then 'Here's how to pair them. It takes a few minutes.').
- fix requested: (1) Replace 'Your audiologist can also help.' with page-supported help: 'If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.' (2) Split step 6 into two steps: '6. Tap **Pair MFi Hearing Device** and follow the steps on the screen. 7. Select your hearing aids, then tap **Pair**.' Then add: 'If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.' Also use a single lead-in sentence.
- unsupported claims: 'Your audiologist can also help.' -> the page does not mention audiologists; it points to the hearing device's user guide, the manufacturer's app, and the vendor
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108780

## tr068-d
- reasons: Unsupported audiologist referral; step 6 bundles two branches plus the Pair tap in one step.
- fix requested: (1) Replace 'Your audiologist can also help.' with page-supported help: 'If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.' (2) Split step 6 into two steps: '6. Tap **Pair MFi Hearing Device** and follow the steps on the screen. 7. Select your hearing aids, then tap **Pair**.' Then add: 'If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.'
- unsupported claims: 'Your audiologist can also help.' -> the page does not mention audiologists; it points to the hearing device's user guide, the manufacturer's app, and the vendor
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108780

## tr069-a
- reasons: Pairing-mode step and the Refresh troubleshooting line are not supported by the cited page as worded.
- fix requested: Add a second source https://support.google.com/android/answer/9769184?hl=en (it says 'Check that your accessory is discoverable and ready to pair' and 'Follow the instructions that came with your accessory'). Reword step 1: 'Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.' (avoid the unsourced claim that brands differ). Reword troubleshooting: 'If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.' Keep the 0000/1234 line.
- unsupported claims: 'Put your headphones in **pairing mode**. Each brand does this differently, so check the instructions that came with them.' -> the cited page has no text about pairing mode or the accessory's instructions | 'If your headphones don't appear, check under **Available devices**, or tap **More** and then **Refresh**.' -> the page gives this only for when the 'Pair new device' option is missing, not for when the headphones don't show up
- required actions missing from the reply: Make the headphones discoverable / ready to pair, following their instructions (critical; NOT on the cited page, see https://support.google.com/android/answer/9769184?hl=en)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9417604?hl=en

## tr069-c
- reasons: Two questions (what won't connect, and iPhone or Android). Two question marks.
- fix requested: Ask one question only: 'It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9417604?hl=en

## tr069-d
- reasons: Pairing-mode step and the Refresh troubleshooting line are not supported by the cited page as worded.
- fix requested: Add a second source https://support.google.com/android/answer/9769184?hl=en (it says 'Check that your accessory is discoverable and ready to pair' and 'Follow the instructions that came with your accessory'). Reword step 1: 'Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.' (avoid the unsourced claim that brands differ). Reword troubleshooting: 'If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.' Keep the 0000/1234 line.
- unsupported claims: 'Put your headphones in **pairing mode**. Each brand does this differently, so check the instructions that came with them.' -> the cited page has no text about pairing mode or the accessory's instructions | 'If your headphones don't appear, check under **Available devices**, or tap **More** and then **Refresh**.' -> the page gives this only for when the 'Pair new device' option is missing, not for when the headphones don't show up
- required actions missing from the reply: Make the headphones discoverable / ready to pair, following their instructions (critical; NOT on the cited page, see https://support.google.com/android/answer/9769184?hl=en)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9417604?hl=en

## tr070-a
- reasons: Number stated differently from the page.
- fix requested: Change the last sentence to 'It turns off by itself once the battery is charged to 80% or higher.'
- unsupported claims: 'It turns off by itself once you charge above 80%.' -> page says 'When you charge the device to 80% or higher'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101604

## tr070-d
- reasons: Number stated differently from the page. The user said iPhone 14 but the reply still gives the 'iPhone 15 and newer' branch and the 'older iPhones' branch.
- fix requested: Change the last sentence to 'It turns off by itself once the battery is charged to 80% or higher.' In Settings step 3 say only: 'Turn on **Low Power Mode**.' (iPhone 14 and earlier: Settings > Battery > Low Power Mode) and drop the iPhone 15 branch.
- unsupported claims: 'It turns off by itself once you charge above 80%.' -> page says 'When you charge the device to 80% or higher'
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101604

## tr071-a
- reasons: 'Turn it on' step is not on the cited page.
- fix requested: Make step 3 match the page: 'Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.' If the writer wants an explicit 'turn it on' step, add a second official Google/Android page that names the switch and cite it. Keep the dark-theme/background and 'some phones call it low power mode' lines.
- unsupported claims: 'Tap **Battery Saver** and turn it on.' -> the page's step 3 is 'Choose a schedule for battery saver mode or automatically turn it off'; it names no on/off switch, so 'turn it on' is not supported
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7664692?hl=en

## tr071-c
- reasons: 'Turn it on' step is not on the cited page. Lead-in is pasted twice ('Here's how to turn it on. Menu names on Samsung phones can differ a little:' then 'Here's how. It takes less than a minute.').
- fix requested: Make step 3 match the page: 'Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.' If the writer wants an explicit 'turn it on' step, add a second official Google/Android page that names the switch and cite it. Keep the dark-theme/background and 'some phones call it low power mode' lines. Use a single lead-in sentence that includes the Samsung hedge.
- unsupported claims: 'Tap **Battery Saver** and turn it on.' -> the page's step 3 is 'Choose a schedule for battery saver mode or automatically turn it off'; it names no on/off switch, so 'turn it on' is not supported
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7664692?hl=en

## tr071-d
- reasons: 'Turn it on' step is not on the cited page.
- fix requested: Make step 3 match the page: 'Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.' If the writer wants an explicit 'turn it on' step, add a second official Google/Android page that names the switch and cite it. Keep the dark-theme/background and 'some phones call it low power mode' lines.
- unsupported claims: 'Tap **Battery Saver** and turn it on.' -> the page's step 3 is 'Choose a schedule for battery saver mode or automatically turn it off'; it names no on/off switch, so 'turn it on' is not supported
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7664692?hl=en

## tr072-d
- reasons: Added safety tip is not on the cited page (the intent is good, but nothing may be added from memory). The lead-in ends with 'then:' and is followed by a second lead-in ('Here's how to update them all at once.'), and 'Open the App Store' is said twice.
- fix requested: Delete 'Open the App Store from your Home Screen, not from a link in a message, then:' (or support it with a second Apple page). Use one lead-in: 'Thanks. Here's how to update your banking app.' Then step 1 'Open the **App Store**', and in step 4 stress tapping **Update** next to the banking app, with **Update All** as the alternative.
- unsupported claims: 'Open the App Store from your Home Screen, not from a link in a message' -> not on the cited page (nothing about links in messages)
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102629

## tr073-a
- reasons: Missing the 'tap the screen' step needed to start full-screen zoom; volume-key option misworded.
- fix requested: (1) In the shortcut list say 'pressing and holding both volume keys' (page label: Hold volume keys). (2) In 'Use it', after 'Start magnification with your shortcut' add a step: 'Tap anywhere on the screen, except the keyboard or the navigation bar.' (the page requires this for full-screen zoom; with Triple-tap the triple-tap itself starts it). Then keep pinch, two-finger drag, and use the shortcut again to stop.
- unsupported claims: '**pressing both volume keys**' -> the page's option is 'Hold volume keys' ('Press and hold both volume keys')
- required actions missing from the reply: Start with the shortcut, then tap anywhere on the screen except the keyboard or navigation bar (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr073-c
- reasons: Missing the 'tap the screen' step needed to start full-screen zoom; volume-key option misworded.
- fix requested: (1) In the shortcut list say 'pressing and holding both volume keys' (page label: Hold volume keys). (2) In 'Use it', after 'Start magnification with your shortcut' add a step: 'Tap anywhere on the screen, except the keyboard or the navigation bar.' (the page requires this for full-screen zoom; with Triple-tap the triple-tap itself starts it). Then keep pinch, two-finger drag, and use the shortcut again to stop.
- unsupported claims: '**pressing both volume keys**' -> the page's option is 'Hold volume keys' ('Press and hold both volume keys')
- required actions missing from the reply: Start with the shortcut, then tap anywhere on the screen except the keyboard or navigation bar (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr073-d
- reasons: Missing the 'tap the screen' step needed to start full-screen zoom; volume-key option misworded.
- fix requested: (1) In the shortcut list say 'pressing and holding both volume keys' (page label: Hold volume keys). (2) In 'Use it', after 'Start magnification with your shortcut' add a step: 'Tap anywhere on the screen, except the keyboard or the navigation bar.' (the page requires this for full-screen zoom; with Triple-tap the triple-tap itself starts it). Then keep pinch, two-finger drag, and use the shortcut again to stop.
- unsupported claims: '**pressing both volume keys**' -> the page's option is 'Hold volume keys' ('Press and hold both volume keys')
- required actions missing from the reply: Start with the shortcut, then tap anywhere on the screen except the keyboard or navigation bar (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr074-a
- reasons: Lost Mode (the protective action) is only named, with no steps to turn it on; Play Sound path also not given.
- fix requested: Add the Lost Mode steps from the page: 'Open **Find My**, tap **Devices**, select your iPhone, tap **More**, scroll down and turn on **Lost Mode**. You can add a phone number and a message, then tap **Activate**.' Also say how to play a sound: 'Tap your iPhone and use **Play Sound**.' On a computer: 'If you're asked for a verification code, select **Find Devices** instead.' Keep the scam warning (it is supported). Stay under the 2,200 character cap.
- required actions missing from the reply: Lost Mode: Find My > Devices > select iPhone > More > scroll to Lost Mode > (optional contact number and message) > Activate; on icloud.com mark as lost; if asked for a verification code select Find Devices
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101593

## tr074-b
- reasons: Two questions (iPhone or Android, and whether another device is available). The second does not change the steps because both device and computer options are given.
- fix requested: Keep the empathy line and ask one question only: 'I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?' Update tr074-d's first assistant turn to match.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101593

## tr074-c
- reasons: Lost Mode (the protective action) is only named, with no steps to turn it on; Play Sound path also not given.
- fix requested: Add the Lost Mode steps from the page: 'Open **Find My**, tap **Devices**, select your iPhone, tap **More**, scroll down and turn on **Lost Mode**. You can add a phone number and a message, then tap **Activate**.' Also say how to play a sound: 'Tap your iPhone and use **Play Sound**.' On a computer: 'If you're asked for a verification code, select **Find Devices** instead.' Keep the scam warning (it is supported). Stay under the 2,200 character cap.
- required actions missing from the reply: Lost Mode: Find My > Devices > select iPhone > More > scroll to Lost Mode > (optional contact number and message) > Activate; on icloud.com mark as lost; if asked for a verification code select Find Devices
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101593

## tr074-d
- reasons: Lost Mode steps missing. The user said they are on a laptop, yet the reply says 'Good, your laptop will work.' and then repeats 'You'll need another device or a computer.' and still gives the Option 1 steps for another Apple device.
- fix requested: Add the Lost Mode steps from the page: 'Open **Find My**, tap **Devices**, select your iPhone, tap **More**, scroll down and turn on **Lost Mode**. You can add a phone number and a message, then tap **Activate**.' Also say how to play a sound: 'Tap your iPhone and use **Play Sound**.' On a computer: 'If you're asked for a verification code, select **Find Devices** instead.' Keep the scam warning (it is supported). Stay under the 2,200 character cap. Because the user is on a laptop, give only the computer steps (icloud.com/find, sign in with the Apple Account, All Devices) and drop Option 1; remove the repeated 'You'll need another device or a computer.' Earlier turn has two questions; change it as in tr074-b.
- required actions missing from the reply: Lost Mode: Find My > Devices > select iPhone > More > scroll to Lost Mode > (optional contact number and message) > Activate; on icloud.com mark as lost; if asked for a verification code select Find Devices
- low scores: {'steps': 1, 'constraints': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101593

## tr075-a
- reasons: Missing the PIN prompt and the confirm tap for Mark as lost (the protective action).
- fix requested: Add the missing actions from the page: after selecting the phone, 'If asked, enter your lock screen PIN or password' (page: the phone's lock screen PIN); under Mark as lost add 'add a message and phone number, then tap **Mark as lost** again to confirm.' Keep the Play sound / Factory reset text (supported).
- required actions missing from the reply: If prompted, enter the phone's lock screen PIN (Android 9 and up) | Mark as lost: locks the phone, adds contact info and a message, then tap Mark as lost again to confirm
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/accounts/answer/6160491?hl=en

## tr075-b
- reasons: Two questions with two question marks (iPhone or Android, and whether a computer or another phone is available). The second does not change the steps.
- fix requested: Ask one question only: 'Let's try to find it. Is it an **iPhone** or an **Android** phone?' Update tr075-d's first assistant turn to match.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/accounts/answer/6160491?hl=en

## tr075-c
- reasons: One question mark but two asks (phone type, and whether a computer or another phone is available). The second does not change the steps.
- fix requested: Ask one question only: 'I'm sorry, let's try to find it. Is it an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/accounts/answer/6160491?hl=en

## tr075-d
- reasons: Missing the PIN prompt and the confirm tap for Mark as lost. The user will use their husband's phone, whose type is unknown, but the steps cover only an Android phone or a computer.
- fix requested: Add the missing actions from the page: after selecting the phone, 'If asked, enter your lock screen PIN or password' (page: the phone's lock screen PIN); under Mark as lost add 'add a message and phone number, then tap **Mark as lost** again to confirm.' Keep the Play sound / Factory reset text (supported). Add: 'If your husband's phone isn't an Android phone, open a web browser on it and go to **google.com/android/find**' (page: without an Android device, use a browser). Earlier turn has two questions; change it as in tr075-b.
- required actions missing from the reply: If prompted, enter the phone's lock screen PIN (Android 9 and up) | Mark as lost: locks the phone, adds contact info and a message, then tap Mark as lost again to confirm
- low scores: {'steps': 1, 'constraints': 1} | gates not passed: {}
- sources: https://support.google.com/accounts/answer/6160491?hl=en
