"""Fill examples for group 6 (batch fx6). New examples only."""
TASKS = []

TASKS.append({
    "task_id": 'TR-076', "task_type": 'scan_qr', "task": 'Scan a QR code',
    "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Apple Support: Scan a QR code with your iPhone or iPad', "url": 'https://support.apple.com/en-us/102680'},
    "source_notes": """Camera app method: open Camera app from Home Screen, Lock Screen, or Control Center (supported models can also use Camera Control). Hold device so that the QR code appears, then tap the link to open the content. The page gives no position for the link on screen.
Control Center method: open Control Center, tap the Scan Code button (QR viewfinder icon), hold device so the code is in view, tap the link.
Setup for method 2: Scan Code shows in Control Center only after adding it. Open Control Center, touch and hold the background of the screen, tap Add a Control, in the gallery tap Scan Code, then tap anywhere on the screen to return to Control Center.
No troubleshooting section on the page.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
         "messages": [
             "My iPhone screen is asleep on the counter and my hands are messy from cooking. Is there a quicker way to get to the camera for the QR code on my recipe card, without hunting for apps?",
             """Yes, you can open the camera straight from the Lock Screen.

1. Open the **Camera** from the Lock Screen.
2. Hold your iPhone so the QR code is in view.
3. Tap the **link**.

The link or content from the code will open.

You can also open the camera from **Control Center**. On supported iPhone models you can also open the camera with the **Camera Control** button.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
         "messages": [
             "How do I use the Scan Code button on my iPhone to read a QR code?",
             """The **Scan Code** button is in Control Center. Here is how to use it.

1. Open **Control Center**.
2. Tap the **Scan Code** button. It has a little square viewfinder picture.
3. Hold your iPhone so the QR code is in view.
4. Tap the **link** that appears.

If you don't see **Scan Code** in Control Center, tell me and I'll show you how to add it.""",
             "There is no Scan Code button in my Control Center.",
             """That button only shows up after you add it. Here is how:

1. Open **Control Center**.
2. Touch and hold the background of the screen, then tap **Add a Control**.
3. In the list that opens, tap **Scan Code**.
4. Tap anywhere on the screen to go back to Control Center.

Now **Scan Code** should be in Control Center, and you can use it to scan.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-077', "task_type": 'scan_qr', "task": 'Scan a QR code',
    "platform": 'Android', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Camera from Google Help: Scan QR codes', "url": 'https://support.google.com/camerafromgoogle/answer/12033278?hl=en'},
    "source_notes": """Steps for Camera from Google app: 1 Open the Camera from Google app. 2 Choose a method: QR mode (tap the QR button, then point the camera at the code) or default photo mode (point the camera at the code without changing modes). You can't scan a QR code in portrait and video mode. 3 When the code is detected, tap/click the banner that appears to open the browser page, app, or payments app.
Feature available only on selected devices; page lists no models. If you have a Pixel Camera rather than Camera from Google, the page points to the Pixel Camera Help Center. No other troubleshooting.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "I use the Camera from Google app on my Android. It is set to video mode because I was filming my granddaughter, and I'd like to scan a QR code without leaving video mode. Can I?",
             """Not in video mode. QR codes can't be scanned in video mode or portrait mode, so you need to switch out of video mode first.

1. Open the **Camera from Google** app.
2. Switch to regular photo mode, or tap the **QR** button.
3. Point your camera at the QR code.
4. When a banner appears, tap it to open the page or app.

You can switch back to video mode when you are done.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "How do I scan a QR code with the Camera from Google app on my Android?",
             """You can do it right in the camera. It takes a few seconds.

1. Open the **Camera from Google** app.
2. Tap the **QR** button, then point your camera at the code. You can also just point at the code in regular photo mode.
3. When a banner appears, tap it to open the page or app.

QR codes can't be scanned in portrait or video mode.""",
             "I don't see a QR button anywhere.",
             """That is okay. Try this instead:

1. Make sure the camera is in regular photo mode, not portrait or video.
2. Point the camera at the code without tapping anything.
3. When the banner appears, tap it.

If nothing shows up, this feature is only on selected devices, so your phone may not have it.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-078', "task_type": 'emergency_info', "task": 'Set up emergency medical info',
    "platform": 'iPhone (Medical ID)', "category": 'technical_support', "sensitive": True,
    "source": {"title": 'Apple Support: Set up your Medical ID in the Health app on your iPhone', "url": 'https://support.apple.com/en-us/105072'},
    "source_notes": """Medical ID: open Health app, tap Summary tab, tap profile picture in upper corner, under it tap Medical ID. Turn on Show When Locked (so Medical ID appears on Lock screen). Turn on Share During Emergency Call (shares with emergency services when you call or text them). Tap Edit or Add next to a field such as Medications, Allergies, Conditions and enter details. Tap Done.
Emergency Contacts: Health, Summary, profile picture, Medical ID. Tap Edit next to Emergency Contacts. Tap the plus button next to Add Emergency Contact, choose a contact, add their relationship. To remove: delete button next to them, tap Delete. Tap Done.
Organ donor (US only): profile picture, Features, Organ Donation, Sign Up with Donate Life, fill form, Continue, Complete Registration with Donate Life, Done.
Responders see Medical ID on Lock screen without passcode (allergies, conditions, emergency contacts). If Share During Emergency Call is on, shared automatically when you call or text emergency services from iPhone or Apple Watch.
To confirm sharing works: Settings, Privacy & Security, Location Services, System Services, make sure Emergency Calls & SOS is on. If it is off, Medical ID info won't be shared. Apple cannot read the info shared. Enhanced Emergency Data not in all countries or regions.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone (Medical ID)",
         "messages": [
             "I have an iPhone. I don't want to type in my medications or conditions, I only want my son listed as my emergency contact on my Medical ID. What do I do?",
             """You can add just an emergency contact and leave everything else empty.

1. Open the **Health** app.
2. Tap the **Summary** tab.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Tap **Edit** next to **Emergency Contacts**.
6. Tap the **plus** button next to **Add Emergency Contact**.
7. Choose your son from your contacts and add how he is related to you.
8. Tap **Done**.

To remove a contact later, go back to the same place, tap the **delete** button next to the name, then tap **Delete**.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone (Medical ID)",
         "messages": [
             "How do I make my iPhone share my Medical ID with emergency services when I call them? I have an iPhone.",
             """You can turn that on in your Medical ID.

1. Open the **Health** app and tap the **Summary** tab.
2. Tap your **profile picture** in the upper corner.
3. Tap **Medical ID**.
4. Turn on **Share During Emergency Call**.
5. Tap **Done**.

Then your Medical ID is shared when you call or text emergency services from your iPhone.""",
             "I did that, but how can I be sure it will really get sent? I'm worried it's not working.",
             """Good question. There is one more setting to check:

1. Open **Settings**.
2. Tap **Privacy & Security**, then **Location Services**.
3. Tap **System Services**.
4. Make sure **Emergency Calls & SOS** is turned on.

If it is off, your Medical ID information won't be shared.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-079', "task_type": 'emergency_info', "task": 'Add emergency information',
    "platform": 'Android', "category": 'technical_support', "sensitive": True,
    "source": {"title": 'Android Help: Get help during an emergency with your Android phone', "url": 'https://support.google.com/android/answer/9319337?hl=en'},
    "source_notes": """Safety app (called Safety in app list; Personal Safety in Play Store and Settings). Steps: open Safety app; sign in to Google Account; tap Your info; Medical information: tap Medical information, then tap an item such as blood type, allergies, medications to update. Emergency contacts: tap Emergency contacts, then Add contact, choose an existing contact. Show on lock screen (optional): tap Emergency info access, then Show when locked.
Others view: on locked screen swipe up, tap Emergency, tap View emergency info. To share with responders during a call: Your info, Emergency Info access, Share during emergency call.
Lock screen info can be seen by anyone holding the phone, even locked; you can turn this off in the Safety app. Family Link supervised users with contact limits must also add each emergency contact as a Parent Managed Contact. Without a SIM/eSIM you may place emergency calls but can't call emergency contacts.
Troubleshooting: if you can't find the Safety app, check whether device includes Personal Safety app; availability may vary. Some steps require Android 12 or later; check Android version in Settings. On Android 12 and earlier without the Personal Safety app, you can sign in with Google Account, add emergency contacts and list medical info.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "I want to save my emergency contact and my medicines in my Android phone, but I do not want any of it showing on the lock screen for strangers to see. Is that possible?",
             """Yes. The lock screen part is optional, so you can simply skip it.

1. Open the **Safety** app and sign in to your Google Account.
2. Tap **Your info**.
3. Tap **Medical information**, then tap **Medications** and type your details.
4. Go back and tap **Emergency contacts**.
5. Tap **Add contact** and choose someone.

Do not turn on **Show when locked** under **Emergency info access**. Anyone holding your phone can see information that is shown on the lock screen. If it is already showing there, you can turn it off in the Safety app.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "How do I put my allergies and an emergency contact on my Android phone?",
             """You can do it in the **Safety** app.

1. Open the **Safety** app and sign in to your Google Account.
2. Tap **Your info**.
3. Tap **Medical information**, then tap **Allergies** and type your details.
4. Go back and tap **Emergency contacts**.
5. Tap **Add contact** and choose someone.""",
             "I can't find an app called Safety on my phone.",
             """Here are a few things that can explain it.

1. In your list of apps it is called **Safety**. In the Play Store and in **Settings** it is called **Personal Safety**, so look for that name there.
2. If the app has been turned off (disabled), it will not show in your app list.
3. This app is only on some Android phones, so yours may not have it.
4. On Android 12 and earlier without the app, you can still sign in with your Google Account, add emergency contacts, and list medical information.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-080', "task_type": 'app_notifications_off', "task": 'Turn off notifications from an app',
    "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Apple Support: Turn notifications on or off for a specific app on your iPhone', "url": 'https://support.apple.com/en-us/120681'},
    "source_notes": """Steps: 1 Open Settings app and tap Apps. 2 Tap the app you want to change. 3 Tap Notifications. 4 Turn Allow Notifications on or off.
If Notifications doesn't appear for an app, that app may not be able to send notifications. After turning Allow Notifications on, you can also adjust sounds, placement and appearance of that app's notifications. No other troubleshooting.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
         "messages": [
             "My iPhone's news app buzzes me all day. I need my text messages and calendar alerts to keep working, so I only want to stop the news app. How?",
             """You can change this for one app at a time, so your other apps will not be touched.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Tap the news app.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

Only the news app goes quiet. Your messages and calendar keep sending alerts the way they do now.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
         "messages": [
             "My iPhone keeps showing alerts from a coupon app. How do I stop them?",
             """You can turn them off for just that app.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Tap the coupon app.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.""",
             "I tapped the coupon app but I don't see Notifications there.",
             """Let's check two things.

1. Go back to the **Apps** list in **Settings** and make sure you tapped the coupon app itself.
2. If you are in the right app and still don't see **Notifications**, that app may not be able to send notifications at all.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-081', "task_type": 'app_notifications_off', "task": 'Turn off notifications from an app',
    "platform": 'Android', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Android Help: Control notifications on Android', "url": 'https://support.google.com/android/answer/9079661?hl=en'},
    "source_notes": """Settings path: open Settings, tap Notifications, then App notifications. Under Most recent (or All apps in the dropdown), tap the app and turn its notifications off.
From a notification: swipe down, touch and hold the notification, tap the Settings icon, turn off All notifications.
Categories: on the app's page, tap a category to see more options, then turn off the categories you don't want.
Snooze only hides temporarily. Silent: notifications don't make sound or vibrate but still appear when you swipe down (Settings, Notifications, pick app, tap notification type, choose Silent; or touch and hold a notification, tap Settings, choose Silent, tap Apply).
Versions: Most recent list is on newer Android; on older versions tap App notifications and then choose an app.
Troubleshooting: settings vary by phone, check manufacturer's support page if menus differ.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "On my Android phone, my pharmacy app sends both sale ads and refill reminders. I want to keep the refill reminders and stop only the ads. Can I do that?",
             """Yes. You can turn off just the kinds of alerts you don't want.

1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Tap the pharmacy app.
4. Tap a **category** to see more options.
5. Turn off the categories you don't want, like the ads.

Leave the refill reminder category turned on. Menu names can vary a little on different phones.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "How can I turn off notifications for a weather app on my Android phone?",
             """You can turn them off for just that app.

1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Under **Most recent**, tap the weather app.
4. Turn its notifications off.""",
             "The weather app isn't in that list.",
             """The list may only show recent apps. Try this:

1. In **App notifications**, tap the dropdown near the top and choose **All apps**.
2. Tap the weather app and turn its notifications off.

On an older Android version, there is no recent list. Tap **App notifications**, then choose the app.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-082', "task_type": 'browser_zoom', "task": 'Make a web page bigger',
    "platform": 'Chrome (computer)', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Google Chrome Help: Change text, image & video sizes (zoom), computer', "url": 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop'},
    "source_notes": """Zoom one page from the menu: open Chrome, at top right click More, next to Zoom use Zoom in (larger), Zoom out (smaller), or Full screen.
Shortcuts: larger Ctrl and + (Windows, Linux, Chrome OS), Command and + (Mac); smaller Ctrl and - / Command and -.
Reset zoom for specific sites: Chrome, More, Settings, Privacy and security, Site Settings, Additional content settings, Zoom levels, click X next to a site to remove its resize settings.
Change for all pages: More, Settings, Appearance. Page zoom: click the down arrow next to Page zoom and select an option (resizes everything). Font size only: click the down arrow next to Font size and select a size; more options under Customize fonts.
Some websites don't let browsers change only the text size, so Chrome can't adjust font size on those sites.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
         "messages": [
             "I use Chrome on my Windows laptop. I want the words bigger on every website, but I don't want the pictures and buttons to get bigger too, it messes up the layout. Is there a way?",
             """Yes. Chrome has a setting for the text size only.

1. Open Chrome and click **More** at the top right.
2. Click **Settings**.
3. Click **Appearance**.
4. Click the down arrow next to **Font size** and pick a size.

This changes the words and leaves the page size setting alone. Do not use **Page zoom**, because that makes everything bigger.

Some websites don't let Chrome change only the text size, so on those sites the words may stay the same.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
         "messages": [
             "How do I zoom in on one website in Chrome on my computer?",
             """You can zoom in from the menu.

1. Open Chrome and go to the website.
2. Click **More** at the top right.
3. Next to **Zoom**, click **Zoom in**. Click it again to go bigger.

You can also hold **Ctrl** and press **+**. To go smaller, use **Zoom out** or hold **Ctrl** and press **-**.""",
             "I made that site way too big and now it opens huge every time. How do I put it back?",
             """Chrome remembers the size for each site. You can clear it:

1. Click **More**, then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Additional content settings**, then **Zoom levels**.
4. Click the **X** next to that site.

That removes the saved size for the site.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-083', "task_type": 'find_downloads', "task": 'Find a downloaded file',
    "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Microsoft Support: Find my downloads in Windows', "url": 'https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8'},
    "source_notes": """Find downloads in File Explorer: 1 Press Windows logo key + E to open File Explorer (or select it from taskbar or Start menu). 2 Select Home in the left navigation pane. 3 Look for Downloads among the pinned folders in Quick access. In Windows 11 version 22H2 and later Downloads is pinned there by default. In Windows 11 22H2 or later, Downloads no longer appears under This PC.
Troubleshooting: Downloads missing from Quick access: select Home, select the Up arrow beside the address bar, right-click Downloads, select Pin to Quick access. Left navigation pane hidden: select View, then Show, then Navigation Pane. Find a file by name: search from Home; to include cloud files sign in to your cloud account from Start > Settings > Accounts. Files look hidden or unfamiliar: View > Show, turn on File name extensions or Hidden items.
Page does not cover Edge downloads, Ctrl+J, or changing download location.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
         "messages": [
             "I'm on Windows 11 and I saved a tax paper last week but I can't remember where. All I remember is the name started with 'W2'. I don't want to open folder after folder. Can I just search for it?",
             """Yes. You can search by name instead of opening folders.

1. Press the **Windows logo key** and **E** together to open File Explorer.
2. Select **Home** in the left pane.
3. In **Home**, search for the file by the name you remember.

The search looks for relevant files on your PC and in your cloud accounts.

On Windows 11 version 22H2 or later, **Downloads** is pinned under **Quick access** on **Home**, so you can open it too.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
         "messages": [
             "Where do I find the picture I just downloaded on my Windows 11 computer?",
             """It is most likely in your **Downloads** folder.

1. Press the **Windows logo key** and **E** together to open File Explorer.
2. Select **Home** in the left pane.
3. Under **Quick access**, open **Downloads**.
4. Look for your picture in the list.

On Windows 11 version 22H2 or later, **Downloads** is pinned there by default.""",
             "My File Explorer doesn't have a list on the left side.",
             """The left pane may be hidden. You can turn it back on:

1. In File Explorer, select **View**.
2. Select **Show**.
3. Select **Navigation Pane**.

Then select **Home** and open **Downloads** under **Quick access**.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-084', "task_type": 'mouse_pointer_size', "task": 'Make the mouse pointer bigger',
    "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
    "source": {"title": 'Microsoft Support: Make Windows easier to see', "url": 'https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see'},
    "source_notes": """Section 'Know where you're pointing': make your mouse more visible by changing the color and size of the mouse pointer. Select the Start button, then Settings > Accessibility > Mouse pointer & touch, and choose the options that work best for you. (Page does not name a size slider or style list.)
Pointer trails: Start, Settings > Accessibility > Mouse pointer & touch, turn on Mouse pointer trails; trails show where the mouse is moving.
Touch indicator: same place, turn on Touch indicator; expand its settings and select Make the circle darker and larger checkbox.
Related, not needed for pointer: Text size is Settings > Accessibility > Text size (slider enlarges only text); Scale is Settings > System > Display. No troubleshooting.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
         "messages": [
             "I have Windows 11. I only want the little arrow to be bigger. Please don't change my text or the size of everything else on the screen, I just got it the way I like it.",
             """You can change just the pointer. Your text and screen size will stay as they are.

1. Click the **Start** button, then click **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Choose the options that change the pointer's color and size, and pick what works best for you.

Leave the **Text size** and **Display** settings alone, because those change other things on your screen.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
         "messages": [
             "How can I see my mouse pointer better on Windows 11? It's too small.",
             """You can change how the pointer looks.

1. Click the **Start** button, then click **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Choose the options that change the pointer's color and size.""",
             "It's bigger now, but I still lose it when I move the mouse fast.",
             """Pointer trails can help you follow it.

1. Go back to **Settings**, then **Accessibility**, then **Mouse pointer & touch**.
2. Turn on **Mouse pointer trails**.

Now you will see a trail that shows where the mouse is moving on the screen.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-085', "task_type": 'two_step_verification', "task": 'Turn on 2-Step Verification',
    "platform": 'Google Account', "category": 'online_services', "sensitive": True,
    "source": {"title": 'Google Account Help: Turn on 2-Step Verification', "url": 'https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop'},
    "source_notes": """Computer steps: 1 Open your Google Account at myaccount.google.com. 2 Select Security & sign-in. 3 Under How you sign in to Google, select Turn on 2-Step Verification. 4 Follow the on-screen steps.
Conditions: if you use a work, school or other group account these steps might not work; contact your administrator. Advanced Protection Program users can't download backup codes.
After setup: signing in with a password requires a second step; signing in with a passkey skips it. Adding a phone number: Google may take up to 7 days to trust it. Prompts: push notification on Android phones signed in, or iPhones with Gmail, Google Photos, YouTube or Google app; tap Yes to allow or No to block; may ask for PIN.
Other second steps: passkeys, security keys, Google Authenticator (works without internet or mobile service), text or voice codes (more vulnerable to phone number hacks), backup codes (8-digit, keep somewhere safe).
Trusted devices: check Don't ask again on this computer only on devices you use regularly and don't share.
Suspicious new phone number: Google disables it and notifies you; 30 days to confirm or it is deleted. Page does not say how to turn off or check status.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Account",
         "messages": [
             "I want to turn on 2-Step Verification for my Google account on my home computer. Only I use this computer, and I get tired of typing codes, so I don't want to be asked every single time I sign in here. What should I do?",
             """You can turn it on and tell Google not to ask again on your own computer.

1. Go to **myaccount.google.com** on your computer and sign in.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

When you are asked for a second step, check **Don't ask again on this computer**. Only do that on a computer you use regularly and don't share with anyone, like your home computer.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Account",
         "messages": [
             "my gmail keeps asking me about a second step thing, I'm on my laptop, how do I get that set up properly?",
             """You can do it from your Google Account page.

1. Go to **myaccount.google.com** and sign in.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

If you use a work or school account, these steps might not work.""",
             "I'm on my school email and there's no Turn on 2-Step Verification button.",
             """That is likely because it is a school account. Those steps might not work for a work, school, or other group account.

1. Contact the administrator who manages the account.
2. Ask them about 2-Step Verification for your account.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-086', "task_type": 'phishing_email', "task": 'Is this email asking me to log in real?',
    "platform": 'email', "category": 'online_services', "sensitive": True,
    "source": {"title": 'FTC Consumer Advice: How to Recognize and Avoid Phishing Scams', "url": 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams'},
    "source_notes": """Signs: unexpected messages that look like they are from a company you know; scammers may claim a problem with your account or payment info; generic greetings, billing problem notices, invitations to click a link to update payment details. Legitimate companies won't email or text with a link to update your payment information.
What to do: ask whether you have an account with the company or know the sender. If not, it could be phishing: review warning signs, report it, delete it. If so, contact the company using a phone number or website you know is real, not the info in the message. Attachments and links might install harmful malware.
Protect: security software set to update automatically; phone software automatic updates; multi-factor authentication; back up data.
If you responded or clicked: credit card payments go to the card issuer (use the number on the back of the card; ask for a refund). If a scammer used your Social Security number, go to IdentityTheft.gov to report it. If you gave a scammer access to your computer or phone, update your security software, run a scan, and delete anything it identifies as a problem.
Report: phishing email forward to reportphishing@apwg.org (Anti-Phishing Working Group); phishing text forward to SPAM (7726); report to the FTC at ReportFraud.ftc.gov.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "email",
         "messages": [
             "An email says my payment info for my streaming service is out of date and my account will be closed in 24 hours unless I click the link. I can't call anyone until Monday, it's Saturday. Should I just click it to be safe?",
             """Please don't click the link. Real companies won't email you a link to update your payment information.

1. Do not click anything in the email. Report it now, as in step 3.
2. To check your streaming account, contact the company using a website or phone number you already know is real, not anything in the email.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

Links and attachments in a scam email can also install harmful software.""",
         ]},
        {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "email",
         "sources": [{"title": 'FTC Consumer Advice: How to Recognize and Avoid Phishing Scams', "url": 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams', "accessed": '2026-11-13'},
                     {"title": 'FTC Consumer Advice: What To Do if You Were Scammed', "url": 'https://consumer.ftc.gov/articles/what-do-if-you-were-scammed', "accessed": '2026-11-13'}],
         "messages": [
             "I clicked the link in an email that said it was from my bank, and I typed in my credit card number. Now I think it was fake. What do I do?",
             """Thank you for telling me. Please act on this right away, starting with your credit card company.

1. Call your credit card company right away, using the number on the back of your card, and tell them you gave your card number to a scammer. Ask them to refund any charges.
2. If a scammer used your Social Security number, go to **IdentityTheft.gov** to report it.
3. If you gave a scammer access to your computer or phone, update your security software to make sure you have the latest protections. Then run a scan and delete anything it identifies as a problem.
4. Report the email at **ReportFraud.ftc.gov**, and forward it to **reportphishing@apwg.org**.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-087', "task_type": 'report_spam_text', "task": 'Report a spam text message',
    "platform": 'phone', "category": 'online_services', "sensitive": True,
    "source": {"title": 'FTC Consumer Advice: How to Recognize and Report Spam Text Messages', "url": 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages'},
    "source_notes": """Recognize: scammers send fake texts to get personal or financial info; legitimate companies won't ask for information about your account by text. Common lures: fake prize, gift card or coupon offers; false alerts about account activity or payments; fake invoices; fake package delivery notices.
What to do: don't click links in an unexpected text that asks for personal or financial info. If it might be real, contact the company using a phone number or website you know is real, not the details in the text. (Page does not say whether to reply.)
Filter/block: your phone may have an option to filter and block spam or messages from unknown senders; ask your wireless provider about tools that block calls and texts; some call-blocking apps also block texts.
Report: forward to 7726 (SPAM): copy the message and forward it to 7726; this helps your provider block similar messages. Report in your messaging app: look for an option to report junk or spam (iPhone and Android: page links to Apple and Google instructions, no steps on the page). Report at ReportFraud.ftc.gov.
If you already clicked or replied: page doesn't give steps; warns links can lead to spoofed websites that look real where logging in can expose your username and password, and some messages install malware that steals information.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "phone",
         "messages": [
             "I get fake package delivery texts. I don't know how to copy a text and send it to another number, and I don't use a computer. Is there another way to report them?",
             """Yes. You do not have to copy and forward the text. Please don't click any link in it.

1. Open the text in your messaging app and look for an option to **report junk or spam**.
2. If you are able to open web pages on your phone, you can also report it at **ReportFraud.ftc.gov**.
3. Ask your phone company about tools that block unwanted texts.

Real delivery companies don't ask for your account information by text. If you think a delivery might be real, contact the company using a phone number or website you know is real, not the one in the text.""",
         ]},
        {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "phone",
         "messages": [
             "I tapped the link in a text that said my package was delayed. A page came up asking me to log in, so I closed it right away without typing anything. Did I do something bad?",
             """You did the right thing by closing it. Please don't open that link again.

1. Don't type any information into that page if you open it again by accident.
2. If you think the package could be real, contact the company using a phone number or website you know is real, not the details in the text.
3. Forward the text to **7726** (SPAM), and report it at **ReportFraud.ftc.gov**.

Links in scam texts can lead to fake websites that look real, and some can install harmful software. Closing the page right away without typing anything is a good move.""",
         ]},
    ],
})

TASKS.append({
    "task_id": 'TR-088', "task_type": 'romance_scam', "task": 'Online friend asks for money',
    "platform": 'any', "category": 'online_services', "sensitive": True,
    "source": {"title": 'FTC Consumer Advice: What You Need to Know About Romance Scams', "url": 'https://consumer.ftc.gov/articles/what-know-about-romance-scams'},
    "source_notes": """Signs: they want to move off the platform quickly (email, call, message off the platform); say they live far away often for work or military; declare strong feelings early; chat often to build trust; ask for money, often urgent.
If you suspect: talk to someone you trust; reverse image search the person's profile picture (page gives no meaning for the result); search online for the person's job plus scammer.
How they ask for payment: claim they can't meet in person; ask for money for medical bills, plane tickets, visas, fees, or crypto investing; hard to reverse methods: wire transfers (Western Union, MoneyGram), gift cards with PIN codes, money transfer apps, cryptocurrency; push for fast payment.
Already paid: contact the company or your bank right away, say you paid a scammer, ask for a refund (same instruction for gift card, wire transfer, credit/debit card, crypto).
Report: ReportFraud.ftc.gov; notify the social networking site or app where you met the scammer. No phone numbers on page.
Avoid: never send money or gifts to a sweetheart you haven't met in person.""",
    "examples": [
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
         "messages": [
             "A man I met on a dating site wants me to move our chats to email, and now he says he needs money for a visa so he can visit me. He asked me not to tell my kids because they won't understand. I really do care about him. What should I do?",
             """Please don't send him any money. Never send money or gifts to someone you haven't met in person.

What you describe matches signs of a romance scam: asking to move off the site and asking for money for a visa.

1. Talk to someone you trust about what is happening.
2. Do a reverse image search of his profile photo. This is a search that finds other places online where the same photo appears.
3. Report it at **ReportFraud.ftc.gov**, and tell the dating site.

I know this is hard when you care about someone.""",
         ]},
        {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
         "messages": [
             "I already sent $500 in gift cards to a man I met online. I read the PINs to him over the phone. Now he wants more. What do I do?",
             """Please don't send him anything more, and stop talking to him. 

1. Contact the gift card company right away. Tell them you paid a scammer and ask for a refund.
2. Report it at **ReportFraud.ftc.gov**.
3. Tell the site or app where you met him.
4. Talk to a trusted friend or family member about what happened.

Gift cards are one of the hard-to-reverse ways scammers ask for money, so acting quickly matters.""",
         ]},
    ],
})
