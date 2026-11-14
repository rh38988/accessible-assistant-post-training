# Revision list: batch ny7a, after review round 1 (12 examples)

Edit ONLY these examples in data/v2/specs/ny7a.py, then rebuild.

## tr199-a
- reasons: source unreadable. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- fix requested: Source page text for the Outlook.com (Web) tab could not be read. Re-verify against the Web tab (or add a readable official Microsoft page for Outlook on the web) and confirm the exact labels Attach, Browse this computer, Browse cloud locations, Next, More actions, Manage access, and the CTRL/Command multi-select claim before re-submitting. Do not change the text until the labels are confirmed.
- unsupported claims: 'select **Attach**' / '**Browse this computer**' / 'hold the CTRL key' -> WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified. The only readable text (New Outlook) says 'Attach File' and 'Browse This Computer'; CTRL multi-select is not on the readable page.
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

## tr199-c
- reasons: source unreadable. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- fix requested: Source page text for the Outlook.com (Web) tab could not be read. Re-verify against the Web tab (or add a readable official Microsoft page for Outlook on the web) and confirm the exact labels Attach, Browse this computer, Browse cloud locations, Next, More actions, Manage access, and the CTRL/Command multi-select claim before re-submitting. Do not change the text until the labels are confirmed.
- unsupported claims: 'Hold down the Command key, then click each of the other three pictures.' -> not on the readable page; Mac Command-key multi-select is not stated in the readable source text. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

## tr199-d
- reasons: source unreadable. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- fix requested: Source page text for the Outlook.com (Web) tab could not be read. Re-verify against the Web tab (or add a readable official Microsoft page for Outlook on the web) and confirm the exact labels Attach, Browse this computer, Browse cloud locations, Next, More actions, Manage access, and the CTRL/Command multi-select claim before re-submitting. Do not change the text until the labels are confirmed.
- unsupported claims: 'Select **Attach**' / '**Browse this computer**' -> WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified. | 'you can also drag the document from your computer into the message' -> readable page mentions drag and drop only for attaching an email in New Outlook, not for files from the computer.
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

## tr199-e
- reasons: source unreadable. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- fix requested: Source page text for the Outlook.com (Web) tab could not be read. Re-verify against the Web tab (or add a readable official Microsoft page for Outlook on the web) and confirm the exact labels Attach, Browse this computer, Browse cloud locations, Next, More actions, Manage access, and the CTRL/Command multi-select claim before re-submitting. Do not change the text until the labels are confirmed.
- unsupported claims: 'Select **Browse cloud locations**' and 'Select **Next**' -> not on the readable page (page says 'Locations include OneDrive, SharePoint sites, or connected third-party cloud storage providers'). | 'select **More actions**, then **Manage access**' -> readable page only says to select Manage access to resolve a warning, and set permissions via the arrow beside the attachment name; 'More actions' is not supported. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

## tr199-r
- reasons: source unreadable. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- fix requested: Source page text for the Outlook.com (Web) tab could not be read. Re-verify against the Web tab (or add a readable official Microsoft page for Outlook on the web) and confirm the exact labels Attach, Browse this computer, Browse cloud locations, Next, More actions, Manage access, and the CTRL/Command multi-select claim before re-submitting. Do not change the text until the labels are confirmed.
- unsupported claims: 'Hold down the CTRL key (the Command key on a Mac)' -> not on the readable page. | 'You can also drag the pictures from your computer into the message.' -> readable page mentions drag and drop only for attaching an email. WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified.
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

## tr200-c
- reasons: Steps 1 and 2 have no starting point: 'Open your mailbox storage page' and 'Free up some space' do not say where the page is or how to free space. The cited page gives no menu path either ('Check your mailbox storage to see what's taking up space').
- fix requested: Add a second official source that gives the path and ways to free space, e.g. https://support.microsoft.com/office/storage-limits-in-outlook-com-7ac99134-69e5-4619-ac0b-2d313bba5e9e (verify it first), then rewrite steps 1-2 with the exact Settings path and the exact label(s) for what to delete or empty. If the path cannot be verified, state the cited-page wording only ('Check your mailbox storage to see what is taking up space') and say plainly that deleting large or old messages and emptying Deleted Items frees space only if the second page supports it.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

## tr200-d
- reasons: Steps 2 and 3 ('Check whether email forwarding is turned on', 'Check for email rules') and step 4 give no starting point or what the user will see; the cited page itself gives no Settings path for these. Step 1 also lacks where to find the Junk Email folder, but the folder name is on the page. Also omits the Other tab/filter check, which the page lists.
- fix requested: Either add a second verified Microsoft page that gives the Settings path for forwarding and rules, and write those steps with exact labels, or cut steps 2-3 to the cited-page wording and keep the reply short. Add the page's 'Check your Other tab and ensure there are no filters preventing you from accessing all your messages' check. For storage, give the path only if a second page supports it.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

## tr200-e
- reasons: Two unsupported reassurance claims, and the Other-tab step ('Make sure you can see all of your messages') could lead the user to change a filter, against their stated limit.
- fix requested: Delete 'This only moves that one message to your Inbox.' and 'None of these steps changes your settings or rules.' Keep: 'Right-click it and select Mark as not junk. This moves it back to your inbox.' Make step 1 look-only: 'Click the Other tab and look through it for the message.' (do not tell the user to adjust filters), and tell them to tell you if they see a filter applied.
- unsupported claims: 'This only moves that one message to your Inbox.' -> the page says only that Mark as not junk moves the message back to the inbox; it does not say nothing else happens. | 'None of these steps changes your settings or rules.' -> 'Make sure you can see all of your messages' on the Other tab may require changing a filter; the page does not support this blanket claim.
- low scores: {'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

## tr201-r
- reasons: One unsupported sentence. Also the page's other 'if nothing turns up' checks (Junk Email, Other tab, filter set to All) are missing, which is a non-critical gap.
- fix requested: Replace 'Check your Archive folder next. Archived messages do not show in your inbox.' with 'Check your Archive folder next, in case the message was archived.' Optionally add after the 30-day line: 'You can also check your Junk Email folder and the Other tab, and make sure your filter is set to All.' Keep the Archive steps (Open Archive, select the message, Move to, then Inbox).
- unsupported claims: 'Archived messages do not show in your inbox.' -> not stated on the page; the page only says 'If you archived the message' select it and Move to > Inbox.
- required actions missing from the reply: (Also on page) Check Junk Email and the Other tab; filter set to All
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

## tr202-a
- reasons: Unsupported icon description.
- fix requested: Delete 'It looks like a plus icon.' Keep 'On the left, next to **Labels**, click **Create new label**.' If you want to describe the control, only do so if another official Google page states it.
- unsupported claims: 'It looks like a plus icon.' -> the page says only 'click Create new label'; its icon has empty alt text and no text describes a plus symbol.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/118708?hl=en

## tr202-r
- reasons: Unsupported icon description.
- fix requested: Change step 1 to: 'At the top right, click **Settings**, then **See all settings**.' (drop 'the gear icon').
- unsupported claims: '**Settings**, the gear icon' -> the page gives the icon alt text 'Settings' only and does not describe a gear.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/118708?hl=en

## tr205-e
- reasons: The direct answer to 'do I have to have an email for him?' is not on the cited page and was added from memory (G1). The four steps themselves are supported.
- fix requested: Delete the sentence 'You do not need an email address.' Replace it with 'Google Contacts can save names, email addresses, phone numbers, and more.' Keep steps 1 to 4 unchanged. Then add one sentence saying that the help page does not say whether an email address is required, so the user can save the plumber's name and phone number now. Do not state a yes or no answer unless a second official Google Contacts page confirms it; if one does, cite it and then give the direct answer.
- unsupported claims: 'You do not need an email address.' -> the page says only 'You can save names, email addresses, phone numbers, and more in Google Contacts' and states that it does not say whether an email address is required (checked twice); the answer to the user's question is not supported by the source.
- required actions missing from the reply: Tell the user whether an email address is required to save a contact (critical for the question asked)
- low scores: {'ask_or_answer': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/contacts/answer/1069522?hl=en
