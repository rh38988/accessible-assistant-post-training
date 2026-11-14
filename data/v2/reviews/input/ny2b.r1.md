# Review input: batch ny2b, round 1 (36 examples)

## tr141-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

**USER:**
How do I set up voicemail on my iPhone?

**ASSISTANT:**
Here is how to set up voicemail on your iPhone.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap **Set Up Now**.
4. Create a voicemail password.
5. Choose a greeting, either **Default** or **Custom**.
6. If you picked **Custom**, record your new greeting.

If you do not see **Set Up Now**, your phone may not offer Visual Voicemail. Tap **Voicemail** and follow the instructions on the screen.

## tr141-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

**USER:**
My daughter set up my iPhone last year and voicemail is already working. There is a little red number on the Voicemail icon at the bottom of the Phone app and I think someone left me a message but I have never listened to one on this phone. How do I hear it? I would like to delete it afterward too.

**ASSISTANT:**
The red number shows how many messages you have not heard yet. Here is how to listen and delete.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap the message you want.
4. Tap the **Play** button.
5. When it is done, tap the **Delete** button to remove it.

Messages stay saved until you delete them. If you delete one by mistake, tap **Deleted Messages**, tap the message, then tap **Undelete**.

## tr141-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

**USER:**
Can you help me set up voicemail on my phone?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr141-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

**USER:**
Can you help me set up voicemail on my phone?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
It's an iPhone.

**ASSISTANT:**
Thank you. Here is how to set up voicemail on an iPhone.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap **Set Up Now**.
4. Create a voicemail password.
5. Choose a greeting, either **Default** or **Custom**.
6. If you picked **Custom**, record your new greeting.

If you do not see **Set Up Now**, tap **Voicemail** and follow the instructions on the screen.

## tr141-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

**USER:**
I have an iPhone and my fingers shake so I really struggle to tap the little buttons in the Phone app. Is there any way to find out if I have new voicemail without tapping through all the screens? I can talk to the phone fine.

**ASSISTANT:**
Yes, you can ask Siri instead of tapping. Use your voice to say things like:

1. "Do I have any new voicemail?"
2. "Play the voicemail from" and then the name of the person, for example "Play the voicemail from Eliza."

Siri will answer or play the message for you. If you ever want to tap instead, open the **Phone** app, tap **Voicemail**, then tap a message and tap the **Play** button.

## tr141-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0

**USER:**
My iPhone keeps saying I have no voicemail greeting. Please walk me through setting up my voicemail.

**ASSISTANT:**
Here is how to set up voicemail on your iPhone.

1. Open the **Phone** app.
2. Tap **Voicemail**.
3. Tap **Set Up Now**.
4. Create a voicemail password.
5. Choose a greeting, either **Default** or **Custom**.
6. If you picked **Custom**, record your new greeting.

If you do not see **Set Up Now**, tap **Voicemail** and follow the instructions on the screen.

**USER:**
I tapped Voicemail but there is no Set Up Now button. It just shows something different.

**ASSISTANT:**
That can happen when your phone does not offer Visual Voicemail. Try this.

1. Open the **Phone** app and tap **Voicemail**.
2. Follow the instructions on the screen.

Or you can use another phone.

1. Call your own mobile number.
2. When your greeting plays, press * or #, depending on your carrier, to skip it.
3. Enter your voicemail password.

## tr142-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
How do I forward my iPhone calls to my husband's phone number?

**ASSISTANT:**
Here is how to forward your calls on an iPhone.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To**.
7. Type in your husband's phone number.
8. Tap **Back**.

You will see a Call Forwarding icon at the top of the screen while it is on. Your phone must be in range of the cellular network when you do this, or calls will not forward.

## tr142-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
I'm going on a cruise next week and I will not have my iPhone with me, it is staying at home with the charger. My son said I can send calls to his number so I don't miss anything from the doctor's office. My iPhone has two SIMs in it because I travel for work. Please tell me what to do.

**ASSISTANT:**
Yes, you can forward your calls to your son's number. Set it up before you leave.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To** and type in your son's number.
7. Because your iPhone has two SIMs, choose the line you want to forward.
8. Tap **Back**.

A Call Forwarding icon shows at the top of the screen while it is on. Your phone must be in range of the cellular network when you set it up, or calls will not forward.

## tr142-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
I need my calls to go to my sister's number for a week. How?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr142-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
I need my calls to go to my sister's number for a week. How?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thank you. Here is how to forward calls on an iPhone.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To**.
7. Type in your sister's number.
8. Tap **Back**.

A Call Forwarding icon shows at the top of the screen while it is on.

## tr142-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
My iPhone is on a CDMA network, my grandson told me that's the kind of service I have. I would like to send calls to my neighbor's number while I'm in the hospital. Can you give me the steps for that?

**ASSISTANT:**
The iPhone steps for call forwarding are for phones on a GSM network. Since your service is CDMA, please contact your carrier and ask them to set up call forwarding for you.

If your carrier tells you that you are on a GSM network, the steps are these.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding** and turn it on.
5. Tap **Forward To**, type your neighbor's number, then tap **Back**.

## tr142-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
Please help me make my iPhone send my calls to my cell number at my cabin.

**ASSISTANT:**
Here is how to forward your calls on an iPhone.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Tap **Forward To**.
7. Type in the number.
8. Tap **Back**.

You will see a Call Forwarding icon at the top of the screen while it is on.

**USER:**
I did all that but when my friend called me it didn't go to the other number. What went wrong?

**ASSISTANT:**
Two things are worth checking.

1. Your phone must be in range of the cellular network when you set up forwarding. If it was not, calls will not forward. Move to a spot with signal and set it up again.
2. Call forwarding works on a GSM network. If your phone uses a CDMA network, contact your carrier.

## tr143-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
I have trouble hearing my iPhone. Can I make the little light on the back flash when I get an alert?

**ASSISTANT:**
Yes, your iPhone can blink its light for alerts.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

After that, the light next to the camera lens blinks when you get a notification. This only works while the phone is locked.

## tr143-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
I work in a loud garage all day and my iPhone is always on silent so it doesn't buzz off my workbench. My wife says I miss her messages. I've heard there is a setting where the flashlight blinks. I want it to blink even though the phone is on silent. I'm on an iPhone. What should I do?

**ASSISTANT:**
Yes, there is a setting for that.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.
5. Make sure **Flash on Silent** is turned on.

With both on, the light next to the camera lens blinks when you get a notification, even in silent mode. It only blinks while the phone is locked.

## tr143-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
My hearing isn't good. Is there a way to have a light blink on my phone instead of a sound?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr143-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
My hearing isn't good. Is there a way to have a light blink on my phone instead of a sound?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
It is an iPhone

**ASSISTANT:**
Thank you. On an iPhone, you can make the light blink for alerts.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

The light next to the camera lens will then blink when you get a notification. This only works while the phone is locked.

## tr143-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
I want my iPhone light to blink for alerts, but at church and at night I put my phone on silent and I do NOT want it blinking then. I only want the light when the phone isn't on silent. It's an iPhone.

**ASSISTANT:**
You can do that.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.
5. Turn off **Flash on Silent**.

Now the light blinks for notifications, but not while your phone is in silent mode. It only blinks while the phone is locked.

## tr143-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
Is there a setting to make my iPhone's flash blink when something comes in? I keep missing things.

**ASSISTANT:**
Yes, there is.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

The light next to the camera lens blinks when you get a notification while the phone is locked.

**USER:**
I turned it on but I was holding the phone and reading it, and the light never blinked when a message came.

**ASSISTANT:**
That is expected. **LED Flash for Alerts** only works when your phone is locked.

1. Press the side button to lock the phone, or put it down and let the screen go dark.
2. Wait for the next notification. The light next to the camera lens should blink.

If you are still not seeing it, go back to **Settings**, **Accessibility**, **Audio/Visual** and check that **LED Flash for Alerts** is on.

## tr144-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
How can I find out which model my iPhone is? I'm trying to sell it.

**ASSISTANT:**
You can find the model number in Settings.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. The part number is shown to its right.
5. Tap that part number and it changes to the model number.

The model number starts with the letter A and four digits. You can match it against Apple's list of iPhone models to see which model you have.

## tr144-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
I found my old iPhone 7 in a drawer, the one my late husband used. The battery is dead and I don't have the right charger so I can't turn it on. A repair shop asked me for the model number. Is there a way to see it without turning it on?

**ASSISTANT:**
Yes. On an iPhone 7 or earlier, the model number is on the back of the phone.

1. Turn the phone over so the back faces you.
2. Look at the writing on the back and find the model number.

You do not need to turn the phone on. The model number starts with the letter A and four digits.

## tr144-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
What model is my phone? The store wants to know.

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr144-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
What model is my phone? The store wants to know.

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iphone

**ASSISTANT:**
Thank you. Here is how to find the model number on an iPhone.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. A part number is shown to its right.
5. Tap that part number and it changes to the model number.

The model number starts with the letter A and four digits. You can tell the store that number.

## tr144-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
I forgot the passcode on my iPhone 8 so I can't open Settings, and I do not want to try guessing it. It has a SIM tray on the side. Can I still find the model number some other way?

**ASSISTANT:**
Yes, you do not need to unlock the phone.

1. Remove the SIM tray from the side of the phone.
2. Hold the tray slot under bright overhead light and look inside the slot.
3. Look on the upper side of the slot, the side with the display. The model number is there.

The model number starts with the letter A and four digits.

## tr144-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
Please show me where the model number is on my iPhone, I need it for an insurance form.

**ASSISTANT:**
You can find it in Settings.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. A part number is shown to its right.
5. Tap that part number and it changes to the model number.

**USER:**
I got to About and Model Number but the number there is a long one that doesn't look like what the insurance form wants.

**ASSISTANT:**
That long number is the part number. Tap it once.

1. On the **About** screen, find **Model Number**.
2. Tap the number to the right of it.
3. It changes to the model number. Use that one on the form.

## tr145-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Scan a paper document with the phone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108963

**USER:**
How do I scan a paper form with my iPhone so I can email it?

**ASSISTANT:**
You can scan it in the Notes app.

1. Open **Notes**.
2. Open a note, or start a new one.
3. Tap the paperclip button.
4. Tap **Scan Documents**.
5. Hold the phone so the paper is in view of the camera. If your phone is in Auto mode, it scans by itself.
6. Tap **Done**.

If the paper has more pages, scan them before you tap **Done**.

## tr145-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Scan a paper document with the phone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108963

**USER:**
I never use the Notes app on my iPhone, I only know the Files app because my grandson put my tax papers in there. I have a letter from the county on my kitchen table that I want to scan and keep in Files. How do I do that? I want it saved in a folder, not floating around.

**ASSISTANT:**
You can scan it right inside the Files app.

1. Open **Files**.
2. Tap the **More** button, the three dots.
3. Tap **Scan Documents**.
4. Hold the phone so the letter is in view of the camera. In Auto mode it scans by itself.
5. Tap **Done**, or scan more pages first.
6. Choose the folder where you want it.
7. Tap **Save**.

## tr145-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Scan a paper document with the phone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108963

**USER:**
how do i scan a paper with my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr145-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Scan a paper document with the phone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108963

**USER:**
how do i scan a paper with my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
its an iphone

**ASSISTANT:**
Thank you. On an iPhone you can scan in the Notes app.

1. Open **Notes**.
2. Open a note, or start a new one.
3. Tap the paperclip button.
4. Tap **Scan Documents**.
5. Hold the phone so the paper is in view of the camera. In Auto mode it scans by itself.
6. Tap **Done**.

## tr145-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Scan a paper document with the phone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108963

**USER:**
I have an iPhone. When I scan, the phone grabs the picture too fast before I have the paper lined up. I want to be the one who decides when it takes the picture. How do I scan a bill in Notes that way?

**ASSISTANT:**
You can capture the scan yourself.

1. Open **Notes**, then open a note or start a new one.
2. Tap the paperclip button.
3. Tap **Scan Documents**.
4. Line up the bill in view of the camera.
5. Tap the Shutter button, or press a Volume button, when you are ready.
6. Drag the corners so they fit the page.
7. Tap **Keep Scan**.
8. Tap **Done**.

## tr145-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Scan a paper document with the phone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108963

**USER:**
My iPhone needs to scan my lease papers. Can you tell me how in the Notes app?

**ASSISTANT:**
Here is how to scan in Notes.

1. Open **Notes**.
2. Open a note, or start a new one.
3. Tap the paperclip button.
4. Tap **Scan Documents**.
5. Hold the phone so the paper is in view of the camera. In Auto mode it scans by itself.
6. Tap **Done**.

**USER:**
I pointed it at the paper but it never scanned by itself. It just keeps showing the camera.

**ASSISTANT:**
Then capture it yourself.

1. With the paper in view, tap the Shutter button, or press a Volume button.
2. Drag the corners so they fit the page.
3. Tap **Keep Scan**.
4. Tap **Done**, or scan more pages first.

## tr146-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Move apps and organize the Home Screen (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108307

**USER:**
How do I move the Weather app to the bottom row of my iPhone so it's easier to reach? I have an iPhone 14.

**ASSISTANT:**
Here is how to move an app on your iPhone.

1. Touch and hold the Weather app until a menu appears.
2. Tap **Edit Home Screen**.
3. Drag the app to its new spot, such as the Dock at the bottom of the screen.
4. Tap **Done** to save your change.

## tr146-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Move apps and organize the Home Screen (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108307

**USER:**
My iPhone 8 has so many apps on the first page that I can't find anything. I want the Camera app moved over to the second page of my Home Screen. I am afraid of messing something up. The phone has the round Home button at the bottom. What do I do exactly?

**ASSISTANT:**
Here is how to move the Camera app to another page.

1. Touch and hold the Camera app until the apps jiggle.
2. Drag the app to the right edge of the screen. A new page may take a second to appear.
3. Let go of the app when it is on the page you want.
4. Press the Home button to save your changes.

If you do not see dots to the right of the bright dot above the Dock, dragging to the right edge makes a new page.

## tr146-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Move apps and organize the Home Screen (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108307

**USER:**
The apps on my phone are all in a mess. How do I put them where I want?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr146-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Move apps and organize the Home Screen (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108307

**USER:**
The apps on my phone are all in a mess. How do I put them where I want?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone, a newer one with no home button

**ASSISTANT:**
Thank you. Here is how to move apps on your iPhone.

1. Touch and hold any app until a menu appears.
2. Tap **Edit Home Screen**.
3. Drag the app to its new spot.
4. Repeat for any other apps you want to move.
5. Tap **Done** to save your changes.

## tr146-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Move apps and organize the Home Screen (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108307

**USER:**
I have an iPhone and I have six card game apps all over my screen. I do NOT want to delete any of them, I just want them together in one place. Is there a way to group them?

**ASSISTANT:**
Yes, you can put them in a folder. Nothing gets deleted.

1. Touch and hold one of the game apps until the apps jiggle.
2. Drag it onto another game app. This makes a folder.
3. Drag each of the other game apps into the folder.

To give the folder a name, touch and hold the folder until a menu appears, tap **Rename**, type the name, then tap **Done**.

## tr146-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Move apps and organize the Home Screen (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108307

**USER:**
Can you tell me how to get my Photos app onto a different page of my iPhone Home Screen? I'm on an iPhone with Face ID.

**ASSISTANT:**
Here is how to move Photos to another page.

1. Touch and hold the Photos app until the apps jiggle.
2. Drag the app to the right edge of the screen.
3. Let go when you are on the page you want.
4. Tap **Done** to save your change.

**USER:**
I dragged it to the right edge but nothing happened, the page didn't change.

**ASSISTANT:**
Try this.

1. Keep holding the app at the right edge for a second. A new page may take a moment to appear.
2. Look at the dots above the Dock. If there are dots to the right of the bright dot, keep dragging toward that side to reach the next page.
3. If there are no dots to the right, dragging to that side makes a new page.
