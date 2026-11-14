# Review input: batch ny8a, round 2 (16 examples)

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

Even if you see the funds in your account, that does not mean the check is good.

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

Because the check was fake, you may have to repay the bank.

## tr213-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A contractor at the door pushes for a quick repair deal and upfront payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

**USER:**
I already signed a contract at my kitchen table with a door to door contractor and gave him a deposit. Now I think he was pushy and I'm worried. What can I do?

**ASSISTANT:**
You still have steps you can take.

1. Look in your contract for a written statement of your right to cancel. A contract signed in your home should include one, and you have three business days to cancel, so act quickly.
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
2. Do not pay the full cost up front, and never make the final payment until the work is finished and she is satisfied. Some states limit how much a contractor can ask for as a down payment, so check the rules with your state or local consumer agency before she pays any deposit.
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
5. Read the contract carefully. It should show the contractor's name, address, phone, license number, start and finish dates, and a written statement of your right to cancel. Write in any spoken promises and fill in all blank spaces.

Do not pay everything up front.

## tr214-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
A man keeps calling me at 7 in the morning and again at night, six times this week, about some credit card I don't have. He says if I don't pay he will have me arrested. I'm scared. I don't know whose debt this is and I don't want to just pay to make it stop. What are my rights?

**ASSISTANT:**
A collector is not allowed to treat you this way, and you can dispute a debt you do not recognize.

1. Collectors cannot threaten arrest or legal action they will not take, and cannot call before 8 a.m. or after 9 p.m. unless you agree.
2. They also cannot harass you or call more than seven times in seven days.
3. Do not share personal or financial information until you get validation information in writing.
4. Send a letter within 30 days of getting it saying you do not owe the money, by certified mail with a return receipt.
5. If you want the calls to stop, mail the collector a letter asking it to stop contacting you. Keep a copy and send it by certified mail with a return receipt.
6. Report the calls to the FTC at reportfraud.ftc.gov or the CFPB at cfpb.gov/complaint.

## tr214-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: A caller demands payment for a debt the user does not recognize (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

**USER:**
A debt collector called my mother's friend and also called her daughter and talked about the debt. The friend says she doesn't owe it. How can I help her?

**ASSISTANT:**
Help her avoid paying until the debt is proven, and know that a collector may not discuss her debt with her daughter.

1. A collector generally cannot discuss a debt with anyone other than her or her spouse.
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
4. Reveal your debt publicly, or generally discuss it with anyone other than you or your spouse.

To report one, go to the FTC at reportfraud.ftc.gov, the CFPB at cfpb.gov/complaint, or your state attorney general's office.

## tr215-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: A text says the user owes an unpaid road toll (any) | sensitive: True | reviewed by a person: False
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

**USER:**
I don't have the number for my state toll agency and I don't want to look anything up. The text has a link that says I can just pay quickly there. Can I tap it just this once, since I did drive on a toll road?

**ASSISTANT:**
I would not tap it, even once. Driving on a toll road does not make the text real.

1. Do not click links in unexpected texts or respond to them.
2. Find your state's tolling agency yourself, with a phone number or website you know is real, not the one in the text.
3. Ask the agency whether you owe a toll.
4. Report the text with "report junk," or forward it to 7726 (SPAM), then delete it.

Taking a minute to check is better than reacting quickly.

## tr216-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A call or message claims to be the IRS and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/298362 ; https://consumer.ftc.gov/articles/what-know-about-identity-theft

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

Scammers use specific names and designated court hearing times.

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
3. Contact your local court clerk's office or U.S. Marshals Service office, and tell the Clerk of Court's office of the U.S. District Court in your area about the call.

Knowing your name and a hearing time is how scammers seem credible. A judge, not a caller, decides any fine.

## tr217-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: A caller says the user missed jury duty and must pay a fine (any) | sensitive: True | reviewed by a person: False
- sources: https://www.uscourts.gov/node/14024 ; https://consumer.ftc.gov/articles/what-do-if-you-were-scammed

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

## tr218-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
I got an email saying the sender hacked my computer and recorded me on adult websites. They will send the video to my family unless I pay in Bitcoin. What do I do?

**ASSISTANT:**
Do not pay anything. This is a scam, and the claims are all talk.

1. Do not pay anything.
2. Delete the message.
3. Report it to the FTC at ReportFraud.ftc.gov.

Scammers claim they have a video of you or access to your computer or webcam, but that is just a threat to scare you.

## tr218-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: An email claims to have embarrassing video or a password and demands payment (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

**USER:**
I already sent some Bitcoin after an email said it had a video of me, and now they are asking for more. What do I do?

**ASSISTANT:**
I am sorry. Please stop here and do not pay anything more. It is a scam.

1. Do not send any more money.
2. Delete the message.
3. Report it to the FTC at ReportFraud.ftc.gov.

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
2. Have him delete the message.
3. If it includes a password, help him change the password on that account, and consider updating his other passwords too.
4. Help him report the message to the FTC at ReportFraud.ftc.gov.

The password may be one he used before, possibly from a data breach.
