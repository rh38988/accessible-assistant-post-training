# Revision list: batch fx1b, after review round 1 (1 examples)

Edit ONLY these examples in data/v2/specs/fx1b.py, then rebuild.

## tr009-e
- reasons: Reply has no branch for the common case where other devices work and only the iPhone fails (Airplane Mode off, Connectivity Assist off, uninstall VPN or security software, restart, test), none of which loses saved passwords. Also one claim not on the page.
- fix requested: Delete 'If they can, the router is working.' Reword step 1 to 'See if other devices on the same network can get online.' Add a short branch: if only the iPhone has trouble, open Settings, tap Wi-Fi, check that Airplane Mode is off and Connectivity Assist is off, and if a VPN or security app is installed, uninstall it, restart the iPhone, and test again (if they need the app, contact whoever manages the VPN or the app maker). Keep the Reset Network Settings warning. Source: https://support.apple.com/en-euro/111786 items on Airplane Mode, Connectivity Assist, VPN and security software, router, outage.
- unsupported claims: 'If they can, the router is working.' -> inference not on the page; the page only says to test other devices and that if they also fail there may be an outage.
- required actions missing from the reply: If only this iPhone fails, check non-destructive iPhone causes (Airplane Mode, Connectivity Assist, VPN or security software)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-euro/111786
