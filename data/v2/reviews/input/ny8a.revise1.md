# Revision list: batch ny8a, after review round 1 (16 examples)

Edit ONLY these examples in data/v2/specs/ny8a.py, then rebuild.

## tr212-e
- reasons: Last line is confusing and does not address the sender's instruction not to talk to the bank.
- fix requested: Replace the last line 'If you want to know more about the check, you do not need anyone's permission to report it.' with 'Even if you see the funds in your account, that does not mean the check is good.' (the fakechecks page says this). Do not add advice about telling the bank; the page does not give it.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/fakechecks

## tr212-r
- reasons: One unsupported clause: the advice to tell the bank what happened.
- fix requested: Delete the clause 'so it is worth telling them what happened' from the last paragraph. Keep 'Because the check was fake, you may have to repay the bank' (supported). No second source is needed.
- unsupported claims: 'so it is worth telling them what happened' (telling the bank) -> not on https://consumer.ftc.gov/fakechecks; that page says you may have to repay the bank but does not advise telling the bank. The refund request in step 2 is supported: the page says 'Ask them if they can refund your money.'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/fakechecks

## tr213-r
- reasons: Reply only says to look for a cancel statement; it never says the user generally has three business days to cancel and should act quickly, which is the key time-limited action for someone who already signed at home.
- fix requested: Rewrite step 1 as: 'A contract signed in your home generally gives you three business days to cancel. Check your contract for the written statement of your right to cancel, and act quickly.' Do not invent how to send a cancellation; the page does not say. Keep steps 2 to 5 as they are.
- required actions missing from the reply: Check contract for written statement of right to cancel; generally three business days to cancel for a contract signed at home (critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

## tr213-f
- reasons: The neighbor was asked for half up front. Saying only 'do not pay the full cost up front' can suggest half is fine; page says some states limit down payments and to check local rules.
- fix requested: In step 2 add: 'Some states limit how much can be asked for up front, so check your local rules before she pays any deposit.' Keep the rest.
- required actions missing from the reply: Do not pay full cost up front; some states limit down payments, check local rules; no final payment until satisfied
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

## tr213-g
- reasons: Contract checklist omits 'a written statement of your right to cancel', which the page lists.
- fix requested: In step 5 add 'a written statement of your right to cancel' to the list of things the contract should show.
- required actions missing from the reply: Contract: name, address, phone, license number, start/completion dates, spoken promises, written statement of right to cancel, no blanks
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/how-avoid-home-improvement-scam

## tr214-c
- reasons: Opening claim 'You do not have to pay' is not on the page. Also the user is scared by repeated calls and the page's stop-contact letter is not offered.
- fix requested: Change the first line to: 'Do not pay anything yet, and a collector is not allowed to treat you this way.' Optionally add one step: 'If you want the calls to stop, send the collector a letter asking it to stop contacting you; keep a copy and use certified mail with a return receipt.'
- unsupported claims: 'You do not have to pay' -> not stated on the page; the page says dispute and ask for verification of an unrecognized debt
- required actions missing from the reply: Optional: letter asking collector to stop contacting you
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

## tr214-f
- reasons: Drops the page's 'generally' qualifier, so the rule is stated more strongly than the source.
- fix requested: In step 1 change 'A collector cannot discuss a debt' to 'A collector generally cannot discuss a debt'. Keep the rest.
- unsupported claims: 'A collector cannot discuss a debt with anyone other than her or her spouse.' -> the page says 'Generally, a debt collector can't discuss your debt with anyone but you or your spouse'; the reply drops 'generally' and states an absolute rule
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

## tr214-g
- reasons: Drops the page's 'generally' qualifier.
- fix requested: In item 4 change 'or discuss it with anyone other than you or your spouse' to 'or generally discuss it with anyone other than you or your spouse'. Keep the rest.
- unsupported claims: 'Reveal your debt publicly, or discuss it with anyone other than you or your spouse.' -> the page says 'Generally, a debt collector can't discuss your debt with anyone but you or your spouse'; the reply drops 'generally'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.consumer.ftc.gov/articles/debt-collection-faqs

## tr215-e
- reasons: Suggests searching to find the agency, which the page does not support and which could lead a low-confidence user to a lookalike number or site.
- fix requested: In step 2 delete the sentence 'A quick search on your phone is fine.' Keep the rest of step 2, which reads 'Find your state's tolling agency yourself, with a phone number or website you know is real, not the one in the text.' Keep the other steps.
- unsupported claims: 'A quick search on your phone is fine.' -> the page says to use a phone number or website you already know is real and does not mention searching; a search can lead to a lookalike site
- low scores: {} | gates not passed: {'source': 'fail', 'safety': 'fail'}
- sources: https://www.consumer.ftc.gov/consumer-alerts/2025/01/got-text-about-unpaid-tolls-its-probably-scam

## tr216-r
- reasons: The user already gave an SSN and bank name. The reply only repeats prevention steps and the generic IRS-call advice; it has nothing that fixes the reported problem. The cited page does not cover this, but another official FTC page does.
- fix requested: Add second source https://consumer.ftc.gov/articles/what-know-about-identity-theft. Add steps from it: (1) Go to IdentityTheft.gov to report it and get a free recovery plan; (2) Place a free fraud alert by contacting one of the three credit bureaus (it must tell the other two); a credit freeze (free) is also possible by contacting each bureau; (3) Get your free credit reports (the page links to them), and check bank statements for withdrawals you did not make. Remove the step 'If you are in doubt, call the IRS directly' (the caller is already known to be fake in this story) or keep it as a last line. Do not say anything about contacting the bank; that page does not cover it.
- required actions missing from the reply: Recovery after sharing an SSN and bank name: report at IdentityTheft.gov for a recovery plan, consider a fraud alert or credit freeze, review credit reports and bank statements (critical for this scenario; NOT on cited page)
- low scores: {'steps': 0} | gates not passed: {}
- sources: https://consumer.ftc.gov/node/298362

## tr217-c
- reasons: The last sentence adds a conclusion the page does not state. The first part is supported, and 'Scammers use fear to cloud judgment.' is supported by the page's point about fear impairing judgment.
- fix requested: Replace the last sentence with 'Scammers use specific names and designated court hearing times.' Keep 'Scammers use fear to cloud judgment.' (supported).
- unsupported claims: 'Scammers use names and hearing times to seem real, so those details do not prove anything.' -> the page says scammers use 'specific names and designated court hearing times'; it does not say those details 'do not prove anything'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.uscourts.gov/node/14024

## tr217-e
- reasons: Steps 3 and 4 both tell the user to contact the clerk's office, so the list repeats itself.
- fix requested: Merge steps 3 and 4 into one step: 'Contact your local court clerk's office or U.S. Marshals Service office, and tell the Clerk of Court's office of the U.S. District Court in your area about the call.' Keep the last two sentences as written; both are supported.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://www.uscourts.gov/node/14024

## tr217-r
- reasons: The user already wired money. The reply never tells them to contact the wire transfer company, which is the step that might stop or recover the money. The cited page does not cover this; another official FTC page does.
- fix requested: Add second source https://consumer.ftc.gov/articles/what-do-if-you-were-scammed. Make it step 1: 'Report it to the wire transfer company immediately, such as Western Union or MoneyGram, and ask them to refund your money.' Later add 'Report it to the FTC at ReportFraud.ftc.gov.' Keep the clerk, Marshals, and Clerk of Court steps. Do not give phone numbers. Do not promise the money will come back; the page says it might be gone already.
- required actions missing from the reply: Wired money: report it to the wire transfer company immediately and ask them to refund your money (NOT on cited page) (critical) | Report to FTC at ReportFraud.ftc.gov (NOT on cited page)
- low scores: {'steps': 0} | gates not passed: {}
- sources: https://www.uscourts.gov/node/14024

## tr218-a
- reasons: Adds an instruction not to reply that the cited page does not give. Everything else is supported.
- fix requested: Change step 1 from 'Do not pay, and do not reply.' to 'Do not pay anything.' Keep the other steps and the closing lines.
- unsupported claims: 'Do not pay, and do not reply.' -> the page says 'Stop. Don't pay anything. Delete the message.' A targeted check found the page does not address replying
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

## tr218-r
- reasons: Two unsupported steps: a reply instruction the page does not give, and a password change applied to a user whose email mentions no password.
- fix requested: Change step 1 to 'Do not send any more money.' Delete step 3 (the password change) entirely. Keep the delete and report steps.
- unsupported claims: 'Do not send any more money, and do not reply.' -> 'do not reply' is not on the page | 'Change the password on the account named in the message, and consider updating your other passwords too.' -> the page makes a password change conditional on the email including a password; this user's email mentions no password or account
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail

## tr218-f
- reasons: One unsupported instruction (not to reply). The password step is correctly conditional.
- fix requested: In step 2 change 'Have him delete the message and not reply.' to 'Have him delete the message.' Keep the rest.
- unsupported claims: 'Have him delete the message and not reply.' -> not on the page; the page only says 'Delete the message.'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail
