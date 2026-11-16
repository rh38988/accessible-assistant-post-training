# Rule scan input, part 06 (50 examples)

## tr061-e
- task: Free up storage space | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

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

---

## tr061-r
- task: Free up storage space | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to check the storage on your iPhone and iPad <https://support.apple.com/en-us/108429>

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

---

## tr062-a
- task: Free up storage space | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Free up storage on your Android device <https://support.google.com/android/answer/7431795?hl=en>

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

---

## tr062-b
- task: Free up storage space | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Free up storage on your Android device <https://support.google.com/android/answer/7431795?hl=en>

**USER:**
phone says storage full

**ASSISTANT:**
I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?

---

## tr062-e
- task: Free up storage space | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Free up storage on your Android device <https://support.google.com/android/answer/7431795?hl=en>

**USER:**
My phone keeps saying storage is almost full. All my pictures are already backed up in Google Photos, and I would rather not dig through folders by hand every few weeks. Can the phone clear things out on its own?

**ASSISTANT:**
Yes, Android has a setting for that. It clears photos and videos that are already backed up when your storage is almost full.

1. Open the **Settings** app.
2. Tap **Storage**, then tap **Free up space**.
3. Tap the **Menu** icon, then tap **Settings**.
4. Turn on **Smart Storage**.

Your backed-up pictures still show in the **Google Photos** app when you are online. Some of these steps need Android 14 or newer, and menu names can differ a little between phones.

---

## tr063-a
- task: Turn on the flashlight | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro <https://support.apple.com/en-us/105001>

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

---

## tr063-r
- task: Turn on the flashlight | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro <https://support.apple.com/en-us/105001>

**USER:**
iPhone SE here, the one with the round button at the bottom. How can I turn on the light on the back?

**ASSISTANT:**
Here is the quickest way.

1. **Swipe up from the bottom edge** of the screen to open Control Center.
2. Tap the **Flashlight** button.
3. Tap it again to turn it off.

**USER:**
I swiped up and the controls came up but I don't see a flashlight button anywhere.

**ASSISTANT:**
It may just need to be added to Control Center.

1. Open **Settings**.
2. Tap **Control Center**.
3. In the list of controls, tap **Flashlight**.
4. Swipe up from the bottom again and tap the **Flashlight** button.

---

## tr064-b
- task: Turn on the flashlight | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Change settings quickly on your Android phone <https://support.google.com/android/answer/9083864?hl=en>

**USER:**
where is the flashlight

**ASSISTANT:**
I can show you. Is your phone an **iPhone** or an **Android** phone?

---

## tr064-e
- task: Turn on the flashlight | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Change settings quickly on your Android phone <https://support.google.com/android/answer/9083864?hl=en>

**USER:**
I use the flashlight button every night to get to the bathroom. I do have it, but I have to swipe down twice to find it and my hands are stiff. Can I move it so one swipe is enough?

**ASSISTANT:**
Yes. The first swipe shows only the first few settings, so you can drag the flashlight up into that group.

1. **Swipe down** twice from the top of the screen.
2. Tap **Edit**.
3. Tap and **drag** the **Flashlight** button to the front of the list, among the first few.

After that, one swipe down should show it. Tap it to turn the light on, and tap it again to turn it off.

---

## tr064-r
- task: Turn on the flashlight | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Change settings quickly on your Android phone <https://support.google.com/android/answer/9083864?hl=en>

**USER:**
Pixel phone. Where do I tap to turn on the torch?

**ASSISTANT:**
Here is the quickest way.

1. **Swipe down** from the top of the screen to see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight** to turn it on. A dimmed icon means it is off.
3. Tap it again to turn it off.

**USER:**
I swiped down twice and there are lots of buttons but I don't see Flashlight.

**ASSISTANT:**
Let's check the list of buttons you can add.

1. With the buttons showing, tap **Edit**.
2. Scroll down to see all the settings you can add.
3. If you find **Flashlight**, tap **Add**.

If it is not in that list, tell me what you see there.

---

## tr066-a
- task: Set an alarm | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

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

---

## tr066-b
- task: Set an alarm | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

**USER:**
how do I set an alarm to wake me up

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr066-c
- task: Set an alarm | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

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

---

## tr066-d
- task: Set an alarm | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

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

---

## tr066-e
- task: Set an alarm | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

**USER:**
My iPhone stays on silent all day and I turn on Do Not Disturb at night. I have a flight at 8 so I need to be up at 5:45 AM. Will an alarm still wake me if the phone is silent like that?

**ASSISTANT:**
Yes. Silent mode and Do Not Disturb do not silence alarms, so you can leave both on.

1. Open the **Clock** app.
2. Tap the **Alarms** tab.
3. Tap the **Add** button.
4. Set the time to **5:45 AM**.
5. Tap **Done**.

The alarm's loudness follows the **Ringtone and Alerts** slider. To check it, open **Settings**, tap **Sounds & Haptics**, and drag the slider toward the louder end.

---

## tr066-r
- task: Set an alarm | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

**USER:**
Need my iPhone to wake me at 7:15 tomorrow, please walk me through it.

**ASSISTANT:**
Here is how to set it.

1. Open the **Clock** app.
2. Tap the **Alarms** tab.
3. Tap the **Add** button.
4. Set the time to **7:15 AM**.
5. Tap **Done**.

**USER:**
It went off this morning but it only buzzed. No sound at all.

**ASSISTANT:**
The alarm's sound is probably set to **None**. Let's pick a sound.

1. Open **Clock** and tap **Alarms**.
2. Tap **Edit** in the upper-left corner, then tap your alarm.
3. Tap **Sound** and choose a sound instead of **None**.
4. Tap **Save**.

---

## tr067-a
- task: Set an alarm | platform: Android (Clock) | scenario: direct | sensitive: False
- sources: Android Help: Set, cancel, or snooze alarms on your Android device <https://support.google.com/android/answer/2840926?hl=en>

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

---

## tr067-c
- task: Set an alarm | platform: Android (Clock) | scenario: missing_info | sensitive: False
- sources: Android Help: Set, cancel, or snooze alarms on your Android device <https://support.google.com/android/answer/2840926?hl=en>

**USER:**
alarm for 7

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr067-d
- task: Set an alarm | platform: Android (Clock) | scenario: followup | sensitive: False
- sources: Android Help: Set, cancel, or snooze alarms on your Android device <https://support.google.com/android/answer/2840926?hl=en>

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

---

## tr067-e
- task: Set an alarm | platform: Android (Clock) | scenario: constraint | sensitive: False
- sources: Android Help: Set, cancel, or snooze alarms on your Android device <https://support.google.com/android/answer/2840926?hl=en>

**USER:**
I work Monday to Friday and sleep in on weekends. I want an alarm on my Android phone for 7:00 in the morning, but it must not go off on Saturday or Sunday.

**ASSISTANT:**
You can set the alarm and then choose which days it repeats.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time to **7:00** and choose **AM**.
5. Tap **OK**.
6. Tap the alarm you just made.
7. Tap the days of the week you want it to repeat, **Monday through Friday**.

Leave Saturday and Sunday untapped so it stays quiet on weekends.

---

## tr067-r
- task: Set an alarm | platform: Android (Clock) | scenario: failure_recovery | sensitive: False
- sources: Android Help: Set, cancel, or snooze alarms on your Android device <https://support.google.com/android/answer/2840926?hl=en>

**USER:**
Android here. Could you show me how to put an alarm on for 7 in the morning?

**ASSISTANT:**
Here is how, in the **Clock** app.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time to **7:00** and choose **AM**.
5. Tap **OK**.

**USER:**
Thanks. I added a second one at 7:03 as a backup, but this morning only one of them rang.

**ASSISTANT:**
Alarms set within 5 minutes of each other can cancel one another. Move the backup so they are at least 5 minutes apart.

1. Open **Clock** and tap **Alarm**.
2. Tap the time of the second alarm.
3. Set it to **7:05** or later, then tap **OK**.

Or tap the second alarm and tap **Delete** to remove it.

---

## tr068-a
- task: Pair hearing aids or Bluetooth headphones | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Use Made for iPhone hearing devices <https://support.apple.com/en-us/108780>

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

---

## tr068-c
- task: Pair hearing aids or Bluetooth headphones | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Use Made for iPhone hearing devices <https://support.apple.com/en-us/108780>

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

---

## tr068-d
- task: Pair hearing aids or Bluetooth headphones | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Use Made for iPhone hearing devices <https://support.apple.com/en-us/108780>

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

---

## tr068-e
- task: Pair hearing aids or Bluetooth headphones | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Use Made for iPhone hearing devices <https://support.apple.com/en-us/108780>

**USER:**
My new hearing aids are the rechargeable kind. There is no battery door and no on and off switch, they just sit in a little charging case. I have an iPhone and want to connect them. How do I get them into pairing mode?

**ASSISTANT:**
For hearing aids with no switch, pairing mode means taking them out of the charger.

1. Make sure your iPhone has the latest software update.
2. Take both hearing aids **out of the charger**. Keep them close to your iPhone.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**, then tap **Hearing Devices**.
5. Tap **Pair MFi Hearing Device** and follow the instructions on the screen.
6. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name in **Hearing Devices**, then tap **Pair** when the Bluetooth requests appear.

---

## tr068-r
- task: Pair hearing aids or Bluetooth headphones | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Use Made for iPhone hearing devices <https://support.apple.com/en-us/108780>

**USER:**
My daughter got me hearing aids that work with iPhone. Where do I go on my iPhone to connect them?

**ASSISTANT:**
Here is how to pair them.

1. Put your hearing aids in **pairing mode**. Your hearing aid instructions say how. It might mean opening and closing the battery doors, turning them off and on, or taking them out of the charger.
2. Open **Settings** on your iPhone.
3. Tap **Accessibility**, then tap **Hearing Devices**.
4. Tap **Pair MFi Hearing Device**.
5. Select your hearing aids, then tap **Pair**.

**USER:**
I did all that and my hearing aids never show up on the screen.

**ASSISTANT:**
Let's try a few things.

1. Put the hearing aids back in pairing mode.
2. Restart your iPhone.
3. If they were paired with another Apple device, like an iPad, unpair them there first.
4. Try **Settings**, **Accessibility**, **Hearing Devices** again.

Also check that your hearing aids are the kind made to work with iPhone.

---

## tr069-a
- task: Pair Bluetooth headphones | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Find & set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604?hl=en>; Android Help: Fix Bluetooth problems on Android <https://support.google.com/android/answer/9769184?hl=en>

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

---

## tr069-b
- task: Pair Bluetooth headphones | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Find & set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604?hl=en>

**USER:**
how do I connect my earbuds

**ASSISTANT:**
Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?

---

## tr069-c
- task: Pair Bluetooth headphones | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Find & set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604?hl=en>

**USER:**
bluetooth wont

**ASSISTANT:**
It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else?

---

## tr069-d
- task: Pair Bluetooth headphones | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Find & set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604?hl=en>; Android Help: Fix Bluetooth problems on Android <https://support.google.com/android/answer/9769184?hl=en>

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

---

## tr069-e
- task: Pair Bluetooth headphones | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Find & set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604?hl=en>

**USER:**
My headphones connected to my Android phone fine last month, then I used them with my tablet and now they won't play on the phone. I don't want to go through the whole setup again, I just want to reconnect the ones my phone already knows.

**ASSISTANT:**
You can reconnect them from your saved devices, with no new pairing.

1. **Pull down** from the top of the screen and make sure **Bluetooth** is on.
2. **Touch and hold** **Bluetooth**.
3. Under **Saved devices**, tap your headphones.
4. Wait until they show **Connected**.

Make sure the headphones are turned on and close to the phone.

---

## tr069-r
- task: Pair Bluetooth headphones | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Find & set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604?hl=en>

**USER:**
I bought wireless earbuds for my walks. My phone is an Android. How do I get them connected?

**ASSISTANT:**
Here is how to pair them.

1. Put the earbuds in **pairing mode**. Check the instructions that came with them.
2. **Pull down** from the top of the screen.
3. **Touch and hold** **Bluetooth**.
4. Tap **Pair new device**.
5. Tap the name of your earbuds.
6. Follow any instructions on the screen.

**USER:**
I touched and held Bluetooth but I don't see Pair new device anywhere.

**ASSISTANT:**
Try these:

1. Look under **Available devices** for your earbuds.
2. If they are not there, tap **More**, then tap **Refresh**.
3. Tap the name of your earbuds when it appears.

If you are asked for a passcode, try **0000** or **1234**.

---

## tr070-a
- task: Turn on battery saving mode | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad <https://support.apple.com/en-us/101604>

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

---

## tr070-b
- task: Turn on battery saving mode | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad <https://support.apple.com/en-us/101604>

**USER:**
how do I make my battery last longer today

**ASSISTANT:**
There's a battery-saving mode that can help. Is your phone an **iPhone** or an **Android** phone?

---

## tr070-d
- task: Turn on battery saving mode | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad <https://support.apple.com/en-us/101604>

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

---

## tr070-e
- task: Turn on battery saving mode | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad <https://support.apple.com/en-us/101604>

**USER:**
My hands are covered in dough and my iPhone is on the counter, at 15 percent. I don't want to touch it or go through menus. Can I turn on the battery saving thing by talking to it?

**ASSISTANT:**
Yes, Siri can do it.

1. Say **"Siri, turn on Low Power Mode."**
2. Look at the battery icon at the top of the screen once you can. When it turns **yellow**, Low Power Mode is on.

To turn it off later, say **"Hey Siri, turn off Low Power Mode."** It also turns off by itself once the battery charges to 80% or higher.

---

## tr070-r
- task: Turn on battery saving mode | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad <https://support.apple.com/en-us/101604>

**USER:**
iPhone 15. Walk me through turning on Low Power Mode please.

**ASSISTANT:**
Here is how.

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power Mode**.
4. Tap to turn **Low Power Mode** on.

The battery icon at the top of the screen turns yellow when it is on.

**USER:**
It worked, but after I charged my phone the yellow battery went away and it seems to be off.

**ASSISTANT:**
That is normal. Low Power Mode turns itself off once the battery charges to 80% or higher. To turn it back on:

1. Open **Settings** and tap **Battery**.
2. Tap **Power Mode**.
3. Tap to turn **Low Power Mode** on.

You will see the battery icon turn yellow again.

---

## tr071-a
- task: Turn on battery saving mode | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Get the most life from your Android device's battery <https://support.google.com/android/answer/7664692?hl=en>

**USER:**
How do I turn on Battery Saver on my Android phone?

**ASSISTANT:**
Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

---

## tr071-b
- task: Turn on battery saving mode | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Get the most life from your Android device's battery <https://support.google.com/android/answer/7664692?hl=en>

**USER:**
my phone battery won't last the day, can I make it last longer?

**ASSISTANT:**
Yes, a battery-saving mode can help. Is your phone an **iPhone** or an **Android** phone?

---

## tr071-c
- task: Turn on battery saving mode | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Get the most life from your Android device's battery <https://support.google.com/android/answer/7664692?hl=en>

**USER:**
Galaxy S23, battery at 40%, I need it until 10pm tonight. I'd like to turn on whatever the power saving setting is.

**ASSISTANT:**
Here's how. Menu names on Samsung phones can differ a little, and it takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.

---

## tr071-d
- task: Turn on battery saving mode | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Get the most life from your Android device's battery <https://support.google.com/android/answer/7664692?hl=en>

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

---

## tr071-e
- task: Turn on battery saving mode | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Get the most life from your Android device's battery <https://support.google.com/android/answer/7664692?hl=en>

**USER:**
I don't want my Android phone stuck in battery saving mode all day because it slows everything down. I only need it in the evenings when I'm out. Can it switch on and off by itself on a timetable?

**ASSISTANT:**
Yes, Battery Saver lets you choose a schedule, or have it turn off automatically.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**.
4. Look for the option to set a schedule or to turn it off automatically, and choose what fits you.

The choices can look a little different on some phones.

While it is on, it switches the screen to a dark theme and limits background activity, so some apps may be a little slower.

---

## tr071-r
- task: Turn on battery saving mode | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Get the most life from your Android device's battery <https://support.google.com/android/answer/7664692?hl=en>

**USER:**
Android phone and the battery never lasts. Is there a power saving mode I can switch on?

**ASSISTANT:**
Yes. Here is how to turn on Battery Saver.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver** and turn it on.

It limits background activity and turns on a dark theme.

**USER:**
I did that days ago and the battery still drains really fast.

**ASSISTANT:**
Let's try the usual fixes for battery trouble.

1. **Restart** the phone. Hold the power button for about 30 seconds, then tap **Restart** if it appears.
2. Check for an Android update: **Settings**, then **System**, then **Software update**.
3. Open the **Play Store**, tap your **profile icon**, tap **Manage apps & devices**, and update apps under **Updates available**.

If it still drains fast, your phone maker or carrier can help.

---

## tr072-a
- task: Update apps | platform: iPhone (App Store) | scenario: direct | sensitive: False
- sources: Apple Support: How to manually update apps from the App Store <https://support.apple.com/en-us/102629>

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

---

## tr072-b
- task: Update apps | platform: iPhone (App Store) | scenario: missing_info | sensitive: False
- sources: Apple Support: How to manually update apps from the App Store <https://support.apple.com/en-us/102629>

**USER:**
my banking app says I need to update it

**ASSISTANT:**
Updating the app is usually quick. Is your phone an **iPhone** or an **Android** phone?

---

## tr072-c
- task: Update apps | platform: iPhone (App Store) | scenario: missing_info | sensitive: False
- sources: Apple Support: How to manually update apps from the App Store <https://support.apple.com/en-us/102629>

**USER:**
update apps on

**ASSISTANT:**
It looks like your message got cut off. Which device do you want to update apps on: an **iPhone**, an **Android** phone, or a **computer**?

---

## tr072-d
- task: Update apps | platform: iPhone (App Store) | scenario: followup | sensitive: False
- sources: Apple Support: How to manually update apps from the App Store <https://support.apple.com/en-us/102629>

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

---

## tr072-e
- task: Update apps | platform: iPhone (App Store) | scenario: constraint | sensitive: False
- sources: Apple Support: How to manually update apps from the App Store <https://support.apple.com/en-us/102629>

**USER:**
Last week my iPhone changed how my banking app looks on its own and I got lost. I don't want apps changing behind my back anymore. How do I stop them updating by themselves? I will update them when I'm ready.

**ASSISTANT:**
You can turn off automatic updates.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **App Store**.
4. Turn off **App Updates**.

When you do want to update, open the **App Store**, tap your **profile photo** at the top of the screen, tap **App Updates**, then tap **Update** next to the app you want, or **Update All**.

---

## tr072-r
- task: Update apps | platform: iPhone (App Store) | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to manually update apps from the App Store <https://support.apple.com/en-us/102629>

**USER:**
My iPhone apps are out of date. Could you take me through updating them?

**ASSISTANT:**
Here is how to update them.

1. Open the **App Store**.
2. Tap your **profile photo** at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update** next to an app, or tap **Update All**.

**USER:**
I opened the App Store but I don't have a profile photo up top, just a plain icon.

**ASSISTANT:**
At the top of the screen the button can also be called **My Account**.

1. Tap the **My Account** button.
2. Tap **App Updates**.
3. Tap **Update** next to an app, or tap **Update All**.

---

## tr073-a
- task: Zoom in on the screen | platform: Android | scenario: direct | sensitive: False
- sources: Android Accessibility Help: Use magnification on your screen <https://support.google.com/accessibility/android/answer/6006949?hl=en>

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

---
