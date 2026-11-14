# Revise report: batch ny8b, revise1 (16 listed, from review round 1)

Result: 15 fixed, 1 left unchanged (tr223-a, the page supports the sentence the reviewer flagged), 0 cannot fix. Builder: OK.

Revision list was missing and was built with `review_io.py todo ny8b 1` (16 examples). Its snapshot is in `data/v2/snapshots/ny8b.before_revise1.jsonl`, and `data/v2/reviews/ny8b.r2.todo.json` was written for re-review.

## Fixed
- tr219-a: added the lock-symbol caution (encrypted is not proof of a real site) and the phone OS and automatic-updates sentence. Browser update advice for a phone was not on the page, so it was left out.
- tr219-c: step 3 no longer says to sign in just because the lock is there. The two-factor and update sentences are unchanged.
- tr219-r: removed "Probably not" and the "scrambled on its way" line. The reply now opens with the protective check, then the lock-symbol check, then the real-site check, then the FTC report line.
- tr219-f: added the lock-symbol caution after the list. The reviewer's clause about being careful with sites that ask for payment details is not on the page, so it was left out.
- tr220-c: added the no-contact step first ("Do not contact the sender..."). The page says "sender", not "seller", so the reviewer's wording was changed to match the page. Added the credit report step from the page.
- tr220-e: added "Check your credit report weekly for free at AnnualCreditReport.com" as step 3 and renumbered the FTC step to 4.
- tr221-a: the reviewer's "replace the first sentence" would have removed the protective sentence "Do not pay the upfront fee yet." The $500 to $2,500 sentence (the one the reviewer quoted as unsupported) was reworded as one FTC case. Step 4 is now two steps (refund policies in writing, then reading the contract). "Do not sign..." follows the list.
- tr221-c: added the refund-policies-in-writing sentence after the list.
- tr221-r: "These companies often charge..." replaced with a sentence about the FTC's one described company.
- tr222-a: removed "Do not deposit the check", which the page does not say. Step 1 is now "Do not send any of the money onward." The clear-then-repay point is in the opening paragraph. The reviewer's "do not use any of the money" was not on the page, so it was left out.
- tr222-c: added the gift cards and wire transfers "almost like sending cash" sentence after the legal-trouble sentence.
- tr222-e: split step 1 into stop the wire transfer, and stop communicating.
- tr222-r: split step 1 into stop the payment, and stop communicating.
- tr224-a: replaced the fee-timing sentence with the page's wording (illegal to charge until a written loan offer from your lender is accepted). The reviewer's "Under federal rules" was replaced by the page's own phrasing.
- tr224-r: replaced the quoted guide title with the page's link text and URL.

## Not changed
- tr223-a: the reviewer marked "Once scammers get your money, they disappear." as not on the page. The FTC page says: "Once the scammer gets your money or personal information, they disappear and you're left with no place to move in to." The sentence is supported and was kept. The reviewer's source-gate fail should be re-checked.

## Cannot fix
- None.

## Follow-ups touched
- None. None of the listed examples has a follow-up partner, so no earlier turns were edited.

## Page contradicted the reviewer
- tr223-a (above).
- tr220-c and tr220-e: the page says "Don't contact the sender", not "seller".
- tr221-a: the reviewer's "replace the first sentence" would have removed the protective sentence, so the $500 to $2,500 sentence was reworded instead.

## Source pages fetched (6)
- https://consumer.ftc.gov/articles/are-public-wi-fi-networks-safe-what-you-need-know
- https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-package-you-didnt-order-its-probably-scam
- https://consumer.ftc.gov/node/298260
- https://www.consumer.ftc.gov/blog/2021/12/avoiding-money-mule-scam
- https://consumer.ftc.gov/articles/rental-listing-scams
- https://consumer.ftc.gov/articles/mortgage-relief-scams
