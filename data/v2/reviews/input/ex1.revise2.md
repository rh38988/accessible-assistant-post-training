# Revision list: batch ex1, after review round 2 (6 examples)

Edit ONLY these examples in data/v2/specs/ex1.py, then rebuild.

## pilot-003
- reasons: Source gate fails on one unsupported location claim. All required actions are covered and every score is 2.
- fix requested: In the last paragraph, remove the words "next to the typing box". Keep the rest of the paragraph as written, so it reads: "If you don't see a Gallery icon, your phone may use a different messaging app. Tell me what icons you see and I'll guide you from there."
- unsupported claims: "icons you see next to the typing box" -> the page describes no location for the icons next to the message box or typing area; it only shows the Gallery and Send icons without giving their position
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/6159880?hl=en

## pilot-007
- reasons: Step 6 is not an action the source describes, so the source gate fails. It is also vague, so actionable scores 1. The move-closer advice in the last paragraph is supported by the router section of the second cited page (111786, 'you might be too far from the signal') and is not counted against the reply.
- fix requested: Delete step 6 ("6. Confirm the connection."). Leave steps 1 to 5 as they are, and keep the paragraph that begins "When you're connected" as the check that the phone is connected. Nothing else needs to change.
- unsupported claims: "6. Confirm the connection." -> neither cited Apple page describes a Join, Confirm, or other confirmation action after tapping the network name; the only check described is the blue tick
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-au/111107 ; https://support.apple.com/en-euro/111786

## pilot-008
- reasons: Two control descriptions (the Windows logo on the Start button, and the gear icon on Settings) are not in the source, so the source gate fails. All required actions are covered and the scores are 2.
- fix requested: In step 1, delete " (the Windows logo)" so it reads "Click the **Start** button." In step 2, delete the sentence "Its icon is a gear." so it reads "Click **Settings**." Leave the other steps unchanged.
- unsupported claims: "Click the **Start** button (the Windows logo)." -> the page names the Start button and the Windows logo key, but says nothing about the Start button showing the Windows logo | "Its icon is a gear." -> the page does not describe the Settings icon
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

## pilot-010
- reasons: Two sentences are not supported by the cited pages, so the source gate fails. The steps themselves are all covered. The sentence "Never give it to anyone who calls or texts you offering help with your account." is supported by https://support.apple.com/en-us/102568 ("never share your Apple Account password or verification codes with anyone"), which is a second official Apple page, but it is not cited yet.
- fix requested: (1) In the first paragraph, replace "because you can still open your iPhone, you can make a new password right on the phone" with "you can make a new password right on your iPhone if it is already signed in to your Apple Account". (2) Delete the sentence "Write the new password down and keep it somewhere safe at home." (3) Keep "Never give it to anyone who calls or texts you offering help with your account." and add https://support.apple.com/en-us/102568 as a second source for this example. Leave the steps unchanged.
- unsupported claims: "because you can still open your iPhone, you can make a new password right on the phone" -> the cited page says the easiest method is on a device already signed in to the Apple Account with two-factor authentication; it does not tie the change to opening the phone with the passcode | "Write the new password down and keep it somewhere safe at home." -> neither cited Apple page says to write down or store a new password
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-mz/101567 ; https://support.apple.com/en-us/ht201487

## pilot-012
- reasons: The 25 MB limit is stated as if it applies to every account. The source applies it to personal Gmail accounts only. The steps are all supported and covered.
- fix requested: Replace the last sentence of the reply, "If the photo is bigger than 25 MB, Gmail puts a Google Drive link in the email instead.", with: "In a personal Gmail account, if the attachments are bigger than 25 MB in total, Gmail adds a Google Drive link to the email instead of the file." Leave the steps unchanged.
- unsupported claims: "If the photo is bigger than 25 MB, Gmail puts a Google Drive link in the email instead." -> the page gives the 25 MB limit only for personal Gmail accounts, says work and school accounts use limits set by the Google Workspace administrator, and says the Drive link is added when the total attachment size exceeds the limit
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/6584

## pilot-013
- reasons: One unsupported control position ("at the top") in step 2. The rest of the steps, the switch label, and the Library step are supported. Earlier turns are context only and were not scored.
- fix requested: In step 2, delete the words " at the top" so the step reads "Tap **your name**." Leave all other steps unchanged.
- unsupported claims: "Tap **your name** at the top." -> the page says only to tap "[your name]" and gives no position for it, so "at the top" is an unsupported location
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48
