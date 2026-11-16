# Rule scan input, part 04 (50 examples)

## tr038-b
- task: Reset forgotten Google Account password | platform: Google Account | scenario: missing_info | sensitive: True
- sources: Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
I can't get into my email

**ASSISTANT:**
That's stressful, but it can usually be fixed. **Which email do you use**, for example Gmail, which ends in @gmail.com?

---

## tr038-d
- task: Reset forgotten Google Account password | platform: Google Account | scenario: followup | sensitive: True
- sources: Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
I can't get into my email

**ASSISTANT:**
That's stressful, but it can usually be fixed. **Which email do you use**, for example Gmail, which ends in @gmail.com?

**USER:**
Gmail, I forgot the password

**ASSISTANT:**
Thanks. You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to **accounts.google.com/signin/recovery** (Google's account recovery page).
2. Answer the questions it asks to show the account is yours. Answer as accurately as you can, and if you're not sure, make your best guess. A wrong guess doesn't end the process, and you can try again.
3. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If you recently changed your recovery info, it can take up to 7 days to take effect, so try again after a few days.

---

## tr038-e
- task: Reset forgotten Google Account password | platform: Google Account | scenario: constraint | sensitive: True
- sources: Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
I'm not good with websites. I'd rather just phone Google and have them reset my Gmail password for me. What's their number?

**ASSISTANT:**
Google can't help you sign in over the phone, so there's no number to call for this. Please be careful with anyone who offers to recover your account for you, because Google doesn't work with account or password recovery services. Never give out your password or any verification codes.

The way back in is Google's recovery page, which asks you some questions:

1. Go to **https://accounts.google.com/signin/recovery?ec=ar_hc_7682439**.
2. Answer the questions as accurately as you can. They confirm it's your account.
3. When prompted, reset your password. Choose a strong one you haven't used with this account.

---

## tr038-r
- task: Reset forgotten Google Account password | platform: Google Account | scenario: failure_recovery | sensitive: True
- sources: Google Account Help: How to recover your Google Account or Gmail <https://support.google.com/accounts/answer/7682439?hl=en>

**USER:**
My grandson says I need to reset my Google password. I use it for email on my tablet. How do I do that?

**ASSISTANT:**
You can do it on Google's recovery page.

1. Go to **https://accounts.google.com/signin/recovery?ec=ar_hc_7682439**.
2. Answer the questions as accurately as you can. They confirm it's your account.
3. When prompted, reset your password. Choose a strong one you haven't used with this account.

Never share your password or any verification code with anyone, and remember that Google can't help you sign in over the phone.

**USER:**
I answered the questions but it says it can't tell it's my account.

**ASSISTANT:**
Don't worry, you can try again.

1. Go through the questions again and answer as accurately as you can. Wrong guesses don't end the process, and there's no limit on tries.
2. Read Google's tips for trouble at **https://support.google.com/accounts/answer/7299973**.
3. If you changed your recovery information recently, the change can take up to 7 days to take effect. Try again in a few days.

---

## tr039-a
- task: Call that sounds like a family member's voice asking for money | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes <https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes>

**USER:**
My granddaughter called crying and said she's in jail and needs bail money wired right now. It really sounded like her. Is this real?

**ASSISTANT:**
Please **don't send any money yet**. Scammers can now copy a person's voice from a short recording, like a video posted online, so a call can sound exactly like someone you love.

Here's what to do:

1. **Don't trust the voice**, even if it sounds like her. Call your granddaughter on a phone number you know is hers, not a number from the call.
2. If you can't reach her, try another family member or her friends.

**Warning sign:** Scammers ask you to pay in ways that make it hard to get your money back: wire money, cryptocurrency, or gift cards.

If it turns out to be a scam, you can report it at **ReportFraud.ftc.gov**. If you already sent money, tell me right away and we'll work out the next steps.

---

## tr039-b
- task: Call that sounds like a family member's voice asking for money | platform: any | scenario: missing_info | sensitive: True
- sources: FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes <https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes>

**USER:**
Someone called and said my granddaughter needs money, what should I do?

**ASSISTANT:**
I'm glad you asked before doing anything. **Please don't send any money yet.** Have you already sent anything, or are you still deciding?

---

## tr039-c
- task: Call that sounds like a family member's voice asking for money | platform: any | scenario: missing_info | sensitive: True
- sources: FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes <https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes>

**USER:**
Got a strange call last night. Not sure what to make of it.

**ASSISTANT:**
I'm happy to help you figure it out. Please don't send money or share any codes or personal details until we check. **What did the caller say?**

---

## tr039-d
- task: Call that sounds like a family member's voice asking for money | platform: any | scenario: followup | sensitive: True
- sources: FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes <https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes>

**USER:**
Someone called and said my granddaughter needs money, what should I do?

**ASSISTANT:**
I'm glad you asked before doing anything. **Please don't send any money yet.** Have you already sent anything, or are you still deciding?

**USER:**
I haven't sent anything. They wanted me to wire $3,000, and the voice sounded just like her.

**ASSISTANT:**
Thank you for telling me, and I'm glad you haven't sent anything. A request to wire money is a warning sign, even when the voice sounds right.

Please **don't send any money yet**. Scammers can now copy a person's voice from a short recording, like a video posted online, so a call can sound exactly like someone you love.

Here's what to do:

1. **Don't trust the voice**, even if it sounds like her. Call your granddaughter on a phone number you know is hers, not a number from the call.
2. If you can't reach her, try another family member or her friends.

**Warning sign:** Scammers ask you to pay in ways that make it hard to get your money back: wire money, cryptocurrency, or gift cards.

If it turns out to be a scam, you can report it at **ReportFraud.ftc.gov**. If you already sent money, tell me right away and we'll work out the next steps.

---

## tr039-e
- task: Call that sounds like a family member's voice asking for money | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes <https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes>

**USER:**
My grandson called from a number I don't know, sounding scared, and said he'd been in a car accident and needs $2,000 sent through Western Union. He begged me not to tell his parents. I've tried his own phone but it goes straight to voicemail.

**ASSISTANT:**
Please **don't send any money**. Scammers can copy a person's voice, sometimes from a short recording posted online, so a call can sound just like your grandson. Don't trust the voice.

1. **Hang up** if you haven't already.
2. **Call him again** at the number you already know is his, not the number that called you.
3. Since you can't reach him, **contact him through another family member or his friends**. That includes his parents, even though the caller asked you not to tell them.

Asking you to wire money, send cryptocurrency, or buy gift cards are warning signs, because those payments are hard to get back.

You can report the call at **ReportFraud.ftc.gov**.

---

## tr039-r
- task: Call that sounds like a family member's voice asking for money | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes <https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes>; FTC Consumer Advice: What To Do if You Were Scammed <https://consumer.ftc.gov/articles/what-do-if-you-were-scammed>

**USER:**
A call came in that sounded just like my granddaughter saying she was in trouble. I wired $2,500 through Western Union an hour ago, and now I can't reach her and I'm afraid it was a scam.

**ASSISTANT:**
I'm sorry, this happens to careful people. Please don't send any more money, and contact the wire transfer company right away.

1. **Report it to the wire transfer company immediately.** Tell them a scammer tricked you, and ask for a refund.
2. **Check on your granddaughter.** Call her at a number you know is hers. If you can't reach her, contact her through another family member or her friends.
3. **Report the scam to the FTC** at **ReportFraud.ftc.gov**.

---

## tr040-a
- task: Text says package could not be delivered | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Alert: Think that text message is from USPS? It could be a scam <https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam>

**USER:**
I got a text saying USPS couldn't deliver my package and I need to click a link to update my address. I am expecting a package. Should I click it?

**ASSISTANT:**
Please **don't click the link**. Texts like this are a common scam, even when you really are expecting a package. The link usually leads to a fake website that looks real and asks for your personal or card information.

Instead:

1. **Don't click** the link or give any information.
2. Check on your package using the website or app of the **store where you bought it**. Go there directly, not through the text.
3. **Report the text.** Use your messaging app's **junk** or **spam** report option. If there isn't one, forward the text to **7726**. You can also tell the FTC at **ReportFraud.ftc.gov**.

If you already clicked the link or typed in any information, tell me and we'll look at what to do next.

---

## tr040-b
- task: Text says package could not be delivered | platform: any | scenario: missing_info | sensitive: True
- sources: FTC Consumer Alert: Think that text message is from USPS? It could be a scam <https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam>

**USER:**
I got a text about a package, is it real?

**ASSISTANT:**
Let's check it together. For now, **please don't click any link or give any information** in that text. **What does the text ask you to do?**

---

## tr040-c
- task: Text says package could not be delivered | platform: any | scenario: missing_info | sensitive: True
- sources: FTC Consumer Alert: Think that text message is from USPS? It could be a scam <https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam>

**USER:**
usps text link

**ASSISTANT:**
If you got a text that looks like it's from **USPS** with a link in it, please **don't click the link** yet. **What does the text ask you to do?**

---

## tr040-d
- task: Text says package could not be delivered | platform: any | scenario: followup | sensitive: True
- sources: FTC Consumer Alert: Think that text message is from USPS? It could be a scam <https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam>

**USER:**
I got a text about a package, is it real?

**ASSISTANT:**
Let's check it together. For now, **please don't click any link or give any information** in that text. **What does the text ask you to do?**

**USER:**
It has a link and says I need to pay $1.99 for redelivery.

**ASSISTANT:**
Thanks. A small fee plus a link is a very common sign of a scam, even when you really are expecting a package. Please **don't click the link**. It usually leads to a fake website that looks real and asks for your personal or card information.

Instead:

1. **Don't click** the link or reply.
2. Check on your package using the website or app of the **store where you bought it**. Go there directly, not through the text.
3. **Report the text.** Use your phone's **junk** or **spam** reporting option if you see one, or forward the text to **7726**. You can also report it at **ReportFraud.ftc.gov**.
4. Then delete it.

If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.

---

## tr040-r
- task: Text says package could not be delivered | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Alert: Think that text message is from USPS? It could be a scam <https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam>; FTC Consumer Advice: What To Do if You Were Scammed <https://consumer.ftc.gov/articles/what-do-if-you-were-scammed>

**USER:**
I got a text from USPS about a missed delivery. I clicked the link and typed in my credit card number to pay a $1.99 fee, then got suspicious. What do I do?

**ASSISTANT:**
I'm sorry, these texts look very real and fool many people. Contact your credit card company right away.

1. **Report it to the credit card issuer immediately.** Call the number on the back of your card, or log in to your account online or in the app.
2. Tell them what happened and **ask for a refund**.
3. **Report the text.** Use your messaging app's junk or spam option, or forward it to **7726**.
4. **Report it to the FTC** at **ReportFraud.ftc.gov**.

---

## tr041-r
- task: Someone asks to be paid with gift cards | platform: any | scenario: failure_recovery | sensitive: True
- sources: FTC Consumer Advice: Avoiding and Reporting Gift Card Scams <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams>

**USER:**
I got an email from my pastor asking me to buy five $100 gift cards for church members and send him the numbers on the back. He said he's in a meeting and can't talk. Should I do it?

**ASSISTANT:**
Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.

**USER:**
Oh no. I already bought two $100 cards this morning and emailed him the numbers before I saw this.

**ASSISTANT:**
I'm sorry this happened. This scam fools a lot of careful people. Acting quickly gives you the best chance of getting money back.

1. **Contact the gift card company right away.** Tell them the cards were used in a scam and ask for your money back. Sometimes they can freeze money that hasn't been spent yet. The FTC's gift card scam page lists contact information for major gift card companies.
2. **Keep the cards and the store receipt**, and take a photo of both. You'll need them when you report it.
3. **Report the scam** at **ReportFraud.ftc.gov**.
4. **Don't reply** to the email, and don't buy more cards, even if you're asked again.
5. **Tell your church office**, so they can warn other members, and let your pastor know his email may have been hacked.

Do you have the cards and the receipt with you? If so, we can look at step 1 together.

---

## tr042-a
- task: Set up Family Sharing | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac <https://support.apple.com/en-us/108380>

**USER:**
How do I set up Family Sharing on my iPhone so my daughter can be part of it?

**ASSISTANT:**
Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen to set up your family group and invite members.

**To invite your daughter later, or if you skipped that:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.

---

## tr042-b
- task: Set up Family Sharing | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac <https://support.apple.com/en-us/108380>

**USER:**
how do I share things with my family on my phone

**ASSISTANT:**
There are a few ways to do that. Is your phone an **iPhone** or an **Android** phone?

---

## tr042-d
- task: Set up Family Sharing | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac <https://support.apple.com/en-us/108380>

**USER:**
how do I share things with my family on my phone

**ASSISTANT:**
There are a few ways to do that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. My daughter said to set up Family Sharing so we can share stuff.

**ASSISTANT:**
Got it. Family Sharing is a good choice for that.

Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen to set up your family group and invite members.

**To invite your daughter later, or if you skipped that:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.

---

## tr042-e
- task: Set up Family Sharing | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac <https://support.apple.com/en-us/108380>

**USER:**
I have an iPhone and my 12 year old grandson doesn't have his own Apple Account yet. I'd like him in my Family Sharing, but I don't want to give him my login.

**ASSISTANT:**
Family Sharing is made for that. You can share things like iCloud+, Apple Music, and Apple TV without sharing an Apple Account. For a child without an account, you create a Child Account.

**Set up the group (if you haven't yet):**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen.

**Add your grandson:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Create Child Account** and follow the instructions on the screen.
7. Finish the prompts for parental controls, location sharing, and similar settings.

---

## tr042-r
- task: Set up Family Sharing | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac <https://support.apple.com/en-us/108380>

**USER:**
I'm on an iPhone and I want to invite my wife to my Family Sharing group. I already made the group.

**ASSISTANT:**
Here's how to invite her.

1. Open **Settings**, then tap **Family**.
2. Tap the **Add Member** button.
3. Tap **Invite Others**.
4. Finish the prompts that follow.

The invitation is sent to her by Messages or email.

**USER:**
She says the invitation never came.

**ASSISTANT:**
Let's check on it and send it again.

1. Open **Settings**, then tap **Family**.
2. Tap her name to see the invitation status.
3. Tap **Resend Invitation**.

She can accept from the email or text invitation. Or on her iPhone she can open **Settings**, tap her name, tap **Invitations**, and follow the instructions on the screen.

---

## tr043-a
- task: Add a contact | platform: Android | scenario: direct | sensitive: False
- sources: Contacts Help: Add or move contacts (Android) <https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
How do I add a new contact on my Android phone? I want to save my new doctor's office number.

**ASSISTANT:**
Here's how to save the number. It takes about a minute.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type a name, like **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now you can find the number in Contacts.

If your phone uses a different contacts app and you don't see **Add**, tell me what you see.

---

## tr043-b
- task: Add a contact | platform: Android | scenario: missing_info | sensitive: False
- sources: Contacts Help: Add or move contacts (Android) <https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how do I save a phone number

**ASSISTANT:**
Happy to help you save it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

---

## tr043-d
- task: Add a contact | platform: Android | scenario: followup | sensitive: False
- sources: Contacts Help: Add or move contacts (Android) <https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
how do I save a phone number

**ASSISTANT:**
Happy to help you save it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
Android

**ASSISTANT:**
Thanks.

Here's how to save the number. It takes about a minute.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type a name, like **Mom** or **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now you can find the number in Contacts.

If your phone uses a different contacts app and you don't see **Add**, tell me what you see.

---

## tr043-e
- task: Add a contact | platform: Android | scenario: constraint | sensitive: False
- sources: Contacts Help: Add or move contacts (Android) <https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid>

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

---

## tr043-r
- task: Add a contact | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Contacts Help: Add or move contacts (Android) <https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid>

**USER:**
I'm using an Android phone. How do I put my friend Linda's number into my Contacts?

**ASSISTANT:**
Here's how.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type Linda's name.
4. Type her phone number.
5. Tap **Save**.

**USER:**
I saved her, but when I signed in on my new Android phone, Linda isn't there.

**ASSISTANT:**
Contacts saved to a Google Account sync to your Android devices, so Linda may be saved somewhere else. You can move her to your Google Account:

1. Open the **Contacts** app and tap **Linda**.
2. At the top right, tap **Contact settings**.
3. Tap **Move to another account**.
4. Choose your Google Account.

Moving a contact deletes it from its original account.

---

## tr045-a
- task: Block a phone number | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad <https://support.apple.com/en-us/111104>

**USER:**
Someone keeps calling me from the same number and hanging up. How do I block it on my iPhone?

**ASSISTANT:**
You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the number you want to block. (In Classic view, tap the **Info** button instead.)
4. Scroll down and tap **Block Caller**.

The caller won't be told they're blocked. If they leave a voicemail, you won't get a notification.

---

## tr045-b
- task: Block a phone number | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad <https://support.apple.com/en-us/111104>

**USER:**
how do I stop a number from calling me

**ASSISTANT:**
You can block it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

---

## tr045-c
- task: Block a phone number | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad <https://support.apple.com/en-us/111104>

**USER:**
There's a number from out of state that calls me three or four times a day. When I answer nobody's there. My neighbor said I should block it but I don't know how. I have an iPhone 11.

**ASSISTANT:**
Your neighbor is right: blocking it will stop those calls from ringing. You can do it from your list of recent calls in less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. If a message asks you to confirm, tap **Block Contact**.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.

---

## tr045-d
- task: Block a phone number | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad <https://support.apple.com/en-us/111104>

**USER:**
how do I stop a number from calling me

**ASSISTANT:**
You can block it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
iPhone

**ASSISTANT:**
Thanks. You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the number you want to block. (In Classic view, tap the **Info** button instead.)
4. Scroll down and tap **Block Caller**.

The caller won't be told they're blocked. If they leave a voicemail, you won't get a notification.

---

## tr045-e
- task: Block a phone number | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad <https://support.apple.com/en-us/111104>

**USER:**
A man keeps texting me from a number I don't know on my iPhone, mostly rude stuff. He never calls, so there's nothing in my recent calls. I don't want him to know I blocked him.

**ASSISTANT:**
You can block him right from the text conversation, and he won't be told.

1. Open the **Messages** app and open the conversation with him.
2. Tap his number or name at the top.
3. Scroll down and tap **Block Caller**.

After that, messages he sends won't be delivered to you, and he isn't notified that he was blocked.

---

## tr045-r
- task: Block a phone number | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad <https://support.apple.com/en-us/111104>

**USER:**
A telemarketer calls my iPhone every afternoon. Please show me how to block the number.

**ASSISTANT:**
You can block it from your recent calls.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the phone number. If you see the **Info** button, tap that instead.
4. Scroll down and tap **Block Caller**.

After that, the caller isn't told they were blocked.

**USER:**
Oh no, I think I blocked my daughter's number by mistake. How do I undo it?

**ASSISTANT:**
No problem, you can unblock her. These steps are for the newest iPhone software, iOS 26.

1. Open **Settings** and tap **Privacy & Security**.
2. Tap **Blocked Contacts**.
3. Tap **Edit**.
4. Tap the delete button next to her number.
5. Tap **Unblock**.

---

## tr046-a
- task: Block a phone number | platform: Android | scenario: direct | sensitive: False
- sources: Phone app Help: Block or unblock a phone number <https://support.google.com/phoneapp/answer/6325463?hl=en>

**USER:**
How do I block a phone number on my Android phone? It's a spam caller.

**ASSISTANT:**
You can block it from your call history in the **Phone** app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **More**, then choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.

---

## tr046-b
- task: Block a phone number | platform: Android | scenario: missing_info | sensitive: False
- sources: Phone app Help: Block or unblock a phone number <https://support.google.com/phoneapp/answer/6325463?hl=en>

**USER:**
a spam number keeps calling

**ASSISTANT:**
That's annoying. I can show you how to block it. Is your phone an **iPhone** or an **Android** phone?

---

## tr046-c
- task: Block a phone number | platform: Android | scenario: missing_info | sensitive: False
- sources: Phone app Help: Block or unblock a phone number <https://support.google.com/phoneapp/answer/6325463?hl=en>

**USER:**
block this number

**ASSISTANT:**
Sure, I can help you block it. Is your phone an **iPhone** or an **Android** phone?

---

## tr046-d
- task: Block a phone number | platform: Android | scenario: followup | sensitive: False
- sources: Phone app Help: Block or unblock a phone number <https://support.google.com/phoneapp/answer/6325463?hl=en>

**USER:**
a spam number keeps calling

**ASSISTANT:**
That's annoying. I can show you how to block it. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, Pixel 6

**ASSISTANT:**
Thanks, here's how in Google's Phone app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **More**, then choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.

---

## tr046-e
- task: Block a phone number | platform: Android | scenario: constraint | sensitive: False
- sources: Phone app Help: Block or unblock a phone number <https://support.google.com/phoneapp/answer/6325463?hl=en>

**USER:**
Calls keep coming in on my Android phone that show up as Unknown with no number at all, so I can't pick one from my call history to block. Is there another way?

**ASSISTANT:**
Yes. You can block all unknown (private or unidentified) numbers.

1. Open the **Phone** app.
2. Tap **More**.
3. Tap **Settings**, then **Blocked numbers**.
4. Turn on **Unknown**.

Your phone will then decline calls from those numbers automatically. That covers every unknown caller, not only the one bothering you.

---

## tr046-r
- task: Block a phone number | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Phone app Help: Block or unblock a phone number <https://support.google.com/phoneapp/answer/6325463?hl=en>

**USER:**
A telemarketer keeps ringing my Pixel phone. Show me how to block that number from my call history.

**ASSISTANT:**
You can block it from your call history.

1. Open the **Phone** app.
2. Tap **More**, then **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.

After that, your phone declines that number's calls automatically.

**USER:**
I think I blocked the wrong number. How do I undo it?

**ASSISTANT:**
You can unblock it.

1. Open the **Phone** app and tap **More**.
2. Tap **Settings**, then **Blocked numbers**.
3. Next to the number, tap **Clear**.
4. Tap **Unblock**.

---

## tr048-b
- task: Silence calls from unknown numbers | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Manage unknown callers on iPhone <https://support.apple.com/en-us/111106>

**USER:**
How do I stop spam calls?

**ASSISTANT:**
There are a few ways to cut down on them. Is your phone an **iPhone** or an **Android** phone?

---

## tr048-c
- task: Silence calls from unknown numbers | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Manage unknown callers on iPhone <https://support.apple.com/en-us/111106>

**USER:**
Every day I get calls about my car warranty and I don't even have a car anymore. It's driving me crazy.

**ASSISTANT:**
Those calls are so annoying. There are phone settings that can quiet calls from numbers you don't know.

**Is your phone an iPhone or an Android phone?**

---

## tr048-e
- task: Silence calls from unknown numbers | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Manage unknown callers on iPhone <https://support.apple.com/en-us/111106>

**USER:**
I have an iPhone and I'm waiting to hear from a new specialist's office, so I can't just send every unknown number to voicemail. But I am sick of the spam. Is there something in between?

**ASSISTANT:**
Yes. On iPhone you can have unknown callers asked why they're calling before your phone rings.

1. Open the **Settings** app.
2. Tap **Apps**, then tap **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Ask Reason for Calling**.

The caller is asked why they're calling before your phone rings, so you can tell a real call from spam.

Calls from numbers saved in your Contacts always come through, so save the specialist's number once you have it. Call screening may use your standard calling and data rates.

---

## tr048-r
- task: Silence calls from unknown numbers | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Manage unknown callers on iPhone <https://support.apple.com/en-us/111106>

**USER:**
Robocalls keep ringing my iPhone all day. How do I make it stop ringing for numbers I haven't saved?

**ASSISTANT:**
You can silence calls from numbers you haven't saved. They go to voicemail.

1. Open the **Settings** app.
2. Tap **Apps**, then tap **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from your Contacts will still ring.

**USER:**
I did that. Now my Recents list is a big mess and I can't tell which calls came from unknown numbers. Can I see just those?

**ASSISTANT:**
Yes. Turn on a filter, then open the list.

1. Open **Settings**, tap **Apps**, then tap **Phone**.
2. Scroll to **Call Filtering** and turn on **Unknown Callers**.
3. In the Phone app, tap the **Filter** button, then tap **Unknown Callers**.

Missed calls and voicemails from unknown numbers now move to that list. In the Phone app it appears in the **Recents** tab in Classic view, or the **Calls** tab in Unified view.

---

## tr049-b
- task: Filter spam calls | platform: Android (Pixel) | scenario: missing_info | sensitive: False
- sources: Phone app Help: Use caller ID & spam protection <https://support.google.com/phoneapp/answer/3459196?hl=en>

**USER:**
too many robocalls, can my phone block them?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr049-c
- task: Filter spam calls | platform: Android (Pixel) | scenario: direct_messy | sensitive: False
- sources: Phone app Help: Use caller ID & spam protection <https://support.google.com/phoneapp/answer/3459196?hl=en>

**USER:**
Pixel 8, using the default Google Phone app. Caller ID shows 'Suspected spam' but they still ring. How do I make those not ring at all?

**ASSISTANT:**
Since your phone already labels them, you just need to turn on **Filter spam calls**. It takes about a minute.

1. Open the **Phone** app.
2. Tap **More options**.
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls are handled by the filter. You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

---

## tr049-d
- task: Filter spam calls | platform: Android (Pixel) | scenario: followup | sensitive: False
- sources: Phone app Help: Use caller ID & spam protection <https://support.google.com/phoneapp/answer/3459196?hl=en>

**USER:**
too many robocalls, can my phone block them?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, a Google Pixel 7a

**ASSISTANT:**
Thanks. The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap **More options**.
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

You won't get missed call or voicemail notifications for filtered calls, but they still show in your call history, and you can still check your voicemail.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.

---

## tr049-e
- task: Filter spam calls | platform: Android (Pixel) | scenario: constraint | sensitive: False
- sources: Phone app Help: Use caller ID & spam protection <https://support.google.com/phoneapp/answer/3459196?hl=en>

**USER:**
Pixel phone with the Google Phone app here. I don't want anything blocked or hidden, because my pharmacy calls from lots of different numbers. I just want the phone to warn me when a call looks like spam. What should I do?

**ASSISTANT:**
You can have the Phone app warn you without blocking anything.

1. Open the **Phone** app.
2. Tap **More options** (three dots), then tap **Settings**.
3. Tap **Caller ID and spam**.
4. Make sure **See caller ID & spam** is on.
5. Leave **Filter spam calls** turned off.

Calls that look like spam may show **Suspected spam caller** or **Spam** as the caller ID, and your phone will still ring.

This setting is on by default, so it may already be on.

---

## tr049-r
- task: Filter spam calls | platform: Android (Pixel) | scenario: failure_recovery | sensitive: False
- sources: Phone app Help: Use caller ID & spam protection <https://support.google.com/phoneapp/answer/3459196?hl=en>

**USER:**
My Pixel keeps ringing with robocalls. How do I make the Phone app block the spam ones?

**ASSISTANT:**
You can turn on spam filtering in the Phone app.

1. Open the **Phone** app.
2. Tap **More options** (three dots), then tap **Settings**.
3. Tap **Caller ID and spam**.
4. Make sure **See caller ID & spam** is on.
5. Turn on **Filter spam calls**.

Filtered calls won't notify you, but they still show in your call history.

**USER:**
I did that. But now a call from my dentist's office got marked as spam and I think it was blocked. Help!

**ASSISTANT:**
You can fix that in a few taps.

1. Open the **Phone** app and tap **Recent calls**.
2. Tap the call that is labeled as spam.
3. Tap **Not spam**.
4. Tap **Unblock**.

Calls that were filtered still appear in your call history, and you can still check your voicemail.

---

## tr050-b
- task: Check battery health | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: iPhone battery and performance <https://support.apple.com/en-us/101575>

**USER:**
my battery dies so fast

**ASSISTANT:**
That's annoying. Is your phone an **iPhone** or an **Android** phone?

---

## tr050-c
- task: Check battery health | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: iPhone battery and performance <https://support.apple.com/en-us/101575>

**USER:**
battery health

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr050-d
- task: Check battery health | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: iPhone battery and performance <https://support.apple.com/en-us/101575>

**USER:**
my battery dies so fast

**ASSISTANT:**
That's annoying. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone, about 4 years old

**ASSISTANT:**
Thanks. At four years old, the battery may be worn. Let's check:

You can check it in Settings. It takes a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**. On some versions the name is slightly different.
4. Look at **Maximum Capacity**. This compares your battery now to when it was new. A lower number means it won't last as long between charges.

If you see a message that your battery's health is **significantly degraded**, it isn't a safety problem, but a new battery would help it last longer. Apple offers battery service, and it may be covered if your phone is still under warranty.

---
