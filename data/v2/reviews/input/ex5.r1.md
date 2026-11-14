# Review input: batch ex5, round 1 (52 examples)

## tr062-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
How do I free up storage space on my Android phone?

**ASSISTANT:**
Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**. You'll see which kinds of files use the most space.
3. Tap **Free up space**.
4. Choose a category, then tap **Select files**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.

## tr062-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
phone says storage full

**ASSISTANT:**
I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?

## tr062-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
how do i clear

**ASSISTANT:**
It looks like your message got cut off. What would you like to clear: **storage space** on your phone, your **notifications**, or something else?

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
Thanks. Samsung menus can look a little different, so tell me if something doesn't match.

Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**. You'll see which kinds of files use the most space.
3. Tap **Free up space**.
4. Choose a category, then tap **Select files**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.

## tr063-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
How do I turn on the flashlight on my iPhone?

**ASSISTANT:**
There are a few quick ways.

**From Control Center:**
1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.
2. Tap the **Flashlight** button.
3. Tap it again to turn it off.

**From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.

**With Siri:** say "Hey Siri, turn on my flashlight."

## tr063-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
how do I turn on the light on my phone

**ASSISTANT:**
Do you mean the **flashlight**? Sure. Is your phone an **iPhone** or an **Android** phone?

## tr063-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
I was trying to find my keys in my purse last night and my husband said use your phone light but I couldn't figure out how.

**ASSISTANT:**
Your phone has a flashlight, and it's handy for things like that.

**Is your phone an iPhone or an Android phone?** Then I'll show you the quickest way.

## tr063-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
how do I turn on the light on my phone

**ASSISTANT:**
Do you mean the **flashlight**? Sure. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Yes the flashlight. iPhone.

**ASSISTANT:**
Got it.

There are a few quick ways.

**From Control Center:**
1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.
2. Tap the **Flashlight** button.
3. Tap it again to turn it off.

**From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.

**With Siri:** say "Hey Siri, turn on my flashlight."

## tr064-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Turn on the flashlight (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9083864?hl=en

**USER:**
How do I turn on the flashlight on my Android phone?

**ASSISTANT:**
Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.

## tr064-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on the flashlight (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9083864?hl=en

**USER:**
where is the flashlight

**ASSISTANT:**
I can show you. Is your phone an **iPhone** or an **Android** phone?

## tr064-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on the flashlight (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9083864?hl=en

**USER:**
Samsung A15. I know it's somewhere in the pull-down menu but I only see Wi-Fi, Bluetooth, and a few others.

**ASSISTANT:**
You're in the right place. Swipe down a second time to see more, and if it's still not there, you can add it:

Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.

## tr064-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn on the flashlight (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9083864?hl=en

**USER:**
where is the flashlight

**ASSISTANT:**
I can show you. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.

## tr066-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
How do I set an alarm on my iPhone for 6:30 in the morning?

**ASSISTANT:**
Here's how. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarms** at the bottom.
3. Tap the **plus (+)** button.
4. Set the time to **6:30 AM**.
5. If you want it every day, tap **Repeat** and choose the days.
6. Tap **Save** (on some versions, **Done**).

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.

## tr066-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
how do I set an alarm to wake me up

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone, and what time would you like to wake up?

## tr066-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
I have a doctor's appointment early tomorrow and I'm worried I'll oversleep. I usually wake up on my own but I can't risk it. I need to be up at 6:30. I have an iPhone.

**ASSISTANT:**
Good idea to set one. Here's how to make sure you're up at 6:30:

Here's how. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarms** at the bottom.
3. Tap the **plus (+)** button.
4. Set the time to **6:30 AM**.
5. If you want it every day, tap **Repeat** and choose the days.
6. Tap **Save** (on some versions, **Done**).

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.

## tr066-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

**USER:**
how do I set an alarm to wake me up

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone, and what time would you like to wake up?

**USER:**
iPhone, 6:30 in the morning

**ASSISTANT:**
Got it. Here's how to set it for 6:30.

Here's how. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarms** at the bottom.
3. Tap the **plus (+)** button.
4. Set the time to **6:30 AM**.
5. If you want it every day, tap **Repeat** and choose the days.
6. Tap **Save** (on some versions, **Done**).

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.

## tr067-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Clock)
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

**USER:**
How do I set an alarm on my Android phone?

**ASSISTANT:**
Here's how, using the **Clock** app. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time. On a round clock face, drag the hand to the hour, then to the minutes. Choose **AM** or **PM**.
5. Tap **OK**.

Make sure your alarm volume isn't too low. Below about 30%, you might not hear it.

If you set more than one alarm, leave at least 5 minutes between them.

## tr067-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

**USER:**
need an alarm for tomorrow

**ASSISTANT:**
I can help you set one. Is your phone an **iPhone** or an **Android** phone?

## tr067-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

**USER:**
alarm for 7

**ASSISTANT:**
Sure. Do you mean **7 in the morning** or **7 in the evening**? And is your phone an iPhone or an Android phone?

## tr067-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Clock)
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

**USER:**
need an alarm for tomorrow

**ASSISTANT:**
I can help you set one. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

Here's how, using the **Clock** app. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time. On a round clock face, drag the hand to the hour, then to the minutes. Choose **AM** or **PM**.
5. Tap **OK**.

Make sure your alarm volume isn't too low. Below about 30%, you might not hear it.

If you set more than one alarm, leave at least 5 minutes between them.

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
6. Tap **Pair MFi Hearing Device** if you see it, or tap your hearing aids' name when it appears. Then tap **Pair**.

If you don't see them, put them back in pairing mode and try again. Your audiologist can also help.

## tr068-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

**USER:**
how do I connect my hearing aids to my phone

**ASSISTANT:**
I can help you pair them. Is your phone an **iPhone** or an **Android** phone?

## tr068-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

**USER:**
My audiologist set up my new hearing aids in the office but she said I could connect them to my iPhone so phone calls go straight into my ears. I forgot to ask her how.

**ASSISTANT:**
That's a great feature. Here's how to connect them:

Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** if you see it, or tap your hearing aids' name when it appears. Then tap **Pair**.

If you don't see them, put them back in pairing mode and try again. Your audiologist can also help.

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
6. Tap **Pair MFi Hearing Device** if you see it, or tap your hearing aids' name when it appears. Then tap **Pair**.

If you don't see them, put them back in pairing mode and try again. Your audiologist can also help.

## tr069-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

**USER:**
How do I connect my new Bluetooth headphones to my Android phone?

**ASSISTANT:**
Here's how. It takes a couple of minutes.

1. Put your headphones in **pairing mode**. Each brand does this differently, so check the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If your headphones don't appear, check under **Available devices**, or tap **More** and then **Refresh**.

If you're asked for a code and don't have one, try **0000** or **1234**.

## tr069-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

**USER:**
how do I connect my earbuds

**ASSISTANT:**
Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?

## tr069-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

**USER:**
bluetooth wont

**ASSISTANT:**
It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else? And is your phone an iPhone or an Android phone?

## tr069-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

**USER:**
how do I connect my earbuds

**ASSISTANT:**
Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?

**USER:**
My Android phone

**ASSISTANT:**
Thanks.

Here's how. It takes a couple of minutes.

1. Put your headphones in **pairing mode**. Each brand does this differently, so check the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If your headphones don't appear, check under **Available devices**, or tap **More** and then **Refresh**.

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

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once you charge above 80%.

## tr070-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on battery saving mode (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101604

**USER:**
how do I make my battery last longer today

**ASSISTANT:**
There's a battery-saving mode that can help. Is your phone an **iPhone** or an **Android** phone?

## tr070-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Turn on battery saving mode (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101604

**USER:**
We're going to a wedding tomorrow and it'll be a long day. My phone usually dies by dinner and I want to take pictures all night.

**ASSISTANT:**
A battery-saving mode can help it last longer.

**Is your phone an iPhone or an Android phone?** I'll show you how to turn it on.

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
3. On iPhone 15 and newer, tap **Power Mode**, then **Low Power Mode**. On older iPhones, turn on **Low Power Mode**.

You'll know it's on when the battery icon at the top of the screen turns **yellow**.

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once you charge above 80%.

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
3. Tap **Battery Saver** and turn it on.

You can also set it to turn on by itself on a schedule.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

## tr071-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

**USER:**
my phone battery won't last the day, can I make it last longer?

**ASSISTANT:**
Yes, a battery-saving mode can help. Is your phone an **iPhone** or an **Android** phone?

## tr071-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

**USER:**
Galaxy S23, battery at 40%, I need it until 10pm tonight. I'd like to turn on whatever the power saving setting is.

**ASSISTANT:**
Here's how to turn it on. Menu names on Samsung phones can differ a little:

Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver** and turn it on.

You can also set it to turn on by itself on a schedule.

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
3. Tap **Battery Saver** and turn it on.

You can also set it to turn on by itself on a schedule.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

## tr072-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone (App Store)
- task: Update apps (iPhone (App Store)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102629

**USER:**
How do I update the apps on my iPhone?

**ASSISTANT:**
Here's how to update them all at once. It takes a few minutes.

1. Open the **App Store**.
2. Tap your **profile picture** (or the account icon) at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update All**, or tap **Update** next to just one app.

**To have apps update by themselves:**
1. Open **Settings**.
2. Tap **Apps**, then **App Store**.
3. Turn on **App Updates**.

## tr072-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Update apps (iPhone (App Store)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102629

**USER:**
my banking app says I need to update it

**ASSISTANT:**
Updating the app is usually quick. Is your phone an **iPhone** or an **Android** phone?

## tr072-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Update apps (iPhone (App Store)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102629

**USER:**
update apps on

**ASSISTANT:**
It looks like your message got cut off. Which device do you want to update apps on: an **iPhone**, an **Android** phone, or a **computer**?

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
Thanks. Open the App Store from your Home Screen, not from a link in a message, then:

Here's how to update them all at once. It takes a few minutes.

1. Open the **App Store**.
2. Tap your **profile picture** (or the account icon) at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update All**, or tap **Update** next to just one app.

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
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. **Pinch** with two fingers to zoom in or out.
3. **Drag with two fingers** to move around.
4. Use the shortcut again to stop.

It can zoom up to 8 times.

## tr073-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
can I zoom in on my phone screen

**ASSISTANT:**
Yes, most phones can. Is yours an **iPhone** or an **Android** phone?

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
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. **Pinch** with two fingers to zoom in or out.
3. **Drag with two fingers** to move around.
4. Use the shortcut again to stop.

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
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. **Pinch** with two fingers to zoom in or out.
3. **Drag with two fingers** to move around.
4. Use the shortcut again to stop.

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

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account.
2. Select your iPhone under **All Devices**.

From there you can **play a sound** to help find it nearby, or turn on **Lost Mode**. Lost Mode locks your phone and shows a message with a number where you can be reached.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.

## tr074-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I lost my phone

**ASSISTANT:**
I'm sorry, that's stressful. Let's try to find it. Is your phone an **iPhone** or an **Android** phone? And do you have another device or a computer you can use right now?

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

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account.
2. Select your iPhone under **All Devices**.

From there you can **play a sound** to help find it nearby, or turn on **Lost Mode**. Lost Mode locks your phone and shows a message with a number where you can be reached.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.

## tr074-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I lost my phone

**ASSISTANT:**
I'm sorry, that's stressful. Let's try to find it. Is your phone an **iPhone** or an **Android** phone? And do you have another device or a computer you can use right now?

**USER:**
iPhone. I'm on my laptop now.

**ASSISTANT:**
Good, your laptop will work.

Let's try to find it. You'll need another device or a computer.

**Option 1: another Apple device**
1. Open the **Find My** app and tap **Devices**.
2. Select your iPhone to see it on a map.
(A family member's iPhone also works if you're in the same Family Sharing group.)

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account.
2. Select your iPhone under **All Devices**.

From there you can **play a sound** to help find it nearby, or turn on **Lost Mode**. Lost Mode locks your phone and shows a message with a number where you can be reached.

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
3. Select your lost phone. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** locks your phone and lets you show a message and a contact number on the screen.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.

## tr075-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
can't find my phone anywhere

**ASSISTANT:**
Let's try to find it. Is it an **iPhone** or an **Android** phone? And do you have a computer or another phone you can use right now?

## tr075-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
lost phone help

**ASSISTANT:**
I'm sorry, let's try to find it. **Is it an iPhone or an Android phone**, and is there a computer or another phone you can use right now?

## tr075-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
can't find my phone anywhere

**ASSISTANT:**
Let's try to find it. Is it an **iPhone** or an **Android** phone? And do you have a computer or another phone you can use right now?

**USER:**
Android. I can use my husband's phone.

**ASSISTANT:**
Good, your husband's phone will work.

You can look for it with **Find Hub** from another device. It works if your phone is on and connected to the internet.

1. On another Android phone, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** locks your phone and lets you show a message and a contact number on the screen.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.
