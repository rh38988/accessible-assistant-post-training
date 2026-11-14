# Review report: batch fx6, round 2 (8 re-reviewed examples)

Decisions: 2 keep, 6 revise, 0 reject. Checker: OK (data/v2/reviews/fx6.r2.jsonl written).

Sources read (WebFetch, one or two fetches per page): Apple 102680; Google support 9319337; Microsoft "find my downloads"; FTC phishing; FTC "what to do if you were scammed" (cited by tr086-r only, not used for a claim in its final reply beyond the card steps); FTC spam texts (two fetches); FTC romance scams. No unreadable pages.

Keep: tr087-e, tr087-r.

Revise (fix in reviews/fx6.r2.py):
- tr076-e: "appears over the code" is a position detail the page does not give (source fail). Remove it.
- tr079-r: "or someone else turned the app off" is not on the page (source fail). Remove.
- tr083-e: partial-name search ("part of the name ... such as W2") is not on the page; the page only says search from File Explorer Home finds relevant files on the PC and in the cloud (source fail).
- tr086-e: "You don't have to do anything about it today" and "wait until Monday" are not on the page and delay the report-and-delete step; the page supports contacting the company through a known website now (source fail, actionable 1).
- tr086-r: "Because you clicked a link" is not a trigger the page gives; the security-software steps are tied to a scammer having access to the computer or phone (source fail, actionable 1, bundled step).
- tr088-e: "Stop communicating with him right away" is not on the page (source fail); "reverse image search" is unexplained jargon (plain 1).

Most common problems:
1. Unsupported trigger or condition added to a page step (3 examples: tr076-e, tr086-r, tr083-e).
2. Advice not on the page that delays or replaces a page step (tr086-e Monday wait).
3. Unexplained jargon for low-confidence users (tr088-e).

Note: the round-1 "newer models" claim in tr076-e is gone from the revised text (it now says "supported iPhone models"), which matches the page.
