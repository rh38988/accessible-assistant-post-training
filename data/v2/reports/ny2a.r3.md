# Review report: batch ny2a, round 3 (final re-review)

Examples reviewed: 9 (the examples revised after round 2, from reviews/ny2a.r3.todo.json). Checker: OK.

Decisions: 5 keep, 0 revise, 4 reject. Round 3 is the last allowed re-review, so no revise was issued.

Keep: tr134-d, tr134-e, tr135-c, tr135-e, tr136-a

Reject:
- tr136-d: unsupported SOS condition on the iOS update step; step 5 bundles several actions.
- tr136-e: Airplane Mode step can interrupt the Wi-Fi download the user is waiting on; step 5 bundles several actions.
- tr138-e: keep-on workaround is not on the page (the page says to turn the device off first).
- tr139-r: manual-time fallback for a dimmed switch is not supported; "locked" and "ask the person" are not on the page; step 3 bundles many actions.

Pages read (WebFetch, two fetches for 118433 and 120000, one to two for the others; no page unreadable):
- support.apple.com/en-us/102578 (Mail): tr134-d and tr134-e supported.
- support.apple.com/en-us/118433 (text and photo messages): tr135-c and tr135-e supported after one extra fetch. The page does not use the heading "Lower-quality sending" that the round 2 note cited; the sentence "If you experience an issue when you try to send full size images, you can manually send lower quality images" supports the reply's wording.
- support.apple.com/en-us/120000 (No Service or SOS): the carrier settings path (Wi-Fi, Settings, General, About) is here, and tr136-a, tr136-d, tr136-e are judged against it.
- support.apple.com/en-us/118575 (Software Update): used as the second source for the update path. It does not cover carrier settings, which the round 2 note said it did not need to.
- support.apple.com/en-us/118431 (temperature warning): the page says to turn the device off, move it to a cooler environment, and allow it to cool down. It does not offer a keep-on option.
- support.apple.com/en-us/101619 (Date & Time): manual setting requires turning off Set Automatically. The page says the option may be dimmed for a Screen Time passcode or corporate profile, or not available with some carriers or countries.

Most common problems in this round:
1. Bundled steps that combine plugging in, joining Wi-Fi, a menu path, and a Download and Install tap (tr136-d, tr136-e) or a long multi-action Date & Time step (tr139-r).
2. Added conditions or workarounds that the page does not give (tr136-d SOS trigger, tr138-e keep-on option, tr139-r manual fallback for a dimmed switch).

Judgment calls to check:
- tr136-e: the S3 point rests on the fact that Airplane Mode also switches off Wi-Fi. That is device behavior and is not on the page.
- Backup before a software update (118575) and the removal-and-re-add step (102578) were not counted as required actions. The update is optional for the No Service fix, and removal can delete downloaded mail. The same rule was applied to tr134-d and tr134-e.
