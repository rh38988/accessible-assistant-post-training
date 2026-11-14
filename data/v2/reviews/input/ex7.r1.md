# Review input: batch ex7, round 1 (52 examples)

## tr089-a
- scenario: direct | style: plain | specification: fully_specified | platform: phone
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
A caller said he's from Social Security and my number has been suspended because of a crime. He wants me to buy gift cards to fix it. What should I do?

**ASSISTANT:**
Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**. Your benefits are not being cut off.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.

## tr089-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
Got a call from the government saying I owe money. Is that real?

**ASSISTANT:**
Let's check before you do anything. **Which agency did they say they were from, and how did they want you to pay?**

## tr089-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: True
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
social security called me

**ASSISTANT:**
Okay, let's make sure it was really them. Until we know, please don't give them any money or personal information.

**Did the caller ask you for money or personal information?**

## tr089-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: phone
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
Got a call from the government saying I owe money. Is that real?

**ASSISTANT:**
Let's check before you do anything. **Which agency did they say they were from, and how did they want you to pay?**

**USER:**
Social Security. They said I need to buy gift cards or my number will be suspended.

**ASSISTANT:**
Thank you. That's a scam.

Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**. Your benefits are not being cut off.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.

## tr090-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
How do I make a strong password that I can actually remember?

**ASSISTANT:**
A good trick is to use a **passphrase**: several random words strung together. It's long, which makes it strong, but it's easier to remember than a jumble of symbols.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Several random words work well.
2. **Use a different password for each account**, so if one is stolen, the others stay safe.
3. **Avoid famous quotes or song lyrics**, because hacking programs can guess them.
4. **Consider a password manager.** It can create and remember strong passwords for you, and many web browsers have one built in.
5. **Turn on two-step verification** where you can, so a stolen password alone isn't enough to get in.

Your **email** password is the most important one to protect, since password reset links usually go there.

## tr090-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
Can you help me with my passwords?

**ASSISTANT:**
Of course. What would you like help with: **making a strong new password**, **keeping track of the ones you have**, or **resetting one you forgot**?

## tr090-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
I use my dog's name and my birthday for everything because that's the only way I remember. My grandson says that's not safe. What should I do instead?

**ASSISTANT:**
Your grandson is right that one easy-to-guess password everywhere is risky. The good news is there are safer options that are still easy to remember.

A good trick is to use a **passphrase**: several random words strung together. It's long, which makes it strong, but it's easier to remember than a jumble of symbols.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Several random words work well.
2. **Use a different password for each account**, so if one is stolen, the others stay safe.
3. **Avoid famous quotes or song lyrics**, because hacking programs can guess them.
4. **Consider a password manager.** It can create and remember strong passwords for you, and many web browsers have one built in.
5. **Turn on two-step verification** where you can, so a stolen password alone isn't enough to get in.

Your **email** password is the most important one to protect, since password reset links usually go there.

## tr090-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
Can you help me with my passwords?

**ASSISTANT:**
Of course. What would you like help with: **making a strong new password**, **keeping track of the ones you have**, or **resetting one you forgot**?

**USER:**
Making a strong new one that I can remember.

**ASSISTANT:**
Sure.

A good trick is to use a **passphrase**: several random words strung together. It's long, which makes it strong, but it's easier to remember than a jumble of symbols.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Several random words work well.
2. **Use a different password for each account**, so if one is stolen, the others stay safe.
3. **Avoid famous quotes or song lyrics**, because hacking programs can guess them.
4. **Consider a password manager.** It can create and remember strong passwords for you, and many web browsers have one built in.
5. **Turn on two-step verification** where you can, so a stolen password alone isn't enough to get in.

Your **email** password is the most important one to protect, since password reset links usually go there.

## tr091-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Maps (phone)
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I get directions to my doctor's office in Google Maps on my Android phone?

**ASSISTANT:**
Here's how. It takes about a minute.

1. Open the **Google Maps** app.
2. Tap the search bar and type the address or name of the place.
3. Tap the correct result.
4. Tap **Directions** at the bottom left.
5. Choose how you're traveling: **driving**, **transit**, or **walking**.
6. Pick a route. The best route is shown in **blue**, and other options are gray.

If you're starting from where you are now, Maps can give turn-by-turn directions as you go. To see the list of turns before you leave, tap **Preview**.

## tr091-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I find my way to a new place

**ASSISTANT:**
I can help. Do you have **Google Maps** or another maps app on your phone? And is your phone an **iPhone** or an **Android** phone?

## tr091-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
directions to

**ASSISTANT:**
It looks like your message got cut off. **Where would you like to go?** And will you be driving, taking transit, or walking?

## tr091-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Maps (phone)
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I find my way to a new place

**ASSISTANT:**
I can help. Do you have **Google Maps** or another maps app on your phone? And is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, Google Maps

**ASSISTANT:**
Great.

Here's how. It takes about a minute.

1. Open the **Google Maps** app.
2. Tap the search bar and type the address or name of the place.
3. Tap the correct result.
4. Tap **Directions** at the bottom left.
5. Choose how you're traveling: **driving**, **transit**, or **walking**.
6. Pick a route. The best route is shown in **blue**, and other options are gray.

If you're starting from where you are now, Maps can give turn-by-turn directions as you go. To see the list of turns before you leave, tap **Preview**.

## tr093-a
- scenario: direct | style: plain | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
My book club meets on Zoom now and they emailed me a link. How do I join from my computer?

**ASSISTANT:**
Joining with a link is pretty simple. The first time, give yourself 5 to 10 minutes before the meeting starts.

1. Open the email and **click the Zoom link**.
2. Your web browser will open a page asking if you want to **open Zoom Meetings**.
3. Click the button to open it. Depending on your computer, it may say **Open Zoom Meetings**, **Allow**, or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

## tr093-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
how do I get on a zoom call

**ASSISTANT:**
Happy to help. Do you have a **link** to the meeting, maybe in an email or text? And will you join from a **computer**, **phone**, or **tablet**?

## tr093-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
Since my knees got bad I can't drive to my book club anymore, so the ladies started doing it on Zoom. My friend emailed me the link for Thursday but I've never done a Zoom before and I'm nervous I'll mess it up.

**ASSISTANT:**
You won't mess it up, and it's lovely that your book club found a way to keep you in. Here's what to do on Thursday:

Joining with a link is pretty simple. The first time, give yourself 5 to 10 minutes before the meeting starts.

1. Open the email and **click the Zoom link**.
2. Your web browser will open a page asking if you want to **open Zoom Meetings**.
3. Click the button to open it. Depending on your computer, it may say **Open Zoom Meetings**, **Allow**, or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

## tr093-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
how do I get on a zoom call

**ASSISTANT:**
Happy to help. Do you have a **link** to the meeting, maybe in an email or text? And will you join from a **computer**, **phone**, or **tablet**?

**USER:**
I have a link in my email. I'll use my laptop.

**ASSISTANT:**
Great, having the link makes it easy.

Joining with a link is pretty simple. The first time, give yourself 5 to 10 minutes before the meeting starts.

1. Open the email and **click the Zoom link**.
2. Your web browser will open a page asking if you want to **open Zoom Meetings**.
3. Click the button to open it. Depending on your computer, it may say **Open Zoom Meetings**, **Allow**, or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

## tr094-a
- scenario: direct | style: plain | specification: fully_specified | platform: YouTube
- task: Turn on captions (YouTube) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I turn on captions for a YouTube video on my phone? I can't hear it well.

**ASSISTANT:**
Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.

## tr094-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on captions (YouTube) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
can I see the words on videos

**ASSISTANT:**
Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?

## tr094-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Turn on captions (YouTube) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
captions

**ASSISTANT:**
Sure. Where would you like to turn on captions: **YouTube**, a **video call**, your **phone** in general, or somewhere else?

## tr094-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: YouTube
- task: Turn on captions (YouTube) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
can I see the words on videos

**ASSISTANT:**
Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?

**USER:**
YouTube on my phone

**ASSISTANT:**
Great.

Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.

## tr095-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone (iCloud Backup)
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
How do I back up my whole iPhone to iCloud before I get a new phone?

**ASSISTANT:**
Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.

## tr095-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
how do I make sure I don't lose anything on my phone

**ASSISTANT:**
A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?

## tr095-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
My phone is getting old and my son is going to help me switch to a new one next month. I'm scared I'll lose my pictures and messages from my late husband.

**ASSISTANT:**
Those are precious, and it's wise to protect them before switching. A backup saves a copy of everything.

**Is your phone an iPhone or an Android phone?** Then I'll walk you through backing it up.

## tr095-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone (iCloud Backup)
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
how do I make sure I don't lose anything on my phone

**ASSISTANT:**
A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks. An iCloud backup saves a copy of your iPhone.

Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.

## tr096-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
What is Stolen Device Protection on iPhone and how do I turn it on?

**ASSISTANT:**
Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.

## tr096-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
how do I protect my iPhone if it gets stolen

**ASSISTANT:**
Good thing to set up ahead of time. Are you asking about **protecting it before** anything happens, or **what to do now** because it's already been stolen?

## tr096-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
stolen device

**ASSISTANT:**
Do you mean **Stolen Device Protection**, the iPhone setting that protects your phone if it's stolen? Or has your phone **been stolen**? Let me know so I can help with the right thing.

## tr096-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
how do I protect my iPhone if it gets stolen

**ASSISTANT:**
Good thing to set up ahead of time. Are you asking about **protecting it before** anything happens, or **what to do now** because it's already been stolen?

**USER:**
Before, just in case

**ASSISTANT:**
Great. One of the best protections is called Stolen Device Protection.

Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.

## tr097-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Turn on live captions (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/9350862?hl=en

**USER:**
How do I turn on Live Caption on my Android phone so I can read what people say in videos?

**ASSISTANT:**
**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.

## tr097-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on live captions (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/9350862?hl=en

**USER:**
I can't hear people on videos well, can my phone show the words?

**ASSISTANT:**
Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?

## tr097-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Turn on live captions (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/9350862?hl=en

**USER:**
My hearing isn't what it used to be and my grandkids send me videos all the time. I just nod along but I can't make out what they're saying.

**ASSISTANT:**
Your phone may be able to show captions for those videos so you can read along.

**Is your phone an iPhone or an Android phone?**

## tr097-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn on live captions (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/9350862?hl=en

**USER:**
I can't hear people on videos well, can my phone show the words?

**ASSISTANT:**
Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, a Pixel

**ASSISTANT:**
Thanks. On Android, this is called Live Caption.

**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.

## tr098-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
How do I make just the text bigger on my Windows 11 computer?

**ASSISTANT:**
You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.

## tr098-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
the writing on my computer is too small

**ASSISTANT:**
I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**? And do you want **just the text** bigger, or **everything** on the screen?

## tr098-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
make text

**ASSISTANT:**
It looks like your message got cut off. Do you want to **make text bigger**? If so, on which device: a computer or a phone?

## tr098-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
the writing on my computer is too small

**ASSISTANT:**
I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**? And do you want **just the text** bigger, or **everything** on the screen?

**USER:**
Windows 11, just the text

**ASSISTANT:**
Got it.

You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.

## tr099-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
Why does my iPhone stop charging at 80% overnight? Is something wrong with it?

**ASSISTANT:**
Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.

## tr099-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge all the way

**ASSISTANT:**
Let's figure out why. Is your phone an **iPhone** or an **Android** phone? And does it stop at a certain number, like **80%**?

## tr099-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
I plug in my iPhone every night before bed and when I wake up it says 80% and charging is on hold or something. I thought my charger was broken so I bought a new one but it does the same thing.

**ASSISTANT:**
Your charger is probably fine.

Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.

## tr099-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge all the way

**ASSISTANT:**
Let's figure out why. Is your phone an **iPhone** or an **Android** phone? And does it stop at a certain number, like **80%**?

**USER:**
iPhone, it always stops at 80%

**ASSISTANT:**
Thanks, that detail helps.

Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.

## tr101-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: True
- sources: https://support.apple.com/en-us/105103

**USER:**
My iPhone only vibrates when someone calls. It doesn't ring. How do I fix that?

**ASSISTANT:**
Your iPhone is probably in **Silent mode**. Here's how to check.

**If your iPhone has a small switch on the side** (above the volume buttons):
1. Look at the switch. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

**If your iPhone has an Action button instead** (iPhone 15 Pro and newer):
1. **Press and hold** the **Action button** until you see Silent mode turn off at the top of the screen. By default, this button turns Silent mode on and off. If it's been set to do something else, tell me and we'll check another way.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.

## tr101-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
my phone isn't ringing, only buzzing

**ASSISTANT:**
That usually means a silent setting is on. Is your phone an **iPhone** or an **Android** phone?

## tr101-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
phone wont ring just

**ASSISTANT:**
It sounds like your phone only **vibrates** or stays **silent** when someone calls. Is that right? And is it an iPhone or an Android phone?

## tr101-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
my phone isn't ringing, only buzzing

**ASSISTANT:**
That usually means a silent setting is on. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone 13

**ASSISTANT:**
Thanks. On an iPhone 13, it's usually the switch on the side.

Your iPhone is probably in **Silent mode**. Here's how to check.

**If your iPhone has a small switch on the side** (above the volume buttons):
1. Look at the switch. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

**If your iPhone has an Action button instead** (iPhone 15 Pro and newer):
1. Press the **Action button**. By default, it turns Silent mode on and off. If it's been set to do something else, tell me and we'll check another way.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.

## tr102-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Have the phone read the screen aloud (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

**USER:**
Can my Android phone read the words on the screen out loud to me?

**ASSISTANT:**
Yes, with a feature called **Select to Speak**. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Select to Speak**.
4. Turn on the **Select to Speak shortcut**.

If you don't see **Select to Speak**, update the **Android Accessibility Suite** app in the Play Store.

**Use it:**
1. Start it with the shortcut: swipe up from the bottom of the screen with **two fingers**, or tap the **Accessibility button**.
2. Tap any text you want to hear.
3. To hear everything on the screen, tap **Play**.

## tr102-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Have the phone read the screen aloud (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

**USER:**
is there a way to have my phone read things to me

**ASSISTANT:**
Most phones can. Is your phone an **iPhone** or an **Android** phone?

## tr102-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Have the phone read the screen aloud (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

**USER:**
Reading long emails on my phone tires out my eyes. I'd love it if the phone could just read them to me like an audiobook.

**ASSISTANT:**
Many phones can read text out loud.

**Is your phone an iPhone or an Android phone?** I'll show you how to turn it on.

## tr102-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Have the phone read the screen aloud (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

**USER:**
is there a way to have my phone read things to me

**ASSISTANT:**
Most phones can. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

Yes, with a feature called **Select to Speak**. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Select to Speak**.
4. Turn on the **Select to Speak shortcut**.

If you don't see **Select to Speak**, update the **Android Accessibility Suite** app in the Play Store.

**Use it:**
1. Start it with the shortcut: swipe up from the bottom of the screen with **two fingers**, or tap the **Accessibility button**.
2. Tap any text you want to hear.
3. To hear everything on the screen, tap **Play**.

## tr103-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
How do I set a reminder on my iPhone to call the pharmacy tomorrow at 10 AM?

**ASSISTANT:**
You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **info** button (a small "i") next to it.
5. Tap **Date and Time**.
6. Choose **Custom**, pick tomorrow's date, and set the time to **10:00 AM**.
7. Tap **Done**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.

## tr103-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
how do I get my phone to remind me to do something

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone? And what would you like to be reminded about, and when?

## tr103-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
I keep forgetting to call in my prescription refill and then I run out. Tomorrow at 10 is when they open. Can my iPhone remind me?

**ASSISTANT:**
Yes, a reminder will help with that. Here's how to set it for tomorrow at 10:

You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **info** button (a small "i") next to it.
5. Tap **Date and Time**.
6. Choose **Custom**, pick tomorrow's date, and set the time to **10:00 AM**.
7. Tap **Done**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.

## tr103-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
how do I get my phone to remind me to do something

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone? And what would you like to be reminded about, and when?

**USER:**
iPhone. Call the pharmacy tomorrow at 10.

**ASSISTANT:**
Got it.

You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **info** button (a small "i") next to it.
5. Tap **Date and Time**.
6. Choose **Custom**, pick tomorrow's date, and set the time to **10:00 AM**.
7. Tap **Done**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.
