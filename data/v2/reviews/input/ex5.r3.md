# Review input: batch ex5, round 3 (5 examples)

## tr073-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Zoom in on the screen (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

**USER:**
The print on my medicine reminder app is so tiny, and making the text bigger messes up how the app looks. My Android phone is a Pixel.

**ASSISTANT:**
Magnification can help with that. It zooms in on the whole screen, and you turn it on and off with your shortcut.

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
2. Select your iPhone to locate it.
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
2. Select your iPhone to locate it.
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

## tr075-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Find a lost phone (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/6160491?hl=en

**USER:**
I lost my Android phone. How can I find it?

**ASSISTANT:**
You can look for it with **Find Hub** from another device. If its current location can't be found, you may still see its last known location, if available.

1. On another Android phone, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. If asked, enter your lock screen PIN. If the phone has no PIN, or runs Android 8 or lower, you may be asked for your Google password.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** tap **Mark as lost**, then **Next**. Add a message and a phone number, then tap **Mark as lost** again to confirm.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.

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

You can look for it with **Find Hub** from another device. If its current location can't be found, you may still see its last known location, if available.

1. On another Android phone, open the **Find Hub** app. If your husband's phone isn't an Android phone, open a web browser on it and go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. If asked, enter your lock screen PIN. If the phone has no PIN, or runs Android 8 or lower, you may be asked for your Google password.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** tap **Mark as lost**, then **Next**. Add a message and a phone number, then tap **Mark as lost** again to confirm.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.
