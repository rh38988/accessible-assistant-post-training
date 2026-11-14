# fx7 round 2 review report

Examples reviewed: 6 (re-review of revised examples: tr091-e, tr093-r, tr099-e, tr099-r, tr103-e, tr103-r).
Source pages: 5 (Google Maps 144339; Zoom KB0065180 and KB0060732; Apple 108805 and 108055; Apple 102484). All were readable.

Decisions: 2 keep (tr093-r, tr103-e), 4 revise (tr091-e, tr099-e, tr099-r, tr103-r), 0 reject.
Checker: OK (data/v2/reviews/fx7.r2.jsonl written).

Most common problems:
1. Unsupported time or duration claim (2): "just for today" (tr099-e) and "For just one day" (tr099-r). The Apple page describes Charge Now as getting the iPhone fully charged sooner and does not say it lasts one day.
2. Action named without the how (1): tr091-e step 6 says to add the pharmacy as a stop without saying how to find and select it.
3. Requirement not on the page (1): tr103-r says an address "must be on My Card". The page only says adding addresses lets Siri help. The paragraph is also not needed for this user, so it was flagged as extra text.
4. Missing tap (1): tr103-r step 2 says "Turn on Location Services" without "tap Location Services".

Notes:
- tr099-e and tr099-r needed a second fetch of Apple 108055 for the Lock Screen notification and Charge Now. The first answer on 108805 did not cover them, and the second answer confirmed them.
- tr093-r's passcode statement in the earlier turn needed a second fetch of KB0065180. It is supported ("can oftentimes include an embedded passcode, allowing participants to join more quickly").
- tr103-e's Date and Time, Custom, and default-to-next-hour claims needed a second fetch of 102484. All are supported.
