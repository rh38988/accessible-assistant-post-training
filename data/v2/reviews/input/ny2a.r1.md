# Review input: batch ny2a, round 1 (42 examples)

## tr134-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

**USER:**
The Mail app on my iPhone will not send or get any email. What should I do?

**ASSISTANT:**
Try these in order and stop when your email works.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider if two-step verification is turned on. You may need a special password from them to use email on your iPhone.
5. Make sure all your email is on the provider's website, because deleting the account can remove emails saved on the phone.
6. Open **Settings**, then tap **Apps**.
7. Tap **Mail**, then tap **Mail Accounts**.
8. Tap your account, then tap **Delete Account**.
9. Add the account again.

If that does not help, contact your email provider.

## tr134-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

**USER:**
I wrote my daughter a long note about Thursday's dinner on my iPhone, in the Mail app, and it keeps saying it was not sent. She says she never got it. I'm not very good with this. Is there somewhere the note might be waiting?

**ASSISTANT:**
Yes, an email that did not go out waits in the Outbox.

1. Open **Mail** and go to your list of mailboxes.
2. Tap **Outbox**. If there is no Outbox, your email was sent.
3. Tap the email.
4. Check that your daughter's address is correct.
5. Tap **Send**.

If it still will not send, make sure your iPhone is connected to the internet, and check with your email provider to see if it has an outage.

## tr134-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

**USER:**
my email is not working, can you help me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr134-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

**USER:**
my email is not working, can you help me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. Nothing new is coming in.

**ASSISTANT:**
Let's check these in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. Open **Settings**, then tap **Apps**.
4. Tap **Mail**, then tap **Mail Accounts**.
5. Tap **Fetch New Data**.
6. Choose a setting such as **Automatically** or **Manually**, or pick a schedule.

With **Automatically**, the iPhone fetches new mail in the background only when it is charging and on Wi-Fi.

## tr134-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

**USER:**
On my iPhone, the Mail app gets nothing new and my sent emails fail. I have years of old emails stored on this phone and I do not want to delete my account and lose them. What can I check instead?

**ASSISTANT:**
You can check these without deleting anything. Try them in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider if two-step verification or other security features are on. You may need a special password from them to use email on your iPhone.
5. Ask your provider to confirm that your account settings are correct.

Deleting the account is the last step on the list, and it can remove emails already downloaded to the phone, so you can leave it alone for now.

## tr134-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

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

## tr135-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Text messages will not send or arrive (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118433

**USER:**
My iPhone text will not send. There is a little red circle with an exclamation point next to it. What do I do?

**ASSISTANT:**
That red mark means the message was not delivered. Try this.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.
3. If it still will not send, tap the red exclamation point again.
4. Tap **Send as Text Message**. Messaging rates may apply.

If it still says Not Delivered after that, contact your carrier.

## tr135-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Text messages will not send or arrive (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118433

**USER:**
I have an iPhone and I like to send pictures of the grandkids to my family in a text. Lately the pictures will not go through, and a few I was sent do not show up either. I am not sure what to touch. Can you walk me through it?

**ASSISTANT:**
Let's try these.

1. Make sure your iPhone has enough storage to receive pictures and videos.
2. Open **Settings**, then tap **Apps**.
3. Tap **Messages**.
4. Turn on **Send Photo Previews** or **Low Quality Image Mode**.

Some carriers limit the size of attachments on regular text messages, and these settings help with that.

## tr135-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Text messages will not send or arrive (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118433

**USER:**
my texts are not working right, can you help

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr135-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Text messages will not send or arrive (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118433

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

## tr135-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Text messages will not send or arrive (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118433

**USER:**
My iPhone shows Not Delivered under my message to my neighbor, with a red exclamation point. I do not want to be charged for sending a regular text message. What can I try?

**ASSISTANT:**
You can try this without sending a regular text.

1. Check that your iPhone has a network connection.
2. Tap the red exclamation point, then tap **Try Again**.

A blue bubble message goes over Wi-Fi or cellular data, so it does not need a text-messaging plan.

If it still will not send, the only other choice is **Send as Text Message**, and messaging rates may apply. If you would rather not use it, contact your carrier.

## tr135-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Text messages will not send or arrive (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118433

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

## tr136-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000

**USER:**
My iPhone says No Service at the top of the screen and I cannot make calls. What do I do?

**ASSISTANT:**
Try these in order and stop when your bars come back.

1. Open **Settings**.
2. Turn on **Airplane Mode** and wait at least 15 seconds.
3. Turn **Airplane Mode** off.
4. Restart your iPhone.
5. Contact your carrier. Ask them to check that your account is active, that you are in a coverage area with no outage, and that your device is not blocked and has the correct data plan.
6. Update your iPhone to the latest iOS.

## tr136-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000

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

## tr136-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000

**USER:**
my phone says no service. help!

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr136-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000

**USER:**
my phone says no service. help!

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. It says SOS in the corner.

**ASSISTANT:**
SOS means your iPhone cannot reach your cellular network. In Australia, Canada, and the United States it can still make emergency calls through other carrier networks.

To get your service back:

1. Open **Settings**.
2. Turn on **Airplane Mode** for at least 15 seconds, then turn it off.
3. Restart your iPhone.
4. Contact your carrier to check your account and coverage.

## tr136-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000

**USER:**
My iPhone says No Service. I am waiting on a download and I do not want to restart the phone right now. I do have Wi-Fi at home. What else can I try?

**ASSISTANT:**
You can try these without restarting.

1. Open **Settings**.
2. Turn on **Airplane Mode** and wait at least 15 seconds, then turn it off.
3. With Wi-Fi connected, tap **General**, then tap **About**.
4. If an update is available, you will see an option to update your carrier settings. Tap it.
5. If you still see No Service, contact your carrier to check your account, coverage, and that your device is not blocked.

You can restart the iPhone later if you need to.

## tr136-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000

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
2. Update your iPhone to the latest iOS.
3. If you still see No Service after that, contact your carrier again.

## tr137-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: The screen is too sensitive or only responds to touch some of the time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102567

**USER:**
The screen on my iPhone only works some of the time when I touch it. What can I do?

**ASSISTANT:**
Try these in order.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug anything connected to the charging port, such as a cable or other accessory.
4. Take off any case or screen protector.

If the screen still does not work after that, you may need to arrange service for your iPhone with Apple.

## tr137-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: The screen is too sensitive or only responds to touch some of the time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102567

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

## tr137-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: The screen is too sensitive or only responds to touch some of the time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102567

**USER:**
my phone screen is acting up when i touch it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr137-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: The screen is too sensitive or only responds to touch some of the time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102567

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

## tr137-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: The screen is too sensitive or only responds to touch some of the time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102567

**USER:**
My iPhone screen only reacts to my finger some of the time. I just paid to have a screen protector put on and I really do not want to take it off. What else can I try first?

**ASSISTANT:**
You can try these first.

1. Restart your iPhone.
2. Make sure the screen is clean and free of any debris or water.
3. Unplug any accessories connected to the charging port.

If the screen still acts up, the next step is removing any case or screen protector. If you would rather keep it on, the other option is to arrange service for your iPhone with Apple.

## tr137-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: The screen is too sensitive or only responds to touch some of the time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102567

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

## tr138-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

**USER:**
My iPhone got really hot and a screen came up with a temperature warning. What should I do?

**ASSISTANT:**
Do this to let it cool safely.

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

An iPhone showing this warning screen might still be able to make emergency calls.

## tr138-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

**USER:**
We were driving to my cousin's house on a sunny afternoon with my iPhone on the dashboard using the maps, and the screen suddenly went black and said Temperature: iPhone needs to cool down. I was scared it broke. It is an iPhone. Is it ruined?

**ASSISTANT:**
It is not broken. The iPhone got too hot in the sun and turned the screen off to cool down. The spoken directions keep going, and the screen lights up near a turn.

To cool it down:

1. Turn off your iPhone.
2. Move it to a cooler place, away from direct sunlight.
3. Let it cool down before you use it again.

Long use of GPS navigation in heat or direct sun can cause this, and leaving the phone in a car on a hot day should be avoided.

## tr138-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

**USER:**
my phone is burning hot, what do i do

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr138-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

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

## tr138-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

**USER:**
My iPhone is showing a temperature warning, but I am waiting on an important call from the hospital and I do not want to turn it off. Is there another way to cool it down?

**ASSISTANT:**
The usual steps for a temperature warning start with turning the iPhone off, and I cannot offer another way to cool it. The closest option is this:

1. Move your iPhone to a cooler place, away from direct sunlight.
2. Let it cool down before you use it again.

An iPhone showing the warning screen might still be able to make emergency calls.

## tr138-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

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

## tr139-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619

**USER:**
The time on my iPhone is wrong. How do I get it to fix itself?

**ASSISTANT:**
Let your iPhone set the time on its own.

1. Make sure your iPhone is connected to the internet.
2. Open **Settings**, then tap **General**.
3. Tap **Date & Time**.
4. Turn on **Set Time Automatically**.

If the time zone is still wrong, let the iPhone use your location for it:

1. Open **Settings**, then tap **Privacy & Security**.
2. Tap **Location Services**, then scroll to the bottom and tap **System Services**.
3. Turn on **Setting Time Zone**.

## tr139-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619

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

## tr139-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619

**USER:**
everything on my phone shows the wrong day and hour lately, can you help me fix it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr139-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619

**USER:**
everything on my phone shows the wrong day and hour lately, can you help me fix it

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. The date and time are both off.

**ASSISTANT:**
Let's turn on automatic time.

1. Make sure your iPhone is connected to the internet.
2. Open **Settings**, then tap **General**.
3. Tap **Date & Time**.
4. Turn on **Set Time Automatically**.

If a message says updated time zone information is available, restart your iPhone.

## tr139-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619

**USER:**
My iPhone shows the wrong time. I do not have Wi-Fi or any data right now because I am out at the lake, so the automatic setting will not work. Can I fix it by hand?

**ASSISTANT:**
Yes, you can set it by hand.

1. Open **Settings**, then tap **General**.
2. Tap **Date & Time**.
3. Turn off **Set Automatically**.
4. To change the time zone, tap **Time Zone** and enter a city in the zone you need.
5. To change the date or time, tap the date and set it.

## tr139-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619

**USER:**
my iphone shows the wrong time. how do i fix it

**ASSISTANT:**
Try this.

1. Make sure your iPhone is connected to the internet.
2. Open **Settings**, then tap **General**.
3. Tap **Date & Time**.
4. Turn on **Set Time Automatically**.

**USER:**
The switch is gray and I cannot turn it on.

**ASSISTANT:**
A gray switch means the setting is dimmed. It can happen for a few reasons.

1. Someone may have set a Screen Time passcode on this iPhone.
2. The iPhone may have a work profile with device restrictions.
3. With some carriers, or in some countries and regions, the option is not available.

## tr140-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Make the screen brighter or dimmer (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/109351

**USER:**
I can barely read my iPhone in the kitchen, the screen looks so dim. Can I turn it up somehow?

**ASSISTANT:**
You can change it in Settings.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Drag the slider to the right to make the screen brighter.

Drag it to the left to make the screen dimmer.

## tr140-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Make the screen brighter or dimmer (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/109351

**USER:**
I have an old iPhone 7 that my son gave me. It is too bright at night and hurts my eyes when I read in bed. He said there is a quick way to dim it without going into the Settings, but I forgot what he showed me.

**ASSISTANT:**
Yes, use Control Center. On an iPhone 7 it works like this.

1. Swipe up from the bottom edge of the screen.
2. Drag the brightness bar down to make the screen dimmer.

Drag the bar up to make the screen brighter.

## tr140-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Make the screen brighter or dimmer (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/109351

**USER:**
my screen is too dark and i cannot see anything

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr140-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Make the screen brighter or dimmer (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/109351

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

## tr140-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Make the screen brighter or dimmer (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/109351

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

## tr140-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Make the screen brighter or dimmer (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/109351

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
