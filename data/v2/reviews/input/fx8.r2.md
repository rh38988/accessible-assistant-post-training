# Review input: batch fx8, round 2 (5 examples)

## tr104-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I have a lot of bookmarks in Chrome on my computer and I really don't want a bar taking up room across my screen. Last week I saved a recipe site and I just want to find it again by typing a word. Is that possible?

**ASSISTANT:**
Yes, you can search your bookmarks from the address bar. It takes a few seconds.

1. Open **Chrome** on your computer.
2. Click the address bar.
3. Type **@bookmarks**, then press **Tab** or **Space**.
4. Type a word from the site's name, like "recipe".
5. Click the bookmark in the list that appears.

You can also click **Search bookmarks** in the suggestions instead of typing @bookmarks.

If you would rather look through all of them, click **More** at the top right, then **Bookmarks and lists**, then **Bookmark Manager**, and click the bookmark there.

## tr105-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/mail/answer/15621070?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
Gmail on my computer. How do I stop the emails from a clothing store?

**ASSISTANT:**
Gmail can do it in a few clicks.

1. Go to **mail.google.com**.
2. Open an email from the store.
3. Click **Unsubscribe** next to the sender's name.
4. In the box that pops up, click **Unsubscribe**.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site. Emails may keep arriving for a few days.

**USER:**
I did that last week and the store still sends me emails.

**ASSISTANT:**
That can happen. Unsubscribing from one email may only remove you from one of the sender's mailing lists, so the store may have other lists.

1. Go to **mail.google.com**.
2. On the left, click **More**.
3. Click **Manage subscriptions**.
4. Find the store in the list. On the right, next to the number of recent emails from the store, click **Unsubscribe**.

It can take a few days for the emails to stop.

## tr108-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/108330

**USER:**
I have an older iPhone 8 with the round Home button. I read in bed and want the page to stay upright, but later I'll want it to turn sideways again for photos. Can I do both?

**ASSISTANT:**
Yes, you can lock it now and turn the lock off later. This takes a few seconds.

1. Swipe up from the bottom edge of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Tap the top of the screen or press the Home button to close Control Center.

When you want the screen to turn sideways again:

1. Open **Control Center** again.
2. Tap the **Portrait Orientation Lock** button to make sure it's off.
3. Tap the top of the screen or press the Home button to close it.
4. Turn the iPhone sideways.

Some apps don't support turning sideways, so the screen may stay upright in those even with the lock off.

## tr108-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/108330

**USER:**
iPhone 13 here. The screen keeps flipping sideways while I read. Help?

**ASSISTANT:**
You can lock the screen so it stays upright.

1. **Swipe down from the top-right corner** of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

**USER:**
I swiped down from the top but I can't find any button.

**ASSISTANT:**
Control Center opens from the corner, not the middle of the top edge.

1. Put your finger on the **top-right corner** of the screen.
2. Swipe down from there to open **Control Center**.
3. Tap the **Portrait Orientation Lock** button.
4. Close Control Center.

## tr109-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

**USER:**
My Android screen won't stop turning when I tilt the phone. How do I turn that off?

**ASSISTANT:**
You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Select **Auto-rotate screen** to turn it off.

**USER:**
I opened Settings but there is no Display & touch on my phone.

**ASSISTANT:**
I'm sorry about that. The steps I have use **Display & touch**, and I can't confirm another place for this setting on your phone.

For more accessibility help, you can reach the Disability Support team here: https://support.google.com/accessibility/answer/7641084

Tell me what you see in Settings and I'll try to help.
