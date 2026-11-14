# Revision list: batch ny6b, after review round 2 (2 examples)

Edit ONLY these examples in data/v2/specs/ny6b.py, then rebuild.

## tr194-c
- reasons: Source gate fails: the reply promises Spanish captions, but the page only says 'a language other than English' and does not list Spanish for Live Caption. Constraint score is 1 because the user's stated goal (Spanish captions) is not confirmed by the source. Steps 1 to 4 and 'the Down arrow' wording are supported (the page says 'Down arrow icon'), so no change is needed there.
- fix requested: In the opening line, replace 'Yes, Chrome can do that.' with 'Chrome can show captions in a language other than English.' Replace step 5 'Choose Spanish. Chrome downloads the language pack by itself.' with 'Choose the language you want from the list. Chrome downloads the language pack by itself.' Replace step 7 'Choose Spanish.' with 'Choose the same language.' Keep step 6 'Next to Preferred caption language, select the down arrow.' Add one sentence after the steps: 'This page does not say whether Spanish is in the list, so if it is not there, Live Caption may not support Spanish.' Do not cite Live Translate for Spanish captions.
- unsupported claims: 'Choose Spanish.' (step 5) and 'Choose Spanish.' (step 7) -> the page does not say Spanish can be chosen for Live Caption captions; it names Spanish only in the Live Translate section (Chromebook Plus devices). The request for Spanish captions is therefore not supported by the cited page.
- low scores: {'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/10538231

## tr197-r
- reasons: The 48 to 72 hour wait and the automatic backup explanation are supported by the page. But the final turn ends on an explanation with no next action: it does not tell the user what to do if the storage is still full after the wait, and it names no place to check or turn off automatic backup. The page gives no steps for that, so the reply cannot give them from this source.
- fix requested: Replace the last paragraph of the final assistant turn with: 'If it is still full after 48 to 72 hours, some photos and videos may be set to back up automatically. Automatic backup can be turned off, and then files waiting to be backed up will stop using the free space.' Keep the sentence 'The total can take 48 to 72 hours to update after a large deletion, so please wait that long first.' Do not name Google Photos backup settings or give steps to find them unless a source page gives them. To give a location, add the Google Photos backup help article linked from https://support.google.com/googleone/answer/9776477 as a second source and cite its steps.
- required actions missing from the reply: If still full, check which files are set to back up automatically and turn off automatic backup (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/googleone/answer/9776477
