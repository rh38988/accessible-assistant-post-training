# Review input: batch ex5, round 2 (31 examples)

## tr062-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
How do I free up storage space on my Android phone?

**ASSISTANT:**
Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**.
3. Tap **Free up space**.
4. Scroll to a category, then tap **Select files**. If you don't see the category, tap **Browse**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.

## tr062-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
phone says storage full

**ASSISTANT:**
I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, Samsung

**ASSISTANT:**
Thanks. Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**.
3. Tap **Free up space**.
4. Scroll to a category, then tap **Select files**. If you don't see the category, tap **Browse**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.

## tr063-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
my phone is dark and I need some light, where is it

**ASSISTANT:**
I can help with the flashlight. Is your phone an **iPhone** or an **Android** phone?

## tr066-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
How do I set an alarm on my iPhone for 6:30 in the morning?

**ASSISTANT:**
Here's how. It takes about a minute.

1. Open the **Clock** app, then tap the **Alarms** tab.
2. Tap the **Add** button.
3. Set the time to **6:30 AM**.
4. Only if you want it to repeat, tap **Repeat** and choose the days.
5. Tap **Done**.

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.

## tr066-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
how do I set an alarm to wake me up

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

## tr066-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
I have a doctor's appointment early tomorrow and I'm worried I'll oversleep. I usually wake up on my own but I can't risk it. I need to be up at 6:30. I have an iPhone.

**ASSISTANT:**
Good idea to set one. Here's how to make sure you're up at 6:30.

1. Open the **Clock** app, then tap the **Alarms** tab.
2. Tap the **Add** button.
3. Set the time to **6:30 AM**.
4. Only if you want it to repeat, tap **Repeat** and choose the days.
5. Tap **Done**.

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.

## tr066-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
how do I set an alarm to wake me up

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. Here's how to set an alarm.

1. Open the **Clock** app, then tap the **Alarms** tab.
2. Tap the **Add** button.
3. Set the time you want to wake up.
4. Only if you want it to repeat, tap **Repeat** and choose the days.
5. Tap **Done**.

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.

## tr067-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

**USER:**
alarm for 7

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

## tr068-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

**USER:**
I just got new hearing aids that work with iPhone. How do I connect them?

**ASSISTANT:**
Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** and follow the steps on the screen.
7. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.

If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.

## tr068-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

**USER:**
My audiologist set up my new hearing aids in the office but she said I could connect them to my iPhone so phone calls go straight into my ears. I forgot to ask her how.

**ASSISTANT:**
That's a great feature. Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** and follow the steps on the screen.
7. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.

If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.

## tr068-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

**USER:**
how do I connect my hearing aids to my phone

**ASSISTANT:**
I can help you pair them. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks.

Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** and follow the steps on the screen.
7. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.

If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.

## tr069-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en ; https://support.google.com/android/answer/9769184?hl=en

**USER:**
How do I connect my new Bluetooth headphones to my Android phone?

**ASSISTANT:**
Here's how. It takes a couple of minutes.

1. Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.

If you're asked for a code and don't have one, try **0000** or **1234**.

## tr069-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

**USER:**
bluetooth wont

**ASSISTANT:**
It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else?

## tr069-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en ; https://support.google.com/android/answer/9769184?hl=en

**USER:**
how do I connect my earbuds

**ASSISTANT:**
Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?

**USER:**
My Android phone

**ASSISTANT:**
Thanks.

Here's how. It takes a couple of minutes.

1. Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.

If you're asked for a code and don't have one, try **0000** or **1234**.

## tr070-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn on battery saving mode (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101604

**USER:**
How do I turn on Low Power Mode on my iPhone? I'm going out and my battery is low.

**ASSISTANT:**
Here's how. It takes a few seconds.

**Quickest way:** swipe down from the top-right corner to open **Control Center**, then tap the **battery** icon.

**In Settings:**
1. Open **Settings**.
2. Tap **Battery**.
3. On iPhone 15 and newer, tap **Power Mode**, then **Low Power Mode**. On older iPhones, turn on **Low Power Mode**.

You'll know it's on when the battery icon at the top of the screen turns **yellow**.

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once the battery is charged to 80% or higher.

## tr070-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn on battery saving mode (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101604

**USER:**
how do I make my battery last longer today

**ASSISTANT:**
There's a battery-saving mode that can help. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone 14

**ASSISTANT:**
Thanks. On your iPhone, it's called Low Power Mode.

Here's how. It takes a few seconds.

**Quickest way:** swipe down from the top-right corner to open **Control Center**, then tap the **battery** icon.

**In Settings:**
1. Open **Settings**.
2. Tap **Battery**.
3. Turn on **Low Power Mode**.

You'll know it's on when the battery icon at the top of the screen turns **yellow**.

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once the battery is charged to 80% or higher.

## tr071-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

**USER:**
How do I turn on Battery Saver on my Android phone?

**ASSISTANT:**
Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

## tr071-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

**USER:**
Galaxy S23, battery at 40%, I need it until 10pm tonight. I'd like to turn on whatever the power saving setting is.

**ASSISTANT:**
Here's how. Menu names on Samsung phones can differ a little, and it takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

## tr071-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

**USER:**
my phone battery won't last the day, can I make it last longer?

**ASSISTANT:**
Yes, a battery-saving mode can help. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

## tr072-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (App Store)
- task: Update apps (iPhone (App Store)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102629

**USER:**
my banking app says I need to update it

**ASSISTANT:**
Updating the app is usually quick. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. Here's how to update your banking app.

1. Open the **App Store**.
2. Tap your **profile picture** (or the account icon) at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update** next to your banking app. If you want to update every app, tap **Update All** instead.

**To have apps update by themselves:**
1. Open **Settings**.
2. Tap **Apps**, then **App Store**.
3. Turn on **App Updates**.

## tr073-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
Is there a way to zoom in on my Android phone's screen to read small things?

**ASSISTANT:**
Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing and holding both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. Tap anywhere on the screen, except the keyboard or the navigation bar.
3. **Pinch** with two fingers to zoom in or out.
4. **Drag with two fingers** to move around.
5. Use the shortcut again to stop.

It can zoom up to 8 times.

## tr073-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
The print on my medicine reminder app is so tiny, and making the text bigger messes up how the app looks. My Android phone is a Pixel.

**ASSISTANT:**
Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time.

Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing and holding both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. Tap anywhere on the screen, except the keyboard or the navigation bar.
3. **Pinch** with two fingers to zoom in or out.
4. **Drag with two fingers** to move around.
5. Use the shortcut again to stop.

It can zoom up to 8 times.

## tr073-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
can I zoom in on my phone screen

**ASSISTANT:**
Yes, most phones can. Is yours an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing and holding both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. Tap anywhere on the screen, except the keyboard or the navigation bar.
3. **Pinch** with two fingers to zoom in or out.
4. **Drag with two fingers** to move around.
5. Use the shortcut again to stop.

It can zoom up to 8 times.

## tr074-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I can't find my iPhone. I think I left it at a restaurant. How do I find it?

**ASSISTANT:**
Let's try to find it. You'll need another device or a computer.

**Option 1: another Apple device**
1. Open the **Find My** app and tap **Devices**.
2. Select your iPhone to see it on a map.
(A family member's iPhone also works if you're in the same Family Sharing group.)
3. To protect it, tap **More**.
4. Scroll down and turn on **Lost Mode**.
5. Follow the steps on the screen to add a phone number and a message.
6. Tap **Activate**.

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account. If you're asked for a verification code, select **Find Devices** instead.
2. Select your iPhone under **All Devices**.
3. Choose to play a sound to help find it nearby, or mark it as lost.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.

## tr074-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I lost my phone

**ASSISTANT:**
I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?

## tr074-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I left the grocery store and when I got home my iPhone wasn't in my bag. My husband has an iPhone too. I'm panicking a little.

**ASSISTANT:**
Take a breath. There's a good chance you can find it, and your husband's iPhone may help if you're both in the same Family Sharing group.

Let's try to find it. You'll need another device or a computer.

**Option 1: another Apple device**
1. Open the **Find My** app and tap **Devices**.
2. Select your iPhone to see it on a map.
(A family member's iPhone also works if you're in the same Family Sharing group.)
3. To protect it, tap **More**.
4. Scroll down and turn on **Lost Mode**.
5. Follow the steps on the screen to add a phone number and a message.
6. Tap **Activate**.

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account. If you're asked for a verification code, select **Find Devices** instead.
2. Select your iPhone under **All Devices**.
3. Choose to play a sound to help find it nearby, or mark it as lost.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.

## tr074-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I lost my phone

**ASSISTANT:**
I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. I'm on my laptop now.

**ASSISTANT:**
Good, your laptop will work. Here's how to look for your iPhone.

1. Go to **icloud.com/find** and sign in with your Apple Account. If you're asked for a verification code, select **Find Devices** instead.
2. Select your iPhone under **All Devices**.
3. Choose to play a sound to help find it nearby, or mark it as lost.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.

## tr075-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
I lost my Android phone. How can I find it?

**ASSISTANT:**
You can look for it with **Find Hub** from another device. It works if your phone is on and connected to the internet.

1. On another Android phone, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. If asked, enter your lock screen PIN or password. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** tap **Mark as lost**, then **Next**. Add a message and a phone number, then tap **Mark as lost** again to confirm.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.

## tr075-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
can't find my phone anywhere

**ASSISTANT:**
Let's try to find it. Is it an **iPhone** or an **Android** phone?

## tr075-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
lost phone help

**ASSISTANT:**
I'm sorry, let's try to find it. Is it an **iPhone** or an **Android** phone?

## tr075-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
can't find my phone anywhere

**ASSISTANT:**
Let's try to find it. Is it an **iPhone** or an **Android** phone?

**USER:**
Android. I can use my husband's phone.

**ASSISTANT:**
Good, your husband's phone will work.

You can look for it with **Find Hub** from another device. It works if your phone is on and connected to the internet.

1. On another Android phone, open the **Find Hub** app. If your husband's phone isn't an Android phone, open a web browser on it and go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. If asked, enter your lock screen PIN or password. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** tap **Mark as lost**, then **Next**. Add a message and a phone number, then tap **Mark as lost** again to confirm.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.
