# Revision list: batch ex8, after review round 2 (1 examples)

Edit ONLY these examples in data/v2/specs/ex8.py, then rebuild.

## tr111-d
- reasons: The user said the phone 'doesn't charge at all' (not stopping partway), yet the reply still ends with the 80% note, which answers the 'stop partway' case the user ruled out. Extra text the task does not need.
- fix requested: In the final assistant reply, delete the last paragraph '**If it stops at 80%:** that's usually a battery-saving feature, not a problem.' Leave everything else unchanged (keep tr111-a as is, since that user did not say which problem).
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-ca/108805
