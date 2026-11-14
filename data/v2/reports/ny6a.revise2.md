# Revise report: batch ny6a, revise 2

Revision list: data/v2/reviews/input/ny6a.revise2.md (built with review_io.py todo ny6a 2; 5 examples).
Edited file: data/v2/specs/ny6a.py. Builder: OK (7 tasks, 42 examples).

## Fixed

- tr188-a: deleted the Ctrl+Plus sentence. The reviewer's "(Windows)" heading is not on the page (see below), so no platform was claimed.
- tr188-r: "On Windows, hold down the Ctrl key and press the 0 key." Settings and more, then Zoom out kept as written. No Mac shortcut added.
- tr192-a: step 3 now "Under **Passwords**, select the password." (page wording). Every other step unchanged.
- tr192-d: same step 3 change.
- tr192-e: last sentence replaced. It now says Windows Hello is used when Chrome fills in a saved password, that the same check can also cover revealing, copying, or editing a password, and that the setting is optional and off by default. It no longer says Chrome requires verification. Steps 1 to 5 unchanged.
- tr188-e (not on the list, edited as instructed): deleted "(the three dots menu)"; the line now reads "1. Select **Settings and more**." The page names the menu but gives no three-dots description.

## Cannot fix

None.

## Follow-ups touched

None. tr188-e has no follow-up pair in the batch.

## Source notes changed

- TR-192 source_notes: "select the site" corrected to "select the password" (view steps), and the verification sentence now says biometric checks are off by default, optional, and used to reveal, copy, or edit. The old text said Chrome asks to verify identity before a password can be revealed.

## Where the page contradicted the reviewer

- tr188-a and tr188-r (reviewer's citation): the reviewer cited a section headed "Making a web page bigger in Edge (Windows)". Two WebFetch passes found no such heading on the Edge accessibility page. The zoom content sits under "Make text larger", and the Ctrl+Plus, Ctrl+Minus and Ctrl+0 table follows "Or use the following keyboard shortcuts". The page has Windows and Mac tabs at the top, but the extracted text does not show which tab holds the table, and the page does not say the shortcuts are Windows-only or give no Ctrl shortcut for other computers. Result: tr188-a drops the sentence (the reviewer allowed deletion); tr188-r keeps Ctrl+0 with the "On Windows," prefix, as instructed by the batch request. If the Windows scope is wrong, revisit tr188-r.
- Page wording for the Passwords step matches the reviewer's fix exactly ("Under "Passwords," select the password.").
- The page does not require identity verification before reveal, copy, or edit. It says biometric authentication is off by default and optional.

## Other warnings seen (not on this list, left unchanged)

- tr189-e: builder warning "no numbered steps in the reply". Not in the revision list.
