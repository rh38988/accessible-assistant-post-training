# Revision list: batch ex1, after review round 1 (13 examples)

Edit ONLY these examples in data/v2/specs/ex1.py, then rebuild.

## pilot-001
- reasons: Source page ends at 'Font size and style > adjust the options as desired'. The gear icon, slider, slide-right direction and live sample text are not supported.
- fix requested: Delete 'Its icon looks like a gear.' Replace step 4 with 'Adjust the options on that screen until the letters are easy to read.' Delete the sentences about the sample words changing as you slide and about messages using the bigger size. Keep the hedge about menu names. The page also says High contrast fonts is under Accessibility > Visibility enhancements; do not add it unless the user asks.
- unsupported claims: 'Its icon looks like a gear.' -> the Samsung page does not describe the Settings icon | 'Find the font size slider and slide it to the right to make the letters bigger.' -> the page only says 'adjust the options as desired'; no slider or direction is described | 'The sample words on the screen change size as you slide' -> not on the page | 'Your messages will use the bigger size too.' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

## pilot-002
- reasons: Asking is correct (the Android page steps do not apply to iPhone). The question is one question. But the apple-logo identification tip is from memory and not on the cited page.
- fix requested: Delete the sentence 'If you're not sure, look at the back of the phone. An iPhone has an apple logo on the back.' Replace with a short sentence such as 'If you're not sure, tell me the name on the phone or the box and I'll help.' Keep the single question.
- unsupported claims: 'An iPhone has an apple logo on the back.' -> the cited Android page does not mention iPhone or any way to identify a phone
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## pilot-003
- reasons: Steps match the page, but icon descriptions and positions and the 'what you will see' lines are not on the page.
- fix requested: Step 3: 'Tap the **Gallery** icon.' (remove position and 'It looks like a small picture', remove 'Your photos will appear.'). Step 5: 'Tap the **Send** icon, the paper-plane shaped button.' Delete the sentence 'You'll see the picture appear in your conversation once it's sent.' Keep the closing hedge about a different messaging app.
- unsupported claims: 'Next to the box where you type, tap the **Gallery** icon. It looks like a small picture.' -> the page gives no position or visual description of the Gallery icon | 'Tap the **Send** button. It looks like an arrow.' -> the page shows a paper-plane-style button; 'arrow' is not what it says | 'Your photos will appear.' -> not on the page | 'You'll see the picture appear in your conversation once it's sent.' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/6159880?hl=en

## pilot-004
- reasons: A question is needed (page splits Face ID / Touch ID with side button / Touch ID with top button). But the Home-button description is from memory, and a yes/no Home button question does not separate the two Touch ID models, whose steps differ.
- fix requested: Replace the question with one question using the page's categories: 'Do you know which iPhone model you have, for example iPhone 8 or iPhone 13?' (one question mark, no Home-button description, no steps). Remove 'Just answer yes or no.'
- unsupported claims: 'a **round button below the screen** (called the Home button)' -> the page never describes the Home button's shape or position or says which iPhones have one
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/102616

## pilot-005
- reasons: Missing information is real, but the reply asks two questions (where she reads email, and what follows the @ sign). Rubric S2 requires ONE question. The cited page covers only Gmail not loading, so the provider is the detail that decides whether it applies.
- fix requested: Keep the warm first paragraph. Replace the two questions with one: 'What is at the end of your email address, for example @gmail.com or @yahoo.com?' Delete the question about where she reads email.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7074871?hl=en

## pilot-006
- reasons: The reply asks two questions (computer or phone, then Windows or Mac) and states what the green light means, which is not on the page. The page covers only Windows 10 and 11, so the deciding detail is whether it is a Windows computer.
- fix requested: Delete the green-light sentence (or say only 'I'm glad the light is on' without claiming meaning). Ask ONE question, for example: 'Are you printing from a Windows computer?' Remove the computer-or-phone and Mac wording.
- unsupported claims: 'The green light is a good sign: it means the printer has power.' -> the Microsoft page never mentions a green light or what it means
- low scores: {'ask_or_answer': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

## pilot-007
- reasons: Core steps match 111107, but many control descriptions, the Join button, the case-sensitivity note and the retype tip are unsupported. Same problem affects tr007-r's first turn.
- fix requested: Step 1: 'Open the **Settings** app.' (drop gray gear). Step 2: 'Tap **Wi-Fi**.' Step 3: 'Make sure Wi-Fi is turned on.' Step 4: 'Tap **SmithHome** in the list.' Step 5: 'Type the password from the card if it asks.' Step 6: delete the Join step, or say 'Confirm the connection.' Success line: 'You'll see a blue tick next to **SmithHome**, and the Wi-Fi icon at the top corner of the screen.' Delete the retype tip. Keep 'move closer to the router' (supported by https://support.apple.com/en-euro/111786).
- unsupported claims: 'Its icon is a gray gear.' -> Apple page gives no icon description | 'Tap **Wi-Fi** near the top.' -> position not on the page | 'the switch next to **Wi-Fi** is on (green)' -> colour not on the page | 'Capital and small letters must match exactly.' -> not on the page | 'Tap **Join**.' -> page does not name a Join button (it says 'confirm the connection') | 'a Wi-Fi symbol (it looks like a fan)' -> page says only 'the Wi-Fi icon' | 'tap **SmithHome** again and retype it slowly' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-au/111107 ; https://support.apple.com/en-euro/111786

## pilot-008
- reasons: Core steps right. Position of Start, example percentages and the restart claim are not supported; the page says sign out and back in.
- fix requested: Step 1: 'Click the **Start** button (the Windows logo).' Step 4: 'Under **Scale & layout**, open the **Scale** dropdown.' Step 5: 'Choose a bigger percentage.' Final paragraph: replace 'restart the computer' with 'sign out and back in'. Remove 'at the bottom of the screen', '100%', '125% or 150%'.
- unsupported claims: 'at the bottom of the screen' -> position of Start not on the page | 'click the box with a percentage in it, such as 100%' and 'like 125% or 150%' -> page says open the Scale dropdown and choose a percentage; no specific numbers | 'Some programs may look right only after you restart the computer.' -> page says some apps may need you to sign out and back in, not restart
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

## pilot-009
- reasons: The message is cut off so a question is right, but the reply asks two questions (which device, and what happens when you go online). Rubric S2 requires ONE.
- fix requested: Keep the first sentence. Replace the two bold questions with one: 'Which device is having trouble with the internet, for example your phone, computer, or TV?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-euro/111786

## pilot-010
- reasons: Missing the page's final choice (Remove Other Devices / Keep All Devices Signed In). Passcode and type-twice claims are unsupported. Safety is fine: no code or password is requested, and the protective warning is included.
- fix requested: Merge steps 5 and 6 into: 'Follow the instructions on the screen to set your new password.' Add a step: 'If it asks, choose **Remove Other Devices** (other devices must sign in again) or **Keep All Devices Signed In**.' Delete the passcode sentence. Change the parenthesis to '(Apple calls this your Apple Account.)'. Keep the one-hour wait (rephrase: 'You may have to wait one hour before you can change it') and the safety warning.
- unsupported claims: 'If it asks for a passcode, use the one you use to unlock your iPhone.' -> the iPhone steps on the page do not mention a passcode prompt | 'Type your new password twice, then confirm.' -> page says only 'follow the onscreen instructions' | '(Apple now calls the Apple ID an **Apple Account**.)' -> page uses 'Apple Account' but does not say it was renamed
- required actions missing from the reply: Choose Remove Other Devices or Keep All Devices Signed In
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-mz/101567 ; https://support.apple.com/en-us/ht201487

## pilot-011
- reasons: Steps match, but the restart and duration paragraph is not on the page.
- fix requested: Delete 'The update can take a while, and your iPhone will turn off and back on by itself. Start when you won't need your phone for a bit.' Optionally replace with 'Follow the instructions on the screen.' Replace step 8 with 'Follow the instructions on the screen (it may ask for your passcode).' Keep the storage note and add that you tap **Continue** to allow it.
- unsupported claims: 'The update can take a while, and your iPhone will turn off and back on by itself. Start when you won't need your phone for a bit.' -> page mentions neither restart nor duration | 'Enter your iPhone passcode if asked.' -> page only links 'If you don't know your passcode'; weakly supported | 'Updates are generally a good idea because they fix problems' -> page supports 'security updates and bug fixes', so this is acceptable
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ie/118575

## pilot-012
- reasons: Respects the user's constraint (skips writing the email). Icon name, file-picker layout, wait-then-Send and the reassurance about the link are not supported.
- fix requested: Step 1: 'At the bottom of the message window, click the **Attach** icon.' Step 2: 'Select the photo **birthday.jpg**. It is in your Pictures folder.' (remove 'On the left side, click Pictures' and merge with step 3). Step 4: 'Click **Open**.' Replace the last two paragraphs: 'You'll see the file appear in your email. If the photo is bigger than 25 MB, Gmail puts a Google Drive link in the email instead.' Remove the Send and wait instruction.
- unsupported claims: 'Click the **paperclip** icon.' -> page says the **Attach** icon (labeled 'Attach'); paperclip not stated | 'On the left side, click **Pictures**.' -> file picker layout not on the page | 'Wait until it finishes loading, then click **Send**.' -> not on the page | 'That's fine: your son can still open it.' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/6584

## pilot-013
- reasons: First turn correctly asks one question; final steps match the page. Green colour, Wi-Fi and charging advice, and the storage-full message are unsupported.
- fix requested: Step 5: 'Turn on the switch next to **Sync this iPhone**.' Delete 'so it turns green'. Delete 'If you have a lot of photos... Wi-Fi and charging.' and the iCloud storage paragraph. Optionally add: 'To see your photos in iCloud, open the **Photos** app and tap **Library**.'
- unsupported claims: 'so it turns green' -> colour not on the page | 'it's best to leave your phone connected to Wi-Fi and charging' -> page says nothing about Wi-Fi or charging | 'If your iCloud storage fills up, your iPhone will let you know.' -> not on the page
- required actions missing from the reply: Optional: view synced photos in Photos app > Library
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48
