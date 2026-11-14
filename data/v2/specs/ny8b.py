def ex(suffix, scenario, style, messages):
    return {"suffix": suffix, "scenario": scenario, "style": style, "specification": "fully_specified", "platform": "any", "messages": messages}

TASKS = [
    {
        "task_id": "TR-219",
        "task_type": "public_wifi_safety",
        "task": "Is it safe to use public Wi-Fi",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Are Public Wi-Fi Networks Safe? What You Need to Know", "url": "https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know"},
        "source_notes": """Confirm the connection is encrypted: look for a lock symbol or https in the address bar to the left of the website address. Works on a mobile browser too. Hard to tell if a mobile app uses encryption, but the majority do.
Create and use strong passwords. Turn on two-factor authentication when it is available.
If you go online by computer, make sure security software, operating system, and internet browser are up to date. Update your phone's operating system too. Turn on automatic updates to keep up with the latest protections.
Scammers pose as a well-known company or the government. They also create fake websites and encrypt them to make you think they are safe when they are not. Encryption will not be safe from scammers operating the site.
Report scammers to the FTC at ReportFraud.ftc.gov.
NOT on the page: VPNs, auto-connect settings, specific Wi-Fi settings, lists of things to avoid, steps if information is compromised.""",
        "examples": [
            ex("a", "direct", "plain", [
                "Is it okay to check my email on the free Wi-Fi at the coffee shop? My daughter said it isn't safe.",
                """Yes, you can use it, as long as you take a few precautions. Here is what to do:

1. Before you type anything into a website, look at the address bar. A lock symbol or **https** to the left of the website address means the connection is encrypted. This works on a phone browser too.
2. Use a strong password for your email account.
3. Turn on two-factor authentication for it, if it is offered.
4. Keep your phone or computer up to date. Turn on automatic updates so you get the latest protections.

Remember that a lock does not prove a website is honest. Scammers can build fake websites with a lock too.""",
            ]),
            ex("c", "direct_messy", "verbose", [
                "We are going on a cruise next month and the ship has Wi-Fi, and I also plan to use the hotel and airport networks. I do a bit of online shopping and look at my account pages on my iPad. My neighbor said anything I type on those networks can be seen by strangers. Should I just not use them at all? I do not really understand how this works.",
                """You do not have to avoid them, but take these steps first:

1. On any website, look for a lock symbol or **https** to the left of the website address. It works in a mobile browser too.
2. Use strong passwords for your shopping and account pages.
3. Turn on two-factor authentication wherever it is offered.
4. Update your iPad's operating system, and turn on automatic updates.

Most apps use encryption, but it can be hard to tell for sure. Also, a lock on a page does not make a shop honest, because scammers set up fake websites with a lock to look safe.""",
            ]),
            ex("e", "constraint", "over_specified", [
                "I am at the library and I have to pay a bill on my laptop right now because it is due today. I cannot wait until I get home. The library Wi-Fi is the only internet I have. What should I check before I type in my card number?",
                """Check the connection first, and only continue if it looks right:

1. Look at the address bar. A lock symbol or **https** to the left of the website address means the connection is encrypted.
2. Make sure your laptop's security software, operating system, and internet browser are up to date.
3. Use a strong password if you log in to your account, and use two-factor authentication if it is offered.

A lock is not enough on its own. Scammers make fake websites with a lock to look safe, so be sure you reached the real company's website.""",
            ]),
            ex("r", "already_acted", "failure_recovery", [
                "I was at the airport on their free Wi-Fi and a page popped up offering a discount on a trip. It had the little lock and I typed in my card number. Now I am not sure it was real.",
                """Do not enter anything else on that site. A lock only means the connection is encrypted, and scammers build fake websites and encrypt them to make you think they are safe.

1. Report it to the FTC at ReportFraud.ftc.gov.
2. Use strong passwords on your accounts, and turn on two-factor authentication where it is offered.
3. Keep your phone or computer up to date, and turn on automatic updates.""",
            ]),
            ex("f", "helper", "plain", [
                "My mother uses her phone on the library Wi-Fi to look at her accounts. She is 80 and not very careful. What should I tell her to do?",
                """You can tell her to do these things:

1. Look for a lock symbol or **https** to the left of the website address whenever she logs in. It works on a phone browser too.
2. Use strong passwords, and turn on two-factor authentication when it is available.
3. Update her phone's operating system, and turn on automatic updates.

Also tell her that scammers pretend to be well-known companies or the government, and they can build fake websites with a lock. If she is ever scammed, she can report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("g", "prevention", "plain", [
                "How can I tell if a website I land on over hotel Wi-Fi is a fake one trying to steal from me?",
                """A lock can help, but it cannot tell you a site is honest. Here is what to do:

1. Look for the lock symbol or **https** to the left of the website address. If it is missing, do not enter private information.
2. Remember that scammers make fake websites and encrypt them, so the lock appears on them too.
3. Be careful with anything that claims to come from a well-known company or the government.
4. Keep your device updated, use strong passwords, and use two-factor authentication.

If you find a scammer, report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
        ],
    },
    {
        "task_id": "TR-220",
        "task_type": "unordered_package_scam",
        "task": "A package arrives that the user never ordered",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Alert: Unexpected package you got could be a brushing scam (plus FTC: What to do if you're billed for things you never got or you get unordered products)", "url": "https://consumer.ftc.gov/consumer-alerts/2026/08/unexpected-package-you-got-could-be-brushing-scam"},
        "source_notes": """Alert page: You do not need to return an item you did not order, and do not have to pay for it; the law says you do not need to return things you did not order. Be cautious about using the product since you do not know who sent it.
Change passwords on all your online shopping accounts in case they were compromised.
If the package came from Amazon or another online marketplace, message the platform so it can investigate and remove the seller.
Check your credit weekly for free at AnnualCreditReport.com; monitor your credit report for signs of identity theft.
Report a brushing scam to the FTC at ReportFraud.ftc.gov.
Scammers want to create validation of delivery and use your name to post fake reviews ("brush up" sales), and steal personal information: a note with a QR code may lead to a phishing site that collects credit card numbers, usernames, or passwords.
Unordered products page: companies cannot send unordered merchandise then demand payment; you never have to pay; you can keep it as a free gift. If billed: contact your card issuer right away. Credit cards: dispute the charge in writing within 60 days of the first statement showing the error, sending it to the billing-disputes address, not the payment address. Debit cards: protections differ, you may not get a refund; call your bank as soon as possible, then follow up with a letter.""",
        "examples": [
            ex("a", "direct", "plain", [
                "A box came to my door today with my name on it, but I did not order anything. What do I do?",
                """You do not have to pay for it, and you do not have to send it back. The law says you do not need to return things you did not order.

1. Be careful about using what is inside, since you do not know who sent it.
2. Change the passwords on your online shopping accounts, in case someone got into them.
3. Check your credit for free at AnnualCreditReport.com, and look for signs of identity theft.
4. Report it to the FTC at ReportFraud.ftc.gov.

This may be a brushing scam, where a seller sends you items so they can post fake reviews in your name.""",
            ]),
            ex("c", "direct_messy", "verbose", [
                "I got a small box from an online marketplace seller I have never heard of. Inside was a cheap phone case, and I never bought it. I have bought other things on that marketplace before, so I am worried they have my account. I do not know who to tell about this.",
                """You do not have to pay for it or return it. Here is what to do:

1. Send a message to the marketplace so it can investigate and remove the seller.
2. Change the passwords on all your online shopping accounts, in case they were compromised.
3. Check your credit for free each week at AnnualCreditReport.com, and watch for signs of identity theft.
4. Report it to the FTC at ReportFraud.ftc.gov.

Scammers sometimes do this to get "validation" of a delivery, then use your name to post fake reviews.""",
            ]),
            ex("e", "constraint", "over_specified", [
                "A package came with a note inside that says to scan a QR code to claim a free gift card. I did not order the package. My neighbor says I have to send it back or I will be charged. I do not want to be rude. What should I do?",
                """Do not scan the QR code. A QR code in a package like this may lead to a fake website that collects credit card numbers, usernames, or passwords.

1. You do not have to return it or pay for it. The law says you do not need to return things you did not order.
2. Change the passwords on your online shopping accounts.
3. Check your credit for free each week at AnnualCreditReport.com.
4. Report the package to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("r", "already_acted", "failure_recovery", [
                "I got a package I never ordered, and now my credit card statement shows a charge for it. I paid my card bill already. What can I do?",
                """Contact your card issuer right away. You never have to pay for something you did not order.

1. If it is a credit card, dispute the charge in writing within 60 days of the first statement that shows it. Send the letter to the billing-disputes address, not the payment address.
2. If it is a debit card, call your bank as soon as possible, then follow up with a letter. Debit card protections are different, and you may not get a refund.
3. Change the passwords on your online shopping accounts.
4. Report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("f", "helper", "plain", [
                "My dad lives alone and keeps getting boxes he never ordered. Some have small items like earbuds. How do I help him handle this?",
                """Tell him he does not have to pay for the boxes or send them back. The law says people do not need to return things they did not order.

1. Ask him to be careful about using the items, since he does not know who sent them.
2. Help him change the passwords on his online shopping accounts.
3. If a box came from an online marketplace, message the marketplace so it can investigate and remove the seller.
4. Help him check his credit for free at AnnualCreditReport.com.
5. Report the boxes to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("g", "prevention", "plain", [
                "Why do people send random packages to strangers, and how do I protect myself from it?",
                """Scammers send these packages for two reasons. They want proof of a delivery so they can use your name to post fake reviews. They also want your personal information, and a note with a QR code may lead to a fake website that asks for card numbers, usernames, or passwords.

To protect yourself:

1. Do not pay for or return things you did not order.
2. Do not scan a QR code that came with one.
3. Change your shopping account passwords.
4. Check your credit weekly for free at AnnualCreditReport.com.
5. Report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
        ],
    },
    {
        "task_id": "TR-221",
        "task_type": "timeshare_resale_scam",
        "task": "A company promises to sell the user's timeshare for an upfront fee",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Timeshares, Vacation Clubs, and Related Scams", "url": "https://consumer.ftc.gov/articles/timeshares-vacation-clubs-and-related-scams"},
        "source_notes": """Signs of resale scams: ads promising quick sales ("The market is hot, so we'll sell your unit fast" is a lie); guarantees of a sale or big returns (anyone who guarantees a sale or big returns is a scammer); advance payment demands (better to use a reseller that is paid after the timeshare sells); unsolicited calls or messages offering to get you out of a timeshare or guarantees to cancel your contract; instructions to stop paying your mortgage or timeshare fees.
Before paying: 1 contact your timeshare developer or the resort's management company first and ask about options (ARDA tool at responsibleexit.com/property-search/). 2 check the reseller with the state attorney general (naag.org/our-work/center-for-consumer-protection/consumer-file-a-complaint/) and local consumer protection agencies (usa.gov/state-consumer); search the company name with complaint or scam. 3 ask about fees; if you must pay in advance, get the refund policy in writing. 4 confirm the agents are licensed to sell real estate where the timeshare is located, via that state's real estate licensing agency; ask for references. 5 ask how they will advertise and how often progress reports come. 6 get everything in writing; check the contract matches verbal promises, lists services, states all fees and due dates; do not sign if the deal is not what you wanted. 7 do not assume you will recover your purchase price; consider an appraisal from an appraiser licensed in the timeshare's state. 8 study paperwork on your own; ask for all promises in writing.
If you already paid: page gives no specific refund steps. Scammers may do nothing after taking payment or only contact the timeshare company for you, which you could do for free. Contact your timeshare company directly and review your contract for cancellation terms. State law or your contract may say how long a cooling-off period lasts; if within one, send a cancellation letter to the seller by certified mail and request a return receipt.
Report: FTC at ReportFraud.ftc.gov; state attorney general in the state where the timeshare is located; Better Business Bureau bbb.org/file-a-complaint. No phone numbers.""",
        "examples": [
            ex("a", "direct", "plain", [
                "A man called and said he has a buyer for my timeshare, but I have to pay him $1,800 first to start the sale. Is that normal?",
                """Do not pay him anything yet. Asking for money in advance is a sign of a resale scam, and the better kind of reseller is paid after the timeshare sells.

1. Contact your timeshare developer or the resort's management company first and ask about your options.
2. Search the company's name online with the word "complaint" or "scam."
3. Check the reseller with your state attorney general.
4. If you ever must pay in advance, get the refund policy in writing.

Anyone who guarantees a sale or big returns is a scammer.""",
            ]),
            ex("c", "direct_messy", "verbose", [
                "I got a nice letter in the mail from a company saying the timeshare market is hot right now and they can sell my week at the resort quickly. They want a fee to begin. We have not used the timeshare in years and the maintenance fees keep going up, so I am tempted. How can I tell if they are honest?",
                """Hold off on paying. Claims that the market is hot and that they will sell your unit fast are a lie told by resale scammers.

1. Ask your timeshare developer or the resort's management company about your options first.
2. Check the company with your state attorney general, and search its name with "complaint" or "scam."
3. Ask about all fees and when they are due. If you must pay in advance, get the refund policy in writing.
4. Ask how they will advertise the timeshare and how often they will send progress reports.
5. Get every promise in writing, and do not sign if the contract does not match what you were told.""",
            ]),
            ex("e", "constraint", "over_specified", [
                "The salesman says he has a buyer ready and the offer ends today, so I must send the fee by tonight. He also told me to stop paying my timeshare fees because the sale will take care of it. I cannot reach anyone at the resort until Monday. What should I do?",
                """Do not send the fee tonight. A rush and a promise of a sure sale are signs of a scam, and telling you to stop paying your timeshare fees is another one.

1. Do not stop paying your timeshare fees because he said so.
2. Wait until Monday and contact your timeshare developer or the resort's management company about your options.
3. Check the company with your state attorney general, and search its name with "complaint" or "scam."
4. Do not sign or pay until everything is in writing.""",
            ]),
            ex("r", "already_acted", "failure_recovery", [
                "I already paid a company $2,500 to sell my timeshare and now they do not answer my calls. What can I do?",
                """Stop sending money and contact your timeshare company directly. Some scammers do nothing after taking payment.

1. Look at your contract for cancellation terms. State law or your contract may allow a cooling-off period.
2. If you are inside a cooling-off period, send a cancellation letter to the seller by certified mail, and ask for a return receipt.
3. Report it to the FTC at ReportFraud.ftc.gov.
4. Report it to the attorney general in the state where the timeshare is located.
5. You can also file a complaint with the Better Business Bureau at bbb.org/file-a-complaint.""",
            ]),
            ex("f", "helper", "plain", [
                "My mother is 78 and a company keeps calling her saying they can get her out of her timeshare contract and cancel it for a fee. How can I help her?",
                """Tell her not to pay them. Unexpected calls that guarantee to cancel a contract are a sign of a scam.

1. Help her contact the timeshare developer or the resort's management company herself and ask about her options.
2. Check the caller's company with the state attorney general, and search its name with "complaint" or "scam."
3. Remind her not to stop paying her mortgage or timeshare fees if someone tells her to.
4. If she has already paid, report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("g", "prevention", "plain", [
                "If I decide to sell my timeshare someday, how do I pick a reseller without getting fooled?",
                """Do not pay anyone before you have checked them. Here is what to do:

1. Contact your timeshare developer or the resort's management company first about your options.
2. Check the reseller with your state attorney general, and search the name with "complaint" or "scam."
3. Ask about fees. If you must pay in advance, get the refund policy in writing.
4. Check that the agents are licensed to sell real estate where the timeshare is located, and ask for references.
5. Get everything in writing, and do not sign if the deal is not what you wanted.

Be wary of anyone who guarantees a sale.""",
            ]),
        ],
    },
    {
        "task_id": "TR-222",
        "task_type": "money_mule_scam",
        "task": "Someone asks the user to receive money and forward it",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Alert: Avoiding a Money Mule Scam", "url": "https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam"},
        "source_notes": """Scammers look for people to help move stolen money. They contact people through online dating, job search, and social media sites, using made-up stories and reasons to send money, usually by check or Bitcoin. They then tell the person to forward that money to someone else using gift cards or wire transfers. They do not say the money is stolen.
Helping move stolen money is a crime even if you did not know it was stolen; you might be acting as what law enforcement calls a money mule.
Financial risk: a deposited check may clear at first, but when found to be fake the bank can require you to repay the full amount; fees, overdrawn or closed account. Gift card PINs and wire transfers are almost like sending cash and the money is nearly impossible to recover.
Advice: Do not forward money for an online romantic interest who sends you money. Do not accept a job that asks you to transfer money. Do not accept a grant or prize award and forward some of the money.
If asked or already did it: stop the payment transaction and stop communicating with the person. Tell your bank, the wire transfer service, or any gift card companies right away. If the scammer has your bank account information, close your account immediately.
Report to the FTC at ReportFraud.ftc.gov. No phone numbers.""",
        "examples": [
            ex("a", "direct", "plain", [
                "A man I met on a dating site mailed me a check and wants me to deposit it and then send most of it to his friend. Should I do it?",
                """No, do not deposit it or send anything on. This is a known scam, and you could be acting as what law enforcement calls a money mule, which can be a crime even if you did not know the money was stolen.

1. Do not forward money for someone you met online who sends you money.
2. Stop communicating with him.
3. Report it to the FTC at ReportFraud.ftc.gov.

A check can seem to clear at first. When the bank finds it is fake, you may have to repay the full amount and could face fees or a closed account.""",
            ]),
            ex("c", "direct_messy", "verbose", [
                "I applied for a work from home job and they hired me right away. My job is to receive payments into my own bank account and then send the money on to their clients using gift cards or a wire. They said I keep a small part as pay. It sounds easy but it also sounds odd. Is this a real job?",
                """Do not take this job and do not move any money. Scammers use jobs like this to get people to move stolen money, and you can be called a money mule even if you did not know.

1. Do not accept a job that asks you to transfer money.
2. Stop communicating with the person.
3. Report it to the FTC at ReportFraud.ftc.gov.

Sending money by gift card PINs or wire transfer is almost like sending cash, and it is nearly impossible to get back.""",
            ]),
            ex("e", "constraint", "over_specified", [
                "A friend I have only talked to online sent me money by Bitcoin and said I must forward it to his cousin in another country by wire transfer today. He said not to tell my bank because they will cause trouble. I cannot reach him by phone, only messages. What should I do?",
                """Do not forward the money. Telling you to keep your bank out of it is a warning sign, because the money may be stolen.

1. Stop the payment and stop communicating with this person.
2. Tell your bank right away, and the wire transfer service if you have started one.
3. If the person has your bank account information, close your account right away.
4. Report it to the FTC at ReportFraud.ftc.gov.

Helping move stolen money can be a crime even if you did not know it was stolen.""",
            ]),
            ex("r", "already_acted", "failure_recovery", [
                "I deposited a check from someone I met online and sent most of it to a person he named, using gift cards. Now the bank says the check was fake. What do I do?",
                """Stop any more payments and stop communicating with that person. Then act quickly:

1. Tell your bank, and the gift card companies, right away.
2. If the person has your bank account information, close your account immediately.
3. Report it to the FTC at ReportFraud.ftc.gov.

The bank may require you to repay the full amount of the fake check. Gift card PIN codes are almost like sending cash, so that money is very hard to get back.""",
            ]),
            ex("f", "helper", "plain", [
                "my uncle is 82 and some woman he talks to online keeps sending him money and asking him to pass it on to someone. he thinks she loves him. how do i get him to stop?",
                """Ask him not to send anything on. Scammers use made-up stories to get people to move stolen money, and he could be acting as a money mule without knowing it.

1. Tell him not to forward money for an online romantic interest who sends him money.
2. Help him stop the payment and stop communicating with her.
3. Help him tell his bank, the wire transfer service, or any gift card company right away.
4. If she has his bank account information, help him close the account.
5. Report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("g", "prevention", "plain", [
                "What are the rules I should follow so I never get tricked into moving money for someone?",
                """Here are three simple rules:

1. Do not forward money for an online romantic interest who sends you money.
2. Do not accept a job that asks you to transfer money.
3. Do not accept a grant or prize award and then forward some of the money.

Scammers find people on online dating, job search, and social media sites. If you are asked to do any of this, stop communicating with the person, and tell your bank. You can report it to the FTC at ReportFraud.ftc.gov.""",
            ]),
        ],
    },
    {
        "task_id": "TR-223",
        "task_type": "rental_listing_scam",
        "task": "A rental listing asks for a deposit before any viewing",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Rental Listing Scams", "url": "https://consumer.ftc.gov/articles/rental-listing-scams"},
        "source_notes": """Signs: scammers copy pictures, description, or virtual tour from a real listing; surprisingly low rent or amazing amenities; owner says they are out of the country or gives another reason to skip a viewing; pressure to decide quickly; demands for wire transfer (Western Union, MoneyGram), gift cards, or cryptocurrency; asking early for Social Security number, driver's license photo, paystubs, or credit score screenshots before you agree to rent; home listed for sale instead of rent; other ads for same address show a different owner or company.
What to do: 1 search the rental address plus owner or company name; other ads with a different owner is a warning sign; check the rental company's own website. 2 if anyone pressures you to decide quickly, walk away. 3 search the owner or company name with complaint, review, or scam. 4 compare rent to typical prices in the area. 5 look at the property before you sign or pay, in person or by video or virtual tour; in-person visits: ask the agent for a business card from the owning or managing company and check the agent's ID; private landlords: use city or county tax assessment websites to confirm ownership, then check landlord's ID; vacation rentals: get a copy of the contract before sending any deposit, confirm the address exists, for resort properties call the front desk. 6 never give personal or financial information to someone who says they work with the owner; contact the owner or company using information you already have. 7 landlords do not need your SSN or credit score before you agree to rent; most pull credit themselves. 8 treat any demand for wire transfer, gift card, or crypto as a scam signal.
If already paid: no specific section; wire transfers, gift cards, and crypto are like sending cash and once sent you probably cannot get the money back. Use reporting.
Report: local law enforcement; the website where the ad was posted; FTC at ReportFraud.ftc.gov; state attorney general. No phone numbers.""",
        "examples": [
            ex("a", "direct", "plain", [
                "I found an apartment online with really low rent. The owner says I need to send a deposit first and then he will send the keys. I have not seen the place. Is that okay?",
                """Do not send the deposit. Look at the place first, either in person or by video or virtual tour, before you sign or pay anything.

1. Search the address along with the owner's name. If other ads for it show a different owner, that is a warning sign.
2. Compare the rent to typical prices in your area. A much lower price can signal a scam.
3. Search the owner's name with the word "complaint," "review," or "scam."

If someone pressures you to decide fast, walk away.""",
            ]),
            ex("c", "direct_messy", "verbose", [
                "I am moving to be closer to my grandchildren and I found a cute house for rent on a website. The owner wrote that he is out of the country on a mission trip, so he cannot show it, but his agent will take my deposit through gift cards and mail the keys. The photos look lovely. I am so excited but my son is worried.",
                """Your son is right to be careful. Do not pay, and do not send gift cards. Any demand for a wire transfer, gift cards, or cryptocurrency is a scam signal, and an owner who cannot show the place is another.

1. Do not give personal or financial information to someone who says they work with the owner.
2. See the house before you sign or pay, in person or by video or virtual tour.
3. Search the address and the owner's name to see if other ads show a different owner.
4. Report the listing to the website where you found it.""",
            ]),
            ex("e", "constraint", "over_specified", [
                "The landlord says three other people want the same apartment so I need to wire the deposit today and send my Social Security number and a photo of my driver's license to hold it. I am in another state and cannot go see it. What should I do?",
                """Do not wire any money and do not send your Social Security number or license photo. Pressure to decide fast and a wire transfer demand are both scam signs, so walk away unless it checks out.

1. Landlords do not need your Social Security number or credit score before you agree to rent.
2. Ask to see the property by video or a virtual tour before you sign or pay.
3. Search the address with the owner's name, and check whether other ads show a different owner.
4. Search the owner's name with "complaint" or "scam."""",
            ]),
            ex("r", "already_acted", "failure_recovery", [
                "I already wired a $1,200 deposit for a rental and now the owner stopped answering. What can I do?",
                """Stop sending money and do not share any more personal information. Wire transfers, gift cards, and cryptocurrency are like sending cash, and once the money is sent you probably cannot get it back. You can still report it:

1. Report it to your local law enforcement agency.
2. Report it to the website where the ad was posted.
3. Report it to the FTC at ReportFraud.ftc.gov.
4. Report it to your state attorney general.""",
            ]),
            ex("f", "helper", "plain", [
                "My granddaughter is looking for an apartment and found one online that wants a deposit before she can see it. She wants me to help her check if it is real. What do we do?",
                """Tell her not to pay the deposit yet. Here is what you can both do:

1. Search the rental address along with the owner or company name. Other ads showing a different owner is a warning sign.
2. Check the rental company's own website for the property.
3. Search the owner or company name with "complaint," "review," or "scam."
4. Compare the rent to typical prices in the area.
5. Have her see the place before she signs or pays, in person or by video or virtual tour.""",
            ]),
            ex("g", "prevention", "plain", [
                "What are the warning signs of a fake rental ad, and where can I report one?",
                """Be wary if you see any of these:

1. A surprisingly low rent or amazing amenities.
2. An owner who says he is out of the country or gives another reason not to show the place.
3. Pressure to decide quickly.
4. A request for a wire transfer, gift cards, or cryptocurrency.
5. A request for your Social Security number or credit score before you agree to rent.

To report a fake ad, tell your local law enforcement, the website where it was posted, the FTC at ReportFraud.ftc.gov, and your state attorney general.""",
            ]),
        ],
    },
    {
        "task_id": "TR-224",
        "task_type": "mortgage_relief_scam",
        "task": "A company promises to stop foreclosure for an upfront fee",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Mortgage Relief Scams", "url": "https://consumer.ftc.gov/articles/mortgage-relief-scams"},
        "source_notes": """Signs: scammers demand payment upfront before any services; want payment only by cashier's check, wire transfer, or mobile payment app; ask you to transfer your home's deed (if you transfer the deed you are not likely to get it back); tell you to stop contacting your lender, lawyer, housing counselor, or credit counselor; claim to be housing counselors, lawyers, auditors, or government representatives; promise a forensic loan audit will get a modification; rent-to-buy deals, cash offers, or rescue loans that hide a deed transfer; push to sign loan papers quickly.
What to do instead: do not pay any money until the company delivers the results you want. Contact your servicer or lender immediately, even if foreclosure has started; you can always contact your lender directly. Find a free certified housing counselor through HUD's list of approved agencies (apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm). Visit makinghomeaffordable.gov or call 1-888-995-HOPE (4673). Visit the Homeowner Preservation Foundation at 995hope.org. If you hire a lawyer confirm they are licensed in your state, check with state bar, get name, licensing states, license numbers, cost and payment schedule in writing, keep a file of communications. Be wary of mass joinder lawsuit mailers charging upfront fees.
Legal protections: companies cannot charge until they give you a written loan modification or relief offer from your lender that you accept. Ads and telemarketing must state the company is not affiliated with the government and your lender may not agree to change your loan.
If already paid: act as soon as possible, the sooner the better chance of recovering money; learn how to try to get money back at consumer.ftc.gov/articles/what-do-if-you-were-scammed (Paid section).
Report: FTC at ReportFraud.ftc.gov; state attorney general.""",
        "examples": [
            ex("a", "direct", "plain", [
                "A company called and said they can stop my house from going into foreclosure if I pay them $1,500 right now. I am behind on my mortgage. Is this real?",
                """Do not pay them. Companies that ask for payment upfront before they do anything are a sign of a mortgage relief scam. Don't pay any money until a company delivers the results you want.

1. Contact your servicer or lender right away to ask about your options.
2. Find a free, certified housing counselor through HUD's list of approved agencies.
3. You can also call 1-888-995-HOPE (4673), the Making Home Affordable help line.

Report the call to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("c", "direct_messy", "verbose", [
                "I got a very official looking letter from a group calling themselves housing counselors. They say they work with the government and can get my loan changed, but they want a fee first and told me to stop talking to my bank because it will only hurt my case. I have been sick and fell behind on payments, and I am scared of losing the house.",
                """Do not pay them and do not stop talking to your lender. Telling you to stop contacting your lender and asking for a fee first are signs of a scam.

1. Contact your servicer or lender right away. You can always do this directly, even if foreclosure has started.
2. Find a free, certified housing counselor through HUD's list of approved agencies.
3. You can also call 1-888-995-HOPE (4673), or visit makinghomeaffordable.gov.
4. Report the letter to the FTC at ReportFraud.ftc.gov.""",
            ]),
            ex("e", "constraint", "over_specified", [
                "They said foreclosure has already started so it is too late to call my bank, and I need to sign my deed over to them today to save the house. They said it will be returned later. I do not have time to check anything. What should I do?",
                """Do not sign over your deed and do not pay anything. If you transfer the deed, you are not likely to get it back.

1. Contact your servicer or lender right away. You can do this even if foreclosure has started.
2. Find a free, certified housing counselor through HUD's list of approved agencies.
3. Or call 1-888-995-HOPE (4673).
4. Report them to the FTC at ReportFraud.ftc.gov.

Pressure to sign quickly is a common scam sign.""",
            ]),
            ex("r", "already_acted", "failure_recovery", [
                "I already paid a company $2,000 by wire to stop my foreclosure and they have done nothing. What now?",
                """Act as soon as you can, because the sooner you act, the better the chance of getting money back. Do not send any more money.

1. Read the FTC's advice on what to do if you were scammed and paid, and follow the steps to try to get your money back.
2. Contact your servicer or lender right away about your options.
3. Report it to the FTC at ReportFraud.ftc.gov.
4. Report it to your state attorney general.""",
            ]),
            ex("f", "helper", "plain", [
                "My brother is behind on his mortgage and a company wants a big fee to negotiate with the bank for him. Should he pay?",
                """He should not pay. Do not pay any money until a company delivers the results you want, and companies cannot charge until your lender gives a written offer that you accept.

1. Have him contact his servicer or lender right away to ask about options.
2. Help him find a free certified housing counselor on HUD's list of approved agencies.
3. He can also call 1-888-995-HOPE (4673).
4. If he hires a lawyer, check that the lawyer is licensed in his state, and get the cost in writing.""",
            ]),
            ex("g", "prevention", "plain", [
                "What are the warning signs of a mortgage relief scam, and who can I trust for real help?",
                """Be wary of anyone who:

1. Demands payment upfront, or wants cashier's check, wire transfer, or mobile payment app.
2. Tells you to stop contacting your lender or housing counselor.
3. Asks you to transfer your deed.
4. Pushes you to sign loan papers fast.

For real help, contact your servicer or lender, find a free certified housing counselor on HUD's list of approved agencies, or call 1-888-995-HOPE (4673). Report scams to the FTC at ReportFraud.ftc.gov.""",
            ]),
        ],
    },
]
