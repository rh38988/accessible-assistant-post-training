# Revision list: batch fx1b, after review round 2 (1 examples)

Edit ONLY these examples in data/v2/specs/fx1b.py, then rebuild.

## tr009-e
- reasons: Skips the page's first check (Settings > Wi-Fi, Wi-Fi on, blue checkmark next to the network), so the reply never gives a clear starting point or tells the user what they should see. Step 3 'Tap Wi-Fi' is also a separate action inside a step about Connectivity Assist. Constraint (no Reset Network Settings) is handled correctly.
- fix requested: Insert a new first step: 'Open **Settings**, then tap **Wi-Fi**. Make sure Wi-Fi is on and your network has a blue checkmark next to its name.' Then step 2 Airplane Mode (return to **Settings**), step 3 'In the **Wi-Fi** settings, make sure **Connectivity Assist** is off. If it looks dimmed, restart your iPhone.' Keep the remaining steps and the Reset Network Settings warning unchanged.
- required actions missing from the reply: Open Settings > Wi-Fi: make sure Wi-Fi is on and the network shows a blue checkmark
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-euro/111786
