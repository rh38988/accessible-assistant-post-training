# Review input: batch ex7, round 2 (31 examples)

## tr089-a
- scenario: direct | style: plain | specification: fully_specified | platform: phone
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
A caller said he's from Social Security and my number has been suspended because of a crime. He wants me to buy gift cards to fix it. What should I do?

**ASSISTANT:**
Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**.

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
Please don't pay or share any personal information yet, and don't call back any number they gave you. **Which agency did the caller say they were from?**

## tr089-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: phone
- task: Caller claims to be from Social Security (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

**USER:**
Got a call from the government saying I owe money. Is that real?

**ASSISTANT:**
Please don't pay or share any personal information yet, and don't call back any number they gave you. **Which agency did the caller say they were from?**

**USER:**
Social Security. They said I need to buy gift cards or my number will be suspended.

**ASSISTANT:**
Thank you.

Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**.

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
You may find it easier to use a **passphrase**: a series of random words separated by spaces. It may be easier to remember.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Make sure the words in a passphrase are random.
2. **If you used the same or a similar password on other sites, change it there too.**
3. **Avoid common phrases, song lyrics, or movie quotes**, because hacking programs can guess them.
4. **A password manager, or your web browser,** can create strong passwords and save them for you.
5. **Turn on two-factor authentication** where you can. Then a hacker who steals your password still can't log in without another step.

Protect your **email** account with a strong password, because a hacker who takes it over can get password reset links for your other accounts.

## tr090-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Make a strong password (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

**USER:**
I use my dog's name and my birthday for everything because that's the only way I remember. My grandson says that's not safe. What should I do instead?

**ASSISTANT:**
Your grandson has a good point. Since you use the same password everywhere, you should change it on every site. Here are some tips for new ones.

You may find it easier to use a **passphrase**: a series of random words separated by spaces. It may be easier to remember.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Make sure the words in a passphrase are random.
2. **If you used the same or a similar password on other sites, change it there too.**
3. **Avoid common phrases, song lyrics, or movie quotes**, because hacking programs can guess them.
4. **A password manager, or your web browser,** can create strong passwords and save them for you.
5. **Turn on two-factor authentication** where you can. Then a hacker who steals your password still can't log in without another step.

Protect your **email** account with a strong password, because a hacker who takes it over can get password reset links for your other accounts.

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

You may find it easier to use a **passphrase**: a series of random words separated by spaces. It may be easier to remember.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Make sure the words in a passphrase are random.
2. **If you used the same or a similar password on other sites, change it there too.**
3. **Avoid common phrases, song lyrics, or movie quotes**, because hacking programs can guess them.
4. **A password manager, or your web browser,** can create strong passwords and save them for you.
5. **Turn on two-factor authentication** where you can. Then a hacker who steals your password still can't log in without another step.

Protect your **email** account with a strong password, because a hacker who takes it over can get password reset links for your other accounts.

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

To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap **Preview**.

## tr091-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I find my way to a new place

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone?

## tr091-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
directions to

**ASSISTANT:**
It looks like your message got cut off. Are you using an **iPhone** or an **Android** phone?

## tr091-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Maps (phone)
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I find my way to a new place

**ASSISTANT:**
I can help. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, and I use Google Maps

**ASSISTANT:**
Great.

Here's how. It takes about a minute.

1. Open the **Google Maps** app.
2. Tap the search bar and type the address or name of the place.
3. Tap the correct result.
4. Tap **Directions** at the bottom left.
5. Choose how you're traveling: **driving**, **transit**, or **walking**.
6. Pick a route. The best route is shown in **blue**, and other options are gray.

To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap **Preview**.

## tr093-a
- scenario: direct | style: plain | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
My book club meets on Zoom now and they emailed me a link. How do I join from my computer?

**ASSISTANT:**
Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
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
Happy to help. Did someone send you a **link** to the meeting, in an email or a text?

## tr093-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

**USER:**
Since my knees got bad I can't drive to my book club anymore, so the ladies started doing it on Zoom. My friend emailed me the link for Thursday but I've never done a Zoom before and I'm nervous I'll mess it up.

**ASSISTANT:**
You won't mess it up, and it's lovely that your book club found a way to keep you in. Here's what to do on Thursday:

Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
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
Happy to help. Did someone send you a **link** to the meeting, in an email or a text?

**USER:**
Yes, I have a link in my email.

**ASSISTANT:**
Great, having the link makes it easy.

Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.

## tr095-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone (iCloud Backup)
- task: Back up the whole phone (iPhone (iCloud Backup)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108366

**USER:**
How do I back up my whole iPhone to iCloud before I get a new phone?

**ASSISTANT:**
Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name**.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.

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
2. Open **Settings** and tap **your name**.
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

It needs a few things to work: an iPhone updated to **iOS 17.3 or later**, a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.

## tr096-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
how do I protect my phone if it gets stolen

**ASSISTANT:**
Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?

## tr096-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
stolen device

**ASSISTANT:**
Do you want to turn on **Stolen Device Protection**, the iPhone setting that helps protect your phone if it is stolen?

## tr096-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn on Stolen Device Protection (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/120340

**USER:**
how do I protect my phone if it gets stolen

**ASSISTANT:**
Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Great. A helpful setting is called Stolen Device Protection.

Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: an iPhone updated to **iOS 17.3 or later**, a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.

## tr098-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
the writing on my computer is too small

**ASSISTANT:**
I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**?

## tr098-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Make text bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
make text

**ASSISTANT:**
It looks like your message got cut off. Do you want to make the text bigger on a **computer** or on a **phone**?

## tr099-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge all the way

**ASSISTANT:**
Let's figure out why. Is your phone an **iPhone** or an **Android** phone?

## tr101-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Phone only vibrates, does not ring (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
phone wont ring just

**ASSISTANT:**
It sounds like your phone only vibrates when someone calls. Is it an **iPhone** or an **Android** phone?

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
Thanks.

Your iPhone is probably in **Silent mode**. Here's how to check.

1. Look at the switch on the side of your iPhone. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

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
1. Start it with the shortcut: swipe up with **two fingers**, or tap the **Accessibility button**. If TalkBack is on, use a **three-finger** swipe up instead.
2. Tap any text you want to hear.
3. To hear everything on the screen, tap **Play**.

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
1. Start it with the shortcut: swipe up with **two fingers**, or tap the **Accessibility button**. If TalkBack is on, use a **three-finger** swipe up instead.
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
4. Tap the **Date and Time** button.
5. To set your own day and time, tap **Custom**, then pick tomorrow's date and set the time to **10:00 AM**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.

## tr103-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
how do I get my phone to remind me to do something

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

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
4. Tap the **Date and Time** button.
5. To set your own day and time, tap **Custom**, then pick tomorrow's date and set the time to **10:00 AM**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.

## tr103-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
how do I get my phone to remind me to do something

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. Call the pharmacy tomorrow at 10.

**ASSISTANT:**
Got it.

You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **Date and Time** button.
5. To set your own day and time, tap **Custom**, then pick tomorrow's date and set the time to **10:00 AM**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.
