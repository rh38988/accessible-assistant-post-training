# Review input: batch ex4, round 3 (14 examples)

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

If a recipient is not using iMessage, the message is sent as an MMS or SMS.

To send a group MMS message on your iPhone, go to **Settings**, then **Messages**, and turn on **MMS Messaging**. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging.

## tr051-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

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

If a recipient is not using iMessage, the message is sent as an MMS or SMS.

To send a group MMS message on your iPhone, go to **Settings**, then **Messages**, and turn on **MMS Messaging**. If you don't see that option, contact your carrier to check whether your plan supports Group MMS Messaging.

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

To zoom in with the keyboard, press **Ctrl** and **+** (on a Mac, press **Command** and **+**).

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

To zoom in with the keyboard, press **Ctrl** and **+** (on a Mac, press **Command** and **+**).

## tr055-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

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

## tr055-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Maps)
- task: Share location with family (Android (Google Maps)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid

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

## tr059-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

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

## tr059-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Delete an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleplay/answer/13627402?hl=en ; https://support.google.com/android/answer/7431795?hl=en ; https://support.google.com/googleplay/answer/13627571?hl=en

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

If the program can't be uninstalled here, type **Control Panel** in the search box on the taskbar and open it. Click **Programs**, then **Programs and Features**. Right-click the program, choose **Uninstall** or **Uninstall/Change**, and follow the directions on the screen.

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
5. Click **More** next to it, then click **Uninstall**.
6. Follow any directions that appear on the screen.

If the program can't be uninstalled here, type **Control Panel** in the search box on the taskbar and open it. Click **Programs**, then **Programs and Features**. Right-click the program, choose **Uninstall** or **Uninstall/Change**, and follow the directions on the screen.

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
5. Tap an app's name. In the detailed view, you can offload the app or delete the app. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.

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
5. Tap an app's name. In the detailed view, you can offload the app or delete the app. Offloading frees up space but keeps the app's documents and data. Deleting removes the app and its related data.
