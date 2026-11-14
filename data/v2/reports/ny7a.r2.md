# ny7a round 2 report (re-review of 12 revised examples)

Decisions: 2 keep (tr202-a, tr202-r), 10 revise, 0 reject. Checker: OK.

Sources read (WebFetch, one or two per page): Microsoft new Outlook attach page (readable) and the Microsoft Outlook screen-reader attach page; Outlook.com can't-send-or-receive page, storage-limits page, automatic-forwarding page; Outlook.com recover-deleted-email page; Gmail create-label page; Google Contacts add-contact page. No page was unreadable.

Most common problems:
1. Insert tab label (tr199-a, c, d, e, r; 5 examples). The readable Microsoft page places Attach File in the Insert group on the Message tab and names no separate Insert tab. The screen-reader page does say "Insert" tab, so the two Microsoft pages disagree. Fix used: name the Insert group on the Message tab, which is the readable page's wording. The Data Lead may want to decide the label across all tr199 examples.
2. Claims the page does not make (tr199-c, tr199-r, tr201-r, tr205-e): "one picture at a time" stated as product fact (the page says nothing on multi-select); "Archived messages do not show in your inbox"; "the steps save a phone-only contact" (the page says it does not say).
3. Safety or constraint issues: tr200-c suggests permanently deleting all items in a folder with no warning (safety fail); tr200-e moves the message in step 3 although the user asked only to look (constraints 1); tr200-d tells the user to clear forwarding without checking whether it was deliberate (actionable 1).
4. Missing non-critical coverage: tr201-r omits the Junk Email, Other tab, filter and rule checks the page lists when a message is not in the recover list (steps 1).

Notes for the Data Lead:
- The new Outlook tr199 steps still have the revised structure; only the tab label conflicts.
- The tr199 accessibility page supports the OneDrive link path and the Manage access warning; the link-versus-copy choice on the readable page is not shown in the reply (not scored down).
- tr200-d's forwarding fix is a judgment call; the page does not say forwarding causes missing mail.
