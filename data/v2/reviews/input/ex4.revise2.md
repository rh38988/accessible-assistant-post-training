# Revision list: batch ex4, after review round 2 (14 examples)

Edit ONLY these examples in data/v2/specs/ex4.py, then rebuild.

## tr051-a
- reasons: Two closing claims are not on the source page (guaranteed delivery to all three; an Android-specific failure). The MMS note also drops the carrier fallback.
- fix requested: Delete the sentence "All three will get your message." Replace the Android sentence with: "If a recipient is not on iMessage, the group is sent as MMS, SMS, or RCS. To send group MMS on iPhone, go to Settings, then Messages, and turn on MMS Messaging. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging." Source: https://support.apple.com/en-us/118236
- unsupported claims: "All three will get your message." -> the page says Messages picks the message type from settings, connection, and carrier plan, and does not explicitly guarantee delivery to every recipient | "If one of your kids has an Android phone and the message won't send, go to Settings, then Messages, and make sure MMS Messaging is turned on." -> the page never mentions Android; it says MMS Messaging is needed for group MMS on iPhone, and that if the option is missing the carrier should be contacted
- required actions missing from the reply: Recipients who are not on iMessage receive the group as MMS, SMS, or RCS
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr051-c
- reasons: Opening and closing sentences promise delivery to everyone, which the page does not guarantee. The Android MMS sentence is not on the page and drops the carrier fallback.
- fix requested: Replace the first sentence with: "You can send one group text from Messages to all three of them." Delete "All three will get your message." Replace the Android sentence with: "If a recipient is not on iMessage, the group is sent as MMS, SMS, or RCS. To send group MMS on iPhone, go to Settings, then Messages, and turn on MMS Messaging. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging." Source: https://support.apple.com/en-us/118236
- unsupported claims: "A group text will send it to all three at once, so no one gets left out." -> the page does not say a group message reaches everyone or that no one is left out | "All three will get your message." -> the page does not explicitly guarantee delivery to every recipient | "If one of your kids has an Android phone and the message won't send, go to Settings, then Messages, and make sure MMS Messaging is turned on." -> the page never mentions Android; it says MMS Messaging is needed for group MMS on iPhone, and that if the option is missing the carrier should be contacted
- required actions missing from the reply: Recipients who are not on iMessage receive the group as MMS, SMS, or RCS
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr051-d
- reasons: Closing claims go beyond the page (delivery to all three; Android-specific failure). The MMS note drops the carrier fallback.
- fix requested: Delete the sentence "All three will get your message." Replace the Android sentence with: "If a recipient is not on iMessage, the group is sent as MMS, SMS, or RCS. To send group MMS on iPhone, go to Settings, then Messages, and turn on MMS Messaging. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging." Source: https://support.apple.com/en-us/118236
- unsupported claims: "All three will get your message." -> the page does not explicitly guarantee delivery to every recipient | "If one of your kids has an Android phone and the message won't send, go to Settings, then Messages, and make sure MMS Messaging is turned on." -> the page never mentions Android; it says MMS Messaging is needed for group MMS on iPhone, and that if the option is missing the carrier should be contacted
- required actions missing from the reply: Recipients who are not on iMessage receive the group as MMS, SMS, or RCS
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr052-a
- reasons: The scope claim "just one page" is not on the page. The steps themselves match the source.
- fix requested: Change the last paragraph to: "To zoom in with the keyboard, press Ctrl and + (on a Mac, press Command and +)." Delete "just one page". Source: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop
- unsupported claims: "To zoom in on just one page, hold the Ctrl key and press +" -> the page gives the Ctrl and + (Command and + on Mac) shortcut but does not say it zooms only one page; its shortcut section names no scope, and its headings refer to a specific site and to all webpages
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr052-d
- reasons: The scope claim "just one page" is not on the page. The steps themselves match the source.
- fix requested: Change the last paragraph to: "To zoom in with the keyboard, press Ctrl and + (on a Mac, press Command and +)." Delete "just one page". Source: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop
- unsupported claims: "To zoom in on just one page, hold the Ctrl key and press +" -> the page gives the Ctrl and + (Command and + on Mac) shortcut but does not say it zooms only one page; its shortcut section names no scope
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr055-a
- reasons: The no-Gmail option says "you can share a link instead" but gives no action; the page's action is to tap Copy to clipboard in place of the contact and Share steps.
- fix requested: Replace "If he doesn't use Gmail, you can share a link instead, which works for up to 24 hours." with: "If he doesn't use Gmail, skip steps 6 and 7. Instead, tap Copy to clipboard, then paste the link into a text or email to him. Anyone with the link can see your location for up to 24 hours." Source: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid
- required actions missing from the reply: Without a Gmail account: tap Copy to clipboard instead of steps 6 and 7, then paste the link into a text or email
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

## tr055-c
- reasons: The no-Gmail option says "you can share a link instead" but gives no action; the page's action is to tap Copy to clipboard in place of the contact and Share steps.
- fix requested: Replace "If he doesn't use Gmail, you can share a link instead, which works for up to 24 hours." with: "If he doesn't use Gmail, skip steps 6 and 7. Instead, tap Copy to clipboard, then paste the link into a text or email to him. Anyone with the link can see your location for up to 24 hours." Source: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid
- required actions missing from the reply: Without a Gmail account: tap Copy to clipboard instead of steps 6 and 7, then paste the link into a text or email
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

## tr059-a
- reasons: The page says some of these steps work only on Android 13 and up; the reply gives no version condition, so older phones may not match the steps.
- fix requested: Add one sentence before the numbered steps: "Some of these steps work only on Android 13 and up." Source: https://support.google.com/googleplay/answer/13627402?hl=en
- required actions missing from the reply: Some of these steps work only on Android 13 and up
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

## tr059-c
- reasons: Overstated claims about how many preinstalled apps can be removed, plus the missing Android 13 condition for the steps.
- fix requested: Change the first two sentences to: "Some apps that came with the phone can't be removed. On certain phones you can turn them off instead. Apps you installed can be uninstalled through the Play Store like this, though some of these steps work only on Android 13 and up." Delete "most" everywhere in the reply. Sources: https://support.google.com/googleplay/answer/13627402?hl=en and https://support.google.com/googleplay/answer/13627571?hl=en
- unsupported claims: "You can remove most of them." -> the page does not say how many preinstalled apps can be removed; it says some system apps cannot be removed | "most apps can be removed through the Play Store like this" -> the page covers uninstalling apps you installed; the 'most' is not on the page | "can only be turned off, not deleted" -> the page says some system apps cannot be removed and that on certain phones you can turn them off, not that turning off is the only option
- required actions missing from the reply: Some of these steps work only on Android 13 and up
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

## tr059-d
- reasons: "Works on most Android phones" is not on the page, and the Android 13 condition is missing.
- fix requested: Replace "Here's one way that works on most Android phones." with: "Here's one way to do it. Some of these steps work only on Android 13 and up." Source: https://support.google.com/googleplay/answer/13627402?hl=en
- unsupported claims: "Here's one way that works on most Android phones." -> the page does not say the steps work on most phones; it says some steps work only on Android 13 and up
- required actions missing from the reply: Some of these steps work only on Android 13 and up
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

## tr060-a
- reasons: The Control Panel fallback for programs that cannot be removed from Settings is missing; the page names it as the method for that case.
- fix requested: Add after step 6: "If the program is not in the list or cannot be removed here, type Control Panel in the search box on the taskbar and open it. Click Programs, then Programs and Features. Right-click the program, choose Uninstall or Uninstall/Change, and follow the directions on the screen." Source: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98
- required actions missing from the reply: Some apps cannot be uninstalled from Settings; use Control Panel, then Programs, Programs and Features, then Uninstall or Uninstall/Change
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

## tr060-d
- reasons: The Control Panel fallback for programs that cannot be removed from Settings is missing; the page names it as the method for that case.
- fix requested: Add after step 6: "If the program is not in the list or cannot be removed here, type Control Panel in the search box on the taskbar and open it. Click Programs, then Programs and Features. Right-click the program, choose Uninstall or Uninstall/Change, and follow the directions on the screen." Source: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98
- required actions missing from the reply: Some apps cannot be uninstalled from Settings; use Control Panel, then Programs, Programs and Features, then Uninstall or Uninstall/Change
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

## tr061-a
- reasons: The buttons are not shown with their on-screen labels; the reply says "offload or delete" where the page names the buttons Offload App and Delete App.
- fix requested: In step 5, replace "choose to offload or delete it" with: "choose Offload App or Delete App." Keep the explanation that Offload App keeps the app's documents and data and Delete App removes the app and its related data. Source: https://support.apple.com/en-us/108429
- required actions missing from the reply: Tap an app's name, then choose Offload App or Delete App (critical)
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108429

## tr061-d
- reasons: The buttons are not shown with their on-screen labels; the reply says "offload or delete" where the page names the buttons Offload App and Delete App.
- fix requested: In step 5, replace "choose to offload or delete it" with: "choose Offload App or Delete App." Keep the explanation that Offload App keeps the app's documents and data and Delete App removes the app and its related data. Source: https://support.apple.com/en-us/108429
- required actions missing from the reply: Tap an app's name, then choose Offload App or Delete App (critical)
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108429
