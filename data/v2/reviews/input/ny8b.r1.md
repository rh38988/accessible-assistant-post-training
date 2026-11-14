# Review input: batch ny8b, round 1 (36 examples)

## tr219-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
Is it okay to check my email at the coffee shop using their free Wi-Fi?

**ASSISTANT:**
Yes, it is usually safe now, as long as the website is encrypted. Here is how to check.

1. Open your email in a web browser.
2. Look at the address bar at the top.
3. Make sure you see a lock symbol or **https** in the address.

This works on a phone browser too. Most websites use encryption these days, which is why public Wi-Fi is usually safe. Also use a strong password for your email, and turn on two-factor authentication if it is offered.

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
3. If you see it, go ahead and sign in with a strong password.

If the site offers two-factor authentication, turn it on. Keep your tablet's software updated too, and you can turn on automatic updates so it happens on its own.

## tr219-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
I never use a browser, I only use the little apps on my phone, like my pharmacy app, while I sit in the library using their Wi-Fi. There is no address bar to look at in an app, so how do I know if it's safe?

**ASSISTANT:**
You are right, an app has no address bar, and it can be hard to tell if an app uses encryption. The good news is that the majority of apps do.

To protect yourself while using the library Wi-Fi:

1. Use a strong password for each of your accounts.
2. Turn on two-factor authentication when an app offers it.
3. Update your phone's operating system.
4. Turn on automatic updates, so you get the latest protections.

## tr219-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
I just typed my password into a shopping website on the airport Wi-Fi and now I'm worried. Did I do something dangerous?

**ASSISTANT:**
Probably not. Most websites use encryption now, so public Wi-Fi is usually safe. Here is what to check.

1. Look at the website's address bar for a lock symbol or **https**. If it was there, your information was scrambled on its way.
2. Use a strong password on your accounts, and turn on two-factor authentication if the site offers it.
3. Make sure the website is the real one. Scammers can make fake websites that also use encryption, and your information would not be safe from the people running them.

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

Also help her keep her laptop's security software, operating system, and internet browser up to date. Turning on automatic updates will do much of that for her.

## tr219-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Is it safe to use public Wi-Fi (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

**USER:**
How can I tell a fake website from a real one when I'm out using public Wi-Fi? My friend said the lock symbol is enough.

**ASSISTANT:**
The lock symbol is not enough by itself. Scammers can make fake websites that use encryption to look safe. Your data may be scrambled on the way there, but it is not safe from the scammers running the site.

1. Be wary of any website or message that claims to be from a well-known company or the government.
2. Still look for the lock symbol or **https**, but do not treat it as proof the site is real.
3. Report scammers to the FTC at ReportFraud.ftc.gov.

## tr220-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

**USER:**
A box came to my door today with a set of kitchen knives in it. I never ordered anything. What do I do?

**ASSISTANT:**
Do not contact the seller. Anyone who replies will likely try to get more sensitive information from you. Here is what to do.

1. Keep the item. Do not send it back.
2. Change the passwords on all your online shopping accounts, in case they were compromised.
3. Check your credit report for free at AnnualCreditReport.com. You can check it every week.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

An unexpected package can mean someone has your personal information, so these steps are worth doing today.

## tr220-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

**USER:**
So I got a package from Amazon yesterday, a phone case for a phone I don't even own. I looked at my orders and there is nothing there. My husband says just throw it out but I feel uneasy about it. The return label is stuck on it already. What is the right thing to do?

**ASSISTANT:**
Please do not send it back, and do not throw it out yet. Keep the item. Here is what to do.

1. Send Amazon a message about it, so they can investigate removing the seller.
2. Change the passwords on all your online shopping accounts, in case they were compromised.
3. Check your credit report for free at AnnualCreditReport.com.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

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
3. Report the scam to the FTC at ReportFraud.ftc.gov.

## tr220-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

**USER:**
I already emailed the company on the package slip to ask what it was, and they wrote back asking for my full address and card number to confirm my order. I haven't answered yet. Should I?

**ASSISTANT:**
No, do not answer them. Anyone who replies to the sender will likely be asked for more sensitive information so they can steal your money. Stop contacting them, then do these steps.

1. Keep the item. Do not send it back.
2. Change the passwords on all your online shopping accounts.
3. Check your credit report for free at AnnualCreditReport.com, and check it every week.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

## tr220-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

**USER:**
My neighbor is 82 and keeps getting boxes she never ordered. She wants to mail them all back. What should I tell her?

**ASSISTANT:**
Tell her not to mail them back, and not to contact the sender. Anyone who replies will likely be asked for more sensitive information. Here is what she should do.

1. Keep the items.
2. Change the passwords on all her online shopping accounts, in case they were compromised.
3. Check her credit report for free at AnnualCreditReport.com.
4. Report the scam to the FTC at ReportFraud.ftc.gov.

If a package came from Amazon or another online marketplace, she can send that company a message so they can investigate removing the seller.

## tr220-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A package arrives that the user never ordered (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

**USER:**
Why would anyone send me stuff I didn't buy? I want to understand it and know where to report it.

**ASSISTANT:**
This is called a brushing scam. Sellers ship goods you did not order, then post fake reviews in your name to boost their sales. It can also mean someone has your personal information.

1. Keep what arrives and do not contact the sender.
2. Change the passwords on your online shopping accounts.
3. Check your credit weekly for free at AnnualCreditReport.com.
4. Report fake reviews and scams to the FTC at ReportFraud.ftc.gov.

## tr221-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

**USER:**
A company called me and said they have a buyer for my timeshare, but I have to pay a $1,500 fee first. Is this legit?

**ASSISTANT:**
Do not pay the upfront fee yet. Some timeshare resale companies charge a fee, usually $500 to $2,500, and then do not sell the property. Check them out first.

1. Contact your state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
2. Search online for complaints about the company.
3. Look for a reseller that takes its fee after the timeshare is sold.
4. Get everything in writing, and do not sign if the deal is not what you expected.

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

It is better to use a reseller that takes its fee after the timeshare is sold.

## tr221-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

**USER:**
The salesman says the buyer's offer ends tomorrow, so I have to pay the $900 fee today. He says the fee is fully refundable. I really do not want to lose this buyer. What should I do?

**ASSISTANT:**
Do not pay today because of a deadline. Take the time to check first. If you must pay in advance, get the refund policy in writing, not just by phone.

1. Contact your state Attorney General and local consumer protection agencies where the company is located, and ask about complaints.
2. Search online for complaints about the company.
3. Read the contract to make sure it lists the services, fees, and when you pay, and that it matches what he told you.
4. If the deal is not what you expected, do not sign.

It is better to deal with a reseller that takes fees after the timeshare is sold.

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

You did not do anything foolish. These companies often charge an upfront fee and then do not sell the property.

## tr221-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

**USER:**
My dad is 79 and wants to pay a company $2,000 to sell his timeshare. How can I help him check if it's real?

**ASSISTANT:**
Ask him to wait before paying anything. Then you can check the company together.

1. Contact the state Attorney General and the local consumer protection agencies where the company is located. Ask whether they have complaints on file.
2. Search online for complaints about the company.
3. Look at the contract together. It should list the services, fees, and payment timing, and match what the company told him.
4. If he must pay in advance, get the refund policy in writing.

It is better to use a reseller that takes its fee after the timeshare is sold. If the deal is not what he expected, he should not sign.

## tr221-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A company promises to sell the user's timeshare for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298260

**USER:**
How do I pick a safe company if I ever want to sell my timeshare? And where do I report a bad one?

**ASSISTANT:**
Check out any reseller before you agree to anything.

1. Contact your state Attorney General and local consumer protection agencies where the reseller is located. Ask whether they have complaints on file.
2. Search online for complaints.
3. Pick a reseller that takes its fees after the timeshare is sold. If you must pay in advance, get the refund policy in writing.
4. Read the contract to make sure it matches what you were told. Do not sign if the deal is not what you expected.

To report a bad company, go to ftc.gov/complaint.

## tr222-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
A man I met on a dating site mailed me a check and asked me to wire part of it to his friend. Should I do it?

**ASSISTANT:**
Do not forward any of the money, and stop talking to him. Scammers use people to move stolen money, and you could get into legal trouble even if you did not know.

1. Do not deposit the check, or do not send anything onward if you already deposited it. A fake check might clear at first, and then the bank can make you repay the full amount.
2. Stop communicating with him.
3. Report it to the FTC at ReportFraud.ftc.gov.

## tr222-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
Someone messaged me on Facebook and said I was picked for a $5,000 grant. They want to send it to my bank account first and then have me send $1,000 back to them as a fee to their courier by gift cards. They sound very professional and I could use the help. Is this normal?

**ASSISTANT:**
No, this is not normal. Do not forward any money, and stop communicating with this person. Scammers send money, often by check or Bitcoin, then ask you to forward part of it by gift cards or wire transfers. The money is stolen, and you could get into legal trouble for moving it.

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

1. Stop the wire transfer and stop communicating with her.
2. Tell your bank right away.
3. Report it to the FTC at ReportFraud.ftc.gov.

You could also get into legal trouble if you help move stolen money, even by accident.

## tr222-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
I deposited a check from an online boyfriend and sent $2,000 of it to someone he named by wire. Now my bank says the check is bad. He also has my bank account number. What do I do?

**ASSISTANT:**
Act right away. Here is what to do.

1. Stop the payment transaction if you can, and stop communicating with him.
2. Tell your bank and the wire transfer service right away.
3. He has your bank account information, so close your account immediately.
4. Report it to the FTC at ReportFraud.ftc.gov.

You may have been used to move stolen money without knowing it, so doing these steps quickly matters.

## tr222-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
My mother says her online boyfriend sends her money and she forwards some to his business partner with gift cards. I think something is wrong. What should I tell her?

**ASSISTANT:**
Tell her to stop forwarding money and to stop communicating with him. Scammers send money, then ask people to forward it, and the money is stolen. She could get into legal trouble even if she did not know.

1. Stop any payment she can still stop.
2. Tell her bank and any gift card companies right away.
3. If he has her bank account information, close her account immediately.
4. Report it to the FTC at ReportFraud.ftc.gov.

## tr222-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Someone asks the user to receive money and forward it (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

**USER:**
What are the warning signs of being asked to be a money mule, so I never fall for it?

**ASSISTANT:**
A money mule helps scammers move stolen money. Scammers find people on dating, job search, and social media sites. Watch for these:

1. Do not forward money for an online romantic interest who sends you money.
2. Do not accept a job that asks you to transfer money or packages, even if you are told it goes to a client or supplier.
3. Do not accept a grant or prize award and forward some of the money.

If you are asked, stop communicating with the person and report it to the FTC at ReportFraud.ftc.gov.

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

## tr223-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A rental listing asks for a deposit before any viewing (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

**USER:**
I am moving for a new job and saw a lovely little house on a classifieds website. The owner says she is overseas on missionary work, so I cannot see the house, but she will mail me the keys once I send a deposit by Western Union. She also asked for my Social Security number for a background check. It sounds so kind. What do you think?

**ASSISTANT:**
Please do not send the deposit or your Social Security number. A fake owner will usually claim to be out of the country when you ask to see the rental, and insisting on Western Union is another warning sign. Sending money that way is the same as sending cash, and you probably cannot get it back.

1. Until you have agreed to rent, a landlord does not need your Social Security number or other sensitive information.
2. Search the owner's name with "complaint," "review," or "scam."
3. Look up who owns the house on the city or county tax assessment website.
4. If anyone pressures you to decide quickly, walk away.

## tr223-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A rental listing asks for a deposit before any viewing (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

**USER:**
I live in another state and cannot drive over to see the apartment before I pay. The agent says I must wire the deposit by Friday or someone else gets it. How can I be sure it is real?

**ASSISTANT:**
Do not wire the deposit by Friday. If anyone pressures you to decide quickly, walk away. Wiring money is the same as sending cash, and you probably cannot get it back. You can still check from far away.

1. Search the company's or agent's name with "complaint," "review," or "scam."
2. Check whether the property is listed on the rental company's own website.
3. Ask the agent for a business card from the company that owns or manages the property, and check the ID against the records.
4. For a private landlord, look up who owns the property on the city or county tax assessment website.
5. Contact the owner or company using contact details you already have.

## tr223-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A rental listing asks for a deposit before any viewing (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

**USER:**
I already sent $1,200 in gift cards as a deposit for an apartment and now the landlord is not answering and the ad is gone. What do I do?

**ASSISTANT:**
I am sorry. Once you send gift cards it is probably hard to get the money back, but you should report it right away.

1. Report it to your local law enforcement agency.
2. Report it to the website where the ad was posted.
3. Report it to the FTC at ReportFraud.ftc.gov.
4. You can also report it to your state attorney general.

If you shared personal information with the scammer, the FTC has an identity theft article that can help.

## tr223-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A rental listing asks for a deposit before any viewing (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

**USER:**
My granddaughter found a cheap apartment online and the owner wants a deposit and her credit score before showing it. Is that normal?

**ASSISTANT:**
Tell her not to pay or share anything yet. Rent that is a lot cheaper than most in the area is a sign of a scam. Also, most landlords pull your credit score themselves, so be wary of anyone asking her to get her own score for them.

1. Until she agrees to rent a place, a landlord does not need her Social Security number, credit score, or other sensitive information.
2. If she can, she should look at the property before she signs or pays.
3. Search the owner's name with "complaint," "review," or "scam."
4. Check whether the property is listed on the rental company's own website.

## tr223-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A rental listing asks for a deposit before any viewing (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

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

A company should not charge you anything until it has given you a written offer for relief and you accept it.

## tr224-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A company promises to stop foreclosure for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

**USER:**
I fell behind on my mortgage after my surgery and a man phoned saying he is a government foreclosure specialist. He wants me to sign my deed over to his company so they can hold the house safe while they fix things and he said I should stop calling my bank because it will only make things worse. He is so confident. Should I do what he says?

**ASSISTANT:**
Please do not sign over your deed, and do not stop talking to your bank. A company cannot tell you to stop talking to your lender. Asking you to transfer the deed and claiming to be from the government are signs of a scam.

1. Contact your servicer or lender right away, even if the foreclosure has started.
2. Talk to a certified housing counselor for free. Find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. Keep a file of every call, letter, email, text, and paper you receive.

## tr224-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A company promises to stop foreclosure for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

**USER:**
They told me not to call my lender and not to tell my counselor, or it would ruin the deal. They want a cashier's check today for $1,500. I already got a foreclosure notice and I am scared. What do I do?

**ASSISTANT:**
Do not send the cashier's check. Scammers often tell you not to contact your lender or housing counselor, and no company can tell you to stop talking to your lender. Do not pay anything until a company delivers the results you want.

1. Contact your servicer or lender right away. You can do this even if the foreclosure process has already started.
2. Talk to a certified housing counselor for free. Find a HUD-approved agency at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. You can also call 1-888-995-HOPE (4673).

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

The FTC also has a guide called "What to do if you were scammed" with steps for recovering money.

## tr224-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A company promises to stop foreclosure for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

**USER:**
My brother is behind on his mortgage and a company wants a fee before doing anything. How can I help him?

**ASSISTANT:**
Tell him not to pay any money until a company delivers the results he wants. Here is how you can help.

1. Help him contact his servicer or lender right away, even if foreclosure has started.
2. Help him talk to a certified housing counselor for free. A HUD-approved agency can be found at apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm.
3. He can also call Making Home Affordable at 1-888-995-HOPE (4673).
4. Keep a file of every conversation, letter, email, text, and paper.

## tr224-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A company promises to stop foreclosure for an upfront fee (FTC) (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

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
