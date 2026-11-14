# ny5a round 3 report (re-review of 4 examples revised in round 2)

Decisions: 2 keep, 2 reject, 0 revise. Checker: OK.

| id | decision | main problem |
|---|---|---|
| tr177-a | keep | none |
| tr177-e | keep | none |
| tr175-r | reject | S1 = 1: the "keyboard turned on, charged or has fresh batteries, and in range" check (Bluetooth fix page step 3) is missing |
| tr178-r | reject | Source gate fail: "Captions only show sound that goes to your default sound output." The page says captions "pays attention to the default sound output device" and turns "any audio that passes through your PC" into captions. |

Why reject instead of revise: DATA_RUBRIC section 3 allows at most two revise-and-re-review rounds. Round 1 led to revise 1, round 2 to revise 2, so round 3 is the last re-review. Failing examples are rejected. The fix text for each is kept in the review file in case the Data Lead wants one more revision.

Notes:
- Round 3 input did not exist. Built with `review_io.py todo ny5a 2` (wrote `reviews/ny5a.r3.todo.json`, `reviews/input/ny5a.revise2.md`, and a snapshot in `snapshots/`), then `review_io.py render ny5a 3` (wrote `reviews/input/ny5a.r3.md`).
- The first Bluetooth fix-page fetch was ambiguous about whether "product specifications" applied to the PC or the device. A targeted re-fetch confirmed it refers to the PC (step title "Verify Bluetooth compatibility for your Windows 11 device"), so the tr175-r claim about the computer is treated as supported.
- The Magnifier keyboard-shortcuts page lists Ctrl+Alt+L (Lens view) and Ctrl+Alt+F (Full screen view), so tr177-e is supported. The zoom-level page does not mention views; tr177-e cites both pages.
- Pages fetched: Microsoft pair-Bluetooth, Microsoft fix-Bluetooth (twice), Magnifier zoom-level, Magnifier keyboard-shortcuts, live captions, and fix-sound-or-audio (once each unless noted).
- Files written: `reviews/ny5a.r3.py`, `reviews/ny5a.r3.jsonl` (by checker), `reviews/input/ny5a.r3.md`, `reviews/ny5a.r3.todo.json`, `reports/ny5a.r3.md`.
