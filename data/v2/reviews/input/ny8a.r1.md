# Review input: batch ny8a, round 1 (42 examples)

## tr212-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Someone sends a check and asks the user to send part of the money back (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/fakechecks

**USER:**
I sold my old camera online and the buyer mailed me a check for more than the price. He wants me to send him back the extra. Is that okay?

**ASSISTANT:**
Please do not send him anything. This is a common trick: the extra money is the bait, and the check is likely fake.

1. Do not accept a check for more than the selling price.
2. Do not send back the difference, by any method.
3. Fake checks can look real, even to bank workers, and it can take weeks for a bank to find the fraud.
4. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

If the check was already deposited, remember that seeing the money in your account does not mean the check is good. If it is fake, you may have to repay the bank.

## tr212-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Someone sends a check and asks the user to send part of the money back (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/fakechecks

**USER:**
I got an email saying I was picked to be a mystery shopper for a money transfer store. They mailed me a big check and told me to deposit it, keep a little for myself, and wire the rest to a man they named. I went to the bank and the teller said the money is already showing in my account. I really need the extra money right now. Should I wire it?

**ASSISTANT:**
No, please do not wire any of it. Wiring money from a check to someone who asks is a classic fake check scam.

1. Never use money from a check to wire money to anyone who asks.
2. Do not rely on money from a check unless you know and trust the person who sent it.
3. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

Banks must make deposited funds available quickly, so seeing the money in your account does not mean the check is good. If it turns out to be fake, you may have to repay the bank.

## tr212-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Someone sends a check and asks the user to send part of the money back (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/fakechecks

**USER:**
The check I deposited cleared and the bank website shows the full amount as available, so it must be real. The sender keeps texting that I need to send back the extra today, and that I shouldn't bother anyone at the bank about it. Can I just send it?

**ASSISTANT:**
No, please do not send it. Money showing as available does not make the check good.

1. Banks must make deposited funds available quickly by law, even when the check is fake.
2. It can take weeks for a bank to find the fraud, and then you may have to repay the bank.
3. Do not send any of the money back, no matter how urgent the texts sound.
4. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

If you want to know more about the check, you do not need anyone's permission to report it.

## tr212-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Someone sends a check and asks the user to send part of the money back (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/fakechecks

**USER:**
A man mailed me a check and said to deposit it and buy gift cards with the money for his company. I already bought the cards and sent him the numbers on the back. Now my bank says the check was fake. What do I do?

**ASSISTANT:**
I am sorry, this happens to many people. Act quickly on the gift cards.

1. Contact the company that issued each gift card right away.
2. Tell them the card was used in a scam and ask for a refund.
3. Tell the store where you bought the cards.
4. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

Because the check was fake, you may have to repay the bank, so it is worth telling them what happened.

## tr212-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: Someone sends a check and asks the user to send part of the money back (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/fakechecks

**USER:**
My grandfather got a check in the mail from a company that wants to put an ad wrap on his car. They told him to deposit it and then pay the installers out of it. He is excited. What should I tell him?

**ASSISTANT:**
Tell him not to pay anyone from that check. This is a known fake check scam called car wrap decals.

1. Ask him not to deposit and spend money, or send any to the installers.
2. Explain that fake checks often look real, even to bank workers.
3. Remind him that a bank can find the fraud weeks later, and then he may have to repay it.
4. Help him report it to the Federal Trade Commission at reportfraud.ftc.gov.

If he already sent money, tell me how and I can help with the next step.

## tr212-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Someone sends a check and asks the user to send part of the money back (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/fakechecks

**USER:**
How can I spot a fake check scam before I fall for one, and where do I report it?

**ASSISTANT:**
Here are the warning signs and the rules to follow.

1. Be wary if you are asked to wire money, buy gift cards, or buy cryptocurrency. Gift cards are for gifts, not payments.
2. Be wary if a check is for more than the selling price, or you are asked to pay fees to get a prize.
3. Never use money from a check to buy gift cards or money orders, buy cryptocurrency, or wire money.
4. Do not rely on money from a check unless you know and trust the person.

To report one, go to the Federal Trade Commission at reportfraud.ftc.gov, the U.S. Postal Inspection Service at uspis.gov/report, or your state Attorney General.

## tr213-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
A man knocked on my door and said he was in the area and noticed my roof needs work. He wants to start today and says the price is good only right now. Should I say yes?

**ASSISTANT:**
Please do not agree today. Being "in the area" and pushing you to decide right now are both signs of a home improvement scam.

1. Tell him you will think about it, and do not pay anything.
2. Hire only a licensed and insured contractor. Confirm the license with your state or county, and ask for proof of insurance.
3. Ask people you know and trust for recommendations.
4. Get more than one written estimate before you choose.

A real contractor can wait for you to check.

## tr213-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
Two men came by saying they had leftover paving materials from a job down the street and could do my driveway cheap. They want all the money up front, in cash, and they said I should go get the building permit from the city myself. My husband is at work so I can't ask him. It sounds like a good deal but something feels off.

**ASSISTANT:**
Your feeling is right. Please do not pay them anything today.

1. Do not pay the full cost up front. Never make the final payment until the work is finished and you are satisfied.
2. Be careful of anyone who accepts only cash, or who asks you to get the building permits yourself.
3. Leftover materials from a previous job is another sign of this scam.
4. Wait and talk it over with your husband. A real contractor will give you a written estimate you can compare with others.

If they keep pressuring you, that is another warning sign.

## tr213-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
The contractor at my door says the repair price is only good if I sign today, and he offered to set me up with a lender he knows so I don't have to pay now. I don't have the savings. He's standing on my porch waiting. What do I do?

**ASSISTANT:**
Do not sign anything today. Pushing for an immediate decision and offering a lender he knows are both signs of a scam.

1. Tell him you will not sign today, and close the door.
2. Do not sign anything you have not read, do not understand, or that has blank spaces.
3. If you need a loan, shop around and compare loan terms before accepting financing from a contractor.
4. Make sure you can afford the payments.
5. Do not let anyone pressure you into signing.

Never transfer your deed to anyone without first talking to an attorney or someone you trust.

## tr213-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
I already signed a contract at my kitchen table with a door to door contractor and gave him a deposit. Now I think he was pushy and I'm worried. What can I do?

**ASSISTANT:**
You still have steps you can take.

1. Look in your contract for a written statement of your right to cancel within three business days. A contract signed in your home should include one.
2. Try to settle the problem with the contractor directly.
3. Follow up any phone call with a letter by certified mail, and ask for a return receipt.
4. Keep notes and copies of all letters and documents.
5. If it is not settled, contact your state attorney general or local consumer protection office.

Do not pay anything more until the work is finished and you are satisfied.

## tr213-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
My elderly neighbor says a contractor keeps coming to her door pushing to fix her gutters, and wants half the money first. I want to help her without scaring her. What should I tell her?

**ASSISTANT:**
Here is what to share with her, kindly and simply.

1. She does not have to decide right away. Pressure for an immediate decision is a sign of a scam.
2. Do not pay the full cost up front, and never make the final payment until the work is finished and she is satisfied.
3. Use only a licensed and insured contractor. Help her confirm the license with the state or county, and ask for proof of insurance.
4. Get recommendations from people she knows and trusts, and more than one written estimate.

If something goes wrong, her state attorney general or local consumer protection office can help.

## tr213-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
How do I make sure a contractor is honest before I hire anyone to work on my house?

**ASSISTANT:**
Take these steps before you agree to anything.

1. Use only licensed and insured contractors. Confirm the license with your state or county and ask for proof of insurance.
2. Ask people you know and trust for recommendations.
3. Check with your local Home Builders Association and consumer protection officials for complaints. Search the company name with "scam," "review," or "complaint."
4. Get several written estimates. Do not automatically pick the lowest one.
5. Read the contract carefully. It should show the contractor's name, address, phone, license number, and start and finish dates. Write in any spoken promises and fill in all blank spaces.

Do not pay everything up front.

## tr214-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
Someone called and said I owe money on an old account and have to pay today. I have never heard of this debt. What should I do?

**ASSISTANT:**
Do not pay and do not share any personal or financial information on that call. First get proof that the debt is real.

1. Ask the caller to send you a written validation notice. The collector must provide it when it first contacts you or within five days after.
2. When it arrives, check the collector's name and address, the original creditor, and the amount owed.
3. If you do not owe it, send a dispute letter within 30 days. Say you do not owe the money and ask for verification of the debt.
4. Send the letter by certified mail with a return receipt, and keep a copy.

Once the collector gets your dispute, it must stop trying to collect until it sends written verification.

## tr214-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
A man keeps calling me at 7 in the morning and again at night, six times this week, about some credit card I don't have. He says if I don't pay he will have me arrested. I'm scared. I don't know whose debt this is and I don't want to just pay to make it stop. What are my rights?

**ASSISTANT:**
You do not have to pay, and a collector is not allowed to treat you this way.

1. Collectors cannot threaten arrest or legal action they will not take, and cannot call before 8 a.m. or after 9 p.m. unless you agree.
2. They also cannot harass you or call more than seven times in seven days.
3. Do not share personal or financial information until you get validation information in writing.
4. Send a letter within 30 days of getting it saying you do not owe the money, by certified mail with a return receipt.
5. Report the calls to the FTC at reportfraud.ftc.gov or the CFPB at cfpb.gov/complaint.

## tr214-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
A caller says they are suing me today unless I give my debit card number right now to settle a debt. I don't recognize it and I can't reach anyone I trust to ask. He says it's my last chance. Should I give the number?

**ASSISTANT:**
No. Do not give your card number or any other information, and end the call.

1. Collectors cannot threaten legal action they will not take, or lie about the amount you owe.
2. Do not share personal or financial information until you have validation information in writing.
3. Ask for the written validation notice, which must arrive when they first contact you or within five days after.
4. Within 30 days of getting it, send a letter by certified mail with a return receipt. Say you do not owe the money and ask for verification of the debt.

Keep a copy of everything.

## tr214-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
I stayed on the phone with a debt collector and told him my birth date and address before I realized I don't recognize this debt at all. What now?

**ASSISTANT:**
Do not give them anything more, and do not pay yet.

1. Ask for a written validation notice. It lists the collector's name and address, the original creditor, and the amount owed.
2. Within 30 days of getting it, send a dispute letter saying you do not owe the money and asking for verification of the debt. Use certified mail with a return receipt, and keep a copy.
3. If you want the calls to end, send a letter asking the collector to stop contacting you.
4. Report the collector to the FTC at reportfraud.ftc.gov.

Once they receive your dispute, they must stop collecting until they send written verification.

## tr214-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
A debt collector called my mother's friend and also called her daughter and talked about the debt. The friend says she doesn't owe it. How can I help her?

**ASSISTANT:**
Help her avoid paying until the debt is proven, and know that a collector may not discuss her debt with her daughter.

1. A collector cannot discuss a debt with anyone other than her or her spouse.
2. Help her ask for a written validation notice.
3. Within 30 days of getting it, help her send a dispute letter by certified mail with a return receipt, saying she does not owe the money and asking for verification. Keep a copy.
4. Report the collector to the FTC at reportfraud.ftc.gov, the CFPB at cfpb.gov/complaint, or her state attorney general.

She should not share personal information until the validation notice arrives.

## tr214-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
What can a debt collector not do, and where do I report one who breaks the rules?

**ASSISTANT:**
Here is what a collector cannot do.

1. Harass or threaten you, or use obscene or profane language.
2. Call more than seven times in seven days, or contact you before 8 a.m. or after 9 p.m. unless you agree.
3. Lie about the amount owed, pretend to be an attorney or a government representative, or threaten arrest or legal action they will not take.
4. Reveal your debt publicly, or discuss it with anyone other than you or your spouse.

To report one, go to the FTC at reportfraud.ftc.gov, the CFPB at cfpb.gov/complaint, or your state attorney general's office.

## tr215-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

**USER:**
I got a text saying I owe an unpaid toll and need to pay with a link. Is this real?

**ASSISTANT:**
It is probably a scam. Do not tap the link or reply to the text.

1. Look up your state's tolling agency yourself and contact it with a phone number or website you know is real, not the one in the text.
2. Ask the agency whether you really owe anything.
3. Report the text with your phone's "report junk" option, or forward it to 7726 (SPAM).
4. Once you have checked it and reported it, delete the text.

Scammers want you to hurry, so it is best to stop and check.

## tr215-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

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

## tr215-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

**USER:**
I don't have the number for my state toll agency and I don't want to look anything up. The text has a link that says I can just pay quickly there. Can I tap it just this once, since I did drive on a toll road?

**ASSISTANT:**
I would not tap it, even once. Driving on a toll road does not make the text real.

1. Do not click links in unexpected texts or respond to them.
2. Find your state's tolling agency yourself, with a phone number or website you know is real, not the one in the text. A quick search on your phone is fine.
3. Ask the agency whether you owe a toll.
4. Report the text with "report junk," or forward it to 7726 (SPAM), then delete it.

Taking a minute to check is better than reacting quickly.

## tr215-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

**USER:**
I tapped the link in that unpaid toll text and a page opened, but I closed it before typing anything. What should I do now?

**ASSISTANT:**
Good that you closed it. Do not respond to the text or go back to the link.

1. Contact your state's tolling agency using a phone number or website you know is real, not the one in the text.
2. Ask whether you owe any toll.
3. Report the text with your phone's "report junk" option, or forward it to 7726 (SPAM).
4. Delete the text once you have checked and reported it.

You can learn more about spotting text scams at ftc.gov/textscams.

## tr215-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

**USER:**
My mom just showed me a text saying she owes a toll and there is a link. She is about to tap it. What should I tell her?

**ASSISTANT:**
Tell her to stop and not tap the link or reply. It is probably a scam.

1. Explain that scammers want people to react quickly.
2. Together, contact the state's tolling agency using a phone number or website you know is real, not the info in the text.
3. Report the text with the "report junk" option, or forward it to 7726 (SPAM).
4. Then delete the text.

If the real agency says she owes a toll, she can handle it with them.

## tr215-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

**USER:**
How do I handle these toll texts in the future, and where do I report them?

**ASSISTANT:**
Handle any unexpected text the same way each time.

1. Do not click any links in unexpected texts, and do not respond.
2. If you wonder whether it is real, contact the state's tolling agency using a phone number or website you know is real, not the info in the text.
3. Report the text with your phone's "report junk" option, or forward it to 7726 (SPAM).
4. Delete the text after you have checked and reported it.

For more on spotting text scams, see ftc.gov/textscams.

## tr216-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362

**USER:**
A man called saying he is from the IRS and that I owe money and must pay today. Is this real?

**ASSISTANT:**
Hang up. Do not give him any personal or financial information, and do not pay.

1. Do not send money by wire transfer, prepaid card, or gift card to someone claiming to be from the IRS.
2. If you are in doubt, call the IRS directly at 1-800-829-1040.
3. Report the call to the Treasury Inspector General for Tax Administration at tigta.gov.
4. Also report it to the FTC at ftc.gov/complaint.

The IRS will not require a specific type of payment.

## tr216-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362

**USER:**
There was a voicemail on my phone from someone who says they are with the Internal Revenue Service. The recording was very serious and says I have a problem with my taxes and to call back and arrange payment with gift cards. I am retired and nervous about anything with the IRS. I don't know if I should call the number.

**ASSISTANT:**
Please do not call that number back or pay anything. This is a message from someone pretending to be the IRS.

1. Do not give personal or financial information to anyone claiming to be from the IRS.
2. Never pay by wire transfer, prepaid card, or gift card. The IRS will not require a specific type of payment.
3. If you are in doubt, call the IRS directly at 1-800-829-1040.
4. Report it to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

It is normal to feel nervous, but you did the right thing by asking.

## tr216-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362

**USER:**
The caller knew my full name and address and said police would come to my door today if I hang up without paying. He said not to tell my family. I don't want trouble. What should I do?

**ASSISTANT:**
Hang up. You can end the call and you do not have to keep it secret.

1. Do not give personal or financial information to someone claiming to be from the IRS.
2. Do not pay by wire transfer, prepaid card, or gift card.
3. If you are in doubt, call the IRS directly at 1-800-829-1040.
4. Report the call to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

Please tell your family. Letting friends and family know about IRS imposters helps keep everyone safe.

## tr216-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362

**USER:**
A person claiming to be from the IRS called, and I gave them my Social Security number and bank name before I got suspicious. What do I do now?

**ASSISTANT:**
Stop talking to them and do not give anything more.

1. Hang up if they call again. Do not give more personal or financial information.
2. Do not send money by wire transfer, prepaid card, or gift card.
3. If you are in doubt, call the IRS directly at 1-800-829-1040.
4. Report the call to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

For more on stopping imposter scams, visit ftc.gov/imposters.

## tr216-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362

**USER:**
My brother got a message from someone saying they are from the IRS and he must pay right away. He's worried. How can I help him?

**ASSISTANT:**
Tell him not to respond or pay. It is likely an imposter.

1. Remind him not to give personal or financial information to someone claiming to be from the IRS.
2. Tell him never to pay by wire transfer, prepaid card, or gift card.
3. If either of you is in doubt, call the IRS directly at 1-800-829-1040.
4. Help him report it to TIGTA at tigta.gov and to the FTC at ftc.gov/complaint.

Share this with other family members too, so no one else is caught off guard.

## tr216-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362

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

## tr217-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024

**USER:**
A man called and said he is a U.S. Marshal and I missed jury duty, so I have to pay a fine or I will be arrested. Is that real?

**ASSISTANT:**
Hang up. Do not give him any of the information he asks for. A federal court will never threaten you or demand immediate payment.

1. Hang up and contact your local court clerk's office or U.S. Marshals Service office.
2. Find the court's contact information at uscourts.gov/court-locator.
3. Notify the Clerk of Court's office of the U.S. District Court in your area about the call.

Jurors who miss jury duty are usually contacted by the court Clerk's Office, and any fine is imposed by a judge in open court.

## tr217-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024

**USER:**
I got a voicemail from a woman who said she is with the federal court. She said I failed to appear for jury service, gave me a hearing time and my name, and left a number to call back right away to settle a fine. I never got a jury summons that I remember. I don't know what to do and I'm shaking.

**ASSISTANT:**
Take a breath. Please do not call that number back or share any information. A federal court will never threaten you or demand immediate payment.

1. Step away from the message so you can think calmly. Scammers use fear to cloud judgment.
2. Contact your local court clerk's office or U.S. Marshals Service office yourself. Find court contact information at uscourts.gov/court-locator.
3. Tell the Clerk of Court's office of the U.S. District Court in your area about the message.

Scammers use names and hearing times to seem real, so those details do not prove anything.

## tr217-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024

**USER:**
The caller knows my name and gave a court time and says if I hang up I'll be arrested. He wants payment by wire transfer today. I can't reach anyone at the court right now because the line he gave me is the only number I have. What should I do?

**ASSISTANT:**
Hang up anyway. A federal court will never threaten you or demand immediate payment, by phone or by wire transfer.

1. Do not send money or give him the information he wants.
2. Find your local court's real contact information at uscourts.gov/court-locator.
3. Contact your local court clerk's office or U.S. Marshals Service office.
4. Tell the Clerk of Court's office of the U.S. District Court in your area.

Knowing your name and a hearing time is how scammers seem credible. A judge, not a caller, decides any fine.

## tr217-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024

**USER:**
I already wired money to a man who said I missed jury duty. Now I think it was a scam. What do I do?

**ASSISTANT:**
I am sorry. Please act right away.

1. Contact your local court clerk's office or U.S. Marshals Service office right away and tell them what happened.
2. Find the court's contact information at uscourts.gov/court-locator.
3. Notify the Clerk of Court's office of the U.S. District Court in your area.
4. If he calls again, hang up and do not give him any information.

A federal court will never demand immediate payment by telephone or money wire service.

## tr217-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024

**USER:**
My husband got a call saying he missed jury duty and owes a fine, and he is panicking. How do I help him?

**ASSISTANT:**
Help him stay calm and not pay anything. A federal court will never threaten anyone or demand immediate payment.

1. Have him hang up and not give the caller any information.
2. Together, contact your local court clerk's office or U.S. Marshals Service office. Find it at uscourts.gov/court-locator.
3. Notify the Clerk of Court's office of the U.S. District Court in your area about the call.

Remind him that jurors who miss jury duty are usually contacted by the court Clerk's Office, and a judge imposes any fine in open court.

## tr217-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024

**USER:**
How does a real court handle someone who misses jury duty, so I can tell a fake call?

**ASSISTANT:**
Here is how the real process goes, and how to spot a fake call.

1. Jurors who miss jury duty are typically contacted by the court Clerk's Office.
2. Any fine is imposed by a judge in open court, and the juror can explain before it is imposed.
3. A federal court will never threaten you or demand immediate payment by phone or money wire service.
4. If someone calls like that, hang up and contact your local court clerk's office or U.S. Marshals Service office.
5. Report it to the Clerk of Court's office of the U.S. District Court in your area. Find it at uscourts.gov/court-locator.

## tr218-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
I got an email saying the sender hacked my computer and recorded me on adult websites. They will send the video to my family unless I pay in Bitcoin. What do I do?

**ASSISTANT:**
Do not pay anything. This is a scam, and the claims are all talk.

1. Do not pay, and do not reply.
2. Delete the message.
3. Report it to the FTC at ReportFraud.ftc.gov.

Scammers claim they have a video of you or access to your computer or webcam, but that is just a threat to scare you.

## tr218-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
Something terrible came in my email today. It had a password I used to use years ago right in the first line, and said they have my webcam and a video of me. I haven't done anything wrong but now I am frightened they actually have access to my computer. They want money in Bitcoin by tonight. How would they know my password?

**ASSISTANT:**
Please do not pay. This is a scam, and it is understandable to be frightened.

1. They may really know one of your old or recent passwords. They may have gotten your email from a data breach, which is likely why it appeared in the message.
2. Their claims about your webcam and computer are all talk.
3. Change the password on the account named in the message, and consider updating your other passwords too.
4. Delete the message.
5. Report it to the FTC at ReportFraud.ftc.gov.

## tr218-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
The email says it will send the video to all of my friends and family within a few hours unless I pay. It says if I tell anyone or report it, it will be sent sooner. I'm so embarrassed I can't tell anyone. Should I just pay to make it go away?

**ASSISTANT:**
No, please do not pay. This is a scam, and there is nothing to be embarrassed about.

1. Do not pay anything. Delete the message.
2. Their claims about access to your computer or webcam are all talk, even if the message includes a real old password.
3. If it shows a password, change the password on that account, and consider updating other passwords too.
4. Report the message to the FTC at ReportFraud.ftc.gov.

A threat to send something within hours is meant to rush you.

## tr218-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
I already sent some Bitcoin after an email said it had a video of me, and now they are asking for more. What do I do?

**ASSISTANT:**
I am sorry. Please stop here and do not pay anything more. It is a scam.

1. Do not send any more money, and do not reply.
2. Delete the message.
3. Change the password on the account named in the message, and consider updating your other passwords too.
4. Report it to the FTC at ReportFraud.ftc.gov.

Their claims about a video and access to your computer or webcam are all talk, so there is nothing more to gain from paying.

## tr218-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
My dad got an email demanding Bitcoin or they'll send a video of him to his friends. He's embarrassed and wants to pay. What should I tell him?

**ASSISTANT:**
Tell him not to pay. It is a scam, and he is not in trouble.

1. Explain that the claims about a video and access to his computer or webcam are all talk.
2. Have him delete the message and not reply.
3. If it includes a password, help him change the password on that account, and consider updating his other passwords too.
4. Help him report the message to the FTC at ReportFraud.ftc.gov.

The password may be one he used before, possibly from a data breach.

## tr218-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
How can I tell these blackmail emails are fake, and what should I do with them in the future?

**ASSISTANT:**
Here is what these emails usually look like and what to do.

1. They claim the sender hacked your computer and recorded you, and threaten to send the video to friends and family within hours unless you pay in Bitcoin.
2. They may include one of your old or recent passwords. That can come from a data breach, and does not mean they hacked you.
3. Their claims about your computer or webcam are all talk.
4. Do not pay anything, and delete the message.
5. Change the password on the account named, consider updating others, and report it at ReportFraud.ftc.gov.
