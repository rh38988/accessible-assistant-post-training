# fx7 revise2 report

Revision list: data/v2/reviews/input/fx7.revise2.md (built with review_io.py todo fx7 2; the reviewer notes were in data/v2/reviews/fx7.r2.md and fx7.r2.jsonl, not fx7.r2.py as the prompt said).
Snapshot before revision: data/v2/snapshots/fx7.before_revise2.jsonl.
No earlier revise2 work existed; the four examples still had the reviewed text.

## Fixed (4)
- tr091-e: step 6 now reads "Search for the pharmacy along your route and add it as a stop. You can add up to 9 stops, including the final destination." The "Add stop" label is gone. Page checked: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid
- tr099-e: opening sentence now "You can have your iPhone charged fully sooner from the Lock Screen." "just for today" and "without changing any settings" removed. Pages checked: https://support.apple.com/en-ca/108805 and https://support.apple.com/en-ca/108055
- tr099-r: "For just one day," removed; the sentence now says Charge Now gets the iPhone "fully charged sooner". Same pages.
- tr103-r: the Siri / My Card paragraph removed; step 2 is now "Tap **Location Services**, then turn it on." Page checked: https://support.apple.com/en-us/102484

## Cannot fix (0)

## Follow-ups touched
None. tr099 has no missing-info example, and tr091 and tr103 have no follow-up.

## Where the page differed from the reviewer or left gaps
- tr091-e: the reviewer asked for "tap it to add it as a stop". The page does not say to tap a place to add it. It only says "You can search for places along your route" and names Edit stops. The reply uses the search tip and "add it as a stop" without naming a tap.
- tr099-e and tr099-r: the reviewer cited 108805 for Charge Now, but that page does not mention it. The wording is supported by 108055 ("If you need to have your iPhone fully charged sooner, touch and hold the notification and then tap Charge Now"). Neither page says Charge Now lasts one day or leaves settings unchanged, so both claims are gone.
- tr099-e: the final line "Your iPhone will keep charging past 80%." is kept as the reviewer asked. It is an inference from "fully charged sooner", not stated word for word on the pages.
- tr103-r: confirmed that the page does not say the address must be on My Card. The page only says adding home and work addresses lets Siri help set location reminders.

## Build
python3 data/v2/tools/build_v2.py fx7 -> OK. One warning kept on purpose: tr103-r reply is 23 words (failure recovery should be 1 to 4 steps, so it is short by design).
