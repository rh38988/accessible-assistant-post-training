"""fx2: new examples to bring TR-014..TR-031 (group ex2) to six each."""
TASKS = [
    {
        "task_id": "TR-014", "task_type": "family_emergency_scam", "task": "Caller claims to be grandchild needing gift cards",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC: Talking Turkey (family emergency scams)", "url": "https://www.ftc.gov/node/54353"},
        "source_notes": """Family emergency scam ("grandparent scam"). Signs: caller impersonates a family member; urgent plea for emergency cash (medical care, bail, escape a dangerous situation); stock lines like "I know I don't sound like myself, Grandpa." and "Don't tell Mom. Let's keep this our secret."; a fake doctor, lawyer or police officer is involved; insists on money right away.
What to do: resist the urge to act immediately, no matter how dramatic; take time to check whether there is really an emergency; check the story with another trusted family member, even if the caller asks you to keep it confidential; call the relative at a number you know is genuine before taking any action.
Do not wire money, pay with a gift card, or send cash in response to an emergency request. Insistence on immediate payment is a warning sign. Agree within your family that no one will ever call with an emergency request for wired money, gift card payment, or cash.
Report to the FTC at www.ftc.gov/complaint. The page has NO advice for people who already paid and no phone numbers.""",
        "examples": [
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """I got a Facebook message from someone who says she is my granddaughter Emily. She wrote that she is stuck in another country, lost her bag, and needs me to wire her money today or she can't get home. The picture looks like her but the writing sounds a bit odd. I want to help her but I'm not sure. What should I do?""",
                 """I'm glad you stopped to ask. **Please don't wire any money yet.** Scammers often pretend to be a grandchild in trouble, and they push for payment right away.

1. Take a breath. You don't have to act right now, even if the story sounds dramatic.
2. Call Emily on a phone number **you know is really hers**. Don't use any number from the message.
3. Check the story with another trusted family member too.
4. Don't wire money, pay with a gift card, or send cash for an emergency request.

You can report the message at **www.ftc.gov/complaint**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """A man called saying he is my grandson Kevin and he was in a car accident. He said a lawyer will call me for the bail money, and he begged me not to tell his parents because they'd be so angry. His mother is traveling and I can't reach her right now. He says there's no time. Should I do what he asks?""",
                 """**Please don't send any money yet.** A caller who begs for secrecy and says there is no time is a common sign of a family emergency scam. A fake lawyer is another sign.

1. Hang up and take your time. There is no need to rush.
2. Call Kevin on a number **you know is genuine**.
3. If you can't reach his mother, check the story with **another trusted family member**, even though the caller asked you to keep it secret.
4. Don't wire money, pay with a gift card, or send cash.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """Oh no. I think I got scammed. A woman said my grandson was in jail and I mailed $1,500 cash to an address she gave me. Now I called my grandson's real number and he is fine. What do I do now?""",
                 """I'm sorry this happened. It is not your fault, and you did the right thing by calling your grandson.

1. **Don't send any more money**, even if the caller contacts you again.
2. Tell another trusted family member what happened so you have support.
3. Report it to the FTC at **www.ftc.gov/complaint**.

I don't have steps for getting the cash back. Reporting helps. Agree with your family that no one will ever call with an emergency request for wired money, gift cards, or cash.""",
             ]},
            {"suffix": "f", "scenario": "helper", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """My mother is 84 and just told me someone called saying he was her grandson and needed money fast for bail. She hasn't sent anything but she is shaken. How can I help her?""",
                 """It's good she told you before sending anything. Here is how to help her.

1. Reassure her. These calls are built to make people panic, and the caller pushes for money right away.
2. Help her call her grandson on a number you know is genuine.
3. Check the story with another trusted family member, even if the caller asked for secrecy.
4. Remind her not to wire money, pay with a gift card, or send cash for an emergency request.
5. Report the call at **www.ftc.gov/complaint**.

It also helps to agree as a family that no one will ever call with an emergency request for wired money, gift card payment, or cash.""",
             ]},
            {"suffix": "g", "scenario": "prevention", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "My friend was just fooled by a call from a fake grandchild. How can I tell if a call like that is a scam in the future?",
                 """Here are the signs of this kind of scam:

1. The caller says they are a family member in an emergency, such as needing bail or medical care.
2. They say things like "I know I don't sound like myself" or "Don't tell Mom. Let's keep this our secret."
3. A doctor, lawyer, or police officer may be part of the story.
4. They want money **right away**, by wire, gift card, or cash.

What to do if it happens:
1. Don't act right away, however dramatic the story is.
2. Call your relative on a number you know is genuine.
3. Check with another trusted family member.

Agree with your family that no one will ever call with an emergency request for wired money, gift cards, or cash. You can report scams at **www.ftc.gov/complaint**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-015", "task_type": "verification_code_scam", "task": "Stranger asks for a verification code",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Verification code scams", "url": "https://consumer.ftc.gov/node/84809"},
        "source_notes": """Scammers try to trick you into sharing your verification code so they can get into your account. They pose as someone you trust and claim a problem with one of your accounts or identity theft; they may know details about you and seem sympathetic before asking for the code. With the code they can log in and move money out of savings or investment accounts.
What to do: if someone asks for your code, don't engage. Hang up, block the number, and stop texting them. Report to the FTC at ReportFraud.ftc.gov. If worried about your account, contact your bank, credit union, or investment advisor directly using a number you trust, like the one on your statement or in your app. Never use the number the caller gave you; it will take you to the scammer.
Prevention: never give your verification code to someone else. Anyone who asks you for your account verification code is a scammer.
Already shared a code: the page has no specific steps; closest guidance is to contact your bank, credit union or investment advisor directly using a trusted number. No phone numbers listed.""",
        "examples": [
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """A woman phoned me saying she works in the fraud department at my bank and that someone is trying to take money out of my account. She was very polite and said she would text me a code to stop it, and I just need to read the code back to her. I'm worried about my savings. Is this real?""",
                 """**Please don't read her the code.** This is a known scam. Scammers pretend to be someone you trust and claim there is a problem with your account. With the code, they can log in and move your money.

1. Hang up. Don't argue with her.
2. Block the number.
3. If you're worried about your account, contact your bank directly. Use a number you trust, like the one on your statement or in your app. Don't use any number the caller gave you.
4. Report the call at **ReportFraud.ftc.gov**.

Remember that anyone who asks for your verification code is a scammer.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """A man keeps calling and texting me. He already knows my full name and the town I live in, and he sounds very kind. He says someone stole my identity and he'll help me fix it, but first I must tell him the code that was just texted to my phone. He knows so much about me that it must be real, right?""",
                 """**Please don't tell him the code.** Scammers often know details about you and sound sympathetic. That is part of how they earn your trust. Anyone who asks you for your verification code is a scammer.

1. Don't engage. Hang up and stop texting him.
2. Block his number.
3. If you're worried about your accounts, contact your bank, credit union, or investment advisor directly. Use a number you trust, such as the one on your statement or in your app.
4. Report him at **ReportFraud.ftc.gov**.

Never call back a number he gave you.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """I already read a code to a man who said he was from my credit union. Right after, I got a bad feeling. What should I do?""",
                 """I'm sorry, and thank you for acting quickly. With a code, a scammer may be able to log in to your account, so contact your credit union right away.

1. Call your credit union directly. Use a number you trust, like the one on your statement or in your app.
2. Don't call back any number the man gave you. It would take you to the scammer.
3. Don't talk to him or text him again, and block his number.
4. Report it at **ReportFraud.ftc.gov**.

I don't have more specific steps than these, so your credit union is the best place to ask what else to do.""",
             ]},
            {"suffix": "f", "scenario": "helper", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """My dad is 79 and keeps getting texts and calls from people who say there is a problem with his accounts and ask for a code that gets sent to his phone. What should I tell him to do?""",
                 """It's good you're looking out for him. Here is what to tell him.

1. **Never give a verification code to anyone.** Anyone who asks for it is a scammer.
2. If someone asks, don't engage. Hang up, block the number, and stop texting.
3. If he is worried about an account, he should contact his bank, credit union, or investment advisor directly, using a number he trusts, like the one on his statement or in his app.
4. He should never use a number the caller gave him.
5. You can report the contacts at **ReportFraud.ftc.gov**.

If he already shared a code, he should contact his bank or credit union right away using a trusted number.""",
             ]},
            {"suffix": "g", "scenario": "prevention", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "How do these verification code scams work, and how can I stay safe from them?",
                 """Here is how they work. Scammers pretend to be someone you trust and say there is a problem with an account or that your identity was stolen. They may know details about you and sound sympathetic. Then they ask for your verification code. With it, they can log in to your account and move money out of savings or investment accounts.

How to stay safe:

1. **Never give your verification code to anyone.**
2. Remember that anyone who asks for it is a scammer.
3. If someone asks, hang up, block the number, and stop texting.
4. If you're worried, contact your bank directly using a number on your statement or in your app.
5. Report it at **ReportFraud.ftc.gov**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-016", "task_type": "online_payment_safety", "task": "Is it safe to pay online?",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Alert: A way to spot scams: how someone asks you to pay", "url": "https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay"},
        "source_notes": """If someone says the ONLY way to pay is bank transfer, wire transfer, cryptocurrency, payment app, or gift card, it is probably a scam. "Never send money to anyone who says you can only pay with a specific payment method, no matter what reason they give you."
Advice: check the person or company: search online for the name plus words like "review," "scam," or "complaint" and see what others say. Pay by credit card whenever possible (more protections, lets you dispute charges).
If you already paid a scammer: act fast. Contact the company you used to send the money right away, tell them it was fraud, and ask whether they can stop or reverse the transaction and return your money. For credit card payments, you can also dispute the charges. No method-specific steps beyond that.
Report at ReportFraud.ftc.gov. More advice: ftc.gov/scams. No phone numbers.""",
        "examples": [
            {"suffix": "d", "scenario": "followup", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "is it safe to pay for something online?",
                 """It can be, but it depends on what you're buying, who you're buying from, and how they want you to be paid.

**What are you trying to buy, and how is the seller asking you to pay** (for example a credit card, a gift card, or a bank transfer)?

One quick tip while you check: if a seller says you can only pay with **gift cards, a wire transfer, or cryptocurrency**, stop. That's a common sign of a scam.""",
                 "I'm buying a used lawn mower from a man on a website and he says I have to pay with a gift card.",
                 """**Please don't pay with a gift card.** When someone says gift card is the only way to pay, that is a sign of a scam. The same goes for a bank transfer, wire transfer, cryptocurrency, or a payment app.

1. Don't send money to anyone who says you can only pay one specific way, whatever reason they give.
2. Search online for the seller's name with words like "review," "scam," or "complaint" and see what others say.
3. If you decide to buy, pay by **credit card** whenever possible. It has more protections and lets you dispute charges.

You can report a seller like this at **ReportFraud.ftc.gov**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """I found a beautiful rocking chair on a website I've never heard of, and the price is half what stores charge. They only accept cryptocurrency and say it's because of fees. My nephew says no but I really want it. Is it safe to pay them that way?""",
                 """**Please don't pay with cryptocurrency.** When a seller says that is the only way to pay, it is probably a scam, whatever reason they give.

1. Don't send money to anyone who says you can only pay one specific way.
2. Search online for the website's name with words like "review," "scam," or "complaint."
3. If the seller accepts a **credit card**, that is safer. Credit cards have more protections and let you dispute charges.

Your nephew is right to be careful. If you want to report the website, you can do that at **ReportFraud.ftc.gov**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """I don't have a credit card, only a debit card and some cash. A person selling concert tickets online says they only take a payment app like Zelle, and that tickets are going fast. Is that okay? I really can't use a credit card.""",
                 """**Please don't pay this seller with Zelle.** A seller who says you can only pay with a payment app is probably a scammer.

1. Don't send money to anyone who says you can only pay one specific way, whatever reason they give.
2. Search online for the seller's name with words like "review," "scam," or "complaint."
3. The FTC suggests a credit card when possible because it lets you dispute charges. Since you can't use one, the safe choice is to skip a seller who insists on a payment app.

You can report the seller at **ReportFraud.ftc.gov**. For more tips, you can visit **ftc.gov/scams**.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "messages": [
                 """I already paid. A seller told me to wire money for a puppy and now they've stopped answering. What can I do?""",
                 """I'm sorry. Act quickly, because the sooner you do, the better.

1. Contact the company you used to send the wire right away.
2. Tell them it was fraud.
3. Ask whether they can stop or reverse the transaction and return your money.
4. Report the seller at **ReportFraud.ftc.gov**.

I don't have steps that are specific to wire transfers beyond these.""",
             ]},
            {"suffix": "g", "scenario": "prevention", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "What are the warning signs that someone is trying to scam me when I buy things online?",
                 """The biggest warning sign is how they ask you to pay.

1. If someone says the **only** way to pay is a bank transfer, wire transfer, cryptocurrency, payment app, or gift card, it is probably a scam.
2. Never send money to anyone who says you can only pay one specific way, whatever reason they give.
3. Check the seller. Search online for the name with words like "review," "scam," or "complaint."
4. Pay by **credit card** whenever possible. It has more protections and lets you dispute charges.

If you already paid a scammer, contact the company you used to send the money right away, tell them it was fraud, and ask if they can stop or reverse it. You can report scams at **ReportFraud.ftc.gov**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-021", "task_type": "text_size", "task": "Make text bigger",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: Change the font size on your iPhone, iPad, and iPod touch", "url": "https://support.apple.com/en-us/102453"},
        "source_notes": """Standard size: Settings > Display & Brightness > Text Size, drag the slider to the size you want.
Larger sizes: Settings > Accessibility > Display & Text Size > tap Larger Text to see larger options, drag the slider.
Applies to apps that support Dynamic Type (Mail, Contacts, Calendar, Phone, Notes). Making text too large might make it hard to tap buttons in some apps. If text becomes hard to use, return to the same settings and adjust. Page does not cover Bold Text, Control Center, or per-app text size.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """I already made the text bigger on my iPhone using the slider in Display & Brightness, but my eyes are bad and it still isn't big enough. That slider is at the end. Is there any way to get the words even larger?""",
                 """Yes, there is a separate setting for larger sizes.

1. Open the **Settings** app.
2. Tap **Accessibility**.
3. Tap **Display & Text Size**.
4. Tap **Larger Text**.
5. Drag the slider to the size you want.

The larger sizes work in apps like Mail, Contacts, Calendar, Phone, and Notes. Very large text can make some buttons hard to tap. If that happens, come back to the same screen and slide it down a little.""",
             ]},
        ],
    },
    {
        "task_id": "TR-022", "task_type": "text_size", "task": "Make text bigger",
        "platform": "Android (Pixel)", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Accessibility Help: Change text & display settings", "url": "https://support.google.com/accessibility/android/answer/11183305?hl=en"},
        "source_notes": """Font size (Settings): open Settings, search for and select Font size, move the slider left or right. A preview of the new size appears after you set the slider. Tap Reset settings to return to the device default.
Display size: Settings, search Display size, slider, same preview and Reset settings.
Quick Settings: swipe down from top of screen to open Quick Settings, tap Font Size, tap Increase or Decrease or drag the percentage slider. Font size can go up to 200%. Changing font size in Settings adds the Font Size tile to Quick Settings automatically; otherwise add the tile first (no steps given).
Bold text: Settings > Accessibility > Display size and text > Bold text on/off (some apps ignore it).
Font size setting does not apply to some apps. Some steps need Android 13 or later.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 """I have a Pixel phone and I like to change the text size depending on whether I'm wearing my glasses. I don't want to dig through Settings every single time. Is there a quicker way to switch the size?""",
                 """Yes. Once it is set up, the quick way is the top of the screen. Set it up first in Settings.

1. Open the **Settings** app.
2. Search for **Font size** and tap it.
3. Move the slider once. This adds a **Font Size** tile to Quick Settings.

From then on:

1. Swipe down from the top of the screen to open Quick Settings.
2. Tap **Font Size**.
3. Tap **Increase** or **Decrease**, or drag the percentage slider.

Font size can go up to 200%.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "My Pixel's text is too small to read. How do I make it bigger?",
                 """You can make it bigger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** and tap it.
3. Move the slider toward the larger end.

You will see a preview of the new size. A few apps ignore this setting, so text in them may stay the same.""",
                 "I slid it all the way and now it is way too big and I can't even read the screen. How do I go back?",
                 """You can put it back to the way it was.

1. Open **Settings**.
2. Search for **Font size** and tap it.
3. Tap **Reset settings** to return to the phone's default size.

Or move the slider back toward the smaller end a little at a time until it is comfortable.""",
             ]},
        ],
    },
    {
        "task_id": "TR-024", "task_type": "ring_volume", "task": "Turn up ringer volume",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: Use the volume buttons, side button, and other controls on your iPhone", "url": "https://support.apple.com/en-us/105103"},
        "source_notes": """Volume buttons control media volume when listening to music, watching videos, or playing games. "When you're not using other apps, the buttons will adjust the ringer volume."
Ring/Silent switch: on iPhone 8 and earlier, iPhone 15 and earlier (except 15 Pro) and 16e/17e, the Ring/Silent switch toggles Silent mode. When the switch shows orange, the iPhone is in Silent mode and vibrates for calls and alerts. Calls from favorite contacts still ring in Silent mode and clock alarms still sound. On iPhone 15 Pro, 16 and later (Camera Control), the Action button toggles Silent mode by default.
Settings > Sounds & Haptics has Fixed Position Volume Controls. The alarms page (118444) says the Sounds & Haptics slider under Ringtone and Alerts is framed as ALARM volume, with Change with Buttons toggle. So the existing examples that call that slider the ringer volume are not supported.
Not covered: Control Center volume.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """Every time I press the volume up button on my iPhone it only makes my YouTube videos louder, not the phone ringing. I'm usually watching videos when my daughter calls. I want the ringer louder, not the videos. How do I do that?""",
                 """That happens because the volume buttons change **media volume** while you are watching videos, listening to music, or playing games. They change the ringer volume only when you aren't using other apps.

1. Close the video app and go to your Home Screen, so no other app is in use.
2. Press the **volume up** button a few times.

Now the buttons raise the ringer volume. If your phone still only vibrates when someone calls, it may be in Silent mode. Tell me and I'll show you how to check.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Can you tell me how to make my iPhone ringer louder?",
                 """Yes, you can use the volume buttons. It takes a few seconds.

1. Go to your Home Screen so you are not inside another app.
2. Press the **volume up** button on the side of the phone a few times.

When no other app is in use, these buttons change the ringer volume. If your phone only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.""",
                 "I did that but it still only buzzes when someone calls. I see something orange on the side of the phone.",
                 """The orange means your iPhone is in **Silent mode**. In Silent mode it vibrates for calls instead of ringing.

1. Find the **Ring/Silent switch**, where you see the orange.
2. Flip it so the orange is no longer showing.
3. Press the **volume up** button a few times.""",
             ]},
        ],
    },
    {
        "task_id": "TR-025", "task_type": "ring_volume", "task": "Turn up ring volume",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Help: Change volume, sound & vibrate settings", "url": "https://support.google.com/android/answer/9082609?hl=en"},
        "source_notes": """Press a volume button, tap the Menu icon at the right (opens the full panel), slide each level: Media volume, Call volume, Ring Volume, Notification volume, Alarm volume. If you don't find Settings, use older Android steps. On older Android versions, tap the Down arrow instead, then pick Media, Ring, or Alarm (choose Ring to adjust ring volume).
Vibrate/silent: press a volume button, tap the Ring icon above the slider, tap Vibrate or Mute; to restore sound turn off Vibrate or turn on Ring.
To silence an incoming call's ring press a volume button. Some steps need Android 12 or later. Note: the page says "Menu icon", not "More icon" as in existing tr025-a.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 """My Android phone is quite old and I can't update it. When I press the volume button I only see a little slider with a small arrow, no menu thing. How do I make the ring louder on an older phone like that?""",
                 """On older Android phones you use the small arrow.

1. Press a **volume button** on the side of the phone.
2. At the right, tap the **Down arrow**.
3. Find **Ring** in the list.
4. Slide the **Ring** level to where you want it.

The Down arrow is where older versions show Media, Ring, and Alarm.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Please show me how to make my Android phone ring louder.",
                 """You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button** on the side of the phone.
2. Tap the **Menu** icon on the right side of the volume panel.
3. Find the **Ring Volume** slider and slide it to the right.

If you don't see the **Menu** icon, tell me what you see and I'll help you find it.""",
                 "I pressed the button but there is no menu icon. I only see a small arrow pointing down.",
                 """That's normal on older Android versions. Use the arrow instead.

1. Press a **volume button** again.
2. At the right, tap the **Down arrow**.
3. Choose **Ring**.
4. Slide the **Ring** level to where you want it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-026", "task_type": "wifi_calling", "task": "Turn on Wi-Fi Calling",
        "platform": "iPhone", "category": "communication", "sensitive": False,
        "source": {"title": "Apple Support: Make a call with Wi-Fi Calling", "url": "https://support.apple.com/en-us/108066"},
        "source_notes": """Turn on: Settings > Cellular. If your iPhone has multiple SIMs, select the line you want to use. Tap Wi-Fi Calling, turn on "Wi-Fi Calling on This iPhone". Tap Enable. You may need to enter or confirm your emergency address.
When Wi-Fi Calling is available, the status bar shows "Wi-Fi" while viewing Control Center and calls use Wi-Fi Calling.
Carrier must offer Wi-Fi Calling; devices need latest software; some Wi-Fi networks don't work with it.
Troubleshooting: if you can't turn on or use Wi-Fi Calling, first confirm your carrier offers it and your software is current. If it continues, contact your carrier. If the carrier can't resolve it, try these, waiting two minutes between each: Settings > Cellular (select line), Wi-Fi Calling confirm on, restart iPhone, connect to a different Wi-Fi network, turn Wi-Fi Calling off then on, Settings > General > Transfer or Reset iPhone > Reset > Reset Network Settings.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 """My iPhone has two phone lines, my personal number and a work number. The signal is bad at my desk, but I only want Wi-Fi Calling for my work line. How do I turn it on for just that one?""",
                 """When you have two lines, you pick the line first.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Select your **work line**.
4. Tap **Wi-Fi Calling**.
5. Turn on **Wi-Fi Calling on This iPhone**.
6. Tap **Enable**.

You may be asked to enter or confirm your address for emergency services. Wi-Fi Calling also needs your carrier to offer it.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I want my iPhone to use my home Wi-Fi for phone calls because the signal here is poor. How do I set that up?",
                 """You can turn on **Wi-Fi Calling**. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable**.

You may be asked to enter or confirm an address for emergency services. Your carrier must offer Wi-Fi Calling.""",
                 "I tried but I can't get it to turn on.",
                 """Let's try these in order.

1. Make sure your carrier offers Wi-Fi Calling. The carrier can confirm this.
2. Make sure your iPhone has the latest software.
3. Open **Settings**, tap **Cellular**, tap **Wi-Fi Calling**, and make sure **Wi-Fi Calling on This iPhone** is on.
4. Restart your iPhone.
5. Connect to a different Wi-Fi network, because some networks don't work with Wi-Fi Calling.
6. Turn Wi-Fi Calling off, then on again.
7. Open **Settings**, tap **General**, tap **Transfer or Reset iPhone**, tap **Reset**, then tap **Reset Network Settings**.

Wait about two minutes between steps. If it still won't turn on, contact your carrier.""",
             ]},
        ],
    },
    {
        "task_id": "TR-027", "task_type": "screenshot", "task": "Take a screenshot",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Help: Take a screenshot or record your screen", "url": "https://support.google.com/android/answer/9075928?hl=en"},
        "source_notes": """Open the screen, press Power and Volume down at the same time. If that doesn't work, press and hold Power for a few seconds, then tap Screenshot. If neither works, check the phone maker's support site. You see a preview at the bottom left; on some phones an indicator appears at the top.
Find screenshots: Photos app > Collections > On this device > Screenshots; Share or Edit icons. If no Photos app (older Android), open Gallery > Album view > Screenshots folder.
Scrolling screenshot: Android 12+, after Power + Volume down tap Capture more.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 """I have arthritis in my hands and I can't press two buttons at the same time on my Android phone. My daughter asked me to send her a picture of an error message. Is there another way to take a screenshot?""",
                 """Yes, you can do it with one button.

1. Open the screen you want to capture.
2. Press and hold the **Power** button for a few seconds.
3. Tap **Screenshot**.

You will see a small preview at the bottom left of the screen. If **Screenshot** doesn't appear, check your phone maker's support site.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "What's the way to take a screenshot on an Android phone?",
                 """Here is how.

1. Open the screen you want to capture.
2. Press the **Power** button and the **Volume down** button at the same time.

You will see a small preview at the bottom left of the screen. If that doesn't work, press and hold **Power** for a few seconds, then tap **Screenshot**.""",
                 "I think it worked because I saw a little picture, but now where do I find it?",
                 """Your screenshots are saved in the Photos app.

1. Open the **Photos** app.
2. At the bottom, tap **Collections**.
3. Tap **On this device**, then tap **Screenshots**.
4. Tap the screenshot, then tap the **Share** icon to send it.

If you don't have a Photos app, open the **Gallery** app, tap **Album view**, then open the **Screenshots** folder.""",
             ]},
        ],
    },
    {
        "task_id": "TR-028", "task_type": "screenshot", "task": "Take a screenshot",
        "platform": "Windows 11", "category": "technical_support", "sensitive": False,
        "source": {"title": "Microsoft Support: Use Snipping Tool to capture screenshots", "url": "https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots"},
        "source_notes": """Open: select Start, type snipping tool, select Snipping Tool. Shortcuts: Windows logo key + Shift + S opens the overlay for an image snip; Print Screen (PrtSc) captures the entire screen as a static image onto the clipboard.
Modes: select Snipping Mode, choose a mode, then select New: Rectangle (drag a rectangular area), Window (select a window), Full screen (captures whole screen immediately), Freeform.
Saving: snips save automatically to the Screenshots folder; to change it select See More then Settings. For an extra copy select Save as, pick location and name, Save. Ctrl + C copies a snip. To share: See More > Share. No troubleshooting section.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I'm on a Windows 11 computer and want to send my doctor's office a picture of just one box on a web page. I don't want the whole screen, because my email inbox is open too and I don't want them to see it. How can I capture only that box?""",
                 """You can use **Snipping Tool** to capture just one part of the screen.

1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
2. Select **Snipping Mode**, then choose **Rectangle**.
3. Select **New**.
4. Drag a rectangle around the box you want.

The snip saves automatically to your **Screenshots** folder. A faster way next time is to press the **Windows logo key + Shift + S**, which opens the snip overlay.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "sources": [{'title': 'Microsoft Support: Use Snipping Tool to capture screenshots', 'url': 'https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots', 'accessed': '2026-11-13'}, {'title': 'Microsoft Support: Keyboard shortcut for Print Screen', 'url': 'https://support.microsoft.com/en-us/windows/experience/keyboard-shortcut-for-print-screen', 'accessed': '2026-11-13'}],
             "messages": [
                 "How can I take a picture of my whole screen on my Windows 11 computer?",
                 """You can use **Snipping Tool**.

1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
2. Select **Snipping Mode**, then choose **Full screen**.
3. Select **New**.

It captures the whole screen right away.""",
                 "OK it took the picture but I can't tell where it went. How do I find it?",
                 """Snips are saved automatically in your **Screenshots** folder.

1. Open **File Explorer** from the taskbar.
2. On the left side, select the **Pictures** folder, then select **Screenshots**.
3. If you want another copy somewhere else, select **Save as** in Snipping Tool, choose a location and a name, then select **Save**.

To change where snips are saved, select **See More** in Snipping Tool, then **Settings**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-030", "task_type": "wifi_connect", "task": "Connect to a Wi-Fi network",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Help: Connect to Wi-Fi networks on your Android device", "url": "https://support.google.com/android/answer/9075847?hl=en"},
        "source_notes": """Settings > Network & internet > Internet; tap a listed network (lock icon means password needed). Quick: swipe down from top, tap Internet, select a network. After connecting the network is labeled Saved and connects automatically when nearby.
Add network manually: Settings > Network & internet > Internet; at the bottom of the list tap Add network; enter the network name (SSID) and security details if needed; tap Save. Hidden network: in Add network form tap Advanced options; under Hidden Network select Yes; tap Save.
Troubleshooting: network not listed, wait for the list to reload. Reset connection: swipe down, touch and hold Internet, tap Reset (ends active calls). Some steps need Android 12 or later.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 """My son set up our Wi-Fi at the new apartment and hid the network, so it doesn't show up in the list on my Android phone. He told me the name and password. How do I connect to a network that isn't listed?""",
                 """You can add it yourself.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. At the bottom of the list, tap **Add network**.
4. Type the network name your son gave you.
5. Enter the security details your son gave you, including the password.
6. Tap **Advanced options**, and under **Hidden Network** select **Yes**.
7. Tap **Save**.

Once connected, the network is labeled **Saved**, and your phone joins it automatically when you're nearby.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I'm at my sister's house with an Android phone. How do I get on her Wi-Fi?",
                 """Here is how.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. Tap your sister's network in the list. A lock icon means it needs a password.
4. Enter the password if asked.

When you're connected, the network shows as **Saved**.""",
                 "I don't see her network in the list at all.",
                 """Ask her for the network name and the password. Then check the list first.

1. Open the **Settings** app, tap **Network & internet**, then tap **Internet**.
2. Wait for the list to refresh. If her network is nearby but still not listed, it may be hidden.
3. Scroll to the bottom of the list and tap **Add network**.
4. Type the network name, then enter the security details (the password).
5. Tap **Advanced options**, and under **Hidden Network** select **Yes**.
6. Tap **Save**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-031", "task_type": "wifi_connect", "task": "Connect to a Wi-Fi network",
        "platform": "Windows 11", "category": "technical_support", "sensitive": False,
        "source": {"title": "Microsoft Support: Connect to a Wi-Fi network in Windows", "url": "https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows"},
        "source_notes": """Select the Network, Sound, or Battery icons on the taskbar to open quick settings. In the Wi-Fi quick setting select Manage Wi-Fi connections. Choose your network and select Connect. If it doesn't appear, select the Refresh network list button in the lower right to scan again. Enter the network password and select Next. When not connected the taskbar shows a "Disconnected" icon. Hidden networks, airplane mode and troubleshooting steps are not covered.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I'm visiting my daughter with my Windows 11 laptop and she hasn't given me her Wi-Fi password yet because she's out. Can I get my laptop connected to her network before she gets home?""",
                 """You can get everything ready, but joining her network needs the password. Without it, you can't finish.

1. Select the **Network**, **Sound**, or **Battery** icons on the taskbar.
2. In the Wi-Fi quick setting, select **Manage Wi-Fi connections**.
3. Choose her network and select **Connect**.
4. When it asks for the password, enter it and select **Next**.

When she gets home, ask her for the password and finish at step 4.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I need to connect my Windows 11 laptop to the Wi-Fi in my house. How do I do it?",
                 """Here is how.

1. Select the **Network**, **Sound**, or **Battery** icons on the taskbar.
2. In the Wi-Fi quick setting, select **Manage Wi-Fi connections**.
3. Choose your network and select **Connect**.
4. Enter the network password and select **Next**.

If you are not connected, the taskbar shows a **Disconnected** icon.""",
                 "My network isn't showing up in the list.",
                 """Ask the laptop to look again.

1. Open the Wi-Fi list the same way, with **Manage Wi-Fi connections**.
2. Select the **Refresh network list** button in the lower right.
3. When your network appears, select it and select **Connect**.""",
             ]},
        ],
    },
]
