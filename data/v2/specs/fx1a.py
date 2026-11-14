"""Fill batch fx1a: new examples for TR-001 to TR-006."""
TASKS = []

TASKS.append({
    "task_id": "TR-001", "task_type": "text_size", "task": "Make text bigger",
    "platform": "Samsung Galaxy", "category": "technical_support", "sensitive": False,
    "source": {"title": "Samsung Support: How to adjust the font size and style on your Galaxy phone", "url": "https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/"},
    "source_notes": """Change font size and style: 1. Launch the Settings app, select Display. 2. Select Font size and style. 3. Here you can adjust the options as desired. Intro: you can pick a font size or style that works for you; make the font appear small, big, or make it bold. The page does NOT mention a slider, Apply/Done, Zoom, Easy mode.
Font style: Font style > Download fonts (opens Galaxy Store) > Install icon next to a font. Downloading over mobile data may incur charges; Wi-Fi recommended for large downloads.
High contrast fonts: Settings > Accessibility > Visibility enhancements > switch next to high contrast fonts.
Troubleshooting: Device screenshots and menu may vary depending on device model and software version. Samsung Support options: Live Chat, Call, Email, Service Centers.""",
    "examples": [
        {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
         "messages": [
             """Hello, my daughter gave me her old Samsung Galaxy phone last month and I am still getting used to it. My eyes are not what they were since the cataract surgery and I cannot read the recipes my friends send me, the writing is just too small. Could the words be made larger, and maybe darker too?""",
             """Yes, you can make the words larger and bolder in the Settings. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. You can also choose to make it bold, which makes the letters darker and thicker.

Try one change at a time so you can see what suits your eyes. Menu names can look a little different depending on the phone model and software version.""",
         ]},
        {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
         "messages": [
             "everything on my phone is written so small now, is there a way to make it bigger",
             "I can help with that. Is your phone an **iPhone**, a **Samsung Galaxy**, or another kind of phone?",
         ]},
        {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
         "messages": [
             "everything on my phone is written so small now, is there a way to make it bigger",
             "I can help with that. Is your phone an **iPhone**, a **Samsung Galaxy**, or another kind of phone?",
             "its a samsung galaxy",
             """Good, here is how to make the writing bigger on a Samsung Galaxy.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. You can also make it bold.

If you don't see **Font size and style**, the menus can be a little different on some models. Tell me what you see after tapping **Display** and I'll help.""",
         ]},
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
         "messages": [
             """I have a Samsung Galaxy and the print is too small for me. My grandson told me I could download special fonts but I do not want to download anything or pay for anything, I just want the same letters to look bigger. What do I do?""",
             """You don't need to download anything. The size can be changed right in your settings, and it's free.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. Leave **Font style** alone, because that is the part that downloads new fonts.

Your letters will keep the same look, just bigger.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
         "messages": [
             "How do I make the writing bigger on my Samsung Galaxy phone?",
             """Here is how to make the writing bigger on your Samsung Galaxy.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Font size and style**.
4. On that screen, adjust the options to make the font bigger. You can also make it bold.

The menus can look a little different depending on your phone model and software version.""",
             "I tapped Display but I do not see anything called Font size and style.",
             """That can happen, because the menus can look different depending on the phone model and software version. Samsung Support can help you directly. You can use Live Chat or Email, or use Find a Support Center to visit someone in person.""",
         ]},
    ],
})

TASKS.append({
    "task_id": "TR-002", "task_type": "ring_volume", "task": "Turn up ring volume (device unknown)",
    "platform": "unknown", "category": "technical_support", "sensitive": False,
    "source": {"title": "Android Help: Change volume, sound & vibrate settings", "url": "https://support.google.com/android/answer/9082609?hl=en"},
    "source_notes": """Change volume (Android 12 or later): 1. Press a volume button. 2. Tap the Menu icon (labeled More) at the right. 3. Slide each level: Media volume, Call volume, Ring Volume, Notification volume, Alarm volume. Pressing a volume button changes whatever is playing; if nothing is playing, it changes media volume.
If you don't see Settings under the Menu, use the older-version steps. Older versions: press a volume button, tap the Down arrow at the right, choose Media, Ring, or Alarm; or Settings > Sound. If media volume dropped instead: tap the Down arrow, then slide Ring all the way left (i.e. left = quieter).
Vibrate or Mute: press a volume button, tap the Ring icon above the slider, tap Vibrate or Mute. To restore sound, turn off Vibrate or turn on Ring.
Change ringtone: Settings > Sound & vibration > Ringtone, pick one, tap Save.
Troubleshooting: some steps require Android 12 or later; if you can't find Settings under the Menu, use the older-version steps.""",
    "examples": [
        {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "I have a Google Pixel phone and I can't hear it ring from the other room. How do I make the ringer louder?",
             """You can turn the ringer up with the buttons on the side of your phone.

1. Press one of the **volume buttons** on the side of your phone.
2. A small volume bar appears on the screen. Tap the **Menu** icon at the right.
3. Find **Ring Volume** and slide it up to make the ring louder.

If you don't see a **Menu** icon, your phone has older software. Tap the **Down arrow** at the right instead, then slide **Ring**.

If your phone was set to vibrate or mute, tap the **Ring** icon above the slider, then turn off **Vibrate** or turn on **Ring** to bring the sound back.""",
         ]},
        {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (older version)",
         "messages": [
             """My phone is an older Android phone, the kind with the Google system, I think it is about six years old because my son bought it for me when I retired. The Menu thing at the side that people talk about does not show up on mine. I keep missing calls from the pharmacy when the phone is in my purse. How can I turn the ringing up?""",
             """Older Android phones do this in a slightly different way. Here is how to turn the ringing up.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Down arrow** at the right of the volume bar.
3. Find the **Ring** slider and slide it up to make calls ring louder.

If you would rather use the Settings app, you can also open **Settings** and tap **Sound**.""",
         ]},
        {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "My phone hardly makes any sound when someone calls and I keep missing calls from my doctor's office.",
             """I'm sorry you've been missing those calls. I can help you make the ringing louder.

First, one quick question: is your phone an **iPhone**, or another kind of phone, like a Samsung or Google Pixel?

If you're not sure, look at the back of the phone. An iPhone has an apple logo on the back.""",
             "no apple on the back, its a google pixel",
             """Thank you. A Pixel is an Android phone, so here is how to make the ringing louder.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up.

If your phone was set to vibrate or mute, tap the **Ring** icon above the slider and turn off **Vibrate** or turn on **Ring**.""",
         ]},
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
         "messages": [
             """I have an Android phone, a Google Pixel. I get lost whenever I go into the Settings app, so please do not send me there. Is there any way to make the ring louder using just the buttons on the side of the phone?""",
             """Yes, you can do it without opening the Settings app.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up to make the ring louder.

If you don't see a **Menu** icon, your phone may be an older version. Tell me and I'll give you the steps for that.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
         "messages": [
             "My Android phone's ring is too quiet. How do I make it louder?",
             """You can turn the ring up with the buttons on the side of your phone.

1. Press one of the **volume buttons** on the side of your phone.
2. Tap the **Menu** icon at the right of the volume bar.
3. Find **Ring Volume** and slide it up.

If you don't see the **Menu** icon, your phone may be an older version, and I can give you different steps.""",
             "I pressed the button and a little bar came up but I do not see any Menu icon, just a little arrow.",
             """That means your phone is an older version. Try these steps.

1. Press one of the **volume buttons** on the side again.
2. Tap the **Down arrow** at the right of the bar.
3. Find the **Ring** slider and slide it up to make calls ring louder.""",
         ]},
    ],
})

TASKS.append({
    "task_id": "TR-003", "task_type": "send_photo_text", "task": "Send a photo by text message",
    "platform": "Android (Google Messages)", "category": "communication", "sensitive": False,
    "source": {"title": "Google Messages Help: Send photos, videos, or voice messages", "url": "https://support.google.com/messages/answer/6159880?hl=en"},
    "source_notes": """Send photos, videos, or GIFs: 1. Open Google Messages. 2. Open or start a conversation. 3. Tap Gallery. 4. Select a file or take a picture. 5. (Optional) Tap HD or HD+ to change media quality: HD (Optimized for chat) sends faster and uses less data; HD+ (Original quality) sends at full resolution. 6. Tap Send.
What you see: an image preview where you can change quality; the option you choose is saved for future images, and you can change it for each new attachment.
Notes: Messages needs permission to send/receive files. Use RCS rather than MMS for clearer images because carriers compress MMS. Photos taken in Google Messages are not saved on the device. Page gives no steps for multiple photos at once. Some steps need Android 6.0 or later.""",
    "examples": [
        {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Google Messages)",
         "messages": [
             """My grandson just graduated and my neighbor took a lovely picture of the two of us in front of the stage. She put it on my phone and now I want to text it to my son who lives in Denver. I have a Samsung phone and I use the Google Messages app for all my texting. My son says I just never send pictures, so I want to learn. What do I press?""",
             """Congratulations to your grandson. Here is how to text that picture from the Messages app.

1. Open the **Messages** app.
2. Open your conversation with your son. If you haven't texted him before, start a new conversation with him.
3. Tap **Gallery**.
4. Tap the picture of you and your grandson.
5. Look at the preview of the picture. You can leave the quality as it is.
6. Tap **Send**.

You will see the picture in your conversation once it has gone through.""",
         ]},
        {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
         "messages": [
             "my daughter wants me to text her the picture of the baby. how do i do that",
             "I'd be glad to help you send it. Is your phone an **iPhone** or an **Android** phone?",
         ]},
        {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
         "messages": [
             "my daughter wants me to text her the picture of the baby. how do i do that",
             "I'd be glad to help you send it. Is your phone an **iPhone** or an **Android** phone?",
             "android, and i use the messages app",
             """Good, here is how to send the picture in the Messages app.

1. Open the **Messages** app.
2. Open your conversation with your daughter. If you haven't texted her before, start a new conversation with her.
3. Tap **Gallery**.
4. Tap the picture of the baby.
5. Tap **Send**.

The picture will show up in your conversation once it is sent.""",
         ]},
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
         "messages": [
             """I want to text a picture of my tomato plants to my brother using the Messages app on my Android phone. I am away from home and my data is nearly used up for the month, so I do not want it to use more data than it has to. Can I still send it?""",
             """Yes. Messages has a quality choice that sends faster and uses less data.

1. Open the **Messages** app.
2. Open your conversation with your brother.
3. Tap **Gallery**.
4. Tap the picture of your tomato plants.
5. On the preview, tap **HD+** or **HD** to change the quality. Choose **HD**, which says "Optimized for chat". It sends faster and uses less data.
6. Tap **Send**.

Your phone remembers the choice for your next pictures, and you can change it again for any new picture.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Google Messages)",
         "messages": [
             "I use the Messages app on my Android phone. How do I text a photo of my new puppy to my friend Carol?",
             """Here is how to send the photo in the Messages app.

1. Open the **Messages** app.
2. Open your conversation with Carol. If you haven't texted her before, start a new conversation with her.
3. Tap **Gallery**.
4. Tap the photo of your puppy.
5. Tap **Send**.

You'll see the photo in your conversation once it's sent.""",
             "It went through but Carol says the picture looks blurry. Can I send it better?",
             """Yes. Messages can send the picture in its full original quality. Send it again like this.

1. Open your conversation with Carol.
2. Tap **Gallery**.
3. Tap the photo of your puppy.
4. On the preview, tap **HD** and choose **HD+**, which says "Original quality".
5. Tap **Send**.

Pictures sent as old-style picture messages (called MMS) get squeezed by phone companies, which makes them blurrier. Messages that go through as RCS chats come out clearer.""",
         ]},
    ],
})

TASKS.append({
    "task_id": "TR-004", "task_type": "screenshot", "task": "Take a screenshot",
    "platform": "iPhone", "category": "technical_support", "sensitive": False,
    "source": {"title": "Apple Support: Take a screenshot on your iPhone", "url": "https://support.apple.com/102616"},
    "source_notes": """iPhone with Face ID: 1. Press the side button and the volume up button at the same time. 2. Release both buttons quickly. 3. Edit, share, or save the screenshot. On iOS 18 or earlier a thumbnail appears in the lower-left corner.
iPhone with Home button and Touch ID: 1. Press the side button and the Home button at the same time. 2. Release both quickly. 3. Same.
iPhone with top button and Home button: press the top button and the Home button together, release quickly.
After capture: iOS 26: screenshot appears right away with quick tools (Markup to draw, crop, send to apps or contacts, save button to choose where it is stored). iOS 18 and earlier: thumbnail briefly in lower-left corner; tap it to open, swipe left to dismiss.
Find screenshots: open Photos, go to Collections, tap Media Types, tap Screenshots.
Troubleshooting: if nothing happens, make sure both buttons are pressed together and released quickly. If you do not see a thumbnail, check the iOS version: iOS 26 shows quick tools instead. Only a two-button method is given; no one-button alternative on the page.""",
    "examples": [
        {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
         "messages": [
             "My iPhone has no home button, you just look at it to unlock it. How do I take a screenshot of my boarding pass?",
             """On your iPhone you take a screenshot with two buttons on the sides.

1. Open the screen you want to capture, such as your boarding pass.
2. Press the **side button** and the **volume up button** at the same time.
3. Let go of both buttons quickly.

On iOS 18 or earlier, a small picture of your screenshot appears in the lower-left corner for a moment. On iOS 26, the screenshot appears right away with tools you can use.

You can find it later in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.""",
         ]},
        {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone (older model)",
         "messages": [
             """Hi there, I have an old iPhone that my husband had before he passed, it has a round button at the bottom of the screen and a button on the very top edge, there is nothing on the right side. I want to save a recipe from a website to show my sister. Someone said a screenshot does that. How do I take one on this phone?""",
             """A screenshot is a good way to keep that recipe. On your iPhone you use the button on the top edge and the round button together.

1. Open the website so the recipe is on the screen.
2. Press the **top button** and the **Home button** (the round button) at the same time.
3. Let go of both buttons quickly.

Your recipe is now saved as a picture. You can find it in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.""",
         ]},
        {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone (Home button)",
         "messages": [
             "How do I take a picture of what's on my iPhone screen? My grandson wants me to send him a screenshot.",
             """Happy to help. The buttons you press depend on your iPhone model, so one quick question first: is the button that wakes your iPhone on the **top edge** or on the **right side**?""",
             "its on the right side, and there is a round button under the screen too",
             """Thank you. Here is how to take the screenshot on your iPhone.

1. Open the screen you want to send to your grandson.
2. Press the **side button** and the **Home button** (the round button) at the same time.
3. Let go of both buttons quickly.

You can find it later in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.""",
         ]},
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone (Face ID)",
         "messages": [
             """I have an iPhone with Face ID, no home button. I want a screenshot of a text message but my hands shake and arthritis makes it hard to press two buttons at once. Is there a way to take a screenshot with just one button?""",
             """I'm sorry, the only way I can give you is the two-button way. I don't have a one-button way to take a screenshot. Here it is, in case you want to try it.

1. Open the text message you want to capture.
2. Press the **side button** and the **volume up button** at the same time.
3. Let go of both quickly.

It is a short press, not a long hold. You do not need to keep the buttons down.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone (Face ID)",
         "messages": [
             "I have a newer iPhone with Face ID. How do I take a screenshot?",
             """Here is how to take a screenshot on your iPhone.

1. Open the screen you want to capture.
2. Press the **side button** and the **volume up button** at the same time.
3. Let go of both buttons quickly.

You can find your screenshots later in **Photos**. Tap **Collections**, then **Media Types**, then **Screenshots**.""",
             "i pressed them but i didnt see a little picture in the corner like my friend said",
             """That is likely fine. Here is how to check.

1. Look in the lower-left corner right after you press. On iOS 18 or earlier, the little picture only shows for a moment. On iOS 26, there is no little picture. The screenshot appears right away with tools like drawing and cropping.
2. Open **Photos**, tap **Collections**, then **Media Types**, then **Screenshots**. Your screenshot should be there.
3. If it is not there, try again. Press the **side button** and the **volume up button** together, and let go quickly.""",
         ]},
    ],
})

TASKS.append({
    "task_id": "TR-005", "task_type": "email_not_working", "task": "Email stopped working (details unknown)",
    "platform": "unknown", "category": "communication", "sensitive": False,
    "source": {"title": "Gmail Help: Gmail won't load", "url": "https://support.google.com/mail/answer/7074871?hl=en"},
    "source_notes": """The page covers only browser-based Gmail on a computer. No steps for the Gmail apps on phones.
Before you start: check Gmail's status in the Google Workspace Status Dashboard.
Check your browser: 1. Use a supported browser; update your browser to the latest version; if problems continue, try another browser. 2. Check extensions and applications: turn off extensions and uninstall applications one at a time, reopening Gmail after each change to see if it is fixed; if available, try incognito or private browsing mode. 3. Clear your browser's cache and cookies, then open Gmail again.
Check your internet connection: 1. Restart your device. 2. Turn your Wi-Fi or mobile data off, then back on. If Gmail still will not load on Wi-Fi, restart your router (router manual has instructions). 3. Connect to a different network. If connectivity problems continue, contact your service provider or your Wi-Fi network host.
Try another device: Gmail may not load in browsers on older devices; try another device.""",
    "examples": [
        {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Gmail (computer browser)",
         "messages": [
             "I read my Gmail in a web browser on my computer and the page will not load today. What should I try?",
             """Let's try a few things, starting with the easiest.

1. Make sure your browser is up to date. Update it to the latest version.
2. Open Gmail again.
3. If it still will not load, try a different browser and open Gmail there.
4. Clear your browser's saved website data (called cache and cookies), then open Gmail again.

If Gmail still will not load, tell me and we'll check your internet connection next.""",
         ]},
        {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Gmail (computer browser)",
         "messages": [
             """My nephew put a bunch of add-ons into my web browser last summer, some coupon thing and a shopping helper and I don't know what else. Ever since then, when I go to Gmail on my desktop computer, the page just sits there and never opens. My internet is fine because I can read the news. I don't want to call him again. What could be causing it and how do I fix it?""",
             """Those add-ons (called extensions) could be the cause. You can check them one at a time.

1. Turn off one extension in your browser.
2. Open Gmail again and see if it loads.
3. If it still does not load, turn off the next extension and open Gmail again. Repeat until Gmail loads.

You can also try a private browsing window, if your browser has one (it may be called incognito), and open Gmail there.

If you turn off an extension and Gmail loads, that extension was the cause.""",
         ]},
        {"suffix": "d", "scenario": "followup", "style": "verbose", "specification": "fully_specified", "platform": "Gmail (computer browser)",
         "messages": [
             "Good morning. I hope you can help me. My husband always took care of these things. Since about Tuesday the Gmail page will not open for me, it just sits there. I tried turning it off and on.",
             """Good morning. I'm glad you asked, and we can figure this out together. Turning it off and on was a good first try.

So I can give you the right steps, **do you open Gmail in a web browser on a computer**, or in an app on a phone or tablet?""",
             "i open it in the browser on my computer",
             """Thank you, that helps. Here are some things to try for Gmail on your computer.

1. Update your browser to the latest version, then open Gmail again.
2. If it still does not load, try a different browser.
3. Restart your computer and open Gmail again.
4. Turn your Wi-Fi off, then back on, and open Gmail again.

If none of that works, tell me what happens and we'll try the next step.""",
         ]},
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail (computer browser)",
         "messages": [
             """Gmail will not open on my laptop in my web browser. The last time I deleted a program, the whole computer went wrong, so please do not tell me to uninstall anything or take any programs off. I only want to try the gentle things. Which ones are those?""",
             """Here are gentle things to try. None of them remove any programs.

1. Update your browser to the latest version, then open Gmail again.
2. Try a different browser and open Gmail there.
3. Restart your laptop and open Gmail again.
4. Turn your Wi-Fi off, then back on, and open Gmail again.

If your browser has a private window (it may be called incognito), you can open Gmail there too.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail (computer browser)",
         "messages": [
             "Gmail won't open in the browser on my computer. I think it might be my internet. What do I check?",
             """Let's check your internet connection.

1. Restart your computer.
2. Turn your Wi-Fi off, then back on.
3. Open Gmail again.

If it still will not load, tell me and we'll try the next step.""",
             "I did both of those and Gmail is still stuck. my husband said something about the router",
             """Your husband is right, the router is the next thing to try.

1. Restart your router. The router's manual has instructions on how.
2. Open Gmail again.
3. If it still will not load, connect to a different network, if you have one nearby, and open Gmail there.

If the connection keeps having trouble, contact your internet service provider, or whoever runs your Wi-Fi network.""",
         ]},
    ],
})

TASKS.append({
    "task_id": "TR-006", "task_type": "printer_not_printing", "task": "Printer will not print",
    "platform": "unknown", "category": "technical_support", "sensitive": False,
    "source": {"title": "Microsoft Support: Fix printer connection and printing problems in Windows", "url": "https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73"},
    "source_notes": """Windows 11 can first run the troubleshooter in Get Help (via a link on the page); Windows 10 skips that.
General troubleshooting (both): Step 1 Restart the printer: turn off the printer and unplug it, wait 30 seconds, plug it back in, turn it on.
Step 2 Check the connection. Wired: confirm the USB cable is firmly connected at both ends. Wireless: turn on the printer's wireless option (look for a blue wireless icon or a menu option), then run the printer's built-in wireless test; if that passes but the problem continues, check whether the PC is online. With extenders, access points, or multiple SSIDs the PC must be on the same network as the printer. If the printer shows "Printer in error state", check for low ink or paper, an open cover, or a paper jam.
Step 3 Remove and reinstall: Remove: Start > Settings > Bluetooth & devices > Printers & scanners; select the printer, select Remove; select Yes. Reinstall automatically: same page, make sure printer is on and connected, select Add device (or Refresh); wait while Windows searches; if the printer appears select Add device next to it; if not select Add manually. Tip: print a test page to confirm it works; if not, check the manufacturer's website for troubleshooting or driver updates.
Step 4 install the latest driver from the manufacturer. Step 5 clear and reset the print spooler (Services). Step 6 offline status: separate article.""",
    "examples": [
        {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows",
         "messages": [
             "My printer is plugged into my Windows computer with a USB cable but nothing comes out when I press print. What should I check?",
             """Let's start with two simple things.

1. Turn off the printer and unplug it from the wall.
2. Wait 30 seconds.
3. Plug the printer back in and turn it on.
4. Check the USB cable. Make sure it is firmly connected at both ends, on the printer and on the computer.
5. Try printing again.

If your printer shows an error, check for low ink or paper, an open cover, or a paper jam.

If it still does not print, tell me and we'll try the next step.""",
         ]},
        {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11 (wireless printer)",
         "messages": [
             """We got a wireless printer a few years ago and I use it with my Windows 11 laptop from the sunroom. Last week the internet company sent a little box to make the Wi-Fi reach the back of the house and since then the printer will not print anything. I have a tax form to print. The printer lights are on. Please explain it simply, I am not very good with this.""",
             """The new Wi-Fi box could be the reason. Let's check the printer's wireless first.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. Look for a button on the printer that shows a blue wireless icon. Use it to make sure wireless is on.
5. Run the printer's built-in wireless test. Many printers have a menu option for it.
6. If the test passes but it still will not print, make sure your laptop is online.
7. Make sure your laptop is on the same Wi-Fi network as the printer. With a Wi-Fi box like the new one, the laptop can end up on a different network from the printer.
8. Try printing again.

If it still does not print, tell me what happens and we'll try the next step.""",
         ]},
        {"suffix": "d", "scenario": "followup", "style": "verbose", "specification": "fully_specified", "platform": "Windows",
         "messages": [
             "My printer won't print anything and I need to print my boarding pass for Thursday. It worked fine last month. The little green light is on.",
             """Let's get that boarding pass printed.

The next steps depend on what you're printing from. **Are you printing from a computer or from a phone?** If it's a computer, do you know if it's a Windows computer or a Mac?""",
             "its a windows computer",
             """Thank you. Let's try these steps for your Windows computer.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. If it connects with a USB cable, make sure the cable is firmly connected at both ends.
5. If it connects wirelessly, make sure the printer's wireless option is turned on. Look for a button on the printer that shows a blue wireless icon.
6. Try printing your boarding pass again.

If it still does not print, tell me and we'll try the next step.""",
         ]},
        {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows",
         "messages": [
             """The printer by my Windows computer stopped printing. My son warned me never to remove or reinstall the printer on the computer, because it took him hours to set up. So I want to stay away from the computer settings and only try things on the printer itself. It is connected by a USB cable. What can I do?""",
             """You can try these things right at the printer, without changing anything on the computer.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. Make sure the USB cable is firmly connected at both ends.
5. If the printer shows an error, check for low ink or paper, an open cover, or a paper jam.
6. Try printing again.

If that does not help, the next steps are on the computer, so you may want to ask your son before we try them.""",
         ]},
        {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
         "messages": [
             "My printer stopped printing from my Windows 11 computer. I already tried switching it off and on. What next?",
             """Let's check the connection and give the printer a longer restart.

1. Turn off the printer and unplug it.
2. Wait 30 seconds.
3. Plug it back in and turn it on.
4. If it uses a USB cable, make sure the cable is firmly connected at both ends.
5. If it connects wirelessly, make sure the printer's wireless option is on. Look for a button on the printer that shows a blue wireless icon.
6. Try printing again.""",
             "I did all that and it still won't print",
             """Next, let's remove the printer from your computer and add it again.

1. Click **Start**, then **Settings**, then **Bluetooth & devices**, then **Printers & scanners**.
2. Click your printer, then click **Remove**, then click **Yes**.
3. Make sure the printer is on and connected. On the same page, click **Add device**.
4. Wait while Windows searches. When your printer appears, click **Add device** next to it.
5. If it does not appear, click **Add manually**.
6. Click **Add a local printer or network printer with manual settings**, then click **Next**.
7. Click **Use an existing port**, pick the port your printer uses, then click **Next**.
8. Choose your printer's maker and model, then click **Next**.
9. Type a name, click **Next**, and choose **Do not share this printer**.
10. Click **Print a test page**, then click **Finish**.""",
         ]},
    ],
})
