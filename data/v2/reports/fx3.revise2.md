# fx3 revise2

Revision list: data/v2/reviews/input/fx3.revise2.md (1 example, built with review_io.py todo fx3 2).

Fixed:
- tr041-e (gift card scam, constraint): added the fallback when the nephew's phone stays off ("If his phone stays off, ask another family member or his friends to check on him."), supported by the FTC alert "Scammers use AI to enhance their family emergency schemes" ("If you can't reach your loved one, try to get in touch with them through another family member or their friends."). Added that alert as a second source in the example's "sources" list (original FTC article kept first).

Page vs reviewer:
- The reviewer asked to replace "Keep a copy of the gift card and the store receipt" with "Keep the card and the store receipt, and take photos of both." The FTC article does not say that. It says "Keep a copy of the gift card and your store receipt" and "Take a picture of the gift card and store receipt with your phone." I kept the page's wording and added "by taking a picture of each with your phone."
- Required action "hang up / stop" is covered by "Don't reply" (the scam came by text). No other required action was missing after the fallback and photo sentence were added.

Cannot fix: none.
Follow-ups touched: none.
Not changed: task-level source_notes for TR-041 (only one example uses it). Builder warnings on tr038-e and tr038-r (web address check) are on examples not in this list, so left alone.
Builder: OK.
