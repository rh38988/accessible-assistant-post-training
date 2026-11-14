# ex5 revise2 report

Source pages were fetched for all five listed examples (2026-11-13). Builder: `python3 data/v2/tools/build_v2.py ex5` prints OK (13 tasks, 52 examples).

## Fixed (5)

- tr073-c: First sentence replaced with the reviewer's supported wording ("Magnification can help with that. It zooms in on the whole screen, and you turn it on and off with your shortcut."). The Android page gives "Zoom in & make everything bigger" for full-screen magnification and says to use the shortcut again to stop. It says nothing about how the app looks when magnification is off, so that claim is gone.
- tr074-a: "Select your iPhone to see it on a map." changed to "Select your iPhone to locate it." The Find My steps on the Apple page give no map or post-selection screen.
- tr074-c: Same change as tr074-a.
- tr075-a: Two changes.
  - Condition: the reviewer's suggested "It works best when your phone is on and connected" was not applied. The Google page lists power and connection only for securing or erasing, not locating, so the page contradicted that part of the requested fix. The sentence now reads "If its current location can't be found, you may still see its last known location, if available." That wording comes from the page.
  - PIN: "enter your lock screen PIN or password" changed to "enter your lock screen PIN", with "If the phone has no PIN, or runs Android 8 or lower, you may be asked for your Google password." added, as the reviewer asked.
- tr075-d: Same changes as tr075-a, in the final assistant message.

## Additional fix beyond the reviewer's list (tr075-a, tr075-d)

- "You'll see where it is on a map." removed from step 3. The Find Hub page describes selecting the device from the list and says the lost device receives a notification. It does not describe a map. The reviewer did not flag this sentence.

## Cannot fix

- None.

## Follow-ups touched

- None. tr073-d, tr074-d and tr075-d's earlier turns were not changed. tr075-d was edited only in its final assistant message, the same as tr075-a.

## Not changed, possibly unsupported (not on the revision list)

These are not in the reviewer's list, and I did not change them. A later reviewer may want to check them.
- tr074-a and tr074-c: "Follow the steps on the screen to add a phone number and a message." The Apple page summary says only "Follow the onscreen steps if you want to display your contact information." Also "Apple will never contact you to say your iPhone has been found." was not seen on the page summary.
- tr074-c: "There's a good chance you can find it." This is reassurance, not a stated fact, but it is not on the page.
- tr075-a and tr075-d: "Mark as lost: tap Mark as lost, then Next ... then tap Mark as lost again to confirm." The Google page summary says only that you can add contact info and a lock-screen message, then tap Mark as lost. "then Next" and the second confirming tap were not seen.
- tr075-a and tr075-d: "Only do this if you can't get it back" for Factory reset. The page's reset warning is not that advice.
- tr064-a: builder warning that its opening is nearly the same as tr063-a (0.93). Not on this list, so left alone.
