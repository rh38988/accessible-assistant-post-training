# ny4a revise2 report

Batch: ny4a, revision round 2 (revision list: data/v2/reviews/input/ny4a.revise2.md, built with review_io.py todo ny4a 2).

## Fixed (1)
- tr166-e (TR-166, Samsung Galaxy watch ring): added the sentence "The phone must be turned on and have a network connection." directly after "The watch must be connected to the phone by Bluetooth, Wi-Fi, or LTE." Nothing else changed (steps and website fallback kept).
  - Source checked: https://www.samsung.com/us/support/answer/ANS00080182. The page says "The phone or tablet must be turned on." and "The device must be connected to a stable network connection." The added sentence is supported.

## Could not fix (0)

## Follow-up examples touched (0)

## Page vs. reviewer
- No contradiction. The reviewer quoted the page as "It also needs a stable network connection"; the page's wording is "The device must be connected to a stable network connection." The added sentence is a close paraphrase of that, so the fix stands.
- The reviewer noted the Samsung account and Lost device protection prerequisites. Not added, as the reviewer advised (they do not change the watch steps).

## Build
- python3 data/v2/tools/build_v2.py ny4a: OK (7 tasks, 42 examples).
- Non-listed warning left alone: tr161-c reply contains a web address; make sure it appears in the source. This example is not on the revision list, so it was not edited.
