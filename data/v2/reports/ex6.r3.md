# Batch ex6, round 3 (final re-review of 19 revised examples)

Input: data/v2/reviews/input/ex6.r3.md (built with review_io.py render ex6 3 from ex6.r3.todo.json).
Review file: data/v2/reviews/ex6.r3.py (checker OK, saved as ex6.r3.jsonl).

## Decisions

- keep: 8 (tr078-a, tr078-d, tr082-a, tr082-d, tr084-a, tr084-d, tr085-a, tr085-d)
- reject: 11 (tr077-d, tr081-a, tr081-d, tr083-a, tr083-c, tr083-d, tr086-a, tr086-d, tr087-a, tr087-c, tr087-d)
- revise: 0 (round 3 is final)

## Most common problems

1. Unsupported quoted or specific claims in the source gate (7 examples):
   - Microsoft Downloads page does not say where downloaded files are saved, so "should be in the list" is unsupported (tr083-a, tr083-c, tr083-d).
   - FTC phishing page has no "Dear Customer" example and limits warning signs to payment details (tr086-a, tr086-d).
   - FTC spam-text page gives no reply rule and no "never send by text" rule (tr087-a, tr087-c, tr087-d).
2. Specific time limit not on the source page: "It takes less than a minute" (tr081-a, tr081-d). Borderline: the rubric allows "about a minute" but this is a stated limit. Flag for the Data Lead.
3. Unsupported remedy and safety advice on the Pixel QR page (tr077-d).

## Checks that passed

- Medical ID steps (Health, Summary, profile picture, Medical ID, Show When Locked, Edit/Add, Emergency Contacts, Done) match the Apple page.
- Chrome zoom steps (More, Zoom in/out, Ctrl/Command with + and -, Appearance, Page zoom) match the Chrome page.
- Pointer size and color steps match the Microsoft accessibility page sentence "changing the color and size of the mouse pointer".
- 2-Step Verification steps, the "Yes" prompt, and the no-call rule match the Google pages.
- The Pixel "bubble or link" wording is on the Pixel page (Camera app step 4), so it is supported.

## Unreadable pages

None. All 11 source URLs were fetched; two claims were re-checked with a second fetch before judging.
