# Review input: batch fx7, round 1 (26 examples)

## tr089-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: phone
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
A man phoned and said he is with Social Security and my number is tied to fraud. He knew my name and my street address. He told me I must not tell my family or I could be arrested, and my caller ID really did say Social Security. He is going to call me back in an hour. Is this real?

**ASSISTANT:**
Please **do not give him anything**, and hang up if he calls again. This is a scam. The real Social Security Administration **won't threaten you** or suspend your Social Security number. Knowing your name and address, threats of arrest, and a real-looking caller ID are all tricks scammers use. Caller ID can be faked.

1. When he calls back, **hang up**. Don't share personal or bank information.
2. Don't call back the number he gave you or the one on your caller ID.
3. If you are worried, **call your local Social Security office yourself**. You can find the number at **secure.ssa.gov/ICON/main.jsp**.
4. **Report the call** at **reportfraud.ftc.gov**, and to the Social Security Office of the Inspector General at **oig.ssa.gov**.

## tr089-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: phone
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
I feel so silly. A woman from Social Security said my number was being suspended, and I told her my Social Security number and my birthday before I got suspicious and hung up. What do I do now?

**ASSISTANT:**
Please don't feel silly. These callers are good at sounding real, and you did the right thing by hanging up. Here is what to do now.

1. Go to **IdentityTheft.gov** for steps to protect your identity.
2. **Report the call** to the FTC at **reportfraud.ftc.gov**.
3. Also report it to the Social Security Office of the Inspector General at **oig.ssa.gov**, and to your state attorney general.

If she calls again, hang up and don't call back the number she used. If you ever want to check on your account, call your local Social Security office using a number you find yourself.

## tr090-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
I'm making a new password for my insurance company's website and it keeps rejecting my long phrase of words because it has a length limit. I also don't trust password manager programs and don't want one. How can I still make a strong password?

**ASSISTANT:**
You can still make a strong one without a password manager. When a site rejects long passwords, **mix different kinds of characters** instead.

1. Use **uppercase and lowercase letters**, **numbers**, and **symbols** together.
2. Make it as long as the site allows. Aim for at least 12 characters if you can.
3. Don't use a common phrase, song lyric, or movie quote.

Your **email** password matters most, because password reset links often go to your email inbox.

## tr090-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
An online store emailed me that it lost its customers' passwords in a data breach. I use the same password for that store and for my email and my bank. What should I do?

**ASSISTANT:**
Please **change your password right away**, starting with the store. Then do the other two, since you used the same one.

1. At the store, **create a new strong password**. Make it long, at least 12 characters. Several random words work well.
2. Change the password on your **email** and your **bank** account too, since they share the old one.
3. If you see that someone is using your personal information, get help at **IdentityTheft.gov**.

Email is the most important one to protect, because password reset links often go there.

## tr091-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Maps (phone)
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I'm driving to my sister's house tomorrow with my Android phone and I use Google Maps. I have to pick up a prescription at the pharmacy on the way, so I can't just go straight there. Can Maps take me to the pharmacy first and then my sister's?

**ASSISTANT:**
Yes. You can add the pharmacy as a stop on the way.

1. Open the **Google Maps** app.
2. Search for your sister's address and tap it.
3. At the bottom left, tap **Directions**.
4. Choose **Driving**.
5. Tap **More** (the three dots), then tap **Edit stops**.
6. Add the pharmacy as a stop.
7. Tap **Done**.

Maps will show the route with your stop in it. The best route is **blue** and other routes are gray.

## tr091-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Maps (phone)
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
Using Google Maps on my Android phone, how do I get walking directions to the library downtown?

**ASSISTANT:**
Here is how.

1. Open the **Google Maps** app.
2. Search for the library, or tap it on the map.
3. At the bottom left, tap **Directions**.
4. Choose **Walking**.
5. Tap a route on the map to pick it. The best route is **blue** and the others are gray.
6. Swipe up on the route information to see a list of turns.

To see a turn-by-turn preview, tap **Preview**.

**USER:**
I did all that but it only shows me a preview and won't start guiding me. What's wrong?

**ASSISTANT:**
Navigation only starts when your starting point is **your location**. Otherwise it only shows a preview.

1. Look at the starting point at the top of the screen. If it shows some other place, tap it and change it to **your location**.
2. Then try again.

## tr093-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
I join the same church Bible study on Zoom every Tuesday from my computer using the link in the email. Every week a box pops up asking me about opening Zoom and I'm tired of answering it. Can I make it stop asking me each week?

**ASSISTANT:**
You may be able to. When the box appears, there can be a checkbox for it.

1. Click the **Zoom link** in your email.
2. When the pop-up asks if you want to open Zoom Meetings, **select the checkbox** to always let Zoom open this kind of link in the app.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you into the meeting.

That checkbox only shows up on some browsers. If you don't see it, your browser doesn't offer it, and you will need to click through the pop-up each time. If you use Safari, you have to choose to launch Zoom each time you join.

## tr093-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
My daughter sent me a Zoom link by email for a family call tonight. I'm on my computer. What do I do to get in?

**ASSISTANT:**
Here is how.

1. Open the email and **click the Zoom link**. You can also copy the link and paste it into your web browser.
2. A pop-up will ask if you want to open **Zoom Meetings**.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you to the meeting.

If the link already includes the passcode, you can join more quickly.

**USER:**
I clicked the link and a page came up, but the Zoom app never opened. What now?

**ASSISTANT:**
That can happen when the **Zoom Launcher plug-in** in your browser is turned off, set up wrong, or failed to run.

1. Check whether the plug-in is turned on in your browser. If it is turned off, turn it back on.
2. Then click the link in your email again.

If you use Safari, it no longer supports most plug-ins, so you have to choose to launch Zoom each time you join.

## tr094-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: YouTube
- task: Turn on captions (YouTube) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I watch a lot of cooking videos on the YouTube app on my Android phone and my hearing isn't good. Tapping the captions button on every single video is a pain. Is there a way to have captions on for all of them without doing it each time?

**ASSISTANT:**
Yes, there is a setting for that.

1. Open the **YouTube** app.
2. Tap your **profile picture**.
3. Tap **Settings** (the gear icon).
4. Tap **Captions**.
5. Tap **Show captions**.

After that, YouTube shows captions on videos whenever they are available.

## tr094-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: YouTube
- task: Turn on captions (YouTube) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do i get the words to show up on a youtube video on my android phone

**ASSISTANT:**
Here is how.

1. Start the video in the **YouTube** app.
2. Tap the video once so the options appear.
3. Tap the **Closed captions** icon to turn captions on.
4. Tap the icon again if you want to turn them off.

If you don't see the **Closed captions** icon, that video doesn't have captions available.

**USER:**
ok the words are showing now but they're really tiny and I can't read them

**ASSISTANT:**
You can make them bigger.

1. Tap your **profile picture**.
2. Tap **Settings** (the gear icon).
3. Tap **Captions**.
4. Tap **Caption size and style**, then change the size.

This changes the default size for your captions.

## tr095-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone (iCloud Backup)
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
I have an iPhone and I keep forgetting to back it up. I don't want to sit there tapping buttons every time. Is there a way for my phone to back itself up to iCloud on its own, like while it charges at night?

**ASSISTANT:**
Yes. iCloud can back up your iPhone automatically. First check that it is turned on.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **iCloud Backup**.
4. Make sure **Back Up This iPhone** is turned on.

After that, the backup runs by itself when your iPhone is all of these things:
1. Plugged in to a power source.
2. Connected to **Wi-Fi**.
3. Locked.

You can see when the last backup happened under **Back Up Now** on the same screen.

## tr095-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone (iCloud Backup)
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
I'm on Wi-Fi with my iPhone. What do I tap to back up everything to iCloud right now?

**ASSISTANT:**
Here is how.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **iCloud Backup**.
4. Tap **Back Up Now**.
5. Stay on Wi-Fi until it finishes.

When it is done, the date and time of your last backup show under **Back Up Now**.

**USER:**
It says there isn't enough iCloud storage to finish the backup. What do I do?

**ASSISTANT:**
That means your iCloud storage is full for this backup.

1. Follow the steps on the screen to **buy more iCloud storage**.
2. Then go back to **Settings**, your name, **iCloud**, **iCloud Backup**, and tap **Back Up Now** again.

## tr096-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
I already have Stolen Device Protection on my iPhone. But I'm worried because I mostly use my phone at home and at my daughter's house, and I heard it relaxes the rules at familiar places like that. I want the extra protection everywhere, even at home. Can I do that?

**ASSISTANT:**
Yes. You can make the extra protection apply everywhere, including familiar places like home.

1. Open **Settings** and tap **Face ID & Passcode**. On an iPhone with Touch ID, it says **Touch ID & Passcode**.
2. Tap **Stolen Device Protection**.
3. Under **Require Security Delay**, choose **Always**.

Now the extra security steps apply at home too, not only away from familiar places.

## tr096-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
Please walk me through turning on Stolen Device Protection on my iPhone. I want it on in case it gets stolen.

**ASSISTANT:**
Good idea to turn it on before anything happens. Here is how.

1. Open **Settings** and tap **Face ID & Passcode**.
2. Enter your **device passcode**.
3. Tap **Stolen Device Protection**.
4. Turn it **on**.

It may already be on. Once it is on, your iPhone asks for extra security steps when you are away from familiar places like home or work.

**USER:**
I looked in Face ID & Passcode and I don't see Stolen Device Protection there. Where is it?

**ASSISTANT:**
It only works on an iPhone that meets all of these. Please check:
1. Your iPhone has **iOS 17.3 or later**.
2. **Two-factor authentication** is on for your Apple Account.
3. Your iPhone has a **passcode**, and **Face ID** or **Touch ID** is set up.
4. **Find My** is on.
5. **Significant Locations** is on. It is under **Settings**, **Privacy & Security**, **Location Services**, **System Services**, then **Significant Locations & Routes**.

## tr097-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on live captions (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/9350862?hl=en

**USER:**
The volume buttons on the side of my Android phone are broken and I can't press them at all. I'd like to turn on Live Caption so I can read what people say in my videos, but every guide I find starts with the volume button. Is there another way?

**ASSISTANT:**
Yes, you can do it without the volume buttons, from your settings.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Captions then appear for speech in audio playing on your phone. The first time you use it, your phone needs **Wi-Fi** to download the language pack.

## tr097-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn on live captions (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/9350862?hl=en

**USER:**
My hearing is going and I want my Android phone to show words on screen when someone is talking in a video. How do I turn on live captions with the volume button?

**ASSISTANT:**
Here is how.

1. Press a **volume button** on the side of the phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**.
4. Tap **Done**.

Captions then appear for speech in audio playing on your phone.

**USER:**
I pressed the volume button but I never saw a Live Caption choice. Now what?

**ASSISTANT:**
Try turning it on from your settings instead.

1. Open **Settings** and search for **Live Caption**. You can also tap **Accessibility** and then **Live Caption**.
2. Turn **Live Caption** on.

If you still don't see a Live Caption option anywhere, check with your phone's maker.

## tr098-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
My Windows 11 computer has tiny words in the menus and under the little pictures on my desktop. I don't want the pictures and everything else blown up, only the writing, or my screen will look too crowded. Can I do that?

**ASSISTANT:**
Yes. There is a setting that makes only the text bigger.

1. Press the **Windows logo key** and **U** together. This opens Accessibility settings. You can also select **Start**, then **Settings**, then **Accessibility**.
2. Select **Text size**.
3. Drag the **Text size** slider to the right. The sample text gets bigger as you move it.
4. Select **Apply**.

After you apply it, the text in title bars, menus, and icon labels gets larger.

## tr098-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
Windows 11 laptop. I can't read the words on the screen. How do I make the text larger?

**ASSISTANT:**
Here is how.

1. Press the **Windows logo key** and **U** together to open Accessibility settings.
2. Select **Text size**.
3. Drag the **Text size** slider to the right.
4. Select **Apply**.

The sample text gets larger as you drag. After you select **Apply**, text in title bars, menus, and icon labels gets larger.

**USER:**
The words are bigger now, thank you, but the pictures and buttons are still small. Can I fix that too?

**ASSISTANT:**
Yes. Display scaling makes everything on the screen bigger, not just the text.

1. Press the **Windows logo key** and **I** together to open Settings.
2. Select **Display**.
3. Under **Scale & layout**, open the **Scale** menu and choose a bigger option.

Most changes happen right away. If an app still looks the same, you may need to sign out and sign back in.

## tr099-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
My iPhone has been sitting at 80% since last night and I'm leaving for the airport in a half hour and I need it full. I don't want to go digging through settings or change anything for good. It's just for today. What can I tap?

**ASSISTANT:**
You can charge it fully just for today, without changing any settings.

1. Wake your iPhone and look at its **Lock Screen**.
2. **Touch and hold** the notification from **Optimized Battery Charging**. It says when your iPhone will be fully charged.
3. Tap **Charge Now**.

Your iPhone will keep charging past 80%. Optimized Battery Charging stays on for other days.

## tr099-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
I have an iPhone 14. I want to switch off whatever makes it wait at 80% when it's charging. Where is it?

**ASSISTANT:**
It is probably **Optimized Battery Charging**. Here is how to turn it off.

1. Open **Settings** and tap **Battery**.
2. Tap **Battery Health & Charging**.
3. Turn **Optimized Battery Charging** off.

Turning it off can make the battery wear out faster.

**USER:**
Oh wait, I just checked and it's actually an iPhone 15. I don't see Battery Health & Charging, only a Charging choice.

**ASSISTANT:**
That is right for an iPhone 15. The setting is in a different place.

1. Open **Settings** and tap **Battery**.
2. Tap **Charging**.
3. Choose an option on the slider for the charge limit. Optimized Battery Charging can only be on when the limit is 100%, so set it **below 100%** to turn it off.

For just one day, you can also touch and hold the Optimized Battery Charging notification on your Lock Screen and tap **Charge Now**.

## tr101-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
I have a new iPhone 16. My calls only buzz and never ring. I looked all along the side for the little switch my old phone had and there isn't one, only a button. I'm afraid of pressing the wrong thing and messing it up. Is that button the cause?

**ASSISTANT:**
It could be. Your iPhone 16 doesn't have the old switch. It has an **Action button**, and by default the **Action button turns Silent mode on or off**.

1. Use the **Action button** to switch Silent mode off. Your iPhone vibrates for calls when Silent mode is on, and rings when it is off.
2. If it still seems quiet, go to your Home Screen and press the **volume up** button. When you aren't using another app, the volume buttons change the ringer volume.

You can set the Action button to do other things, like open the Camera or turn on the flashlight. If it was changed, it may not control Silent mode.

## tr101-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
My old iPhone 8 won't ring for calls, it only buzzes. What should I check?

**ASSISTANT:**
It may be in **Silent mode**. Check the small **Ring/Silent switch** on the side of your iPhone.

1. Look at the switch. If it shows **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

In Silent mode your iPhone vibrates for calls. Alarms you set in the Clock app still sound, and calls from favorite contacts still ring.

**USER:**
There's no orange showing now, but the ring is really quiet. What else can I do?

**ASSISTANT:**
Then turn up the ringer volume.

1. Go to your **Home Screen**. Don't be inside another app.
2. Press the **volume up** button on the side. When you are not using other apps, the volume buttons adjust the ringer volume.

## tr102-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Have the phone read the screen aloud (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

**USER:**
I have an Android phone and Select to Speak is already working for me. My problem is that it stops reading when I leave the page. I'd like to start it reading a long article and then keep scrolling or open my other apps while it reads. Can it do that?

**ASSISTANT:**
Yes. There is a setting called **Read in background**.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Select to Speak**.
3. Tap **Settings**.
4. Turn on **Read in background**.

Now you can scroll or switch to other apps while it keeps reading.

## tr102-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Have the phone read the screen aloud (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

**USER:**
My Android phone is a Samsung. I'd like it to read a web page out loud to me. How?

**ASSISTANT:**
You can use **Select to Speak**. Turn it on first.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Select to Speak**.
3. Turn on **Select to Speak shortcut**.

Then use it on the page:
1. Start it with a **2-finger swipe up** from the bottom of the screen, or tap the **Accessibility button**.
2. Tap the text you want to hear, or tap **Play** to hear everything.

**USER:**
I did that in my browser and it just sits there, nothing gets read.

**ASSISTANT:**
Select to Speak may not work with every mobile web browser. Also, it only reads readable text, like the text of a web page. Try this instead, which doesn't need Select to Speak:

1. **Select the text** on the page.
2. In the pop-up menu, tap **More**.
3. Tap **Read aloud**.

## tr103-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
My iPhone is on silent almost all the time because I can't stand the noise. But I have a heart pill I must take at noon and I need the reminder to actually make a sound anyway. Can a reminder be loud even on silent? I want one for today at noon.

**ASSISTANT:**
Yes, if your iPhone has **iOS 26.2 or later**, you can mark a reminder as **Urgent**. Urgent alarms sound even when your iPhone is silenced.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take heart pill**.
3. Tap the **Date and Time** button, then tap **Custom** and choose today at **12:00 PM**.
4. Tap the **Info** button.
5. Turn on **Urgent** under **Date & Time**.

You also need iCloud Reminders set up to mark a reminder urgent.

## tr103-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
Can my iPhone remind me to take my pills when I leave the house? I want it to go off when I walk out the door.

**ASSISTANT:**
Yes. A location reminder can do that.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take pills**.
3. Tap the **Location** button.
4. Pick a preset or tap **Custom**.
5. Choose **leaving**, and set the area around the place.

Your iPhone reminds you when you leave that place.

**USER:**
I set it up like that but this morning it never went off when I left.

**ASSISTANT:**
Location reminders need **Location Services** turned on.

1. Open **Settings** and tap **Privacy & Security**.
2. Turn on **Location Services**.

If you picked your home or work, also make sure that address is on your card. Open **Contacts**, tap **My Card**, tap **Edit**, add the address, and tap **Done**.
