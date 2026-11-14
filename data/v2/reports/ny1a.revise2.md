# ny1a revise2 report

Revision list: data/v2/reviews/input/ny1a.revise2.md (3 examples, built with review_io.py todo ny1a 2).
Builder: `build_v2.py ny1a` prints OK (warnings: tr124-r and tr125-e contain a web address; both addresses appear in the sources).

## Fixed
- tr125-a: Step 3 now gives the Finder path (Applications in the sidebar, drag to Trash); step 4 now gives Finder > Empty Trash. Steps 1, 2 and the closing line kept. Added `sources` with 102610 as second source (checked: Finder > Empty Trash; Applications in sidebar; drag to Trash).
- tr125-e: Step 2 replaced with the page's steps, one per step: APFS or Mac OS Extended (Journaled) drive, not Time Machine, SD or USB flash drive; quit Photos; open Pictures; drag Photos Library to the drive; double-click it on the drive; optional move of the old library to Trash and Empty Trash (library stays on the drive, so no photos are thrown away); Storage check last. Warning added: keep the drive on and connected before opening Photos, or Photos creates a new empty library in Pictures. Apple link kept as a "More help" line. Sources list already had 102624 and 108345 (both checked).

## Not fixed
- tr121-e: The reviewer asked for "swipe your Apple Pencil UP from either bottom corner". Two fetches of https://support.apple.com/102500 found no direction word: the sentence reads "swipe your Apple Pencil from the bottom corner of either side of your iPad screen". The word "up" does not appear, so the reply was left as it was (it already matches the page wording). Contradicts the reviewer on this point.

## Follow-ups touched
- None. tr125-a and tr125-e have no follow-up example that shares their opening question, so no pair changes were needed.

## Notes for the main session
- tr125-d (followup, same opening as tr125-b, Mac) has the same vague steps 3 and 4 that tr125-a had ("Delete apps you no longer use", "Empty the Trash"). It was not on the revision list, so it was not changed.
- The task-level source_notes for TR-125 do not yet include the Finder app-deletion steps from 102610 or the Photos library steps from 108345. Not changed (task-level, not an example).
