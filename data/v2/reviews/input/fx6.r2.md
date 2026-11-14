# Review input: batch fx6, round 2 (8 examples)

## tr076-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Scan a QR code (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102680

**USER:**
My iPhone screen is asleep on the counter and my hands are messy from cooking. Is there a quicker way to get to the camera for the QR code on my recipe card, without hunting for apps?

**ASSISTANT:**
Yes, you can open the camera straight from the Lock Screen.

1. Open the **Camera** from the Lock Screen.
2. Hold your iPhone so the QR code is in view.
3. Tap the **link** that appears over the code.

The link or content from the code will open.

You can also open the camera from **Control Center**. On supported iPhone models you can also open the camera with the **Camera Control** button.

## tr079-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Add emergency information (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/9319337?hl=en

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
2. If you or someone else turned the app off (disabled it), it will not show in your app list.
3. This app is only on some Android phones, so yours may not have it.
4. On Android 12 and earlier without the app, you can still sign in with your Google Account, add emergency contacts, and list medical information.

## tr083-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Find a downloaded file (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

**USER:**
I'm on Windows 11 and I saved a tax paper last week but I can't remember where. All I remember is the name started with 'W2'. I don't want to open folder after folder. Can I just search for it?

**ASSISTANT:**
Yes. You can search by name instead of opening folders.

1. Press the **Windows logo key** and **E** together to open File Explorer.
2. Select **Home** in the left pane.
3. In **Home**, search for the part of the name you remember, such as **W2**. Matching files on your PC will be listed.

On Windows 11 version 22H2 or later, **Downloads** is pinned under **Quick access** on **Home**, so you can open it too.

## tr086-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
An email says my payment info for my streaming service is out of date and my account will be closed in 24 hours unless I click the link. I can't call anyone until Monday, it's Saturday. Should I just click it to be safe?

**ASSISTANT:**
Please don't click the link. Real companies won't email you a link to update your payment information.

1. Leave the email alone for now. You don't have to do anything about it today.
2. On Monday, if you want to check your account, contact the company using a phone number or website you know is real, not anything in the email.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

Links and attachments in a scam email can also install harmful software.

## tr086-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams ; https://consumer.ftc.gov/articles/what-do-if-you-were-scammed

**USER:**
I clicked the link in an email that said it was from my bank, and I typed in my credit card number. Now I think it was fake. What do I do?

**ASSISTANT:**
Thank you for telling me. Please act on this right away, starting with your credit card company.

1. Call your credit card company right away, using the number on the back of your card, and tell them you gave your card number to a scammer. Ask them to refund any charges.
2. Go to **IdentityTheft.gov**. It gives steps based on what information you gave away.
3. Because you clicked a link, update your security software, run a scan, and remove anything it flags.
4. Report the email at **ReportFraud.ftc.gov**, and forward it to **reportphishing@apwg.org**.

## tr087-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
I get fake package delivery texts. I don't know how to copy a text and send it to another number, and I don't use a computer. Is there another way to report them?

**ASSISTANT:**
Yes. You do not have to copy and forward the text. Please don't click any link in it.

1. Open the text in your messaging app and look for an option to **report junk or spam**.
2. If you are able to open web pages on your phone, you can also report it at **ReportFraud.ftc.gov**.
3. Ask your phone company about tools that block unwanted texts.

Real delivery companies don't ask for your account information by text. If you think a delivery might be real, contact the company using a phone number or website you know is real, not the one in the text.

## tr087-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: phone
- task: Report a spam text message (phone) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

**USER:**
I tapped the link in a text that said my package was delayed. A page came up asking me to log in, so I closed it right away without typing anything. Did I do something bad?

**ASSISTANT:**
You did the right thing by closing it. Please don't open that link again.

1. Don't type any information into that page if you open it again by accident.
2. If you think the package could be real, contact the company using a phone number or website you know is real, not the details in the text.
3. Forward the text to **7726** (SPAM), and report it at **ReportFraud.ftc.gov**.

Links in scam texts can lead to fake websites that look real, and some can install harmful software. Closing the page right away without typing anything is a good move.

## tr088-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
A man I met on a dating site wants me to move our chats to email, and now he says he needs money for a visa so he can visit me. He asked me not to tell my kids because they won't understand. I really do care about him. What should I do?

**ASSISTANT:**
Please don't send him any money. Never send money or gifts to someone you haven't met in person.

What you describe matches signs of a romance scam: asking to move off the site and asking for money for a visa.

1. Stop communicating with him right away.
2. Talk to a trusted friend or family member, including your kids, and listen if they voice concerns.
3. Do a reverse image search on his profile photo to see if it is linked to other names.
4. Report it at **ReportFraud.ftc.gov**, and tell the dating site.

I know this is hard when you care about someone.
