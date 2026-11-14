# Review input: batch fx3, round 2 (5 examples)

## tr034-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates ; https://support.microsoft.com/en-us/windows/troubleshoot-problems-updating-windows-188c2b0f-10a7-d72f-65b8-32d177eb136c

**USER:**
Can you walk me through updating my Windows 11 PC? I've never done it before.

**ASSISTANT:**
Sure, it only takes a few clicks.

1. Click **Start**, then **Settings**.
2. Click **Windows Update**.
3. Click **Check for Windows updates**.
4. If updates are available, click **Download & install**.
5. If Windows asks you to restart, restart to finish the update.

Save your work before restarting.

**USER:**
I clicked Check for Windows updates but it just shows an error.

**ASSISTANT:**
Let's try Windows' built-in fixer.

1. Click **Start**, then **Settings**, then **System**, then **Troubleshoot**, then **Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Make sure you're online: go to **Start**, **Settings**, **Network & Internet**, **Wi-Fi**, and reconnect if needed.
4. Go back to **Settings**, **Windows Update**, and click **Check for Windows updates** again.

If you still get an error, write down the error code and tell me what it says.

## tr039-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes ; https://consumer.ftc.gov/articles/what-do-if-you-were-scammed

**USER:**
A call came in that sounded just like my granddaughter saying she was in trouble. I wired $2,500 through Western Union an hour ago, and now I can't reach her and I'm afraid it was a scam.

**ASSISTANT:**
I'm sorry, this happens to careful people. Please don't send any more money, and contact the wire transfer company right away.

1. **Report it to the wire transfer company immediately.** Tell them a scammer tricked you, and ask for a refund.
2. **Check on your granddaughter.** Call her at a number you know is hers. If you can't reach her, contact her through another family member or her friends.
3. **Report the scam to the FTC** at **ReportFraud.ftc.gov**.

## tr040-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam ; https://consumer.ftc.gov/articles/what-do-if-you-were-scammed

**USER:**
I got a text from USPS about a missed delivery. I clicked the link and typed in my credit card number to pay a $1.99 fee, then got suspicious. What do I do?

**ASSISTANT:**
I'm sorry, these texts look very real and fool many people. Contact your credit card company right away.

1. **Report it to the credit card issuer immediately.** Call the number on the back of your card, or log in to your account online or in the app.
2. Tell them what happened and **ask for a refund**.
3. **Report the text.** Use your messaging app's junk or spam option, or forward it to **7726**.
4. **Report it to the FTC** at **ReportFraud.ftc.gov**.

## tr041-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
My nephew texted me from a new number saying he's stuck at the airport and needs me to buy Google Play gift cards to pay for a rebooked flight, then text him the codes. His regular phone seems to be off, so I can't reach him to check. He says it's really urgent.

**ASSISTANT:**
Please **don't buy the gift cards**. Scammers say it's urgent so you'll rush, so slow down and don't pay. No real business or government agency will ever tell you to buy a gift card to pay them, and gift cards are for gifts only.

1. **Don't reply** and don't send any codes or photos of cards.
2. **Reach your nephew through a number you already know is his**, not the new number that texted you. Scammers may also use voice cloning, so check with him directly.
3. **Report the text** at **ReportFraud.ftc.gov**.

If you've already bought cards or shared the numbers, report it to the gift card company right away and ask for your money back. Keep a copy of the gift card and the store receipt.

## tr043-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
My son's teacher gave me only her email address, no phone number. I have an Android phone. Can I still make a contact for her?

**ASSISTANT:**
Yes. A contact needs a name and either an email address or a phone number.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type her name.
4. Type her email address.
5. Tap **Save**.

If you want to add more details, such as a street address or notes, tap **Add fields** before you tap **Save**.
