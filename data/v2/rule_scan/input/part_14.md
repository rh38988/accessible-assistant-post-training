# Rule scan input, part 14 (50 examples)

## tr154-c
- task: Pair a Bluetooth accessory | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Find and set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604>

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

---

## tr154-d
- task: Pair a Bluetooth accessory | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Find and set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604>

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

---

## tr154-r
- task: Pair a Bluetooth accessory | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Find and set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604>

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

---

## tr155-a
- task: Make the screen brighter or dimmer | platform: Android | scenario: direct | sensitive: False
- sources: Pixel Phone Help: Change screen brightness <https://support.google.com/pixelphone/answer/6111557>

**USER:**
My Pixel phone screen is too dim. How do I make it brighter?

**ASSISTANT:**
Here is how to make the screen brighter:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to set the brightness you like.

If you don't see the brightness setting, tap **Advanced** on the **Display & touch** screen to see more settings.

---

## tr155-b
- task: Make the screen brighter or dimmer | platform: Android | scenario: missing_info | sensitive: False
- sources: Pixel Phone Help: Change screen brightness <https://support.google.com/pixelphone/answer/6111557>

**USER:**
My phone screen is way too dark to see. Can you help?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr155-c
- task: Make the screen brighter or dimmer | platform: Android | scenario: direct_messy | sensitive: False
- sources: Pixel Phone Help: Change screen brightness <https://support.google.com/pixelphone/answer/6111557>

**USER:**
I read a lot at night before bed on my Pixel phone and the screen is so bright it hurts my eyes and keeps my husband awake. I went into Settings and Display & touch but I do not see anything about brightness on that screen, just a bunch of other things. How do I make it dimmer?

**ASSISTANT:**
Let's get it dimmer. Since you are already in Settings:

1. On the **Display & touch** screen, tap **Advanced** to see more settings.
2. Tap **Brightness level**.
3. Move the slider toward the dimmer side.

---

## tr155-d
- task: Make the screen brighter or dimmer | platform: Android | scenario: followup | sensitive: False
- sources: Pixel Phone Help: Change screen brightness <https://support.google.com/pixelphone/answer/6111557>

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

---

## tr155-e
- task: Make the screen brighter or dimmer | platform: Android | scenario: constraint | sensitive: False
- sources: Pixel Phone Help: Change screen brightness <https://support.google.com/pixelphone/answer/6111557>

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

---

## tr155-r
- task: Make the screen brighter or dimmer | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Pixel Phone Help: Change screen brightness <https://support.google.com/pixelphone/answer/6111557>

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

---

## tr156-a
- task: Fix the wrong date or time | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Set time, date and time zone <https://support.google.com/android/answer/2841106>

**USER:**
The date and time on my Android phone is wrong. How do I fix it?

**ASSISTANT:**
Here is how to fix it:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Turn on **Automatic date and time**.

If your screen looks a little different, the names can vary a bit on some phones.

---

## tr156-c
- task: Fix the wrong date or time | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Set time, date and time zone <https://support.google.com/android/answer/2841106>

**USER:**
So I just flew back from visiting my sister and now my Android phone shows the wrong time, it is still on the old time zone, and I missed a doctor reminder because of it. The time is right when I look at my watch. I would like the phone to just fix the time zone on its own. What do I do?

**ASSISTANT:**
Let's make the phone fix its own time zone:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Under **Time zone**, turn on **Automatic time zone**.

If you don't see **Automatic time zone**, your phone may not support it. Only some devices do.

---

## tr156-d
- task: Fix the wrong date or time | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Set time, date and time zone <https://support.google.com/android/answer/2841106>

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

---

## tr156-e
- task: Fix the wrong date or time | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Set time, date and time zone <https://support.google.com/android/answer/2841106>

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

---

## tr156-r
- task: Fix the wrong date or time | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Set time, date and time zone <https://support.google.com/android/answer/2841106>

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

---

## tr157-a
- task: Add and move apps on the Home screen | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Add apps, shortcuts & widgets to your Home screens <https://support.google.com/android/answer/9450271>

**USER:**
How do I put the Gmail app on my Android home screen so I can open it faster?

**ASSISTANT:**
Here is how to add Gmail to your Home screen:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the Gmail app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

If it lands in the wrong place, just drag it again.

---

## tr157-b
- task: Add and move apps on the Home screen | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Add apps, shortcuts & widgets to your Home screens <https://support.google.com/android/answer/9450271>

**USER:**
I want my favorite app on the main screen of my phone. How?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr157-c
- task: Add and move apps on the Home screen | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Add apps, shortcuts & widgets to your Home screens <https://support.google.com/android/answer/9450271>

**USER:**
I have an Android phone and the camera app is way down in the corner where I always miss it. My grandson showed me once how to rearrange things but I forgot. I want to take the camera icon that is already on my home screen and put it right at the bottom in the middle. How?

**ASSISTANT:**
You can move it like this:

1. Touch and drag the camera app. Thumbnails of your Home screens appear.
2. Drag it to the spot you want.
3. Let go of it there.

If it lands in the wrong place, just drag it again.

Some of these steps only work on Android 14 and newer.

---

## tr157-d
- task: Add and move apps on the Home screen | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Add apps, shortcuts & widgets to your Home screens <https://support.google.com/android/answer/9450271>

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

---

## tr157-e
- task: Add and move apps on the Home screen | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Add apps, shortcuts & widgets to your Home screens <https://support.google.com/android/answer/9450271>

**USER:**
I'm scared of deleting something by accident on my Android phone. I only want to add the weather app to my home screen and I do not want to uninstall or lose anything. Can you tell me what to do and what to stay away from?

**ASSISTANT:**
Adding an app does not delete anything. Here is how to add the weather app:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the weather app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

Stay away from **Remove** and **Uninstall**. They show up when you touch and hold an app and drag it up. **Remove** only takes an app off the Home screen. **Uninstall** takes it off your phone.

---

## tr157-r
- task: Add and move apps on the Home screen | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Add apps, shortcuts & widgets to your Home screens <https://support.google.com/android/answer/9450271>

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

---

## tr158-a
- task: Turn on theft protection | platform: Android | scenario: direct | sensitive: True
- sources: Android Help: Protect your personal data against theft <https://support.google.com/android/answer/15146908>

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

---

## tr158-c
- task: Turn on theft protection | platform: Android | scenario: direct_messy | sensitive: True
- sources: Android Help: Protect your personal data against theft <https://support.google.com/android/answer/15146908>

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

---

## tr158-d
- task: Turn on theft protection | platform: Android | scenario: followup | sensitive: True
- sources: Android Help: Protect your personal data against theft <https://support.google.com/android/answer/15146908>

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

---

## tr158-e
- task: Turn on theft protection | platform: Android | scenario: constraint | sensitive: True
- sources: Android Help: Protect your personal data against theft <https://support.google.com/android/answer/15146908>

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

To lock the phone later, use your laptop:

1. Go to android.com/lock.
2. Enter your phone number.
3. Complete the security check (reCaptcha) that appears.
4. Request the lock.

The phone screen locks shortly after.

---

## tr158-r
- task: Turn on theft protection | platform: Android | scenario: failure_recovery | sensitive: True
- sources: Android Help: Protect your personal data against theft <https://support.google.com/android/answer/15146908>

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

---

## tr159-a
- task: Make calls over Wi-Fi | platform: Android | scenario: direct | sensitive: False
- sources: Phone app Help: Make calls over Wi-Fi <https://support.google.com/phoneapp/answer/2811843>

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

---

## tr159-b
- task: Make calls over Wi-Fi | platform: Android | scenario: missing_info | sensitive: False
- sources: Phone app Help: Make calls over Wi-Fi <https://support.google.com/phoneapp/answer/2811843>

**USER:**
I have bad signal at home. Can I call people over my Wi-Fi instead?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr159-c
- task: Make calls over Wi-Fi | platform: Android | scenario: direct_messy | sensitive: False
- sources: Phone app Help: Make calls over Wi-Fi <https://support.google.com/phoneapp/answer/2811843>

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

---

## tr159-d
- task: Make calls over Wi-Fi | platform: Android | scenario: followup | sensitive: False
- sources: Phone app Help: Make calls over Wi-Fi <https://support.google.com/phoneapp/answer/2811843>

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

---

## tr159-r
- task: Make calls over Wi-Fi | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Phone app Help: Make calls over Wi-Fi <https://support.google.com/phoneapp/answer/2811843>

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

---

## tr160-a
- task: Take a screenshot | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung US Support: How to take a screenshot on a Samsung phone or tablet <https://www.samsung.com/us/support/answer/ANS10002500/>

**USER:**
How do I take a screenshot on my Samsung Galaxy phone?

**ASSISTANT:**
You can capture your screen with two buttons. Here is how.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

If nothing happens, check where the buttons are on your model, since their position can differ.

---

## tr160-b
- task: Take a screenshot | platform: Samsung Galaxy | scenario: missing_info | sensitive: False
- sources: Samsung US Support: How to take a screenshot on a Samsung phone or tablet <https://www.samsung.com/us/support/answer/ANS10002500/>

**USER:**
I need to save what is on my screen as a picture. How do I do that?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

---

## tr160-c
- task: Take a screenshot | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung US Support: How to take a screenshot on a Samsung phone or tablet <https://www.samsung.com/us/support/answer/ANS10002500/>

**USER:**
My daughter sent me a long recipe on a website and I want to keep the whole thing as one picture, not a bunch of little pieces. I have a Samsung Galaxy phone. The recipe goes way past the bottom of the screen. Is there a way to get all of it?

**ASSISTANT:**
Yes, there is a way to capture a long page as one picture.

1. Open the recipe on your screen.
2. Press and hold the **Power** (side) button and the **Volume Down** button together, then let go. The screen flashes.
3. Tap the **Scroll capture** icon. It looks like two arrows pointing down.

Long content is then captured as one image.

---

## tr160-d
- task: Take a screenshot | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung US Support: How to take a screenshot on a Samsung phone or tablet <https://www.samsung.com/us/support/answer/ANS10002500/>

**USER:**
I need to save what is on my screen as a picture. How do I do that?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
It's a Samsung Galaxy.

**ASSISTANT:**
Thank you. On a Samsung Galaxy it takes two buttons.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

---

## tr160-e
- task: Take a screenshot | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung US Support: How to take a screenshot on a Samsung phone or tablet <https://www.samsung.com/us/support/answer/ANS10002500/>

**USER:**
I have a Samsung Galaxy and my hands have arthritis, so pressing two buttons at once is really hard for me. Is there another way to take a screenshot that does not use the buttons?

**ASSISTANT:**
Yes. You can turn on a swipe that captures the screen with the side of your hand.

1. Swipe down from the top right corner with two fingers to open the **Quick panel**.
2. Tap **Settings**, the gear icon.
3. Swipe to **Advanced features** and tap it.
4. Tap **Palm swipe to capture** and turn its switch on.

After that, swipe the edge of your hand across the screen to take a screenshot.

You can also say "Hey Google, take a screenshot" or "Hey Bixby, take a screenshot".

---

## tr160-r
- task: Take a screenshot | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung US Support: How to take a screenshot on a Samsung phone or tablet <https://www.samsung.com/us/support/answer/ANS10002500/>

**USER:**
Samsung Galaxy here. How can I take a picture of what is on my screen?

**ASSISTANT:**
You can do that with two buttons.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

**USER:**
The screen flashed, but now I can't find the picture anywhere.

**ASSISTANT:**
Good, that means it worked. You can find it in either of these places.

1. Open **Gallery**, tap the **Albums** tab, then tap the **Screenshots** folder.
2. Or open **My Files** and tap **Images**.

---

## tr161-a
- task: Update the phone's software | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung US Support: How to update your Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS10002027/>

**USER:**
How do I update the software on my Samsung Galaxy phone?

**ASSISTANT:**
You can do it right on the phone. Here is how.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.

---

## tr161-b
- task: Update the phone's software | platform: Samsung Galaxy | scenario: missing_info | sensitive: False
- sources: Samsung US Support: How to update your Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS10002027/>

**USER:**
My phone keeps saying it needs an update. How do I do it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

---

## tr161-c
- task: Update the phone's software | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung US Support: How to update your Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS10002027/>

**USER:**
My grandson keeps telling me my Samsung Galaxy is out of date and that I need to get the latest software. I have a laptop here that I use for email, and I would rather do it with the laptop and the cable that came in the box if that works. What should I do?

**ASSISTANT:**
Yes, you can update with a computer by using a program called Smart Switch.

1. Make sure the Smart Switch program is installed on your computer. If it is not, you can get it from Samsung's Smart Switch page: https://www.samsung.com/us/support/owners/app/smart-switch
2. Plug your Galaxy into the computer with the USB cable from the box. Some computers need a USB adapter.
3. Open **Smart Switch** on the computer and let it find your phone.
4. If an update is available, click **Update** and follow the prompts.

Keep the cable plugged in and do not use the phone until it finishes. The phone will restart by itself.

---

## tr161-d
- task: Update the phone's software | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung US Support: How to update your Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS10002027/>

**USER:**
My phone keeps saying it needs an update. How do I do it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
Samsung Galaxy

**ASSISTANT:**
Thanks. You can update it right on the phone.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.

---

## tr161-e
- task: Update the phone's software | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung US Support: How to update your Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS10002027/>

**USER:**
I have a Samsung Galaxy and I don't own a computer, so I can't plug it into anything. Before I update, I would also like to know what the update changes. Can I see that on the phone?

**ASSISTANT:**
Yes, you can see that on the phone, and you do not need a computer.

To see what the update includes:
1. Swipe down with two fingers from the top right corner, then tap the **Settings** icon.
2. Swipe to **Software update** (or **System updates**) and tap it.
3. Tap **Last update**, then tap **All changes**.

To update on the phone:
1. Go back to **Software update** (or **System updates**).
2. Tap **Download and install**. On some phones you may need to tap **Download now**.
3. When it finishes downloading, follow the instructions on the screen.

Note that you cannot use the phone while it installs, and that includes emergency calls.

---

## tr161-r
- task: Update the phone's software | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung US Support: How to update your Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS10002027/>

**USER:**
Please walk me through updating my Samsung Galaxy phone's software.

**ASSISTANT:**
Here is how to update it on the phone.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.

**USER:**
I looked all through Settings and there is no Software update. Where did it go?

**ASSISTANT:**
On some phones it has a different name. Try this.

1. In **Settings**, swipe down the list and look for **System updates**.
2. Tap it, then tap **Download and install**, **Check for system updates**, or **Check for software updates**. Which one you see depends on your phone company.
3. If an update is found and you see **Download now**, tap it.

---

## tr162-a
- task: Connect to a Wi-Fi network | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung Canada Support: Connect your Samsung Galaxy to the Internet <https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/>

**USER:**
How do I connect my Samsung Galaxy phone to my home Wi-Fi?

**ASSISTANT:**
Here is how to join a Wi-Fi network.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on. The networks nearby will appear in a list.
4. Tap the name of your network.
5. Type the password, then tap **Connect**.

When it works, your network name shows under **Current network** with the word **Connected** under it.

---

## tr162-c
- task: Connect to a Wi-Fi network | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung Canada Support: Connect your Samsung Galaxy to the Internet <https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/>

**USER:**
I am visiting my sister for the week and she gave me her Wi-Fi name and password on a piece of paper. I have a Samsung Galaxy and I think the Wi-Fi on my phone is switched off because I turned it off on the plane. I don't want to mess anything up. What do I tap?

**ASSISTANT:**
You will not mess anything up. Follow these steps.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. Tap the switch to turn Wi-Fi on. The networks nearby will appear in a list.
4. Tap the name your sister wrote down.
5. Type the password from the paper, then tap **Connect**.

When it works, her network name shows under **Current network** with **Connected** under it.

---

## tr162-d
- task: Connect to a Wi-Fi network | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung Canada Support: Connect your Samsung Galaxy to the Internet <https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/>

**USER:**
My phone says I have no internet at home. How do I get it onto my Wi-Fi?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
its a samsung galaxy

**ASSISTANT:**
Thanks. Here is how to join your Wi-Fi.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your home network in the list.
5. Type the password, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.

---

## tr162-e
- task: Connect to a Wi-Fi network | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung Canada Support: Connect your Samsung Galaxy to the Internet <https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/>

**USER:**
I just got a new internet router and my Samsung Galaxy needs to join it. The problem is I never wrote down the password and I have no idea what it is. Where would I find it, and what do I tap on the phone?

**ASSISTANT:**
The password is often printed on a sticker on the router, so look there first.

Then on your phone:
1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your router's network.
5. Type the password from the sticker, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.

---

## tr162-r
- task: Connect to a Wi-Fi network | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung Canada Support: Connect your Samsung Galaxy to the Internet <https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/>

**USER:**
Samsung Galaxy phone. Please tell me how to connect to Wi-Fi.

**ASSISTANT:**
Here is how to join a Wi-Fi network.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your network in the list.
5. Type the password, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.

**USER:**
I did all that but it will not connect. I think I might have typed the password wrong.

**ASSISTANT:**
A mistyped password is the most common reason. Try this.

1. Tap the network name again.
2. In the password box, tap the eye icon to see what you typed.
3. Fix any mistakes, then tap **Connect**.

If it still fails, go to **Settings**, **Connections**, then turn Wi-Fi off, wait a few seconds, and turn it back on.

---

## tr163-a
- task: Block a phone number | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung US Support: Block a phone number or contact on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10002869/>

**USER:**
Someone keeps calling me from a number I don't know. How do I block it on my Samsung Galaxy phone?

**ASSISTANT:**
You can block it from your list of recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number that keeps calling.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.

---

## tr163-c
- task: Block a phone number | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung US Support: Block a phone number or contact on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10002869/>

**USER:**
I have a Samsung Galaxy. A salesman is saved in my contacts from a while back, and now he calls me every single day about insurance. I don't want to delete him because I might forget, but I never want to hear from him again. Can I just block him from the contacts?

**ASSISTANT:**
Yes. A blocked contact stays in your list but cannot reach you.

1. Open the **Contacts** app.
2. Tap his name.
3. Tap **More**.
4. Tap **Block contact**.
5. Tap **Block** to confirm.

---

## tr163-d
- task: Block a phone number | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung US Support: Block a phone number or contact on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10002869/>

**USER:**
There is a number I want to stop hearing from. How do I block it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
Samsung Galaxy

**ASSISTANT:**
Thanks. If the number called you recently, you can block it from your recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.

---
