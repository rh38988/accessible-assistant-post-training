# Review input: batch ny2a, round 2 (13 examples)

## tr134-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Cannot send or receive email in the Mail app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102578

**USER:**
The Mail app on my iPhone will not send or get any email. What should I do?

**ASSISTANT:**
Try these first, in order, and stop when your email works.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider if two-step verification is turned on. You may need a special password from them to use email on your iPhone.
5. Open **Settings**, then tap **Apps**.
6. Tap **Mail**, then tap **Mail Accounts**.
7. Tap **Fetch New Data**, then choose **Automatically**, **Manually**, or a schedule.

Last resort, only if nothing above works: removing the account can delete emails already saved on your phone. So first, on a computer, sign in to your provider's website and make sure all your email is there or saved somewhere other than the phone. Then:

1. Open **Settings**, tap **Apps**, then tap **Mail**.
2. Tap **Mail Accounts**, tap your account, then tap **Delete Account**.
3. Add the account again.

If that does not help, contact your email provider.

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
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Open **Settings**, then tap **Apps**.
5. Tap **Mail**, then tap **Mail Accounts**.
6. Tap **Fetch New Data**.
7. Tap **Automatically** (or **Manually**, or pick a schedule).

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
3. Open **Settings**, then tap **Apps**. Tap **Mail**, then **Mail Accounts**, then **Fetch New Data**. Choose **Automatically**, **Manually**, or a schedule.
4. In a web browser, sign in to your provider's website to confirm your email address and password.
5. Ask your provider if two-step verification or other security features are on. You may need a special password from them to use email on your iPhone.
6. Ask your provider to confirm that your account settings are correct.

Deleting the account is the last step on the list, and it can remove emails already downloaded to the phone, so you can leave it alone for now.

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
4. Look for **Send Photo Previews** or **Low Quality Image Mode** and turn on whichever one you see.

Some carriers limit the size of attachments on regular text messages, and these settings help with that.

If pictures still will not go through, ask your carrier whether it supports MMS (picture messages) for your plan.

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
3. Restart your iPhone.
4. Check that your neighbor's phone number or email address is correct in the contact.

A blue bubble message goes over Wi-Fi or cellular data, so it does not need a text-messaging plan.

If it still will not send, **Send as Text Message** is another option, but messaging rates may apply. If you do not want that, contact Apple Support for blue bubble (iMessage) problems.

## tr136-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

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

## tr136-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

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
5. If it still says SOS, update your iPhone. Plug it in and connect to Wi-Fi, open **Settings**, tap **General**, then tap **Software Update**. If an update is shown, tap **Download and Install**.

## tr136-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

**USER:**
My iPhone says No Service. I am waiting on a download and I do not want to restart the phone right now. I do have Wi-Fi at home. What else can I try?

**ASSISTANT:**
You can try these without restarting.

1. Stay connected to Wi-Fi, open **Settings**, tap **General**, then tap **About**.
2. If an update is available, you will see an option to update your carrier settings. Tap it. If no update shows, there is nothing more to do here.
3. Turn on **Airplane Mode** and wait at least 15 seconds, then turn it off. This may pause your download, so you may prefer to do it after the download finishes.
4. If you still see No Service, contact your carrier to check your account, coverage, and that your device is not blocked.
5. When your download is done, plug in your iPhone, open **Settings**, tap **General**, then tap **Software Update**. If an update is available, tap **Download and Install**.

You can restart the iPhone later if you need to.

## tr136-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Phone shows No Service or SOS (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

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

## tr138-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: The phone is too hot or shows a temperature warning (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118431

**USER:**
My iPhone is showing a temperature warning, but I am waiting on an important call from the hospital and I do not want to turn it off. Is there another way to cool it down?

**ASSISTANT:**
The usual steps for a temperature warning start with turning the iPhone off, and I cannot offer another way to cool it. The closest option is this:

1. Move your iPhone to a cooler place, away from direct sunlight.

Apple says to let the iPhone cool down before using it again, so I cannot promise it will work for your call. If the call is important, it may be safer to turn it off and let it cool, or ask the hospital for another number to call.

## tr139-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619 ; https://support.apple.com/en-us/118575

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

## tr139-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Fix the wrong date or time (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101619 ; https://support.apple.com/en-us/118575

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
A gray switch means the setting is dimmed. It can happen for a few reasons, and each has a next step.

1. Someone may have set a Screen Time passcode on this iPhone. Ask the person who set it up, or enter the passcode if you know it.
2. The iPhone may have a corporate profile with device restrictions. Ask whoever manages it, such as your workplace's IT help.
3. With some carriers, or in some countries and regions, the option is not available. You cannot turn it on, so set the time by hand instead. Open **Settings**, tap **General**, tap **Date & Time**, and if **Set Automatically** is not locked, turn it off. Then tap **Time Zone**, or tap the date.
