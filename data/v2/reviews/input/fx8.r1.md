# Review input: batch fx8, round 1 (16 examples)

## tr104-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I have a lot of bookmarks in Chrome on my computer and I really don't want a bar taking up room across my screen. Last week I saved a recipe site and I just want to find it again by typing a word. Is that possible?

**ASSISTANT:**
Yes, you can search your bookmarks from the address bar. It takes a few seconds.

1. Open **Chrome** on your computer.
2. Click the address bar at the top.
3. Type **@bookmarks**, then press **Tab** or **Space**.
4. Type a word from the site's name, like "recipe".
5. Click the bookmark in the list that appears.

You can also click **Search bookmarks** in the suggestions instead of typing @bookmarks.

If you would rather look through all of them, click **More** at the top right, then **Bookmarks and lists**, then **Bookmark Manager**, and click the bookmark there.

## tr104-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I keep losing pages I like. How do I save a website in Chrome on my computer?

**ASSISTANT:**
Here's how to save a page. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar.

To find it later, look under the address bar. If the **bookmarks bar** is turned on, click the bookmark there.

**USER:**
I saved one but I don't see any bar under the address bar.

**ASSISTANT:**
The bar may just be turned off. Let's turn it on.

1. Click **More** at the top right of Chrome.
2. Click **Bookmarks and lists**.
3. Click **Show bookmarks bar**.

Your bookmark should now show in the bar. Click it to open the site.

You can also click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

## tr105-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I only use Gmail on my laptop and I don't want to visit any other websites or sign up for anything new. Can I stop a store's emails just from inside Gmail?

**ASSISTANT:**
You can try it right inside Gmail. It takes a few seconds.

1. Go to **mail.google.com**.
2. Open an email from that store.
3. Click **Unsubscribe** next to the sender's name.
4. In the box that pops up, click **Unsubscribe**.

Some senders require you to unsubscribe on their own website. For those, you will see **Go to website** instead, and Gmail can't finish it for you inside the email.

After you unsubscribe, emails may keep arriving for a few days.

## tr105-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

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
4. Check it for the store's other lists.

## tr106-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I was writing a long email in Gmail on my computer. It was a draft, I never sent it, and I think I deleted it by mistake. I'd really like it back in my inbox, please.

**ASSISTANT:**
I'm sorry, but a deleted draft can't be recovered from Trash, so I can't offer a way to bring it back.

If you also deleted other emails (not drafts) in the last 30 days, you can get those back.

1. Go to **mail.google.com**.
2. On the left, click **More**, then click **Trash**.
3. Check the box next to the email.
4. At the top, click **Move to**.
5. Choose **Inbox**.

## tr106-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I deleted an email in Gmail on my computer last week by accident. How do I get it back?

**ASSISTANT:**
Deleted emails stay in **Trash** for up to 30 days, so it may still be there.

1. Go to **mail.google.com**.
2. On the left, click **More**, then click **Trash**.
3. Check the box next to the email.
4. At the top, click **Move to**.
5. Choose **Inbox**.

**USER:**
I opened Trash but the email isn't there.

**ASSISTANT:**
I'm sorry. Check that you are looking in the right place: on the left, click **More**, then **Trash**.

If it still isn't there, it may have been removed for good. Emails are permanently deleted after 30 days, and **Delete forever** or **Empty Trash now** can't be undone. Deleted drafts also can't be recovered from Trash. Once an email is permanently deleted, it can't be recovered.

## tr107-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

**USER:**
I have about ten junk emails sitting in my Gmail inbox on my computer and I really don't want to click on each one and report it separately. Can I report them all together?

**ASSISTANT:**
Yes, you can select several emails and report them at the same time.

1. Open **Gmail** in your web browser.
2. Check the box next to each junk email.
3. At the top, click the **Report spam** icon.

Reporting sends Google a copy of the emails, which it may analyze.

## tr107-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

**USER:**
Gmail on my computer: what do I click to report an email as spam?

**ASSISTANT:**
Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. At the top, click the **Report spam** icon.

Reporting sends Google a copy of the email, which it may analyze.

**USER:**
Oh no, I just did that to an email from my daughter by mistake.

**ASSISTANT:**
That's easy to undo.

1. In **Gmail**, on the left, click **More**, then click **Spam**.
2. Check the box next to the email from your daughter.
3. At the top, click **Not spam**.

## tr108-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226

**USER:**
I have an older iPhone 8 with the round Home button. I read in bed and want the page to stay upright, but later I'll want it to turn sideways again for photos. Can I do both?

**ASSISTANT:**
Yes, you can lock it now and turn the lock off later. This takes a few seconds.

1. Swipe up from the bottom edge of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

When you want the screen to turn sideways again:

1. Open **Control Center** again.
2. Tap the **Portrait Orientation Lock** button to make sure it's off.
3. Close Control Center.
4. Turn the iPhone sideways.

Some apps don't support turning sideways, so the screen may stay upright in those even with the lock off.

## tr108-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226

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

## tr109-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

**USER:**
I use TalkBack on my Android phone because my eyesight is poor. When I turn the phone in my hand the screen turns too and it interrupts the voice. How do I stop the screen rotating?

**ASSISTANT:**
Turning off auto-rotate is the right fix. If you use TalkBack, auto-rotate must be off, because turning the screen can interrupt the spoken voice.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Select **Auto-rotate screen** to turn it off.

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

For more accessibility help, you can contact the Disability Support team.

## tr110-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

**USER:**
I have arthritis in my hands and I can't press two buttons at once. My iPhone has Face ID, it's frozen and the screen won't respond at all. Is there a way to restart it?

**ASSISTANT:**
Yes. For an iPhone with Face ID, you press one button at a time. No step needs two buttons together.

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This might take longer than 10 seconds, so keep holding.

If it still doesn't turn on, charge it for one hour and try again. If it still won't turn on after that, it might need service.

## tr110-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

**USER:**
My iPhone 7 froze and won't respond to anything. How do I restart it?

**ASSISTANT:**
For an iPhone 7, you force restart it with two buttons.

1. Press and hold the **side button** and the **volume down** button at the same time.
2. Keep holding both until you see the **Apple logo**. This might take longer than 10 seconds.

**USER:**
I held both for a long time and the screen is still black.

**ASSISTANT:**
Let's try charging it first.

1. Charge the iPhone for one hour.
2. Then try again: hold the **side button** and **volume down** together until you see the **Apple logo**.

If it still won't turn on, it might need service.

## tr111-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
My iPhone 12 only shows a little picture of a battery and won't charge. I have just the one cable and charger, so I can't borrow another one. What can I do with only what I have?

**ASSISTANT:**
You can try these with your own cable and charger. This takes about an hour, mostly waiting.

1. Check the cable and the adapter for damage. If either is damaged, don't use it.
2. Plug into a wall outlet. Make sure the cable, the adapter, and the outlet connect firmly, or try a different outlet.
3. Look at the charging port on the bottom of the phone and remove any debris. Then plug the cable in firmly.
4. Let it charge for half an hour.
If it still won't turn on or still shows the battery picture, force restart it:
5. Press and quickly release the **volume up** button.
6. Press and quickly release the **volume down** button.
7. Press and **hold** the **side button** until you see the **Apple logo**.
8. Let it charge for another half hour.

If it still won't charge, it might need service.

## tr111-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
iPhone 11 isn't charging when I plug it in. What can I check?

**ASSISTANT:**
Let's go through some checks. This takes about an hour, mostly waiting.

1. Check the cable and the adapter for damage. Don't use damaged ones.
2. Plug into a wall outlet. Make sure everything connects firmly, or try a different outlet.
3. Remove any debris from the charging port on the bottom of the phone, then plug the cable in firmly.
4. Let it charge for half an hour.
If it still won't turn on or shows a battery picture, force restart it:
5. Press and quickly release **volume up**.
6. Press and quickly release **volume down**.
7. Press and **hold** the **side button** until you see the **Apple logo**.
8. Let it charge for another half hour.

**USER:**
Now it shows a message that the accessory is not supported or certified.

**ASSISTANT:**
Try these.

1. Plug the iPhone straight into the charger, with no adapters or other equipment in between.
2. Remove any debris from the charging port on the bottom of the phone.
3. Restart the iPhone.
4. Try a different USB cable or charger.

Also make sure your iPhone has the latest version of iOS. If it still won't charge, it might need service.
