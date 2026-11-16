# Rule scan input, part 05 (50 examples)

## tr050-e
- task: Check battery health | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: iPhone battery and performance <https://support.apple.com/en-us/101575>

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

---

## tr051-b
- task: Start a group text | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Send a group text message on your iPhone or iPad <https://support.apple.com/en-us/118236>

**USER:**
how do I text all my kids at once

**ASSISTANT:**
You can send a group text. Is your phone an **iPhone** or an **Android** phone? If you're not sure, an iPhone has an apple logo on the back.

---

## tr051-c
- task: Start a group text | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Send a group text message on your iPhone or iPad <https://support.apple.com/en-us/118236>

**USER:**
I want to tell my three children about our Thanksgiving plans but typing the same message three times is a pain and I always forget someone. I have an iPhone.

**ASSISTANT:**
You can send one group text from Messages to all three of them. It takes about a minute. Here's how:

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

If a recipient is not using iMessage, the message is sent as an MMS or SMS.

To send a group MMS message on your iPhone, go to **Settings**, then **Messages**, and turn on **MMS Messaging**. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging.

---

## tr051-d
- task: Start a group text | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Send a group text message on your iPhone or iPad <https://support.apple.com/en-us/118236>

**USER:**
how do I text all my kids at once

**ASSISTANT:**
You can send a group text. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks, here's how on your iPhone.

You can start a group text. It takes about a minute.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

If a recipient is not using iMessage, the message is sent as an MMS or SMS.

To send a group MMS message on your iPhone, go to **Settings**, then **Messages**, and turn on **MMS Messaging**. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging.

---

## tr051-e
- task: Start a group text | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Send a group text message on your iPhone or iPad <https://support.apple.com/en-us/118236>

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

---

## tr052-a
- task: Make every web page bigger by default | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
Is there a way to make every website bigger in Chrome on my computer, so I don't have to zoom in each time?

**ASSISTANT:**
You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click **More** at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.

Every website will now open at that size.

To zoom in with the keyboard, press **Ctrl** and **+** (on a Mac, press **Command** and **+**).

---

## tr052-b
- task: Make every web page bigger by default | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
websites are too small on my computer

**ASSISTANT:**
I can help you make them bigger. Which web browser do you use, for example **Chrome**, **Edge**, or **Safari**? If you're not sure, tell me what the icon you click looks like.

---

## tr052-d
- task: Make every web page bigger by default | platform: Chrome (computer) | scenario: followup | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
websites are too small on my computer

**ASSISTANT:**
I can help you make them bigger. Which web browser do you use, for example **Chrome**, **Edge**, or **Safari**? If you're not sure, tell me what the icon you click looks like.

**USER:**
Chrome

**ASSISTANT:**
Thanks. You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click **More** at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.

Every website will now open at that size.

To zoom in with the keyboard, press **Ctrl** and **+** (on a Mac, press **Command** and **+**).

---

## tr052-e
- task: Make every web page bigger by default | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

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

---

## tr052-r
- task: Make every web page bigger by default | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

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

---

## tr054-a
- task: Share location with family | platform: iPhone (Find My) | scenario: direct | sensitive: True
- sources: Apple Support: Share your location with iPhone <https://support.apple.com/en-us/105104>

**USER:**
How can I share my location with my daughter on my iPhone so she knows I got home safe?

**ASSISTANT:**
You can do this in the **Find My** app. It takes about two minutes. You and your daughter both need iPhones with a recent software update.

1. Open the **Find My** app.
2. Tap **Me** at the bottom, and make sure **Share My Location** is turned on.
3. Tap **People** at the bottom.
4. Tap the **Add** button (a plus sign), then tap **Share My Location**.
5. Choose your daughter.
6. Choose how long to share, such as **one hour**, **until the end of the day**, or **indefinitely**. Some versions also let you pick a custom time.

Your daughter can then see where you are in her Find My app.

Only share your location with people you trust.

---

## tr054-b
- task: Share location with family | platform: iPhone (Find My) | scenario: missing_info | sensitive: True
- sources: Apple Support: Share your location with iPhone <https://support.apple.com/en-us/105104>

**USER:**
how can my daughter see where I am

**ASSISTANT:**
That's a nice way to give her peace of mind. Do you and your daughter both use **iPhones**?

---

## tr054-d
- task: Share location with family | platform: iPhone (Find My) | scenario: followup | sensitive: True
- sources: Apple Support: Share your location with iPhone <https://support.apple.com/en-us/105104>

**USER:**
how can my daughter see where I am

**ASSISTANT:**
That's a nice way to give her peace of mind. Do you and your daughter both use **iPhones**?

**USER:**
Yes, we both have iPhones

**ASSISTANT:**
Great. Since you both have iPhones, you can do this in the **Find My** app. It takes about two minutes. You and your daughter both need iPhones with a recent software update.

1. Open the **Find My** app.
2. Tap **Me** at the bottom, and make sure **Share My Location** is turned on.
3. Tap **People** at the bottom.
4. Tap the **Add** button (a plus sign), then tap **Share My Location**.
5. Type your daughter's name and tap it when it appears.
6. Tap **Send**.
7. Choose how long to share, such as **one hour**, **until the end of the day**, or **indefinitely**. Some versions also let you pick a custom time.

Your daughter can then see where you are in her Find My app.

Only share your location with people you trust.

---

## tr054-e
- task: Share location with family | platform: iPhone (Find My) | scenario: constraint | sensitive: True
- sources: Apple Support: Share your location with iPhone <https://support.apple.com/en-us/105104>

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

---

## tr055-a
- task: Share location with family | platform: Android (Google Maps) | scenario: direct | sensitive: True
- sources: Google Maps Help: Share your real-time location with others (Android) <https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
How do I share my location with my son using Google Maps on my Android phone?

**ASSISTANT:**
Here's how. It takes about two minutes. If he uses Gmail, save his Gmail address in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your location will be shared for the time you picked.

If he doesn't use Gmail, skip steps 6 and 7. Instead, tap **Copy to clipboard**, then paste the link into a text or email to him. Anyone with the link can see your real-time location for up to 24 hours. Only share your location with people you trust.

---

## tr055-b
- task: Share location with family | platform: Android (Google Maps) | scenario: missing_info | sensitive: True
- sources: Google Maps Help: Share your real-time location with others (Android) <https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I want my son to be able to see where I am when I drive

**ASSISTANT:**
That's a good safety idea. Is your phone an **iPhone** or an **Android** phone?

---

## tr055-c
- task: Share location with family | platform: Android (Google Maps) | scenario: direct_messy | sensitive: True
- sources: Google Maps Help: Share your real-time location with others (Android) <https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I drive to my sister's house two hours away every weekend and my son always wants me to text him when I get there but I forget. He said there's a way in Google Maps so he can just see. I have an Android.

**ASSISTANT:**
Yes, then he won't have to wait for your text. It takes about two minutes. If he uses Gmail, save his Gmail address in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your location will be shared for the time you picked.

If he doesn't use Gmail, skip steps 6 and 7. Instead, tap **Copy to clipboard**, then paste the link into a text or email to him. Anyone with the link can see your real-time location for up to 24 hours. Only share your location with people you trust.

---

## tr055-d
- task: Share location with family | platform: Android (Google Maps) | scenario: followup | sensitive: True
- sources: Google Maps Help: Share your real-time location with others (Android) <https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I want my son to be able to see where I am when I drive

**ASSISTANT:**
That's a good safety idea. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, and yes he uses Gmail

**ASSISTANT:**
Great. Google Maps can do this. It takes about two minutes, and your son's Gmail address needs to be saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your location will be shared for the time you picked.

Only share your location with people you trust.

---

## tr055-e
- task: Share location with family | platform: Android (Google Maps) | scenario: constraint | sensitive: True
- sources: Google Maps Help: Share your real-time location with others (Android) <https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid>

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

---

## tr055-r
- task: Share location with family | platform: Android (Google Maps) | scenario: failure_recovery | sensitive: True
- sources: Google Maps Help: Share your real-time location with others (Android) <https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid>

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

---

## tr056-a
- task: Install an app | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Download apps on your iPhone or iPad <https://support.apple.com/en-us/102590>

**USER:**
How do I download the WhatsApp app on my iPhone?

**ASSISTANT:**
You can get it from the **App Store**. It takes a couple of minutes.

1. Open the **App Store** app.
2. Tap **Search** at the bottom.
3. Type **WhatsApp** to search.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the **Touch ID** button. You may also be asked for your Apple Account password.

When it's done, you'll see **Open** instead of **Get**.

---

## tr056-b
- task: Install an app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Download apps on your iPhone or iPad <https://support.apple.com/en-us/102590>

**USER:**
how do I download an app

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone?

---

## tr056-c
- task: Install an app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Download apps on your iPhone or iPad <https://support.apple.com/en-us/102590>

**USER:**
app store download

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr056-d
- task: Install an app | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Download apps on your iPhone or iPad <https://support.apple.com/en-us/102590>

**USER:**
how do I download an app

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone, I want WhatsApp

**ASSISTANT:**
Great, here's how to get WhatsApp.

You can get it from the **App Store**. It takes a couple of minutes.

1. Open the **App Store** app.
2. Tap **Search** at the bottom.
3. Type **WhatsApp** to search.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the **Touch ID** button. You may also be asked for your Apple Account password.

When it's done, you'll see **Open** instead of **Get**.

---

## tr056-e
- task: Install an app | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Download apps on your iPhone or iPad <https://support.apple.com/en-us/102590>

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

---

## tr057-a
- task: Install an app | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Download apps to your Android device <https://support.google.com/android/answer/9457058?hl=en>; Google Play Help: Download and install apps from Google Play <https://support.google.com/googleplay/answer/113409>

**USER:**
How do I install an app on my Android phone? My doctor's office wants me to download their app.

**ASSISTANT:**
You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Search for the app by name, or browse.
3. Tap the app, then check the star ratings and the number of downloads under its title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)

It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.

---

## tr057-b
- task: Install an app | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Download apps to your Android device <https://support.google.com/android/answer/9457058?hl=en>

**USER:**
how do I get an app on my phone

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone?

---

## tr057-c
- task: Install an app | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Download apps to your Android device <https://support.google.com/android/answer/9457058?hl=en>; Google Play Help: Download and install apps from Google Play <https://support.google.com/googleplay/answer/113409>

**USER:**
My neighbor told me there's an app that shows when the bus is coming, and I'd like to try it. I've never downloaded an app myself. My phone is a Samsung Galaxy.

**ASSISTANT:**
That sounds handy. Ask your neighbor for the app's exact name, then follow these steps:

You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Search for the app by name, or browse.
3. Tap the app, then check the star ratings and the number of downloads under its title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)

It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.

---

## tr057-d
- task: Install an app | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Download apps to your Android device <https://support.google.com/android/answer/9457058?hl=en>; Google Play Help: Download and install apps from Google Play <https://support.google.com/googleplay/answer/113409>

**USER:**
how do I get an app on my phone

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android. It's the app for my doctor's office.

**ASSISTANT:**
Thanks. If you don't have the app's exact name, ask the office for it. Then:

You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Search for the app by name, or browse.
3. Tap the app, then check the star ratings and the number of downloads under its title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)

It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.

---

## tr057-e
- task: Install an app | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Download apps to your Android device <https://support.google.com/android/answer/9457058?hl=en>

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

---

## tr057-r
- task: Install an app | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Download apps to your Android device <https://support.google.com/android/answer/9457058?hl=en>

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
2. Tapping the price is how you buy the app, so only tap it if you mean to pay for it.

---

## tr058-a
- task: Delete an app | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Delete apps on your iPhone or iPad <https://support.apple.com/en-us/101550>; Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
How do I delete an app I don't use anymore from my iPhone?

**ASSISTANT:**
Here's how. It takes a few seconds.

1. Find the app on your Home Screen.
2. **Press and hold** the app's icon until a menu appears.
3. Tap **Remove App**.
4. Tap **Delete App**.
5. Tap **Delete** to confirm.

If the icons start to jiggle instead of showing a menu:
1. Tap the **minus** sign in the app's upper-left corner.
2. Tap **Delete App**.
3. Tap **Delete**.
4. Tap **Done** at the top of the screen.

Deleting an app also removes its data from your phone.

Deleting an app does **not** cancel any paid subscriptions inside it. If you pay for the app every month, cancel the subscription first.

---

## tr058-b
- task: Delete an app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Delete apps on your iPhone or iPad <https://support.apple.com/en-us/101550>; Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
how do I get rid of an app

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr058-c
- task: Delete an app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Delete apps on your iPhone or iPad <https://support.apple.com/en-us/101550>; Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
delete app

**ASSISTANT:**
Sure, I can help you delete an app. Is it on an **iPhone**, an **Android** phone, or a **computer**?

---

## tr058-d
- task: Delete an app | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Delete apps on your iPhone or iPad <https://support.apple.com/en-us/101550>; Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
how do I get rid of an app

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iphone

**ASSISTANT:**
Thanks.

Here's how. It takes a few seconds.

1. Find the app on your Home Screen.
2. **Press and hold** the app's icon until a menu appears.
3. Tap **Remove App**.
4. Tap **Delete App**.
5. Tap **Delete** to confirm.

If the icons start to jiggle instead of showing a menu:
1. Tap the **minus** sign in the app's upper-left corner.
2. Tap **Delete App**.
3. Tap **Delete**.
4. Tap **Done** at the top of the screen.

Deleting an app also removes its data from your phone. If you might want it later, you can download it again from the App Store.

Deleting an app does **not** cancel any paid subscriptions inside it. If you pay for the app every month, cancel the subscription first.

---

## tr058-e
- task: Delete an app | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Delete apps on your iPhone or iPad <https://support.apple.com/en-us/101550>

**USER:**
All the icons on my iPhone are shaking and have little minus signs on them. I must have held one too long. I don't want to mess up the others, I only want to delete the Candy Crush game. What do I do now?

**ASSISTANT:**
Your phone is in the mode where you can delete apps, so you can finish from there. Only the app you pick will be deleted.

1. Tap the **minus** icon in the upper-left corner of the Candy Crush app.
2. Tap **Delete App**.
3. Tap **Delete** to confirm.
4. Tap **Done** at the top of the screen to stop the icons shaking.

Deleting an app does not cancel subscriptions inside it. If you pay for something in the game, cancel that first.

---

## tr059-a
- task: Delete an app | platform: Android | scenario: direct | sensitive: False
- sources: Google Play Help: Delete apps on your Android device <https://support.google.com/googleplay/answer/13627402?hl=en>; Android Help: Free up storage on your Android device <https://support.google.com/android/answer/7431795?hl=en>; Google Play Help: Disable apps that came with your Android device <https://support.google.com/googleplay/answer/13627571?hl=en>

**USER:**
How do I uninstall an app on my Android phone?

**ASSISTANT:**
You can remove it through the Play Store. It takes about a minute. Some of these steps work only on Android 13 and up.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & devices**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

Some apps that came with the phone can't be deleted. On some phones you can turn them off instead.

If you change your mind later, you can reinstall it from the Play Store without paying again.

---

## tr059-c
- task: Delete an app | platform: Android | scenario: direct_messy | sensitive: False
- sources: Google Play Help: Delete apps on your Android device <https://support.google.com/googleplay/answer/13627402?hl=en>; Android Help: Free up storage on your Android device <https://support.google.com/android/answer/7431795?hl=en>; Google Play Help: Disable apps that came with your Android device <https://support.google.com/googleplay/answer/13627571?hl=en>

**USER:**
When I bought my Android phone the store guy put a bunch of games and things on it that I'll never use, and they keep sending me notifications. How do I take them off?

**ASSISTANT:**
Some apps that came with the phone can't be removed. On some phones you can turn them off instead. Other apps can be uninstalled through the **Play Store** like this, though some of these steps work only on Android 13 and up. It takes about a minute:

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & devices**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.

---

## tr059-d
- task: Delete an app | platform: Android | scenario: followup | sensitive: False
- sources: Google Play Help: Delete apps on your Android device <https://support.google.com/googleplay/answer/13627402?hl=en>; Android Help: Free up storage on your Android device <https://support.google.com/android/answer/7431795?hl=en>; Google Play Help: Disable apps that came with your Android device <https://support.google.com/googleplay/answer/13627571?hl=en>

**USER:**
my phone has apps I never use, can I get rid of them

**ASSISTANT:**
Yes, you can remove them. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks. Here's one way to do it. Some of these steps work only on Android 13 and up.

You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & devices**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

Some apps that came with the phone can't be deleted. On some phones you can turn them off instead.

If you change your mind later, you can reinstall it from the Play Store without paying again.

---

## tr059-e
- task: Delete an app | platform: Android | scenario: constraint | sensitive: False
- sources: Google Play Help: Delete apps on your Android device <https://support.google.com/googleplay/answer/13627402?hl=en>

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

---

## tr059-r
- task: Delete an app | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Google Play Help: Delete apps on your Android device <https://support.google.com/googleplay/answer/13627402?hl=en>

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

---

## tr060-a
- task: Uninstall a program | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Uninstall or remove apps and programs in Windows <https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98>

**USER:**
How do I uninstall a program from my Windows 11 computer?

**ASSISTANT:**
Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click **More** next to it, then click **Uninstall**.
6. Follow any directions that appear on the screen.

If the program can't be uninstalled here, type **Control Panel** in the search box on the taskbar and open it. Click **Programs**, then **Programs and Features**. Right-click the program, choose **Uninstall** or **Uninstall/Change**, and follow the directions on the screen.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.

---

## tr060-b
- task: Uninstall a program | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Uninstall or remove apps and programs in Windows <https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98>

**USER:**
how do I remove a program from my computer

**ASSISTANT:**
I can help. Is your computer a **Windows** computer or a **Mac**?

---

## tr060-c
- task: Uninstall a program | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Uninstall or remove apps and programs in Windows <https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98>

**USER:**
Windows 11 Home, HP laptop. There's an old program called PhotoEasy that came preinstalled. I want it gone. Settings or Control Panel?

**ASSISTANT:**
You can start in Settings. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click **More** next to it, then click **Uninstall**.
6. Follow any directions that appear on the screen.

If PhotoEasy is not in the list, use Control Panel:

1. Type **Control Panel** in the search box on the taskbar and open it.
2. Click **Programs**, then **Programs and Features**.
3. Right-click PhotoEasy and choose **Uninstall** (or **Uninstall/Change**).
4. Follow any directions that appear on the screen.

---

## tr060-d
- task: Uninstall a program | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Uninstall or remove apps and programs in Windows <https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98>

**USER:**
how do I remove a program from my computer

**ASSISTANT:**
I can help. Is your computer a **Windows** computer or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks.

Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click **More** next to it, then click **Uninstall**.
6. Follow any directions that appear on the screen.

If the program can't be uninstalled here, type **Control Panel** in the search box on the taskbar and open it. Click **Programs**, then **Programs and Features**. Right-click the program, choose **Uninstall** or **Uninstall/Change**, and follow the directions on the screen.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.

---

## tr060-e
- task: Uninstall a program | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Uninstall or remove apps and programs in Windows <https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98>

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

---

## tr060-r
- task: Uninstall a program | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Uninstall or remove apps and programs in Windows <https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98>

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

---

## tr061-a
- task: Free up storage space | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
My iPhone says storage is almost full. How do I free up space?

**ASSISTANT:**
Let's see what's using the space first. This takes a few minutes.

1. Open the **Settings** app.
2. Tap **General**.
3. Tap **iPhone Storage**.
4. You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.
5. Tap an app's name. In the detailed view, you can offload the app or delete the app. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.

---

## tr061-b
- task: Free up storage space | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
my phone says it's full

**ASSISTANT:**
I can help you free up some space. Is your phone an **iPhone** or an **Android** phone?

---

## tr061-d
- task: Free up storage space | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

**USER:**
my phone says it's full

**ASSISTANT:**
I can help you free up some space. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone 11

**ASSISTANT:**
Thanks.

Let's see what's using the space first. This takes a few minutes.

1. Open the **Settings** app.
2. Tap **General**.
3. Tap **iPhone Storage**.
4. You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.
5. Tap an app's name. In the detailed view, you can offload the app or delete the app. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.

---
