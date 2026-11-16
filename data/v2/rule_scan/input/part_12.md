# Rule scan input, part 12 (50 examples)

## tr134-r
- task: Cannot send or receive email in the Mail app | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If you can't receive email on your iPhone or iPad (send steps from Apple Support: If you can't send email on your iPhone or iPad, support.apple.com/en-us/102556) <https://support.apple.com/en-us/102578>

**USER:**
email on my iphone stopped coming in. nothing new since yesterday. it is the Mail app

**ASSISTANT:**
Let's check these in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Open **Settings**, tap **Apps**, then tap **Mail**.
5. Tap **Mail Accounts**, then tap **Fetch New Data**.
6. Choose a setting such as **Automatically** or **Manually**, or pick a schedule.

**USER:**
I signed in on the website and my password works fine there. But the Mail app on the phone still says my password is wrong.

**ASSISTANT:**
Then the provider needs to look at it.

1. Contact your email provider or system administrator about the user name or password error.
2. Ask them if two-step verification or other security features are on. You may need a special password or authorization from them to use email on your iPhone.
3. Ask them to confirm your account settings are correct.

---

## tr135-a
- task: Text messages will not send or arrive | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If you can't send or receive messages on your iPhone or iPad <https://support.apple.com/en-us/118433>

**USER:**
My iPhone text will not send. There is a little red circle with an exclamation point next to it. What do I do?

**ASSISTANT:**
That red mark means the message was not delivered. Try this.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.
3. If it still will not send, tap the red exclamation point again.
4. Tap **Send as Text Message**. Messaging rates may apply.

If it still says Not Delivered after that, contact your carrier.

---

## tr135-c
- task: Text messages will not send or arrive | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: If you can't send or receive messages on your iPhone or iPad <https://support.apple.com/en-us/118433>

**USER:**
I have an iPhone and I like to send pictures of the grandkids to my family in a text. Lately the pictures will not go through, and a few I was sent do not show up either. I am not sure what to touch. Can you walk me through it?

**ASSISTANT:**
Let's try these.

1. Make sure your iPhone has enough storage to receive pictures and videos.
2. Open **Settings**, then tap **Apps**.
3. Tap **Messages**.
4. Look for **Send Photo Previews** or **Low Quality Image Mode** and turn on whichever one you see.
5. Restart your iPhone.

Your carrier may limit the size of picture messages. Turning on Send Photo Previews or Low Quality Image Mode lets you send pictures at a lower quality when full-size pictures will not go through.

If pictures still will not go through, ask your carrier whether it supports MMS (picture messages) for your plan.

---

## tr135-d
- task: Text messages will not send or arrive | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: If you can't send or receive messages on your iPhone or iPad <https://support.apple.com/en-us/118433>

**USER:**
my texts are not working right, can you help

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. I get my messages on my iPad but not on the iPhone.

**ASSISTANT:**
Let's check where your iPhone receives messages.

1. Open **Settings**, then tap **Apps**.
2. Tap **Messages**, then tap **Send & Receive**.
3. Choose your phone number or email address.

If your phone number does not appear, link your iPhone number to your Apple Account, or set up Text Message Forwarding.

---

## tr135-e
- task: Text messages will not send or arrive | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: If you can't send or receive messages on your iPhone or iPad <https://support.apple.com/en-us/118433>

**USER:**
My iPhone shows Not Delivered under my message to my neighbor, with a red exclamation point. I do not want to be charged for sending a regular text message. What can I try?

**ASSISTANT:**
You can try this without sending a regular text.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.
3. Restart your iPhone.
4. Check that your neighbor's phone number or email address is correct in the contact.

A blue bubble message goes over Wi-Fi or cellular data, so it does not need a text-messaging plan.

If it still will not send, tap the red exclamation point again, then tap **Send as Text Message**, but only if you are fine with messaging rates. Messaging rates may apply. If you do not want that, contact Apple Support for blue bubble (iMessage) problems.

---

## tr135-r
- task: Text messages will not send or arrive | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If you can't send or receive messages on your iPhone or iPad <https://support.apple.com/en-us/118433>

**USER:**
my iphone says Not Delivered under the text i sent my son. there is a red exclamation point

**ASSISTANT:**
Try this.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.
3. If it still will not send, tap the red exclamation point again.
4. Tap **Send as Text Message**. Messaging rates may apply.

**USER:**
I did both of those and it still says Not Delivered.

**ASSISTANT:**
Here is what to try next.

1. Restart your iPhone.
2. Check that your son's phone number or email address is correct in the contact.
3. Make sure your iPhone has Wi-Fi or cellular data.
4. If it still fails, contact your carrier.

---

## tr136-a
- task: Phone shows No Service or SOS | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If you see SOS, No Service, or Searching on your iPhone or iPad <https://support.apple.com/en-us/120000>; Apple Support: Update your iPhone or iPad <https://support.apple.com/en-us/118575>

**USER:**
My iPhone says No Service at the top of the screen and I cannot make calls. What do I do?

**ASSISTANT:**
Try these in order and stop when your bars come back.

1. Open **Settings**.
2. Turn on **Airplane Mode** and wait at least 15 seconds.
3. Turn **Airplane Mode** off.
4. Restart your iPhone.
5. Contact your carrier. Ask them to check that your account is active, that you are in a coverage area with no outage, and that your device is not blocked and has the correct data plan.
6. Plug in your iPhone and connect to Wi-Fi.
7. Open **Settings**, tap **General**, then tap **Software Update**.
8. If an update is available, tap **Download and Install** and follow the instructions on the screen.
9. Make sure your iPhone is connected to Wi-Fi.
10. Open **Settings**, tap **General**, then tap **About**.
11. If an update is available, you will see an option to update your carrier settings. Tap it.

---

## tr136-b
- task: Phone shows No Service or SOS | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If you see SOS, No Service, or Searching on your iPhone or iPad <https://support.apple.com/en-us/120000>

**USER:**
my phone says no service. help!

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr136-c
- task: Phone shows No Service or SOS | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: If you see SOS, No Service, or Searching on your iPhone or iPad <https://support.apple.com/en-us/120000>

**USER:**
We flew to Spain for my sister's wedding and as soon as we landed my iPhone started saying No Service. I only have the one SIM, nothing fancy, and I did not change any settings before we left. My husband says there is a roaming switch somewhere. Where is it?

**ASSISTANT:**
Yes, the roaming switch is in your Cellular settings.

1. Open **Settings**.
2. Tap **Cellular** (it may say **Cellular Data**).
3. Turn on **Cellular Data**.
4. Tap **Cellular Data Options**.
5. Turn on **Data Roaming**.

If you still see No Service, turn **Airplane Mode** on for at least 15 seconds and then off, restart your iPhone, and contact your carrier.

---

## tr136-r
- task: Phone shows No Service or SOS | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If you see SOS, No Service, or Searching on your iPhone or iPad <https://support.apple.com/en-us/120000>; Apple Support: Update your iPhone or iPad <https://support.apple.com/en-us/118575>

**USER:**
iphone says No Service since this morning. what should i do

**ASSISTANT:**
Try these first.

1. Open **Settings**.
2. Turn on **Airplane Mode** for at least 15 seconds, then turn it off.
3. Restart your iPhone.

**USER:**
I did the airplane mode and restarted it. Still No Service.

**ASSISTANT:**
The next step is your carrier.

1. Contact your carrier. Ask them to verify that your account is active and in good standing, that you are in a coverage area with no outages, and that your device is not blocked and has the correct data plan.
2. Plug in your iPhone and connect to Wi-Fi. Open **Settings**, tap **General**, then tap **Software Update**. If an update is available, tap **Download and Install**.
3. With Wi-Fi connected, open **Settings**, tap **General**, then tap **About**. If an update is available, you will see an option to update your carrier settings. Tap it.
4. If your carrier says your account and network are fine and you think the phone itself has a problem, get service from Apple.

---

## tr137-a
- task: The screen is too sensitive or only responds to touch some of the time | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If the screen isn't working on your iPhone or iPad <https://support.apple.com/en-us/102567>

**USER:**
The screen on my iPhone only works some of the time when I touch it. What can I do?

**ASSISTANT:**
Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug anything connected to the charging port, such as a cable or other accessory.
4. Take off any case or screen protector.

If the screen still does not work after that, you may need to arrange service for your iPhone with Apple.

---

## tr137-b
- task: The screen is too sensitive or only responds to touch some of the time | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If the screen isn't working on your iPhone or iPad <https://support.apple.com/en-us/102567>

**USER:**
my phone screen is acting up when i touch it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr137-c
- task: The screen is too sensitive or only responds to touch some of the time | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: If the screen isn't working on your iPhone or iPad <https://support.apple.com/en-us/102567>

**USER:**
My iPhone has gone strange. Sometimes it acts like I am touching the screen when I am not, and the letters jump around when I type an email. It has a clear case on it and I usually leave it plugged in by my bed. I have an iPhone. Where do I start?

**ASSISTANT:**
That sounds like the screen is too sensitive. Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug the charging cable and any other accessory connected to the charging port.
4. If the screen works after unplugging, try a different outlet, cable, or charger.
5. Take off the case and any screen protector.

If the screen still does not work, you may need to arrange service for your iPhone with Apple.

---

## tr137-d
- task: The screen is too sensitive or only responds to touch some of the time | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: If the screen isn't working on your iPhone or iPad <https://support.apple.com/en-us/102567>

**USER:**
my phone screen is acting up when i touch it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. It only answers my touch every now and then.

**ASSISTANT:**
Let's go through these in order.

1. Restart your iPhone.
2. Wipe the screen so it is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.
4. Remove any case or screen protector.

If it still does not respond, you may need to arrange service for your iPhone with Apple.

---

## tr137-e
- task: The screen is too sensitive or only responds to touch some of the time | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: If the screen isn't working on your iPhone or iPad <https://support.apple.com/en-us/102567>

**USER:**
My iPhone screen only reacts to my finger some of the time. I just paid to have a screen protector put on and I really do not want to take it off. What else can I try first?

**ASSISTANT:**
You can try these first.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.

If the screen still acts up, the next step is removing any case or screen protector. If you would rather keep it on, the other option is to arrange service for your iPhone with Apple.

---

## tr137-r
- task: The screen is too sensitive or only responds to touch some of the time | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If the screen isn't working on your iPhone or iPad <https://support.apple.com/en-us/102567>

**USER:**
my iphone screen keeps jumping around and only works sometimes. what do i do

**ASSISTANT:**
Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.
4. Take off any case or screen protector.

**USER:**
When I unplugged the charger the screen worked fine. But it starts jumping again when I plug it back in.

**ASSISTANT:**
That points to the charger, not the screen.

1. Try a different outlet.
2. Try a different cable.
3. Try a different charger.

If the screen still does not work, you may need to arrange service for your iPhone with Apple.

---

## tr138-a
- task: The phone is too hot or shows a temperature warning | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If your iPhone or iPad gets too hot or too cold <https://support.apple.com/en-us/118431>

**USER:**
My iPhone got really hot and a screen came up with a temperature warning. What should I do?

**ASSISTANT:**
Do this to let it cool safely.

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

An iPhone showing this warning screen might still be able to make emergency calls.

---

## tr138-b
- task: The phone is too hot or shows a temperature warning | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If your iPhone or iPad gets too hot or too cold <https://support.apple.com/en-us/118431>

**USER:**
my phone is burning hot, what do i do

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr138-c
- task: The phone is too hot or shows a temperature warning | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: If your iPhone or iPad gets too hot or too cold <https://support.apple.com/en-us/118431>

**USER:**
We were driving to my cousin's house on a sunny afternoon with my iPhone on the dashboard using the maps, and the screen suddenly went black and said Temperature: iPhone needs to cool down. I was scared it broke. It is an iPhone. Is it ruined?

**ASSISTANT:**
It is not broken. The iPhone got too hot in the sun and turned the screen off to cool down. The spoken directions keep going, and the screen lights up near a turn.

To cool it down:

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

Long use of GPS navigation in heat or direct sun can cause this, and leaving the phone in a car on a hot day should be avoided.

---

## tr138-d
- task: The phone is too hot or shows a temperature warning | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: If your iPhone or iPad gets too hot or too cold <https://support.apple.com/en-us/118431>

**USER:**
my phone is burning hot, what do i do

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. It feels hot while it charges and I do not see any warning.

**ASSISTANT:**
An iPhone can feel warm during wireless charging, setup, a restore from backup, a big software update, camera use, or video streaming. It cools down when that activity ends. If no temperature warning appears, you can keep using it.

If a temperature warning does appear:

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

---

## tr138-r
- task: The phone is too hot or shows a temperature warning | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If your iPhone or iPad gets too hot or too cold <https://support.apple.com/en-us/118431>

**USER:**
my iphone is too hot and shows a temperature warning, what do i do

**ASSISTANT:**
Do this.

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

**USER:**
It cooled down, but now when I plug it in the Lock Screen says Charging On Hold.

**ASSISTANT:**
That message is expected after it got hot.

1. Keep your iPhone in a cooler place, away from direct sunlight.
2. Wait for it to return to normal temperature.

Charging resumes when the iPhone is back to normal temperature.

---

## tr139-a
- task: Fix the wrong date or time | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If you can't change the time or time zone on your Apple device <https://support.apple.com/en-us/101619>; Apple Support: Update your iPhone or iPad <https://support.apple.com/en-us/118575>

**USER:**
The time on my iPhone is wrong. How do I get it to fix itself?

**ASSISTANT:**
Let your iPhone set the time on its own.

1. Make sure your iPhone is connected to the internet.
2. Install the latest iPhone update if one is waiting. Open **Settings**, tap **General**, tap **Software Update**, then tap **Download and Install**.
3. Open **Settings**, then tap **General**.
4. Tap **Date & Time**.
5. Turn on **Set Time Automatically**.
6. If a message says updated time zone information is available, restart your iPhone.

If the time zone is still wrong, let the iPhone use your location for it:

1. Open **Settings**, then tap **Privacy & Security**.
2. Tap **Location Services**, then scroll to the bottom and tap **System Services**.
3. Turn on **Setting Time Zone**.

---

## tr139-b
- task: Fix the wrong date or time | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If you can't change the time or time zone on your Apple device <https://support.apple.com/en-us/101619>

**USER:**
everything on my phone shows the wrong day and hour lately, can you help me fix it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr139-c
- task: Fix the wrong date or time | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: If you can't change the time or time zone on your Apple device <https://support.apple.com/en-us/101619>

**USER:**
I moved from the East Coast to the West Coast to be near my kids and my iPhone still shows the old time zone, so I keep missing my appointments. I do not want the automatic thing, I just want to pick the time zone myself. It is an iPhone.

**ASSISTANT:**
You can choose it yourself.

1. Open **Settings**, then tap **General**.
2. Tap **Date & Time**.
3. Turn off **Set Automatically**.
4. Tap **Time Zone**.
5. Type a city in the time zone you need and tap it.

To change the date or time instead, tap the date and set it by hand.

---

## tr139-d
- task: Fix the wrong date or time | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: If you can't change the time or time zone on your Apple device <https://support.apple.com/en-us/101619>; Apple Support: Update your iPhone or iPad <https://support.apple.com/en-us/118575>

**USER:**
everything on my phone shows the wrong day and hour lately, can you help me fix it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. The date and time are both off.

**ASSISTANT:**
Let's turn on automatic time.

1. Make sure your iPhone is connected to the internet.
2. Install the latest iPhone update if one is waiting. Open **Settings**, tap **General**, tap **Software Update**, then tap **Download and Install**.
3. Open **Settings**, then tap **General**.
4. Tap **Date & Time**.
5. Turn on **Set Time Automatically**.

If a message says updated time zone information is available, restart your iPhone.

If the time zone is still wrong, open **Settings**, tap **Privacy & Security**, tap **Location Services**, scroll to the bottom and tap **System Services**, then turn on **Setting Time Zone**.

---

## tr139-e
- task: Fix the wrong date or time | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: If you can't change the time or time zone on your Apple device <https://support.apple.com/en-us/101619>

**USER:**
My iPhone shows the wrong time. I do not have Wi-Fi or any data right now because I am out at the lake, so the automatic setting will not work. Can I fix it by hand?

**ASSISTANT:**
Yes, you can set it by hand.

1. Open **Settings**, then tap **General**.
2. Tap **Date & Time**.
3. Turn off **Set Automatically**.
4. To change the time zone, tap **Time Zone** and enter a city in the zone you need.
5. To change the date or time, tap the date and set it.

---

## tr140-a
- task: Make the screen brighter or dimmer | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Adjust the brightness and color temperature on your iPhone or iPad <https://support.apple.com/en-us/109351>

**USER:**
I can barely read my iPhone in the kitchen, the screen looks so dim. Can I turn it up somehow?

**ASSISTANT:**
You can change it in Settings.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Drag the slider to the right to make the screen brighter.

Drag it to the left to make the screen dimmer.

---

## tr140-b
- task: Make the screen brighter or dimmer | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Adjust the brightness and color temperature on your iPhone or iPad <https://support.apple.com/en-us/109351>

**USER:**
my screen is too dark and i cannot see anything

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr140-c
- task: Make the screen brighter or dimmer | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Adjust the brightness and color temperature on your iPhone or iPad <https://support.apple.com/en-us/109351>

**USER:**
I have an old iPhone 7 that my son gave me. It is too bright at night and hurts my eyes when I read in bed. He said there is a quick way to dim it without going into the Settings, but I forgot what he showed me.

**ASSISTANT:**
Yes, use Control Center. On an iPhone 7 it works like this.

1. Swipe up from the bottom edge of the screen.
2. Drag the brightness bar down to make the screen dimmer.

Drag the bar up to make the screen brighter.

---

## tr140-d
- task: Make the screen brighter or dimmer | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Adjust the brightness and color temperature on your iPhone or iPad <https://support.apple.com/en-us/109351>

**USER:**
my screen is too dark and i cannot see anything

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. I want a quick way to change it.

**ASSISTANT:**
Use Control Center.

1. On an iPhone X or later, swipe down from the top-right corner of the screen. On an iPhone 8 or earlier, swipe up from the bottom edge.
2. Drag the brightness bar up to make the screen brighter.

Drag the bar down to make it dimmer.

---

## tr140-e
- task: Make the screen brighter or dimmer | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Adjust the brightness and color temperature on your iPhone or iPad <https://support.apple.com/en-us/109351>

**USER:**
My iPhone keeps changing how bright the screen is by itself, and I want it to stay exactly where I put it. How do I stop that, and then how do I set it myself?

**ASSISTANT:**
First turn off Auto-Brightness.

1. Open **Settings**, then tap **Accessibility**.
2. Tap **Display & Text Size**.
3. Scroll to **Auto-Brightness** and tap it to turn it off.

Now set the brightness yourself.

1. Go back to **Settings** and tap **Display & Brightness**.
2. Drag the slider right for brighter or left for dimmer.

---

## tr140-r
- task: Make the screen brighter or dimmer | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Adjust the brightness and color temperature on your iPhone or iPad <https://support.apple.com/en-us/109351>

**USER:**
how do i make my iphone screen brighter

**ASSISTANT:**
Here is how.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Drag the slider to the right.

**USER:**
I dragged it all the way to the right and the screen still looks dim. The phone feels warm too.

**ASSISTANT:**
The warmth is likely the reason.

1. If your iPhone is too warm, the display may dim and its top brightness is lowered until it cools down. Let it cool.
2. If it is not warm and the brightness still looks wrong, open **Settings** and tap **Accessibility**.
3. Tap **Display & Text Size**, then scroll to **Auto-Brightness**.
4. Turn it off, then turn it back on.

---

## tr141-a
- task: Set up and listen to voicemail | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up voicemail / Check voicemail <https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0>

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

---

## tr141-b
- task: Set up and listen to voicemail | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up voicemail / Check voicemail <https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0>

**USER:**
Can you help me set up voicemail on my phone?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr141-c
- task: Set up and listen to voicemail | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up voicemail / Check voicemail <https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0>

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

---

## tr141-d
- task: Set up and listen to voicemail | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up voicemail / Check voicemail <https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0>

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

---

## tr141-r
- task: Set up and listen to voicemail | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up voicemail / Check voicemail <https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0>

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

---

## tr142-a
- task: Forward calls to another number | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up call forwarding on iPhone <https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios>

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

---

## tr142-b
- task: Forward calls to another number | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up call forwarding on iPhone <https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios>

**USER:**
I need my calls to go to my sister's number for a week. How?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr142-d
- task: Forward calls to another number | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up call forwarding on iPhone <https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios>

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

---

## tr142-e
- task: Forward calls to another number | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up call forwarding on iPhone <https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios>

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

---

## tr142-r
- task: Forward calls to another number | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: iPhone User Guide, Set up call forwarding on iPhone <https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios>

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

---

## tr143-a
- task: Make the light flash for alerts | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Get LED flash alerts on your iPhone or iPad <https://support.apple.com/en-us/111774>

**USER:**
I have trouble hearing my iPhone. Can I make the little light on the back flash when I get an alert?

**ASSISTANT:**
Yes, your iPhone can blink its light for alerts.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

After that, the light next to the camera lens blinks when you get a notification. This only works while the phone is locked.

---

## tr143-b
- task: Make the light flash for alerts | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Get LED flash alerts on your iPhone or iPad <https://support.apple.com/en-us/111774>

**USER:**
My hearing isn't good. Is there a way to have a light blink on my phone instead of a sound?

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr143-c
- task: Make the light flash for alerts | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Get LED flash alerts on your iPhone or iPad <https://support.apple.com/en-us/111774>

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

---

## tr143-d
- task: Make the light flash for alerts | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Get LED flash alerts on your iPhone or iPad <https://support.apple.com/en-us/111774>

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

---

## tr143-e
- task: Make the light flash for alerts | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Get LED flash alerts on your iPhone or iPad <https://support.apple.com/en-us/111774>

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

---

## tr144-a
- task: Find the model number of the iPhone to identify which model it is | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Find the model number of your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/106343>

**USER:**
How can I find out which model my iPhone is? I'm trying to sell it.

**ASSISTANT:**
You can find the model number in Settings.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. The part number is shown to its right.
5. Tap that part number and it changes to the model number.

Use that number when you sell the phone.

---

## tr144-b
- task: Find the model number of the iPhone to identify which model it is | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Find the model number of your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/106343>

**USER:**
What model is my phone? The store wants to know.

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr144-c
- task: Find the model number of the iPhone to identify which model it is | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Find the model number of your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/106343>

**USER:**
I found my old iPhone 7 in a drawer, the one my late husband used. The battery is dead and I don't have the right charger so I can't turn it on. A repair shop asked me for the model number. Is there a way to see it without turning it on?

**ASSISTANT:**
Yes. On an iPhone 7 or earlier, the model number is on the back of the phone.

1. Turn the phone over so the back faces you.
2. Look at the writing on the back and find the model number.

---
