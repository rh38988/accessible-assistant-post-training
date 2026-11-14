# Review input: batch ny8b, round 2 (16 examples)

## tr219-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
Is it okay to check my email at the coffee shop using their free Wi-Fi?

**ASSISTANT:**
Yes, it is usually safe now. Here is how to check the website.

1. Open your email in a web browser.
2. Look at the address bar at the top.
3. Make sure you see a lock symbol or **https** in the address.

A lock symbol means the connection is encrypted, but it does not prove the website is the real one, because scammers can build fake websites that use encryption. This works on a phone browser too. Most websites use encryption these days, which is why public Wi-Fi is usually safe. Also use a strong password for your email, and turn on two-factor authentication if it is offered. Keep your phone's operating system updated, and turn on automatic updates to get the latest protections.

## tr219-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
I am staying at a hotel for my daughter's wedding and the front desk gave me the Wi-Fi password. My grandson set up my tablet before I left and told me to be careful but he did not say how. I want to look at my account on a website tonight. What should I look for so I know it is safe to type my password?

**ASSISTANT:**
Before you type your password, look at the address bar at the top of the page. You should see a lock symbol or **https**. That means the website scrambles your information as it travels, and most websites do this now.

1. Open the website in your tablet's browser.
2. Check the address bar for the lock symbol or **https**.
3. If you see it, the connection is encrypted, but that does not prove the site is the real one, because scammers can build fake websites that use encryption.

Then sign in with a strong password. If the site offers two-factor authentication, turn it on. Keep your tablet's software updated too, and you can turn on automatic updates so it happens on its own.

## tr219-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
I just typed my password into a shopping website on the airport Wi-Fi and now I'm worried. Did I do something dangerous?

**ASSISTANT:**
Check right away whether that shopping website was the real one. Scammers can build fake websites that use encryption, so a lock symbol alone does not prove the site was safe.

1. Look at the address bar for a lock symbol or **https**.
2. Use a strong password on your accounts, and turn on two-factor authentication if the site offers it.
3. Make sure the website is the real one. On a scammer's website, your information is not safe, even if it is encrypted.

If you think the site was fake, report it to the FTC at ReportFraud.ftc.gov.

## tr219-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
My mother uses the library Wi-Fi on her laptop to pay her bills. What should I tell her so she stays safe?

**ASSISTANT:**
Tell her that public Wi-Fi is usually safe now, because most websites use encryption. She should check two things.

1. Before she signs in, look for a lock symbol or **https** in the address bar.
2. Use a strong password and turn on two-factor authentication when it is available.

A lock symbol does not prove the site is the real one, because scammers can build fake websites that use encryption.

Also help her keep her laptop's security software, operating system, and internet browser up to date. Turning on automatic updates will do much of that for her.

## tr220-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

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

## tr220-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

**USER:**
There is a phone number printed on the packing slip of this package I never ordered. I would like to just call them and politely tell them to come pick it up. Is that fine?

**ASSISTANT:**
Please do not call that number. Do not contact the sender, even if you look them up online. Anyone who replies will likely try to get more sensitive information from you so they can steal your money.

1. Keep the item. Do not send it back.
2. Change the passwords on all your online shopping accounts.
3. Check your credit report weekly for free at AnnualCreditReport.com.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

## tr221-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

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

## tr221-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

**USER:**
We got a nice glossy letter in the mail from a resale firm saying they can sell our Florida timeshare quickly. My husband and I have not used it in years and the fees keep coming. The letter says to send a check to hold our spot in line. We are retired and I do not want to make a mistake.

**ASSISTANT:**
Please hold off on sending the check. A company that asks for money before it sells anything deserves a close look.

1. Contact your state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
2. Search online for complaints about the company.
3. Ask for the fees and the contract in writing. Read it to make sure it matches what you were told, and do not sign if the deal is not what you expected.

If you must pay any fee in advance, get the refund policies in writing.

It is better to use a reseller that takes its fee after the timeshare is sold.

## tr221-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

**USER:**
I paid a resale company $1,800 four months ago to sell my timeshare. Nothing has been sold and they stopped answering. What can I do now?

**ASSISTANT:**
You can report this. Here is what to do.

1. Report it to the FTC at ftc.gov/complaint.
2. Contact your state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
3. Search online for complaints about the company.

You did not do anything foolish. The FTC describes a company that charged an up-front fee and did not sell the property.

## tr222-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
A man I met on a dating site mailed me a check and asked me to wire part of it to his friend. Should I do it?

**ASSISTANT:**
Do not forward any of the money, and stop talking to him. A fake check might clear at first, and then the bank can make you repay the full amount. Scammers use people to move stolen money, and you could get into legal trouble even if you did not know.

1. Do not send any of the money onward.
2. Stop communicating with him.
3. Report it to the FTC at ReportFraud.ftc.gov.

## tr222-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
Someone messaged me on Facebook and said I was picked for a $5,000 grant. They want to send it to my bank account first and then have me send $1,000 back to them as a fee to their courier by gift cards. They sound very professional and I could use the help. Is this normal?

**ASSISTANT:**
No, this is not normal. Do not forward any money, and stop communicating with this person. Scammers send money, often by check or Bitcoin, then ask you to forward part of it by gift cards or wire transfers. The money is stolen, and you could get into legal trouble for moving it. Gift cards and wire transfers are almost like sending cash, and it is almost impossible to recover the money.

1. Do not accept the grant money and send some of it onward.
2. Stop messaging the person.
3. Report it to the FTC at ReportFraud.ftc.gov.

## tr222-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
My new online friend deposited a check in my account and it already shows as available. She says I can keep $300 and just send the rest to her cousin by wire, and not to bother the bank about it. The money is there, so it must be real, right?

**ASSISTANT:**
Please do not send anything. A scammer's check might clear at first and still be fake. If the bank finds out later, it can make you repay the full amount, and you may face fees, an overdrawn account, or a closed account.

1. Stop the wire transfer.
2. Stop communicating with her.
3. Tell your bank right away.
4. Report it to the FTC at ReportFraud.ftc.gov.

You could also get into legal trouble if you help move stolen money, even by accident.

## tr222-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

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

## tr223-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A rental listing asks for a deposit before any viewing (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

**USER:**
I found an apartment online with great rent. The owner says to send a deposit first and then I can see it. Is that okay?

**ASSISTANT:**
Do not send the deposit before you see the place. A landlord that wants money first, and low rent, are signs of a scam. Once scammers get your money, they disappear. Here is what to do.

1. If you can, look at the property before you sign or pay.
2. Search the owner's name with the words "complaint," "review," or "scam."
3. Check whether the property is listed on the rental company's own website.
4. If the owner pressures you to decide quickly, walk away.

## tr224-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A company promises to stop foreclosure for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

**USER:**
A company says they can stop my house from being foreclosed if I pay them $2,000 up front. Should I pay?

**ASSISTANT:**
Do not pay them. Asking for money upfront, before any results, is a sign of a scam. Here is what to do.

1. Contact your servicer or lender right away, even if the foreclosure has already started.
2. Talk to a certified housing counselor for free. You can find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. You can also call Making Home Affordable at 1-888-995-HOPE (4673).

It is illegal for a company to charge you a penny until it has given you a written offer for a loan modification or other relief from your lender, and you accept the offer.

## tr224-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A company promises to stop foreclosure for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

**USER:**
I already wired $1,800 to a company that promised to save my home and now they won't return my calls. What can I do?

**ASSISTANT:**
Act quickly, because the sooner you act, the better. Scammers often use payment methods that are hard to reverse.

1. Report it to the FTC at reportfraud.ftc.gov.
2. Report it to your state attorney general.
3. Contact your servicer or lender right away, even if the foreclosure has started.
4. Talk to a certified housing counselor for free. Find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.

The FTC also has a page on how to try to get your money back: consumer.ftc.gov/articles/what-do-if-you-were-scammed.
