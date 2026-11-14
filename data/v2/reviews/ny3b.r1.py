def R(id, ra, covered=None, nc=False, src="pass", saf="pass", dup="pass", unsup=None,
      steps=2, ask=2, con=2, act=2, plain=2, real=2, dec="keep", reasons="", fix=""):
    return {
        "id": id,
        "required_actions": ra,
        "covered": covered if covered is not None else [True] * len(ra),
        "needs_clarification": nc,
        "gates": {"source": src, "safety": saf, "duplicate": dup},
        "unsupported_claims": unsup or [],
        "scores": {"steps": steps, "ask_or_answer": ask, "constraints": con,
                   "actionable": act, "plain": plain, "realistic_user": real},
        "decision": dec, "reasons": reasons, "fix": fix,
    }

BT = ["Swipe down from the top of the screen (critical)",
      "Touch and hold the Bluetooth icon (critical)",
      "Tap Pair new device (critical)",
      "Tap the name of the device (critical)",
      "Follow the on-screen instructions (critical)"]
BR = ["Find the device under Available devices, or tap More icon then Refresh if Pair new device is missing"]
BT_PASS = BT + ["If asked for a passcode and none is known, try 0000 or 1234"]
CLAR = dict(ra=[], covered=[], nc=True, steps="NA")

def clar(id):
    return R(id, [], [], True, steps="NA")

BR_ = ["Open Settings (critical)", "Tap Display & touch (critical)",
       "Tap Brightness level, use Advanced for more settings (critical)", "Drag the slider (critical)"]
DT = ["Open the Clock app (critical)", "Tap More, then Settings (critical)",
      "Tap Change date and time (critical)", "Turn on Automatic date and time (critical)"]
DTZ = ["Open the Clock app (critical)", "Tap More, then Settings (critical)",
       "Tap Change date and time (critical)", "Under Time zone, turn on Automatic time zone (critical)",
       "Only some devices support Automatic time zone"]
DTM = ["Tap Change date and time", "Tap Time zone", "If Set automatically is present, turn it off",
       "Tap Time zone and select your zone (critical)"]
HS = ["Swipe up from the bottom of the Home screen to open apps (critical)",
      "Touch and drag the app; Home screen thumbnails appear (critical)",
      "Slide to the spot, lift finger (critical)"]
HM = ["Touch and drag the app; thumbnails appear (critical)", "Slide to new position (critical)", "Lift finger (critical)"]
TP = ["Open Settings", "Tap Google, then All services", "Under Personal & device safety, tap Theft protection"]
WF = ["Open Settings (critical)", "Tap Network & internet, SIMs, Carrier SIM, Wi-Fi calling (critical)",
      "Turn on Wi-Fi calling (critical)"]

REVIEWS = [
 R("tr154-a", BT + BR[:0] + ["If Pair new device is missing: Available devices or More then Refresh"]),
 R("tr154-c", BT_PASS),
 clar("tr154-b"),
 R("tr154-d", BT + ["If Pair new device is missing: Available devices or More then Refresh"]),
 R("tr154-e", BT + ["If Bluetooth is off in Airplane mode, turn Airplane mode off first"],
   src="fail",
   unsup=["'If the Bluetooth icon is off, tap it once to turn Bluetooth on.' -> the page only says to touch and hold the Bluetooth icon; it never says a single tap turns Bluetooth on."],
   dec="revise", reasons="Unsupported claim about tapping the icon once; contradicts the touch-and-hold step as written on the page.",
   fix="Delete the sentence 'If the Bluetooth icon is off, tap it once to turn Bluetooth on.' Keep only the Airplane mode note, e.g. 'Bluetooth is off while Airplane mode is on, so turn Airplane mode off before you pair.'"),
 R("tr154-r", BR + ["Tap the device name and follow the on-screen instructions"]),
 R("tr155-a", BR_),
 R("tr155-c", BR_),
 clar("tr155-b"),
 R("tr155-d", BR_),
 R("tr155-e", BR_ + ["Adaptive brightness is on by default, adjusts to surrounding light, manual change still possible"]),
 R("tr155-r", ["Tap Advanced on Display & touch to see more settings (critical)", "Tap Brightness level (critical)", "Drag the slider (critical)"]),
 R("tr156-a", DT),
 R("tr156-c", DTZ),
 clar("tr156-b"),
 R("tr156-d", DT),
 R("tr156-e", DTM + ["Open Clock, More, Settings first"]),
 R("tr156-r", DTM),
 R("tr157-a", HS),
 R("tr157-c", HM + ["Android 14 and up note"]),
 clar("tr157-b"),
 R("tr157-d", HS),
 R("tr157-e", HS + ["Remove takes app off Home screen only; Uninstall takes it off the device"]),
 R("tr157-r", HM),
 R("tr158-a", TP + ["Turn on Theft Detection Lock (critical)", "Screen lock required; grayed out means unsupported"]),
 R("tr158-c", TP + ["Turn on Offline Device Lock (critical)", "Phone must be unlocked when it goes offline", "Screen lock required"]),
 clar("tr158-b"),
 R("tr158-d", TP + ["Turn on Theft Detection Lock (critical)", "Screen lock required"]),
 R("tr158-e", TP + ["Tap Remote Lock", "Turn on Remote lock (critical)", "If number not verified: Verify number, then Automatically verify phone numbers",
                    "Later lock: android.com/lock, enter phone number, complete reCaptcha, request lock"],
   plain=1, act=1,
   unsup=[],
   dec="revise",
   reasons="The android.com/lock instructions are packed into one run-on sentence with four separate actions (S4), and 'reCAPTCHA' is unexplained jargon for this audience (S5). Content matches the page.",
   fix="Rewrite the last paragraph as a short numbered list: 'To lock the phone later, use your laptop: 1. Go to android.com/lock. 2. Enter your phone number. 3. Complete the security check (reCaptcha) that appears. 4. Request the lock. The phone screen locks shortly after.' Do not add any description of what the reCaptcha looks like beyond what the page says."),
 R("tr158-r", ["Grayed-out Theft Detection Lock means the device does not support it"]),
 R("tr159-a", WF + ["Notification screen shows Internet Call or Wi-Fi calling", "If option missing, carrier does not support it"]),
 R("tr159-c", WF + ["May be extra charges; ask mobile provider", "If option missing, carrier does not support it"]),
 clar("tr159-b"),
 R("tr159-d", WF + ["If option missing, carrier does not support it"]),
 R("tr159-e", WF + ["Some carriers allow Wi-Fi calling without a service plan; otherwise a carrier is needed", "If option missing, carrier does not support it"],
   covered=[True, True, True, False, True], steps=1, dec="revise",
   reasons="The page says some carriers allow Wi-Fi calling without service, 'otherwise, you need a carrier for this to work'. The reply gives only the hopeful half, so a user with no plan is not told it may not work at all.",
   fix="After 'Some carriers let you use Wi-Fi calling without a mobile service plan.' add 'If yours does not, you need a mobile service plan for calls to work.' Keep the final line 'If you don't see Wi-Fi calling, your carrier doesn't support it,' and add 'Ask your carrier to confirm.'"),
 R("tr159-r", ["If Wi-Fi calling does not appear, carrier does not support it; check with carrier"]),
]
