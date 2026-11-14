# Review report: batch ny8a, round 1

Examples: 42 (7 source pages). Checker: OK.

## Decisions
- keep: 26
- revise: 16
- reject: 0

Revise by source page:
- FTC fake checks (tr212): 3 (tr212-e plain line; tr212-r unsupported "tell the bank" clause)
- FTC home improvement (tr213): 3 (tr213-r, tr213-f, tr213-g)
- FTC debt collection FAQs (tr214): 3 (tr214-c, tr214-f, tr214-g)
- FTC toll text (tr215): 1 (tr215-e)
- IRS impostor (tr216): 1 (tr216-r)
- uscourts jury duty (tr217): 3 (tr217-c, tr217-e, tr217-r)
- FTC blackmail email (tr218): 3 (tr218-a, tr218-f, tr218-r)

## Corrections to records from the earlier partial run
- tr212-r: the earlier record flagged "ask for a refund" as unsupported. The fakechecks page does say "Ask them if they can refund your money." The record now flags only the "tell the bank" clause, and drops a required action that is not on the cited page.
- tr217-c: the earlier record flagged "Scammers use fear to cloud judgment" as unsupported. The page says a scammer's power "lies solely in his or her ability to create fear as a means of impairing judgement." Only the names/hearing-times conclusion is flagged now.
- tr217-e: the earlier source flag is removed. The page says scammers use "specific names and designated court hearing times." The record now flags the repeated steps 3 and 4.
- tr215-e: the reasons no longer claim step 4 says to delete right away. The reply says "report ... then delete it", which matches the page.
- tr212-e: the earlier fix suggested a new sentence the page does not support. The fix now uses the page's own sentence: "Even if you see the funds in your account, that doesn't mean it's a good check."
- tr216-r and tr217-r: second sources were fetched and confirmed. The bank-statement wording was narrowed to "withdrawals you did not make", which the identity-theft page supports.

## Most common problems
1. Unsupported "do not reply" instruction (tr218-a, tr218-f, tr218-r). The blackmail page only says to stop, not pay, and delete the message.
2. Dropped "generally" qualifier on the debt collector rule (tr214-f, tr214-g). The page says "Generally, a debt collector can't discuss your debt with anyone but you or your spouse."
3. Conditional source step applied unconditionally (tr218-r). The page's password change applies only if the email includes a password; this user's email does not.
4. Failure-recovery replies missing the step that fixes the problem (tr216-r: identity-theft steps after SSN exposure; tr217-r: contact the wire transfer company after wiring money). Second sources added in the fixes.
5. Unsupported search suggestion in the toll reply (tr215-e, also safety fail): "A quick search on your phone is fine."
6. Plain-language and repetition issues (tr212-e, tr213-r, tr217-e).

## Source pages
All 7 pages were fetched and read. None were unreadable. Targeted follow-up fetches were run for each claim not in the first summary: fakechecks (bank workers, uspis.gov/report, refund), home improvement (contract items, permits, deed, certified mail), debt collection (certified mail, CFPB URL, "generally"), blackmail (replying, data breach, rush), uscourts (names and hearing times, never threatens, fine in open court), tolls (search, replying, reporting address).

## Notes
- No example has `reviewed: true`. No example was marked reject.
- Accepted as reassurance, not flagged: "Do not pay" before validation (debt collection pages, protective and not contrary to the page); "close the door" and "tell him you will think about it" (conduct, not a fact claim); "data breach" used without a definition.
- Records for the 36 examples from the earlier run were kept and re-checked, not rewritten from scratch, except where the corrections above apply.
