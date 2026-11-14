# Revision list: batch ny4b, after review round 2 (3 examples)

Edit ONLY these examples in data/v2/specs/ny4b.py, then rebuild.

## tr169-c
- reasons: The source's open-network section warns that information on the network is available to other people. The user is at a coffee shop and says they have never done this before, and the reply does not mention it.
- fix requested: Add one sentence after step 5 in the final reply, for example: 'No password is needed, but other people on that network can see your information.' Source wording: 'your information is available to other people on that network' (open network section of https://support.google.com/chromebook/answer/1047420?hl=en). Keep every other line unchanged.
- required actions missing from the reply: Warn that on an open network your information is available to other people on that network (non-critical, safety-relevant for this user)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr169-r
- reasons: Step 4 says only 'Enter the network information'. The user said the network name is hidden and that they know the name and password, and the reply never says to type them. The source says only that the box asks for network information and does not list its fields, so the step should use the user's own information rather than describe fields.
- fix requested: Replace step 4 with: '4. In the box that appears, type the network name and the password you already know.' Do not name any field or label beyond these. Keep steps 1 to 3 and 5 to 6 and the Wi-Fi-off line unchanged. Source for the path: 'select Add connection, then Add Wi-Fi. Enter the network information in the box that appears, then select Connect' (https://support.google.com/chromebook/answer/1047420?hl=en).
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr170-r
- reasons: Two source problems: the phone or mobile data condition is widened, and the reset sentence turns 'can reset without deleting personal files' into a guarantee that every reset keeps personal files. Both affect what a user will believe about their files. All required actions are present and the steps match the source otherwise.
- fix requested: (1) Replace the bullet 'If you ever use your phone's connection, switch to Wi-Fi or Ethernet instead.' with: 'If you have trouble with your phone or mobile data connection while updating, disconnect it and connect to Wi-Fi or Ethernet instead.' (2) Replace the sentence 'A reset does not delete your personal files.' with: 'You can reset your Chromebook without deleting your personal files.' Keep the rest of the reply unchanged. Source: https://support.google.com/chromebook/answer/177889?hl=en, section 'System update doesn't download'.
- unsupported claims: 'If you ever use your phone's connection, switch to Wi-Fi or Ethernet instead.' -> the source's condition is trouble with the phone or mobile data during the update, not any use of it | 'A reset does not delete your personal files.' -> the source says 'You can reset your Chromebook without deleting your personal files'; the reply turns a possible option into a flat guarantee about every reset
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/177889?hl=en
