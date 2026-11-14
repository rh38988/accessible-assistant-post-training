# Review input: batch fx4, round 1 (26 examples)

## tr048-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Silence calls from unknown numbers (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111106

**USER:**
I have an iPhone and I'm waiting to hear from a new specialist's office, so I can't just send every unknown number to voicemail. But I am sick of the spam. Is there something in between?

**ASSISTANT:**
Yes. On iPhone you can have unknown callers asked why they're calling before your phone rings.

1. Open the **Settings** app.
2. Tap **Apps**, then tap **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Ask Reason for Calling**.

The caller is asked why they're calling before your phone rings, so you can tell a real call from spam.

Calls from numbers saved in your Contacts always come through, so save the specialist's number once you have it. Call screening may use your standard calling and data rates.

## tr048-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Silence calls from unknown numbers (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111106

**USER:**
Robocalls keep ringing my iPhone all day. How do I make it stop ringing for numbers I haven't saved?

**ASSISTANT:**
You can silence calls from numbers you haven't saved. They go to voicemail.

1. Open the **Settings** app.
2. Tap **Apps**, then tap **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from your Contacts will still ring.

**USER:**
I did that. Now my Recents list is a big mess and I can't tell which calls came from unknown numbers. Can I see just those?

**ASSISTANT:**
Yes. Turn on a filter, then open the list.

1. Open **Settings**, tap **Apps**, then tap **Phone**.
2. Scroll to **Call Filtering** and turn on **Unknown Callers**.
3. In the Phone app, tap the **Filter** button, then tap **Unknown Callers**.

Missed calls and voicemails from unknown numbers now move to that list. In the Phone app it appears in the **Recents** tab in Classic view, or the **Calls** tab in Unified view.

## tr049-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
Pixel phone with the Google Phone app here. I don't want anything blocked or hidden, because my pharmacy calls from lots of different numbers. I just want the phone to warn me when a call looks like spam. What should I do?

**ASSISTANT:**
You can have the Phone app warn you without blocking anything.

1. Open the **Phone** app.
2. Tap **More options** (three dots), then tap **Settings**.
3. Tap **Caller ID and spam**.
4. Make sure **See caller ID & spam** is on.
5. Leave **Filter spam calls** turned off.

Calls that look like spam may show **Suspected spam caller** or **Spam** as the caller ID, and your phone will still ring.

This setting is on by default, so it may already be on.

## tr049-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
My Pixel keeps ringing with robocalls. How do I make the Phone app block the spam ones?

**ASSISTANT:**
You can turn on spam filtering in the Phone app.

1. Open the **Phone** app.
2. Tap **More options** (three dots), then tap **Settings**.
3. Tap **Caller ID and spam**.
4. Make sure **See caller ID & spam** is on.
5. Turn on **Filter spam calls**.

Filtered calls won't notify you, but they still show in your call history.

**USER:**
I did that. But now a call from my dentist's office got marked as spam and I think it was blocked. Help!

**ASSISTANT:**
You can fix that in a few taps.

1. Open the **Phone** app and tap **Recent calls**.
2. Tap the call that is labeled as spam.
3. Tap **Not spam**.
4. Tap **Unblock**.

Calls that were filtered still appear in your call history, and you can still check your voicemail.

## tr050-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
I can't afford a new phone or a new battery right now, I'm on a fixed income. But my iPhone 8 doesn't hold a charge like it used to. Can you show me how to look at the battery and what I can do to make it last?

**ASSISTANT:**
Looking at the battery costs nothing. Battery Health is available on iPhone 6 and later, so your iPhone 8 has it.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**.
4. Look at **Maximum Capacity**. It compares your battery now to when it was new. A lower number can mean fewer hours between charges.

Ways to take care of the battery:
- Avoid charging your iPhone or leaving it in hot places, such as direct sun, for long periods.
- If you store it for a long time, keep it about half charged.

## tr050-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
My iPhone XR battery goes down fast. How can I see how healthy it is?

**ASSISTANT:**
You can check it in Settings.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**.
4. Look at **Maximum Capacity**. It compares your battery now to when it was new.

**USER:**
I did that, but there's no capacity number. It says Unable to verify this iPhone has a genuine Apple battery. What does that mean?

**ASSISTANT:**
That message means the iPhone could not confirm that it has a genuine Apple battery. The battery health information on that screen may not be accurate.

1. Don't rely on the numbers shown there.
2. Get the battery checked.

Your phone is not broken just because of this message.

## tr051-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

**USER:**
My hands shake and typing names on my iPhone is hard. I want to text my bridge club ladies all at once about Thursday. Can I pick them from my contacts instead of typing each name?

**ASSISTANT:**
Yes, you can pick people from your contacts.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil).
3. Tap the **Add** button (a plus icon) to add people from your Contacts.
4. Choose each of the ladies you want in the group.
5. Type your message.
6. Tap the **Send** button (the up arrow).

Everyone in the group will get the message.

If someone in the group doesn't use an iPhone, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.

## tr051-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

**USER:**
How do I send one message to my brother and two cousins at once on my iPhone? One cousin has an Android.

**ASSISTANT:**
You can send a group text.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil).
3. Enter their names, or tap the **Add** button (a plus icon) to pick them from Contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

Because one person uses Android, go to **Settings**, then **Messages**, and turn on **MMS Messaging**.

**USER:**
I went to Settings, then Messages, but there is no MMS Messaging switch. My cousin with the Android didn't get anything.

**ASSISTANT:**
When that option is missing, the next step is to check with your carrier.

1. Contact your phone carrier.
2. Ask whether your plan supports Group MMS Messaging.

Once your plan supports it, **MMS Messaging** can be turned on in **Settings**, then **Messages**.

## tr052-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I use Chrome on my laptop. The writing on websites is too tiny for me, but the pictures are fine and I don't want those blown up. Can I make just the text bigger on every site?

**ASSISTANT:**
Yes. You can change Chrome's font size.

1. Click the **More** menu (three dots) at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Next to **Font size**, click the down arrow and choose a bigger size.

If you want more choices, click **Customize fonts**.

Some websites don't let Chrome change only the text size. On those sites the text stays the same. If that happens, you can use **Page zoom** in the same **Appearance** section, but it makes pictures bigger too.

## tr052-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
chrome on my pc, how do i make all websites open bigger without zooming every time

**ASSISTANT:**
You can set a bigger default size.

1. Click the **More** menu (three dots) at the top right.
2. Click **Settings**.
3. Click **Appearance**.
4. Next to **Page zoom**, click the down arrow and choose a bigger size.

**USER:**
I did that and most sites are bigger, but my bank's website still looks small.

**ASSISTANT:**
A site can have its own saved size. You can remove it.

1. Click **More**, then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Additional content settings**, then **Zoom levels**.
4. Click the **X** next to your bank's site.

That removes the site's own resize settings.

## tr054-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone (Find My)
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

**USER:**
I have an iPhone. My son keeps asking where I am, but I don't want him watching me all day. I just want to send him where I am right now at the park, one time. Can I do that?

**ASSISTANT:**
Yes. You can send a one-time pin in Messages.

1. Open the **Messages** app and open the conversation with your son, or start a new message to him.
2. Tap the **Plus** button, then tap **Location**.
3. Tap the **Map Pin** button in the corner.
4. Tap **Send Pin**.
5. Send your message.

Your son sees only that spot. He can't follow you as you move.

## tr054-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone (Find My)
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

**USER:**
My daughter has an iPhone too. How can I let her see where I am on my iPhone while I drive to her house?

**ASSISTANT:**
You can do this in the **Find My** app.

1. Open **Find My**.
2. Tap the **Me** tab and turn on **Share My Location**.
3. Tap the **People** tab, tap the **Add** button (a plus icon), then tap **Share My Location**.
4. Choose your daughter.
5. Pick how long to share: an hour, until the end of the day, indefinitely, or a custom period.

Only share your location with people you trust.

**USER:**
When I tap the plus button I don't see Share My Location at all.

**ASSISTANT:**
When a sharing option is missing, update your iPhone.

1. Update your iPhone to the latest software.
2. Open **Find My** and try the steps again.

Live Location needs both you and your daughter to have an iPhone with iOS 15 or later. Some options need iOS 17.

## tr055-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I'm on Android and use Google Maps. My brother in law doesn't have Gmail, he only has some other email. We're driving to the lake and he wants to see where I am along the way. Can he still do that?

**ASSISTANT:**
Yes. You can share a link with him instead.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Tap **Copy to clipboard**.
6. Paste the link into an email, text, or messaging app and send it to him.

The link shares your real-time location for up to 24 hours.

Only share your location with people you trust.

## tr055-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
Android phone. My son uses Gmail. How do I let him see my location in Google Maps?

**ASSISTANT:**
You can do it in **Google Maps**.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**, then tap **New share**.
4. Choose how long to share.
5. Tap your son's profile.
6. Tap **Share**.

His Gmail address needs to be saved in your Google Contacts.

**USER:**
I tapped New share but my son isn't in the list.

**ASSISTANT:**
The usual reason is that his contact isn't ready for sharing.

1. Add your son's Gmail address to your Google Contacts. He must have a Gmail account.
2. If Google Maps asks for access to your contacts, allow it.
3. Tap your picture or initial, then **Location sharing**, then **New share** again.

If he doesn't have Gmail, tap **Copy to clipboard** on that screen and send him the link instead.

## tr056-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
I want the Spotify app on my iPhone but I don't want to be charged anything just for getting it. How do I make sure it's free and get it?

**ASSISTANT:**
Free apps show **Get** instead of a price, and you won't be charged to download them.

1. Open the **App Store** app.
2. Tap the **Search** tab and look for **Spotify**.
3. Check the button next to the app. If it says **Get**, it is free to download. If it shows a price, it is not free.
4. Tap **Get**.
5. Confirm by double-clicking the **side button**. Look at the screen if you use Face ID, or rest your finger on the Touch ID button. You may need your Apple Account password.

Some free apps offer in-app purchases and subscriptions, but those are optional.

## tr056-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
Please tell me how to get the Zoom app on my iPhone.

**ASSISTANT:**
You can get it from the **App Store**.

1. Open the **App Store** app.
2. Tap the **Search** tab and look for **Zoom**.
3. Tap **Get**.
4. Confirm by double-clicking the **side button**. Use Face ID or Touch ID, or enter your Apple Account password if asked.

**USER:**
I can't find the App Store on my phone. The icon is gone.

**ASSISTANT:**
Let's look for it.

1. Swipe down from the middle of your Home Screen and search for **App Store**.
2. If it still doesn't appear, **Content & Privacy Restrictions** may be turned on. Adjust the **iTunes & App Store Purchases** settings and set **Installing Apps** to **Allow**.

The App Store should then reappear.

## tr057-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
I have an Android phone and I need my bank's app. I only want to get it from a safe place and I want to be sure it's a good one before I put it on my phone. What should I do?

**ASSISTANT:**
The safest place is the **Play Store**. Google Play Protect checks for harmful apps, warns you, and removes them if necessary. Apps from unknown sources can put your device and personal information at risk.

1. Open the **Play Store** app.
2. Find the app you want.
3. Under the app's title, look at the star ratings and the number of downloads.
4. To read what other people say, scroll down to **Ratings and reviews**.
5. If it looks right, tap **Install**.

When the install is done, the app is on your phone.

## tr057-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
How do I put a weather app on my Android phone?

**ASSISTANT:**
You can get it from the **Play Store**.

1. Open the **Play Store** app.
2. Find the weather app you want.
3. Under the title, look at the star ratings and the number of downloads.
4. Tap **Install**.

**USER:**
There's no Install button. There's a price with a dollar sign where it should be.

**ASSISTANT:**
A price means it is a paid app. Free apps show **Install**.

1. If you only want a free app, don't tap the price. Go back and look for a different weather app that shows **Install**.
2. If you do want this paid app, tap the price.

## tr058-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Delete an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101550

**USER:**
All the icons on my iPhone are shaking and have little minus signs on them. I must have held one too long. I don't want to mess up the others, I only want to delete the Candy Crush game. What do I do now?

**ASSISTANT:**
Your phone is in the mode where you can delete apps, so you can finish from there. Only the app you pick will be deleted.

1. Tap the **minus** icon in the upper-left corner of the Candy Crush app.
2. Tap **Delete App**.
3. Tap **Delete** to confirm.
4. Tap **Done** at the top of the screen to stop the icons shaking.

Deleting an app does not cancel subscriptions inside it. If you pay for something in the game, cancel that first.

## tr058-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Delete an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101550

**USER:**
How can I take the Facebook app off my iPhone? I don't use it anymore.

**ASSISTANT:**
You can delete it from the Home Screen.

1. Touch and hold the app.
2. Tap **Remove App**.
3. Tap **Delete App**.
4. Tap **Delete** to confirm.

Deleting an app doesn't cancel subscriptions inside it, so cancel any you don't need first.

**USER:**
I held it but there is no Remove App choice, or it won't let me delete it.

**ASSISTANT:**
A few things can cause that.

1. Some built-in Apple apps can't be deleted.
2. If it's not an Apple app, check your parental control settings and make sure deleting apps is set to **Allow**. Then try again.
3. If your iPhone is managed by a company or school, you may not be able to delete apps. Contact your device administrator.

## tr059-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en

**USER:**
I paid for a puzzle game on my Android phone, but I never play it and my phone is full. I might want it back someday though and I don't want to pay twice. Can I take it off?

**ASSISTANT:**
Yes. If you bought an app, you can reinstall it later without buying it again.

1. Open the **Play Store** app.
2. At the top right, tap your **Profile icon**.
3. Tap **Manage apps & devices**, then tap **Manage**.
4. Tap the name of the puzzle game.
5. Tap **Uninstall**.

Some of these steps work only on Android 13 and up.

## tr059-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en

**USER:**
How do I get rid of an app I don't use on my Android phone?

**ASSISTANT:**
You can remove it through the Play Store.

1. Open the **Play Store** app.
2. At the top right, tap your **Profile icon**.
3. Tap **Manage apps & devices**, then tap **Manage**.
4. Tap the name of the app you want to delete.
5. Tap **Uninstall**.

**USER:**
I did that for a weather app that came with my phone, but there's no Uninstall button for it.

**ASSISTANT:**
That app is probably a system app that came with the phone. You can't delete some of those.

On some phones you can turn them off instead, so they won't show on your list of apps. I don't have the exact steps for turning one off. Your phone maker's support can tell you if your phone allows it.

Apps you installed yourself can still be removed with **Uninstall**.

## tr060-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

**USER:**
Windows 11 here. The Settings pages confuse me with all the menus. Is there a faster way to remove my old photo program straight from the Start menu?

**ASSISTANT:**
Yes. You can do it right from the Start menu.

1. Click the **Start** button.
2. Click **All apps**.
3. Find your photo program in the list.
4. Right-click it.
5. Click **Uninstall**.

Some programs are built into Windows and can't be uninstalled.

## tr060-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

**USER:**
My Windows 11 PC has an old printer program I never use anymore and I want it gone.

**ASSISTANT:**
You can use Settings.

1. Click **Start**, then **Settings**.
2. Click **Apps**, then **Installed apps**.
3. Find the program in the list.
4. Click the **More** icon next to it, then click **Uninstall**.

**USER:**
I found my program there but Uninstall doesn't work from that screen.

**ASSISTANT:**
Some programs can't be uninstalled from Settings. Use Control Panel instead.

1. In the search box on the taskbar, type **Control Panel** and click it.
2. Click **Programs**, then **Programs and Features**.
3. Right-click the program and click **Uninstall** or **Uninstall/Change**.
4. Follow the directions on the screen.

## tr061-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Free up storage space (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108429

**USER:**
My iPhone is almost out of room. I don't want to lose any of my photos or anything saved inside my apps. Is there a way to get space back without losing my stuff?

**ASSISTANT:**
Yes. Offloading removes an app but keeps its documents and data.

1. Open the **Settings** app.
2. Tap **General**, then tap **iPhone Storage**.
3. Tap **Show All** to see recommendations for your iPhone.
4. If you see **Offload Unused Apps**, tap **Enable**.

You can also offload one app yourself. Tap the app in the list, then tap **Offload App**.

Don't tap **Delete App**. That removes the app and its data.

## tr061-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Free up storage space (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108429

**USER:**
My iPhone keeps saying Storage Almost Full. How do I find out what's taking up the room?

**ASSISTANT:**
You can see it in Settings.

1. Open the **Settings** app.
2. Tap **General**, then tap **iPhone Storage**.
3. Look at the recommendations at the top and the list of apps below.
4. Tap an app to see **Offload App** or **Delete App**.

**USER:**
I see a big piece called Other, and another called System. How do I delete those?

**ASSISTANT:**
You can't delete those directly.

1. **Other** is system files, logs, caches and similar data that can't be removed. **System** is the space iOS itself uses.
2. The phone clears cached and temporary files by itself when it needs space.
3. To free room yourself, tap **Show All** under the recommendations, or tap an app in the list and choose **Offload App** or **Delete App**.
