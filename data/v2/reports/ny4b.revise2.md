# ny4b revise2 report

Revision list: data/v2/reviews/input/ny4b.revise2.md (built with review_io.py todo ny4b 2, which also wrote reviews/ny4b.r3.todo.json and snapshots/ny4b.before_revise2.jsonl).

## Fixed (3)
- tr169-c: added one sentence after step 5 warning that on an open network the user's info is available to other people on it. Source: https://support.google.com/chromebook/answer/1047420?hl=en (open or public network section). The page says "your info is available to other people"; the reviewer's quoted wording ("on that network", "can see") is not on the page, so the sentence follows the page.
- tr169-r: step 4 now tells the user to type the network name and the password they already know. The hidden-network section says only "Enter the network information in the box that appears" and lists no fields, so the wording relies on the user's own stated details rather than on a field list.
- tr170-r: (1) the phone/mobile-data step now covers trouble with that connection during the update, matching the page's condition; (2) "A reset does not delete your personal files" is now "You can reset your Chromebook without deleting your personal files." Source: https://support.google.com/chromebook/answer/177889?hl=en ("System update doesn't download" section).

## Cannot fix (0)

## Follow-ups touched
None.

## Build
python3 data/v2/tools/build_v2.py ny4b printed OK (6 tasks, 36 examples).
