# fx4 revise2 report

Revision list: data/v2/reviews/input/fx4.revise2.md (3 examples), built with review_io.py todo fx4 2. Snapshot: data/v2/snapshots/fx4.before_revise2.jsonl.

## Fixed (2)
- tr050-r (Check battery health, Unable to verify message). Source: https://support.apple.com/en-us/101575. Replaced the garbled steps with one action: follow the link "To have your battery checked, get service", which goes to getsupport.apple.com. Kept the opening note that the health information might not be accurate. The page gives this link wording, not "choose the battery service option", so the reply uses the page's wording.
- tr051-r (Start a group text, carrier step). Source: https://support.apple.com/en-us/118236. Added a plain explanation of group MMS and MMS Messaging. Carrier step now asks whether the plan supports Group MMS Messaging, as the page says. The reviewer's "your phone company has to turn it on" is not on the page (the page says to contact the carrier to see whether the plan supports it), so it was not used.

## Cannot fix (1)
- tr056-r (Install an app, App Store missing). Left unchanged. The page https://support.apple.com/en-us/102590 names the labels (Content & Privacy Restrictions, iTunes & App Store Purchases, Installing Apps, Allow) but gives no Settings path, and its restriction steps do not give a Settings path either. The guide page https://support.apple.com/guide/iphone/block-apps-app-downloads-websites-purchases-iph3ff83f3b1/ios: the first fetch was truncated before the section, and the second fetch (offset 100000) did not contain the Installing Apps setting. Its only path (Settings > Screen Time > Content & Privacy Restrictions > Other Features) does not show the Installing Apps setting. Per the reviewer's condition, the example should be rejected or rewritten once a confirmed path is available. It still contains the unsupported line "If you did not set this up, ask the person who manages your phone." and the step order (Spotlight first) that differs from the page (restrictions first, Spotlight as fallback).

## Follow-ups touched
- None. The two fixed examples are the r examples; their e examples were not changed.

## Page contradicted the reviewer
- tr050-r: the page gives the link text "To have your battery checked, get service"; the reviewer's "choose the battery service option" was not on the page.
- tr051-r: the page does not say the carrier "has to turn it on"; the reviewer's wording was not used.

Builder: `python3 data/v2/tools/build_v2.py fx4` printed OK (26 examples, 13 tasks).
