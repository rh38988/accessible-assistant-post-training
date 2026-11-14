# Review input: batch fx6, round 3 (6 examples)

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
3. Tap the **link**.

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
2. If the app has been turned off (disabled), it will not show in your app list.
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
3. In **Home**, search for the file by the name you remember.

The search looks for relevant files on your PC and in your cloud accounts.

On Windows 11 version 22H2 or later, **Downloads** is pinned under **Quick access** on **Home**, so you can open it too.

## tr086-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: email
- task: Is this email asking me to log in real? (email) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

**USER:**
An email says my payment info for my streaming service is out of date and my account will be closed in 24 hours unless I click the link. I can't call anyone until Monday, it's Saturday. Should I just click it to be safe?

**ASSISTANT:**
Please don't click the link. Real companies won't email you a link to update your payment information.

1. Do not click anything in the email. Report it now, as in step 3.
2. To check your streaming account, contact the company using a website or phone number you already know is real, not anything in the email.
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
2. If a scammer used your Social Security number, go to **IdentityTheft.gov** to report it.
3. If you gave a scammer access to your computer or phone, update your security software to make sure you have the latest protections. Then run a scan and delete anything it identifies as a problem.
4. Report the email at **ReportFraud.ftc.gov**, and forward it to **reportphishing@apwg.org**.

## tr088-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Online friend asks for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

**USER:**
A man I met on a dating site wants me to move our chats to email, and now he says he needs money for a visa so he can visit me. He asked me not to tell my kids because they won't understand. I really do care about him. What should I do?

**ASSISTANT:**
Please don't send him any money. Never send money or gifts to someone you haven't met in person.

What you describe matches signs of a romance scam: asking to move off the site and asking for money for a visa.

1. Talk to someone you trust about what is happening.
2. Do a reverse image search of his profile photo. This is a search that finds other places online where the same photo appears.
3. Report it at **ReportFraud.ftc.gov**, and tell the dating site.

I know this is hard when you care about someone.
