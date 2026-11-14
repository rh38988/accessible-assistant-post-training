# ex4 round 3 review report (final re-review)

Batch: ex4, round 3. Input: data/v2/reviews/input/ex4.r3.md (14 examples, from ex4.r3.todo.json). Records: data/v2/reviews/ex4.r3.py.

## Decision counts
- keep: 14
- revise: 0
- reject: 0
- checker: OK

## Pages reviewed (one fetch per page, plus one follow-up on the Chrome down-arrow wording)
- support.apple.com/en-us/118236 (group text): tr051-a, tr051-c, tr051-d. All steps, labels and MMS conditions supported.
- support.google.com/chrome/answer/96810 (default zoom): tr052-a, tr052-d. The "down arrow" wording is on the page after a follow-up fetch.
- support.google.com/maps/answer/15437054 (location sharing): tr055-a, tr055-c. Gmail path, Copy to clipboard path, and 24-hour link limit supported.
- support.google.com/googleplay/answer/13627402, support.google.com/android/answer/7431795, support.google.com/googleplay/answer/13627571 (uninstall app): tr059-a, tr059-c, tr059-d.
- support.microsoft.com uninstall page (Windows 11): tr060-a, tr060-d. Settings path, Control Panel fallback and All apps method supported.
- support.apple.com/en-us/108429 (iPhone storage): tr061-a, tr061-d. Offload and Delete labels and descriptions supported.

No page was unreadable.

## Source conflict (tr059-a, tr059-c, tr059-d): Android 13 vs 14
- googleplay/answer/13627402 says "Some of these steps work only on Android 13 and up." This page gives the Play Store uninstall steps the reply uses.
- android/answer/7431795 says "Some of these steps only work on Android 14 and up." This page gives no uninstall steps, so its "these steps" refers to other content.
- Judgment: the reply's version wording is supported by the page that covers its steps, so these were kept. The Data Lead may want to confirm the Android version for the Play Store steps. If the version sentence is removed, the examples remain fully supported.

## Most common minor issues (none blocking)
- Vague durations: "It takes about a minute" and "This takes a few minutes" are expectation-setting, not specific claims. Not counted as failures.
- tr059-c and tr059-a/d: preinstalled apps are said to be "turned off" on some phones, but the cited page says to contact the device manufacturer for instructions. The reply does not give that pointer. Treated as non-critical, since the task is uninstalling through the Play Store.
- tr059-d first assistant turn says "Yes, you can remove them" before the device is known. The page says some preinstalled system apps cannot be deleted. The final reply corrects this, so the final reply was scored, not the earlier turn.
- tr051-d and tr052-d: the user is asked one question (iPhone or Android; which browser). Both are correct missing-information asks.

## Duplicates
- tr051-a, tr051-c and tr051-d share steps by design, with different user messages and different reply lead-ins. No duplicate gate failures.
