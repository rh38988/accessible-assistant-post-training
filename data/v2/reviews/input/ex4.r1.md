# Review input: batch ex4, round 1 (52 examples)

## tr048-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Silence calls from unknown numbers (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111106

**USER:**
I get a lot of spam calls from numbers I don't know. Can I make my iPhone only ring for people in my contacts?

**ASSISTANT:**
iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Apps**, then **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from people in your contacts will still ring normally. Unknown callers go to voicemail, so check your voicemail now and then in case a doctor's office or pharmacy calls from a new number.

Tip: save important numbers, like your doctor and pharmacy, to your contacts so they always ring through.

## tr048-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Silence calls from unknown numbers (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111106

**USER:**
How do I stop spam calls?

**ASSISTANT:**
There are a few ways to cut down on them. Is your phone an **iPhone** or an **Android** phone?

## tr048-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Silence calls from unknown numbers (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111106

**USER:**
Every day I get calls about my car warranty and I don't even have a car anymore. It's driving me crazy.

**ASSISTANT:**
Those calls are so annoying. There are phone settings that can quiet calls from numbers you don't know.

**Is your phone an iPhone or an Android phone?**

## tr048-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Silence calls from unknown numbers (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111106

**USER:**
How do I stop spam calls?

**ASSISTANT:**
There are a few ways to cut down on them. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. One helpful option on iPhone is to silence calls from numbers you don't know.

iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Apps**, then **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from people in your contacts will still ring normally. Unknown callers go to voicemail, so check your voicemail now and then in case a doctor's office or pharmacy calls from a new number.

Tip: save important numbers, like your doctor and pharmacy, to your contacts so they always ring through.

## tr049-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
Can my Google Pixel phone filter out spam calls automatically?

**ASSISTANT:**
The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap the **More options** menu (three dots).
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls won't ring or notify you, but they still appear in your call history.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

## tr049-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
too many robocalls, can my phone block them?

**ASSISTANT:**
Many phones can filter them. Is yours an **iPhone** or an **Android** phone? If it's Android, which brand?

## tr049-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
Pixel 8, using the default Google Phone app. Caller ID shows 'Suspected spam' but they still ring. How do I make those not ring at all?

**ASSISTANT:**
Since your phone already labels them, you just need to turn on filtering:

The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap the **More options** menu (three dots).
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls won't ring or notify you, but they still appear in your call history.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

## tr049-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
too many robocalls, can my phone block them?

**ASSISTANT:**
Many phones can filter them. Is yours an **iPhone** or an **Android** phone? If it's Android, which brand?

**USER:**
Google Pixel 7a

**ASSISTANT:**
Thanks. The Pixel has a built-in spam filter.

The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap the **More options** menu (three dots).
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls won't ring or notify you, but they still appear in your call history.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

## tr050-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
My iPhone battery seems to die quickly. How do I check the battery health?

**ASSISTANT:**
You can check it in Settings. It takes a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**. On some versions the name is slightly different.
4. Look at **Maximum Capacity**. This compares your battery now to when it was new. A lower number means it won't last as long between charges.

If you see a message that your battery's health is **significantly degraded**, it isn't a safety problem, but a new battery would help it last longer. Apple offers battery service, and it may be covered if your phone is still under warranty.

## tr050-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
my battery dies so fast

**ASSISTANT:**
That's annoying. I can help you check what's going on. Is your phone an **iPhone** or an **Android** phone, and about how old is it?

## tr050-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
battery health

**ASSISTANT:**
Sure. Do you want to **check your battery's health**? If so, is your phone an iPhone or an Android phone?

## tr050-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
my battery dies so fast

**ASSISTANT:**
That's annoying. I can help you check what's going on. Is your phone an **iPhone** or an **Android** phone, and about how old is it?

**USER:**
iPhone, about 4 years old

**ASSISTANT:**
Thanks. At four years old, the battery may be worn. Let's check:

You can check it in Settings. It takes a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**. On some versions the name is slightly different.
4. Look at **Maximum Capacity**. This compares your battery now to when it was new. A lower number means it won't last as long between charges.

If you see a message that your battery's health is **significantly degraded**, it isn't a safety problem, but a new battery would help it last longer. Apple offers battery service, and it may be covered if your phone is still under warranty.

## tr051-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

**USER:**
How do I send one text message to my three kids at the same time on my iPhone?

**ASSISTANT:**
You can start a group text. It takes about a minute.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

All three will get the message, and when anyone replies, everyone in the group sees it.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.

## tr051-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: True
- sources: https://support.apple.com/en-us/118236

**USER:**
how do I text all my kids at once

**ASSISTANT:**
You can send a group text. Is your phone an **iPhone** or an **Android** phone? If you're not sure, an iPhone has an apple logo on the back.

## tr051-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

**USER:**
I want to tell my three children about our Thanksgiving plans but typing the same message three times is a pain and I always forget someone. I have an iPhone.

**ASSISTANT:**
A group text will send it to all three at once, so no one gets left out. Here's how:

You can start a group text. It takes about a minute.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

All three will get the message, and when anyone replies, everyone in the group sees it.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.

## tr051-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

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

All three will get the message, and when anyone replies, everyone in the group sees it.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.

## tr052-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
Is there a way to make every website bigger in Chrome on my computer, so I don't have to zoom in each time?

**ASSISTANT:**
You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click the **More** menu (three dots) at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom** and choose a bigger number, like **125%** or **150%**.

Every website will now open at that size.

To zoom in on just one page, hold the **Ctrl** key and press **+** (on a Mac, use the **Command** key instead).

## tr052-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
websites are too small on my computer

**ASSISTANT:**
I can help you make them bigger. Which web browser do you use, for example **Chrome**, **Edge**, or **Safari**? If you're not sure, tell me what the icon you click looks like.

## tr052-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
make websites bigger

**ASSISTANT:**
Sure. Do you want to make **one website** bigger right now, or make **every website** bigger from now on? And which browser do you use, such as Chrome or Safari?

## tr052-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
websites are too small on my computer

**ASSISTANT:**
I can help you make them bigger. Which web browser do you use, for example **Chrome**, **Edge**, or **Safari**? If you're not sure, tell me what the icon you click looks like.

**USER:**
Chrome

**ASSISTANT:**
Thanks. Chrome lets you set a bigger size for every website.

You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click the **More** menu (three dots) at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom** and choose a bigger number, like **125%** or **150%**.

Every website will now open at that size.

To zoom in on just one page, hold the **Ctrl** key and press **+** (on a Mac, use the **Command** key instead).

## tr054-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone (Find My)
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

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

## tr054-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

**USER:**
how can my daughter see where I am

**ASSISTANT:**
That's a nice way to give her peace of mind. Is your phone an **iPhone** or an **Android** phone? And does your daughter have an iPhone or Android?

## tr054-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

**USER:**
share location

**ASSISTANT:**
Sure. **Who would you like to share your location with**, and is your phone an **iPhone** or an **Android** phone?

## tr054-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (Find My)
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: True
- sources: https://support.apple.com/en-us/105104

**USER:**
how can my daughter see where I am

**ASSISTANT:**
That's a nice way to give her peace of mind. Is your phone an **iPhone** or an **Android** phone? And does your daughter have an iPhone or Android?

**USER:**
We both have iPhones

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

## tr055-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I share my location with my son using Google Maps on my Android phone?

**ASSISTANT:**
Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial** at the top.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your son can then see where you are in Google Maps.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.

## tr055-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I want my son to be able to see where I am when I drive

**ASSISTANT:**
That's a good safety idea. Is your phone an **iPhone** or an **Android** phone? And does your son use Gmail?

## tr055-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I drive to my sister's house two hours away every weekend and my son always wants me to text him when I get there but I forget. He said there's a way in Google Maps so he can just see. I have an Android.

**ASSISTANT:**
Yes, then he won't have to wait for your text. Here's how:

Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial** at the top.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your son can then see where you are in Google Maps.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.

## tr055-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I want my son to be able to see where I am when I drive

**ASSISTANT:**
That's a good safety idea. Is your phone an **iPhone** or an **Android** phone? And does your son use Gmail?

**USER:**
Android, and yes he uses Gmail

**ASSISTANT:**
Great. Google Maps can do this.

Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial** at the top.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your son can then see where you are in Google Maps.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.

## tr056-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
How do I download the WhatsApp app on my iPhone?

**ASSISTANT:**
You can get it from the **App Store**. It takes a couple of minutes.

1. Open the **App Store** app.
2. Tap **Search** at the bottom.
3. Type **WhatsApp** and tap the search button.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the Home button. You may also be asked for your Apple Account password.

When the download finishes, the button changes to **Open** and the app appears on your Home Screen.

Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.

## tr056-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
how do I download an app

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone? And which app would you like to get?

## tr056-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
app store download

**ASSISTANT:**
Sure, I can help you download an app from the App Store. **Which app would you like to get?**

## tr056-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
how do I download an app

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone? And which app would you like to get?

**USER:**
iPhone, I want WhatsApp

**ASSISTANT:**
Great, here's how to get WhatsApp.

You can get it from the **App Store**. It takes a couple of minutes.

1. Open the **App Store** app.
2. Tap **Search** at the bottom.
3. Type **WhatsApp** and tap the search button.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the Home button. You may also be asked for your Apple Account password.

When the download finishes, the button changes to **Open** and the app appears on your Home Screen.

Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.

## tr057-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
How do I install an app on my Android phone? My doctor's office wants me to download their app.

**ASSISTANT:**
You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.

## tr057-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
how do I get an app on my phone

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone? And which app are you looking for?

## tr057-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
My neighbor told me there's an app that shows when the bus is coming, and I'd like to try it. I've never downloaded an app myself. My phone is a Samsung Galaxy.

**ASSISTANT:**
That sounds handy. Ask your neighbor for the app's exact name, then follow these steps:

You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.

## tr057-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
how do I get an app on my phone

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone? And which app are you looking for?

**USER:**
Android. It's the app for my doctor's office.

**ASSISTANT:**
Thanks. If you don't have the app's exact name, ask the office for it. Then:

You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.

## tr058-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Delete an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101550 ; https://support.apple.com/en-us/108429

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

Deleting an app also removes its data from your phone. If you might want it later, you can download it again from the App Store.

Deleting an app does **not** cancel any paid subscriptions inside it. If you pay for the app every month, cancel the subscription first.

## tr058-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Delete an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101550 ; https://support.apple.com/en-us/108429

**USER:**
how do I get rid of an app

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

## tr058-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Delete an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101550 ; https://support.apple.com/en-us/108429

**USER:**
delete app

**ASSISTANT:**
Sure, I can help you delete an app. Is it on an **iPhone**, an **Android** phone, or a **computer**?

## tr058-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Delete an app (iPhone) | sensitive: False | reviewed by a person: True
- sources: https://support.apple.com/en-us/101550 ; https://support.apple.com/en-us/108429

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

## tr059-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

**USER:**
How do I uninstall an app on my Android phone?

**ASSISTANT:**
You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.

## tr059-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

**USER:**
my phone has apps I never use, can I get rid of them

**ASSISTANT:**
Yes, you can remove them. Is your phone an **iPhone** or an **Android** phone?

## tr059-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

**USER:**
When I bought my Android phone the store guy put a bunch of games and things on it that I'll never use, and they keep sending me notifications. How do I take them off?

**ASSISTANT:**
You can remove most of them. Some apps that came built into the phone can only be turned off, not deleted, but most apps can be removed like this:

You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.

## tr059-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

**USER:**
my phone has apps I never use, can I get rid of them

**ASSISTANT:**
Yes, you can remove them. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks. Here's one way that works on most Android phones.

You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.

## tr060-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

**USER:**
How do I uninstall a program from my Windows 11 computer?

**ASSISTANT:**
Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.

## tr060-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

**USER:**
how do I remove a program from my computer

**ASSISTANT:**
I can help. Is your computer a **Windows** computer or a **Mac**?

## tr060-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

**USER:**
Windows 11 Home, HP laptop. There's an old program called PhotoEasy that came preinstalled. I want it gone. Settings or Control Panel?

**ASSISTANT:**
Settings is the easiest place on Windows 11. If PhotoEasy doesn't appear there, open **Control Panel** and use **Programs and Features** instead.

Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.

## tr060-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

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
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.

## tr061-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Free up storage space (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108429

**USER:**
My iPhone says storage is almost full. How do I free up space?

**ASSISTANT:**
Let's see what's using the space first. This takes a few minutes.

1. Open the **Settings** app.
2. Tap **General**.
3. Tap **iPhone Storage**.
4. At the top, look at the **recommendations**. Tap one to see what it would remove, or tap **Show All** to see more.
5. Below that is a list of your apps. Tap an app to see your choices:
   - **Offload App** removes the app but keeps your documents and data, so nothing is lost if you reinstall it.
   - **Delete App** removes the app and its data.

Offloading apps you rarely use is a safe place to start.

## tr061-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Free up storage space (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108429

**USER:**
my phone says it's full

**ASSISTANT:**
I can help you free up some space. Is your phone an **iPhone** or an **Android** phone?

## tr061-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Free up storage space (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108429

**USER:**
I wanted to take pictures at my grandson's graduation but my phone said not enough storage. I don't understand, I don't have that many things on it.

**ASSISTANT:**
That's frustrating, especially at a big moment. Photos, videos, and apps can fill up space faster than you'd expect.

**Is your phone an iPhone or an Android phone?** Then I'll show you how to see what's using the space.

## tr061-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Free up storage space (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108429

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
4. At the top, look at the **recommendations**. Tap one to see what it would remove, or tap **Show All** to see more.
5. Below that is a list of your apps. Tap an app to see your choices:
   - **Offload App** removes the app but keeps your documents and data, so nothing is lost if you reinstall it.
   - **Delete App** removes the app and its data.

Offloading apps you rarely use is a safe place to start.
