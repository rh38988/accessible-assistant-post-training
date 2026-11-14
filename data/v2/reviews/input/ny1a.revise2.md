# Revision list: batch ny1a, after review round 2 (3 examples)

Edit ONLY these examples in data/v2/specs/ny1a.py, then rebuild.

## tr121-e
- reasons: The page says to swipe the Pencil UP from a bottom corner. The reply says only 'Swipe your Apple Pencil from a bottom corner', so the direction, which is the whole gesture, is missing.
- fix requested: In step 1 write: 'Swipe your Apple Pencil up from either bottom corner of the screen.' Keep the rest.
- required actions missing from the reply: Swipe the Apple Pencil up from either bottom corner of the screen (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/102500

## tr125-a
- reasons: Steps 3 and 4 name an action but not how to do it ('Delete apps you no longer use', 'Empty the Trash'). A low-confidence user has no starting point for either. The reply gives no menu path, and the page supports one.
- fix requested: Step 3: 'Open a Finder window, click Applications in the sidebar, then drag an app you no longer use to the Trash. Apple's steps: https://support.apple.com/en-us/102610' (that page is a second source, so add it to sources). Step 4: 'Click Finder in the menu bar at the top, then choose Empty Trash.' Keep steps 1, 2 and the closing line.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102624

## tr125-e
- reasons: The reply hands the whole job to a link ('following Apple's guide ... https://support.apple.com/en-us/108345'). None of the page's actions are written out. The user's goal is freeing space, and space is freed only after the old library is removed from the Mac, which is not mentioned. The warning that Photos makes a new empty library if the drive is not connected is also missing.
- fix requested: Replace step 2 with the page's steps in plain words, one per step: (a) the drive should be formatted APFS or Mac OS Extended (Journaled); do not use a Time Machine drive, SD card or USB flash drive; (b) close Photos; (c) in Finder, open your Pictures folder; (d) drag Photos Library onto the external drive; (e) when it finishes, double-click the library on the drive to open it; (f) only after you have checked your photos opened from the drive, move the old Photos Library in Pictures to the Trash and choose Finder > Empty Trash to free the space (say this removes the copy on the Mac, not the copy on the drive). Add: keep the drive plugged in and on before you open Photos, or Photos starts a new empty library. Keep the Storage check as the last step. Keep the link as a 'more help' line.
- required actions missing from the reply: Check the drive is APFS or Mac OS Extended (Journaled); not a Time Machine drive, SD card, USB flash drive or network location | Close Photos | In Finder open the Pictures folder in the home folder where Photos Library is stored | Drag Photos Library onto the external drive (critical) | Double-click the library in its new location to open it | Optionally move the old library from Pictures to the Trash and empty the Trash to free space (critical for the goal) | Keep the drive connected and on before opening Photos
- low scores: {'steps': 0, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102624 ; https://support.apple.com/en-us/108345
