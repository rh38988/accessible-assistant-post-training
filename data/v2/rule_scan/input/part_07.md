# Rule scan input, part 07 (50 examples)

## tr073-b
- task: Zoom in on the screen | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Accessibility Help: Use magnification on your screen <https://support.google.com/accessibility/android/answer/6006949?hl=en>

**USER:**
can I zoom in on my phone screen

**ASSISTANT:**
Yes, most phones can. Is yours an **iPhone** or an **Android** phone?

---

## tr073-c
- task: Zoom in on the screen | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Accessibility Help: Use magnification on your screen <https://support.google.com/accessibility/android/answer/6006949?hl=en>

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

---

## tr073-d
- task: Zoom in on the screen | platform: Android | scenario: followup | sensitive: False
- sources: Android Accessibility Help: Use magnification on your screen <https://support.google.com/accessibility/android/answer/6006949?hl=en>

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

---

## tr073-e
- task: Zoom in on the screen | platform: Android | scenario: constraint | sensitive: False
- sources: Android Accessibility Help: Use magnification on your screen <https://support.google.com/accessibility/android/answer/6006949?hl=en>

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

---

## tr074-b
- task: Find a lost phone | platform: iPhone (Find My) | scenario: missing_info | sensitive: True
- sources: Apple Support: How to find your lost iPhone or iPad <https://support.apple.com/en-us/101593>

**USER:**
I lost my phone

**ASSISTANT:**
I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?

---

## tr074-e
- task: Find a lost phone | platform: iPhone (Find My) | scenario: constraint | sensitive: True
- sources: Apple Support: How to find your lost iPhone or iPad <https://support.apple.com/en-us/101593>

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

---

## tr075-b
- task: Find a lost phone | platform: Android | scenario: missing_info | sensitive: True
- sources: Google Account Help: Find, secure, or erase a lost Android device <https://support.google.com/accounts/answer/6160491?hl=en>

**USER:**
can't find my phone anywhere

**ASSISTANT:**
Let's try to find it. Is it an **iPhone** or an **Android** phone?

---

## tr075-c
- task: Find a lost phone | platform: Android | scenario: missing_info | sensitive: True
- sources: Google Account Help: Find, secure, or erase a lost Android device <https://support.google.com/accounts/answer/6160491?hl=en>

**USER:**
lost phone help

**ASSISTANT:**
I'm sorry, let's try to find it. Is it an **iPhone** or an **Android** phone?

---

## tr075-e
- task: Find a lost phone | platform: Android | scenario: constraint | sensitive: True
- sources: Google Account Help: Find, secure, or erase a lost Android device <https://support.google.com/accounts/answer/6160491?hl=en>

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

---

## tr075-r
- task: Find a lost phone | platform: Android | scenario: failure_recovery | sensitive: True
- sources: Google Account Help: Find, secure, or erase a lost Android device <https://support.google.com/accounts/answer/6160491?hl=en>

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

---

## tr076-a
- task: Scan a QR code | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Scan a QR code with your iPhone or iPad <https://support.apple.com/en-us/102680>

**USER:**
How do I scan a QR code with my iPhone? The restaurant menu is a QR code.

**ASSISTANT:**
Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.

---

## tr076-b
- task: Scan a QR code | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Scan a QR code with your iPhone or iPad <https://support.apple.com/en-us/102680>

**USER:**
how do i scan a QR code

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr076-c
- task: Scan a QR code | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Scan a QR code with your iPhone or iPad <https://support.apple.com/en-us/102680>

**USER:**
We went to lunch and there were no paper menus, just a little black and white square on the table. My friend scanned it with her phone but I didn't know how. I have an iPhone 12.

**ASSISTANT:**
That square is a QR code, and your iPhone can read it with the Camera app.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**. If you don't see **Scan Code** in Control Center, touch and hold the background of Control Center, tap **Add a Control**, then tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.

---

## tr076-d
- task: Scan a QR code | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Scan a QR code with your iPhone or iPad <https://support.apple.com/en-us/102680>

**USER:**
how do i scan a QR code

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The page or app that the code is for will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed by a business you know.

---

## tr076-r
- task: Scan a QR code | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Scan a QR code with your iPhone or iPad <https://support.apple.com/en-us/102680>

**USER:**
How do I use the Scan Code button on my iPhone to read a QR code?

**ASSISTANT:**
The **Scan Code** button is in Control Center. Here is how to use it.

1. Open **Control Center**.
2. Tap the **Scan Code** button. It has a little square viewfinder picture.
3. Hold your iPhone so the QR code is in view.
4. Tap the **link** that appears.

If you don't see **Scan Code** in Control Center, tell me and I'll show you how to add it.

**USER:**
There is no Scan Code button in my Control Center.

**ASSISTANT:**
That button only shows up after you add it. Here is how:

1. Open **Control Center**.
2. Touch and hold the background of the screen, then tap **Add a Control**.
3. In the list that opens, tap **Scan Code**.
4. Tap anywhere on the screen to go back to Control Center.

Now **Scan Code** should be in Control Center, and you can use it to scan.

---

## tr077-a
- task: Scan a QR code | platform: Android | scenario: direct | sensitive: False
- sources: Camera from Google Help: Scan QR codes <https://support.google.com/camerafromgoogle/answer/12033278?hl=en>

**USER:**
How do I scan a QR code with my Android phone's camera?

**ASSISTANT:**
Many Android phones can read QR codes with the camera. It takes a few seconds.

1. Open the **Camera** app.
2. Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.
3. Point the camera at the QR code.
4. When a banner appears on the screen, tap it to open the link.

These steps are for Google's Camera app. Other phone brands work in a similar way but may look different. If nothing appears, tell me your phone's brand and I'll help.

Only open QR codes you trust. If a QR code asks you to pay or sign in, double-check that it's from the real business first.

---

## tr077-b
- task: Scan a QR code | platform: Android | scenario: missing_info | sensitive: False
- sources: Camera from Google Help: Scan QR codes <https://support.google.com/camerafromgoogle/answer/12033278?hl=en>

**USER:**
how do I read one of those square codes with my phone

**ASSISTANT:**
Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?

---

## tr077-c
- task: Scan a QR code | platform: Android | scenario: missing_info | sensitive: False
- sources: Camera from Google Help: Scan QR codes <https://support.google.com/camerafromgoogle/answer/12033278?hl=en>

**USER:**
qr code wont

**ASSISTANT:**
It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?

---

## tr077-e
- task: Scan a QR code | platform: Android | scenario: constraint | sensitive: False
- sources: Camera from Google Help: Scan QR codes <https://support.google.com/camerafromgoogle/answer/12033278?hl=en>

**USER:**
I use the Camera from Google app on my Android. It is set to video mode because I was filming my granddaughter, and I'd like to scan a QR code without leaving video mode. Can I?

**ASSISTANT:**
Not in video mode. QR codes can't be scanned in video mode or portrait mode, so you need to switch out of video mode first.

1. Open the **Camera from Google** app.
2. Switch to regular photo mode, or tap the **QR** button.
3. Point your camera at the QR code.
4. When a banner appears, tap it to open the page or app.

You can switch back to video mode when you are done.

---

## tr077-r
- task: Scan a QR code | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Camera from Google Help: Scan QR codes <https://support.google.com/camerafromgoogle/answer/12033278?hl=en>

**USER:**
How do I scan a QR code with the Camera from Google app on my Android?

**ASSISTANT:**
You can do it right in the camera. It takes a few seconds.

1. Open the **Camera from Google** app.
2. Tap the **QR** button, then point your camera at the code. You can also just point at the code in regular photo mode.
3. When a banner appears, tap it to open the page or app.

QR codes can't be scanned in portrait or video mode.

**USER:**
I don't see a QR button anywhere.

**ASSISTANT:**
That is okay. Try this instead:

1. Make sure the camera is in regular photo mode, not portrait or video.
2. Point the camera at the code without tapping anything.
3. When the banner appears, tap it.

If nothing shows up, this feature is only on selected devices, so your phone may not have it.

---

## tr078-a
- task: Set up emergency medical info | platform: iPhone (Medical ID) | scenario: direct | sensitive: True
- sources: Apple Support: Set up your Medical ID in the Health app on your iPhone <https://support.apple.com/en-us/105072>

**USER:**
How do I set up Medical ID on my iPhone so paramedics can see my allergies?

**ASSISTANT:**
Medical ID lets first responders see your important health information from the Lock Screen, without your passcode.

1. Open the **Health** app.
2. Tap **Summary**.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Turn on **Show When Locked** so it can be seen from the Lock Screen.
6. Tap **Add** next to a section, like **Allergies**, and type your information.
7. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you. Then tap **Done**.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.

---

## tr078-d
- task: Set up emergency medical info | platform: iPhone (Medical ID) | scenario: followup | sensitive: True
- sources: Apple Support: Set up your Medical ID in the Health app on your iPhone <https://support.apple.com/en-us/105072>

**USER:**
how can I put my medical information on my phone in case of emergency

**ASSISTANT:**
That's a really good idea. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. On iPhone, this is called Medical ID.

Medical ID lets first responders see your important health information from the Lock Screen, without your passcode.

1. Open the **Health** app.
2. Tap **Summary**.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Turn on **Show When Locked** so it can be seen from the Lock Screen.
6. Tap **Add** next to a section, like **Allergies**, and type your information.
7. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you. Then tap **Done**.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.

---

## tr078-e
- task: Set up emergency medical info | platform: iPhone (Medical ID) | scenario: constraint | sensitive: True
- sources: Apple Support: Set up your Medical ID in the Health app on your iPhone <https://support.apple.com/en-us/105072>

**USER:**
I have an iPhone. I don't want to type in my medications or conditions, I only want my son listed as my emergency contact on my Medical ID. What do I do?

**ASSISTANT:**
You can add just an emergency contact and leave everything else empty.

1. Open the **Health** app.
2. Tap the **Summary** tab.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Tap **Edit** next to **Emergency Contacts**.
6. Tap the **plus** button next to **Add Emergency Contact**.
7. Choose your son from your contacts and add how he is related to you.
8. Tap **Done**.

To remove a contact later, go back to the same place, tap the **delete** button next to the name, then tap **Delete**.

---

## tr078-r
- task: Set up emergency medical info | platform: iPhone (Medical ID) | scenario: failure_recovery | sensitive: True
- sources: Apple Support: Set up your Medical ID in the Health app on your iPhone <https://support.apple.com/en-us/105072>

**USER:**
How do I make my iPhone share my Medical ID with emergency services when I call them? I have an iPhone.

**ASSISTANT:**
You can turn that on in your Medical ID.

1. Open the **Health** app and tap the **Summary** tab.
2. Tap your **profile picture** in the upper corner.
3. Tap **Medical ID**.
4. Turn on **Share During Emergency Call**.
5. Tap **Done**.

Then your Medical ID is shared when you call or text emergency services from your iPhone.

**USER:**
I did that, but how can I be sure it will really get sent? I'm worried it's not working.

**ASSISTANT:**
Good question. There is one more setting to check:

1. Open **Settings**.
2. Tap **Privacy & Security**, then **Location Services**.
3. Tap **System Services**.
4. Make sure **Emergency Calls & SOS** is turned on.

If it is off, your Medical ID information won't be shared.

---

## tr079-a
- task: Add emergency information | platform: Android | scenario: direct | sensitive: True
- sources: Android Help: Get help during an emergency with your Android phone <https://support.google.com/android/answer/9319337?hl=en>

**USER:**
How do I add my emergency contacts and medical info on my Android phone?

**ASSISTANT:**
On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.

---

## tr079-b
- task: Add emergency information | platform: Android | scenario: missing_info | sensitive: True
- sources: Android Help: Get help during an emergency with your Android phone <https://support.google.com/android/answer/9319337?hl=en>

**USER:**
how do I put an emergency contact in my phone

**ASSISTANT:**
Good idea. Is your phone an **iPhone** or an **Android** phone?

---

## tr079-c
- task: Add emergency information | platform: Android | scenario: direct_messy | sensitive: True
- sources: Android Help: Get help during an emergency with your Android phone <https://support.google.com/android/answer/9319337?hl=en>

**USER:**
Pixel 7, Android 15. I want my husband listed as my emergency contact and my blood thinner listed under medications, visible without unlocking.

**ASSISTANT:**
Here's how to set up exactly that:

On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.

---

## tr079-d
- task: Add emergency information | platform: Android | scenario: followup | sensitive: True
- sources: Android Help: Get help during an emergency with your Android phone <https://support.google.com/android/answer/9319337?hl=en>

**USER:**
how do I put an emergency contact in my phone

**ASSISTANT:**
Good idea. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.

---

## tr079-e
- task: Add emergency information | platform: Android | scenario: constraint | sensitive: True
- sources: Android Help: Get help during an emergency with your Android phone <https://support.google.com/android/answer/9319337?hl=en>

**USER:**
I want to save my emergency contact and my medicines in my Android phone, but I do not want any of it showing on the lock screen for strangers to see. Is that possible?

**ASSISTANT:**
Yes. The lock screen part is optional, so you can simply skip it.

1. Open the **Safety** app and sign in to your Google Account.
2. Tap **Your info**.
3. Tap **Medical information**, then tap **Medications** and type your details.
4. Go back and tap **Emergency contacts**.
5. Tap **Add contact** and choose someone.

Do not turn on **Show when locked** under **Emergency info access**. Anyone holding your phone can see information that is shown on the lock screen. If it is already showing there, you can turn it off in the Safety app.

---

## tr079-r
- task: Add emergency information | platform: Android | scenario: failure_recovery | sensitive: True
- sources: Android Help: Get help during an emergency with your Android phone <https://support.google.com/android/answer/9319337?hl=en>

**USER:**
How do I put my allergies and an emergency contact on my Android phone?

**ASSISTANT:**
You can do it in the **Safety** app.

1. Open the **Safety** app and sign in to your Google Account.
2. Tap **Your info**.
3. Tap **Medical information**, then tap **Allergies** and type your details.
4. Go back and tap **Emergency contacts**.
5. Tap **Add contact** and choose someone.

**USER:**
I can't find an app called Safety on my phone.

**ASSISTANT:**
Here are a few things that can explain it.

1. In your list of apps it is called **Safety**. In the Play Store and in **Settings** it is called **Personal Safety**, so look for that name there.
2. If the app has been turned off (disabled), it will not show in your app list.
3. This app is only on some Android phones, so yours may not have it.
4. On Android 12 and earlier without the app, you can still sign in with your Google Account, add emergency contacts, and list medical information.

---

## tr080-a
- task: Turn off notifications from an app | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Turn notifications on or off for a specific app on your iPhone <https://support.apple.com/en-us/120681>

**USER:**
One of my iPhone games keeps sending me notifications. How do I turn them off?

**ASSISTANT:**
You can turn off notifications for just that app. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Find and tap the game.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

The game will still work. It just won't send you alerts anymore.

If you don't see **Notifications** for that app, the app may not be able to send notifications.

---

## tr080-b
- task: Turn off notifications from an app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Turn notifications on or off for a specific app on your iPhone <https://support.apple.com/en-us/120681>

**USER:**
how do I stop all these pop-ups on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr080-c
- task: Turn off notifications from an app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Turn notifications on or off for a specific app on your iPhone <https://support.apple.com/en-us/120681>

**USER:**
notifications keep

**ASSISTANT:**
It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?

---

## tr080-d
- task: Turn off notifications from an app | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Turn notifications on or off for a specific app on your iPhone <https://support.apple.com/en-us/120681>

**USER:**
how do I stop all these pop-ups on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
It's a solitaire game. iPhone.

**ASSISTANT:**
Thanks. Here's how to turn off notifications for the solitaire game.

You can turn off notifications for just that app. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Find and tap the game.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

The game will still work. It just won't send you alerts anymore.

If you don't see **Notifications** for that app, the app may not be able to send notifications.

---

## tr080-e
- task: Turn off notifications from an app | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Turn notifications on or off for a specific app on your iPhone <https://support.apple.com/en-us/120681>

**USER:**
My iPhone's news app buzzes me all day. I need my text messages and calendar alerts to keep working, so I only want to stop the news app. How?

**ASSISTANT:**
You can change this for one app at a time, so your other apps will not be touched.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Tap the news app.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

Only the news app goes quiet. Your messages and calendar keep sending alerts the way they do now.

---

## tr080-r
- task: Turn off notifications from an app | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Turn notifications on or off for a specific app on your iPhone <https://support.apple.com/en-us/120681>

**USER:**
My iPhone keeps showing alerts from a coupon app. How do I stop them?

**ASSISTANT:**
You can turn them off for just that app.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Tap the coupon app.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

**USER:**
I tapped the coupon app but I don't see Notifications there.

**ASSISTANT:**
Let's check two things.

1. Go back to the **Apps** list in **Settings** and make sure you tapped the coupon app itself.
2. If you are in the right app and still don't see **Notifications**, that app may not be able to send notifications at all.

---

## tr081-c
- task: Turn off notifications from an app | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Control notifications on Android <https://support.google.com/android/answer/9079661?hl=en>

**USER:**
Ever since I bought shoes online, my phone buzzes all day with sales and coupons. I just want it to stop.

**ASSISTANT:**
That sounds tiring. Is your phone an **iPhone** or an **Android** phone?

---

## tr081-e
- task: Turn off notifications from an app | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Control notifications on Android <https://support.google.com/android/answer/9079661?hl=en>

**USER:**
On my Android phone, my pharmacy app sends both sale ads and refill reminders. I want to keep the refill reminders and stop only the ads. Can I do that?

**ASSISTANT:**
Yes. You can turn off just the kinds of alerts you don't want.

1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Tap the pharmacy app.
4. Tap a **category** to see more options.
5. Turn off the categories you don't want, like the ads.

Leave the refill reminder category turned on. Menu names can vary a little on different phones.

---

## tr082-a
- task: Make a web page bigger | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
How do I make a web page bigger in Chrome on my computer? The words are tiny.

**ASSISTANT:**
You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. At the top right of Chrome, click **More**.
2. Next to **Zoom**, click **Zoom in** to make the page bigger. Click **Zoom out** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.

---

## tr082-b
- task: Make a web page bigger | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
the words on this website are too small

**ASSISTANT:**
I can help you make them bigger. Are you on a **computer**, a **phone**, or a **tablet**?

---

## tr082-d
- task: Make a web page bigger | platform: Chrome (computer) | scenario: followup | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
the words on this website are too small

**ASSISTANT:**
I can help you make them bigger. Are you on a **computer**, a **phone**, or a **tablet**?

**USER:**
Computer, Chrome

**ASSISTANT:**
Thanks.

You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. At the top right of Chrome, click **More**.
2. Next to **Zoom**, click **Zoom in** to make the page bigger. Click **Zoom out** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.

---

## tr082-e
- task: Make a web page bigger | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I use Chrome on my Windows laptop. I want the words bigger on every website, but I don't want the pictures and buttons to get bigger too, it messes up the layout. Is there a way?

**ASSISTANT:**
Yes. Chrome has a setting for the text size only.

1. Open Chrome and click **More** at the top right.
2. Click **Settings**.
3. Click **Appearance**.
4. Click the down arrow next to **Font size** and pick a size.

This changes the words and leaves the page size setting alone. Do not use **Page zoom**, because that makes everything bigger.

Some websites don't let Chrome change only the text size, so on those sites the words may stay the same.

---

## tr082-r
- task: Make a web page bigger | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Google Chrome Help: Change text, image & video sizes (zoom), computer <https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
How do I zoom in on one website in Chrome on my computer?

**ASSISTANT:**
You can zoom in from the menu.

1. Open Chrome and go to the website.
2. Click **More** at the top right.
3. Next to **Zoom**, click **Zoom in**. Click it again to go bigger.

You can also hold **Ctrl** and press **+**. To go smaller, use **Zoom out** or hold **Ctrl** and press **-**.

**USER:**
I made that site way too big and now it opens huge every time. How do I put it back?

**ASSISTANT:**
Chrome remembers the size for each site. You can clear it:

1. Click **More**, then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Additional content settings**, then **Zoom levels**.
4. Click the **X** next to that site.

That removes the saved size for the site.

---

## tr083-b
- task: Find a downloaded file | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Find my downloads in Windows <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8>

**USER:**
I can't find something I downloaded

**ASSISTANT:**
Let's find it. Is this on a **Windows computer**, a **Mac**, or a **phone**?

---

## tr083-r
- task: Find a downloaded file | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Find my downloads in Windows <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8>

**USER:**
Where do I find the picture I just downloaded on my Windows 11 computer?

**ASSISTANT:**
It is most likely in your **Downloads** folder.

1. Press the **Windows logo key** and **E** together to open File Explorer.
2. Select **Home** in the left pane.
3. Under **Quick access**, open **Downloads**.
4. Look for your picture in the list.

On Windows 11 version 22H2 or later, **Downloads** is pinned there by default.

**USER:**
My File Explorer doesn't have a list on the left side.

**ASSISTANT:**
The left pane may be hidden. You can turn it back on:

1. In File Explorer, select **View**.
2. Select **Show**.
3. Select **Navigation Pane**.

Then select **Home** and open **Downloads** under **Quick access**.

---

## tr084-a
- task: Make the mouse pointer bigger | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Make Windows easier to see <https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see>

**USER:**
How do I make the mouse pointer bigger on Windows 11? I keep losing it on the screen.

**ASSISTANT:**
You can make the pointer bigger and easier to spot. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Change the size of the mouse pointer to make it bigger.
5. You can also change the color of the mouse pointer so it stands out more.

Try a few sizes until it's easy to find.

---

## tr084-b
- task: Make the mouse pointer bigger | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Make Windows easier to see <https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see>

**USER:**
I keep losing the arrow on my screen

**ASSISTANT:**
That's common, and the arrow can be made bigger. Is your computer a **Windows** computer or a **Mac**?

---

## tr084-c
- task: Make the mouse pointer bigger | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Make Windows easier to see <https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see>

**USER:**
mouse too small

**ASSISTANT:**
I can help you make the mouse pointer bigger. Is your computer a **Windows** computer or a **Mac**?

---

## tr084-d
- task: Make the mouse pointer bigger | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Make Windows easier to see <https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see>

**USER:**
I keep losing the arrow on my screen

**ASSISTANT:**
That's common, and the arrow can be made bigger. Is your computer a **Windows** computer or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks.

You can make the pointer bigger and easier to spot. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Change the size of the mouse pointer to make it bigger.
5. You can also change the color of the mouse pointer so it stands out more.

Try a few sizes until it's easy to find.

---

## tr084-e
- task: Make the mouse pointer bigger | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Make Windows easier to see <https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see>

**USER:**
I have Windows 11. I only want the little arrow to be bigger. Please don't change my text or the size of everything else on the screen, I just got it the way I like it.

**ASSISTANT:**
You can change just the pointer. Your text and screen size will stay as they are.

1. Click the **Start** button, then click **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Choose the options that change the pointer's color and size, and pick what works best for you.

Leave the **Text size** and **Display** settings alone, because those change other things on your screen.

---
