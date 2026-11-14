# Revision list: batch ny2a, after review round 1 (13 examples)

Edit ONLY these examples in data/v2/specs/ny2a.py, then rebuild.

## tr134-a
- reasons: Fetch New Data (Settings > Apps > Mail > Mail Accounts > Fetch New Data) is missing. The single 'stop when your email works' list of 9 steps mixes checks with a destructive account removal; step 5 is a worry rather than an action, and Delete Account is presented as just another step in the middle of a flat list. Page warns downloaded emails might be removed. Too long and risky for a low-confidence user.
- fix requested: Rewrite as two short groups. Group 1 (try first, stop when it works): internet; provider status page or contact provider; sign in to provider website to check address and password; ask provider about two-step verification / special password; Settings > Apps > Mail > Mail Accounts > Fetch New Data, choose Automatically or Manually or a schedule. Group 2, clearly labeled 'last resort, only if nothing above works': warn that removing the account can delete emails already saved on the phone, so first sign in to the provider website on a computer and confirm all email is there or saved elsewhere; then Settings > Apps > Mail > Mail Accounts > tap the account > Delete Account; then add the account again. Keep 'If that does not help, contact your email provider.'
- required actions missing from the reply: Settings > Apps > Mail > Mail Accounts > Fetch New Data, choose a setting (critical for not receiving)
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102578

## tr134-d
- reasons: For mail not coming in, the page also says to sign in to the provider website to check address and password; this is missing. Step 6 'Choose a setting such as Automatically or Manually, or pick a schedule' gives no clear choice for a user whose mail is not arriving. The closing note about charging and Wi-Fi is supported (iOS 11 and later) and useful.
- fix requested: Add a step after the outage check: 'In a web browser, sign in to your provider's website to confirm your email address and password.' Change the last step to name one concrete choice, e.g. 'Tap **Automatically** (or **Manually**, or pick a schedule)' and tell the user what they will see: the chosen option is shown with a check. If you cannot support the check mark, only say 'tap the one you want'. Keep the Automatically note.
- required actions missing from the reply: Sign in to the provider's website to check email address and password | Ask provider about two-step verification or other security, may need special password
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102578

## tr134-e
- reasons: Reply keeps the constraint (no account deletion) and is supported, but omits Settings > Apps > Mail > Mail Accounts > Fetch New Data, a check the user can do themselves without deleting anything and that bears on 'gets nothing new'.
- fix requested: Add after step 2: 'Open **Settings**, then tap **Apps**. Tap **Mail**, then **Mail Accounts**, then **Fetch New Data**. Choose **Automatically**, **Manually**, or a schedule.' Renumber. Keep the closing note about deletion.
- required actions missing from the reply: Settings > Apps > Mail > Mail Accounts > Fetch New Data, choose a setting (critical for not receiving)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102578

## tr135-c
- reasons: 'Make sure your iPhone has enough storage' gives no way to do it and no starting point (the page gives none either). The user also says received pictures do not show up, and the page's carrier check (ask the carrier whether it supports MMS) is missing. 'Turn on Send Photo Previews or Low Quality Image Mode' leaves the user to guess which one.
- fix requested: Keep steps 2 and 3. Reword step 4 to 'Look for **Send Photo Previews** or **Low Quality Image Mode** and turn on whichever one you see.' Change step 1 into a plain sentence in the lead-in ('Pictures need free space on the iPhone, so delete things you no longer need if it is full') only if you can support it; otherwise keep it as 'Make sure your iPhone has enough storage to receive pictures and videos.' Add a last line: 'If pictures still will not go through, ask your carrier whether it supports MMS (picture messages) for your plan.'
- required actions missing from the reply: Ask carrier whether it supports MMS (attachment size limits)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118433

## tr135-e
- reasons: 'The only other choice' is wrong per the page; restart and correct-contact-number checks (no charge) are omitted, which matter for this user. 'Contact your carrier' for an iMessage failure: page says contact Apple Support for iMessage and carrier for SMS/MMS.
- fix requested: Replace the closing paragraph: add two steps after Try Again, 'Restart your iPhone.' and 'Check that your neighbor's phone number or email address is correct in the contact.' Then say 'If it still will not send, **Send as Text Message** is another option, but messaging rates may apply. If you do not want that, contact Apple Support for blue-bubble (iMessage) problems.' Remove 'the only other choice' and 'contact your carrier'.
- unsupported claims: 'the only other choice is Send as Text Message' -> page also lists restarting the iPhone and confirming the contact's phone number or email; contacting the carrier is for SMS/MMS, and Apple Support is the page's contact for iMessage
- required actions missing from the reply: Restart iPhone | Confirm correct number/email for the contact
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118433

## tr136-a
- reasons: Step 6 'Update your iPhone to the latest iOS' has no starting point, and the step list puts the update after a phone call to the carrier. Page order: Airplane Mode, restart, contact carrier, update iOS, so order is fine, but a low-confidence user needs the path.
- fix requested: Expand step 6 using the second official page https://support.apple.com/en-us/118575 : 'Plug in your iPhone and connect to Wi-Fi. Open **Settings**, tap **General**, tap **Software Update**. If an update is available, tap **Download and Install** and follow the instructions on the screen.' Keep the rest. Optionally also add the page's carrier settings step (connect to Wi-Fi, Settings > General > About, update carrier settings if offered).
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120000

## tr136-d
- reasons: The SOS explanation and the emergency-call countries are supported. Missing the page's 'Update iOS to the latest version' action; also no mention that the first three steps go in this order and what to do if still SOS.
- fix requested: Add a step 5: 'If it still says SOS, update your iPhone: plug it in and connect to Wi-Fi, open **Settings**, tap **General**, tap **Software Update**, and if an update is shown tap **Download and Install**.' Add https://support.apple.com/en-us/118575 as a second source for this step.
- required actions missing from the reply: Update to the latest iOS
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120000

## tr136-e
- reasons: Update iOS is omitted (the user's 'download' may be that update). Turning on Airplane Mode can interrupt the Wi-Fi download the user is waiting on, and the reply does not warn about that or put the Wi-Fi-based carrier settings check first. Step 4 does not tell the user what they see if no update appears.
- fix requested: Put the Wi-Fi step first: connect to Wi-Fi, Settings > General > About, if an update is offered tap to update carrier settings. Then Airplane Mode (add: 'this may pause your download, so you may prefer to do it after the download finishes'). Then carrier. Add the iOS update step with the Settings > General > Software Update > Download and Install path from https://support.apple.com/en-us/118575 as second source. Add 'If no update shows, nothing more to do here' for step 4.
- required actions missing from the reply: Update iOS
- low scores: {'steps': 1, 'constraints': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120000

## tr136-r
- reasons: 'Update your iPhone to the latest iOS' has no path; carrier settings update is missing; last step loops back to the carrier instead of the page's hardware/service step.
- fix requested: Step 2: add path 'Plug in and connect to Wi-Fi, open Settings > General > Software Update, tap Download and Install' (second source https://support.apple.com/en-us/118575). Add a step for carrier settings (Wi-Fi, Settings > General > About, update if offered). Replace step 3 with 'If your carrier says your account and network are fine and you think the phone itself has a problem, get service from Apple.'
- unsupported claims: 'If you still see No Service after that, contact your carrier again.' -> page sends the user to Apple service when the carrier confirms account and network are fine and a hardware problem is suspected
- required actions missing from the reply: Check carrier settings update (Wi-Fi, General > About) | If carrier confirms all fine and hardware is suspected, get service from Apple
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120000

## tr138-e
- reasons: The honest opening is good. But 'Let it cool down before you use it again' collides with the user waiting for a call, and the emergency-calls sentence answers a different question (making, not receiving, calls).
- fix requested: Keep the opening and step 1. Replace step 2 and the last paragraph with: 'While the warning is showing, Apple says to let the iPhone cool down before using it, so I cannot promise it will work for your call. If the call is important, it may be safer to turn it off and let it cool, or ask the hospital for another number to call.' Remove the emergency-calls sentence (or say plainly it is about making emergency calls only).
- unsupported claims: 'An iPhone showing the warning screen might still be able to make emergency calls.' -> page-supported, but irrelevant to an incoming hospital call and may mislead the user into thinking the phone can still receive it
- required actions missing from the reply: Turn off the iPhone (page step; user declines)
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118431

## tr139-a
- reasons: Page lists installing the latest software updates before turning on Set Time Automatically, and restarting if a message says updated time zone information is available; both are missing.
- fix requested: Add after step 1: 'Install the latest iPhone update if one is waiting (Settings > General > Software Update > Download and Install; second source https://support.apple.com/en-us/118575).' Add after the Set Time Automatically step: 'If a message says updated time zone information is available, restart your iPhone.'
- required actions missing from the reply: Install latest software updates | If message says updated time zone info available, restart iPhone
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101619

## tr139-d
- reasons: Missing the page's step to install the latest software updates; the user's problem is both date and time wrong, and the Setting Time Zone location step is also omitted (non-critical).
- fix requested: Add after step 1: 'Install the latest iPhone update if one is waiting (Settings > General > Software Update > Download and Install; second source https://support.apple.com/en-us/118575).' Optionally add the Privacy & Security > Location Services > System Services > Setting Time Zone step.
- required actions missing from the reply: Install latest software updates | Settings > Privacy & Security > Location Services > System Services > Setting Time Zone on
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101619

## tr139-r
- reasons: Reasons are supported, but the reply ends with no action: the user is left with a list of causes and no next step.
- fix requested: After each reason add a short action the page supports in spirit: Screen Time passcode, ask the person who set it up (or enter the Screen Time passcode if you know it); work profile, ask your workplace's IT help; carrier/country, you cannot turn it on, set the time by hand instead (Settings > General > Date & Time, if the Set Automatically switch is not locked, turn it off, then Time Zone or tap the date). Keep it short and do not add steps the page does not give.
- required actions missing from the reply: Give a next action for each reason
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101619
