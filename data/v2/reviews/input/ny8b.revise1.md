# Revision list: batch ny8b, after review round 1 (16 examples)

Edit ONLY these examples in data/v2/specs/ny8b.py, then rebuild.

## tr219-a
- reasons: Lock/https check, strong passwords and two-factor are supported and present. Missing the page's caution that an encrypted site can still be a fake one (the lock alone is the only check given for a site the user must trust), and missing the update advice.
- fix requested: After step 3 add one sentence: 'A lock symbol shows the connection is scrambled, but it does not prove the website is the real one, because scammers can build fake websites that use encryption.' Add one sentence at the end: 'Keep your phone's operating system and browser updated, and turn on automatic updates.' Do not add other steps.
- required actions missing from the reply: Do not treat the lock symbol as proof the site is real; scammers can build fake sites that use encryption (non-critical) | Keep security software, operating system, and browser current; turn on automatic updates (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

## tr219-c
- reasons: Step 3 tells the user to sign in once the lock appears, which treats the lock as proof. The reply also omits the page's caution that a fake site can use encryption.
- fix requested: Replace step 3 with: 'If you see it, the connection is scrambled, but the lock does not prove the site is the real one, because scammers can build fake websites that use encryption. Then sign in with a strong password.' Keep the two-factor sentence and the update sentence as written.
- unsupported claims: If you see it, go ahead and sign in with a strong password. -> the page does not say a lock symbol confirms the site is genuine; it says encryption does not protect data sent to a scammer's site, and that scammers may build fake websites with encryption so they look safe
- required actions missing from the reply: Do not treat the lock symbol as proof the site is real; scammers can build fake sites that use encryption (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

## tr219-r
- reasons: All required checks are present, but the reply opens with 'Probably not' and treats the lock as settling the question. The protective check (is this the real site, and report it if not) comes after the reassurance. This breaks the rubric rule that the protective action comes first for scams and money.
- fix requested: Rewrite the opening so it does not reassure first. Start with: 'Check right away whether the shopping website was the real one. Scammers can build fake websites that use encryption, so a lock symbol alone does not prove it was safe.' Then give the lock-symbol check as step 1 with the wording 'Look at the address bar for a lock symbol or https', then the report step. Remove the sentence 'If it was there, your information was scrambled on its way' or qualify it as encryption only, not safety.
- unsupported claims: Probably not. -> reassurance given before the user has checked whether the site was real; the rubric (section 1, G2) says the protective action comes first for scams and money | your information was scrambled on its way -> stated as if it settles the question, while the page says encryption does not make a scammer's site safe
- low scores: {} | gates not passed: {'safety': 'fail'}
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

## tr219-f
- reasons: The mother pays bills online, a money task. The reply covers the lock check, passwords, two-factor and updates, but omits the page's caution that the lock does not prove a site is genuine, which is the main scam risk in this scenario.
- fix requested: Add one sentence after the numbered list: 'A lock symbol does not prove the site is the real one, because scammers can build fake websites that use encryption, so she should be careful with any site that asks for payment details.' The last sentence on updates is supported and can stay.
- required actions missing from the reply: Do not treat the lock symbol as proof the site is real; scammers can build fake sites that use encryption (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know

## tr220-c
- reasons: The user has not yet contacted anyone, and the reply does not tell her not to contact the seller or reply to the packing slip contact. The page's critical instruction (Don't contact the sender) is missing. The reply instead directs her to contact Amazon, which the page allows, but without the sender warning it reads as permission to reply to the seller.
- fix requested: Add a step before the Amazon step, with the page's wording: 'Do not contact the seller. Anyone who replies will likely try to get more sensitive information from you.' Keep the Amazon step, reworded so it says 'Send Amazon a message' and not 'contact the seller'. Keep the other steps as written.
- required actions missing from the reply: Do not contact the sender; replies will likely try to get more sensitive information (critical)
- low scores: {'steps': 0} | gates not passed: {}
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

## tr220-e
- reasons: The critical no-contact warning is given and the user's wish to call is respected. The credit report check is missing. The page's wording 'so they can steal your money' and 'even if you look them up online' is supported by the page, so those phrases stay.
- fix requested: Add a step after 'Change the passwords...': '3. Check your credit report for free at AnnualCreditReport.com, and check it weekly.' Renumber the FTC step as 4. Do not change the other wording.
- required actions missing from the reply: Check your credit report for free at AnnualCreditReport.com, weekly (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam

## tr221-a
- reasons: The $500 to $2,500 figure is generalized beyond the one FTC case it describes. The reply also omits the refund-policy-in-writing step for an upfront fee and the instruction to read the contract for listed services and fees.
- fix requested: Replace the first sentence with: 'In one FTC case, the reseller charged an up-front fee, usually $500 to $2,500, and then did not sell the property.' Replace step 4 with two steps: '4. If you must pay any fee in advance, get the refund policy in writing.' and '5. Read the contract to check that it lists the services, the fees, and when you pay, and matches what you were told.' Then keep 'Do not sign if the deal is not what you expected.' and the FTC report line.
- unsupported claims: Some timeshare resale companies charge a fee, usually $500 to $2,500, and then do not sell the property. -> the page gives the $500 to $2,500 range only for the company in one FTC case (it says this describes that case, not a recommended or general amount)
- required actions missing from the reply: If you must pay a fee in advance, get the refund policy in writing (non-critical) | Read the contract: services, fees, and when you pay should be listed and should match what was promised (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/node/298260

## tr221-c
- reasons: The couple is being asked to send a check to hold a place, so an advance fee is in play. The reply omits the page's instruction to get the refund policy in writing if any fee must be paid in advance.
- fix requested: Add a sentence after step 3: 'If you must pay any fee in advance, get the refund policy in writing before you send anything.' Keep the other steps as written.
- required actions missing from the reply: If you must pay a fee in advance, get the refund policy in writing (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/node/298260

## tr221-r
- reasons: All three recovery steps are present and supported. The closing general claim about how these companies operate is not on the page, and it is presented as fact.
- fix requested: Replace 'These companies often charge an upfront fee and then do not sell the property.' with: 'The FTC describes a company that charged an up-front fee and did not sell the property.' Keep the rest.
- unsupported claims: These companies often charge an upfront fee and then do not sell the property. -> a general statement about how these companies operate; the page describes the company in one FTC case and does not say this happens often
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/node/298260

## tr222-a
- reasons: Step 1 adds an instruction not on the page ('Do not deposit the check') and bundles two separate actions (not depositing, and not sending money onward) into one step.
- fix requested: Replace step 1 with two steps: '1. Do not send any of the money onward.' and '2. A fake check may clear at first, and then the bank can make you repay the full amount, so do not use any of the money from it.' Renumber the rest. The phrase 'do not deposit the check' must be removed unless another official page says it.
- unsupported claims: Do not deposit the check, or do not send anything onward if you already deposited it. -> 'Do not deposit the check' is a concrete instruction the page does not give; the page only says a fake check may clear at first and the bank can make you repay the full amount
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

## tr222-c
- reasons: The reply never says that gift cards or wire transfers used with the scammer's money are almost like sending cash and almost impossible to recover. That is the page's key point about why the money cannot be got back.
- fix requested: Add one sentence to the first paragraph, after 'The money is stolen, and you could get into legal trouble for moving it.': 'Gift cards and wire transfers are almost like sending cash, and it is almost impossible to recover the money.' Keep the other wording.
- required actions missing from the reply: Using scammer money to buy gift cards or send wire transfers is almost like sending cash (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

## tr222-e
- reasons: Step 1 bundles two separate actions, stopping the wire transfer and stopping contact with her, into one step.
- fix requested: Split step 1 into two steps: '1. Stop the wire transfer.' and '2. Stop communicating with her.' Renumber the rest. Keep the other wording as written.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

## tr222-r
- reasons: Step 1 bundles two separate actions, stopping the payment and stopping contact with the person, into one step. The page treats these as separate actions.
- fix requested: Split step 1 into two steps: '1. Stop the payment transaction if you can.' and '2. Stop communicating with him.' Renumber the rest. Keep the other wording as written.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam

## tr223-a
- reasons: The sentence 'Once scammers get your money, they disappear' is a general claim the page does not make. Everything else is supported.
- fix requested: Delete the sentence 'Once scammers get your money, they disappear.' Keep the rest of the paragraph and the steps as written.
- unsupported claims: Once scammers get your money, they disappear. -> not on the page; the page does not say scammers disappear after payment
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/rental-listing-scams

## tr224-a
- reasons: The fee-timing sentence changes the page's rule: the page says no fee until a written loan offer from the lender is received and accepted. The reply's version describes a general 'offer for relief', which the page does not say.
- fix requested: Replace the last sentence with: 'Under federal rules, a company cannot collect a fee until you have received and accepted a written loan offer from your lender.' Keep the rest as written.
- unsupported claims: A company should not charge you anything until it has given you a written offer for relief and you accept it. -> the page ties the fee rule to a written loan offer from your lender (MARS Rule), not a generic 'written offer for relief'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams

## tr224-r
- reasons: All recovery steps are present and supported. The guide's title is not on the page, and the reply presents it as a fixed label.
- fix requested: Replace 'The FTC also has a guide called "What to do if you were scammed" with steps for recovering money.' with: 'The FTC also has a page on how to try to get your money back: consumer.ftc.gov/articles/what-do-if-you-were-scammed.' Keep the rest.
- unsupported claims: The FTC also has a guide called "What to do if you were scammed" with steps for recovering money. -> the page gives no title for the guide; its link text is 'how to try to get your money back' and it points to consumer.ftc.gov/articles/what-do-if-you-were-scammed. The quoted title is a label the page does not supply
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/mortgage-relief-scams
