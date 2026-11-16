# Rule scan input, part 19 (50 examples)

## tr214-f
- task: A caller demands payment for a debt the user does not recognize | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: Debt collection FAQs <https://www.consumer.ftc.gov/articles/debt-collection-faqs>

**USER:**
A debt collector called my mother's friend and also called her daughter and talked about the debt. The friend says she doesn't owe it. How can I help her?

**ASSISTANT:**
Help her avoid paying until the debt is proven, and know that a collector may not discuss her debt with her daughter.

1. A collector generally cannot discuss a debt with anyone other than her or her spouse.
2. Help her ask for a written validation notice.
3. Within 30 days of getting it, help her send a dispute letter by certified mail with a return receipt, saying she does not owe the money and asking for verification. Keep a copy.
4. Report the collector to the FTC at reportfraud.ftc.gov, the CFPB at cfpb.gov/complaint, or her state attorney general.

She should not share personal information until the validation notice arrives.

---

## tr214-r
- task: A caller demands payment for a debt the user does not recognize | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Debt collection FAQs <https://www.consumer.ftc.gov/articles/debt-collection-faqs>

**USER:**
I stayed on the phone with a debt collector and told him my birth date and address before I realized I don't recognize this debt at all. What now?

**ASSISTANT:**
Do not give them anything more, and do not pay yet.

1. Ask for a written validation notice. It lists the collector's name and address, the original creditor, and the amount owed.
2. Within 30 days of getting it, send a dispute letter saying you do not owe the money and asking for verification of the debt. Use certified mail with a return receipt, and keep a copy.
3. If you want the calls to end, send a letter asking the collector to stop contacting you.
4. Report the collector to the FTC at reportfraud.ftc.gov.

Once they receive your dispute, they must stop collecting until they send written verification.

---

## tr215-a
- task: A text says the user owes an unpaid road toll | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Alert: Got a text about unpaid tolls? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam>

**USER:**
I got a text saying I owe an unpaid toll and need to pay with a link. Is this real?

**ASSISTANT:**
It is probably a scam. Do not tap the link or reply to the text.

1. Look up your state's tolling agency yourself and contact it with a phone number or website you know is real, not the one in the text.
2. Ask the agency whether you really owe anything.
3. Report the text with your phone's "report junk" option, or forward it to 7726 (SPAM).
4. Once you have checked it and reported it, delete the text.

Scammers want you to hurry, so it is best to stop and check.

---

## tr215-c
- task: A text says the user owes an unpaid road toll | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Alert: Got a text about unpaid tolls? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam>

**USER:**
I was at the grocery store when my phone buzzed with a message from some toll service. It says I have an outstanding toll balance and must pay within a few hours or there will be extra fees. It has a long link. I'm a little worried because I did drive on a highway last month. Should I pay it right away?

**ASSISTANT:**
Please do not pay or tap the link. The rush is meant to make you react quickly.

1. Do not click any link in the text or reply to it.
2. Contact your state's tolling agency using a phone number or website you know is real, not the information in the text.
3. Ask whether you owe anything.
4. Report the text with the "report junk" option, or forward it to 7726 (SPAM).
5. Delete the text.

If the agency says you owe something, you can sort it out with them directly.

---

## tr215-g
- task: A text says the user owes an unpaid road toll | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Alert: Got a text about unpaid tolls? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam>

**USER:**
How do I handle these toll texts in the future, and where do I report them?

**ASSISTANT:**
Handle any unexpected text the same way each time.

1. Do not click any links in unexpected texts, and do not respond.
2. If you wonder whether it is real, contact the state's tolling agency using a phone number or website you know is real, not the info in the text.
3. Report the text with your phone's "report junk" option, or forward it to 7726 (SPAM).
4. Delete the text after you have checked and reported it.

For more on spotting text scams, see ftc.gov/textscams.

---

## tr215-r
- task: A text says the user owes an unpaid road toll | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Alert: Got a text about unpaid tolls? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam>

**USER:**
I tapped the link in that unpaid toll text and a page opened, but I closed it before typing anything. What should I do now?

**ASSISTANT:**
Good that you closed it. Do not respond to the text or go back to the link.

1. Contact your state's tolling agency using a phone number or website you know is real, not the one in the text.
2. Ask whether you owe any toll.
3. Report the text with your phone's "report junk" option, or forward it to 7726 (SPAM).
4. Delete the text once you have checked and reported it.

You can learn more about spotting text scams at ftc.gov/textscams.

---

## tr216-c
- task: A call or message claims to be the IRS and demands payment | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Those (not really) IRS calls <https://consumer.ftc.gov/node/298362>

**USER:**
There was a voicemail on my phone from someone who says they are with the Internal Revenue Service. The recording was very serious and says I have a problem with my taxes and to call back and arrange payment with gift cards. I am retired and nervous about anything with the IRS. I don't know if I should call the number.

**ASSISTANT:**
Please do not call that number back or pay anything. This is a message from someone pretending to be the IRS.

1. Do not give personal or financial information to anyone claiming to be from the IRS.
2. Never pay by wire transfer, prepaid card, or gift card. The IRS will not require a specific type of payment.
3. If you are in doubt, call the IRS directly at 1-800-829-1040.
4. Report it to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

It is normal to feel nervous, but you did the right thing by asking.

---

## tr216-e
- task: A call or message claims to be the IRS and demands payment | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Those (not really) IRS calls <https://consumer.ftc.gov/node/298362>

**USER:**
The caller knew my full name and address and said police would come to my door today if I hang up without paying. He said not to tell my family. I don't want trouble. What should I do?

**ASSISTANT:**
Hang up. You can end the call and you do not have to keep it secret.

1. Do not give personal or financial information to someone claiming to be from the IRS.
2. Do not pay by wire transfer, prepaid card, or gift card.
3. If you are in doubt, call the IRS directly at 1-800-829-1040.
4. Report the call to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

Please tell your family. Letting friends and family know about IRS imposters helps keep everyone safe.

---

## tr216-f
- task: A call or message claims to be the IRS and demands payment | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: Those (not really) IRS calls <https://consumer.ftc.gov/node/298362>

**USER:**
My brother got a message from someone saying they are from the IRS and he must pay right away. He's worried. How can I help him?

**ASSISTANT:**
Tell him not to respond or pay. It is likely an imposter.

1. Remind him not to give personal or financial information to someone claiming to be from the IRS.
2. Tell him never to pay by wire transfer, prepaid card, or gift card.
3. If either of you is in doubt, call the IRS directly at 1-800-829-1040.
4. Help him report it to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

Share this with other family members too, so no one else is caught off guard.

---

## tr216-g
- task: A call or message claims to be the IRS and demands payment | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: Those (not really) IRS calls <https://consumer.ftc.gov/node/298362>

**USER:**
What should I do whenever someone calls claiming to be the IRS, and how do I report it?

**ASSISTANT:**
Follow these steps every time.

1. Hang up. Do not give personal or financial information to someone claiming to be from the IRS.
2. Do not send money by wire transfer, prepaid card, or gift card to them.
3. If in doubt, call the IRS directly at 1-800-829-1040.
4. Report phony IRS calls to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.
5. Tell family and friends about IRS imposters.

To block unwanted calls, see ftc.gov/calls.

---

## tr216-r
- task: A call or message claims to be the IRS and demands payment | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Those (not really) IRS calls <https://consumer.ftc.gov/node/298362>; FTC Consumer Advice: What to know about identity theft <https://consumer.ftc.gov/articles/what-know-about-identity-theft>

**USER:**
A person claiming to be from the IRS called, and I gave them my Social Security number and bank name before I got suspicious. What do I do now?

**ASSISTANT:**
Stop talking to them and do not give anything more.

1. Hang up if they call again. Do not give more personal or financial information.
2. Do not send money by wire transfer, prepaid card, or gift card.
3. Go to IdentityTheft.gov to report it to the Federal Trade Commission. You will get a free personal recovery plan with next steps.
4. Contact one of the three credit bureaus to place a free, one-year fraud alert. That company must tell the other two.
5. Check your bank account statement for withdrawals you did not make, since those could be a sign of identity theft.
6. Get your free credit reports to monitor your credit.
7. Report the call to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

For more on stopping imposter scams, visit ftc.gov/imposters.

---

## tr217-c
- task: A caller says the user missed jury duty and must pay a fine | platform: any | scenario: direct_messy | sensitive: True
- sources: U.S. Courts: Court Scams Affect Citizens Nationwide <https://www.uscourts.gov/node/14024>

**USER:**
I got a voicemail from a woman who said she is with the federal court. She said I failed to appear for jury service, gave me a hearing time and my name, and left a number to call back right away to settle a fine. I never got a jury summons that I remember. I don't know what to do and I'm shaking.

**ASSISTANT:**
Take a breath. Please do not call that number back or share any information. A federal court will never threaten you or demand immediate payment.

1. Step away from the message so you can think calmly. Scammers use fear to cloud judgment.
2. Contact your local court clerk's office or U.S. Marshals Service office yourself. Find court contact information at uscourts.gov/court-locator.
3. Tell the Clerk of Court's office of the U.S. District Court in your area about the message.

Scammers use specific names and designated court hearing times.

---

## tr217-f
- task: A caller says the user missed jury duty and must pay a fine | platform: any | scenario: helper | sensitive: True
- sources: U.S. Courts: Court Scams Affect Citizens Nationwide <https://www.uscourts.gov/node/14024>

**USER:**
My husband got a call saying he missed jury duty and owes a fine, and he is panicking. How do I help him?

**ASSISTANT:**
Help him stay calm and not pay anything. A federal court will never threaten anyone or demand immediate payment.

1. Have him hang up and not give the caller any information.
2. Together, contact your local court clerk's office or U.S. Marshals Service office. Find it at uscourts.gov/court-locator.
3. Notify the Clerk of Court's office of the U.S. District Court in your area about the call.

Remind him that jurors who miss jury duty are usually contacted by the court Clerk's Office, and a judge imposes any fine in open court.

---

## tr217-g
- task: A caller says the user missed jury duty and must pay a fine | platform: any | scenario: prevention | sensitive: True
- sources: U.S. Courts: Court Scams Affect Citizens Nationwide <https://www.uscourts.gov/node/14024>

**USER:**
How does a real court handle someone who misses jury duty, so I can tell a fake call?

**ASSISTANT:**
Here is how the real process goes, and how to spot a fake call.

1. Jurors who miss jury duty are typically contacted by the court Clerk's Office.
2. Any fine is imposed by a judge in open court, and the juror can explain before it is imposed.
3. A federal court will never threaten you or demand immediate payment by phone or money wire service.
4. If someone calls like that, hang up and contact your local court clerk's office or U.S. Marshals Service office.
5. Report it to the Clerk of Court's office of the U.S. District Court in your area. Find it at uscourts.gov/court-locator.

---

## tr217-r
- task: A caller says the user missed jury duty and must pay a fine | platform: any | scenario: already_acted | sensitive: True
- sources: U.S. Courts: Court Scams Affect Citizens Nationwide <https://www.uscourts.gov/node/14024>; FTC Consumer Advice: What to do if you were scammed <https://consumer.ftc.gov/articles/what-do-if-you-were-scammed>

**USER:**
I already wired money to a man who said I missed jury duty. Now I think it was a scam. What do I do?

**ASSISTANT:**
I am sorry. Please act right away.

1. Report it to the wire transfer company immediately, such as Western Union or MoneyGram, and ask them to refund your money.
2. Contact your local court clerk's office or U.S. Marshals Service office right away and tell them what happened.
3. Find the court's contact information at uscourts.gov/court-locator.
4. Notify the Clerk of Court's office of the U.S. District Court in your area.
5. Report it to the FTC at ReportFraud.ftc.gov.
6. If he calls again, hang up and do not give him any information.

Your money might be gone already, but it is always worth asking the company if there is a way to get it back. A federal court will never demand immediate payment by telephone or money wire service.

---

## tr218-a
- task: An email claims to have embarrassing video or a password and demands payment | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Alert: Scam emails demand Bitcoin, threaten blackmail <https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail>

**USER:**
I got an email saying the sender hacked my computer and recorded me on adult websites. They will send the video to my family unless I pay in Bitcoin. What do I do?

**ASSISTANT:**
Do not pay anything. This is a scam, and the claims are all talk.

1. Do not pay anything.
2. Delete the message.
3. Report it to the FTC at ReportFraud.ftc.gov.

Scammers claim they have a video of you or access to your computer or webcam, but that is just a threat to scare you.

---

## tr218-c
- task: An email claims to have embarrassing video or a password and demands payment | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Alert: Scam emails demand Bitcoin, threaten blackmail <https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail>

**USER:**
Something terrible came in my email today. It had a password I used to use years ago right in the first line, and said they have my webcam and a video of me. I haven't done anything wrong but now I am frightened they actually have access to my computer. They want money in Bitcoin by tonight. How would they know my password?

**ASSISTANT:**
Please do not pay. This is a scam, and it is understandable to be frightened.

1. They may really know one of your old or recent passwords. They may have gotten your email from a data breach, which is likely why it appeared in the message.
2. Their claims about your webcam and computer are all talk.
3. Change the password on the account named in the message, and consider updating your other passwords too.
4. Delete the message.
5. Report it to the FTC at ReportFraud.ftc.gov.

---

## tr218-f
- task: An email claims to have embarrassing video or a password and demands payment | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Alert: Scam emails demand Bitcoin, threaten blackmail <https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail>

**USER:**
My dad got an email demanding Bitcoin or they'll send a video of him to his friends. He's embarrassed and wants to pay. What should I tell him?

**ASSISTANT:**
Tell him not to pay. It is a scam, and he is not in trouble.

1. Explain that the claims about a video and access to his computer or webcam are all talk.
2. Have him delete the message.
3. If it includes a password, help him change the password on that account, and consider updating his other passwords too.
4. Help him report the message to the FTC at ReportFraud.ftc.gov.

The password may be one he used before, possibly from a data breach.

---

## tr218-g
- task: An email claims to have embarrassing video or a password and demands payment | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Alert: Scam emails demand Bitcoin, threaten blackmail <https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail>

**USER:**
How can I tell these blackmail emails are fake, and what should I do with them in the future?

**ASSISTANT:**
Here is what these emails usually look like and what to do.

1. They claim the sender hacked your computer and recorded you, and threaten to send the video to friends and family within hours unless you pay in Bitcoin.
2. They may include one of your old or recent passwords. That can come from a data breach, and does not mean they hacked you.
3. Their claims about your computer or webcam are all talk.
4. Do not pay anything, and delete the message.
5. Change the password on the account named, consider updating others, and report it at ReportFraud.ftc.gov.

---

## tr219-a
- task: Is it safe to use public Wi-Fi (FTC) | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: Are Public Wi-Fi Networks Safe? What You Need to Know <https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know>

**USER:**
Is it okay to check my email at the coffee shop using their free Wi-Fi?

**ASSISTANT:**
Yes, it is usually safe now. Here is how to check the website.

1. Open your email in a web browser.
2. Look at the address bar at the top.
3. Make sure you see a lock symbol or **https** in the address.

A lock symbol means the connection is encrypted, but it does not prove the website is the real one, because scammers can build fake websites that use encryption. This works on a phone browser too. Most websites use encryption these days, which is why public Wi-Fi is usually safe. Also use a strong password for your email, and turn on two-factor authentication if it is offered. Keep your phone's operating system updated, and turn on automatic updates to get the latest protections.

---

## tr219-c
- task: Is it safe to use public Wi-Fi (FTC) | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Are Public Wi-Fi Networks Safe? What You Need to Know <https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know>

**USER:**
I am staying at a hotel for my daughter's wedding and the front desk gave me the Wi-Fi password. My grandson set up my tablet before I left and told me to be careful but he did not say how. I want to look at my account on a website tonight. What should I look for so I know it is safe to type my password?

**ASSISTANT:**
Before you type your password, look at the address bar at the top of the page. You should see a lock symbol or **https**. That means the website scrambles your information as it travels, and most websites do this now.

1. Open the website in your tablet's browser.
2. Check the address bar for the lock symbol or **https**.
3. If you see it, the connection is encrypted, but that does not prove the site is the real one, because scammers can build fake websites that use encryption.

Then sign in with a strong password. If the site offers two-factor authentication, turn it on. Keep your tablet's software updated too, and you can turn on automatic updates so it happens on its own.

---

## tr219-e
- task: Is it safe to use public Wi-Fi (FTC) | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Are Public Wi-Fi Networks Safe? What You Need to Know <https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know>

**USER:**
I never use a browser, I only use the little apps on my phone, like my pharmacy app, while I sit in the library using their Wi-Fi. There is no address bar to look at in an app, so how do I know if it's safe?

**ASSISTANT:**
You are right, an app has no address bar, and it can be hard to tell if an app uses encryption. The good news is that the majority of apps do.

To protect yourself while using the library Wi-Fi:

1. Use a strong password for each of your accounts.
2. Turn on two-factor authentication when an app offers it.
3. Update your phone's operating system.
4. Turn on automatic updates, so you get the latest protections.

---

## tr219-g
- task: Is it safe to use public Wi-Fi (FTC) | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: Are Public Wi-Fi Networks Safe? What You Need to Know <https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know>

**USER:**
How can I tell a fake website from a real one when I'm out using public Wi-Fi? My friend said the lock symbol is enough.

**ASSISTANT:**
The lock symbol is not enough by itself. Scammers can make fake websites that use encryption to look safe. Your data may be scrambled on the way there, but it is not safe from the scammers running the site.

1. Be wary of any website or message that claims to be from a well-known company or the government.
2. Still look for the lock symbol or **https**, but do not treat it as proof the site is real.
3. Report scammers to the FTC at ReportFraud.ftc.gov.

---

## tr220-a
- task: A package arrives that the user never ordered (FTC) | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Alert: Got a package you didn't order? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam>

**USER:**
A box came to my door today with a set of kitchen knives in it. I never ordered anything. What do I do?

**ASSISTANT:**
Do not contact the seller. Anyone who replies will likely try to get more sensitive information from you. Here is what to do.

1. Keep the item. Do not send it back.
2. Change the passwords on all your online shopping accounts, in case they were compromised.
3. Check your credit report for free at AnnualCreditReport.com. You can check it every week.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

An unexpected package can mean someone has your personal information, so these steps are worth doing today.

---

## tr220-c
- task: A package arrives that the user never ordered (FTC) | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Alert: Got a package you didn't order? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam>

**USER:**
So I got a package from Amazon yesterday, a phone case for a phone I don't even own. I looked at my orders and there is nothing there. My husband says just throw it out but I feel uneasy about it. The return label is stuck on it already. What is the right thing to do?

**ASSISTANT:**
Please do not send it back, and do not throw it out yet. Keep the item. Here is what to do.

1. Do not contact the sender. Anyone who responds will likely try to get more sensitive information from you.
2. Send Amazon a message about it, so they can investigate removing the seller.
3. Change the passwords on all your online shopping accounts, in case they were compromised.
4. Check your credit report for free at AnnualCreditReport.com.
5. Report the scam to the FTC at ReportFraud.ftc.gov.

An unexpected package can mean someone has your personal information, so your uneasy feeling is a good instinct.

---

## tr220-e
- task: A package arrives that the user never ordered (FTC) | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Alert: Got a package you didn't order? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam>

**USER:**
There is a phone number printed on the packing slip of this package I never ordered. I would like to just call them and politely tell them to come pick it up. Is that fine?

**ASSISTANT:**
Please do not call that number. Do not contact the sender, even if you look them up online. Anyone who replies will likely try to get more sensitive information from you so they can steal your money.

1. Keep the item. Do not send it back.
2. Change the passwords on all your online shopping accounts.
3. Check your credit report weekly for free at AnnualCreditReport.com.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

---

## tr220-f
- task: A package arrives that the user never ordered (FTC) | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Alert: Got a package you didn't order? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam>

**USER:**
My neighbor is 82 and keeps getting boxes she never ordered. She wants to mail them all back. What should I tell her?

**ASSISTANT:**
Tell her not to mail them back, and not to contact the sender. Anyone who replies will likely be asked for more sensitive information. Here is what she should do.

1. Keep the items.
2. Change the passwords on all her online shopping accounts, in case they were compromised.
3. Check her credit report for free at AnnualCreditReport.com.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

If a package came from Amazon or another online marketplace, she can send that company a message so they can investigate removing the seller.

---

## tr220-g
- task: A package arrives that the user never ordered (FTC) | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Alert: Got a package you didn't order? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam>

**USER:**
Why would anyone send me stuff I didn't buy? I want to understand it and know where to report it.

**ASSISTANT:**
This is called a brushing scam. Sellers ship goods you did not order, then post fake reviews in your name to boost their sales. It can also mean someone has your personal information.

1. Keep what arrives and do not contact the sender.
2. Change the passwords on your online shopping accounts.
3. Check your credit weekly for free at AnnualCreditReport.com.
4. Report fake reviews and scams to the FTC at ReportFraud.ftc.gov.

---

## tr220-r
- task: A package arrives that the user never ordered (FTC) | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Alert: Got a package you didn't order? It's probably a scam <https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam>

**USER:**
I already emailed the company on the package slip to ask what it was, and they wrote back asking for my full address and card number to confirm my order. I haven't answered yet. Should I?

**ASSISTANT:**
No, do not answer them. Anyone who replies to the sender will likely be asked for more sensitive information so they can steal your money. Stop contacting them, then do these steps.

1. Keep the item. Do not send it back.
2. Change the passwords on all your online shopping accounts.
3. Check your credit report for free at AnnualCreditReport.com, and check it every week.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

---

## tr221-a
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Alert (2022): timeshare resale company charged upfront fees <https://consumer.ftc.gov/node/298260>

**USER:**
A company called me and said they have a buyer for my timeshare, but I have to pay a $1,500 fee first. Is this legit?

**ASSISTANT:**
Do not pay the upfront fee yet. In one FTC case, the reseller charged an up-front fee, usually $500 to $2,500, and then did not sell the property. Check them out first.

1. Contact your state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
2. Search online for complaints about the company.
3. Look for a reseller that takes its fee after the timeshare is sold.
4. If you must pay any fee in advance, get the refund policies in writing.
5. Read the contract to check that it lists the services, the fees, and when you pay, and matches what you were told.

Do not sign if the deal is not what you expected.

If you have been scammed, report it to the FTC at ftc.gov/complaint.

---

## tr221-e
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Alert (2022): timeshare resale company charged upfront fees <https://consumer.ftc.gov/node/298260>

**USER:**
The salesman says the buyer's offer ends tomorrow, so I have to pay the $900 fee today. He says the fee is fully refundable. I really do not want to lose this buyer. What should I do?

**ASSISTANT:**
Do not pay today because of a deadline. Take the time to check first. If you must pay in advance, get the refund policy in writing, not just by phone.

1. Contact your state Attorney General and local consumer protection agencies where the company is located, and ask about complaints.
2. Search online for complaints about the company.
3. Read the contract to make sure it lists the services, fees, and when you pay, and that it matches what he told you.
4. If the deal is not what you expected, do not sign.

It is better to deal with a reseller that takes fees after the timeshare is sold.

---

## tr221-f
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Alert (2022): timeshare resale company charged upfront fees <https://consumer.ftc.gov/node/298260>

**USER:**
My dad is 79 and wants to pay a company $2,000 to sell his timeshare. How can I help him check if it's real?

**ASSISTANT:**
Ask him to wait before paying anything. Then you can check the company together.

1. Contact the state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
2. Search online for complaints about the company.
3. Look at the contract together. It should list the services, fees, and payment timing, and match what the company told him.
4. If he must pay in advance, get the refund policy in writing.

It is better to use a reseller that takes its fee after the timeshare is sold. If the deal is not what he expected, he should not sign.

---

## tr221-g
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Alert (2022): timeshare resale company charged upfront fees <https://consumer.ftc.gov/node/298260>

**USER:**
How do I pick a safe company if I ever want to sell my timeshare? And where do I report a bad one?

**ASSISTANT:**
Check out any reseller before you agree to anything.

1. Contact your state Attorney General and local consumer protection agencies where the reseller is located. Ask whether they have complaints on file.
2. Search online for complaints.
3. Pick a reseller that takes its fees after the timeshare is sold. If you must pay in advance, get the refund policy in writing.
4. Read the contract to make sure it matches what you were told. Do not sign if the deal is not what you expected.

To report a bad company, go to ftc.gov/complaint.

---

## tr221-r
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Alert (2022): timeshare resale company charged upfront fees <https://consumer.ftc.gov/node/298260>

**USER:**
I paid a resale company $1,800 four months ago to sell my timeshare. Nothing has been sold and they stopped answering. What can I do now?

**ASSISTANT:**
You can report this. Here is what to do.

1. Report it to the FTC at ftc.gov/complaint.
2. Contact your state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
3. Search online for complaints about the company.

You did not do anything foolish. The FTC describes a company that charged an up-front fee and did not sell the property.

---

## tr222-a
- task: Someone asks the user to receive money and forward it (FTC) | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice blog: Avoiding a money mule scam <https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam>

**USER:**
A man I met on a dating site mailed me a check and asked me to wire part of it to his friend. Should I do it?

**ASSISTANT:**
Do not forward any of the money, and stop talking to him. A fake check might clear at first, and then the bank can make you repay the full amount. Scammers use people to move stolen money, and you could get into legal trouble even if you did not know.

1. Do not send any of the money onward.
2. Stop communicating with him.
3. Report it to the FTC at ReportFraud.ftc.gov.

---

## tr222-c
- task: Someone asks the user to receive money and forward it (FTC) | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice blog: Avoiding a money mule scam <https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam>

**USER:**
Someone messaged me on Facebook and said I was picked for a $5,000 grant. They want to send it to my bank account first and then have me send $1,000 back to them as a fee to their courier by gift cards. They sound very professional and I could use the help. Is this normal?

**ASSISTANT:**
No, this is not normal. Do not forward any money, and stop communicating with this person. Scammers send money, often by check or Bitcoin, then ask you to forward part of it by gift cards or wire transfers. The money is stolen, and you could get into legal trouble for moving it. Gift cards and wire transfers are almost like sending cash, and it is almost impossible to recover the money.

1. Do not accept the grant money and send some of it onward.
2. Stop messaging the person.
3. Report it to the FTC at ReportFraud.ftc.gov.

---

## tr222-e
- task: Someone asks the user to receive money and forward it (FTC) | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice blog: Avoiding a money mule scam <https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam>

**USER:**
My new online friend deposited a check in my account and it already shows as available. She says I can keep $300 and just send the rest to her cousin by wire, and not to bother the bank about it. The money is there, so it must be real, right?

**ASSISTANT:**
Please do not send anything. A scammer's check might clear at first and still be fake. If the bank finds out later, it can make you repay the full amount, and you may face fees, an overdrawn account, or a closed account.

1. Stop the wire transfer.
2. Stop communicating with her.
3. Tell your bank right away.
4. Report it to the FTC at ReportFraud.ftc.gov.

You could also get into legal trouble if you help move stolen money, even by accident.

---

## tr222-f
- task: Someone asks the user to receive money and forward it (FTC) | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice blog: Avoiding a money mule scam <https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam>

**USER:**
My mother says her online boyfriend sends her money and she forwards some to his business partner with gift cards. I think something is wrong. What should I tell her?

**ASSISTANT:**
Tell her to stop forwarding money and to stop communicating with him. Scammers send money, then ask people to forward it, and the money is stolen. She could get into legal trouble even if she did not know.

1. Stop any payment she can still stop.
2. Tell her bank and any gift card companies right away.
3. If he has her bank account information, close her account immediately.
4. Report it to the FTC at ReportFraud.ftc.gov.

---

## tr222-g
- task: Someone asks the user to receive money and forward it (FTC) | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice blog: Avoiding a money mule scam <https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam>

**USER:**
What are the warning signs of being asked to be a money mule, so I never fall for it?

**ASSISTANT:**
A money mule helps scammers move stolen money. Scammers find people on dating, job search, and social media sites. Watch for these:

1. Do not forward money for an online romantic interest who sends you money.
2. Do not accept a job that asks you to transfer money or packages, even if you are told it goes to a client or supplier.
3. Do not accept a grant or prize award and forward some of the money.

If you are asked, stop communicating with the person and report it to the FTC at ReportFraud.ftc.gov.

---

## tr222-r
- task: Someone asks the user to receive money and forward it (FTC) | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice blog: Avoiding a money mule scam <https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam>

**USER:**
I deposited a check from an online boyfriend and sent $2,000 of it to someone he named by wire. Now my bank says the check is bad. He also has my bank account number. What do I do?

**ASSISTANT:**
Act right away. Here is what to do.

1. Stop the payment transaction if you can.
2. Stop communicating with him.
3. Tell your bank and the wire transfer service right away.
4. He has your bank account information, so close your account immediately.
5. Report it to the FTC at ReportFraud.ftc.gov.

You may have been used to move stolen money without knowing it, so doing these steps quickly matters.

---

## tr223-c
- task: A rental listing asks for a deposit before any viewing (FTC) | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Rental Listing Scams <https://consumer.ftc.gov/articles/rental-listing-scams>

**USER:**
I am moving for a new job and saw a lovely little house on a classifieds website. The owner says she is overseas on missionary work, so I cannot see the house, but she will mail me the keys once I send a deposit by Western Union. She also asked for my Social Security number for a background check. It sounds so kind. What do you think?

**ASSISTANT:**
Please do not send the deposit or your Social Security number. A fake owner will usually claim to be out of the country when you ask to see the rental, and insisting on Western Union is another warning sign. Sending money that way is the same as sending cash, and you probably cannot get it back.

1. Until you have agreed to rent, a landlord does not need your Social Security number or other sensitive information.
2. Search the owner's name with "complaint," "review," or "scam."
3. Look up who owns the house on the city or county tax assessment website.
4. If anyone pressures you to decide quickly, walk away.

---

## tr223-e
- task: A rental listing asks for a deposit before any viewing (FTC) | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Rental Listing Scams <https://consumer.ftc.gov/articles/rental-listing-scams>

**USER:**
I live in another state and cannot drive over to see the apartment before I pay. The agent says I must wire the deposit by Friday or someone else gets it. How can I be sure it is real?

**ASSISTANT:**
Do not wire the deposit by Friday. If anyone pressures you to decide quickly, walk away. Wiring money is the same as sending cash, and you probably cannot get it back. You can still check from far away.

1. Search the company's or agent's name with "complaint," "review," or "scam."
2. Check whether the property is listed on the rental company's own website.
3. Ask the agent for a business card from the company that owns or manages the property, and check the ID against the records.
4. For a private landlord, look up who owns the property on the city or county tax assessment website.
5. Contact the owner or company using contact details you already have.

---

## tr223-f
- task: A rental listing asks for a deposit before any viewing (FTC) | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: Rental Listing Scams <https://consumer.ftc.gov/articles/rental-listing-scams>

**USER:**
My granddaughter found a cheap apartment online and the owner wants a deposit and her credit score before showing it. Is that normal?

**ASSISTANT:**
Tell her not to pay or share anything yet. Rent that is a lot cheaper than most in the area is a sign of a scam. Also, most landlords pull your credit score themselves, so be wary of anyone asking her to get her own score for them.

1. Until she agrees to rent a place, a landlord does not need her Social Security number, credit score, or other sensitive information.
2. If she can, she should look at the property before she signs or pays.
3. Search the owner's name with "complaint," "review," or "scam."
4. Check whether the property is listed on the rental company's own website.

---

## tr223-g
- task: A rental listing asks for a deposit before any viewing (FTC) | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: Rental Listing Scams <https://consumer.ftc.gov/articles/rental-listing-scams>

**USER:**
What are the warning signs of a fake rental ad? I want to avoid getting scammed when I search for a home.

**ASSISTANT:**
Here are the warning signs.

1. Surprisingly low rent or amazing amenities.
2. Other ads for the same address, but with a different owner or company name.
3. An owner who claims to be out of the country when you ask to see the rental.
4. A home that is also listed for sale instead of for rent.
5. Pressure to decide quickly, or a demand to pay by wire transfer, gift cards, or cryptocurrency.

If you see any of these, walk away. To report a fake ad, tell the website where it was posted and the FTC at ReportFraud.ftc.gov.

---

## tr223-r
- task: A rental listing asks for a deposit before any viewing (FTC) | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Rental Listing Scams <https://consumer.ftc.gov/articles/rental-listing-scams>

**USER:**
I already sent $1,200 in gift cards as a deposit for an apartment and now the landlord is not answering and the ad is gone. What do I do?

**ASSISTANT:**
I am sorry. Once you send gift cards it is probably hard to get the money back, but you should report it right away.

1. Report it to your local law enforcement agency.
2. Report it to the website where the ad was posted.
3. Report it to the FTC at ReportFraud.ftc.gov.
4. You can also report it to your state attorney general.

If you shared personal information with the scammer, the FTC has an identity theft article that can help.

---

## tr224-a
- task: A company promises to stop foreclosure for an upfront fee (FTC) | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: Mortgage Relief Scams <https://consumer.ftc.gov/articles/mortgage-relief-scams>

**USER:**
A company says they can stop my house from being foreclosed if I pay them $2,000 up front. Should I pay?

**ASSISTANT:**
Do not pay them. Asking for money upfront, before any results, is a sign of a scam. Here is what to do.

1. Contact your servicer or lender right away, even if the foreclosure has already started.
2. Talk to a certified housing counselor for free. You can find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. You can also call Making Home Affordable at 1-888-995-HOPE (4673).

It is illegal for a company to charge you a penny until it has given you a written offer for a loan modification or other relief from your lender, and you accept the offer.

---

## tr224-c
- task: A company promises to stop foreclosure for an upfront fee (FTC) | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Mortgage Relief Scams <https://consumer.ftc.gov/articles/mortgage-relief-scams>

**USER:**
I fell behind on my mortgage after my surgery and a man phoned saying he is a government foreclosure specialist. He wants me to sign my deed over to his company so they can hold the house safe while they fix things and he said I should stop calling my bank because it will only make things worse. He is so confident. Should I do what he says?

**ASSISTANT:**
Please do not sign over your deed, and do not stop talking to your bank. A company cannot tell you to stop talking to your lender. Asking you to transfer the deed and claiming to be from the government are signs of a scam.

1. Contact your servicer or lender right away, even if the foreclosure has started.
2. Talk to a certified housing counselor for free. Find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. Keep a file of every call, letter, email, text, and paper you receive.

---

## tr224-f
- task: A company promises to stop foreclosure for an upfront fee (FTC) | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: Mortgage Relief Scams <https://consumer.ftc.gov/articles/mortgage-relief-scams>

**USER:**
My brother is behind on his mortgage and a company wants a fee before doing anything. How can I help him?

**ASSISTANT:**
Tell him not to pay any money until a company delivers the results he wants. Here is how you can help.

1. Help him contact his servicer or lender right away, even if foreclosure has started.
2. Help him talk to a certified housing counselor for free. A HUD-approved agency can be found at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. He can also call Making Home Affordable at 1-888-995-HOPE (4673).
4. Keep a file of every conversation, letter, email, text, and paper.

---

## tr224-g
- task: A company promises to stop foreclosure for an upfront fee (FTC) | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: Mortgage Relief Scams <https://consumer.ftc.gov/articles/mortgage-relief-scams>

**USER:**
How do I spot a mortgage relief scam, and where do I report one?

**ASSISTANT:**
Watch for these signs.

1. They demand payment upfront, before any services.
2. They want payment only by cashier's check, wire transfer, or a mobile payment app.
3. They try to get you to transfer your deed to them.
4. They tell you not to contact your lender, lawyer, or housing counselor.
5. They claim to be housing counselors, lawyers, or government representatives.

To report one, go to the FTC at reportfraud.ftc.gov, or contact your state attorney general.

---

## tr224-r
- task: A company promises to stop foreclosure for an upfront fee (FTC) | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Mortgage Relief Scams <https://consumer.ftc.gov/articles/mortgage-relief-scams>

**USER:**
I already wired $1,800 to a company that promised to save my home and now they won't return my calls. What can I do?

**ASSISTANT:**
Act quickly, because the sooner you act, the better. Scammers often use payment methods that are hard to reverse.

1. Report it to the FTC at reportfraud.ftc.gov.
2. Report it to your state attorney general.
3. Contact your servicer or lender right away, even if the foreclosure has started.
4. Talk to a certified housing counselor for free. Find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.

The FTC also has a page on how to try to get your money back: consumer.ftc.gov/articles/what-do-if-you-were-scammed.

---
