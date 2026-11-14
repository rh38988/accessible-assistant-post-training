# Revision list: batch ex3, after review round 2 (18 examples)

Edit ONLY these examples in data/v2/specs/ex3.py, then rebuild.

## tr033-a
- reasons: Unsupported claim that the update can show a not-enough-space message. The earlier System update label fix is applied correctly.
- fix requested: Delete the final paragraph 'If it says there isn't enough space, tell me and I'll help you free some up first.' Change nothing else.
- unsupported claims: 'If it says there isn't enough space, tell me and I'll help you free some up first.' -> the page never says an update shows a not-enough-space or storage message, so this claim has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7680439?hl=en

## tr033-d
- reasons: Unsupported claim that the update can show a not-enough-space message (same sentence as tr033-a).
- fix requested: In the final reply, delete the closing paragraph 'If it says there isn't enough space, tell me and I'll help you free some up first.' Change nothing else.
- unsupported claims: 'If it says there isn't enough space, tell me and I'll help you free some up first.' -> the page never says an update shows a not-enough-space or storage message, so this claim has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7680439?hl=en

## tr035-a
- reasons: Specific setup time 'a couple of minutes' is not on the page.
- fix requested: Delete the sentence 'It takes a couple of minutes to turn on.' Keep the rest. The page says backup 'can take a while' to finish, which the later paragraph already covers.
- unsupported claims: 'It takes a couple of minutes to turn on.' -> the page gives no setup time; it only says backup can take a while to finish, depending on connection and upload size. Specific duration has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

## tr035-c
- reasons: Specific setup time 'a couple of minutes' is not on the page (same sentence as tr035-a).
- fix requested: In the reply, delete the sentence 'It takes a couple of minutes to turn on.' Keep the rest, including the empathy line.
- unsupported claims: 'It takes a couple of minutes to turn on.' -> the page gives no setup time; it only says backup can take a while to finish, depending on connection and upload size. Specific duration has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

## tr035-d
- reasons: Specific setup time 'a couple of minutes' is not on the page (same sentence as tr035-a).
- fix requested: In the final reply, delete the sentence 'It takes a couple of minutes to turn on.' Keep the rest.
- unsupported claims: 'It takes a couple of minutes to turn on.' -> the page gives no setup time; it only says backup can take a while to finish, depending on connection and upload size. Specific duration has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

## tr036-a
- reasons: Control position 'next to Add a printer & scanner' is not on the page. The rest of the steps match the page.
- fix requested: Step 5: replace 'next to Add a printer & scanner, click Add device.' with 'click Add a printer & scanner, then click Add device.' Change nothing else.
- unsupported claims: 'next to Add a printer & scanner, click Add device.' -> the page says to select Add a printer & scanner, then select Add device; it does not place Add device next to Add a printer & scanner, so the position is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

## tr036-d
- reasons: Control position 'next to Add a printer & scanner' is not on the page (same step as tr036-a).
- fix requested: Step 5: replace 'next to Add a printer & scanner, click Add device.' with 'click Add a printer & scanner, then click Add device.' Change nothing else.
- unsupported claims: 'next to Add a printer & scanner, click Add device.' -> the page says to select Add a printer & scanner, then select Add device; it does not place Add device next to Add a printer & scanner, so the position is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

## tr037-d
- reasons: States the 25 MB Drive-link limit as universal; the page limits it to personal Gmail accounts. The steps match the page.
- fix requested: Replace 'If the attachments are over 25 MB, Gmail adds them as a Google Drive link instead.' with 'If the attachments are over 25 MB on a personal Gmail account, Gmail adds them as a Google Drive link instead. Work and school accounts can have a different limit set by their administrator.' Change nothing else.
- unsupported claims: 'If the attachments are over 25 MB, Gmail adds them as a Google Drive link instead.' -> the page gives 25 MB only for personal Gmail accounts and says work and school limits are set by the Google Workspace administrator; stated as a general limit it is wrong for those accounts.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

## tr041-a
- reasons: Two unsupported claims: 'very hard to get back' and the 'look on the card or search online' instruction.
- fix requested: (1) Replace 'Once you share the numbers, the money is very hard to get back.' with 'Once you share the numbers, act quickly, because the company may be able to freeze the card or return the money.' (2) Replace 'If yours isn't listed, look on the card or search online for the company that issued it.' with 'If yours isn't listed, the FTC page lists other companies that use online chat, forms, or support pages.' Change nothing else.
- unsupported claims: 'Once you share the numbers, the money is very hard to get back.' -> the page does not say this. It says some companies help stop these scams and may return the money, and it advises reporting right away. | 'If yours isn't listed, look on the card or search online for the company that issued it.' (also 'If your friend's isn't listed, they can look on the card or search online for the company that issued it.') -> the page does not tell readers to look on the card or search online. It says other companies are listed with online chat, forms, or support pages.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr041-c
- reasons: 'look on the card or search online for the company' is not on the FTC page.
- fix requested: Replace 'If your friend's isn't listed, they can look on the card or search online for the company that issued it.' with 'If your friend's isn't listed, the FTC page lists other companies that use online chat, forms, or support pages.' Change nothing else.
- unsupported claims: 'If yours isn't listed, look on the card or search online for the company that issued it.' (also 'If your friend's isn't listed, they can look on the card or search online for the company that issued it.') -> the page does not tell readers to look on the card or search online. It says other companies are listed with online chat, forms, or support pages.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr041-d
- reasons: 'the money is very hard to get back' is not on the FTC page, which suggests recovery is possible.
- fix requested: Replace 'Once you share the numbers, the money is very hard to get back.' with 'Once you share the numbers, act quickly, because the company may be able to freeze the card or return the money.' Change nothing else.
- unsupported claims: 'Once you share the numbers, the money is very hard to get back.' -> the page does not say this. It says some companies help stop these scams and may return the money, and it advises reporting right away.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr042-a
- reasons: On-screen label 'Add Member' is not on the page, which shows that button only as an icon with alt text 'Member button'.
- fix requested: Step 5: replace 'Tap the Add Member button.' with 'Tap the Member button (the page shows it as an icon, not a text label).' Change nothing else.
- unsupported claims: 'Tap the Add Member button' -> the page does not show 'Add Member' as a text label; it describes this button only by its icon and alt text ('Member button'), so the on-screen label is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108380

## tr042-d
- reasons: On-screen label 'Add Member' is not on the page (same step as tr042-a).
- fix requested: Step 5: replace 'Tap the Add Member button.' with 'Tap the Member button (the page shows it as an icon, not a text label).' Change nothing else.
- unsupported claims: 'Tap the Add Member button' -> the page does not show 'Add Member' as a text label; it describes this button only by its icon and alt text ('Member button'), so the on-screen label is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108380

## tr043-a
- reasons: Describes the Add control as an icon, which the page does not say. The steps otherwise match the page.
- fix requested: Step 2: replace 'Tap the Add icon at the bottom right.' with 'Tap Add at the bottom right.' In the last paragraph, replace 'you don't see an Add icon' with 'you don't see Add'. Change nothing else.
- unsupported claims: 'Tap the **Add** icon at the bottom right.' (and 'you don't see an **Add** icon') -> the page says to tap Add at the bottom right; it does not describe the control as an icon or its shape, so 'icon' is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

## tr043-d
- reasons: Describes the Add control as an icon, which the page does not say (same as tr043-a).
- fix requested: Step 2: replace 'Tap the Add icon at the bottom right.' with 'Tap Add at the bottom right.' In the last paragraph, replace 'you don't see an Add icon' with 'you don't see Add'. Change nothing else.
- unsupported claims: 'Tap the **Add** icon at the bottom right.' (and 'you don't see an **Add** icon') -> the page says to tap Add at the bottom right; it does not describe the control as an icon or its shape, so 'icon' is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

## tr045-a
- reasons: Claims blocked calls won't ring; the page does not say that either way.
- fix requested: In the paragraph after the steps, delete 'calls from that number won't ring your phone, and'. Keep 'the caller won't be told they're blocked' and the voicemail sentence, starting that sentence with 'The caller won't be told they're blocked.' Change nothing else.
- unsupported claims: 'calls from that number won't ring your phone' -> the page says it does not state directly whether calls still ring; the claim has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/111104

## tr045-d
- reasons: Claims blocked calls won't ring; the page does not say that (same as tr045-a).
- fix requested: In the final paragraph, delete 'calls from that number won't ring your phone, and'. Keep 'the caller won't be told they're blocked' and the voicemail sentence, starting that sentence with 'The caller won't be told they're blocked.' Change nothing else.
- unsupported claims: 'calls from that number won't ring your phone' -> the page says it does not state directly whether calls still ring; the claim has no source.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/111104

## tr046-d
- reasons: Says the steps are for a Pixel, which the page does not mention. The steps match the page for Google's Phone app.
- fix requested: Replace 'Thanks, here's how on your Pixel.' with 'Thanks, here's how in Google's Phone app.' Change nothing else.
- unsupported claims: 'Thanks, here's how on your Pixel.' -> the page does not mention Pixel phones; it only describes steps in Google's Phone app.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en
