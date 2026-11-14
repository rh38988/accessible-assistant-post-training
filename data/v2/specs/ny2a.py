TASKS = [
    {
        "task_id": "TR-134",
        "task_type": "email_not_working",
        "task": "Cannot send or receive email in the Mail app",
        "platform": "iPhone",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Apple Support: If you can't receive email on your iPhone or iPad (send steps from Apple Support: If you can't send email on your iPhone or iPad, support.apple.com/en-us/102556)", "url": "https://support.apple.com/en-us/102578"},
        "source_notes": """Before you begin: mail settings are backed up in iCloud, emails are not. Changing or deleting an account can remove previously downloaded emails from the device. Confirm the device is connected to the internet. Check the email provider for a service outage.
Check your email address and password: 1 Sign in to your email provider's website to confirm address and password. 2 If Mail still shows a username or password error, contact your email provider or system administrator.
Fetch New Data: Settings, tap Apps, Mail, Mail Accounts, Fetch New Data, choose a setting such as Automatically or Manually, or choose a schedule. Notes: if Push is not offered for the account it defaults to Fetch. On iOS 11 and later, Automatically is the default; the device fetches new data in the background only when charging and connected to Wi-Fi.
Contact provider or admin: check provider status page or contact them for outage; ask whether security features such as two-step verification are enabled, you may need a special password or authorization from the provider to send and receive mail on the device; confirm account settings.
Remove account and add again: 1 On a computer sign in to the provider's website, make sure all your email is there or saved somewhere other than the device. 2 On device Settings, tap Apps, Mail, Mail Accounts. 3 Tap the account, tap Delete Account. 4 Add the account again. If these do not work, contact your email provider.
SEND page (102556): Check Outbox: if you see a message that your email was not sent it is in the Outbox. 1 In Mail go to your list of mailboxes. 2 Tap Outbox. If there is no Outbox, your email was sent. 3 Tap the email and confirm the recipient's address is correct. 4 Tap Send. Also same password / provider / remove account steps.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "The Mail app on my iPhone will not send or get any email. What should I do?",
                 """Try these in order and stop when your email works.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider if two-step verification is turned on. You may need a special password from them to use email on your iPhone.
5. Make sure all your email is on the provider's website, because deleting the account can remove emails saved on the phone.
6. Open **Settings**, then tap **Apps**.
7. Tap **Mail**, then tap **Mail Accounts**.
8. Tap your account, then tap **Delete Account**.
9. Add the account again.

If that does not help, contact your email provider.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I wrote my daughter a long note about Thursday's dinner on my iPhone, in the Mail app, and it keeps saying it was not sent. She says she never got it. I'm not very good with this. Is there somewhere the note might be waiting?",
                 """Yes, an email that did not go out waits in the Outbox.

1. Open **Mail** and go to your list of mailboxes.
2. Tap **Outbox**. If there is no Outbox, your email was sent.
3. Tap the email.
4. Check that your daughter's address is correct.
5. Tap **Send**.

If it still will not send, make sure your iPhone is connected to the internet, and check with your email provider to see if it has an outage.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my email is not working, can you help me",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my email is not working, can you help me",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. Nothing new is coming in.",
                 """Let's check these in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. Open **Settings**, then tap **Apps**.
4. Tap **Mail**, then tap **Mail Accounts**.
5. Tap **Fetch New Data**.
6. Choose a setting such as **Automatically** or **Manually**, or pick a schedule.

With **Automatically**, the iPhone fetches new mail in the background only when it is charging and on Wi-Fi.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "On my iPhone, the Mail app gets nothing new and my sent emails fail. I have years of old emails stored on this phone and I do not want to delete my account and lose them. What can I check instead?",
                 """You can check these without deleting anything. Try them in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider if two-step verification or other security features are on. You may need a special password from them to use email on your iPhone.
5. Ask your provider to confirm that your account settings are correct.

Deleting the account is the last step on the list, and it can remove emails already downloaded to the phone, so you can leave it alone for now.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "email on my iphone stopped coming in. nothing new since yesterday. it is the Mail app",
                 """Let's check these in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Open **Settings**, tap **Apps**, then tap **Mail**.
5. Tap **Mail Accounts**, then tap **Fetch New Data**.
6. Choose a setting such as **Automatically** or **Manually**, or pick a schedule.""",
                 "I signed in on the website and my password works fine there. But the Mail app on the phone still says my password is wrong.",
                 """Then the provider needs to look at it.

1. Contact your email provider or system administrator about the user name or password error.
2. Ask them if two-step verification or other security features are on. You may need a special password or authorization from them to use email on your iPhone.
3. Ask them to confirm your account settings are correct.""",
             ]},
        ],
    },
    {
        "task_id": "TR-135",
        "task_type": "messages_not_sending",
        "task": "Text messages will not send or arrive",
        "platform": "iPhone",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Apple Support: If you can't send or receive messages on your iPhone or iPad", "url": "https://support.apple.com/en-us/118433"},
        "source_notes": """Red exclamation point with Not Delivered: 1 Check your network connection. 2 Tap the red exclamation point, then tap Try Again. 3 If the message still will not send, tap the red exclamation point, then tap Send as Text Message. Messaging rates may apply. iMessage (blue bubbles) is sent over Wi-Fi or cellular data to iPhone, iPad, iPod touch or Mac. RCS, SMS, MMS (green bubbles) require a text-messaging plan. To fall back to SMS automatically when iMessage is unavailable: Settings > Apps > Messages, turn on Send as Text Message. If still Not Delivered after sending as text, contact your carrier.
Receiving on one device but not another (iPhone and iPad): Settings > Apps > Messages > Send & Receive, choose your phone number or email address. If your phone number does not appear, link your iPhone number to your Apple Account or set up Text Message Forwarding.
Photos or videos will not send: 1 Make sure the device has enough storage to receive images and videos. 2 For SMS/MMS carriers may limit attachment sizes: Settings > Apps > Messages, turn on Send Photo Previews or Low Quality Image Mode.
Other steps: restart iPhone; check connection (iMessage, RCS, MMS need cellular data or Wi-Fi; SMS needs cellular network unless Wi-Fi Calling is on); confirm with carrier that the message type (RCS, MMS, SMS) is supported; verify the contact's phone number or email address; if problems continue contact Apple Support or carrier.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone text will not send. There is a little red circle with an exclamation point next to it. What do I do?",
                 """That red mark means the message was not delivered. Try this.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.
3. If it still will not send, tap the red exclamation point again.
4. Tap **Send as Text Message**. Messaging rates may apply.

If it still says Not Delivered after that, contact your carrier.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an iPhone and I like to send pictures of the grandkids to my family in a text. Lately the pictures will not go through, and a few I was sent do not show up either. I am not sure what to touch. Can you walk me through it?",
                 """Let's try these.

1. Make sure your iPhone has enough storage to receive pictures and videos.
2. Open **Settings**, then tap **Apps**.
3. Tap **Messages**.
4. Turn on **Send Photo Previews** or **Low Quality Image Mode**.

Some carriers limit the size of attachments on regular text messages, and these settings help with that.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my texts are not working right, can you help",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my texts are not working right, can you help",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. I get my messages on my iPad but not on the iPhone.",
                 """Let's check where your iPhone receives messages.

1. Open **Settings**, then tap **Apps**.
2. Tap **Messages**, then tap **Send & Receive**.
3. Choose your phone number or email address.

If your phone number does not appear, link your iPhone number to your Apple Account, or set up Text Message Forwarding.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone shows Not Delivered under my message to my neighbor, with a red exclamation point. I do not want to be charged for sending a regular text message. What can I try?",
                 """You can try this without sending a regular text.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.

A blue bubble message goes over Wi-Fi or cellular data, so it does not need a text-messaging plan.

If it still will not send, the only other choice is **Send as Text Message**, and messaging rates may apply. If you would rather not use it, contact your carrier.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my iphone says Not Delivered under the text i sent my son. there is a red exclamation point",
                 """Try this.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.
3. If it still will not send, tap the red exclamation point again.
4. Tap **Send as Text Message**. Messaging rates may apply.""",
                 "I did both of those and it still says Not Delivered.",
                 """Here is what to try next.

1. Restart your iPhone.
2. Check that your son's phone number or email address is correct in the contact.
3. Make sure your iPhone has Wi-Fi or cellular data.
4. If it still fails, contact your carrier.""",
             ]},
        ],
    },
    {
        "task_id": "TR-136",
        "task_type": "no_service",
        "task": "Phone shows No Service or SOS",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: If you see SOS, No Service, or Searching on your iPhone or iPad", "url": "https://support.apple.com/en-us/120000"},
        "source_notes": """Status bar: SOS or SOS only means the device cannot reach your cellular network but can still make emergency calls through other carrier networks (available in Australia, Canada and the United States). No Service or Searching means the device is not connected to a cellular network.
Step 1 Reconnect (only if your cellular network is available): open Settings, turn on Airplane Mode for at least 15 seconds, turn off Airplane Mode.
Step 2 Restart the iPhone.
Step 3 Contact your carrier: ask them to verify account is active and in good standing; confirm you are in a coverage area with no outages; confirm device is not blocked or barred and has the correct data plan; tell you whether local government requires IMEI registration for an iPhone bought outside your country. Only your carrier can manage account details.
Step 4 Update to the latest iOS.
Step 5 Carrier settings update: connect to Wi-Fi, Settings, General, About. If an update is available you will see an option to update your carrier settings. If you insert a new SIM, download carrier settings for the new carrier.
Step 6 Dual SIM: Settings, Cellular, tap the cellular line, check if it is on; if off tap Turn On This Line, then check for service. If you do not see your line, contact carrier to set up eSIM or insert a physical SIM. Physical SIM: remove and reinsert it. Damaged or transferred SIM: ask carrier for new one.
Step 7 Traveling internationally: Settings, tap Cellular or Cellular Data. Single SIM or eSIM: turn on Cellular Data, tap Cellular Data Options. Dual SIM: turn on Cellular Data, tap the number, tap Cellular Data Options. Turn on Data Roaming.
Step 8 3G network: iPhone 6 or later: update iOS, Settings, Cellular, Cellular Data Options, turn on Enable LTE. If still No Service contact carrier. Step 9: if hardware problem suspected after carrier confirms no account or network issue, may need Apple service.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone says No Service at the top of the screen and I cannot make calls. What do I do?",
                 """Try these in order and stop when your bars come back.

1. Open **Settings**.
2. Turn on **Airplane Mode** and wait at least 15 seconds.
3. Turn **Airplane Mode** off.
4. Restart your iPhone.
5. Contact your carrier. Ask them to check that your account is active, that you are in a coverage area with no outage, and that your device is not blocked and has the correct data plan.
6. Update your iPhone to the latest iOS.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "We flew to Spain for my sister's wedding and as soon as we landed my iPhone started saying No Service. I only have the one SIM, nothing fancy, and I did not change any settings before we left. My husband says there is a roaming switch somewhere. Where is it?",
                 """Yes, the roaming switch is in your Cellular settings.

1. Open **Settings**.
2. Tap **Cellular** (it may say **Cellular Data**).
3. Turn on **Cellular Data**.
4. Tap **Cellular Data Options**.
5. Turn on **Data Roaming**.

If you still see No Service, turn **Airplane Mode** on for at least 15 seconds and then off, restart your iPhone, and contact your carrier.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone says no service. help!",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my phone says no service. help!",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. It says SOS in the corner.",
                 """SOS means your iPhone cannot reach your cellular network. In Australia, Canada, and the United States it can still make emergency calls through other carrier networks.

To get your service back:

1. Open **Settings**.
2. Turn on **Airplane Mode** for at least 15 seconds, then turn it off.
3. Restart your iPhone.
4. Contact your carrier to check your account and coverage.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone says No Service. I am waiting on a download and I do not want to restart the phone right now. I do have Wi-Fi at home. What else can I try?",
                 """You can try these without restarting.

1. Open **Settings**.
2. Turn on **Airplane Mode** and wait at least 15 seconds, then turn it off.
3. With Wi-Fi connected, tap **General**, then tap **About**.
4. If an update is available, you will see an option to update your carrier settings. Tap it.
5. If you still see No Service, contact your carrier to check your account, coverage, and that your device is not blocked.

You can restart the iPhone later if you need to.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "iphone says No Service since this morning. what should i do",
                 """Try these first.

1. Open **Settings**.
2. Turn on **Airplane Mode** for at least 15 seconds, then turn it off.
3. Restart your iPhone.""",
                 "I did the airplane mode and restarted it. Still No Service.",
                 """The next step is your carrier.

1. Contact your carrier. Ask them to verify that your account is active and in good standing, that you are in a coverage area with no outages, and that your device is not blocked and has the correct data plan.
2. Update your iPhone to the latest iOS.
3. If you still see No Service after that, contact your carrier again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-137",
        "task_type": "touchscreen_unresponsive",
        "task": "The screen is too sensitive or only responds to touch some of the time",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: If the screen isn't working on your iPhone or iPad", "url": "https://support.apple.com/en-us/102567"},
        "source_notes": """The page covers only: If your screen is too sensitive or responds intermittently to touch. Steps: 1 Restart your iPhone or iPad (page links to restart articles, no restart method on this page). 2 Make sure that your screen is clean and free of any debris or water. 3 Disconnect any Lightning or USB-C accessories. If your screen works after removing an accessory, try using a different outlet, cable, or charger. 4 Remove any cases or screen protectors. If the problem continues, if the screen still does not work, you may need to arrange service for the device through Apple. The page has no section on a screen that does not respond at all, no force restart, no model conditions.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "The screen on my iPhone only works some of the time when I touch it. What can I do?",
                 """Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug anything connected to the charging port, such as a cable or other accessory.
4. Take off any case or screen protector.

If the screen still does not work after that, you may need to arrange service for your iPhone with Apple.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone has gone strange. Sometimes it acts like I am touching the screen when I am not, and the letters jump around when I type an email. It has a clear case on it and I usually leave it plugged in by my bed. I have an iPhone. Where do I start?",
                 """That sounds like the screen is too sensitive. Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug the charging cable and any other accessory connected to the charging port.
4. If the screen works after unplugging, try a different outlet, cable, or charger.
5. Take off the case and any screen protector.

If the screen still does not work, you may need to arrange service for your iPhone with Apple.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone screen is acting up when i touch it",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my phone screen is acting up when i touch it",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. It only answers my touch every now and then.",
                 """Let's go through these in order.

1. Restart your iPhone.
2. Wipe the screen so it is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.
4. Remove any case or screen protector.

If it still does not respond, you may need to arrange service for your iPhone with Apple.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone screen only reacts to my finger some of the time. I just paid to have a screen protector put on and I really do not want to take it off. What else can I try first?",
                 """You can try these first.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.

If the screen still acts up, the next step is removing any case or screen protector. If you would rather keep it on, the other option is to arrange service for your iPhone with Apple.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my iphone screen keeps jumping around and only works sometimes. what do i do",
                 """Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.
4. Take off any case or screen protector.""",
                 "When I unplugged the charger the screen worked fine. But it starts jumping again when I plug it back in.",
                 """That points to the charger, not the screen.

1. Try a different outlet.
2. Try a different cable.
3. Try a different charger.

If the screen still does not work, you may need to arrange service for your iPhone with Apple.""",
             ]},
        ],
    },
    {
        "task_id": "TR-138",
        "task_type": "overheating",
        "task": "The phone is too hot or shows a temperature warning",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: If your iPhone or iPad gets too hot or too cold", "url": "https://support.apple.com/en-us/118431"},
        "source_notes": """Temperature warning screen appears when the device passes a certain temperature threshold. An iPhone showing this screen might still be able to make emergency calls. Steps for the warning: 1 Turn off the device. 2 Move it to a cooler place, away from direct sunlight. 3 Let it cool down before using it again.
Use in ambient 0 to 35 C (32 to 95 F). Storage -20 to 45 C (-4 to 113 F); do not leave in a car. Very hot conditions can permanently shorten battery life.
Normal warmth: first setup, restore from backup, major software updates, wireless charging, graphics or processor intensive use (including camera apps), high-quality video streaming. It cools when the activity finishes. If no temperature warning appears you can keep using it.
Avoid: leaving in a car on a hot day; direct sunlight for long periods; GPS navigation, graphics-heavy games or the camera for long periods in heat or direct sun.
When too hot: charging slows or stops including wireless; display dims or goes black; cellular signal may weaken; camera flash or features may be disabled; some apps slower. During navigation an alert "Temperature: iPhone needs to cool down." appears and the display turns off; spoken turn-by-turn directions continue and the display lights up near a turn.
Lock Screen "Charging On Hold": charging resumes when the device returns to normal temperature. "Restore Paused": if it overheats during an iCloud restore, the restore pauses and resumes once it cools down.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone got really hot and a screen came up with a temperature warning. What should I do?",
                 """Do this to let it cool safely.

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

An iPhone showing this warning screen might still be able to make emergency calls.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "We were driving to my cousin's house on a sunny afternoon with my iPhone on the dashboard using the maps, and the screen suddenly went black and said Temperature: iPhone needs to cool down. I was scared it broke. It is an iPhone. Is it ruined?",
                 """It is not broken. The iPhone got too hot in the sun and turned the screen off to cool down. The spoken directions keep going, and the screen lights up near a turn.

To cool it down:

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

Long use of GPS navigation in heat or direct sun can cause this, and leaving the phone in a car on a hot day should be avoided.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone is burning hot, what do i do",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my phone is burning hot, what do i do",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. It feels hot while it charges and I do not see any warning.",
                 """An iPhone can feel warm during wireless charging, setup, a restore from backup, a big software update, camera use, or video streaming. It cools down when that activity ends. If no temperature warning appears, you can keep using it.

If a temperature warning does appear:

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone is showing a temperature warning, but I am waiting on an important call from the hospital and I do not want to turn it off. Is there another way to cool it down?",
                 """The usual steps for a temperature warning start with turning the iPhone off, and I cannot offer another way to cool it. The closest option is this:

1. Move your iPhone to a cooler place, away from direct sunlight.
2. Let it cool down before you use it again.

An iPhone showing the warning screen might still be able to make emergency calls.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my iphone is too hot and shows a temperature warning, what do i do",
                 """Do this.

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.""",
                 "It cooled down, but now when I plug it in the Lock Screen says Charging On Hold.",
                 """That message is expected after it got hot.

1. Keep your iPhone in a cooler place, away from direct sunlight.
2. Wait for it to return to normal temperature.

Charging resumes when the iPhone is back to normal temperature.""",
             ]},
        ],
    },
    {
        "task_id": "TR-139",
        "task_type": "date_time",
        "task": "Fix the wrong date or time",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: If you can't change the time or time zone on your Apple device", "url": "https://support.apple.com/en-us/101619"},
        "source_notes": """Automatic (iPhone): 1 Connect to the internet. 2 Install the latest software update. 3 Open Settings, tap General, tap Date & Time, turn on Set Time Automatically (page wording; sets date and time from your time zone). If the setting is dimmed see notes. 4 If a message says updated time zone information is available, restart the iPhone (and any paired Apple Watch). 5 Open Settings, tap Privacy & Security, tap Location Services, scroll to the bottom, tap System Services, turn on Setting Time Zone; the iPhone uses its current location to determine the time zone.
Manual (if iPhone still shows the wrong date, time or time zone): 1 Open Settings, tap General, tap Date & Time, turn off Set Automatically (page wording in the manual step; the automatic step calls the same switch Set Time Automatically). 2 To change the time zone tap Time Zone and enter a city in the zone you need. To change the date or time, tap the date and set it manually.
Notes: the on/off option may be unavailable with some carriers or in some countries and regions. It may be dimmed if the iPhone has a Screen Time passcode or a corporate profile with device restrictions. If the time is wrong after syncing with a Mac check the Mac's date and time settings. Apple advises against changing time settings manually to affect app behavior such as game timers.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "The time on my iPhone is wrong. How do I get it to fix itself?",
                 """Let your iPhone set the time on its own.

1. Make sure your iPhone is connected to the internet.
2. Open **Settings**, then tap **General**.
3. Tap **Date & Time**.
4. Turn on **Set Time Automatically**.

If the time zone is still wrong, let the iPhone use your location for it:

1. Open **Settings**, then tap **Privacy & Security**.
2. Tap **Location Services**, then scroll to the bottom and tap **System Services**.
3. Turn on **Setting Time Zone**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I moved from the East Coast to the West Coast to be near my kids and my iPhone still shows the old time zone, so I keep missing my appointments. I do not want the automatic thing, I just want to pick the time zone myself. It is an iPhone.",
                 """You can choose it yourself.

1. Open **Settings**, then tap **General**.
2. Tap **Date & Time**.
3. Turn off **Set Automatically**.
4. Tap **Time Zone**.
5. Type a city in the time zone you need and tap it.

To change the date or time instead, tap the date and set it by hand.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "everything on my phone shows the wrong day and hour lately, can you help me fix it",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "everything on my phone shows the wrong day and hour lately, can you help me fix it",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. The date and time are both off.",
                 """Let's turn on automatic time.

1. Make sure your iPhone is connected to the internet.
2. Open **Settings**, then tap **General**.
3. Tap **Date & Time**.
4. Turn on **Set Time Automatically**.

If a message says updated time zone information is available, restart your iPhone.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone shows the wrong time. I do not have Wi-Fi or any data right now because I am out at the lake, so the automatic setting will not work. Can I fix it by hand?",
                 """Yes, you can set it by hand.

1. Open **Settings**, then tap **General**.
2. Tap **Date & Time**.
3. Turn off **Set Automatically**.
4. To change the time zone, tap **Time Zone** and enter a city in the zone you need.
5. To change the date or time, tap the date and set it.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my iphone shows the wrong time. how do i fix it",
                 """Try this.

1. Make sure your iPhone is connected to the internet.
2. Open **Settings**, then tap **General**.
3. Tap **Date & Time**.
4. Turn on **Set Time Automatically**.""",
                 "The switch is gray and I cannot turn it on.",
                 """A gray switch means the setting is dimmed. It can happen for a few reasons.

1. Someone may have set a Screen Time passcode on this iPhone.
2. The iPhone may have a work profile with device restrictions.
3. With some carriers, or in some countries and regions, the option is not available.""",
             ]},
        ],
    },
    {
        "task_id": "TR-140",
        "task_type": "brightness",
        "task": "Make the screen brighter or dimmer",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Adjust the brightness and color temperature on your iPhone or iPad", "url": "https://support.apple.com/en-us/109351"},
        "source_notes": """Control Center: on iPhone X or later swipe down from the top-right corner of the screen; on iPhone 8 or earlier swipe up from the bottom edge. Drag the brightness bar up or down.
Settings: open Settings, tap Display & Brightness, drag the slider right or left.
Auto-Brightness (on by default, ambient light sensor raises brightness in bright conditions and lowers it in dark): open Settings, tap Accessibility, tap Display & Text Size, scroll to Auto-Brightness and tap to turn it on or off. If screen brightness does not adapt correctly, turn auto-brightness off, then back on.
Other: Dark Mode, True Tone, Night Shift in Display & Brightness. Brightness affects battery life. If the device gets too warm, the display may dim and maximum brightness is reduced until it cools down.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I can barely read my iPhone in the kitchen, the screen looks so dim. Can I turn it up somehow?",
                 """You can change it in Settings.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Drag the slider to the right to make the screen brighter.

Drag it to the left to make the screen dimmer.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an old iPhone 7 that my son gave me. It is too bright at night and hurts my eyes when I read in bed. He said there is a quick way to dim it without going into the Settings, but I forgot what he showed me.",
                 """Yes, use Control Center. On an iPhone 7 it works like this.

1. Swipe up from the bottom edge of the screen.
2. Drag the brightness bar down to make the screen dimmer.

Drag the bar up to make the screen brighter.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my screen is too dark and i cannot see anything",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my screen is too dark and i cannot see anything",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone. I want a quick way to change it.",
                 """Use Control Center.

1. On an iPhone X or later, swipe down from the top-right corner of the screen. On an iPhone 8 or earlier, swipe up from the bottom edge.
2. Drag the brightness bar up to make the screen brighter.

Drag the bar down to make it dimmer.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone keeps changing how bright the screen is by itself, and I want it to stay exactly where I put it. How do I stop that, and then how do I set it myself?",
                 """First turn off Auto-Brightness.

1. Open **Settings**, then tap **Accessibility**.
2. Tap **Display & Text Size**.
3. Scroll to **Auto-Brightness** and tap it to turn it off.

Now set the brightness yourself.

1. Go back to **Settings** and tap **Display & Brightness**.
2. Drag the slider right for brighter or left for dimmer.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "how do i make my iphone screen brighter",
                 """Here is how.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Drag the slider to the right.""",
                 "I dragged it all the way to the right and the screen still looks dim. The phone feels warm too.",
                 """The warmth is likely the reason.

1. If your iPhone is too warm, the display may dim and its top brightness is lowered until it cools down. Let it cool.
2. If it is not warm and the brightness still looks wrong, open **Settings** and tap **Accessibility**.
3. Tap **Display & Text Size**, then scroll to **Auto-Brightness**.
4. Turn it off, then turn it back on.""",
             ]},
        ],
    },
]
