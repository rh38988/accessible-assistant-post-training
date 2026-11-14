# Revision list: batch ny4a, after review round 2 (1 examples)

Edit ONLY these examples in data/v2/specs/ny4a.py, then rebuild.

## tr166-e
- reasons: Reply omits the page's requirement that the phone must be turned on and have a network connection for the watch to locate it; the page says 'The phone must be turned on' and 'It also needs a stable network connection'. This is a non-critical precondition, so S1 is 1. The page also lists a Samsung account and Lost device protection remote controls as prerequisites; they do not change the steps, so they are not required here.
- fix requested: In the closing paragraph, add one sentence directly after 'The watch must be connected to the phone by Bluetooth, Wi-Fi, or LTE.': 'The phone must be turned on and have a network connection.' Change nothing else, including the steps and the website fallback.
- required actions missing from the reply: The phone must be turned on and have a network connection
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://www.samsung.com/us/support/answer/ANS00080182
