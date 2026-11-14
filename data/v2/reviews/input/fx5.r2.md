# Review input: batch fx5, round 2 (8 examples)

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
Your phone may show it a little differently. Try this instead:

1. Look for **Browse** and tap it.
2. Select the files you want to delete. You can also select all of them.
3. Tap **Move files to Trash**.

Menu names can differ a little between phones, and some steps need Android 14 or newer.

## tr063-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on the flashlight (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105001

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

## tr068-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Pair hearing aids or Bluetooth headphones (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108780

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

## tr071-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on battery saving mode (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7664692?hl=en

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
4. Turn on **Magnification shortcut**.
5. Tap **Magnification shortcut** and choose **Accessibility button**.
6. Tap the **Accessibility** icon at the bottom of the screen. Its exact spot depends on how your phone is set up.
7. **Drag with two fingers** to move the zoom window, and **pinch** to change how much it zooms.

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

With **Accessibility button**, tap the Accessibility icon at the bottom of the screen. With **Hold volume keys**, hold both volume buttons together.

## tr074-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone (Find My)
- task: Find a lost phone (iPhone (Find My)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/101593

**USER:**
My iPhone is missing since this morning. My wife has an iPad. What should I do on it?

**ASSISTANT:**
Use the web browser on her iPad.

1. Go to **icloud.com/find**.
2. Sign in with your Apple Account.
3. Open **All Devices** and tap your iPhone.
4. Choose to mark it as lost.

You can also play a sound from here.

**USER:**
It shows my phone as offline, no location at all.

**ASSISTANT:**
That means it is off or not on Wi-Fi or cellular. Until it reconnects, it won't show as online or in Lost Mode. You can still mark it as lost now:

1. On her iPad, go to **icloud.com/find** in the web browser.
2. Sign in with your Apple Account if you are asked.
3. Open **All Devices** and tap your iPhone.
4. Choose to mark it as lost.

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
The location can be off by roughly 20 meters, and it is less reliable indoors. Try this:

1. Tap **Play sound**. It rings at full volume for 5 minutes, even on silent.
2. Walk toward the sound.
3. Once you are within 10 meters, tap **Find nearby**. A shape fills in as you get closer.
