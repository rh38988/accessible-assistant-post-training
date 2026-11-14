# ex7 revise2 report

Revision list: data/v2/reviews/input/ex7.revise2.md (10 examples, built with review_io.py todo ex7 2).
Spec edited: data/v2/specs/ex7.py. Builder: OK (warnings only for tr099, not on this list).
Snapshot before revision: data/v2/snapshots/ex7.before_revise2.jsonl.

## Fixed (10)

- tr090-a, tr090-c, tr090-d (FTC passwords page, checked 2026-11-13): tip 2 now keeps the breach condition ("If a company tells you it lost your password in a data breach, change it right away. If you used the same or a similar password on other sites, change it there too."). Added the page's note that text or email codes are the least secure two-factor type and an authenticator app or security key is better.
- tr090-c: removed "Your grandson has a good point" and "Since you use the same password everywhere, you should change it on every site." The page does not support either. Replaced with a passphrase sentence the page supports.
- tr091-a, tr091-d (Google Maps Android directions, checked): steps 2 and 3 now read "Search for your destination, or tap it on the map." The "search bar" and "tap the correct result" steps are removed, since the page mentions neither. Other steps are unchanged and renumbered.
- tr102-a, tr102-d (Select to Speak help, checked): the TalkBack clause is removed (see below).
- tr103-a, tr103-c, tr103-d (Apple Reminders, checked): step 5 is split into "To set your own day and time, tap Custom." / "Choose tomorrow's date." / "Set the time to 10:00 AM." No Done or Add step was added, since the page has none for this flow. The 9:00 AM default note is kept.

## Could not fix

None.

## Where the page contradicted or limited the reviewer

- tr102 (TalkBack): the page never defines TalkBack. It only says the shortcut uses "2-finger swipe up (3-finger swipe if TalkBack is on)". The reviewer's suggested explanation ("reads aloud everything you touch") is therefore not supported. I dropped the clause rather than explain it. Gap: a user whose phone has TalkBack on is now told only the two-finger gesture. This is the page's own rule, so a future fix should add it back with a plain warning rather than a definition.
- tr090: the reviewer's suggested opening ("Short passwords built from familiar things are easier for a hacking program to guess") is not on the page. The page says to avoid common phrases, song lyrics, or movie quotes, and recommends random-word passphrases. I used only the passphrase advice.

## Not flagged by the reviewer, not changed (check in a later round)

- tr090-a/c/d closing line ("a hacker who takes it over can get password reset links for your other accounts") and tip 5 ("a hacker who steals your password still can't log in without another step") do not appear on the FTC page I fetched.
- tr103-a/c/d "Your iPhone will show a reminder at that time." is not stated on the Apple page.

## Follow-ups touched

None. The tr090-b, tr091-b, tr102-b, and tr103-b missing-information questions are unchanged. The tr090-d, tr091-d, tr102-d, and tr103-d follow-ups were edited only as listed examples.
