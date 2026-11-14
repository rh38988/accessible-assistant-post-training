# fx8 generation report

Spec file data/v2/specs/fx8.py was already complete from an earlier run (8 tasks, e and r each, source_notes present). Verified by builder: 16 examples, OK. No topics replaced by backups. All tasks use the same source URL as ex8.py.

Sources:
- TR-104: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop
- TR-105: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop
- TR-106: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop
- TR-107: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer
- TR-108: https://support.apple.com/en-us/118226 and https://support.apple.com/en-us/105001
- TR-109: https://support.google.com/accessibility/android/answer/6006961?hl=en
- TR-110: https://support.apple.com/en-us/116940
- TR-111: https://support.apple.com/en-ca/108805

Not fully sure the page supports:
- tr108-e: the page gives no words for turning the lock on (implied same button); Home button swipe-up comes from the Control Center page.
- tr106-r: "check you are looking in the right place" is mild; the page does not cover Spam or All Mail.
- tr109-r: the source has no alternate path, so the reply says it cannot confirm another place and points to the Disability Support team.
- tr107 is marked sensitive but is not a scam task; r is a failure_recovery (marked Not spam by mistake).

Existing examples with content not supported by the source:
- tr105-a, tr105-c, tr105-d: "Only unsubscribe from senders you recognize / report as spam" is not on the page.
- tr107-a, tr107-d: "Unsubscribe is usually better" is not on the page.
- tr108-a, tr108-c, tr108-d: the lock icon description is not on the page.
- tr109-a, tr109-d: "Menu names can be different on some phones" is not on the page.
- tr111-a, tr111-d: "power strip", "bent pins", and "may need service from Apple" wording are not on the page; the order of restart and force restart differs slightly.
- tr110-a, tr110-c, tr110-d: "keep holding" is fine; "about 10 seconds" for iPhone 6s matches.
