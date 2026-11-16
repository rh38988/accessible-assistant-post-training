# Rule scan input, part 13 (50 examples)

## tr144-d
- task: Find the model number of the iPhone to identify which model it is | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Find the model number of your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/106343>

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

You can tell the store that number.

---

## tr144-e
- task: Find the model number of the iPhone to identify which model it is | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Find the model number of your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/106343>

**USER:**
I forgot the passcode on my iPhone 8 so I can't open Settings, and I do not want to try guessing it. It has a SIM tray on the side. Can I still find the model number some other way?

**ASSISTANT:**
Yes. On an iPhone 8 or later with a SIM tray, you can look inside the SIM tray slot.

1. Remove the SIM tray from the side of the phone.
2. Hold the tray slot under bright overhead light and look inside the slot.
3. Look on the upper side of the slot, the side with the display. The model number is there.

---

## tr144-r
- task: Find the model number of the iPhone to identify which model it is | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Find the model number of your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/106343>

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

---

## tr145-a
- task: Scan a paper document with the phone | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: How to scan documents on your iPhone or iPad <https://support.apple.com/en-us/108963>

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

---

## tr145-b
- task: Scan a paper document with the phone | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: How to scan documents on your iPhone or iPad <https://support.apple.com/en-us/108963>

**USER:**
how do i scan a paper with my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr145-c
- task: Scan a paper document with the phone | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: How to scan documents on your iPhone or iPad <https://support.apple.com/en-us/108963>

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

---

## tr145-d
- task: Scan a paper document with the phone | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: How to scan documents on your iPhone or iPad <https://support.apple.com/en-us/108963>

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

---

## tr145-e
- task: Scan a paper document with the phone | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: How to scan documents on your iPhone or iPad <https://support.apple.com/en-us/108963>

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

---

## tr145-r
- task: Scan a paper document with the phone | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to scan documents on your iPhone or iPad <https://support.apple.com/en-us/108963>

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

---

## tr146-a
- task: Move apps and organize the Home Screen | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Move apps and create folders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/108307>

**USER:**
How do I move the Weather app to the bottom row of my iPhone so it's easier to reach? I have an iPhone 14.

**ASSISTANT:**
Here is how to move an app on your iPhone.

1. Touch and hold the Weather app until a menu appears.
2. Tap **Edit Home Screen**.
3. Drag the app to its new spot, such as the Dock at the bottom of the screen.
4. Tap **Done** to save your change.

---

## tr146-c
- task: Move apps and organize the Home Screen | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Move apps and create folders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/108307>

**USER:**
My iPhone 8 has so many apps on the first page that I can't find anything. I want the Camera app moved over to the second page of my Home Screen. I am afraid of messing something up. The phone has the round Home button at the bottom. What do I do exactly?

**ASSISTANT:**
Here is how to move the Camera app to another page.

1. Touch and hold the Camera app until the apps jiggle.
2. Drag the app to the right edge of the screen. A new page may take a second to appear.
3. Let go of the app when it is on the page you want.
4. Press the Home button to save your changes.

If you do not see dots to the right of the bright dot above the Dock, dragging to the right edge makes a new page.

---

## tr146-d
- task: Move apps and organize the Home Screen | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Move apps and create folders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/108307>

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

---

## tr146-e
- task: Move apps and organize the Home Screen | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Move apps and create folders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/108307>

**USER:**
I have an iPhone and I have six card game apps all over my screen. I do NOT want to delete any of them, I just want them together in one place. Is there a way to group them?

**ASSISTANT:**
Yes, you can put them in a folder. Nothing gets deleted.

1. Touch and hold one of the game apps until the apps jiggle.
2. Drag it onto another game app. This makes a folder.
3. Drag each of the other game apps into the folder.

To give the folder a name, touch and hold the folder until a menu appears, tap **Rename**, type the name, then tap **Done**.

---

## tr146-r
- task: Move apps and organize the Home Screen | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Move apps and create folders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/108307>

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

---

## tr147-b
- task: The phone is frozen or will not respond | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Fix an Android device that freezes or won't respond <https://support.google.com/android/answer/7664998>

**USER:**
my phone wont respond when i touch the screen

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr147-c
- task: The phone is frozen or will not respond | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Fix an Android device that freezes or won't respond <https://support.google.com/android/answer/7664998>

**USER:**
So I was looking at pictures my grandson sent on my Google Pixel phone and then the picture just stopped moving. The screen is still lit up but I can't swipe or tap anything, not even the home button. I've been poking at it for ten minutes. My husband says to take the battery out but I don't think this phone has that. Help please.

**ASSISTANT:**
You do not need to take anything apart. Try this instead.

1. Press and hold the **power button**.
2. Keep holding it for about 60 seconds, even if it seems like a long time.
3. Let go when the phone restarts.

This works when the phone is frozen with the screen on, like yours. If it keeps freezing later, open **Settings**, tap **System**, then **Software update**, and follow the steps on the screen.

---

## tr147-d
- task: The phone is frozen or will not respond | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Fix an Android device that freezes or won't respond <https://support.google.com/android/answer/7664998>

**USER:**
my phone wont respond when i touch the screen

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks. If the screen is on but frozen, force a restart.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding until the phone restarts.

If it keeps freezing, open **Settings**, tap **System**, then **Software update**, and follow the steps on the screen.

---

## tr147-e
- task: The phone is frozen or will not respond | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Fix an Android device that freezes or won't respond <https://support.google.com/android/answer/7664998>

**USER:**
My Android phone froze on the lock screen. I have a lot of photos of my late wife on it and I'm scared of losing them, so please do not tell me to erase or reset anything. Is there something gentle I can try first?

**ASSISTANT:**
Yes. The first thing to try is only a restart.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding until the phone restarts.

A reset that erases everything is the very last thing to try, and only after other fixes fail. If the freezing keeps happening, try **Settings**, then **System**, then **Software update** next.

---

## tr147-r
- task: The phone is frozen or will not respond | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Fix an Android device that freezes or won't respond <https://support.google.com/android/answer/7664998>

**USER:**
My Android phone is frozen with the screen on. How do I restart it?

**ASSISTANT:**
Force a restart.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding until the phone restarts.

If it freezes again, open **Settings**, tap **System**, then **Software update**.

**USER:**
It restarted, thank you, but it freezes again almost every day.

**ASSISTANT:**
Let's look at what may be causing it. Restart the phone after each of these.

1. Open **Settings**, tap **System**, then **Software update**, and follow the steps on the screen.
2. Look at your storage in **Settings**. Problems can start when less than 10% of the storage is free, so free up some space if it is low.

---

## tr148-a
- task: The phone will not charge | platform: Android (Pixel) | scenario: direct | sensitive: False
- sources: Pixel Phone Help: Fix a Pixel phone that won't charge or turn on <https://support.google.com/pixelphone/answer/7167687>

**USER:**
My Google Pixel phone won't charge. I plug it in and nothing seems to happen.

**ASSISTANT:**
Let's check the usual causes.

1. Take the phone case off so it does not block the plug.
2. Make sure the cable is pushed in firmly at both ends, the adapter and the phone.
3. Look in the phone's charging port for dust or lint.
4. Try a different cable or adapter, and a different wall outlet.
5. Leave it plugged in for one minute. A battery icon on the screen means the phone is off and charging.
6. Press and hold the **Power** button for 5 to 7 seconds.

A very low battery can take several minutes before the screen turns on.

---

## tr148-c
- task: The phone will not charge | platform: Android (Pixel) | scenario: direct_messy | sensitive: False
- sources: Pixel Phone Help: Fix a Pixel phone that won't charge or turn on <https://support.google.com/pixelphone/answer/7167687>

**USER:**
My Pixel phone has been sitting in a drawer since the spring because I got a new one for work and now I want to use the old one for my mother. I plugged it in about ten minutes ago and the screen is totally black, no light, no buzzing, nothing. Is it broken? I'm not very good with this stuff.

**ASSISTANT:**
It may not be broken. A phone that has been fully drained for a long time can show nothing at first.

1. Plug it into a working wall outlet with a firmly connected cable and adapter.
2. Press and hold the **Power** button for 5 to 7 seconds.
3. Keep it plugged in. You may see no charging icon, no vibration, and no screen response for up to 25 minutes.

If there is still no response after 25 minutes, the phone needs to be repaired.

---

## tr148-d
- task: The phone will not charge | platform: Android (Pixel) | scenario: followup | sensitive: False
- sources: Pixel Phone Help: Fix a Pixel phone that won't charge or turn on <https://support.google.com/pixelphone/answer/7167687>

**USER:**
my phone wont charge anymore

**ASSISTANT:**
I can help with that. Is it a **Google Pixel** phone, or another kind of phone?

**USER:**
its a pixel

**ASSISTANT:**
Thanks. Try these in order.

1. Take off the phone case.
2. Make sure the cable is firmly connected to both the adapter and the phone.
3. Check the charging port for dust or lint.
4. Try a different cable or adapter, and plug it into a different wall outlet.
5. Wait one minute. A battery icon means the phone is off and charging.
6. Press and hold the **Power** button for 5 to 7 seconds.

---

## tr148-r
- task: The phone will not charge | platform: Android (Pixel) | scenario: failure_recovery | sensitive: False
- sources: Pixel Phone Help: Fix a Pixel phone that won't charge or turn on <https://support.google.com/pixelphone/answer/7167687>

**USER:**
My Pixel phone won't charge. What should I try?

**ASSISTANT:**
Try these in order.

1. Take off the phone case.
2. Make sure the cable is firmly connected at both ends.
3. Check the charging port for dust or lint.
4. Try a different cable, adapter, and wall outlet.
5. Wait one minute. A battery icon means the phone is off and charging.
6. Press and hold the **Power** button for 5 to 7 seconds.

**USER:**
I did all that and no battery picture shows up on the screen.

**ASSISTANT:**
Let's try one more thing.

1. Press and hold the **Power** button for about 35 seconds to reboot.
2. Wait about 2 minutes.
3. Call the phone from another phone, or use the **Find Hub** app, to see if it rings.

If it rings but the screen stays blank, contact an authorized repair center.

---

## tr149-a
- task: The phone cannot connect to the internet | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Fix internet connection problems on Android devices <https://support.google.com/android/answer/2651367>

**USER:**
My Android phone says it has no internet. Web pages won't load. What should I do?

**ASSISTANT:**
Try these in order.

1. Restart your phone.
2. Open **Settings** and tap **Network & internet** (on some phones it is called **Connections**).
3. Turn Wi-Fi off and mobile data on, and see if things load. If not, turn mobile data off and Wi-Fi on, and check again.
4. Turn **Airplane mode** on, wait 10 seconds, then turn it off.
5. If you use home Wi-Fi, unplug the router, wait 30 seconds, plug it back in, and wait about 30 seconds for the lights to come back.

If problems continue, contact your mobile service provider or your internet provider.

---

## tr149-b
- task: The phone cannot connect to the internet | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Fix internet connection problems on Android devices <https://support.google.com/android/answer/2651367>

**USER:**
The internet on my Android phone is not working.

**ASSISTANT:**
I can help with that. Is the problem when you are on **Wi-Fi**, on **mobile data**, or both?

---

## tr149-c
- task: The phone cannot connect to the internet | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Fix internet connection problems on Android devices <https://support.google.com/android/answer/2651367>

**USER:**
Hi, I'm at home and my Android phone shows the Wi-Fi at the top but nothing will open, not the weather, not my email. My daughter's tablet in the next room is fine though, or at least it was an hour ago. I've had the same Wi-Fi for years. I restarted the phone once already. What else can I try?

**ASSISTANT:**
Here is what to try next for Wi-Fi.

1. Open **Settings** and tap **Network & Internet** (or **Connections**), then tap **Wi-Fi**.
2. Make sure **Wi-Fi** is turned on.
3. Look at the Wi-Fi symbol at the top of the screen. If it is missing or has no bars filled, you may be out of range. Move closer to the router and try again.
4. Restart the router. Unplug it and make sure the lights go out. Wait 30 seconds, plug it back in, and wait about 30 seconds for all the lights to come back.

If it still does not work, contact your internet provider.

---

## tr149-d
- task: The phone cannot connect to the internet | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Fix internet connection problems on Android devices <https://support.google.com/android/answer/2651367>

**USER:**
The internet on my Android phone is not working.

**ASSISTANT:**
I can help with that. Is the problem when you are on **Wi-Fi**, on **mobile data**, or both?

**USER:**
mobile data, I'm out shopping

**ASSISTANT:**
Let's check your mobile data.

1. Restart your phone.
2. Open **Settings** and tap **Network & internet** (or **Connections**), then **Mobile data** (or **Cellular data**).
3. Make sure it is on. If it is already on, turn it off and back on.
4. Look for 2G, 3G, 4G, or H next to the signal bars at the top of the screen.
5. If you see none, you may be out of coverage. Move somewhere else, or go outside, and check again.

If this happens often, contact your mobile service provider.

---

## tr149-r
- task: The phone cannot connect to the internet | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Fix internet connection problems on Android devices <https://support.google.com/android/answer/2651367>

**USER:**
My Android phone is on Wi-Fi at home but web pages won't load. What do I try?

**ASSISTANT:**
Try these in order.

1. Restart your phone.
2. Open **Settings**, tap **Network & Internet** (or **Connections**), then **Wi-Fi**, and make sure **Wi-Fi** is on.
3. Check for the Wi-Fi symbol at the top of the screen.
4. Restart the router. Unplug it, wait 30 seconds, plug it back in, and wait about 30 seconds for the lights to return.

**USER:**
I turned Wi-Fi on but there's no Wi-Fi symbol at the top of my screen.

**ASSISTANT:**
If the symbol is missing, or none of its bars are filled, you may be out of range.

1. Move closer to the router.
2. Check that the Wi-Fi symbol now shows a stronger signal.
3. Try opening a web page again.

---

## tr150-a
- task: Text messages will not send or arrive | platform: Android (Google Messages) | scenario: direct | sensitive: False
- sources: Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
None of my texts are going through in Google Messages on my Android phone. What should I check?

**ASSISTANT:**
Check these in order.

1. Update **Google Messages** to the newest version.
2. If your phone has a SIM card, make sure it is inserted properly.
3. Set **Google Messages** as your default texting app.
4. Check that your plan or credit balance covers sending and receiving texts.
5. Check that you have signal.
6. If airplane mode is on, turn it off.

Also check that your carrier supports SMS, MMS, or RCS.

---

## tr150-b
- task: Text messages will not send or arrive | platform: Android (Google Messages) | scenario: missing_info | sensitive: False
- sources: Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
Google Messages on my Android phone is not working right, my texts are failing.

**ASSISTANT:**
I can help with that. Is the problem with **everyone**, with **one person**, or with **picture messages**?

---

## tr150-c
- task: Text messages will not send or arrive | platform: Android (Google Messages) | scenario: direct_messy | sensitive: False
- sources: Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
I can text everyone fine in Google Messages on my Android phone, my kids, my neighbor, everybody, except my friend Margaret. Her texts to me are fine too, but whenever I answer her it just won't go. I saved her number years ago when she lived in another state. What on earth is going on?

**ASSISTANT:**
The trouble is probably with that one contact. Try these.

1. Delete Margaret from your contacts and add her again.
2. Check whether you blocked her.
3. Check that her phone number is correct.
4. Check whether the number needs a country code, for example +1 for US numbers.

---

## tr150-d
- task: Text messages will not send or arrive | platform: Android (Google Messages) | scenario: followup | sensitive: False
- sources: Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
Google Messages on my Android phone is not working right, my texts are failing.

**ASSISTANT:**
I can help with that. Is the problem with **everyone**, with **one person**, or with **picture messages**?

**USER:**
picture messages, plain words go through

**ASSISTANT:**
For picture messages, try these.

1. Make sure you have a data connection.
2. In your phone's **Settings** app, find the **APN** settings (the settings your phone uses to send picture messages) and choose to reset them to default. The exact menu names are a little different on each phone.
3. Open **Google Messages**. At the top right, tap your **Profile picture** or **Initials**, then **Messages settings**, then **Advanced**, then **Group messaging**.
4. Tap **Send an MMS reply to all recipients (group MMS)**.

---

## tr150-e
- task: Text messages will not send or arrive | platform: Android (Google Messages) | scenario: constraint | sensitive: False
- sources: Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
My texts in Google Messages won't send on my Android. Please don't tell me to take out the SIM card, I'm afraid I'll break it and I can't get to the store. What else can I check?

**ASSISTANT:**
No problem, you can skip the SIM card. Check these instead.

1. Update **Google Messages** to the newest version.
2. Set **Google Messages** as your default texting app.
3. Check that your plan or credit balance covers sending and receiving.
4. Check that you have signal.
5. If airplane mode is on, turn it off.
6. Confirm your carrier supports SMS, MMS, or RCS.

---

## tr150-r
- task: Text messages will not send or arrive | platform: Android (Google Messages) | scenario: failure_recovery | sensitive: False
- sources: Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
My texts won't send in Google Messages on my Android. What can I check?

**ASSISTANT:**
Check these in order.

1. Update **Google Messages** to the newest version.
2. Set **Google Messages** as your default texting app.
3. Check that your plan or credit balance covers sending and receiving.
4. Check that you have signal.
5. If airplane mode is on, turn it off.
6. Confirm your carrier supports SMS, MMS, or RCS.

**USER:**
Under my chat it says Not supported - RCS chats are not supported by your carrier. Is that why?

**ASSISTANT:**
That message means your carrier does not currently support RCS chats. It does not point to something you did wrong.

1. Confirm your carrier supports SMS, MMS, or RCS.
2. Check that your plan or credit balance covers sending and receiving.
3. Check that you have signal.

---

## tr151-d
- task: Send a group text | platform: Android (Google Messages) | scenario: followup | sensitive: False
- sources: Google Messages Help: Explore group conversations in Google Messages <https://support.google.com/messages/answer/9367099>; Google Messages Help: Create RCS groups <https://support.google.com/messages/answer/16287429>

**USER:**
I want to send the same message to a whole bunch of people at once on my Android phone

**ASSISTANT:**
I can help with that. Are you using the **Google Messages** app, or a different texting app?

**USER:**
Google Messages

**ASSISTANT:**
Thanks. Start a group text like this.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick the people you want from your contacts.
4. Tap **Next**.
5. Write your message and send it.

---

## tr151-r
- task: Send a group text | platform: Android (Google Messages) | scenario: failure_recovery | sensitive: False
- sources: Google Messages Help: Explore group conversations in Google Messages <https://support.google.com/messages/answer/9367099>; Google Messages Help: Create RCS groups <https://support.google.com/messages/answer/16287429>; Google Messages Help: Fix problems sending, receiving, or connecting to messages <https://support.google.com/messages/answer/9077245>

**USER:**
How do I send a group text to my book club in Google Messages on Android?

**ASSISTANT:**
Start a group like this.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick your book club members.
4. Tap **Next**.
5. Write your message and send it.

**USER:**
It sent, but when people answer, I get their replies in separate chats, not all together.

**ASSISTANT:**
Replies come back separately when the setting is mass text. To keep group replies in one conversation, change this.

1. In **Google Messages**, at the top right, tap your **profile picture** or **initials**.
2. Tap **Messages settings**, then **Advanced**, then **Group messaging**.
3. Tap **Send an MMS reply to all recipients (group MMS)**.

---

## tr152-a
- task: Report and block spam texts | platform: Android (Google Messages) | scenario: direct | sensitive: True
- sources: Google Messages Help: Report spam and block a number in Google Messages <https://support.google.com/messages/answer/9061432>

**USER:**
I keep getting spam texts from the same number in Google Messages on my Android phone. How do I report and block it?

**ASSISTANT:**
You can block that number and report it at the same time.

1. Open **Google Messages**.
2. Press and hold the conversation with that number.
3. Tap **Block**, then tap **Report spam**, then tap **OK**.

The sender is blocked, and the conversation moves to your **Spam & blocked** folder.

---

## tr152-b
- task: Report and block spam texts | platform: Android (Google Messages) | scenario: missing_info | sensitive: True
- sources: Google Messages Help: Report spam and block a number in Google Messages <https://support.google.com/messages/answer/9061432>

**USER:**
how do i get rid of all these junk texts, they never stop

**ASSISTANT:**
I can help with that. Do you read your texts in the **Google Messages** app, or a different app?

---

## tr152-c
- task: Report and block spam texts | platform: Android (Google Messages) | scenario: direct_messy | sensitive: True
- sources: Google Messages Help: Report spam and block a number in Google Messages <https://support.google.com/messages/answer/9061432>

**USER:**
A text came in this morning saying I won a gift card and need to click right away. I've got the conversation open in Google Messages on my Android phone right now. I don't want to hear from them again, and I'd like Google to know about it so they stop doing this to other people too.

**ASSISTANT:**
Since the conversation is already open, do this.

1. Tap **More options**.
2. Tap **Details**.
3. Tap **Block & report spam**.
4. Tap **OK**.

That blocks the sender, moves the conversation to your **Spam & blocked** folder, and reports the number to Google.

---

## tr152-d
- task: Report and block spam texts | platform: Android (Google Messages) | scenario: followup | sensitive: True
- sources: Google Messages Help: Report spam and block a number in Google Messages <https://support.google.com/messages/answer/9061432>

**USER:**
how do i get rid of all these junk texts, they never stop

**ASSISTANT:**
I can help with that. Do you read your texts in the **Google Messages** app, or a different app?

**USER:**
google messages

**ASSISTANT:**
Thanks. You can report and block each spammer's number.

1. Open **Google Messages**.
2. Press and hold the junk conversation.
3. Tap **Block**, then tap **Report spam**, then tap **OK**.

The sender is blocked and the conversation moves to your **Spam & blocked** folder.

---

## tr152-e
- task: Report and block spam texts | platform: Android (Google Messages) | scenario: constraint | sensitive: True
- sources: Google Messages Help: Report spam and block a number in Google Messages <https://support.google.com/messages/answer/9061432>

**USER:**
I replied STOP to a spam text last week and now I'm nervous. If I report them in Google Messages on my Android, will Google see my reply, and will the spammer find out it was me?

**ASSISTANT:**
No on both. Your past replies to the spammer are not sent to Google, and the spammer cannot see your report or know about it. Your name and phone number are not linked to their messages.

To report and block:

1. Open **Google Messages** and press and hold the conversation.
2. Tap **Block**, then tap **Report spam**, then tap **OK**.

Google does get the number and the last 10 incoming messages from the sender.

---

## tr152-r
- task: Report and block spam texts | platform: Android (Google Messages) | scenario: failure_recovery | sensitive: True
- sources: Google Messages Help: Report spam and block a number in Google Messages <https://support.google.com/messages/answer/9061432>

**USER:**
How do I report a spam text in Google Messages on my Android phone?

**ASSISTANT:**
Do this to report and block it.

1. Open **Google Messages**.
2. Press and hold the conversation you want to report.
3. Tap **Block**, then tap **Report spam**, then tap **OK**.

**USER:**
I did that, and now there's a new conversation called Spam reporting. Did I do something wrong?

**ASSISTANT:**
No, that can happen after a report. Your report might create a **Spam reporting** conversation. It sends a copy of the spammer's number and most recent text to your mobile carrier. These conversations may automatically go to **Spam & blocked**.

---

## tr153-a
- task: Check voicemail and turn on visual voicemail | platform: Android (Phone app) | scenario: direct | sensitive: False
- sources: Phone app Help: How to check your voicemail <https://support.google.com/phoneapp/answer/2811844>

**USER:**
I got a notification that someone left me a voicemail on my Android phone. How do I listen to it?

**ASSISTANT:**
You can open it from the notification.

1. Swipe down from the top of the screen.
2. Tap **Voicemail**.

---

## tr153-b
- task: Check voicemail and turn on visual voicemail | platform: Android (Phone app) | scenario: missing_info | sensitive: False
- sources: Phone app Help: How to check your voicemail <https://support.google.com/phoneapp/answer/2811844>

**USER:**
How do I hear my voicemail on my Android phone? I use the Phone app.

**ASSISTANT:**
I can help with that. Do you want to **call in** to hear your messages, or see them as a **list** on the screen?

---

## tr153-c
- task: Check voicemail and turn on visual voicemail | platform: Android (Phone app) | scenario: direct_messy | sensitive: False
- sources: Phone app Help: How to check your voicemail <https://support.google.com/phoneapp/answer/2811844>

**USER:**
My doctor's office said they left a message on my phone but I never saw any notice about it, and I've swiped down and don't see anything there. I use the regular Phone app on my Android. Is there a way to call in and hear my messages myself?

**ASSISTANT:**
Yes, you can call your voicemail from the Phone app.

1. Open the **Phone** app.
2. At the bottom, tap **Dialpad**.
3. Touch and hold the number **1**.

Your phone calls your voicemail so you can listen.

---

## tr153-d
- task: Check voicemail and turn on visual voicemail | platform: Android (Phone app) | scenario: followup | sensitive: False
- sources: Phone app Help: How to check your voicemail <https://support.google.com/phoneapp/answer/2811844>

**USER:**
How do I hear my voicemail on my Android phone? I use the Phone app.

**ASSISTANT:**
I can help with that. Do you want to **call in** to hear your messages, or see them as a **list** on the screen?

**USER:**
a list on the screen please

**ASSISTANT:**
That is called visual voicemail. To turn it on:

1. Open the **Phone** app.
2. At the top right, tap **More options**, then **Settings**, then **Voicemail**.
3. Turn on **Visual voicemail**.

To listen, open the **Phone** app and tap **Voicemail** at the bottom. It works only with some carriers.

---

## tr153-e
- task: Check voicemail and turn on visual voicemail | platform: Android (Phone app) | scenario: constraint | sensitive: False
- sources: Phone app Help: How to check your voicemail <https://support.google.com/phoneapp/answer/2811844>

**USER:**
My son set up my Android phone and told me never to change anything in the settings. I just want to hear one voicemail right now in the Phone app, without changing any settings. Is that possible?

**ASSISTANT:**
Yes. Two ways need no settings.

From the notification:
1. Swipe down from the top of the screen.
2. Tap **Voicemail**.

Or by calling in:
1. Open the **Phone** app.
2. At the bottom, tap **Dialpad**.
3. Touch and hold **1**.

---

## tr153-r
- task: Check voicemail and turn on visual voicemail | platform: Android (Phone app) | scenario: failure_recovery | sensitive: False
- sources: Phone app Help: How to check your voicemail <https://support.google.com/phoneapp/answer/2811844>

**USER:**
How do I see my voicemails as a list in the Phone app on my Android?

**ASSISTANT:**
Turn on visual voicemail.

1. Open the **Phone** app.
2. At the top right, tap **More options**, then **Settings**, then **Voicemail**.
3. Turn on **Visual voicemail**.
4. To listen, open the **Phone** app and tap **Voicemail** at the bottom.

**USER:**
I turned it on but I can't find a Voicemail button at the bottom of the Phone app.

**ASSISTANT:**
If you can't find it, call your voicemail instead.

1. Open the **Phone** app.
2. At the bottom, tap **Dialpad**.
3. Touch and hold **1**.

Visual voicemail works only with some carriers, so it may not be available for yours.

---

## tr154-a
- task: Pair a Bluetooth accessory | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Find and set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604>

**USER:**
How do I connect my new wireless earbuds to my Pixel phone?

**ASSISTANT:**
Here is how to pair your earbuds with your phone:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your earbuds in the list.
5. Follow the on-screen prompts.

When it works, the earbuds show as **Connected**.

If you don't see **Pair new device**, look under **Available devices**, or tap the **More** icon and then **Refresh**.

---

## tr154-b
- task: Pair a Bluetooth accessory | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Find and set up Bluetooth devices near your Android device <https://support.google.com/android/answer/9417604>

**USER:**
I just bought something that connects to my phone with Bluetooth. How do I set it up?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---
