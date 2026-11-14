# Review input: batch ny3b, round 1 (36 examples)

## tr154-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
How do I connect my new wireless earbuds to my Pixel phone?

**ASSISTANT:**
Here is how to pair your earbuds with your phone:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your earbuds in the list.
5. Follow the on-screen prompts.

When it works, the earbuds show as **Connected**.

If you don't see **Pair new device**, look under **Available devices**, or tap the **More** icon and then **Refresh**.

## tr154-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
My daughter gave me a little Bluetooth speaker for my birthday and I have never used Bluetooth before. I have an Android phone. I got as far as seeing the speaker on my phone but now it wants some kind of passcode and I have no idea what to type. Can you walk me through the whole thing?

**ASSISTANT:**
Happy birthday! Here is the whole thing:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your speaker.
5. Follow the on-screen prompts.

If it asks for a passcode and you don't have one, try **0000**. If that does not work, try **1234**.

When it works, the speaker shows as **Connected**.

## tr154-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
I just bought something that connects to my phone with Bluetooth. How do I set it up?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr154-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
I just bought something that connects to my phone with Bluetooth. How do I set it up?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
It's an Android, a Pixel.

**ASSISTANT:**
Thanks. Here is how to pair your Bluetooth device with your Pixel:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your device.
5. Follow the on-screen prompts.

When it works, the device shows as **Connected**.

If you don't see **Pair new device**, look under **Available devices**, or tap the **More** icon and then **Refresh**.

## tr154-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
I want to connect a Bluetooth keyboard to my Android phone so typing is easier on my eyes. I don't want to go hunting through lots of menus, my eyes get tired. Is there a quick way to start from the top of the screen?

**ASSISTANT:**
Yes, you can start right from the top of the screen:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your keyboard.
5. Follow the on-screen prompts.

When it works, the keyboard shows as **Connected**.

If the **Bluetooth** icon is off, tap it once to turn Bluetooth on. Bluetooth stays off while Airplane mode is on, so turn that off first.

## tr154-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
How do I pair my Bluetooth headphones with my Android phone?

**ASSISTANT:**
Here is how to pair them:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your headphones.
5. Follow the on-screen prompts.

When it works, the headphones show as **Connected**.

**USER:**
I touched and held the Bluetooth icon but I can't find Pair new device anywhere.

**ASSISTANT:**
No problem. Try one of these:

1. Look under **Available devices** for your headphones.
2. Or tap the **More** icon, then tap **Refresh**.
3. When you see the name of your headphones, tap it and follow the on-screen prompts.

## tr155-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Make the screen brighter or dimmer (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/6111557

**USER:**
My Pixel phone screen is too dim. How do I make it brighter?

**ASSISTANT:**
Here is how to make the screen brighter:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to set the brightness you like.

If you don't see the brightness setting, tap **Advanced** on the **Display & touch** screen to see more settings.

## tr155-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Make the screen brighter or dimmer (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/6111557

**USER:**
I read a lot at night before bed on my Pixel phone and the screen is so bright it hurts my eyes and keeps my husband awake. I went into Settings and Display & touch but I do not see anything about brightness on that screen, just a bunch of other things. How do I make it dimmer?

**ASSISTANT:**
Let's get it dimmer. Since you are already in Settings:

1. On the **Display & touch** screen, tap **Advanced** to see more settings.
2. Tap **Brightness level**.
3. Move the slider toward the dimmer side.

## tr155-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make the screen brighter or dimmer (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/6111557

**USER:**
My phone screen is way too dark to see. Can you help?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr155-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Make the screen brighter or dimmer (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/6111557

**USER:**
My phone screen is way too dark to see. Can you help?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android. It's a Google Pixel.

**ASSISTANT:**
Thanks. Here is how to make the screen brighter on your Pixel:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to a brighter setting.

If you don't see the brightness setting, tap **Advanced** on the **Display & touch** screen to see more settings.

## tr155-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Make the screen brighter or dimmer (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/6111557

**USER:**
I have a Pixel 8 and I only want to change the brightness myself. I don't want to touch any other settings, and I would like the screen a bit dimmer for the evening. It also seems to change by itself sometimes, why is that?

**ASSISTANT:**
You only need one setting for this:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to make the screen dimmer.

The screen may change by itself because of **Adaptive brightness**. It is on by default and adjusts the screen to the light around you. You can still set the brightness yourself while it is on.

If you don't see the brightness setting, tap **Advanced** first.

## tr155-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Make the screen brighter or dimmer (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/6111557

**USER:**
How can I change the screen brightness on my Pixel phone?

**ASSISTANT:**
Here is how:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to the brightness you want.

**USER:**
I'm on the Display & touch screen but there is no Brightness level there.

**ASSISTANT:**
That can happen. Try this:

1. On the **Display & touch** screen, tap **Advanced** to see more settings.
2. Tap **Brightness level**.
3. Move the slider to the brightness you want.

## tr156-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Fix the wrong date or time (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2841106

**USER:**
The date and time on my Android phone is wrong. How do I fix it?

**ASSISTANT:**
Here is how to fix it:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Turn on **Automatic date and time**.

If your screen looks a little different, the names can vary a bit on some phones.

## tr156-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Fix the wrong date or time (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2841106

**USER:**
So I just flew back from visiting my sister and now my Android phone shows the wrong time, it is still on the old time zone, and I missed a doctor reminder because of it. The time is right when I look at my watch. I would like the phone to just fix the time zone on its own. What do I do?

**ASSISTANT:**
Let's make the phone fix its own time zone:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Under **Time zone**, turn on **Automatic time zone**.

If you don't see **Automatic time zone**, your phone may not support it. Only some devices do.

## tr156-b
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Fix the wrong date or time (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2841106

**USER:**
the clock on my phone is wrong

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr156-d
- scenario: followup | style: incomplete | specification: fully_specified | platform: Android
- task: Fix the wrong date or time (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2841106

**USER:**
the clock on my phone is wrong

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
android

**ASSISTANT:**
Thanks. Here is how to fix the time and date on your Android phone:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Turn on **Automatic date and time**.

Names can look a little different on some phones.

## tr156-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Fix the wrong date or time (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2841106

**USER:**
My Android phone has the wrong time zone. I don't want the phone guessing anything for me, I want to pick my own time zone from the list. I'm in the Central time zone. Please don't tell me to turn on the automatic one.

**ASSISTANT:**
Understood. Here is how to choose it yourself:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Tap **Time zone**.
5. If you see **Set automatically**, turn it off.
6. Tap **Time zone** again.
7. Select your time zone from the list.

## tr156-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Fix the wrong date or time (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2841106

**USER:**
My Android phone shows the wrong time zone. How do I get it to fix itself?

**ASSISTANT:**
Here is how:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Under **Time zone**, turn on **Automatic time zone**.

**USER:**
There is no Automatic time zone on my phone. It's not there at all.

**ASSISTANT:**
That can happen, because only some phones support it. You can pick the time zone yourself:

1. Tap **Time zone**.
2. If you see **Set automatically**, turn it off.
3. Tap **Time zone** again and select your time zone.

## tr157-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Add and move apps on the Home screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9450271

**USER:**
How do I put the Gmail app on my Android home screen so I can open it faster?

**ASSISTANT:**
Here is how to add Gmail to your Home screen:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the Gmail app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

If it lands in the wrong place, just drag it again.

## tr157-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Add and move apps on the Home screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9450271

**USER:**
I have an Android phone and the camera app is way down in the corner where I always miss it. My grandson showed me once how to rearrange things but I forgot. I want to take the camera icon that is already on my home screen and put it right at the bottom in the middle. How?

**ASSISTANT:**
You can move it like this:

1. Touch and drag the camera app. Thumbnails of your Home screens appear.
2. Drag it to the spot you want.
3. Let go of it there.

If it lands in the wrong place, just drag it again.

Some of these steps only work on Android 14 and newer.

## tr157-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Add and move apps on the Home screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9450271

**USER:**
I want my favorite app on the main screen of my phone. How?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr157-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Add and move apps on the Home screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9450271

**USER:**
I want my favorite app on the main screen of my phone. How?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks. Here is how to add an app to the Home screen on your Android phone:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag your favorite app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

If it lands in the wrong place, just drag it again.

## tr157-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Add and move apps on the Home screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9450271

**USER:**
I'm scared of deleting something by accident on my Android phone. I only want to add the weather app to my home screen and I do not want to uninstall or lose anything. Can you tell me what to do and what to stay away from?

**ASSISTANT:**
Adding an app does not delete anything. Here is how to add the weather app:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the weather app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

Stay away from **Remove** and **Uninstall**. They show up when you touch and hold an app and drag it up. **Remove** only takes an app off the Home screen. **Uninstall** takes it off your phone.

## tr157-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Add and move apps on the Home screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9450271

**USER:**
How do I add the Photos app to the home screen on my Android phone?

**ASSISTANT:**
Here is how:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the Photos app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

**USER:**
I did it but it landed in the wrong spot, not where I wanted.

**ASSISTANT:**
That is easy to fix. Just move it again:

1. Touch and drag the app. Thumbnails of your Home screens appear.
2. Drag it to the new spot you want.
3. Let go of it there.

## tr158-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
I heard my Android phone can lock itself if someone grabs it out of my hand and runs. How do I turn that on?

**ASSISTANT:**
That is the **Theft Detection Lock** setting. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Theft Detection Lock**.

Once it is on, the screen locks automatically if the phone is taken from you.

Set a screen lock first, because the setting won't turn on without one. If it is grayed out, your phone doesn't support it.

## tr158-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
My neighbor's phone got snatched on the bus and the thief switched off the internet right away so she could not do anything. I have an Android phone and I want mine to lock itself if that ever happens to me, even with no internet. Is there a setting for that?

**ASSISTANT:**
Yes. It is called **Offline Device Lock**. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Offline Device Lock**.

Once it is on, the screen locks after the phone has been used offline for a short time. Your phone must be unlocked when it loses its internet connection.

Set a screen lock first, because the setting won't turn on without one.

## tr158-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
I want to make my phone safer in case somebody steals it. What should I turn on?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr158-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
I want to make my phone safer in case somebody steals it. What should I turn on?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android phone

**ASSISTANT:**
Thanks. A good setting to start with is **Theft Detection Lock**:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Theft Detection Lock**.

Once it is on, the screen locks automatically if the phone is taken from you.

Set a screen lock first, because the setting won't turn on without one.

## tr158-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
I don't want to count on my phone guessing that it was grabbed. I want to be able to lock it myself from my laptop if it goes missing. My Android phone has a screen lock, a working SIM, and Find Hub is on. What do I set up?

**ASSISTANT:**
You want **Remote Lock**. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Tap **Remote Lock**.
6. Turn on **Remote lock**.

If it says your number isn't verified, tap **Verify number**, then turn on **Automatically verify phone numbers**.

To lock the phone later, go to android.com/lock on your laptop, enter your phone number, complete the reCAPTCHA, and request a lock.

## tr158-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
How do I turn on Theft Detection Lock on my Android phone?

**ASSISTANT:**
Here is how:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Theft Detection Lock**.

**USER:**
The Theft Detection Lock switch is gray and I can't turn it on.

**ASSISTANT:**
When it is grayed out, your phone doesn't support that setting. Support differs from phone to phone.

You can look at the same **Theft protection** screen for other protections your phone may offer, such as **Offline Device Lock**.

## tr159-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
My Android phone gets bad cell signal inside my house. Can I make phone calls over my Wi-Fi instead? How do I set that up?

**ASSISTANT:**
Yes, you can. Here is how to turn on Wi-Fi calling:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

After that, make calls the way you always do. When your phone is connected to the internet, the notification screen shows **Internet Call** or **Wi-Fi calling**.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.

## tr159-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
We live out in the country and the signal is terrible in our basement where my husband's workshop is. Our grandson says my Android phone can call using the internet but I am worried it will cost extra money on our bill. How do I turn it on and will it cost anything?

**ASSISTANT:**
Here is how to turn on Wi-Fi calling:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

About cost, Wi-Fi calling may come with extra charges, so check with your mobile provider before you use it.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.

## tr159-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
I have bad signal at home. Can I call people over my Wi-Fi instead?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr159-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
I have bad signal at home. Can I call people over my Wi-Fi instead?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
It's an Android.

**ASSISTANT:**
Yes, you can. Here is how to turn on Wi-Fi calling on your Android phone:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

After that, make calls the way you always do.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.

## tr159-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
I'm staying at my daughter's house for a while and I don't have a mobile service plan on my Android phone right now, just her Wi-Fi. Is there any way to still make phone calls with it?

**ASSISTANT:**
It may work. Some carriers let you use Wi-Fi calling without a mobile service plan. Here is how to check:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

Then make calls as you normally would while you are connected to her Wi-Fi.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.

## tr159-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
How do I turn on Wi-Fi calling on my Android phone?

**ASSISTANT:**
Here is how:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

**USER:**
I got to Carrier SIM but there is no Wi-Fi calling option on that screen.

**ASSISTANT:**
If **Wi-Fi calling** doesn't appear, your carrier doesn't support it. It is best to ask your carrier to confirm.
