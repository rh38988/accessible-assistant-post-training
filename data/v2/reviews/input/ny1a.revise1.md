# Revision list: batch ny1a, after review round 1 (14 examples)

Edit ONLY these examples in data/v2/specs/ny1a.py, then rebuild.

## tr121-d
- reasons: Final reply gives the Photos path without the scroll-up step: 'under Collections, then Media Types, then Screenshots'. The page says to scroll up before Media Types, so Media Types may not be visible.
- fix requested: In the last sentence use the page path: open Photos, tap Collections, swipe up, tap Media Types, then tap Screenshots (same wording as tr121-a).
- required actions missing from the reply: Find it later: Photos > Collections > scroll up > Media Types > Screenshots
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/102500

## tr121-e
- reasons: Unsupported claim about automatic saving.
- fix requested: Delete the sentence 'The screenshot is saved for you.' Replace with a neutral lead-in such as 'Here is where to look for it afterward.' Keep the Photos > Collections > Media Types > Screenshots path. Step 1 'Hold your Apple Pencil' can be merged into step 2.
- unsupported claims: 'The screenshot is saved for you.' -> the page does not say a Pencil screenshot is saved automatically (and does not mention Markup or Done).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/102500

## tr122-d
- reasons: Page step 1 is to back up the Mac before installing; the final reply omits it (tr122-a and tr122-c include it).
- fix requested: Add a short line before step 1 or after the list: 'Before you install anything, it is a good idea to back up your Mac.'
- required actions missing from the reply: Back up the Mac before installing
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108382

## tr123-a
- reasons: Page says to make sure Wi-Fi is turned on before joining; reply only says to have the password ready.
- fix requested: Change the lead-in to: 'Make sure Wi-Fi is turned on and have the Wi-Fi password ready.' (The page does not say how to turn Wi-Fi on, so add nothing more.)
- required actions missing from the reply: Make sure Wi-Fi is turned on
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/guide/mac-help/mchlp1180

## tr123-c
- reasons: Page lists 'make sure Wi-Fi is turned on' as a prerequisite; reply omits it.
- fix requested: Add a first line: 'Make sure Wi-Fi is turned on, and have the network name, security type, and password from the sticky note ready.'
- required actions missing from the reply: Make sure Wi-Fi is turned on
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/guide/mac-help/mchlp1180

## tr123-d
- reasons: Wi-Fi-on prerequisite missing; this user says the laptop 'is not on the internet', so it matters.
- fix requested: Change lead-in to: 'Make sure Wi-Fi is turned on and have the Wi-Fi password ready.'
- required actions missing from the reply: Make sure Wi-Fi is turned on
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/guide/mac-help/mchlp1180

## tr123-e
- reasons: Unsupported terms-and-conditions claim; Wi-Fi-on prerequisite missing.
- fix requested: Delete 'If it shows terms and conditions, accept them.' Step 3 should read: 'If it asks for a password, type it and click Join.' Add 'Make sure Wi-Fi is turned on.' as a short first line.
- unsupported claims: 'If it shows terms and conditions, accept them.' -> terms and conditions are not mentioned on the cited page.
- required actions missing from the reply: Make sure Wi-Fi is turned on
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/guide/mac-help/mchlp1180

## tr124-r
- reasons: Step 3 uses 'Safe Mode' with no explanation or how-to; the page links a separate Apple guide for it.
- fix requested: Step 3: 'If it still will not delete, restart your Mac and try again.' Then add one line: 'If that does not work, Apple has a guide called start up in Safe Mode: https://support.apple.com/en-us/116946.' Add that URL as a second source.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102610

## tr125-a
- reasons: Step 4 'Delete old iPhone or iPad backups, if your Mac stores any' gives no starting point; the page gives no steps for it either.
- fix requested: Remove step 4 (backups) since the cited page gives no way to do it, or add it only with a second Apple source that has the steps. Renumber the Trash step.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102624

## tr125-e
- reasons: Step 2 'Move the photos and videos you want to keep onto the drive' is not a doable step for a user whose photos live in Photos; the reply only says to 'check that guide' without naming it. The page links the guide.
- fix requested: Replace step 2 with: 'Move your Photos library to the external drive by following Apple's guide Move your Photos library to save space on your Mac: https://support.apple.com/en-us/108345.' Remove 'check that guide before you move yours'. Add that URL as a second source; keep step 1 and the Storage check.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102624

## tr126-d
- reasons: Last line 'If your Mac says System Preferences instead of System Settings, choose that.' leaves an older-macOS user stuck: on those Macs the steps differ (sidebar Battery/Power Adapter, and the option is called Low Power).
- fix requested: Replace the last line with: 'If your Apple menu says System Preferences instead of System Settings, tell me and I will give you the steps for that.'
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/101613

## tr127-a
- reasons: Reply says 'Your Mac may ask whether to erase the drive' but never says what to do; page: 'Either erase it or select a different backup disk or volume.'
- fix requested: Replace that sentence with: 'If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.'
- required actions missing from the reply: If asked to erase, either erase or select a different backup disk or volume
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/104984

## tr127-d
- reasons: Conditional erase prompt step from the page is omitted, so a user who sees it has no guidance.
- fix requested: Add after step 5: 'If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.'
- required actions missing from the reply: If asked to erase, either erase or select a different backup disk or volume
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/104984

## tr127-e
- reasons: Erase prompt guidance omitted; this user has the drive 'plugged in already' and may have used it before.
- fix requested: Add after step 4: 'If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.'
- required actions missing from the reply: If asked to erase, either erase or select a different backup disk or volume
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/104984
