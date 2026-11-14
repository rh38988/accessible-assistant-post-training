# ny2b revise2

Revision list: data/v2/reviews/input/ny2b.revise2.md (built with review_io.py todo ny2b 2; 3 examples).
Fixed (3): tr141-e, tr142-c, tr143-r.
Cannot fix: none.
Follow-ups touched: none.

Page checks (WebFetch of each cited source before editing):
- tr141-e: Apple voicemail page (en-kz, check-voicemail-iph3c99490e) confirms the first tap on Voicemail asks for a voicemail password and greeting, with "Set Up Now" as the first step. Added one closing paragraph for a helper to set up voicemail, as the reviewer requested. Second source (Turn on and activate Siri) already listed.
- tr142-c: Apple call forwarding page (en-ca, iph7405291c4) needed a second fetch to reach the section. It says call forwarding works on a GSM network and that a CDMA user should contact the carrier for setup information. Replaced the GSM/CDMA sentence with a plain sentence asking the carrier for setup information. Steps unchanged.
- tr143-r: Apple LED Flash page (en-us, 111774) says the flash works only when the device is locked. It does not mention the screen going dark or any way to lock the phone. Changed step 1 to "Put the phone down and lock it." with no lock button named.

Page vs reviewer: no contradictions. The page gives no lock-method instructions, so the reviewer's "lock it" wording was used without naming a button.

Builder: python3 data/v2/tools/build_v2.py ny2b printed OK (36 examples, 6 tasks).

Note: one unrelated sports-scores tool call was made by mistake during this run. Its output was not used and it changed nothing.
