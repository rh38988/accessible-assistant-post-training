# Revise report: batch ny7a, revision 1 (12 flagged examples)

Builder: `python3 data/v2/tools/build_v2.py ny7a` prints OK with no warnings.

## Fixed
- tr199-a, tr199-c, tr199-d, tr199-e, tr199-r: NARROWED. The cited Outlook page's Outlook.com (web) tab was not readable, and no readable official page gave Outlook.com steps. The steps now cover New Outlook for Windows only: Insert, Attach file, Browse this computer, then select the file (OneDrive as link for tr199-e). The task platform is now "New Outlook for Windows". User messages say "Outlook" or "the new Outlook app on Windows" in place of "Outlook.com" (the Mac examples are now Windows). Removed: Open, Browse cloud locations, Next, More actions, the CTRL/Command multi-select claim, and the drag-and-drop claim. Multi-select is now stated as not found (tr199-c, tr199-r). Second source added: Microsoft "Basic tasks using a screen reader with email in Outlook" (https://support.microsoft.com/en-us/accessibility/outlook/basic-tasks-using-a-screen-reader-with-email-in-outlook?ad=us&rs=en-us&ui=en-us). The task-level source (8d7c...) is kept, but its title still says Outlook.com; only its New Outlook tab was readable.
- tr200-c: steps 1-2 now use the verified path Settings, then Account, then Storage (from https://support.microsoft.com/office/storage-limits-in-outlook-com-7ac99134-69e5-4619-ac0b-2d313bba5e9e, added as second source). Added the page's note that full storage bounces incoming mail.
- tr200-d: Other tab check added (cited page). Forwarding path Settings, Mail, Forwarding (verified on https://support.microsoft.com/en-us/office/turn-on-or-off-automatic-forwarding-in-outlook-com-6246987c-6c8f-4144-b255-14fc07007dad, added as second source). Storage path added from the storage page. The "Check email rules" step was removed: the cited page gives no path for rules, and no readable page with one was found.
- tr200-e: removed "This only moves that one message to your Inbox." and "None of these steps changes your settings or rules." Step 1 is look-only. Final line asks the user to speak up before any filter is changed.
- tr201-r: NOT CHANGED. The reviewer's claim that "Archived messages do not show in your inbox" is unsupported is contradicted by the page: "If you've archived a message, it won't appear in your inbox." The sentence was restored to its original wording.
- tr202-a: removed "It looks like a plus icon." (Page: the icon has no alt text.) Source notes also lost "(the plus icon)".
- tr202-r: removed "the gear icon" (page alt text is only "Settings"). Source notes also lost "(gear icon)".
- tr205-e: removed "You do not need an email address." Now states that Google Contacts can save email addresses, and that the help page does not say whether an email address is required. Steps 1-4 kept. The page was fetched and confirmed to be silent on this point. The required answer to the user's question was not added, because the source does not give it.

## Cannot fix
- None fully. Gaps that remain: TR-199 Outlook.com (web) steps are not covered (see narrowing above). TR-201-r optional "Other tab / filter set to All" line not added (non-critical; the page supports it, but it was not needed). TR-205-e: the direct yes/no answer is not in the source.

## Follow-ups touched
- tr199-d (follow-up of tr199-b): its user answer changed to "it's on my computer, and I use the new Outlook app on Windows". tr199-b is unchanged, and its question is unchanged.

## Contradictions with the reviewer
- tr201-r: the Archive page supports the sentence the reviewer marked as unsupported (see above).
