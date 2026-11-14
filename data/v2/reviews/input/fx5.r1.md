# Review input: batch fx5, round 1 (26 examples)

## tr062-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
My phone keeps saying storage is almost full. All my pictures are already backed up in Google Photos, and I would rather not dig through folders by hand every few weeks. Can the phone clear things out on its own?

**ASSISTANT:**
Yes, Android has a setting for that. It clears photos and videos that are already backed up when your storage is almost full.

1. Open the **Settings** app.
2. Tap **Storage**, then tap **Free up space**.
3. Tap the **Menu** icon, then tap **Settings**.
4. Turn on **Smart Storage**.

Your backed-up pictures still show in the **Google Photos** app when you are online. Some of these steps need Android 14 or newer, and menu names can differ a little between phones.

## tr062-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Free up storage space (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7431795?hl=en

**USER:**
Android phone, it's nearly full. I want to delete the big stuff I don't need. Where do I go?

**ASSISTANT:**
Here is how to find files to delete.

1. Open the **Settings** app.
2. Tap **Storage**, then tap **Free up space**.
3. Scroll to the category you want.
4. Tap **Select files**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**USER:**
I got to Free up space and found the category but there is no Select files button.

**ASSISTANT:**
That happens when a category is not listed the usual way. Try this instead:

1. Tap **Browse**.
2. Select the files you want to delete. You can also select all of them.
3. Tap **Move files to Trash**.

## tr063-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
I'm in my dark garage carrying two bags of groceries and my iPhone is in my pocket. I can't use my hands at all right now. Is there any way to get the light on without touching it?

**ASSISTANT:**
Yes, you can ask Siri without touching the phone.

1. Say **"Hey Siri, turn on my flashlight."**
2. When you are done, say **"Hey Siri, turn off my flashlight."**

## tr063-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

**USER:**
iPhone 11 here, the one with the round button at the bottom. How can I turn on the light on the back?

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
3. Add **Flashlight**.
4. Swipe up from the bottom again and tap the **Flashlight** button.

## tr064-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on the flashlight (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9083864?hl=en

**USER:**
I use the flashlight button every night to get to the bathroom. I do have it, but I have to swipe down twice to find it and my hands are stiff. Can I move it so one swipe is enough?

**ASSISTANT:**
Yes. The first swipe shows only the first few settings, so you can drag the flashlight up into that group.

1. **Swipe down** twice from the top of the screen.
2. Tap **Edit**.
3. Tap and **drag** the **Flashlight** button to the front of the list, among the first few.

After that, one swipe down should show it. Tap it to turn the light on, and tap it again to turn it off.

## tr064-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn on the flashlight (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9083864?hl=en

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

## tr066-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

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

## tr066-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Set an alarm (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118444

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

## tr067-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Clock)
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

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

## tr067-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Clock)
- task: Set an alarm (Android (Clock)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2840926?hl=en

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

## tr068-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

**USER:**
My new hearing aids are the rechargeable kind. There is no battery door and no on and off switch, they just sit in a little charging case. I have an iPhone and want to connect them. How do I get them into pairing mode?

**ASSISTANT:**
For hearing aids with no switch, pairing mode means taking them out of the charger.

1. Make sure your iPhone has the latest software update.
2. Take both hearing aids **out of the charger**.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**, then tap **Hearing Devices**.
5. Tap **Pair MFi Hearing Device** and follow the instructions on the screen.
6. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name in **Hearing Devices**, then tap **Pair** when the Bluetooth requests appear.

## tr068-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

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

## tr069-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

**USER:**
My headphones connected to my Android phone fine last month, then I used them with my tablet and now they won't play on the phone. I don't want to go through the whole setup again, I just want to reconnect the ones my phone already knows.

**ASSISTANT:**
You can reconnect them from your saved devices, with no new pairing.

1. **Pull down** from the top of the screen and make sure **Bluetooth** is on.
2. **Touch and hold** **Bluetooth**.
3. Under **Saved devices**, tap your headphones.
4. Wait until they show **Connected**.

Make sure the headphones are turned on and close to the phone.

## tr069-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Pair Bluetooth headphones (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604?hl=en

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

## tr070-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn on battery saving mode (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101604

**USER:**
My hands are covered in dough and my iPhone is on the counter, at 15 percent. I don't want to touch it or go through menus. Can I turn on the battery saving thing by talking to it?

**ASSISTANT:**
Yes, Siri can do it.

1. Say **"Siri, turn on Low Power Mode."**
2. Look at the battery icon at the top of the screen once you can. When it turns **yellow**, Low Power Mode is on.

To turn it off later, say **"Hey Siri, turn off Low Power Mode."** It also turns off by itself once the battery charges to 80% or higher.

## tr070-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on battery saving mode (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101604

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

## tr071-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

**USER:**
I don't want my Android phone stuck in battery saving mode all day because it slows everything down. I only need it in the evenings when I'm out. Can it switch on and off by itself on a timetable?

**ASSISTANT:**
Yes, Battery Saver has a schedule.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**.
4. Choose a **Schedule** for when it should run. You can also set it to turn off automatically.

While it is on, it switches the screen to a dark theme and limits background activity, so some apps may be a little slower.

## tr071-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

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

## tr072-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone (App Store)
- task: Update apps (iPhone (App Store)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102629

**USER:**
Last week my iPhone changed how my banking app looks on its own and I got lost. I don't want apps changing behind my back anymore. How do I stop them updating by themselves? I will update them when I'm ready.

**ASSISTANT:**
You can turn off automatic updates.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **App Store**.
4. Turn off **App Updates**.

When you do want to update, open the **App Store**, tap your **profile photo** at the top of the screen, tap **App Updates**, then tap **Update** next to the app you want, or **Update All**.

## tr072-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone (App Store)
- task: Update apps (iPhone (App Store)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102629

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

## tr073-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
I only need a little magnifying glass over the small print, not the whole screen blown up, because then I lose my place. Can my Android phone zoom just a section of the screen?

**ASSISTANT:**
Yes, Android has a partial screen mode that zooms a small window.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Magnification**.
3. Tap **Magnification type** and choose **partial screen**.
4. Turn on **Magnification shortcut**, and pick **Accessibility button** if you are asked how to start it.
5. Tap the **Accessibility button**.
6. **Drag with two fingers** to move the zoom window, and **pinch** to change how much it zooms.

Some of these steps need Android 13 or later.

## tr073-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
Android phone. I want to zoom in to read small print and I like the idea of triple tapping the screen. How do I set that up?

**ASSISTANT:**
Here is how to set it up.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Magnification**.
3. Turn on **Magnification shortcut**.
4. Tap **Magnification shortcut** and choose **Triple-tap screen**.

To zoom, quickly tap the screen 3 times and hold. Use two fingers to pinch and to move around. Use the shortcut again to stop.

**USER:**
It zooms, but now my phone feels slow and my taps are delayed.

**ASSISTANT:**
The triple-tap shortcut can slow your phone, and single taps take slightly longer while zoom is on. Switch to a different shortcut:

1. Open **Settings**, then **Accessibility**, then **Magnification**.
2. Tap **Magnification shortcut**.
3. Choose **Accessibility button** or **Hold volume keys**.

## tr074-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
I lost my iPhone at the park. I don't own any other Apple things, no iPad, no Mac. I only have an old Windows laptop at home. Can I still look for my phone?

**ASSISTANT:**
Yes, you can use the laptop's web browser.

1. Go to **icloud.com/find**.
2. Sign in with your Apple Account.
3. Open the device list under **All Devices** and choose your iPhone.
4. From there, you can **play a sound**, **mark it as lost**, or erase it.

If you are asked for a verification code, select the **Find Devices** button instead. Marking it as lost locks it and can show a phone number and message. Only erase it as a last resort, because that cannot be undone.

Apple will never contact you to say your iPhone has been found, so do not share your passcode or codes with anyone who does.

## tr074-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
My iPhone is missing since this morning. My wife has an iPad. What should I do on it?

**ASSISTANT:**
Use the **Find My** app on her iPad.

1. Open the **Find My** app and sign in with your Apple Account.
2. Tap the **Devices** tab.
3. Select your iPhone.
4. Tap the **More** button, scroll down, and turn on **Lost Mode**.

You can also play a sound or look at the map from here.

**USER:**
It shows my phone as offline, no location at all.

**ASSISTANT:**
That means it is off or not on Wi-Fi or cellular. Until it reconnects, it won't show as online or in Lost Mode. You can set up Lost Mode now:

1. In **Find My**, select your iPhone.
2. Tap the **More** button, then scroll to the **Lost** section and turn on **Lost Mode**.
3. If prompted, add your contact information.
4. Tap **Activate**.

## tr075-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
I think I dropped my Android phone on the bus. I really don't want to wipe it, my photos aren't all saved. I just want it locked, with my number on the screen so an honest person can call me. What do I do?

**ASSISTANT:**
You can lock it and show your number without erasing anything.

1. On another Android phone or tablet, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in and select your lost phone.
3. Tap **Mark as lost**, then tap **Next**.
4. Add your contact info and a message.
5. Tap **Mark as lost** again.

Skip **Factory reset**, since that permanently deletes the data. This works if your phone is on and connected to mobile data or Wi-Fi.

## tr075-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
Lost my Android phone somewhere in the house. I have a laptop handy. How do I find it?

**ASSISTANT:**
Use Find Hub on your laptop.

1. Go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone.
4. If asked, enter the lock screen PIN.
5. Look at the map to see where it is.

From there you can tap **Play sound** to ring it at full volume.

**USER:**
The map shows a pin in my house but I walked there and still can't see the phone.

**ASSISTANT:**
The location can be off by a few meters, especially indoors. Try this:

1. Tap **Play sound**. It rings at full volume for 5 minutes, even on silent.
2. Walk toward the sound.
3. Once you are within 10 meters, tap **Find nearby**. A shape fills in as you get closer.
