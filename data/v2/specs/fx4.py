"""fx4: new examples (e constraint, r failure_recovery) for the tasks in ex4.py."""
TASKS = [
    {
        "task_id": "TR-048", "task_type": "silence_unknown_callers", "task": "Silence calls from unknown numbers",
        "platform": "iPhone", "category": "communication", "sensitive": False,
        "source": {"title": "Apple Support: Manage unknown callers on iPhone", "url": "https://support.apple.com/en-us/111106"},
        "source_notes": """Screen or silence unknown callers: Settings > Apps > Phone (or FaceTime). In Phone, scroll to Screen Unknown Callers and choose Never (unsaved numbers ring like any other call), Ask Reason for Calling (caller is asked why they're calling before your phone rings), or Silence (calls silenced and sent to voicemail).
Filter unknown callers: Settings > Apps > Phone. Scroll to Call Filtering and turn on Unknown Callers. Missed calls and voicemails from unknown numbers move to your Unknown Callers list. To view it, tap the Filter button, then tap Unknown Callers. In the Phone app it appears in the Recents tab in Classic view or the Calls tab in Unified view.
Silence spam callers: Call Filtering, turn on your spam filter; view Spam list via Filter button > Spam.
Conditions: save important numbers in Contacts so they always come through. Call screening may use standard calling and data rates. Earlier than iOS 17 needs Live Voicemail on. Not screened while roaming. Calling emergency services turns screening off for 24 hours.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an iPhone and I'm waiting to hear from a new specialist's office, so I can't just send every unknown number to voicemail. But I am sick of the spam. Is there something in between?",
                 """Yes. On iPhone you can have unknown callers asked why they're calling before your phone rings.

1. Open the **Settings** app.
2. Tap **Apps**, then tap **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Ask Reason for Calling**.

The caller is asked why they're calling before your phone rings, so you can tell a real call from spam.

Calls from numbers saved in your Contacts always come through, so save the specialist's number once you have it. Call screening may use your standard calling and data rates.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Robocalls keep ringing my iPhone all day. How do I make it stop ringing for numbers I haven't saved?",
                 """You can silence calls from numbers you haven't saved. They go to voicemail.

1. Open the **Settings** app.
2. Tap **Apps**, then tap **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from your Contacts will still ring.""",
                 "I did that. Now my Recents list is a big mess and I can't tell which calls came from unknown numbers. Can I see just those?",
                 """Yes. Turn on a filter, then open the list.

1. Open **Settings**, tap **Apps**, then tap **Phone**.
2. Scroll to **Call Filtering** and turn on **Unknown Callers**.
3. In the Phone app, tap the **Filter** button, then tap **Unknown Callers**.

Missed calls and voicemails from unknown numbers now move to that list. In the Phone app it appears in the **Recents** tab in Classic view, or the **Calls** tab in Unified view.""",
             ]},
        ],
    },
    {
        "task_id": "TR-049", "task_type": "spam_call_filter", "task": "Filter spam calls",
        "platform": "Android (Pixel)", "category": "communication", "sensitive": False,
        "source": {"title": "Phone app Help: Use caller ID & spam protection", "url": "https://support.google.com/phoneapp/answer/3459196?hl=en"},
        "source_notes": """Turn caller ID & spam protection on or off: Open Phone app > More options > Settings > Caller ID and spam > turn See caller ID & spam on or off. Optional: turn on Filter spam calls to block spam on the phone. Enabled by default. Filter spam calls does not appear on devices with automatic Call Screen; there spam autoblocking is one of the Call Screen options. Filtered calls skip missed call and voicemail notifications, but they appear in call history and you can still check voicemail. Calls may be flagged with "Suspected spam caller" or "Spam" as the caller ID.
Block or report spam: Phone app > Home at bottom > tap the call > Block or Report spam.
Fix a number wrongly marked as spam: Phone app > Recent calls > tap the call labeled as spam > Not spam > Unblock.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "Pixel phone with the Google Phone app here. I don't want anything blocked or hidden, because my pharmacy calls from lots of different numbers. I just want the phone to warn me when a call looks like spam. What should I do?",
                 """You can have the Phone app warn you without blocking anything.

1. Open the **Phone** app.
2. Tap **More options** (three dots), then tap **Settings**.
3. Tap **Caller ID and spam**.
4. Make sure **See caller ID & spam** is on.
5. Leave **Filter spam calls** turned off.

Calls that look like spam may show **Suspected spam caller** or **Spam** as the caller ID, and your phone will still ring.

This setting is on by default, so it may already be on.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "My Pixel keeps ringing with robocalls. How do I make the Phone app block the spam ones?",
                 """You can turn on spam filtering in the Phone app.

1. Open the **Phone** app.
2. Tap **More options** (three dots), then tap **Settings**.
3. Tap **Caller ID and spam**.
4. Make sure **See caller ID & spam** is on.
5. Turn on **Filter spam calls**.

Filtered calls won't notify you, but they still show in your call history.""",
                 "I did that. But now a call from my dentist's office got marked as spam and I think it was blocked. Help!",
                 """You can fix that in a few taps.

1. Open the **Phone** app and tap **Recent calls**.
2. Tap the call that is labeled as spam.
3. Tap **Not spam**.
4. Tap **Unblock**.

Calls that were filtered still appear in your call history, and you can still check your voicemail.""",
             ]},
        ],
    },
    {
        "task_id": "TR-050", "task_type": "battery_health", "task": "Check battery health",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: iPhone battery and performance", "url": "https://support.apple.com/en-us/101575"},
        "source_notes": """Check: Settings app > Battery > Battery Health. Available on iPhone 6 and later.
Maximum capacity measures the battery capacity relative to when it was new. A lower value can mean fewer hours of use between charges.
Messages: Normal ("Your battery is currently supporting normal peak performance."); Significantly degraded ("Your battery's health is significantly degraded", does not indicate a safety issue); Service (an Apple Authorized Service Provider can replace the battery); Unable to verify ("Unable to verify this iPhone has a genuine Apple battery.", iPhone XS and later; health data on screen may be inaccurate, page recommends getting the battery checked; iPhone X and earlier show "Important Battery Message").
Tips: keep iPhone about half charged when storing long term; avoid charging or leaving it in hot environments, including direct sun, for long periods. Lifespan depends on charge cycles and how it is cared for.
Service: one-year warranty covers a defective battery; out-of-warranty battery service available for a charge.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I can't afford a new phone or a new battery right now, I'm on a fixed income. But my iPhone 8 doesn't hold a charge like it used to. Can you show me how to look at the battery and what I can do to make it last?",
                 """Looking at the battery costs nothing. Battery Health is available on iPhone 6 and later, so your iPhone 8 has it.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**.
4. Look at **Maximum Capacity**. It compares your battery now to when it was new. A lower number can mean fewer hours between charges.

Ways to take care of the battery:
- Avoid charging your iPhone or leaving it in hot places, such as direct sun, for long periods.
- If you store it for a long time, keep it about half charged.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone XR battery goes down fast. How can I see how healthy it is?",
                 """You can check it in Settings.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**.
4. Look at **Maximum Capacity**. It compares your battery now to when it was new.""",
                 "I did that, but there's no capacity number. It says Unable to verify this iPhone has a genuine Apple battery. What does that mean?",
                 """That message means the iPhone could not confirm that it has a genuine Apple battery. The battery health information on that screen might not be accurate, so don't rely on the numbers shown there.

To have the battery checked, follow the link **To have your battery checked, get service** on Apple's battery page. It goes to getsupport.apple.com.""",
             ]},
        ],
    },
    {
        "task_id": "TR-051", "task_type": "group_text", "task": "Start a group text",
        "platform": "iPhone", "category": "communication", "sensitive": False,
        "source": {"title": "Apple Support: Send a group text message on your iPhone or iPad", "url": "https://support.apple.com/en-us/118236"},
        "source_notes": """Send a group text: open Messages, tap the Compose button (square and pencil icon). Enter names, or tap the Add button (plus icon) to add people from Contacts. Type your message, tap the Send button (up arrow).
Before you start: update to the latest iOS.
Types chosen automatically: group iMessage (everyone on Apple devices with iMessage, blue bubbles); group MMS (any recipient not on iMessage, green bubbles, via carrier); group SMS (replies sent as individual texts).
Settings: Settings > Messages > turn on MMS Messaging to send group MMS on iPhone.
Troubleshooting: No MMS option: contact your carrier to check whether your plan supports Group MMS Messaging.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My hands shake and typing names on my iPhone is hard. I want to text my bridge club ladies all at once about Thursday. Can I pick them from my contacts instead of typing each name?",
                 """Yes, you can pick people from your contacts.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil).
3. Tap the **Add** button (a plus icon) to add people from your Contacts.
4. Choose each of the ladies you want in the group.
5. Type your message.
6. Tap the **Send** button (the up arrow).

Everyone in the group will get the message.

If someone in the group doesn't use an iPhone, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I send one message to my brother and two cousins at once on my iPhone? One cousin has an Android.",
                 """You can send a group text.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil).
3. Enter their names, or tap the **Add** button (a plus icon) to pick them from Contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

Because one person uses Android, go to **Settings**, then **Messages**, and turn on **MMS Messaging**.""",
                 "I went to Settings, then Messages, but there is no MMS Messaging switch. My cousin with the Android didn't get anything.",
                 """Group texts to people who don't use iMessage, like your cousin with the Android, use group MMS, and that needs **MMS Messaging** turned on. If you don't see that option, the next step is to check with your carrier.

1. Contact your phone carrier.
2. Ask whether your plan supports **Group MMS Messaging**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-052", "task_type": "browser_zoom", "task": "Make every web page bigger by default",
        "platform": "Chrome (computer)", "category": "technical_support", "sensitive": False,
        "source": {"title": "Google Chrome Help: Change text, image & video sizes (zoom), computer", "url": "https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop"},
        "source_notes": """Zoom one page: Chrome > More (three dots) top right > next to Zoom click Zoom in / Zoom out / Full screen. Keyboard: Ctrl and + (Windows, Linux, Chrome OS), Command and + (Mac).
Default for all pages: More > Settings > Appearance > next to Page zoom click the down arrow and select the zoom option.
Font size only: Appearance > next to Font size click the down arrow and select a size; Customize fonts for more options. Some websites don't let browsers change only the text size; on those Chrome can't adjust the font size.
Per-site zoom: More > Settings > Privacy and security > Site Settings > Additional content settings > Zoom levels; click X next to a site to remove that site's resize settings.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I use Chrome on my laptop. The writing on websites is too tiny for me, but the pictures are fine and I don't want those blown up. Can I make just the text bigger on every site?",
                 """Yes. You can change Chrome's font size.

1. Click the **More** menu (three dots) at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Next to **Font size**, click the down arrow and choose a bigger size.

If you want more choices, click **Customize fonts**.

Some websites don't let Chrome change only the text size. On those sites the text stays the same. If that happens, you can use **Page zoom** in the same **Appearance** section, but it makes pictures bigger too.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "chrome on my pc, how do i make all websites open bigger without zooming every time",
                 """You can set a bigger default size.

1. Click the **More** menu (three dots) at the top right.
2. Click **Settings**.
3. Click **Appearance**.
4. Next to **Page zoom**, click the down arrow and choose a bigger size.""",
                 "I did that and most sites are bigger, but my bank's website still looks small.",
                 """A site can have its own saved size. You can remove it.

1. Click **More**, then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Additional content settings**, then **Zoom levels**.
4. Click the **X** next to your bank's site.

That removes the site's own resize settings.""",
             ]},
        ],
    },
    {
        "task_id": "TR-054", "task_type": "share_location", "task": "Share location with family",
        "platform": "iPhone (Find My)", "category": "communication", "sensitive": True,
        "source": {"title": "Apple Support: Share your location with iPhone", "url": "https://support.apple.com/en-us/105104"},
        "source_notes": """Ongoing Live Location: Find My > Me tab, turn on Share My Location. People tab > Add button (plus icon) > Share My Location to add a friend. Pick a duration: an hour, until the end of the day, indefinitely, or a custom period.
One-time pin: open a conversation (or start a new message) in Messages. Tap the Plus button, then Location. Tap the Map Pin button in the corner, tap Send Pin, then send your message. The person sees only that snapshot and can't follow you as you move.
Stop sharing: Find My > People tab > choose the person > More > Stop Sharing My Location.
Requirements: Live Location needs both people on iPhone with iOS 15 or later; some options require iOS 17.
If you don't see a sharing option, update your iPhone to the latest software.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone (Find My)",
             "messages": [
                 "I have an iPhone. My son keeps asking where I am, but I don't want him watching me all day. I just want to send him where I am right now at the park, one time. Can I do that?",
                 """Yes. You can send a one-time pin in Messages.

1. Open the **Messages** app and open the conversation with your son, or start a new message to him.
2. Tap the **Plus** button, then tap **Location**.
3. Tap the **Map Pin** button in the corner.
4. Tap **Send Pin**.
5. Send your message.

Your son sees only that spot. He can't follow you as you move.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone (Find My)",
             "messages": [
                 "My daughter has an iPhone too. How can I let her see where I am on my iPhone while I drive to her house?",
                 """You can do this in the **Find My** app.

1. Open **Find My**.
2. Tap the **Me** tab and turn on **Share My Location**.
3. Tap the **People** tab, tap the **Add** button (a plus icon), then tap **Share My Location**.
4. Choose your daughter.
5. Pick how long to share: an hour, until the end of the day, indefinitely, or a custom period.

Only share your location with people you trust.""",
                 "When I tap the plus button I don't see Share My Location at all.",
                 """When a sharing option is missing, update your iPhone.

1. Update your iPhone to the latest software.
2. Open **Find My** and try the steps again.

Live Location needs both you and your daughter to have an iPhone with iOS 15 or later. Some options need iOS 17.""",
             ]},
        ],
    },
    {
        "task_id": "TR-055", "task_type": "share_location", "task": "Share location with family",
        "platform": "Android (Google Maps)", "category": "communication", "sensitive": True,
        "source": {"title": "Google Maps Help: Share your real-time location with others (Android)", "url": "https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Requirements: signed in to Google Account in Google Maps; add the recipient's Gmail address to your Google Contacts; the recipient must have a Gmail account; allow Maps access to contacts if it asks.
Share: Google Maps > tap profile picture or initial > Location sharing > New share > choose how long to share > tap the profile of the person > Share.
Link for someone without a Google Account: Maps > profile picture or initial > Location sharing > New share > Copy to clipboard > paste the link into an email, text, or messaging app. The link shares real-time location for up to 24 hours.
Stop: Location sharing > tap the person's profile > Stop.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Google Maps)",
             "messages": [
                 "I'm on Android and use Google Maps. My brother in law doesn't have Gmail, he only has some other email. We're driving to the lake and he wants to see where I am along the way. Can he still do that?",
                 """Yes. You can share a link with him instead.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Tap **Copy to clipboard**.
6. Paste the link into an email, text, or messaging app and send it to him.

The link shares your real-time location for up to 24 hours.

Only share your location with people you trust.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Google Maps)",
             "messages": [
                 "Android phone. My son uses Gmail. How do I let him see my location in Google Maps?",
                 """You can do it in **Google Maps**.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial**.
3. Tap **Location sharing**, then tap **New share**.
4. Choose how long to share.
5. Tap your son's profile.
6. Tap **Share**.

His Gmail address needs to be saved in your Google Contacts.""",
                 "I tapped New share but my son isn't in the list.",
                 """The usual reason is that his contact isn't ready for sharing.

1. Add your son's Gmail address to your Google Contacts. He must have a Gmail account.
2. If Google Maps asks for access to your contacts, allow it.
3. Tap your picture or initial, then **Location sharing**, then **New share** again.

If he doesn't have Gmail, tap **Copy to clipboard** on that screen and send him the link instead.""",
             ]},
        ],
    },
    {
        "task_id": "TR-056", "task_type": "install_app", "task": "Install an app",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: Download apps on your iPhone or iPad", "url": "https://support.apple.com/en-us/102590"},
        "source_notes": """Open the App Store. Find an app: browse the Today, Games, Apps, or Arcade tabs, or tap the Search tab to look for a specific app. Tap the price or the Get button. If you see Open instead, you've already bought or downloaded the app. Confirm: double-click the side button; Face ID: glance at iPhone; Touch ID: rest finger on the button with Touch ID; or you may need your Apple Account password.
An app showing Get instead of a price is free and you won't be charged to download it. Some free apps offer in-app purchases and subscriptions, which are optional.
If the App Store is missing: Content & Privacy Restrictions may be on. Adjust your iTunes & App Store Purchases settings and choose Allow for Installing Apps; the App Store should reappear. If it still doesn't appear, swipe down (from the middle of the Home Screen, Spotlight Search) and search for App Store.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I want the Spotify app on my iPhone but I don't want to be charged anything just for getting it. How do I make sure it's free and get it?",
                 """Free apps show **Get** instead of a price, and you won't be charged to download them.

1. Open the **App Store** app.
2. Tap the **Search** tab and look for **Spotify**.
3. Check the button next to the app. If it says **Get**, it is free to download. If it shows a price, it is not free.
4. Tap **Get**.
5. Confirm by double-clicking the **side button**. Look at the screen if you use Face ID, or rest your finger on the Touch ID button. You may need your Apple Account password.

Some free apps offer in-app purchases and subscriptions, but those are optional.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Please tell me how to get the Zoom app on my iPhone.",
                 """You can get it from the **App Store**.

1. Open the **App Store** app.
2. Tap the **Search** tab and look for **Zoom**.
3. Tap **Get**.
4. Confirm by double-clicking the **side button**. Use Face ID or Touch ID, or enter your Apple Account password if asked.""",
                 "I can't find the App Store on my phone. The icon is gone.",
                 """Let's look for it.

1. Swipe down from the middle of your Home Screen and search for **App Store**.
2. If it still doesn't appear, **Content & Privacy Restrictions** may be turned on.
3. Adjust your **iTunes & App Store Purchases** settings so **Installing Apps** is set to **Allow**.
4. If you did not set this up, ask the person who manages your phone.

The App Store should reappear on your device.""",
             ]},
        ],
    },
    {
        "task_id": "TR-057", "task_type": "install_app", "task": "Install an app",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Help: Download apps to your Android device", "url": "https://support.google.com/android/answer/9457058?hl=en"},
        "source_notes": """Open Google Play: on a phone, the Play Store app. The page does not describe search or browsing controls. Check reliability: under the app's title look at the star ratings and the download count; to read reviews scroll to the Ratings and reviews section. Tap Install for free apps, or tap the app's price for paid apps. No payment steps are given.
Warning: apps from unknown sources put your device and personal information at risk. Google Play Protect checks for potentially harmful apps, warns you, and removes them if necessary.
Some steps work only on Android 8.0 and up.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I have an Android phone and I need my bank's app. I only want to get it from a safe place and I want to be sure it's a good one before I put it on my phone. What should I do?",
                 """The safest place is the **Play Store**. Google Play Protect checks for harmful apps, warns you, and removes them if necessary. Apps from unknown sources can put your device and personal information at risk.

1. Open the **Play Store** app.
2. Find the app you want.
3. Under the app's title, look at the star ratings and the number of downloads.
4. To read what other people say, scroll down to **Ratings and reviews**.
5. If it looks right, tap **Install**.

When the install is done, the app is on your phone.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I put a weather app on my Android phone?",
                 """You can get it from the **Play Store**.

1. Open the **Play Store** app.
2. Find the weather app you want.
3. Under the title, look at the star ratings and the number of downloads.
4. Tap **Install**.""",
                 "There's no Install button. There's a price with a dollar sign where it should be.",
                 """A price means it is a paid app. Free apps show **Install**.

1. If you only want a free app, don't tap the price. Go back and look for a different weather app that shows **Install**.
2. Tapping the price is how you buy the app, so only tap it if you mean to pay for it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-058", "task_type": "delete_app", "task": "Delete an app",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: Delete apps on your iPhone or iPad", "url": "https://support.apple.com/en-us/101550"},
        "source_notes": """Before you delete: cancel any in-app subscriptions you no longer need; deleting an app doesn't cancel them.
Method 1: touch and hold the app, tap Remove App, tap Delete App, tap Delete to confirm.
Method 2 (jiggle mode): touch and hold any app until the apps jiggle; tap the Remove icon in the upper-left corner of the app; tap Delete App, then Delete to confirm; tap the Done button at the top of the screen.
If you don't see the delete option: some built-in Apple apps can't be deleted. For a non-Apple app, check your parental control settings and make sure deleting apps is set to Allow, then try again. If the device is managed by an MDM solution you may not be able to delete apps; contact your device administrator.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "All the icons on my iPhone are shaking and have little minus signs on them. I must have held one too long. I don't want to mess up the others, I only want to delete the Candy Crush game. What do I do now?",
                 """Your phone is in the mode where you can delete apps, so you can finish from there. Only the app you pick will be deleted.

1. Tap the **minus** icon in the upper-left corner of the Candy Crush app.
2. Tap **Delete App**.
3. Tap **Delete** to confirm.
4. Tap **Done** at the top of the screen to stop the icons shaking.

Deleting an app does not cancel subscriptions inside it. If you pay for something in the game, cancel that first.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How can I take the Facebook app off my iPhone? I don't use it anymore.",
                 """You can delete it from the Home Screen.

1. Touch and hold the app.
2. Tap **Remove App**.
3. Tap **Delete App**.
4. Tap **Delete** to confirm.

Deleting an app doesn't cancel subscriptions inside it, so cancel any you don't need first.""",
                 "I held it but there is no Remove App choice, or it won't let me delete it.",
                 """A few things can cause that.

1. Some built-in Apple apps can't be deleted.
2. If it's not an Apple app, check your parental control settings and make sure deleting apps is set to **Allow**. Then try again.
3. If your iPhone is managed by a company or school, you may not be able to delete apps. Contact your device administrator.""",
             ]},
        ],
    },
    {
        "task_id": "TR-059", "task_type": "delete_app", "task": "Delete an app",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Google Play Help: Delete apps on your Android device", "url": "https://support.google.com/googleplay/answer/13627402?hl=en"},
        "source_notes": """Heading "Delete apps that you installed": open the Google Play Store app; at the top right tap the Profile icon; tap Manage apps & devices (plural), then Manage; select the name of the app you want to delete; tap Uninstall.
Some of these steps work only on Android 13 and up. If you delete or disable an app, you can add it back to your phone. If you bought an app, you can reinstall it without buying it again. You can archive apps you haven't used: the app data is removed but the app icon and personal data stay (no steps on the page).
Related page (Disable apps that came with your phone): you can't delete some system apps that came pre-installed. On some phones you can turn them off so they won't show on the list of apps. The page gives no steps and points to the device manufacturer.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I paid for a puzzle game on my Android phone, but I never play it and my phone is full. I might want it back someday though and I don't want to pay twice. Can I take it off?",
                 """Yes. If you bought an app, you can reinstall it later without buying it again.

1. Open the **Play Store** app.
2. At the top right, tap your **Profile icon**.
3. Tap **Manage apps & devices**, then tap **Manage**.
4. Tap the name of the puzzle game.
5. Tap **Uninstall**.

Some of these steps work only on Android 13 and up.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I get rid of an app I don't use on my Android phone?",
                 """You can remove it through the Play Store.

1. Open the **Play Store** app.
2. At the top right, tap your **Profile icon**.
3. Tap **Manage apps & devices**, then tap **Manage**.
4. Tap the name of the app you want to delete.
5. Tap **Uninstall**.""",
                 "I did that for a weather app that came with my phone, but there's no Uninstall button for it.",
                 """That app is probably a system app that came with the phone. You can't delete some of those.

On some phones you can turn them off instead, so they won't show on your list of apps. I don't have the exact steps for turning one off. Your phone maker's support can tell you if your phone allows it.

Apps you installed yourself can still be removed with **Uninstall**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-060", "task_type": "delete_app", "task": "Uninstall a program",
        "platform": "Windows 11", "category": "technical_support", "sensitive": False,
        "source": {"title": "Microsoft Support: Uninstall or remove apps and programs in Windows", "url": "https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98"},
        "source_notes": """Method 1 (Start menu): Start > All apps, find the app in the list. Press and hold (or right-click) the app, then select Uninstall.
Method 2 (Settings): Start > Settings > Apps > Installed apps. Find the app, select the More icon, then select Uninstall. Some apps can't be uninstalled from Settings; for those use Control Panel.
Method 3 (Control Panel): in the taskbar search box enter Control Panel and select it. Select Programs > Programs and Features. Press and hold (or right-click) the program, then select Uninstall or Uninstall/Change. Follow the on-screen directions.
Some apps and programs are built into Windows and can't be uninstalled. Error during uninstall: run the Program Install and Uninstall Troubleshooter.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Windows 11 here. The Settings pages confuse me with all the menus. Is there a faster way to remove my old photo program straight from the Start menu?",
                 """Yes. You can do it right from the Start menu.

1. Click the **Start** button.
2. Click **All apps**.
3. Find your photo program in the list.
4. Right-click it.
5. Click **Uninstall**.

Some programs are built into Windows and can't be uninstalled.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My Windows 11 PC has an old printer program I never use anymore and I want it gone.",
                 """You can use Settings.

1. Click **Start**, then **Settings**.
2. Click **Apps**, then **Installed apps**.
3. Find the program in the list.
4. Click the **More** icon next to it, then click **Uninstall**.""",
                 "I found my program there but Uninstall doesn't work from that screen.",
                 """Some programs can't be uninstalled from Settings. Use Control Panel instead.

1. In the search box on the taskbar, type **Control Panel** and click it.
2. Click **Programs**, then **Programs and Features**.
3. Right-click the program and click **Uninstall** or **Uninstall/Change**.
4. Follow the directions on the screen.""",
             ]},
        ],
    },
    {
        "task_id": "TR-061", "task_type": "free_storage", "task": "Free up storage space",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: How to check the storage on your iPhone and iPad", "url": "https://support.apple.com/en-us/108429"},
        "source_notes": """Settings > General > iPhone Storage shows recommendations and a list of apps with storage use. Tap an app's name for details. In the app's detail view: Offload App removes the app but keeps its documents and data; Delete App removes the app and its related data.
Recommendations: in the Storage section tap Show All, read each recommendation; tap Enable to turn it on, or tap the recommendation to review what you can delete. The only recommendation label named: Offload Unused Apps.
Storage bar: Photos = photos and videos in the Photos app; Other = non-removable system assets, logs, caches and similar data; System = space used by iOS.
Troubleshooting: cached files won't delete: the system removes cached and temporary files itself when it needs space. For a Storage Almost Full alert, check recommendations or remove content such as videos and apps.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone is almost out of room. I don't want to lose any of my photos or anything saved inside my apps. Is there a way to get space back without losing my stuff?",
                 """Yes. Offloading removes an app but keeps its documents and data.

1. Open the **Settings** app.
2. Tap **General**, then tap **iPhone Storage**.
3. Tap **Show All** to see recommendations for your iPhone.
4. If you see **Offload Unused Apps**, tap **Enable**.

You can also offload one app yourself. Tap the app in the list, then tap **Offload App**.

Don't tap **Delete App**. That removes the app and its data.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone keeps saying Storage Almost Full. How do I find out what's taking up the room?",
                 """You can see it in Settings.

1. Open the **Settings** app.
2. Tap **General**, then tap **iPhone Storage**.
3. Look at the recommendations at the top and the list of apps below.
4. Tap an app to see **Offload App** or **Delete App**.""",
                 "I see a big piece called Other, and another called System. How do I delete those?",
                 """You can't delete those directly.

1. **Other** is system files, logs, caches and similar data that can't be removed. **System** is the space iOS itself uses.
2. The phone clears cached and temporary files by itself when it needs space.
3. To free room yourself, tap **Show All** under the recommendations, or tap an app in the list and choose **Offload App** or **Delete App**.""",
             ]},
        ],
    },
]
