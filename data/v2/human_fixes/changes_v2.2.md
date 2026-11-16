# v2.2 changes: Shirley's 15 spot-check fixes (before / after)

Generated from `changes_v2.2.jsonl`. Before = v2.1 text. Each fix was checked against the official pages in its source list (read 2026-11-16), then re-checked by a separate agent (12 OK; tr192-e corrected; tr103-e and tr218-e kept as noted below).
Where the page did not support a suggestion, the page was followed; see 'Page differs'.

Judgment calls after the independent check:
- tr103-e: the checker wanted the iOS 26.2 / iCloud Reminders condition back. Shirley asked to remove it, so it stays out; the reply says to tell us if Urgent is missing.
- tr218-e: 'don't reply' is not on the FTC page. Kept as general protective advice the page does not contradict.

## tr012-e  (Attach a photo to an email, Gmail (computer))

**Shirley's note:** Dragging meets the user's request and is supported by the source. However, the fallback recommends the bottom button the user explicitly finds difficult to click.

**Suggestion:** Specify the body of the message being composed and ask the user to check that the image appears after releasing it. Remove the inaccessible-button fallback; instead ask where dragging becomes difficult.

**What changed:** Drop target is now the message area; added a check that the picture appears; removed the Attach-button fallback and ask which part of dragging is hard.

hash 8a9ac425b8cf -> 0a256d990e23

**Before (last assistant turn):**

> Yes, you can add the picture by dragging it.
> 
> 1. Click the picture in the folder window and hold the mouse button down.
> 2. Drag it into your email window.
> 3. Let go of the mouse button.
> 
> If dragging is hard, the other way is the **Attach** button at the bottom of the email window.

**After:**

*user:*
> I'm writing an email in Gmail on my computer and my picture is already showing in a folder on the screen next to it. The little buttons at the bottom are hard for me to hit with my shaky hand. Can I just pull the picture over into the email instead of using the button?

*assistant:*
> Yes, you can drag the picture into your email instead.
> 
> 1. Click the picture in the folder window and hold the mouse button down.
> 2. Move it over the email you're writing, into the big area where you type your message.
> 3. Let go of the mouse button.
> 4. Check that the picture now shows in your email before you send it.
> 
> If dragging is hard too, tell me which part is hardest, holding the button down or moving the mouse, and we can find another way.

Sources: https://support.google.com/mail/answer/6584

---

## tr014-r  (Caller claims to be grandchild needing gift cards, any)

**Shirley's note:** I agree we should calm the user down first. But since the user already mail out money and contact grandson. The response focuses on prevention and reporting but omits a time-sensitive attempt to intercept the cash shipment, which we should focus on.

**Suggestion:** Ask which carrier was used and whether delivery is complete, while advising immediate contact with the carrier about interception. For USPS, contact the Postal Inspection Service. Do not promise recovery; then provide ReportFraud.ftc.gov.

**What changed:** Leads with intercepting the package (USPIS 1-877-876-2455; FedEx/UPS), asks which carrier and whether it was delivered, makes no recovery promise, reports at ReportFraud.ftc.gov. Added the FTC 'What To Do if You Were Scammed' page as the main source.

hash 70af050a4577 -> 2ceed22b806a

**Before (last assistant turn):**

> I'm sorry this happened. It is not your fault, and you did the right thing by calling your grandson.
> 
> 1. **Don't send any more money**, even if the caller contacts you again.
> 2. Tell another trusted family member what happened so you have support.
> 3. Report it to the FTC at **www.ftc.gov/complaint**.
> 
> I don't have steps for getting the cash back. Reporting helps. Agree with your family that no one will ever call with an emergency request for wired money, gift cards, or cash.

**After:**

*user:*
> Oh no. I think I got scammed. A woman said my grandson was in jail and I mailed $1,500 cash to an address she gave me. Now I called my grandson's real number and he is fine. What do I do now?

*assistant:*
> I'm sorry this happened. It is not your fault, and you did the right thing by calling your grandson. Act quickly, because a package that hasn't been delivered yet may still be stopped.
> 
> 1. If you mailed it through the U.S. Postal Service, call the **U.S. Postal Inspection Service** right away at **1-877-876-2455** and ask them to intercept the package. There is a fee, and it only works if the package hasn't been delivered yet.
> 2. If you sent it with another company, like FedEx or UPS, call that company as soon as you can.
> 3. Report the scam to the FTC at **ReportFraud.ftc.gov**.
> 4. Don't send any more money, even if the caller contacts you again.
> 
> I can't promise you'll get the money back. Which company did you send it with, and has it been delivered yet?

Sources: https://consumer.ftc.gov/articles/what-do-if-you-were-scammed; https://www.ftc.gov/node/54353

---

## tr028-r  (Take a screenshot, Windows 11)

**Shirley's note:** Not Select **Snipping Mode** is called snipping area.  And the evidence does not establish that Screenshots always appears in File Explorer's left sidebar

**Suggestion:** Include button locations and recognizable icons to make the instructions easier to follow. Avoid assuming that a particular folder appears in the sidebar, since layouts can differ. For locating an existing screenshot, provide an alternative such as searching in File Explorer, with a clear search scope and search term.

**What changed:** No longer assumes Screenshots shows in the side pane: the path is Pictures > Screenshots (Print Screen page), with a fallback search from Home for the folder name (Find your files page).

**Page differs:** Shirley said the control is called 'snipping area'. Microsoft's Snipping Tool page says 'select Snipping Mode', so that label was kept. The page shows icons for buttons but does not describe their shapes, so no icon descriptions were added.

hash c29c2add9f25 -> 4a791fb810f0

**Before (last assistant turn):**

> Snips are saved automatically in your **Screenshots** folder.
> 
> 1. Open **File Explorer** from the taskbar.
> 2. On the left side, open the **Screenshots** folder.
> 3. If you want another copy somewhere else, select **Save as** in Snipping Tool, choose a location and a name, then select **Save**.
> 
> To change where snips are saved, select **See More** in Snipping Tool, then **Settings**.

**After:**

*user:*
> How can I take a picture of my whole screen on my Windows 11 computer?

*assistant:*
> You can use **Snipping Tool**.
> 
> 1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
> 2. Select **Snipping Mode**, then choose **Full screen**.
> 3. Select **New**.
> 
> It captures the whole screen right away.

*user:*
> OK it took the picture but I can't tell where it went. How do I find it?

*assistant:*
> Snipping Tool saves each snip automatically in your **Screenshots** folder. Here's how to find it.
> 
> 1. Select **File Explorer** on the taskbar.
> 2. In the pane on the left, select **Pictures**, then open **Screenshots**.
> 3. If you don't see **Pictures** there, select **Home** in File Explorer, type **Screenshots** in the search box, and press **Enter**. Then open the **Screenshots** folder from the results.
> 
> Next time, you can also select **Save as** in Snipping Tool right after a snip, choose a place and a name, then select **Save**.

Sources: https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots; https://support.microsoft.com/en-us/windows/experience/keyboard-shortcut-for-print-screen; https://support.microsoft.com/en-us/windows/find-your-files-in-windows-5c7c8cfe-c289-fae4-f5f8-6b3fdba418d2

---

## tr050-a  (Check battery health, iPhone)

**Shirley's note:** i think the instruction is clear. Maybe we can use plain words to explain some unfamiliar term as well like maxiaum capacity here

**Suggestion:** i think the instruction is clear. Maybe we can use plain words to explain some unfamiliar term as well like maxiaum capacity here

**What changed:** Maximum Capacity explained in plain words from the page. Also removed 'It takes a minute' (duration not on the page) and the unsupported 'may be covered under warranty' line.

hash 9ede05a82bd0 -> ce69d06070df

**Before (last assistant turn):**

> You can check it in Settings. It takes a minute.
> 
> 1. Open the **Settings** app.
> 2. Tap **Battery**.
> 3. Tap **Battery Health**. On some versions the name is slightly different.
> 4. Look at **Maximum Capacity**. This compares your battery now to when it was new. A lower number means it won't last as long between charges.
> 
> If you see a message that your battery's health is **significantly degraded**, it isn't a safety problem, but a new battery would help it last longer. Apple offers battery service, and it may be covered if your phone is still under warranty.

**After:**

*user:*
> My iPhone battery seems to die quickly. How do I check the battery health?

*assistant:*
> You can check it in Settings.
> 
> 1. Open the **Settings** app.
> 2. Tap **Battery**.
> 3. Tap **Battery Health**. On some versions the name is slightly different.
> 4. Look at **Maximum Capacity**. It tells you how much charge your battery can hold now, compared with when it was new. As a battery gets older, it holds less charge, so you get fewer hours of use between charges.
> 
> If you see the message **"Your battery's health is significantly degraded,"** it isn't a safety problem, and you can still use your iPhone. A new battery would bring back its full capacity. Apple offers battery service, and if your iPhone is out of warranty, there is a charge.

Sources: https://support.apple.com/en-us/101575

---

## tr054-r  (Share location with family, iPhone (Find My))

**Shirley's note:** The earlier answer adds a custom duration not listed in the source. After failure, it immediately recommends updating without establishing the screen or version.

**Suggestion:** First ask whether the user is on Find My's People tab and what options appear, then select applicable steps. Set up sharing while safely parked, before driving.

**What changed:** Set up while parked, before driving. The recovery reply now checks the Me and People tabs and asks what choices appear, instead of telling the user to update.

**Page differs:** Shirley said the custom duration is not in the source. Apple's page says 'Choose to share your location for an hour, until the end of the day, indefinitely, or a custom time period', so it was kept. '(a plus icon)' was removed because the page calls it the Add button.

hash b90730035450 -> 45fb4d83115e

**Before (last assistant turn):**

> When a sharing option is missing, update your iPhone.
> 
> 1. Update your iPhone to the latest software.
> 2. Open **Find My** and try the steps again.
> 
> Live Location needs both you and your daughter to have an iPhone with iOS 15 or later. Some options need iOS 17.

**After:**

*user:*
> My daughter has an iPhone too. How can I let her see where I am on my iPhone while I drive to her house?

*assistant:*
> You can do this in the **Find My** app. Set it up before you start driving, while you're parked.
> 
> 1. Open **Find My**.
> 2. Tap the **Me** tab and turn on **Share My Location**.
> 3. Tap the **People** tab, tap the **Add** button, then tap **Share My Location**.
> 4. Choose your daughter.
> 5. Pick how long to share: an hour, until the end of the day, indefinitely, or a custom time period.
> 
> Only share your location with people you trust.

*user:*
> When I tap the plus button I don't see Share My Location at all.

*assistant:*
> Let's check which screen you're on first. Please do this while you're parked.
> 
> 1. Tap the **Me** tab and check that **Share My Location** is turned on.
> 2. Tap the **People** tab.
> 3. Tap the **Add** button and look for **Share My Location** in the list that opens.
> 
> If it's still not there, what choices do you see after you tap **Add**? Tell me, and I'll help you pick the right one.

Sources: https://support.apple.com/en-us/105104

---

## tr058-r  (Delete an app, iPhone)

**Shirley's note:** Although the app is explicitly Facebook, the recovery answer starts with nonremovable Apple apps. "Check parental controls" lacks an actionable navigation path.

**Suggestion:** Remove the irrelevant built-in-app branch. Ask whether icons jiggle or a removal icon appears after holding the app. Provide version-appropriate restriction steps; refer managed-device restrictions to the administrator.

**What changed:** Removed the built-in Apple apps branch. Added the jiggle path, a Screen Time path for the restriction, kept the administrator step, and asks what happens when the app is held.

**Page differs:** Apple's pages give Settings > Screen Time > Content & Privacy Restrictions and say 'Make sure Deleting Apps is set to Allow', but no official page found gives the menu between them (community posts say iTunes & App Store Purchases). The reply says 'find Deleting Apps' rather than naming an unverified menu.

hash df1568dbd516 -> d9e3b97f3a7e

**Before (last assistant turn):**

> A few things can cause that.
> 
> 1. Some built-in Apple apps can't be deleted.
> 2. If it's not an Apple app, check your parental control settings and make sure deleting apps is set to **Allow**. Then try again.
> 3. If your iPhone is managed by a company or school, you may not be able to delete apps. Contact your device administrator.

**After:**

*user:*
> How can I take the Facebook app off my iPhone? I don't use it anymore.

*assistant:*
> You can delete it from the Home Screen.
> 
> 1. Touch and hold the app.
> 2. Tap **Remove App**.
> 3. Tap **Delete App**.
> 4. Tap **Delete** to confirm.
> 
> Deleting an app doesn't cancel subscriptions inside it, so cancel any you don't need first.

*user:*
> I held it but there is no Remove App choice, or it won't let me delete it.

*assistant:*
> Let's check what happens when you hold the app.
> 
> 1. Touch and hold the **Facebook** app. If the apps start to jiggle, tap the **Remove** icon in the upper-left corner of the Facebook app, then tap **Delete App**, then **Delete**.
> 2. If you don't get a way to remove it, deleting apps may be turned off. Open **Settings**, tap **Screen Time**, then **Content & Privacy Restrictions**, then find **Deleting Apps** and make sure it is set to **Allow**.
> 3. If your iPhone is managed by a company or school, ask its administrator.
> 
> When you hold the Facebook app, what happens: a menu opens, the apps jiggle, or nothing changes?

Sources: https://support.apple.com/en-us/101550; https://support.apple.com/guide/iphone/block-features-or-content-with-screen-time-iph3ff83f3b1/ios

---

## tr062-d  (Free up storage space, Android)

**Shirley's note:** The user identifies Samsung, but the answer applies generic Android cleanup navigation. Photo-deletion advice does not distinguish ordinary Google Photos deletion from removing device copies only.

**Suggestion:** Confirm the Samsung model, One UI version, or current Storage screen. Verify backup completion, then use a verified Free up space or Delete from device workflow instead of generic deletion instructions.

**What changed:** Samsung path (Battery and device care > Storage) from Samsung's page. Photo advice now checks backup and uses Delete from device, with a warning that regular Delete also removes the backed-up copy. Asks the user to describe their Storage screen if it differs.

**Page differs:** Shirley suggested confirming the model or One UI version. The reply asks about the Storage screen instead, since Samsung's page only notes that older software calls it Device care.

hash 0c7ff1995cba -> 10c63f903e78

**Before (last assistant turn):**

> Thanks. Here's how to see what's using space and clear some out. It takes a few minutes.
> 
> 1. Open the **Settings** app.
> 2. Tap **Storage**.
> 3. Tap **Free up space**.
> 4. Scroll to a category, then tap **Select files**. If you don't see the category, tap **Browse**.
> 5. Select the files you don't need.
> 6. Tap **Move files to Trash**.
> 
> **Other ways to save space:**
> - If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
> - Uninstall apps you don't use. You can reinstall them later without paying again.
> 
> Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.

**After:**

*user:*
> phone says storage full

*assistant:*
> I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?

*user:*
> Android, Samsung

*assistant:*
> Thanks. On a Samsung phone, here's how to see what's using space and clear some out.
> 
> 1. Open the **Settings** app.
> 2. Tap **Battery and device care**. On some older phones, this is called **Device care**.
> 3. Tap **Storage**.
> 4. Tap **Unused apps**, select the apps you don't use, and tap **Uninstall**. You can also tap **Large files** or **Duplicate files**, select what you don't need, and tap **Delete**.
> 
> **If your photos back up to Google Photos:** you can remove just the copies on your phone. In Google Photos, tap a photo, tap **More**, and scroll to **Details** to check that it's backed up. Then select the photos, tap **More**, and choose **Delete from device**. Don't use the regular **Delete** for this, because that removes the photos from Google Photos too, on every device where backup is on.
> 
> If your Storage screen looks different, tell me what you see on it.

Sources: https://www.samsung.com/uk/support/mobile-devices/how-to-clear-up-storage-space-on-your-smartphone; https://support.google.com/photos/answer/6128858?hl=en

---

## tr063-d  (Turn on the flashlight, iPhone)

**Shirley's note:** user ask my phone is dark and I need some light, where is it. This means they want to light up the device not open the flashlight.

**Suggestion:** ask follow up question when not sure

**What changed:** The first reply now asks what the user means (flashlight or brighter screen) instead of assuming flashlight; the user's answer gives both the goal and the device. Final reply unchanged (checked against the page).

hash f785cbfe62b3 -> a8774d07cac4

**Before (last assistant turn):**

> Got it.
> 
> There are a few quick ways.
> 
> **From Control Center:**
> 1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.
> 2. Tap the **Flashlight** button.
> 3. Tap it again to turn it off.
> 
> **From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.
> 
> **With Siri:** say "Hey Siri, turn on my flashlight."

**After:**

*user:*
> my phone is dark and I need some light, where is it

*assistant:*
> I can help. Do you want to use your phone as a **flashlight**, or make your **screen brighter**?

*user:*
> The flashlight. It's an iPhone.

*assistant:*
> Got it.
> 
> There are a few quick ways.
> 
> **From Control Center:**
> 1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.
> 2. Tap the **Flashlight** button.
> 3. Tap it again to turn it off.
> 
> **From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.
> 
> **With Siri:** say "Hey Siri, turn on my flashlight."

Sources: https://support.apple.com/en-us/105001

---

## tr103-e  (Set a reminder, iPhone)

**Shirley's note:** I think it provide some unnecessary info like"This needs **iOS 26.2** and iCloud Reminders turned on." and "Urgent alarms only sound on the iPhone that Find My uses as your location"  that might confused the user and didn't help to get the task done

**Suggestion:** I think it provide some unnecessary info like"This needs **iOS 26.2** and iCloud Reminders turned on." and "Urgent alarms only sound on the iPhone that Find My uses as your location"  that might confused the user and didn't help to get the task done

**What changed:** Removed the iOS 26.2 / iCloud requirement sentence and the Find My device sentence. Kept one short troubleshooting line.

**Page differs:** v2.1 had removed 'Custom' from step 3. Apple's page says 'Tap the Date and Time button ... or tap Custom to set your own day and time', so Custom is back for setting noon today.

hash 5816bb887db2 -> 83766e8f2901

**Before (last assistant turn):**

> Yes, you can mark a reminder as **Urgent**. Urgent alarms sound even when your iPhone is silenced. This needs **iOS 26.2** and iCloud Reminders turned on.
> 
> 1. Open the **Reminders** app.
> 2. Tap **+ New Reminder** and type **Take heart pill**.
> 3. Set the **Date and Time** to today at **12:00 PM**.
> 4. Tap the reminder, then tap **Info**.
> 5. Turn on **Urgent** under **Date & Time**.
> 6. If urgent alarms don't sound, open **Settings**, tap **Apps**, tap **Reminders**, and under **Allow Reminders to Access** turn on **Alarms**.
> 
> Urgent alarms only sound on the iPhone that Find My uses as your location.

**After:**

*user:*
> My iPhone is on silent almost all the time because I can't stand the noise. But I have a heart pill I must take at noon and I need the reminder to actually make a sound anyway. Can a reminder be loud even on silent? I want one for today at noon.

*assistant:*
> Yes. You can mark the reminder as **Urgent**, and its alarm sounds even when your iPhone is silenced.
> 
> 1. Open the **Reminders** app.
> 2. Tap **+ New Reminder** and type **Take heart pill**.
> 3. Tap the **Date and Time** button, tap **Custom**, and set it for today at **12:00 PM**.
> 4. Tap the reminder, then tap the **Info** button.
> 5. Under **Date & Time**, turn **Urgent** on.
> 
> If you don't see **Urgent**, tell me. If the alarm doesn't sound at noon, open **Settings**, tap **Apps**, tap **Reminders**, and turn on **Alarms** under **Allow Reminders to Access**.

Sources: https://support.apple.com/en-us/102484

---

## tr129-e  (Connect a Bluetooth device, Mac)

**Shirley's note:** did not mention wheres the control center and how to access it

**Suggestion:** provide navigation of how to access the control center. Do not assume user knows that.

**What changed:** Says where Control Center is and how to open it (menu bar, top right), from the Mac User Guide's Control Center page.

**Page differs:** The Control Center page does not describe what the icon looks like, so no icon description was added.

hash 51ae687420aa -> 9049b3557626

**Before (last assistant turn):**

> Yes, there is a quicker way.
> 
> 1. Make sure your headphones are on.
> 2. Click the **Bluetooth** status icon in Control Center.
> 3. Select your headphones from the list.
> 
> If you ever want the longer way, open the **Apple menu**, choose **System Settings**, click **Bluetooth**, point at the headphones, and click **Connect**.

**After:**

*user:*
> My Bluetooth headphones are already set up on my Mac, they just are not connected right now. I do not want to dig through System Settings every time. Is there a quicker way to connect them?

*assistant:*
> Yes. You can use **Control Center**, which is in the menu bar at the top right of your screen.
> 
> 1. Make sure your headphones are on.
> 2. In the menu bar at the top right of the screen, click the **Control Center** icon.
> 3. Click **Bluetooth**, then select your headphones from the list.
> 
> If you ever want the longer way, open the **Apple menu**, choose **System Settings**, click **Bluetooth**, point at the headphones, and click **Connect**.

Sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac; https://support.apple.com/guide/mac-help/mchl50f94f8f/mac

---

## tr133-e  (Report and block junk text messages, iPhone)

**Shirley's note:** Apple supports the limitation on using Report Junk after replying, but the answer generalizes it to all reporting being impossible.

**Suggestion:** Limit the statement to Messages' built-in Report Junk feature. Keep blocking instructions and, if needed, suggest asking the carrier about other reporting methods. Do not imply that blocking also stops messages from new numbers.

**What changed:** The limit is now scoped to Messages' built-in report option. Blocking is described as covering this sender's number only. Added the carrier as another reporting route.

**Page differs:** Shirley's note says 'Report Junk'. The current iPhone User Guide calls it 'Report Spam', so the page label was used.

hash b80c66234bb9 -> cf80b14a1c8e

**Before (last assistant turn):**

> No, you cannot report a message after you have replied to it. You can still block them, which stops their messages from reaching you.
> 
> 1. Open the **Messages** app.
> 2. Open the conversation with the sender and tap the person's icon at the top.
> 3. Tap **Info**.
> 4. Scroll down and tap **Block Contact**.
> 
> The sender does not know they have been blocked.

**After:**

*user:*
> A stranger texted my iPhone and I already wrote back to ask who they were. Now they keep texting. Can I still report them as spam?

*assistant:*
> You can't use the **Report Spam** option in Messages for a message after you've replied to it. You can still block the sender.
> 
> 1. Open the conversation in **Messages**.
> 2. Tap the person's icon at the top.
> 3. Tap **Info**, scroll down, then tap **Block Contact**.
> 
> This blocks this sender's number, and they won't know they've been blocked. If you'd like to report the texts another way, you can ask your phone carrier.

Sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

---

## tr192-e  (Save and find passwords with Google Password Manager, Chrome (computer))

**Shirley's note:** The Windows Hello option is supported, but if both people share the same Windows login and know its PIN, it cannot be presented as identifying only the wife.

**Suggestion:** Clarify whether they share a Windows account or PIN. Explain that verification relies on that Windows identity. Recommend separate Windows user accounts and private sign-in credentials, then explain the Hello option.

**What changed:** Explains that the check relies on the Windows sign-in, so it fails if they share an account or PIN. Recommends a separate account for the husband and a private PIN, then gives the Chrome steps. The account is added for him so her saved passwords stay in her own account.

hash a7cb4cb192aa -> 16b4bb6acfe8

**Before (last assistant turn):**

> Yes. On Windows, you can turn on a check:
> 
> 1. At the top right, click **More**.
> 2. Click **Passwords and autofill**, then **Google Password Manager**.
> 3. Select **Settings**.
> 4. Turn on **Use Windows Hello when filling passwords**.
> 5. Follow the on-screen instructions to confirm.
> 
> Once it is on, Windows Hello is used when Chrome fills in a saved password, and this check can also cover revealing, copying, or editing a password. The setting is optional and off by default, so it stays off until you turn it on.

**After:**

*user:*
> My husband and I share one Windows computer and Chrome has my passwords saved. I don't want him to be able to just click and see them. Can I make Chrome check that it is really me before it shows a saved password?

*assistant:*
> Yes. Chrome can use **Windows Hello** to check before it fills in a saved password, and the same check can be used to reveal, copy, or edit a password. Windows Hello uses the PIN, face, or fingerprint set up for signing in to Windows. So it only keeps your husband out if he can't use that same sign-in.
> 
> First, make sure the Windows sign-in is yours alone:
> 1. If you both use the same Windows account, give him his own. Open **Settings**, select **Accounts** > **Other users**, then under **Add other user** select **Add account** and follow the instructions.
> 2. If he knows your PIN, change it. Open **Settings**, select **Accounts** > **Sign-in options**, then select **PIN (Windows Hello)** > **Change PIN**. You'll need your old PIN to set a new one.
> 
> Then turn on the check in Chrome:
> 3. At the top right, click **More**.
> 4. Click **Passwords and autofill**, then **Google Password Manager**.
> 5. Select **Settings**.
> 6. Turn on **Use Windows Hello when filling passwords**, and follow the on-screen instructions.
> 
> The check is off until you turn it on.

Sources: https://support.google.com/chrome/answer/95606?hl=en; https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0; https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32; https://support.microsoft.com/en-us/windows/security/change-or-reset-your-pin-in-windows

---

## tr214-g  (A caller demands payment for a debt the user does not recognize, any)

**Shirley's note:** Oversimplifies call-frequency limits without the particular-debt scope or the seven-day restriction after a conversation. It also omits exceptions such as communicating with the consumer's attorney.

**Suggestion:** Frame the answer around covered U.S. debt collection, qualify the frequency rules and exceptions, and retain FTC, CFPB, and state attorney-general reporting routes. Do not present it as a worldwide rule.

**What changed:** Framed as U.S. federal law for household debts, with state laws noted. Frequency rule restated as the page gives it, including the seven days after a phone conversation about a particular debt. Added the attorney exception. Kept all three reporting routes.

**Page differs:** The FTC page attaches 'about a particular debt' only to the seven-days-after-a-call limit, not clearly to the seven-calls-in-seven-days limit, so the reply follows that wording.

hash 1a9371836307 -> 1873a4dba90c

**Before (last assistant turn):**

> Here is what a collector cannot do.
> 
> 1. Harass or threaten you, or use obscene or profane language.
> 2. Call more than seven times in seven days, or contact you before 8 a.m. or after 9 p.m. unless you agree.
> 3. Lie about the amount owed, pretend to be an attorney or a government representative, or threaten arrest or legal action they will not take.
> 4. Reveal your debt publicly, or generally discuss it with anyone other than you or your spouse.
> 
> To report one, go to the FTC at reportfraud.ftc.gov, the CFPB at cfpb.gov/complaint, or your state attorney general's office.

**After:**

*user:*
> What can a debt collector not do, and where do I report one who breaks the rules?

*assistant:*
> In the U.S., the federal Fair Debt Collection Practices Act sets these rules for household debts like credit cards, medical bills, and car loans. Business debts aren't covered, and your state may have its own rules too. Collectors can't:
> 
> 1. Harass you, threaten to hurt you, or use obscene or profane language.
> 2. Lie to you, for example about how much you owe, or pretend to be an attorney or from the government.
> 3. Contact you before 8 a.m. or after 9 p.m., unless you agree to it.
> 4. Call you more than seven times in seven days, or call within seven days after talking with you by phone about a particular debt.
> 5. Generally, discuss your debt with anyone except you or your spouse.
> 
> If a lawyer represents you, tell the collector. The collector then has to contact your lawyer, not you.
> 
> To report a collector who breaks the rules, contact the FTC at **ReportFraud.ftc.gov**, the Consumer Financial Protection Bureau at **cfpb.gov/complaint**, or your state attorney general's office.

Sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

---

## tr218-e  (An email claims to have embarrassing video or a password and demands payment, any)

**Shirley's note:** It overgeneralizes an older article about a particular mass-email scam.

**Suggestion:** Keep the no-payment advice and supportive tone, but say this is a common scam and a claim is not proof. Preserve necessary information for reporting before blocking. Treat concrete compromise or video evidence separately, and update any disclosed password that is still used or reused elsewhere.

**What changed:** Calls it a known scam and says a claim is not proof, instead of 'all talk'. Report before deleting. Password change now covers reused passwords. A real picture or video is handled as a separate case.

hash f3187f94894a -> fa3b11d99ad0

**Before (last assistant turn):**

> No, please do not pay. This is a scam, and there is nothing to be embarrassed about.
> 
> 1. Do not pay anything. Delete the message.
> 2. Their claims about access to your computer or webcam are all talk, even if the message includes a real old password.
> 3. If it shows a password, change the password on that account, and consider updating other passwords too.
> 4. Report the message to the FTC at ReportFraud.ftc.gov.
> 
> A threat to send something within hours is meant to rush you.

**After:**

*user:*
> The email says it will send the video to all of my friends and family within a few hours unless I pay. It says if I tell anyone or report it, it will be sent sooner. I'm so embarrassed I can't tell anyone. Should I just pay to make it go away?

*assistant:*
> No, please don't pay. This is a known scam, and there's nothing to be embarrassed about. These emails often claim the sender got into your computer or webcam, but an email saying they have a video is not proof that they do.
> 
> 1. Don't pay, and don't reply.
> 2. If the email shows a real password, change that password now. If you used the same password anywhere else, change it there too.
> 3. Report the email to the FTC at **ReportFraud.ftc.gov**. After you've reported it, delete it.
> 
> The deadline of a few hours is there to rush and scare you. If the email includes an actual picture or video of you, tell me, because that needs different steps.

Sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

---

## tr224-e  (A company promises to stop foreclosure for an upfront fee (FTC), any)

**Shirley's note:** Rejecting the suspicious upfront payment and contacting the lender and HUD assistance are appropriate. However, "Do not pay anything" could be understood as stopping normal mortgage payments too.

**Suggestion:** Specify not paying this company's upfront relief fee. Do not independently stop ordinary mortgage payments; discuss options directly with the servicer or a HUD-approved counselor. Retain the source-supported help routes.

**What changed:** 'Do not pay anything' narrowed to this company's fee. Says not to stop regular mortgage payments on one's own or send them to the company, and to discuss options with the lender or a counselor. Help routes kept; FTC reporting added.

hash 0bb800124f6f -> 650dc8656fd0

**Before (last assistant turn):**

> Do not send the cashier's check. Scammers often tell you not to contact your lender or housing counselor, and no company can tell you to stop talking to your lender. Do not pay anything until a company delivers the results you want.
> 
> 1. Contact your servicer or lender right away. You can do this even if the foreclosure process has already started.
> 2. Talk to a certified housing counselor for free. Find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
> 3. You can also call 1-888-995-HOPE (4673).

**After:**

*user:*
> They told me not to call my lender and not to tell my counselor, or it would ruin the deal. They want a cashier's check today for $1,500. I already got a foreclosure notice and I am scared. What do I do?

*assistant:*
> Do not send the cashier's check. Scammers often tell you not to contact your lender or housing counselor, and no company can tell you to stop talking to your lender. Don't pay this company any fee before it delivers the results you want.
> 
> Don't stop your regular mortgage payments on your own, and never send them to this company. You could lose your home and damage your credit if you stop paying your mortgage, so talk about your options with your lender or a housing counselor.
> 
> 1. Contact your servicer or lender right away. You can do this even if the foreclosure process has already started.
> 2. Talk to a certified housing counselor for free. Find one on HUD's list of approved agencies at **apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm**, or call **1-888-995-HOPE (4673)**.
> 3. Report this company to the FTC at **ReportFraud.ftc.gov**.

Sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

---
