def R(id, ra, cov=None, src="pass", saf="pass", uns=(), sc=(2,2,2,2,2,2), dec="keep", reasons="", fix="", clar=False, dup="pass"):
    k = ["steps", "ask_or_answer", "constraints", "actionable", "plain", "realistic_user"]
    return {
        "id": id, "required_actions": list(ra),
        "covered": list(cov) if cov is not None else [True] * len(ra),
        "needs_clarification": clar,
        "gates": {"source": src, "safety": saf, "duplicate": dup},
        "unsupported_claims": list(uns),
        "scores": dict(zip(k, sc)), "decision": dec, "reasons": reasons, "fix": fix,
    }

REVIEWS = []

# ---- page 1: fakechecks
_fc = ["Do not send money back or forward any of a check's money to anyone (critical)",
       "Do not accept a check for more than the selling price / do not rely on check money (critical)",
       "Report to FTC at reportfraud.ftc.gov"]
REVIEWS += [
    R("tr212-a", _fc),
    R("tr212-c", _fc),
    R("tr212-e", _fc, src="pass", sc=(2,2,2,2,1,2), dec="revise",
      reasons="Last line is confusing and does not address the sender's instruction not to talk to the bank.",
      fix="Replace the last line 'If you want to know more about the check, you do not need anyone's permission to report it.' with a plain sentence such as 'The sender telling you to keep this from your bank is another warning sign, and you do not need anyone's permission to report it.' Do not add advice to call the bank unless sourced; the page does not say that."),
    R("tr212-r",
      ["Contact the gift card issuer right away and say the card was used in a scam (critical)",
       "Tell the store where the card was bought",
       "Report to FTC at reportfraud.ftc.gov",
       "If the card is not listed, check the card or search online for the issuer's contact info"],
      cov=[True, True, True, False], src="fail",
      uns=["'ask for a refund' -> not on https://consumer.ftc.gov/fakechecks (it is on https://consumer.ftc.gov/articles/gift-card-scams, step 'Ask for your money back')",
           "'so it is worth telling them what happened' (telling the bank) -> not on the cited page; the gift-card page does not mention contacting the bank either"],
      sc=(1,2,2,2,2,2), dec="revise",
      reasons="Refund request and 'tell the bank' advice are not supported by the cited page; no hint on how to find the issuer's contact.",
      fix="Add second source https://consumer.ftc.gov/articles/gift-card-scams (it supports 'ask for your money back; some companies may refund you' and 'have the card and receipt ready'). Add one line: if you do not know how to reach the company, look on the back of the card or search online for the company's contact information. Delete 'so it is worth telling them what happened' (keep only 'you may have to repay the bank' if desired; the fakechecks page supports that)."),
    R("tr212-f", _fc),
    R("tr212-g", ["Warning signs: asked to wire/gift card/crypto; check over price; pay to get prize",
                  "Never use check money for gift cards, money orders, crypto, wires; do not rely on check unless you know and trust sender",
                  "Report: FTC, USPIS, or state AG"]),
]

# ---- page 2: how-avoid-home-improvement-scam
_wi = ["Do not agree/sign or pay under pressure; do not decide fast (critical)",
       "Do not pay full cost up front; never make final payment until work finished and satisfied",
       "Use only licensed and insured contractor; confirm license with state/county; ask proof of insurance",
       "Get recommendations and more than one written estimate"]
REVIEWS += [
    R("tr213-a", _wi, cov=[True, True, True, True]),
    R("tr213-c", ["Do not pay up front / cash only; no final payment until done (critical)",
                  "Be wary of cash only, permits yourself, leftover materials",
                  "Take time; get written estimates to compare"]),
    R("tr213-e", ["Do not sign today (critical)", "Be wary of contractor-arranged lender; shop around and compare loan terms",
                  "Do not sign unread or blank-space documents; confirm can afford payments", "Do not let anyone pressure you",
                  "Do not transfer deed without talking to attorney or trusted person"]),
    R("tr213-r", ["Check contract for written statement of right to cancel; generally three business days to cancel for a contract signed at home (critical)",
                  "Try to resolve with contractor first", "Follow up calls with certified-mail letter with return receipt",
                  "Keep notes and copies", "If not settled, contact state attorney general or local consumer protection office",
                  "Do not pay more until work done"],
      cov=[False, True, True, True, True, True], sc=(1,2,2,2,2,2), dec="revise",
      reasons="Reply only says to look for a cancel statement; it never says the user generally has three business days to cancel and should act quickly, which is the key time-limited action for someone who already signed at home.",
      fix="Rewrite step 1 as: 'A contract signed in your home generally gives you three business days to cancel. Check your contract for the written statement of your right to cancel, and act quickly.' Do not invent how to send a cancellation; the page does not say. Keep steps 2 to 5 as they are."),
    R("tr213-f", ["Pressure to decide fast is a warning sign",
                  "Do not pay full cost up front; some states limit down payments, check local rules; no final payment until satisfied",
                  "Licensed and insured; confirm license; proof of insurance", "Recommendations and multiple written estimates",
                  "If trouble, state attorney general or local consumer protection office"],
      cov=[True, False, True, True, True], sc=(1,2,2,2,2,2), dec="revise",
      reasons="The neighbor was asked for half up front. Saying only 'do not pay the full cost up front' can suggest half is fine; page says some states limit down payments and to check local rules.",
      fix="In step 2 add: 'Some states limit how much can be asked for up front, so check your local rules before she pays any deposit.' Keep the rest."),
    R("tr213-g", ["Licensed and insured; confirm license; proof of insurance", "Recommendations from people you trust",
                  "Check Home Builders Association/consumer protection for complaints; search company name with scam/review/complaint",
                  "Several written estimates, not automatically the lowest",
                  "Contract: name, address, phone, license number, start/completion dates, spoken promises, written statement of right to cancel, no blanks",
                  "Do not pay everything up front"],
      cov=[True, True, True, True, False, True], sc=(1,2,2,2,2,2), dec="revise",
      reasons="Contract checklist omits 'a written statement of your right to cancel', which the page lists.",
      fix="In step 5 add 'a written statement of your right to cancel' to the list of things the contract should show."),
]

# ---- page 3: debt-collection-faqs
_dc = ["Do not pay or share personal/financial info until validation information is received in writing (critical)",
       "Ask for written validation notice (sent at first contact or within 5 days); check collector name/address, original creditor, amount",
       "If not owed, send dispute letter within 30 days of receiving validation info, request verification",
       "Send by certified mail with return receipt; keep copy"]
REVIEWS += [
    R("tr214-a", _dc),
    R("tr214-c", ["Collector limits: no threats of arrest/false legal action, no calls before 8 or after 9, no harassment, max seven calls in seven days",
                  "Do not share info until validation info in writing",
                  "Dispute letter within 30 days of getting validation info, certified mail with return receipt",
                  "Report to FTC or CFPB",
                  "Optional: letter asking collector to stop contacting you"],
      cov=[True, True, True, True, False],
      uns=["'You do not have to pay' -> not stated on the page; the page says dispute and ask for verification of an unrecognized debt"],
      src="fail", sc=(2,2,2,2,2,2), dec="revise",
      reasons="Opening claim 'You do not have to pay' is not on the page. Also the user is scared by repeated calls and the page's stop-contact letter is not offered.",
      fix="Change the first line to: 'Do not pay anything yet, and a collector is not allowed to treat you this way.' Optionally add one step: 'If you want the calls to stop, send the collector a letter asking it to stop contacting you; keep a copy and use certified mail with a return receipt.'"),
    R("tr214-e", _dc),
    R("tr214-r", _dc + ["Optional: stop-contact letter", "Report to FTC"]),
    R("tr214-f", ["Collector generally may discuss debt only with her or spouse", "Ask for written validation notice",
                  "Dispute letter within 30 days of getting it, certified mail with return receipt, keep copy",
                  "Report to FTC, CFPB or state AG", "Do not share info until validation notice"]),
    R("tr214-g", ["No harassment/threats/obscene language", "No more than seven calls in seven days; no contact before 8 or after 9 unless agreed",
                  "No lying about amount, posing as attorney/government, false arrest/legal threats", "No revealing debt publicly or discussing with others than you/spouse",
                  "Report to FTC, CFPB, or state AG"]),
]

# ---- page 4: toll text
_tl = ["Do not click links in or respond to the text (critical)",
       "Contact the state's tolling agency using a phone number/website you already know is real, not the text's",
       "Report with 'report junk' or forward to 7726 (SPAM)",
       "Delete the text once checked and reported"]
REVIEWS += [
    R("tr215-a", _tl),
    R("tr215-c", _tl),
    R("tr215-e", _tl, src="fail", saf="fail",
      uns=["'A quick search on your phone is fine.' -> the page says to use a number or website you already know is real and says nothing about searching; a search can lead to a fake site"],
      sc=(2,2,2,2,2,2), dec="revise",
      reasons="Suggests searching to find the agency, which is unsupported and could lead a low-confidence user to a lookalike number or site. Step 4 also tells the user to delete right away, while the page says delete after checking and reporting.",
      fix="Remove 'A quick search on your phone is fine.' Replace with: 'If you do not have a number or website you know is real, do not use the one in the text. Ask someone you trust to help you find the real one.' In step 4 write 'Report the text with \"report junk\", or forward it to 7726 (SPAM). Delete it once you have checked and reported it.'"),
    R("tr215-r", _tl),
    R("tr215-f", _tl),
    R("tr215-g", _tl),
]

# ---- page 5: IRS
_irs = ["Hang up / do not respond; do not give personal or financial info (critical)",
        "Do not pay by wire transfer, prepaid card or gift card (critical)",
        "If in doubt, call the IRS directly at 1-800-829-1040",
        "Report to TIGTA (tigta.gov) and FTC (ftc.gov/complaint)"]
REVIEWS += [
    R("tr216-a", _irs),
    R("tr216-c", _irs),
    R("tr216-e", _irs + ["Let family and friends know"]),
    R("tr216-r", ["Stop talking/hang up if they call again; give no more info (critical)",
                  "Do not pay by wire, prepaid card or gift card",
                  "Report to TIGTA and FTC",
                  "Recovery after sharing an SSN and bank name: report at IdentityTheft.gov for a recovery plan, consider a fraud alert or credit freeze, review credit reports and bank statements (critical for this scenario; NOT on cited page)"],
      cov=[True, True, True, False], dec="revise", sc=(0,2,2,2,2,2),
      reasons="The user already gave an SSN and bank name. The reply only repeats prevention steps and the generic IRS-call advice; it has nothing that fixes the reported problem. The cited page does not cover this, but another official FTC page does.",
      fix="Add second source https://consumer.ftc.gov/articles/what-know-about-identity-theft. Add steps from it: (1) Go to IdentityTheft.gov to report it and get a free recovery plan; (2) Place a free fraud alert by contacting one of the three credit bureaus (it must tell the other two); a credit freeze (free) is also possible by contacting each bureau; (3) Get your free credit reports and check bank statements for charges or accounts you do not recognize. Remove the step 'If you are in doubt, call the IRS directly' (the caller is already known to be fake in this story) or keep it as a last line. Do not say anything about contacting the bank; that page does not cover it."),
    R("tr216-f", _irs + ["Let family and friends know"]),
    R("tr216-g", _irs + ["Tell family and friends"]),
]

# ---- page 6: uscourts jury scam
_jd = ["Hang up / do not call the number back; do not give requested info or pay (critical)",
       "Contact the local court clerk's office or U.S. Marshals Service office (find via uscourts.gov/court-locator)",
       "Notify the Clerk of Court's office of the U.S. District Court in your area"]
REVIEWS += [
    R("tr217-a", _jd),
    R("tr217-c", _jd, src="fail",
      uns=["'Scammers use fear to cloud judgment.' -> not on the page",
           "'Scammers use names and hearing times to seem real, so those details do not prove anything.' -> not on the page"],
      sc=(2,2,2,2,2,2), dec="revise", reasons="Two unsupported statements about how scammers behave.",
      fix="Delete the clause 'Scammers use fear to cloud judgment.' from step 1 (keep 'Step away from the message so you can think calmly'; the page says to separate yourself from the call to assess calmly). Delete the last line about names and hearing times; replace with the sourced line 'A judge, not a caller, decides any fine for missing jury duty, in open court.'"),
    R("tr217-e", _jd, src="fail",
      uns=["'Knowing your name and a hearing time is how scammers seem credible.' -> not on the page"],
      sc=(2,2,2,1,2,2), dec="revise",
      reasons="Unsupported claim about scammers; steps 3 and 4 overlap (contact the clerk's office twice) so the list is repetitive.",
      fix="Replace the last line with 'A judge, not a caller, decides any fine for missing jury duty, in open court.' Merge steps 3 and 4 into one: 'Contact your local court clerk's office or U.S. Marshals Service office, and tell the Clerk of Court's office of the U.S. District Court in your area about the call.'"),
    R("tr217-r", ["Hang up on further calls; give no more info",
                  "Contact local court clerk's office or U.S. Marshals and notify Clerk of Court (page)",
                  "Wired money: report to the wire transfer company immediately, say you were tricked, ask for a refund (NOT on cited page) (critical)",
                  "Report to FTC at ReportFraud.ftc.gov (NOT on cited page)"],
      cov=[True, True, False, False], dec="revise", sc=(0,2,2,2,2,2),
      reasons="The user already wired money. The reply never tells them to contact the wire transfer company, which is the action that might stop or recover the money. The cited page does not cover this; another official FTC page does.",
      fix="Add second source https://consumer.ftc.gov/articles/what-do-if-you-were-scammed. Put as step 1: 'Contact the wire transfer company (for example Western Union or MoneyGram) right away, tell them you were tricked into sending the money, and ask for a refund.' Later add 'Report it to the FTC at ReportFraud.ftc.gov.' Keep the clerk/Marshals/Clerk of Court steps. Do not give phone numbers (that page has none). Do not promise the money will come back; the page says it might be gone."),
    R("tr217-f", _jd),
    R("tr217-g", ["Jurors who miss duty are typically contacted by the Clerk's Office",
                  "Judge imposes any fine in open session; juror can explain first",
                  "Federal court never threatens or demands immediate payment by phone or wire",
                  "Hang up and contact local clerk's office or U.S. Marshals; notify Clerk of Court; court-locator"]),
]
