# Review report: batch ny2a, round 2

Examples reviewed: 13 (the revised examples listed in reviews/ny2a.r2.todo.json). Checker: OK.

Decisions: 4 keep, 9 revise, 0 reject.

Pages read (WebFetch, one or two fetches each; no page unreadable):
- support.apple.com/en-us/102578 (Mail cannot send or receive): tr134-a keep, tr134-d revise, tr134-e revise
- support.apple.com/en-us/118433 (text and photo messages): tr135-c revise, tr135-e revise
- support.apple.com/en-us/120000 (No Service or SOS): tr136-a revise, tr136-d revise, tr136-e revise, tr136-r keep
- support.apple.com/en-us/118575 (Software Update, used as a second source for the update path): no separate decisions
- support.apple.com/en-us/118431 (temperature warning): tr138-e revise
- support.apple.com/en-us/101619 (wrong date or time): tr139-a keep, tr139-d keep, tr139-r revise

Most common problems:
1. Carrier settings update (Settings > General > About, then the carrier settings option) is on the No Service page but missing from the replies (tr136-a, tr136-d). The page does not cover it in 118575.
2. Required non-critical steps dropped: the provider's two-step verification or special password (tr134-d), the restart step (tr135-c), and the "contact provider if still failing" step (tr134-d, tr134-e).
3. Unsupported added claims: the photo settings "help with" carrier size limits (tr135-c), Airplane Mode "may pause your download" (tr136-e), and "enter the passcode if you know it" for a gray Date & Time switch (tr139-r).
4. Constraint handling: tr138-e says it "may be safer to turn it off" when the user said not to turn it off.
5. Incomplete path or reference: "Send as Text Message" has no tap path (tr135-e); the Time Zone step omits "enter a city" (tr139-r); tr134-e calls deletion "the last step on the list" when the list has no such step.

Notes:
- tr135-e: "contact Apple Support for blue bubble problems" was checked with one extra fetch of 118433 and is supported.
- tr136-r: "get service from Apple" is a paraphrase of the page's "get service through its support site"; accepted.
- tr134-a: "on a computer" in the last-resort step is not on the page; not treated as a failure.
