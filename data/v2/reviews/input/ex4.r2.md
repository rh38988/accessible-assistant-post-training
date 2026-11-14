# Review input: batch ex4, round 2 (36 examples)

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
Thanks. iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.

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
2. Tap **More options**.
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

## tr049-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
too many robocalls, can my phone block them?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr049-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
Pixel 8, using the default Google Phone app. Caller ID shows 'Suspected spam' but they still ring. How do I make those not ring at all?

**ASSISTANT:**
Since your phone already labels them, you just need to turn on **Filter spam calls**. It takes about a minute.

1. Open the **Phone** app.
2. Tap **More options**.
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls are handled by the filter. You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

## tr049-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Pixel)
- task: Filter spam calls (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/3459196?hl=en

**USER:**
too many robocalls, can my phone block them?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, a Google Pixel 7a

**ASSISTANT:**
Thanks. The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap **More options**.
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

## tr050-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
my battery dies so fast

**ASSISTANT:**
That's annoying. Is your phone an **iPhone** or an **Android** phone?

## tr050-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
battery health

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

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

All three will get your message.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.

## tr051-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

**USER:**
I want to tell my three children about our Thanksgiving plans but typing the same message three times is a pain and I always forget someone. I have an iPhone.

**ASSISTANT:**
A group text will send it to all three at once, so no one gets left out. It takes about a minute. Here's how:

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

All three will get your message.

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

All three will get your message.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.

## tr052-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
Is there a way to make every website bigger in Chrome on my computer, so I don't have to zoom in each time?

**ASSISTANT:**
You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click **More** at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.

Every website will now open at that size.

To zoom in on just one page, hold the **Ctrl** key and press **+** (on a Mac, use the **Command** key instead).

## tr052-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make every web page bigger by default (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
make websites bigger

**ASSISTANT:**
Sure. Which web browser do you use, such as **Chrome**, **Edge**, or **Safari**?

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
Thanks. You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click **More** at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom**, click the down arrow next to it, and pick a bigger zoom level from the list.

Every website will now open at that size.

To zoom in on just one page, hold the **Ctrl** key and press **+** (on a Mac, use the **Command** key instead).

## tr054-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

**USER:**
how can my daughter see where I am

**ASSISTANT:**
That's a nice way to give her peace of mind. Do you and your daughter both use **iPhones**?

## tr054-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Share location with family (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105104

**USER:**
share location

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

## tr055-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I share my location with my son using Google Maps on my Android phone?

**ASSISTANT:**
Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your location will be shared for the time you picked.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.

## tr055-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I want my son to be able to see where I am when I drive

**ASSISTANT:**
That's a good safety idea. Is your phone an **iPhone** or an **Android** phone?

## tr055-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I drive to my sister's house two hours away every weekend and my son always wants me to text him when I get there but I forget. He said there's a way in Google Maps so he can just see. I have an Android.

**ASSISTANT:**
Yes, then he won't have to wait for your text. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your location will be shared for the time you picked.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.

## tr055-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

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
3. Type **WhatsApp** to search.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the **Touch ID** button. You may also be asked for your Apple Account password.

When it's done, you'll see **Open** instead of **Get**.

## tr056-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
how do I download an app

**ASSISTANT:**
I can walk you through it. Is your phone an **iPhone** or an **Android** phone?

## tr056-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
app store download

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

## tr056-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

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

## tr057-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en ; https://support.google.com/googleplay/answer/113409

**USER:**
How do I install an app on my Android phone? My doctor's office wants me to download their app.

**ASSISTANT:**
You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Search for the app by name, or browse.
3. Tap the app, then check the star ratings and the number of downloads under its title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)

It's safest to get apps from Google Play. Google Play Protect checks for harmful apps, and apps from unknown sources can put your phone and personal information at risk.

## tr057-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
how do I get an app on my phone

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone?

## tr057-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en ; https://support.google.com/googleplay/answer/113409

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

## tr057-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en ; https://support.google.com/googleplay/answer/113409

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

Deleting an app also removes its data from your phone.

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
3. Tap **Manage apps & devices**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

Some apps that came with the phone can't be deleted. On some phones you can turn them off instead.

If you change your mind later, you can reinstall it from the Play Store without paying again.

## tr059-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

**USER:**
When I bought my Android phone the store guy put a bunch of games and things on it that I'll never use, and they keep sending me notifications. How do I take them off?

**ASSISTANT:**
You can remove most of them. Some apps that came built into the phone can only be turned off, not deleted, but most apps can be removed through the **Play Store** like this. It takes about a minute:

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & devices**.
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
3. Tap **Manage apps & devices**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

Some apps that came with the phone can't be deleted. On some phones you can turn them off instead.

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
5. Click **More** next to it, then click **Uninstall**.
6. Follow any directions that appear on the screen.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.

## tr060-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Uninstall a program (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98

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
5. Click **More** next to it, then click **Uninstall**.
6. Follow any directions that appear on the screen.

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
4. You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.
5. Tap an app's name, then choose to offload or delete it. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.

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
4. You'll see recommendations and a list of your apps with how much space each uses. You can tap **Show All** to see more recommendations.
5. Tap an app's name, then choose to offload or delete it. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.
