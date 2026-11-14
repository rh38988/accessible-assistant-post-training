# Revision list: batch fx3, after review round 2 (1 examples)

Edit ONLY these examples in data/v2/specs/fx3.py, then rebuild.

## tr041-e
- reasons: User said his regular phone is off so he cannot be reached; step 2 only says to use a known number, which does not help here and gives no alternative. The FTC family-emergency page says to try another family member or his friends. Gift card keep-advice is slightly misworded.
- fix requested: In step 2 after 'Reach your nephew through a number you already know is his', add: 'If his phone stays off, ask another family member or his friends to check on him.' (source: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes). In the last paragraph replace 'Keep a copy of the gift card and the store receipt.' with 'Keep the card and the store receipt, and take photos of both.'
- unsupported claims: "Keep a copy of the gift card and the store receipt" -> page says keep the card itself and the store receipt (and take photos of both), not 'a copy'
- required actions missing from the reply: Hang up/stop; verify by contacting the nephew directly (known number); if unreachable, try another family member or his friends | If already paid: contact the gift card company, ask for money back, keep the card and store receipt
- low scores: {'steps': 1, 'constraints': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams
