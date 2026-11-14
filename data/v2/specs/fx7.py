"""Batch fx7: new examples (e constraint, r failure_recovery/already_acted) for tasks in ex7."""
TASKS = [
    {
        "task_id": "TR-089", "task_type": "government_impersonation", "task": "Caller claims to be from Social Security",
        "platform": "phone", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Advice: How To Avoid a Government Impersonation Scam", "url": "https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam"},
        "source_notes": """Government agencies never call, email, text, or message on social media to ask for money or personal information. They don't demand payment by wire, gift card, cryptocurrency, or payment app.
SSA: the real Social Security Administration won't threaten you or suspend your Social Security number; won't call, email, text, or message on social media and ask you to pay.
Signs of a scam: caller gives an employee ID number or knows your name or address to seem legitimate; demands immediate payment or personal information; threats of arrest, deportation, or suspended benefits or Social Security numbers; payment by gift card, wire, crypto, or payment app (hard to trace or recover); caller ID showing a real agency name (caller ID can be faked).
If you get a call: hang up or ignore it; don't give financial or personal information; if robocall don't press any numbers; hang up and call the agency directly at a number you know is correct; don't call back the number the caller gave or the one on caller ID; don't click links in unexpected messages.
SSA: call your local office directly; find the number at https://secure.ssa.gov/ICON/main.jsp.
Report: FTC at reportfraud.ftc.gov; your state attorney general; identity theft at IdentityTheft.gov; SSA impersonation to the SSA Office of the Inspector General at oig.ssa.gov.
If you already gave personal information: go to IdentityTheft.gov for steps to protect your identity. Report to FTC and state attorney general. The page has no method-specific recovery steps for payments (it only links to separate articles).""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "phone",
             "messages": [
                 """A man phoned and said he is with Social Security and my number is tied to fraud. He knew my name and my street address. He told me I must not tell my family or I could be arrested, and my caller ID really did say Social Security. He is going to call me back in an hour. Is this real?""",
                 """Please **do not give him anything**, and hang up if he calls again. This is a scam. The real Social Security Administration **won't threaten you** or suspend your Social Security number. Knowing your name and address, threats of arrest, and a real-looking caller ID are all tricks scammers use. Caller ID can be faked.

1. When he calls back, **hang up**. Don't share personal or bank information.
2. Don't call back the number he gave you or the one on your caller ID.
3. If you are worried, **call your local Social Security office yourself**. You can find the number at **secure.ssa.gov/ICON/main.jsp**.
4. **Report the call** at **reportfraud.ftc.gov**, and to the Social Security Office of the Inspector General at **oig.ssa.gov**.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "phone",
             "messages": [
                 """I feel so silly. A woman from Social Security said my number was being suspended, and I told her my Social Security number and my birthday before I got suspicious and hung up. What do I do now?""",
                 """Please don't feel silly. These callers are good at sounding real, and you did the right thing by hanging up. Here is what to do now.

1. Go to **IdentityTheft.gov** for steps to protect your identity.
2. **Report the call** to the FTC at **reportfraud.ftc.gov**.
3. Also report it to the Social Security Office of the Inspector General at **oig.ssa.gov**, and to your state attorney general.

If she calls again, hang up and don't call back the number she used. If you ever want to check on your account, call your local Social Security office using a number you find yourself.""",
             ]},
        ],
    },
    {
        "task_id": "TR-090", "task_type": "strong_passwords", "task": "Make a strong password",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts", "url": "https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts"},
        "source_notes": """Create a strong password: make it long, aim for at least 12 characters. Consider a passphrase of random words separated by spaces. Avoid common phrases, song lyrics, or movie quotes. If the account rejects long passwords, combine uppercase and lowercase letters, numbers, and symbols. Let your browser generate a password, or use a third-party password manager (check expert reviews; make the password for the manager strong too).
Storing: web browser, mobile browser, or password manager can save passwords.
Lock down email: strong password because reset links often go to your inbox.
Two-factor authentication: a hacker who steals your password still can't log in. Text or email passcodes are common, six digits or longer, expire, but least secure type. Authenticator app or security key is stronger if available.
Security questions: choose ones only you can answer; skip easy-to-find answers (zip code, birthplace, mother's maiden name); if unavoidable treat the answer like a password, random and long; make each unique.
If someone steals your password (e.g. company says it lost your password in a data breach): change your password right away, create a new strong one. If you reused the same or similar password elsewhere, change it on those services too. If someone is using your personal information, report and get help at IdentityTheft.gov.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """I'm making a new password for my insurance company's website and it keeps rejecting my long phrase of words because it has a length limit. I also don't trust password manager programs and don't want one. How can I still make a strong password?""",
                 """You can still make a strong one without a password manager. When a site rejects long passwords, **mix different kinds of characters** instead.

1. Use **uppercase and lowercase letters**, **numbers**, and **symbols** together.
2. Make it as long as the site allows. Aim for at least 12 characters if you can.
3. Don't use a common phrase, song lyric, or movie quote.

Your **email** password matters most, because password reset links often go to your email inbox.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """An online store emailed me that it lost its customers' passwords in a data breach. I use the same password for that store and for my email and my bank. What should I do?""",
                 """Please **change your password right away**, starting with the store. Then do the other two, since you used the same one.

1. At the store, **create a new strong password**. Make it long, at least 12 characters. Several random words work well.
2. Change the password on your **email** and your **bank** account too, since they share the old one.
3. If you see that someone is using your personal information, get help at **IdentityTheft.gov**.

Email is the most important one to protect, because password reset links often go there.""",
             ]},
        ],
    },
    {
        "task_id": "TR-091", "task_type": "maps_directions", "task": "Get directions",
        "platform": "Google Maps (phone)", "category": "online_services", "sensitive": False,
        "source": {"title": "Google Maps Help: Get directions & show routes (Android)", "url": "https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Android. Get directions: 1 Open the Google Maps app. 2 Search for your destination, or tap it on the map. 3 At the bottom left, tap Directions. 4 Choose a mode: Driving, Transit, Walking, Ride, Cycle, Motorcycle (icons).
Start point defaults to your location. Change start: tap Your location at the top. Change destination: tap the destination box.
Add stops: tap More (three dots), then Edit stops. Add stops, up to 9 including the final destination. Tap Done. Reorder: press and hold the Reorder icon, drag. Multiple destinations are not available for public transit or flight.
Change time: More, then Set depart or arrive time; select Leave or Arrive, set date and time, tap Set (only routes with one destination).
Best route is blue, other routes gray; tap a route on the map to choose it.
Preview: swipe up on the route info to see a list of directions; tap Preview for turn-by-turn preview.
Navigation starts only when your starting point is your location; otherwise you only get a route preview.
Troubleshooting: if you only see a preview, check that the starting point is your location. Transit directions are not available everywhere (local agency must add data).""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Maps (phone)",
             "messages": [
                 """I'm driving to my sister's house tomorrow with my Android phone and I use Google Maps. I have to pick up a prescription at the pharmacy on the way, so I can't just go straight there. Can Maps take me to the pharmacy first and then my sister's?""",
                 """Yes. You can add the pharmacy as a stop on the way.

1. Open the **Google Maps** app.
2. Search for your sister's address and tap it.
3. At the bottom left, tap **Directions**.
4. Choose **Driving**.
5. Tap **More** (the three dots), then tap **Edit stops**.
6. Add the pharmacy as a stop.
7. Tap **Done**.

Maps will show the route with your stop in it. The best route is **blue** and other routes are gray.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Maps (phone)",
             "messages": [
                 "Using Google Maps on my Android phone, how do I get walking directions to the library downtown?",
                 """Here is how.

1. Open the **Google Maps** app.
2. Search for the library, or tap it on the map.
3. At the bottom left, tap **Directions**.
4. Choose **Walking**.
5. Tap a route on the map to pick it. The best route is **blue** and the others are gray.
6. Swipe up on the route information to see a list of turns.

To see a turn-by-turn preview, tap **Preview**.""",
                 "I did all that but it only shows me a preview and won't start guiding me. What's wrong?",
                 """Navigation only starts when your starting point is **your location**. Otherwise it only shows a preview.

1. Look at the starting point at the top of the screen. If it shows some other place, tap it and change it to **your location**.
2. Then try again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-093", "task_type": "join_video_meeting", "task": "Join a Zoom meeting from a link",
        "platform": "Zoom", "category": "communication", "sensitive": False,
        "source": {"title": "Zoom Support: Joining a meeting with the invite link", "url": "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180"},
        "source_notes": """Computer browser. 1 Click the invite link, or copy and paste it into a web browser. Browser redirects to a launch meeting page. 2 A pop-up asks if you want to open Zoom Meetings. 3 Optional: select the checkbox to always let Zoom open links of this type in the app (appears only on select browsers). 4 Click Open (may read Allow or Open zoom.us depending on browser and device). 5 The Zoom app opens and takes you to the meeting.
Invite links can include an embedded passcode, which lets you join more quickly.
Not covered: mobile steps, passcode/waiting room/audio/video prompts, sign-in, app not installed.
Troubleshooting: the Zoom Launcher plug-in may be not activated, disabled, incorrectly installed, or installed but failed to run; if disabled, check whether it is enabled and re-enable it. Safari no longer supports most plug-ins, so you must choose to launch Zoom each time you join.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Zoom",
             "messages": [
                 """I join the same church Bible study on Zoom every Tuesday from my computer using the link in the email. Every week a box pops up asking me about opening Zoom and I'm tired of answering it. Can I make it stop asking me each week?""",
                 """You may be able to. When the box appears, there can be a checkbox for it.

1. Click the **Zoom link** in your email.
2. When the pop-up asks if you want to open Zoom Meetings, **select the checkbox** to always let Zoom open this kind of link in the app.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you into the meeting.

That checkbox only shows up on some browsers. If you don't see it, your browser doesn't offer it, and you will need to click through the pop-up each time. If you use Safari, you have to choose to launch Zoom each time you join.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Zoom",
             "messages": [
                 "My daughter sent me a Zoom link by email for a family call tonight. I'm on my computer. What do I do to get in?",
                 """Here is how.

1. Open the email and **click the Zoom link**. You can also copy the link and paste it into your web browser.
2. A pop-up will ask if you want to open **Zoom Meetings**.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you to the meeting.

If the link already includes the passcode, you can join more quickly.""",
                 "I clicked the link and a page came up, but the Zoom app never opened. What now?",
                 """That can happen when the **Zoom Launcher plug-in** in your browser is turned off, set up wrong, or failed to run.

1. Check whether the plug-in is turned on in your browser. If it is turned off, turn it back on.
2. Then click the link in your email again.

If you use Safari, it no longer supports most plug-ins, so you have to choose to launch Zoom each time you join.""",
             ]},
        ],
    },
    {
        "task_id": "TR-094", "task_type": "video_captions", "task": "Turn on captions",
        "platform": "YouTube", "category": "technical_support", "sensitive": False,
        "source": {"title": "YouTube Help: Manage caption settings (Android)", "url": "https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Android. Turn captions on/off: go to the watch page of any video; tap the video player once to show options; tap the Closed captions icon to turn captions on; tap it again to turn off. If you don't see the icon, the video doesn't have Closed Captions (CC) available.
Always show captions: tap your profile picture; tap Settings (gear icon); tap Captions; tap Show captions (always serves captions when available).
Change default size and style: profile picture; Settings; Captions; tap Caption size and style to change default size and font.
Show captions when muted: on a watch page tap the player once, tap Settings (gear icon), tap the Captions icon to open the captions menu, next to Show when muted tap the toggle on.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "YouTube",
             "messages": [
                 """I watch a lot of cooking videos on the YouTube app on my Android phone and my hearing isn't good. Tapping the captions button on every single video is a pain. Is there a way to have captions on for all of them without doing it each time?""",
                 """Yes, there is a setting for that.

1. Open the **YouTube** app.
2. Tap your **profile picture**.
3. Tap **Settings** (the gear icon).
4. Tap **Captions**.
5. Tap **Show captions**.

After that, YouTube shows captions on videos whenever they are available.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "YouTube",
             "messages": [
                 "how do i get the words to show up on a youtube video on my android phone",
                 """Here is how.

1. Start the video in the **YouTube** app.
2. Tap the video once so the options appear.
3. Tap the **Closed captions** icon to turn captions on.
4. Tap the icon again if you want to turn them off.

If you don't see the **Closed captions** icon, that video doesn't have captions available.""",
                 "ok the words are showing now but they're really tiny and I can't read them",
                 """You can make them bigger.

1. Tap your **profile picture**.
2. Tap **Settings** (the gear icon).
3. Tap **Captions**.
4. Tap **Caption size and style**, then change the size.

This changes the default size for your captions.""",
             ]},
        ],
    },
    {
        "task_id": "TR-095", "task_type": "backup_phone", "task": "Back up the whole phone",
        "platform": "iPhone (iCloud Backup)", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: How to back up your iPhone or iPad with iCloud", "url": "https://support.apple.com/en-us/108366"},
        "source_notes": """Manual backup: 1 Connect to a Wi-Fi network. 2 Open Settings, tap your name, tap iCloud. 3 Tap iCloud Backup. 4 Tap Back Up Now and stay on Wi-Fi until it finishes.
Automatic backup: 1 Settings, tap your name, tap iCloud, tap iCloud Backup; make sure Back Up This iPhone is on. 2 Connect the device to a power source. 3 Connect to a Wi-Fi network. 4 Keep the screen locked.
Storage alert: if a message says there isn't enough iCloud storage to finish the backup, follow the onscreen steps to buy more iCloud storage.
Under Back Up Now, the date and time of your last backup appear. Page has no other troubleshooting.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone (iCloud Backup)",
             "messages": [
                 """I have an iPhone and I keep forgetting to back it up. I don't want to sit there tapping buttons every time. Is there a way for my phone to back itself up to iCloud on its own, like while it charges at night?""",
                 """Yes. iCloud can back up your iPhone automatically. First check that it is turned on.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **iCloud Backup**.
4. Make sure **Back Up This iPhone** is turned on.

After that, the backup runs by itself when your iPhone is all of these things:
1. Plugged in to a power source.
2. Connected to **Wi-Fi**.
3. Locked.

You can see when the last backup happened under **Back Up Now** on the same screen.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone (iCloud Backup)",
             "messages": [
                 "I'm on Wi-Fi with my iPhone. What do I tap to back up everything to iCloud right now?",
                 """Here is how.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **iCloud Backup**.
4. Tap **Back Up Now**.
5. Stay on Wi-Fi until it finishes.

When it is done, the date and time of your last backup show under **Back Up Now**.""",
                 "It says there isn't enough iCloud storage to finish the backup. What do I do?",
                 """That means your iCloud storage is full for this backup.

1. Follow the steps on the screen to **buy more iCloud storage**.
2. Then go back to **Settings**, your name, **iCloud**, **iCloud Backup**, and tap **Back Up Now** again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-096", "task_type": "stolen_device_protection", "task": "Turn on Stolen Device Protection",
        "platform": "iPhone", "category": "technical_support", "sensitive": True,
        "source": {"title": "Apple Support: About Stolen Device Protection for iPhone", "url": "https://support.apple.com/en-us/120340"},
        "source_notes": """Requirements: iOS 17.3 or later; two-factor authentication for your Apple Account; a device passcode; Face ID or Touch ID; Location Services with Significant Locations on (Settings, Privacy & Security, Location Services, System Services, Significant Locations & Routes); Find My on (can't turn it off while Stolen Device Protection is on). Must be turned on before the iPhone is lost or stolen.
Turn on or off: 1 Open Settings and tap Face ID & Passcode. 2 Enter your device passcode. 3 Tap Stolen Device Protection, then turn it on or off. May already be on by default.
Optional: Settings, Face ID (or Touch ID) & Passcode, Stolen Device Protection, choose Always under Require Security Delay (applies security measures everywhere).
Familiar locations (home, work, other places you regularly use phone): passcode works as usual, extra requirements don't apply. Away from them, Face ID or Touch ID required with no passcode fallback for some actions, and changes to critical settings need Face ID/Touch ID, a one-hour wait, then Face ID/Touch ID again.
Troubleshooting: turn off before you sell, give away, or trade in. Critical settings can't be changed at account.apple.com. Stolen iPhone: mark it lost at iCloud.com/find.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """I already have Stolen Device Protection on my iPhone. But I'm worried because I mostly use my phone at home and at my daughter's house, and I heard it relaxes the rules at familiar places like that. I want the extra protection everywhere, even at home. Can I do that?""",
                 """Yes. You can make the extra protection apply everywhere, including familiar places like home.

1. Open **Settings** and tap **Face ID & Passcode**. On an iPhone with Touch ID, it says **Touch ID & Passcode**.
2. Tap **Stolen Device Protection**.
3. Under **Require Security Delay**, choose **Always**.

Now the extra security steps apply at home too, not only away from familiar places.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Please walk me through turning on Stolen Device Protection on my iPhone. I want it on in case it gets stolen.",
                 """Good idea to turn it on before anything happens. Here is how.

1. Open **Settings** and tap **Face ID & Passcode**.
2. Enter your **device passcode**.
3. Tap **Stolen Device Protection**.
4. Turn it **on**.

It may already be on. Once it is on, your iPhone asks for extra security steps when you are away from familiar places like home or work.""",
                 "I looked in Face ID & Passcode and I don't see Stolen Device Protection there. Where is it?",
                 """It only works on an iPhone that meets all of these. Please check:
1. Your iPhone has **iOS 17.3 or later**.
2. **Two-factor authentication** is on for your Apple Account.
3. Your iPhone has a **passcode**, and **Face ID** or **Touch ID** is set up.
4. **Find My** is on.
5. **Significant Locations** is on. It is under **Settings**, **Privacy & Security**, **Location Services**, **System Services**, then **Significant Locations & Routes**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-097", "task_type": "live_captions", "task": "Turn on live captions",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Accessibility Help: Live Caption", "url": "https://support.google.com/accessibility/android/answer/9350862?hl=en"},
        "source_notes": """Turn on via volume button: press the volume button; under the volume controls tap More, then Live Caption, then Done. Captions then appear for speech in audio playing on your device.
Turn on via Settings: open Settings, tap Accessibility, tap Live Caption and turn it on.
First use requires Wi-Fi to download the default language pack. Processing is on the device, captions don't use mobile data. Works best with clear speech, doesn't caption music.
Troubleshooting: no Live Caption option: check with your phone manufacturer. Volume steps don't work: search for Live Caption in Settings and turn it on. Battery saver mode turns Live Caption off. Some media and calling apps may not support captions.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 """The volume buttons on the side of my Android phone are broken and I can't press them at all. I'd like to turn on Live Caption so I can read what people say in my videos, but every guide I find starts with the volume button. Is there another way?""",
                 """Yes, you can do it without the volume buttons, from your settings.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Captions then appear for speech in audio playing on your phone. The first time you use it, your phone needs **Wi-Fi** to download the language pack.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My hearing is going and I want my Android phone to show words on screen when someone is talking in a video. How do I turn on live captions with the volume button?",
                 """Here is how.

1. Press a **volume button** on the side of the phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**.
4. Tap **Done**.

Captions then appear for speech in audio playing on your phone.""",
                 "I pressed the volume button but I never saw a Live Caption choice. Now what?",
                 """Try turning it on from your settings instead.

1. Open **Settings** and search for **Live Caption**. You can also tap **Accessibility** and then **Live Caption**.
2. Turn **Live Caption** on.

If you still don't see a Live Caption option anywhere, check with your phone's maker.""",
             ]},
        ],
    },
    {
        "task_id": "TR-098", "task_type": "text_size", "task": "Make text bigger",
        "platform": "Windows 11", "category": "technical_support", "sensitive": False,
        "source": {"title": "Microsoft Support: Make text and apps bigger", "url": "https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64"},
        "source_notes": """Text size only: 1 Open Accessibility settings: press Windows logo key+U, or select Start > Settings > Accessibility. 2 Select Text size. 3 Drag the Text size slider to the right; the sample text gets larger. 4 Select Apply. Windows scales up the size of all text (title bars, menus, icon labels).
Display scaling (changes everything on screen, not just text, including images and apps): 1 Open Settings: Windows logo key+I, or Start > Settings. 2 Select Display. 3 Under Scale & layout, expand the Scale menu and choose the option you want.
Troubleshooting: some apps may need you to sign out and back in before certain changes take effect. Most changes apply immediately. Page doesn't cover Magnifier or browser zoom.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """My Windows 11 computer has tiny words in the menus and under the little pictures on my desktop. I don't want the pictures and everything else blown up, only the writing, or my screen will look too crowded. Can I do that?""",
                 """Yes. There is a setting that makes only the text bigger.

1. Press the **Windows logo key** and **U** together. This opens Accessibility settings. You can also select **Start**, then **Settings**, then **Accessibility**.
2. Select **Text size**.
3. Drag the **Text size** slider to the right. The sample text gets bigger as you move it.
4. Select **Apply**.

After you apply it, the text in title bars, menus, and icon labels gets larger.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Windows 11 laptop. I can't read the words on the screen. How do I make the text larger?",
                 """Here is how.

1. Press the **Windows logo key** and **U** together to open Accessibility settings.
2. Select **Text size**.
3. Drag the **Text size** slider to the right.
4. Select **Apply**.

The sample text gets larger as you drag. After you select **Apply**, text in title bars, menus, and icon labels gets larger.""",
                 "The words are bigger now, thank you, but the pictures and buttons are still small. Can I fix that too?",
                 """Yes. Display scaling makes everything on the screen bigger, not just the text.

1. Press the **Windows logo key** and **I** together to open Settings.
2. Select **Display**.
3. Under **Scale & layout**, open the **Scale** menu and choose a bigger option.

Most changes happen right away. If an app still looks the same, you may need to sign out and sign back in.""",
             ]},
        ],
    },
    {
        "task_id": "TR-099", "task_type": "phone_not_charging", "task": "iPhone stops charging at 80%",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: If your iPhone or iPod touch won't charge", "url": "https://support.apple.com/en-ca/108805"},
        "source_notes": """Also read the Apple page linked from the cited page: https://support.apple.com/en-ca/108055 (Optimized Battery Charging and charge limit).
108805: stopping at 80 percent is expected when Optimized Battery Charging (iOS 13 and later) or a charge limit (iPhone 15 and later) is active; heat can also limit charging above 80 percent (move to a cooler location).
108055 settings: iPhone 15 and later: Settings, Battery, Charging, choose an option on the slider for the charge limit (80% to 100% in 5% steps; Optimized Battery Charging can be on only at 100%; to turn it off set limit below 100%). iPhone 14 and earlier: Settings, Battery, Battery Health & Charging, turn Optimized Battery Charging on or off (turning it off can increase battery wear).
Charge to 100% for the day: if Optimized Battery Charging is active, touch and hold its Lock Screen notification, then tap Charge Now. On iPhone 15 and later you can also set the charge limit to 100%. Notification shows when the iPhone will be fully charged. It needs at least 14 days to learn habits, delays past 80% only when it predicts a long charging session.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """My iPhone has been sitting at 80% since last night and I'm leaving for the airport in a half hour and I need it full. I don't want to go digging through settings or change anything for good. It's just for today. What can I tap?""",
                 """You can charge it fully just for today, without changing any settings.

1. Wake your iPhone and look at its **Lock Screen**.
2. **Touch and hold** the notification from **Optimized Battery Charging**. It says when your iPhone will be fully charged.
3. Tap **Charge Now**.

Your iPhone will keep charging past 80%. Optimized Battery Charging stays on for other days.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an iPhone 14. I want to switch off whatever makes it wait at 80% when it's charging. Where is it?",
                 """It is probably **Optimized Battery Charging**. Here is how to turn it off.

1. Open **Settings** and tap **Battery**.
2. Tap **Battery Health & Charging**.
3. Turn **Optimized Battery Charging** off.

Turning it off can make the battery wear out faster.""",
                 "Oh wait, I just checked and it's actually an iPhone 15. I don't see Battery Health & Charging, only a Charging choice.",
                 """That is right for an iPhone 15. The setting is in a different place.

1. Open **Settings** and tap **Battery**.
2. Tap **Charging**.
3. Choose an option on the slider for the charge limit. Optimized Battery Charging can only be on when the limit is 100%, so set it **below 100%** to turn it off.

For just one day, you can also touch and hold the Optimized Battery Charging notification on your Lock Screen and tap **Charge Now**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-101", "task_type": "ring_volume", "task": "Phone only vibrates, does not ring",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: Use the volume buttons, side button, and other controls on your iPhone", "url": "https://support.apple.com/en-us/105103"},
        "source_notes": """Ring/Silent switch (iPhone 8 and earlier; also in a section with the Action button for iPhone 17e, 16e, 15 and earlier models without a Home button): if the switch shows orange, your iPhone is in Silent mode and will vibrate for incoming calls or alerts. In Silent mode, alarms set in the Clock app still sound, and calls from favorite contacts still ring.
Action button (iPhone 16 and later models with Camera Control, and iPhone 17e, 16e, and iPhone 15 Pro models): you can choose what it does, such as opening Camera or the flashlight. By default, the Action button turns Silent mode on or off. Page doesn't say press or press and hold.
Volume buttons: when you're not using other apps, the buttons adjust the ringer volume.
Page doesn't cover Focus, Bluetooth, restart.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """I have a new iPhone 16. My calls only buzz and never ring. I looked all along the side for the little switch my old phone had and there isn't one, only a button. I'm afraid of pressing the wrong thing and messing it up. Is that button the cause?""",
                 """It could be. Your iPhone 16 doesn't have the old switch. It has an **Action button**, and by default the **Action button turns Silent mode on or off**.

1. Use the **Action button** to switch Silent mode off. Your iPhone vibrates for calls when Silent mode is on, and rings when it is off.
2. If it still seems quiet, go to your Home Screen and press the **volume up** button. When you aren't using another app, the volume buttons change the ringer volume.

You can set the Action button to do other things, like open the Camera or turn on the flashlight. If it was changed, it may not control Silent mode.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My old iPhone 8 won't ring for calls, it only buzzes. What should I check?",
                 """It may be in **Silent mode**. Check the small **Ring/Silent switch** on the side of your iPhone.

1. Look at the switch. If it shows **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

In Silent mode your iPhone vibrates for calls. Alarms you set in the Clock app still sound, and calls from favorite contacts still ring.""",
                 "There's no orange showing now, but the ring is really quiet. What else can I do?",
                 """Then turn up the ringer volume.

1. Go to your **Home Screen**. Don't be inside another app.
2. Press the **volume up** button on the side. When you are not using other apps, the volume buttons adjust the ringer volume.""",
             ]},
        ],
    },
    {
        "task_id": "TR-102", "task_type": "read_aloud", "task": "Have the phone read the screen aloud",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Accessibility Help: Use Select to Speak", "url": "https://support.google.com/accessibility/android/answer/7349565?hl=en"},
        "source_notes": """Android (some steps need Android 11.0 or later). Turn on: Settings, Accessibility, Select to Speak, turn on Select to Speak shortcut (optional: tap the shortcut to change it).
Use: start with a 2-finger swipe up (3-finger if TalkBack on) or tap the Accessibility button; tap an item such as text or image; to hear several items drag your finger across the screen; to hear everything tap Play; in the player use buttons to pause or play, skip forward or backward, increase or decrease speed.
Read selected text aloud (no Select to Speak needed): select the text, in the pop-up menu tap More, then Read aloud. Works only on readable text such as web page text.
Read in the background (scroll or switch apps while it reads): Settings, Accessibility, Select to Speak, tap Settings, turn on Read in background.
Troubleshooting: can't find Select to Speak: update Android Accessibility Suite from Google Play. May not work with every mobile web browser. Only readable text, such as web page text, is supported.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 """I have an Android phone and Select to Speak is already working for me. My problem is that it stops reading when I leave the page. I'd like to start it reading a long article and then keep scrolling or open my other apps while it reads. Can it do that?""",
                 """Yes. There is a setting called **Read in background**.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Select to Speak**.
3. Tap **Settings**.
4. Turn on **Read in background**.

Now you can scroll or switch to other apps while it keeps reading.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone is a Samsung. I'd like it to read a web page out loud to me. How?",
                 """You can use **Select to Speak**. Turn it on first.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Select to Speak**.
3. Turn on **Select to Speak shortcut**.

Then use it on the page:
1. Start it with a **2-finger swipe up** from the bottom of the screen, or tap the **Accessibility button**.
2. Tap the text you want to hear, or tap **Play** to hear everything.""",
                 "I did that in my browser and it just sits there, nothing gets read.",
                 """Select to Speak may not work with every mobile web browser. Also, it only reads readable text, like the text of a web page. Try this instead, which doesn't need Select to Speak:

1. **Select the text** on the page.
2. In the pop-up menu, tap **More**.
3. Tap **Read aloud**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-103", "task_type": "reminders", "task": "Set a reminder",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: Use Reminders on your iPhone, iPad, or iPod touch", "url": "https://support.apple.com/en-us/102484"},
        "source_notes": """Create: open Reminders, tap + New Reminder, type the reminder. Details: Date and Time button, pick Today, Tomorrow, This Weekend, Next Week, or Custom to choose a day and time. Location button: pick a preset or Custom, then choose arriving or leaving and set the area's perimeter. 
Urgent (iOS 26.2 and later): tap the Info button, then turn on Urgent under Date & Time. Urgent alarms sound even when the device is silenced or a Focus is on. Can't mark reminders urgent: you need iCloud Reminders set up.
Siri: for location reminders add home and work addresses to your card in Contacts (Contacts, My Card, Edit, add address, Done); Location Services must be on.
A reminder with a date but no time notifies at 9:00 AM by default (change: Settings, Apps, Reminders, time below All-Day Reminders).
Troubleshooting: location reminders don't work: turn on Location Services under Settings > Privacy & Security.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """My iPhone is on silent almost all the time because I can't stand the noise. But I have a heart pill I must take at noon and I need the reminder to actually make a sound anyway. Can a reminder be loud even on silent? I want one for today at noon.""",
                 """Yes, if your iPhone has **iOS 26.2 or later**, you can mark a reminder as **Urgent**. Urgent alarms sound even when your iPhone is silenced.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take heart pill**.
3. Tap the **Date and Time** button, then tap **Custom** and choose today at **12:00 PM**.
4. Tap the **Info** button.
5. Turn on **Urgent** under **Date & Time**.

You also need iCloud Reminders set up to mark a reminder urgent.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Can my iPhone remind me to take my pills when I leave the house? I want it to go off when I walk out the door.",
                 """Yes. A location reminder can do that.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take pills**.
3. Tap the **Location** button.
4. Pick a preset or tap **Custom**.
5. Choose **leaving**, and set the area around the place.

Your iPhone reminds you when you leave that place.""",
                 "I set it up like that but this morning it never went off when I left.",
                 """Location reminders need **Location Services** turned on.

1. Open **Settings** and tap **Privacy & Security**.
2. Turn on **Location Services**.

If you picked your home or work, also make sure that address is on your card. Open **Contacts**, tap **My Card**, tap **Edit**, add the address, and tap **Done**.""",
             ]},
        ],
    },
]
