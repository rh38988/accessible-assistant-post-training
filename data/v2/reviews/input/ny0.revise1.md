# Revision list: batch ny0, after review round 1 (2 examples)

Edit ONLY these examples in data/v2/specs/ny0.py, then rebuild.

## tr117-c
- reasons: The sentence suggests nothing is saved to the desktop when a thumbnail appears, which contradicts the source and could make the user think the screenshot is lost.
- fix requested: Replace with: 'A small picture may appear in the corner of the screen. You can click it to edit the screenshot, or wait and the screenshot is saved on your desktop.'
- unsupported claims: 'The picture is saved on your desktop unless a small picture appears in the corner' -> page: the thumbnail may appear and you can click it to edit 'or wait for the file to save to the desktop'; the file is saved to the desktop either way
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102646

## tr119-e
- reasons: Two assurances are added from memory. The steps themselves match the page.
- fix requested: Change the opening to 'You can look for it in your Library and download it again.' Delete the sentence 'Make sure you are signed in with the same Microsoft account you used before.' Keep steps 1 to 5 and the Order history line.
- unsupported claims: 'with no new purchase' -> page does not say reinstalling is free of charge | 'Make sure you are signed in with the same Microsoft account you used before.' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc
