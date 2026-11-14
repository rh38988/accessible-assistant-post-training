# Review input: batch ex6, round 2 (37 examples)

## tr076-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

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
Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The page or app that the code is for will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed by a business you know.

## tr077-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

**USER:**
qr code wont

**ASSISTANT:**
It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?

## tr077-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Scan a QR code (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en ; https://support.google.com/pixelphone/answer/16561572?hl=en

**USER:**
how do I read one of those square codes with my phone

**ASSISTANT:**
Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, Pixel

**ASSISTANT:**
Thanks. Your Pixel's camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the lens at the code so the whole code is on the screen. You don't need to take a photo.
3. Wait a moment for a bubble or link to appear, then tap it.

If nothing appears, tap the **Settings** icon in Camera, tap **More settings**, and make sure **Camera scan suggestions** is on.

You can also swipe down from the top and tap **Scan QR code**.

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
2. Tap **Summary**.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Turn on **Show When Locked** so it can be seen from the Lock Screen.
6. Tap **Add** next to a section, like **Allergies**, and type your information.
7. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you. Then tap **Done**.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.

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
2. Tap **Summary**.
3. Tap your **profile picture** in the upper corner.
4. Tap **Medical ID**.
5. Turn on **Show When Locked** so it can be seen from the Lock Screen.
6. Tap **Add** next to a section, like **Allergies**, and type your information.
7. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you. Then tap **Done**.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.

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

If you don't see **Notifications** for that app, the app may not be able to send notifications.

## tr080-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
how do I stop all these pop-ups on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr080-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

**USER:**
notifications keep

**ASSISTANT:**
It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?

## tr080-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn off notifications from an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120681

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
3. Find the shopping app. If it's not in the list, open the dropdown and tap **All apps**.
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
Yes, you can turn off an app's notifications. Is your phone an **iPhone** or an **Android** phone?

## tr081-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
Ever since I bought shoes online, my phone buzzes all day with sales and coupons. I just want it to stop.

**ASSISTANT:**
That sounds tiring. Is your phone an **iPhone** or an **Android** phone?

## tr081-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn off notifications from an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9079661?hl=en

**USER:**
can I make an app stop bugging me

**ASSISTANT:**
Yes, you can turn off an app's notifications. Is your phone an **iPhone** or an **Android** phone?

**USER:**
A shopping app on my Android

**ASSISTANT:**
Thanks.

You can turn them off for just that app. It takes less than a minute.

**Option 1, from Settings:**
1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Find the shopping app. If it's not in the list, open the dropdown and tap **All apps**.
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
1. At the top right of Chrome, click **More**.
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.

## tr082-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
the words on this website are too small

**ASSISTANT:**
I can help you make them bigger. Are you on a **computer**, a **phone**, or a **tablet**?

## tr082-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
chrome zoom

**ASSISTANT:**
Sure. Are you using Chrome on a **computer**, a **phone**, or a **tablet**?

## tr082-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Make a web page bigger (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

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
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.

## tr083-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I downloaded a form from a website on my Windows computer. Where did it go?

**ASSISTANT:**
Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.
2. In the list on the left, click **Downloads** (under **Quick access**).
3. Your downloaded form should be in the list.

If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.

## tr083-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I can't find something I downloaded

**ASSISTANT:**
Let's find it. Is this on a **Windows computer**, a **Mac**, or a **phone**?

## tr083-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
My insurance company emailed me a link to download my card as a PDF and I clicked it and something happened at the bottom of the screen but then it disappeared and now I have no idea where the card is. It's a Windows computer.

**ASSISTANT:**
It's most likely in your **Downloads** folder. Here's how to find it.

1. Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.
2. In the list on the left, click **Downloads** (under **Quick access**).
3. Your downloaded insurance card PDF should be in the list.

If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.

## tr083-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I can't find something I downloaded

**ASSISTANT:**
Let's find it. Is this on a **Windows computer**, a **Mac**, or a **phone**?

**USER:**
Windows computer

**ASSISTANT:**
Thanks.

Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.
2. In the list on the left, click **Downloads** (under **Quick access**).
3. Your downloaded file should be in the list.

If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.

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
5. You can also change the pointer's **color** so it stands out more.

Try a few sizes until it's easy to find.

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
5. You can also change the pointer's **color** so it stands out more.

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

After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.

**Never share a verification code with anyone.** Google will not call you to ask for one.

If you use a work or school account, your administrator may control this setting.

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

After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.

**Never share a verification code with anyone.** Google will not call you to ask for one.

If you use a work or school account, your administrator may control this setting.

## tr086-a
- scenario: direct | style: plain | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
I got an email that looks like it's from my bank saying my account is locked and I need to click a link to log in and fix it. Is it real?

**ASSISTANT:**
Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but a link can carry malware.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, contact your bank using a phone number or website you already know is real, not anything from the email.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked a link or opened an attachment, update your computer's security software, run a scan, and remove anything it finds. If you gave out personal information, go to **IdentityTheft.gov** for next steps.

## tr086-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
I got a weird email, should I click on it?

**ASSISTANT:**
Good thinking to check first. Please don't click anything yet. **Who does the email say it's from?**

## tr086-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
is this email from

**ASSISTANT:**
It looks like your message got cut off. Please don't click any links in it until we check. **Who does the email say it's from?**

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

Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but a link can carry malware.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, contact your bank using a phone number or website you already know is real, not anything from the email.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked a link or opened an attachment, update your computer's security software, run a scan, and remove anything it finds. If you gave out personal information, go to **IdentityTheft.gov** for next steps.

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
There are a couple of things you can do about junk texts. Is your phone an **iPhone** or an **Android** phone?

## tr087-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
Every few days I get a text saying my toll bill is overdue or my account needs verifying. I never click them but I want to do something so they stop.

**ASSISTANT:**
Good for you for not clicking. Reporting them helps your phone company block more of these. Here's how:

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

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
There are a couple of things you can do about junk texts. Is your phone an **iPhone** or an **Android** phone?

**USER:**
I want to report them. Android phone.

**ASSISTANT:**
Thanks. Reporting is a great idea.

Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.

## tr088-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
my online friend needs money for an emergency, should I help?

**ASSISTANT:**
I'm glad you asked first. Please don't send any money or gift cards yet. **Have you met this person in person?**

## tr088-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
I've been talking to someone special online and he's asking me for help. I don't know what to do.

**ASSISTANT:**
Thank you for trusting me with this. Please don't send money or gift cards to someone you haven't met in person. **What kind of help is he asking for?**

## tr088-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
my online friend needs money for an emergency, should I help?

**ASSISTANT:**
I'm glad you asked first. Please don't send any money or gift cards yet. **Have you met this person in person?**

**USER:**
No, we've only talked online for three months. He wants me to wire $2,000 for a plane ticket.

**ASSISTANT:**
Thank you for telling me.

I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- After lots of friendly messages, they ask for **money** for emergencies, travel, or fees.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. Stop talking to him, then report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.
