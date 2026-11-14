# ny5a revise2 report

Input: data/v2/reviews/input/ny5a.revise2.md was not on disk. The four items came from the review notes in the batch request (tr175-r, tr177-a, tr177-e, tr178-r), which match the round 2 review in data/v2/reports/ny5a.r2.md. Those notes were used as the revision list.

Pages read (each checked before editing):
- Fix Bluetooth problems in Windows (tr175-r)
- Magnifier zoom level page (tr177-a)
- Keyboard shortcuts for Magnifier (tr177-e)
- Fix sound or audio problems in Windows (tr178-r, second source)
- Use live captions to better understand audio (tr178-r)

Fixed (4):
- TR-175 r: The USB Bluetooth adapter sentence is removed. The reply now says to check the product specifications to make sure your computer has Bluetooth capabilities, which is the page's wording. The Troubleshooting note in source_notes was changed to match. Both sources were already attached. The discovery step (Advanced) is unchanged and matches the page.
- TR-177 a: "Each press makes things on the screen larger." is removed. Step 2 now reads "again to zoom in more," which matches the page's "To increase the Magnifier zoom level, press the Windows key+Plus sign(+)."
- TR-177 e: "To go back to the whole screen" is replaced with "To switch back to **Full screen view**", using the page's Full screen view label. The shortcut Ctrl + Alt + F is unchanged. The second source was already attached.
- TR-178 r: Step 3 now reads: under Output, check the chosen device, and if it is not the headset, select the headset, which makes it the default output device. The page says selecting a device under Output makes it the default. A second source was added (Fix sound or audio problems in Windows, with its original URL kept first). Steps 1, 2 and 4 are unchanged.

Cannot fix: none.

Follow-ups touched: none.

Contradictions with the reviewer:
- TR-177 e: the reviewer asked for the label "switch back to Full screen view". The page has no "switch back" wording. Its label is "Full screen view" (Ctrl+Alt+F). The phrase "switch back to" is used only as a verb around that exact label.
- TR-175 r: the page never mentions USB Bluetooth adapters, so the reviewer's removal request was followed and the page's wording used instead.

Builder: python3 data/v2/tools/build_v2.py ny5a printed OK (7 tasks, 42 examples).
