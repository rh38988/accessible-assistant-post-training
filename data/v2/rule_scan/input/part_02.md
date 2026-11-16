# Rule scan input, part 02 (50 examples)

## tr011-a
- task: Install a software update | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Update your iPhone or iPad <https://support.apple.com/en-ie/118575>

**USER:**
My iPhone says iOS has something new to install. What do I press to get it on there?

**ASSISTANT:**
Here is how to update your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug your iPhone into a power source.
3. Connect your iPhone to Wi-Fi.
4. Open **Settings**.
5. Tap **General**.
6. Tap **Software Update**. It shows whether an update is available.
7. Tap **Download and Install**.
8. Follow the instructions on the screen.

If you see a message about space, tap **Continue** to let your iPhone temporarily remove some apps. They are put back by themselves afterward.

---

## tr011-d
- task: Install a software update | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Update your iPhone or iPad <https://support.apple.com/en-ie/118575>

**USER:**
my phone says there is a new update. how do i put it on

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iphone

**ASSISTANT:**
Here is how to put the update on your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug your iPhone into a power source and connect it to Wi-Fi.
3. Open **Settings**.
4. Tap **General**.
5. Tap **Software Update**.
6. Tap **Download and Install**.
7. Follow the instructions on the screen.

If you do not see the update on your phone, you can update using a computer instead.

---

## tr011-e
- task: Install a software update | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Update your iPhone or iPad <https://support.apple.com/en-ie/118575>

**USER:**
I always forget to update my iPhone and I don't want to sit and watch it while it updates. I'd like it to just happen at night while I'm asleep and the phone is on the charger. Can it?

**ASSISTANT:**
Yes, you can turn on automatic updates.

1. Open **Settings**.
2. Tap **General**.
3. Tap **Software Update**.
4. Tap **Automatic Updates**.
5. Turn on **Automatically Install**.

Your iPhone will then download and install updates overnight while it is charging and on Wi-Fi. It will notify you before it installs.

---

## tr011-r
- task: Install a software update | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Update your iPhone or iPad <https://support.apple.com/en-ie/118575>

**USER:**
Show me how to install the newest update on my iPhone please.

**ASSISTANT:**
Here is how to update your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug it into a power source and connect to Wi-Fi.
3. Open **Settings**, tap **General**, then tap **Software Update**.
4. Tap **Download and Install**.
5. Follow the instructions on the screen.

**USER:**
It says there isn't enough space. Now what?

**ASSISTANT:**
You have two choices.

1. Tap **Continue** to let your iPhone temporarily remove some apps. They are put back by themselves after the update.
2. Or tap **Cancel** and delete some things yourself to free up space.

---

## pilot-012
- task: Attach a photo to an email | platform: Gmail (computer) | scenario: direct_messy | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message <https://support.google.com/mail/answer/6584>

**USER:**
I have a Dell computer with Windows 11 and I use Google Chrome to read my Gmail. I have a photo saved in my Pictures folder called birthday.jpg that I want to email to my son. I already know how to write the email, I just don't know how to add the photo.

**ASSISTANT:**
Since you already know how to write the email, here's just the part for adding the photo:

1. At the bottom of the message window, click the **Attach** icon.
2. Select the photo **birthday.jpg**. It is in your Pictures folder.
3. Click **Open**.

You'll see the file appear in your email. In a personal Gmail account, if the attachments are bigger than 25 MB in total, Gmail adds a Google Drive link to the email instead of the file.

---

## tr012-a
- task: Attach a photo to an email | platform: Gmail (computer) | scenario: direct | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message <https://support.google.com/mail/answer/6584>

**USER:**
How do I put a picture in an email in Gmail on my computer?

**ASSISTANT:**
Here is how to add a picture to your email in Gmail on a computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the picture you want to send.
5. Click **Open**.

If the picture is too big for a personal Gmail account (over 25 MB), Gmail removes it and puts it in the email as a Google Drive link instead.

---

## tr012-d
- task: Attach a photo to an email | platform: Gmail (computer) | scenario: followup | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message <https://support.google.com/mail/answer/6584>

**USER:**
want to email my grandson a snapshot, where do I start

**ASSISTANT:**
I can help with that. Are you using **Gmail** on a computer, or a different email program?

**USER:**
gmail on my computer

**ASSISTANT:**
Here is how to send a picture in Gmail on your computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the picture you want to send.
5. Click **Open**.

If the picture is very large, Gmail may add it to the email as a Google Drive link instead of attaching it.

---

## tr012-r
- task: Attach a photo to an email | platform: Gmail (computer) | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Send attachments with your Gmail message <https://support.google.com/mail/answer/6584>

**USER:**
Show me how to attach a photo in Gmail on my computer please.

**ASSISTANT:**
Here is how to attach a photo in Gmail on your computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the photo you want.
5. Click **Open**.

**USER:**
I picked the wrong photo and it's in the email now. How do I take it out?

**ASSISTANT:**
You can remove it easily.

1. Find the photo's name in your email.
2. Click **Close** to the right of the photo's name.

Then use **Attach** again to add the right photo.

---

## tr013-a
- task: Back up photos | platform: iPhone (iCloud Photos) | scenario: direct | sensitive: False
- sources: Apple iCloud User Guide: Set up and use iCloud Photos <https://support.apple.com/guide/icloud/mm7e90c1ba48>

**USER:**
I have an iPhone. How do I turn on iCloud Photos so my pictures are saved online?

**ASSISTANT:**
Here is how to turn on iCloud Photos on your iPhone.

1. Open **Settings**.
2. Tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **Photos**.
5. Turn on **Sync this iPhone**.

Your photos and videos are then added to iCloud. To see them, open the **Photos** app and tap **Library**.

---

## tr013-b
- task: Back up photos | platform: iPhone (iCloud Photos) | scenario: missing_info | sensitive: False
- sources: Apple iCloud User Guide: Set up and use iCloud Photos <https://support.apple.com/guide/icloud/mm7e90c1ba48>

**USER:**
my phone has thousands of pictures of the kids on it and I'm scared I'll lose them. can you help me save them somewhere

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr013-c
- task: Back up photos | platform: iPhone (iCloud Photos) | scenario: direct_messy | sensitive: False
- sources: Apple iCloud User Guide: Set up and use iCloud Photos <https://support.apple.com/guide/icloud/mm7e90c1ba48>

**USER:**
My husband handles the computer stuff but he's traveling. We have a Mac and all of our family pictures are in the Photos app on it. I want them kept safe in iCloud in case the computer breaks. I'm signed in with my Apple Account already. What do I click?

**ASSISTANT:**
Here is how to keep your Mac's photos in iCloud.

1. Open the **Photos** app.
2. In the menu at the top of the screen, click **Photos**, then click **Settings**.
3. Click **iCloud**.
4. Select **iCloud Photos**.

The photos and videos in Photos are then added to iCloud. To check on progress, scroll to the bottom of the Photos screen.

---

## tr013-e
- task: Back up photos | platform: iPhone (iCloud Photos) | scenario: constraint | sensitive: False
- sources: Apple iCloud User Guide: Set up and use iCloud Photos <https://support.apple.com/guide/icloud/mm7e90c1ba48>

**USER:**
I want my iPhone pictures saved to iCloud, and I also want to look at them on my old laptop. But I don't want to install anything on the laptop, it's slow already. Is there a way?

**ASSISTANT:**
Yes. You can see them in a web browser, with nothing to install.

1. On your iPhone, open **Settings** and tap **your name**.
2. Tap **iCloud**, then tap **Photos**.
3. Turn on **Sync this iPhone**.
4. On your laptop, open a web browser and go to **icloud.com/photos**.
5. Sign in with your Apple Account.

Use the same Apple Account on both.

---

## tr013-r
- task: Back up photos | platform: iPhone (iCloud Photos) | scenario: failure_recovery | sensitive: False
- sources: Apple iCloud User Guide: Set up and use iCloud Photos <https://support.apple.com/guide/icloud/mm7e90c1ba48>

**USER:**
Please show me how to save my iPhone photos to iCloud.

**ASSISTANT:**
Here is how to save your iPhone photos to iCloud.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **Photos**.
4. Turn on **Sync this iPhone**.

**USER:**
I turned it on but I can't tell if anything is happening. How do I check?

**ASSISTANT:**
You can check the progress in the Photos app.

1. Open the **Photos** app.
2. Tap **Collections**.
3. Tap your **profile picture** in the top right corner.
4. Look below your name for the status.

If it still doesn't seem right, make sure you are signed in to the same Apple Account and that iCloud Photos is turned on.

---

## pilot-014
- task: Caller claims to be grandchild needing gift cards | platform: any | scenario: direct | sensitive: True
- sources: FTC: Talking Turkey (family emergency scams) <https://www.ftc.gov/node/54353>; FTC Consumer Alert: A way to spot scams: how someone asks you to pay <https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay>

**USER:**
My grandson just called crying. He said he got arrested and needs me to buy $2,000 in gift cards and read him the numbers. He said not to tell his mom. What should I do?

**ASSISTANT:**
I'm sorry, that must have been frightening. Please **don't buy the gift cards yet**. This has several signs of a common scam where someone pretends to be a grandchild in trouble:

- They need money **right away**
- They want **gift cards**, a way of paying that scammers like because it is hard to get your money back
- They ask you to **keep it a secret**

Here's what to do:

1. Don't buy anything right away. Resist the urge to act immediately, no matter how dramatic the story may be.
2. Call your grandson using the phone number **you already have for him**, not a number the caller gave you.
3. Call his mom or another family member too, even though the caller said not to.

If it really was him, your family can help sort it out. If it was a scammer, you can report it at **www.ftc.gov/complaint**.

If you already bought cards or read any numbers to them, tell me right away and I'll help you with the next steps.

---

## tr014-c
- task: Caller claims to be grandchild needing gift cards | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC: Talking Turkey (family emergency scams) <https://www.ftc.gov/node/54353>

**USER:**
I got a Facebook message from someone who says she is my granddaughter Emily. She wrote that she is stuck in another country, lost her bag, and needs me to wire her money today or she can't get home. The picture looks like her but the writing sounds a bit odd. I want to help her but I'm not sure. What should I do?

**ASSISTANT:**
I'm glad you stopped to ask. **Please don't wire any money yet.** Scammers often pretend to be a grandchild in trouble, and they push for payment right away.

1. Take a breath. You don't have to act right now, even if the story sounds dramatic.
2. Call Emily on a phone number **you know is really hers**. Don't use any number from the message.
3. Check the story with another trusted family member too.
4. Don't wire money, pay with a gift card, or send cash for an emergency request.

You can report the message at **www.ftc.gov/complaint**.

---

## tr014-e
- task: Caller claims to be grandchild needing gift cards | platform: any | scenario: constraint | sensitive: True
- sources: FTC: Talking Turkey (family emergency scams) <https://www.ftc.gov/node/54353>

**USER:**
A man called saying he is my grandson Kevin and he was in a car accident. He said a lawyer will call me for the bail money, and he begged me not to tell his parents because they'd be so angry. His mother is traveling and I can't reach her right now. He says there's no time. Should I do what he asks?

**ASSISTANT:**
**Please don't send any money yet.** A caller who begs for secrecy and says there is no time is a common sign of a family emergency scam. A fake lawyer is another sign.

1. Hang up and take your time. There is no need to rush.
2. Call Kevin on a number **you know is genuine**.
3. If you can't reach his mother, check the story with **another trusted family member**, even though the caller asked you to keep it secret.
4. Don't wire money, pay with a gift card, or send cash.

---

## tr014-f
- task: Caller claims to be grandchild needing gift cards | platform: any | scenario: helper | sensitive: True
- sources: FTC: Talking Turkey (family emergency scams) <https://www.ftc.gov/node/54353>

**USER:**
My mother is 84 and just told me someone called saying he was her grandson and needed money fast for bail. She hasn't sent anything but she is shaken. How can I help her?

**ASSISTANT:**
It's good she told you before sending anything. Here is how to help her.

1. Reassure her. These calls are built to make people panic, and the caller pushes for money right away.
2. Help her call her grandson on a number you know is genuine.
3. Check the story with another trusted family member, even if the caller asked for secrecy.
4. Remind her not to wire money, pay with a gift card, or send cash for an emergency request.
5. Report the call at **www.ftc.gov/complaint**.

It also helps to agree as a family that no one will ever call with an emergency request for wired money, gift card payment, or cash.

---

## tr014-g
- task: Caller claims to be grandchild needing gift cards | platform: any | scenario: prevention | sensitive: True
- sources: FTC: Talking Turkey (family emergency scams) <https://www.ftc.gov/node/54353>

**USER:**
My friend was just fooled by a call from a fake grandchild. How can I tell if a call like that is a scam in the future?

**ASSISTANT:**
Here are the signs of this kind of scam:

1. The caller says they are a family member in an emergency, such as needing bail or medical care.
2. They say things like "I know I don't sound like myself" or "Don't tell Mom. Let's keep this our secret."
3. A doctor, lawyer, or police officer may be part of the story.
4. They want money **right away**, by wire, gift card, or cash.

What to do if it happens:
1. Don't act right away, however dramatic the story is.
2. Call your relative on a number you know is genuine.
3. Check with another trusted family member.

Agree with your family that no one will ever call with an emergency request for wired money, gift cards, or cash. You can report scams at **www.ftc.gov/complaint**.

---

## pilot-015
- task: Stranger asks for a verification code | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: Verification code scams <https://consumer.ftc.gov/node/84809>

**USER:**
Someone texted me saying they sent me a code by mistake and asked me to send it back. It's a 6-digit number from my bank. Should I just send it to them?

**ASSISTANT:**
**No, please don't send it.** That code is only meant for you to log in to your account. Anyone who asks you for it is trying to get into your account, even if their message sounds friendly.

Here's what to do:

1. Don't reply to the text.
2. Block their number and stop texting them.
3. If you're worried about your account, call your bank using a phone number from your bank statement or your bank's app. Don't use any number from the text.
4. You can report the text at **ReportFraud.ftc.gov**.

If you already sent the code, contact your bank using a phone number from your bank statement or your bank's app.

---

## tr015-c
- task: Stranger asks for a verification code | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Verification code scams <https://consumer.ftc.gov/node/84809>

**USER:**
A woman phoned me saying she works in the fraud department at my bank and that someone is trying to take money out of my account. She was very polite and said she would text me a code to stop it, and I just need to read the code back to her. I'm worried about my savings. Is this real?

**ASSISTANT:**
**Please don't read her the code.** This is a known scam. Scammers pretend to be someone you trust and claim there is a problem with your account. With the code, they can log in and move your money.

1. Hang up. Don't argue with her.
2. Block the number.
3. If you're worried about your account, contact your bank directly. Use a number you trust, like the one on your statement or in your app. Don't use any number the caller gave you.
4. Report the call at **ReportFraud.ftc.gov**.

Remember that anyone who asks for your verification code is a scammer.

---

## tr015-e
- task: Stranger asks for a verification code | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Verification code scams <https://consumer.ftc.gov/node/84809>

**USER:**
A man keeps calling and texting me. He already knows my full name and the town I live in, and he sounds very kind. He says someone stole my identity and he'll help me fix it, but first I must tell him the code that was just texted to my phone. He knows so much about me that it must be real, right?

**ASSISTANT:**
**Please don't tell him the code.** Scammers often know details about you and sound sympathetic. That is part of how they earn your trust. Anyone who asks you for your verification code is a scammer.

1. Don't engage. Hang up and stop texting him.
2. Block his number.
3. If you're worried about your accounts, contact your bank, credit union, or investment advisor directly. Use a number you trust, such as the one on your statement or in your app.
4. Report him at **ReportFraud.ftc.gov**.

Never call back a number he gave you.

---

## tr015-f
- task: Stranger asks for a verification code | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: Verification code scams <https://consumer.ftc.gov/node/84809>

**USER:**
My dad is 79 and keeps getting texts and calls from people who say there is a problem with his accounts and ask for a code that gets sent to his phone. What should I tell him to do?

**ASSISTANT:**
It's good you're looking out for him. Here is what to tell him.

1. **Never give a verification code to anyone.** Anyone who asks for it is a scammer.
2. If someone asks, don't engage. Hang up, block the number, and stop texting.
3. If he is worried about an account, he should contact his bank, credit union, or investment advisor directly, using a number he trusts, like the one on his statement or in his app.
4. He should never use a number the caller gave him.
5. You can report the contacts at **ReportFraud.ftc.gov**.

If he already shared a code, he should contact his bank or credit union right away using a trusted number.

---

## tr015-g
- task: Stranger asks for a verification code | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: Verification code scams <https://consumer.ftc.gov/node/84809>

**USER:**
How do these verification code scams work, and how can I stay safe from them?

**ASSISTANT:**
Here is how they work. Scammers pretend to be someone you trust and say there is a problem with an account or that your identity was stolen. They may know details about you and sound sympathetic. Then they ask for your verification code. With it, they can log in to your account and move money out of savings or investment accounts.

How to stay safe:

1. **Never give your verification code to anyone.**
2. Remember that anyone who asks for it is a scammer.
3. If someone asks, hang up, block the number, and stop texting.
4. If you're worried, contact your bank directly using a number on your statement or in your app.
5. Report it at **ReportFraud.ftc.gov**.

---

## tr015-r
- task: Stranger asks for a verification code | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Verification code scams <https://consumer.ftc.gov/node/84809>

**USER:**
I already read a code to a man who said he was from my credit union. Right after, I got a bad feeling. What should I do?

**ASSISTANT:**
I'm sorry, and thank you for acting quickly. With a code, a scammer may be able to log in to your account, so contact your credit union right away.

1. Call your credit union directly. Use a number you trust, like the one on your statement or in your app.
2. Don't call back any number the man gave you. It would take you to the scammer.
3. Don't talk to him or text him again, and block his number.
4. Report it at **ReportFraud.ftc.gov**.

I don't have more specific steps than these, so your credit union is the best place to ask what else to do.

---

## tr016-c
- task: Is it safe to pay online? | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Alert: A way to spot scams: how someone asks you to pay <https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay>

**USER:**
I found a beautiful rocking chair on a website I've never heard of, and the price is half what stores charge. They only accept cryptocurrency and say it's because of fees. My nephew says no but I really want it. Is it safe to pay them that way?

**ASSISTANT:**
**Please don't pay with cryptocurrency.** When a seller says that is the only way to pay, it is probably a scam, whatever reason they give.

1. Don't send money to anyone who says you can only pay one specific way.
2. Search online for the website's name with words like "review," "scam," or "complaint."
3. If the seller accepts a **credit card**, that is safer. Credit cards have more protections and let you dispute charges.

Your nephew is right to be careful. If you want to report the website, you can do that at **ReportFraud.ftc.gov**.

---

## tr016-d
- task: Is it safe to pay online? | platform: any | scenario: followup | sensitive: True
- sources: FTC Consumer Alert: A way to spot scams: how someone asks you to pay <https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay>

**USER:**
is it safe to pay for something online?

**ASSISTANT:**
It can be, but it depends on what you're buying, who you're buying from, and how they want you to be paid.

**What are you trying to buy, and how is the seller asking you to pay** (for example a credit card, a gift card, or a bank transfer)?

One quick tip while you check: if a seller says you can only pay with **gift cards, a wire transfer, or cryptocurrency**, stop. That's a common sign of a scam.

**USER:**
I'm buying a used lawn mower from a man on a website and he says I have to pay with a gift card.

**ASSISTANT:**
**Please don't pay with a gift card.** When someone says gift card is the only way to pay, that is a sign of a scam. The same goes for a bank transfer, wire transfer, cryptocurrency, or a payment app.

1. Don't send money to anyone who says you can only pay one specific way, whatever reason they give.
2. Search online for the seller's name with words like "review," "scam," or "complaint" and see what others say.
3. If you decide to buy, pay by **credit card** whenever possible. It has more protections and lets you dispute charges.

You can report a seller like this at **ReportFraud.ftc.gov**.

---

## tr016-g
- task: Is it safe to pay online? | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Alert: A way to spot scams: how someone asks you to pay <https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay>

**USER:**
What are the warning signs that someone is trying to scam me when I buy things online?

**ASSISTANT:**
The biggest warning sign is how they ask you to pay.

1. If someone says the **only** way to pay is a bank transfer, wire transfer, cryptocurrency, payment app, or gift card, it is probably a scam.
2. Never send money to anyone who says you can only pay one specific way, whatever reason they give.
3. Check the seller. Search online for the name with words like "review," "scam," or "complaint."
4. Pay by **credit card** whenever possible. It has more protections and lets you dispute charges.

If you already paid a scammer, contact the company you used to send the money right away, tell them it was fraud, and ask if they can stop or reverse it. You can report scams at **ReportFraud.ftc.gov**.

---

## tr016-r
- task: Is it safe to pay online? | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Alert: A way to spot scams: how someone asks you to pay <https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay>

**USER:**
I already paid. A seller told me to wire money for a puppy and now they've stopped answering. What can I do?

**ASSISTANT:**
I'm sorry. Act quickly, because the sooner you do, the better.

1. Contact the company you used to send the wire right away.
2. Tell them it was fraud.
3. Ask whether they can stop or reverse the transaction and return your money.
4. Report the seller at **ReportFraud.ftc.gov**.

I don't have steps that are specific to wire transfers beyond these.

---

## tr021-c
- task: Make text bigger | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Change the font size on your iPhone, iPad, and iPod touch <https://support.apple.com/en-us/102453>

**USER:**
the words on my iphone are too

**ASSISTANT:**
It looks like your message got cut off. Do you mean the words are too **small** to read? If so, I can show you how to make them bigger.

---

## tr021-d
- task: Make text bigger | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Change the font size on your iPhone, iPad, and iPod touch <https://support.apple.com/en-us/102453>

**USER:**
how do I make the letters bigger on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?

**USER:**
It's an iPhone.

**ASSISTANT:**
Great, thanks.

You can make the text bigger in Settings. It takes about a minute, and you can change it back anytime.

1. Open the **Settings** app.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider to the right. Stop when the text is easy to read.

If you need it even bigger, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**, and drag that slider. Very large text can make some buttons harder to tap, so slide it back a little if that happens.

---

## tr021-e
- task: Make text bigger | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Change the font size on your iPhone, iPad, and iPod touch <https://support.apple.com/en-us/102453>

**USER:**
I already made the text bigger on my iPhone using the slider in Display & Brightness, but my eyes are bad and it still isn't big enough. That slider is at the end. Is there any way to get the words even larger?

**ASSISTANT:**
Yes, there is a separate setting for larger sizes.

1. Open the **Settings** app.
2. Tap **Accessibility**.
3. Tap **Display & Text Size**.
4. Tap **Larger Text**.
5. Drag the slider to the size you want.

The larger sizes work in apps like Mail, Contacts, Calendar, Phone, and Notes. Very large text can make some buttons hard to tap. If that happens, come back to the same screen and slide it down a little.

---

## tr021-r
- task: Make text bigger | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Change the font size on your iPhone, iPad, and iPod touch <https://support.apple.com/en-us/102453>

**USER:**
How do I make the text bigger on my iPhone? Everything is too small to read.

**ASSISTANT:**
You can make the text bigger in Settings. It takes about a minute, and you can change it back anytime.

1. Open the **Settings** app. Its icon is a gray gear.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider at the bottom of the screen to the right.

The sample text changes as you drag, so you can stop when it's easy to read.

If you need it even bigger, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**, and drag that slider. Very large text can make some buttons harder to tap, so slide it back a little if that happens.

**USER:**
I made it really big and now some of the buttons are cut off and hard to tap.

**ASSISTANT:**
That can happen when the text is set very large. Let's make it a little smaller so the buttons fit again.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider **one step to the left**.
5. Go back to the app and check the buttons.

If you made the text bigger with **Larger Text** instead, the slider is in **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**.

Repeat until the buttons fit on the screen and the text is still easy for you to read.

---

## tr022-a
- task: Make text bigger | platform: Android (Pixel) | scenario: direct | sensitive: False
- sources: Android Accessibility Help: Change text & display settings <https://support.google.com/accessibility/android/answer/11183305?hl=en>

**USER:**
I have a Google Pixel phone. How can I make the writing on the screen larger?

**ASSISTANT:**
You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** in Settings.
3. Tap **Font size**.
4. Move the slider toward the larger end until the text is easy to read.

A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.

---

## tr022-b
- task: Make text bigger | platform: Android (Pixel) | scenario: missing_info | sensitive: False
- sources: Android Accessibility Help: Change text & display settings <https://support.google.com/accessibility/android/answer/11183305?hl=en>

**USER:**
my phone screen writing is too small

**ASSISTANT:**
I can help you make it bigger. What kind of phone do you have, an **iPhone** or an Android phone like a Samsung or Google Pixel?

---

## tr022-c
- task: Make text bigger | platform: Android (Pixel) | scenario: direct_messy | sensitive: False
- sources: Android Accessibility Help: Change text & display settings <https://support.google.com/accessibility/android/answer/11183305?hl=en>

**USER:**
My daughter gave me her old Google Pixel when she got a new phone. It works fine but I can't read anything without my glasses and I always forget where I put them. Is there a way to make the letters on the screen bigger?

**ASSISTANT:**
Yes. You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Tap the search bar at the top of Settings.
3. Type **Font size**.
4. Tap **Font size** in the results.
5. Move the slider toward the larger end until the text is easy to read.

The change happens right away. A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.

---

## tr022-d
- task: Make text bigger | platform: Android (Pixel) | scenario: followup | sensitive: False
- sources: Android Accessibility Help: Change text & display settings <https://support.google.com/accessibility/android/answer/11183305?hl=en>

**USER:**
my phone screen writing is too small

**ASSISTANT:**
I can help you make it bigger. What kind of phone do you have, an **iPhone** or an Android phone like a Samsung or Google Pixel?

**USER:**
Google Pixel 8

**ASSISTANT:**
Thanks.

You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** in Settings.
3. Tap **Font size**.
4. Move the slider toward the larger end until the text is easy to read.

A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.

---

## tr022-e
- task: Make text bigger | platform: Android (Pixel) | scenario: constraint | sensitive: False
- sources: Android Accessibility Help: Change text & display settings <https://support.google.com/accessibility/android/answer/11183305?hl=en>

**USER:**
I have a Pixel phone and I like to change the text size depending on whether I'm wearing my glasses. I don't want to dig through Settings every single time. Is there a quicker way to switch the size?

**ASSISTANT:**
Yes. Once it is set up, the quick way is the top of the screen. Set it up first in Settings.

1. Open the **Settings** app.
2. Search for **Font size** and tap it.
3. Move the slider once. This adds a **Font Size** tile to Quick Settings.

From then on:

1. Swipe down from the top of the screen to open Quick Settings.
2. Tap **Font Size**.
3. Tap **Increase** or **Decrease**, or drag the percentage slider.

Font size can go up to 200%.

---

## tr022-r
- task: Make text bigger | platform: Android (Pixel) | scenario: failure_recovery | sensitive: False
- sources: Android Accessibility Help: Change text & display settings <https://support.google.com/accessibility/android/answer/11183305?hl=en>

**USER:**
My Pixel's text is too small to read. How do I make it bigger?

**ASSISTANT:**
You can make it bigger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** and tap it.
3. Move the slider toward the larger end.

You will see a preview of the new size. A few apps ignore this setting, so text in them may stay the same.

**USER:**
I slid it all the way and now it is way too big and I can't even read the screen. How do I go back?

**ASSISTANT:**
You can put it back to the way it was.

1. Open **Settings**.
2. Search for **Font size** and tap it.
3. Tap **Reset settings** to return to the phone's default size.

Or move the slider back toward the smaller end a little at a time until it is comfortable.

---

## tr024-a
- task: Turn up ringer volume | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
How do I make my iPhone ring louder when someone calls?

**ASSISTANT:**
Here is a quick way to do it. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

---

## tr024-b
- task: Turn up ringer volume | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>; Apple Support: How to set and change alarms on your iPhone <https://support.apple.com/en-us/118444>

**USER:**
My phone is too quiet when it rings.

**ASSISTANT:**
Let's fix that so you don't miss calls. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?

---

## tr024-c
- task: Turn up ringer volume | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
I keep missing calls from my son because I don't hear my iPhone ring when I'm in the kitchen cooking. He gets worried. Can I make the ringing louder?

**ASSISTANT:**
Yes, you can, and that should help your son reach you.

Here is a quick way to do it. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

---

## tr024-d
- task: Turn up ringer volume | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
My phone is too quiet when it rings.

**ASSISTANT:**
Let's fix that so you don't miss calls. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?

**USER:**
iPhone 13

**ASSISTANT:**
Thanks. Here's how on your iPhone. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

---

## tr024-e
- task: Turn up ringer volume | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
Every time I press the volume up button on my iPhone it only makes my YouTube videos louder, not the phone ringing. I'm usually watching videos when my daughter calls. I want the ringer louder, not the videos. How do I do that?

**ASSISTANT:**
That happens because the volume buttons change **media volume** while you are watching videos, listening to music, or playing games. They change the ringer volume only when you aren't using other apps.

1. Close the video app and go to your Home Screen, so no other app is in use.
2. Press the **volume up** button a few times.

Now the buttons raise the ringer volume. If your phone still only vibrates when someone calls, it may be in Silent mode. Tell me and I'll show you how to check.

---

## tr025-a
- task: Turn up ring volume | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
How do I turn up the ringer on my Android phone?

**ASSISTANT:**
You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Drag the **Ring Volume** slider to the right.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right and use the **Ring** slider.

If neither of these matches what you see, tell me and I'll help you find it.

---

## tr025-b
- task: Turn up ring volume | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
how do I make the ringing louder

**ASSISTANT:**
Happy to help. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

---

## tr025-c
- task: Turn up ring volume | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
ringer volume on my android

**ASSISTANT:**
Here's how to change the ringer volume on your Android phone.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Slide the **Ring Volume** slider to the right for louder, or to the left for quieter.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right, choose **Ring**, and slide it the same way.

---

## tr025-d
- task: Turn up ring volume | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
how do I make the ringing louder

**ASSISTANT:**
Happy to help. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
android, it's a samsung

**ASSISTANT:**
Thanks. Phone screens can look a little different, so here is what to look for.

You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Drag the **Ring Volume** slider to the right.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right and use the **Ring** slider.

If neither of these matches what you see, tell me and I'll help you find it.

---

## tr025-r
- task: Turn up ring volume | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Change volume, sound & vibrate settings <https://support.google.com/android/answer/9082609?hl=en>

**USER:**
Please show me how to make my Android phone ring louder.

**ASSISTANT:**
You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button** on the side of the phone.
2. Tap the **Menu** icon on the right side of the volume panel.
3. Find the **Ring Volume** slider and slide it to the right.

If you don't see the **Menu** icon, tell me what you see and I'll help you find it.

**USER:**
I pressed the button but there is no menu icon. I only see a small arrow pointing down.

**ASSISTANT:**
That's normal on older Android versions. Use the arrow instead.

1. Press a **volume button** again.
2. At the right, tap the **Down arrow**.
3. Choose **Ring**.
4. Slide the **Ring** level to where you want it.

---

## tr026-a
- task: Turn on Wi-Fi Calling | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Make a call with Wi-Fi Calling <https://support.apple.com/en-us/108066>

**USER:**
My iPhone has no signal in my basement apartment but I have Wi-Fi. Can I make calls using the Wi-Fi?

**ASSISTANT:**
iPhone has a feature called **Wi-Fi Calling** that lets you make calls over Wi-Fi when there is little or no cellular coverage. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.

---

## tr026-b
- task: Turn on Wi-Fi Calling | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Make a call with Wi-Fi Calling <https://support.apple.com/en-us/108066>

**USER:**
calls keep dropping in my house, what can I do

**ASSISTANT:**
That's frustrating. Is your phone an **iPhone** or an Android phone?

---
