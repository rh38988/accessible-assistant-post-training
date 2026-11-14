# Review input: batch ex6, round 1 (52 examples)

## tr076-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

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

## tr076-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

**USER:**
how do i scan a QR code

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

## tr076-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

**USER:**
We went to lunch and there were no paper menus, just a little black and white square on the table. My friend scanned it with her phone but I didn't know how. I have an iPhone 12.

**ASSISTANT:**
That square is a QR code, and your iPhone can read it with the camera. Next time, try this:

Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.

## tr076-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

**USER:**
how do i scan a QR code

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks.

Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.

## tr077-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

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

## tr077-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

**USER:**
how do I read one of those square codes with my phone

**ASSISTANT:**
Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?

## tr077-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

**USER:**
qr code wont

**ASSISTANT:**
It looks like your message got cut off. Is the QR code **not scanning**, or is it **opening something you didn't expect**? And is your phone an iPhone or an Android phone?

## tr077-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

**USER:**
how do I read one of those square codes with my phone

**ASSISTANT:**
Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, Pixel

**ASSISTANT:**
Thanks. Your Pixel's camera can do it.

Many Android phones can read QR codes with the camera. It takes a few seconds.

1. Open the **Camera** app.
2. Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.
3. Point the camera at the QR code.
4. When a banner appears on the screen, tap it to open the link.

These steps are for Google's Camera app. Other phone brands work in a similar way but may look different. If nothing appears, tell me your phone's brand and I'll help.

Only open QR codes you trust. If a QR code asks you to pay or sign in, double-check that it's from the real business first.

## tr078-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone (Medical ID)
- task: Set up emergency medical info (iPhone (Medical ID)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105072

**USER:**
How do I set up Medical ID on my iPhone so paramedics can see my allergies?

**ASSISTANT:**
Medical ID lets first responders see your important health information from the Lock Screen, without your passcode. It takes about five minutes.

1. Open the **Health** app.
2. Tap **Summary** at the bottom.
3. Tap your **profile picture** at the top.
4. Tap **Medical ID**.
5. Tap **Edit**.
6. Turn on **Show When Locked** so it can be seen from the Lock Screen.
7. Tap **Add** next to a section, like **Allergies**, and type your information.
8. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button, choose a contact, and pick how they're related to you.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.

## tr078-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set up emergency medical info (iPhone (Medical ID)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105072

**USER:**
how can I put my medical information on my phone in case of emergency

**ASSISTANT:**
That's a really good idea. Is your phone an **iPhone** or an **Android** phone?

## tr078-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Set up emergency medical info (iPhone (Medical ID)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105072

**USER:**
I'm allergic to penicillin and my daughter said I should put it in my phone in case something happens.

**ASSISTANT:**
Your daughter has a good idea. Phones can show emergency medical information on the lock screen so responders can see it.

**Is your phone an iPhone or an Android phone?**

## tr078-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (Medical ID)
- task: Set up emergency medical info (iPhone (Medical ID)) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/105072

**USER:**
how can I put my medical information on my phone in case of emergency

**ASSISTANT:**
That's a really good idea. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. On iPhone, this is called Medical ID.

Medical ID lets first responders see your important health information from the Lock Screen, without your passcode. It takes about five minutes.

1. Open the **Health** app.
2. Tap **Summary** at the bottom.
3. Tap your **profile picture** at the top.
4. Tap **Medical ID**.
5. Tap **Edit**.
6. Turn on **Show When Locked** so it can be seen from the Lock Screen.
7. Tap **Add** next to a section, like **Allergies**, and type your information.
8. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button, choose a contact, and pick how they're related to you.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.

## tr079-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

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

## tr079-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

**USER:**
how do I put an emergency contact in my phone

**ASSISTANT:**
Good idea. Is your phone an **iPhone** or an **Android** phone?

## tr079-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Android
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

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

## tr079-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

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

## tr080-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

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

If you don't see **Notifications** for that app, it means the app can't send notifications.

## tr080-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
how do I stop all these pop-ups on my phone

**ASSISTANT:**
I can help. **Which app is sending them** (for example a game, a store, or the news)? And is your phone an **iPhone** or an **Android** phone?

## tr080-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
notifications keep

**ASSISTANT:**
It looks like your message got cut off. Are notifications **popping up too often**, or have they **stopped showing up**? And which app is it?

## tr080-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
how do I stop all these pop-ups on my phone

**ASSISTANT:**
I can help. **Which app is sending them** (for example a game, a store, or the news)? And is your phone an **iPhone** or an **Android** phone?

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

If you don't see **Notifications** for that app, it means the app can't send notifications.

## tr081-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
How do I stop a shopping app from sending notifications on my Android phone?

**ASSISTANT:**
You can turn them off for just that app. It takes less than a minute.

**Option 1, from Settings:**
1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Find the shopping app. If it's not in the list, open the menu at the top and choose all apps.
4. Tap the app and turn its notifications off.

**Option 2, from a notification:**
1. When a notification from the app shows up, swipe down from the top of the screen.
2. Press and hold the notification, then tap the settings icon.
3. Turn off notifications.

Menu names can vary a little on different phones.

## tr081-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
can I make an app stop bugging me

**ASSISTANT:**
Yes, you can turn off its notifications. Which app is it, and is your phone an **iPhone** or an **Android** phone?

## tr081-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
Ever since I bought shoes online, my phone buzzes all day with sales and coupons. I just want it to stop.

**ASSISTANT:**
That sounds tiring. You can usually turn off alerts from just that store.

**Are the alerts coming from an app on your phone, or are they emails or texts?** And is your phone an iPhone or an Android phone?

## tr081-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
can I make an app stop bugging me

**ASSISTANT:**
Yes, you can turn off its notifications. Which app is it, and is your phone an **iPhone** or an **Android** phone?

**USER:**
A shopping app on my Android

**ASSISTANT:**
Thanks.

You can turn them off for just that app. It takes less than a minute.

**Option 1, from Settings:**
1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Find the shopping app. If it's not in the list, open the menu at the top and choose all apps.
4. Tap the app and turn its notifications off.

**Option 2, from a notification:**
1. When a notification from the app shows up, swipe down from the top of the screen.
2. Press and hold the notification, then tap the settings icon.
3. Turn off notifications.

Menu names can vary a little on different phones.

## tr082-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
How do I make a web page bigger in Chrome on my computer? The words are tiny.

**ASSISTANT:**
You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. Click the **More** menu (three dots) at the top right of Chrome.
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, change the default size in **Settings**, then **Appearance**, then **Page zoom**.

## tr082-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
the words on this website are too small

**ASSISTANT:**
I can help you make them bigger. Are you on a **computer**, **phone**, or **tablet**? And if it's a computer, which browser do you use, like Chrome?

## tr082-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
chrome zoom

**ASSISTANT:**
Sure. Do you want to make **just this page** bigger, or **every website** bigger from now on?

## tr082-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
the words on this website are too small

**ASSISTANT:**
I can help you make them bigger. Are you on a **computer**, **phone**, or **tablet**? And if it's a computer, which browser do you use, like Chrome?

**USER:**
Computer, Chrome

**ASSISTANT:**
Thanks.

You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. Click the **More** menu (three dots) at the top right of Chrome.
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, change the default size in **Settings**, then **Appearance**, then **Page zoom**.

## tr083-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I downloaded a form from a website on my Windows computer. Where did it go?

**ASSISTANT:**
Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.

## tr083-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I can't find something I downloaded

**ASSISTANT:**
Let's find it. Did you download it on a **computer** or a **phone**? If it's a computer, is it **Windows** or a **Mac**?

## tr083-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
My insurance company emailed me a link to download my card as a PDF and I clicked it and something happened at the bottom of the screen but then it disappeared and now I have no idea where the card is. It's a Windows computer.

**ASSISTANT:**
It's most likely in your Downloads folder. Here's how to find it:

Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.

## tr083-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I can't find something I downloaded

**ASSISTANT:**
Let's find it. Did you download it on a **computer** or a **phone**? If it's a computer, is it **Windows** or a **Mac**?

**USER:**
Windows computer

**ASSISTANT:**
Thanks.

Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.

## tr084-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Make the mouse pointer bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

**USER:**
How do I make the mouse pointer bigger on Windows 11? I keep losing it on the screen.

**ASSISTANT:**
You can make the pointer bigger and easier to spot. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Change the **size** to make the pointer bigger.
5. You can also change the **style** or color so it stands out more.

Try a few sizes until it's easy to find.

## tr084-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make the mouse pointer bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

**USER:**
I keep losing the arrow on my screen

**ASSISTANT:**
That's common, and the arrow can be made bigger. Is your computer a **Windows** computer or a **Mac**?

## tr084-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make the mouse pointer bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

**USER:**
mouse too small

**ASSISTANT:**
I can help you make the mouse pointer bigger. Is your computer a **Windows** computer or a **Mac**?

## tr084-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Make the mouse pointer bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

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
4. Change the **size** to make the pointer bigger.
5. You can also change the **style** or color so it stands out more.

Try a few sizes until it's easy to find.

## tr085-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Account
- task: Turn on 2-Step Verification (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
How do I turn on 2-Step Verification for my Google account on my computer?

**ASSISTANT:**
2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account. Setting it up takes about five minutes.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, Google may ask you to confirm with your phone when you sign in on a new device.

**Never share these codes with anyone**, even if they say they're from Google.

If you use a work or school account, your administrator may control this setting.

## tr085-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on 2-Step Verification (Google Account) | sensitive: True | reviewed by a person: True
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
how do I make my email account more secure

**ASSISTANT:**
Good question. Which email do you use, for example **Gmail**, **Outlook**, or **Yahoo**?

## tr085-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Turn on 2-Step Verification (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
My friend's email got hacked and sent everyone weird links. Her son told her to turn on two step something. I want to do that too so it doesn't happen to me.

**ASSISTANT:**
That's a smart idea. It's called **2-Step Verification**, and most email services offer it.

**Which email do you use**, for example Gmail, Yahoo, or Outlook?

## tr085-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Account
- task: Turn on 2-Step Verification (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
how do I make my email account more secure

**ASSISTANT:**
Good question. Which email do you use, for example **Gmail**? And are you on a **computer** or a **phone**?

**USER:**
Gmail, on my computer

**ASSISTANT:**
Thanks. A strong next step for Gmail is turning on 2-Step Verification.

2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account. Setting it up takes about five minutes.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, Google may ask you to confirm with your phone when you sign in on a new device.

**Never share these codes with anyone**, even if they say they're from Google.

If you use a work or school account, your administrator may control this setting.

## tr086-a
- scenario: direct | style: plain | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
I got an email that looks like it's from my bank saying my account is locked and I need to click a link to log in and fix it. Is it real?

**ASSISTANT:**
Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but the link can lead to a fake website that steals your password.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, call your bank using the number on the **back of your card**, or go to the bank's website by typing the address yourself.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked and typed your password, call your bank right away and change your password.

## tr086-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
I got a weird email, should I click on it?

**ASSISTANT:**
Good thinking to check first. Please don't click anything yet. **Who does the email say it's from, and what is it asking you to do?**

## tr086-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
is this email from

**ASSISTANT:**
It looks like your message got cut off. **Who does the email say it's from?** And please don't click any links in it until we check.

## tr086-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
I got a weird email, should I click on it?

**ASSISTANT:**
Good thinking to check first. Please don't click anything yet. **Who does the email say it's from, and what is it asking you to do?**

**USER:**
It says it's from my bank and my account is locked, and there's a link to log in.

**ASSISTANT:**
Thank you. That's a very common scam pattern.

Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but the link can lead to a fake website that steals your password.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, call your bank using the number on the **back of your card**, or go to the bank's website by typing the address yourself.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked and typed your password, call your bank right away and change your password.

## tr087-a
- scenario: direct | style: plain | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
I keep getting spam text messages. How do I report them?

**ASSISTANT:**
Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.

## tr087-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
what do I do about junk texts

**ASSISTANT:**
There are a couple of things you can do. Would you like to **report** them, **block** the sender, or both? And is your phone an **iPhone** or an **Android** phone?

## tr087-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
Every few days I get a text saying my toll bill is overdue or my account needs verifying. I never click them but I want to do something so they stop.

**ASSISTANT:**
Good for you for not clicking. Reporting them helps your phone company block more of these:

Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.

## tr087-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
what do I do about junk texts

**ASSISTANT:**
There are a couple of things you can do. Would you like to **report** them, **block** the sender, or both? And is your phone an **iPhone** or an **Android** phone?

**USER:**
I want to report them. Android phone.

**ASSISTANT:**
Thanks. Reporting is a great idea.

Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.

## tr088-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: True
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
I met a man online three months ago. He says he loves me, he works on an oil rig overseas, and now he needs $2,000 for a plane ticket to come see me. Should I send it?

**ASSISTANT:**
I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- Strong feelings grow quickly through lots of messages.
- Now there's a **need for money**, like travel costs or an emergency.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. If it's a scam, stop contact and report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.

## tr088-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
my online friend needs money for an emergency, should I help?

**ASSISTANT:**
I'm glad you asked first. A couple of questions will help me give you good advice: **Have you met this person in person?** And **how are they asking you to send the money?**

## tr088-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
I've been talking to someone special online and he's asking me for help. I don't know what to do.

**ASSISTANT:**
Thank you for trusting me with this. **What kind of help is he asking for?** And have the two of you met in person?

## tr088-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
my online friend needs money for an emergency, should I help?

**ASSISTANT:**
I'm glad you asked first. A couple of questions will help me give you good advice: **Have you met this person in person?** And **how are they asking you to send the money?**

**USER:**
No, we've only talked online for three months. He wants me to wire $2,000 for a plane ticket.

**ASSISTANT:**
Thank you for telling me.

I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- Strong feelings grow quickly through lots of messages.
- Now there's a **need for money**, like travel costs or an emergency.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. If it's a scam, stop contact and report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.
