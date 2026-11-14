TASKS = [
    {
        "task_id": "TR-193",
        "task_type": "app_notifications_off",
        "task": "Stop a website from sending notifications",
        "platform": "Chrome (computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Google Chrome Help: Manage notifications in Chrome", "url": "https://support.google.com/chrome/answer/3220216"},
        "source_notes": """Block one site (computer): 1 Open Chrome. 2 Top right, select the More icon, then Settings. 3 Select Privacy and security, then Site Settings, then Notifications. 4 Next to "Not allowed to send notifications," select Add. 5 Enter the site's web address, then select Add.
Quieter messaging (closest to blocking all): same steps 1-3, under the default setting choose to let sites ask for notifications, then select Use quieter messaging. Sites can still ask, but no pop-up prompt appears; a bell icon shows next to the address bar and you can select it to allow.
Decline a single request: when the "Get notifications?" message appears, select the Settings icon, then Don't allow. Swiping the message away also blocks it.
Troubleshooting: if a site keeps sending after blocking, check it is listed under "Not allowed to send notifications". If you see pop-ups and not notifications, they use a separate setting: Privacy and security > Site Settings > Pop-ups and redirects, find the site under "Allowed to send pop-ups and use redirects," then select More > Block. If you see a "Notifications blocked" icon on a site, select it to re-enable there.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "How do I stop a news website from sending me notifications in Chrome on my computer?",
                 """Here is how to block one website in Chrome:

1. Open **Chrome** on your computer.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
4. Next to **Not allowed to send notifications**, select **Add**.
5. Type the website's web address, then select **Add**.

The site will now be on the blocked list.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I'm on my desktop computer using Chrome and every time I open a certain recipe website a box shows up in the corner asking Get notifications? and I keep closing it. It is happening right now. How do I tell it no so it stops asking?",
                 """Since the box is showing right now, you can answer it directly:

1. In the **Get notifications?** box, select the **Settings** icon.
2. Select **Don't allow**.

You can also just swipe the box away, and that blocks it too.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "A website keeps sending me notifications and I want it to stop. Can you help?",
                 "I can help with that. Are you using **Chrome** on a computer, or on a phone or tablet?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "A website keeps sending me notifications and I want it to stop. Can you help?",
                 "I can help with that. Are you using **Chrome** on a computer, or on a phone or tablet?",
                 "Chrome on my Windows laptop",
                 """Here is how to block the website in Chrome on your computer:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
4. Next to **Not allowed to send notifications**, select **Add**.
5. Type the website's web address, then select **Add**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I use Chrome on my computer. I don't want to block websites one by one, and I might want to say yes to my bank's alerts someday. I just want the pop-up that asks me about notifications to stop showing up. Is there a setting for that?",
                 """Yes. Chrome has a quieter setting that keeps those asking boxes away:

1. Open **Chrome**, then select the **More** icon at the top right and select **Settings**.
2. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
3. Under the default setting, choose the option that lets sites ask for notifications.
4. Select **Use quieter messaging**.

Sites can still ask, but no pop-up box appears. You will see a bell icon next to the address bar, and you can select it if you ever want to allow that site.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I use Chrome on my PC. How do I block a website from sending notifications?",
                 """Here is how to block one website:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
4. Next to **Not allowed to send notifications**, select **Add**.
5. Type the website's web address, then select **Add**.""",
                 "I did all that but the website is still putting little boxes on my screen.",
                 """Those may be pop-ups, which use a different setting from notifications. Try this:

1. Go to **Privacy and security**, then **Site Settings**, then **Pop-ups and redirects**.
2. Find the site under **Allowed to send pop-ups and use redirects**.
3. Select **More**, then select **Block**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-194",
        "task_type": "live_captions",
        "task": "Turn on Live Caption",
        "platform": "Chrome (computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Google Chrome Help: Use Live Caption in Chrome", "url": "https://support.google.com/chrome/answer/10538231"},
        "source_notes": """Windows or Mac: 1 Open Chrome. 2 Top right, select the More icon, then Settings, then Accessibility. 3 Turn Live Caption on.
Linux: 1 Open Chrome. 2 Top right, More icon, Settings, then Accessibility. 3 Select Captions. 4 Turn Live Caption on.
Other language than English (Windows, Mac, Linux): next to "Manage languages" select Add languages (Chrome downloads language packs automatically). Next to "Preferred caption language" open the down arrow and choose your language.
What you see: captions appear in a bubble; drag the bubble to move it. Use the arrow in the bubble to collapse or expand captions. To return to the tab playing audio, select Back to tab. Font, size, color: Settings > Accessibility > "Caption preferences" (Windows or Mac), or Captions > "Caption preferences" (Linux).
Troubleshooting: captions are generated from audio, so for videos that autoplay, turn the video volume on. To turn on captions for all videos, select the Media control icon at the top right.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "How do I turn on Live Caption in Chrome on my Windows computer? I want to read what people say in videos.",
                 """Here is how to turn on Live Caption:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Accessibility**.
4. Turn **Live Caption** on.

Captions will show up in a bubble when a video plays sound.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "My husband and I watch lots of Spanish language shows in Chrome on our Mac and neither of us hears so well anymore. Someone said Chrome can write out the words for us. Can you show me how to turn that on and have it show Spanish?",
                 """Yes, Chrome can do that. Here is how:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Turn **Live Caption** on.
4. Next to **Manage languages**, select **Add languages** and choose Spanish. Chrome downloads the language pack by itself.
5. Next to **Preferred caption language**, open the down arrow and choose Spanish.

The words will appear in a bubble while the show plays.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "Can you tell me how to get captions to show up on the videos I watch?",
                 "I can help with that. Are you watching in **Chrome** on a computer, or on a phone or tablet?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "Can you tell me how to get captions to show up on the videos I watch?",
                 "I can help with that. Are you watching in **Chrome** on a computer, or on a phone or tablet?",
                 "Chrome on my Mac",
                 """Here is how to turn on Live Caption in Chrome:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Turn **Live Caption** on.

Captions will appear in a bubble when a video plays sound.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I use Chrome on a Linux computer. I want captions on my videos, but I don't want a big box covering the picture. Can I turn them on and keep them out of the way?",
                 """Yes. First turn the captions on:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Select **Captions**.
4. Turn **Live Caption** on.

The words appear in a bubble. To keep it out of the way, drag the bubble to a new spot. You can also select the arrow in the bubble to collapse it, and select it again to expand it.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "How do I turn on Live Caption in Chrome on my Windows PC?",
                 """Here is how to turn on Live Caption:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Accessibility**.
4. Turn **Live Caption** on.""",
                 "I turned it on but my video plays with no captions. It starts playing by itself with the sound off.",
                 """Captions are made from the sound, so a silent video gives them nothing to write. Turn the video's volume on, and the words should start to appear in the bubble.""",
             ]},
        ],
    },
    {
        "task_id": "TR-195",
        "task_type": "sign_out",
        "task": "Sign out of a Google Account on a shared computer or another device (from the account's devices page)",
        "platform": "Google Account",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Google Account Help: See devices with account access", "url": "https://support.google.com/accounts/answer/3067630"},
        "source_notes": """Section "Sign out on a device you no longer use": 1 Go to your Google Account at https://myaccount.google.com. 2 Tap Security & sign-in. 3 Under the Your devices panel, tap Manage all devices. 4 Tap the device you want to remove, then tap Sign out. (Page words are 'tap'; I write 'select'.)
Use for devices that are lost, no longer owned, or don't belong to you, such as a shared or public computer.
List shows devices where you are signed in or were within the last few weeks; already signed out ones show "Signed out". Several sessions with the same device name may be one device or several; to make sure no other device has access, sign out of all the sessions with that device name. Some entries are sessions (created when signing in on new device/browser/app, incognito etc).
Signing out ends that device's or session's access to your account. Page describes no confirmation prompt after Sign out. Page has no separate steps for signing out while on the same computer.
Times shown are last communication with Google (may include background syncing), may be more recent than last use.
Troubleshooting: if you don't recognize a device or see unfamiliar activity, follow page's steps to secure your account (not detailed here). A recently factory reset device may still appear. Can also check google.com/devices.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I checked my Gmail on my neighbor's computer and forgot to sign out before I left. How do I sign out of my Google Account on that computer?",
                 """You can sign that computer out from here:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the device you want to remove, then select **Sign out**.

That ends that device's access to your account.

If you see the same device name more than once, sign out of all the entries with that name, to be sure no other device still has access.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I was at the library this afternoon using one of their public computers to look at my Google account and I was in such a hurry to catch my bus that I left without logging out. I'm home now on my own computer. How can I make sure the library computer is signed out of my Google Account?",
                 """You can do it from your own computer:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the library computer in the list, then select **Sign out**.

A device you are already signed out of shows **Signed out** in the list.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I left my account open on a computer I don't own. How do I log out from here?",
                 "I can help with that. Is it your **Google Account** (like Gmail or YouTube), or a different kind of account?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I left my account open on a computer I don't own. How do I log out from here?",
                 "I can help with that. Is it your **Google Account** (like Gmail or YouTube), or a different kind of account?",
                 "Yes it's my Google account, Gmail",
                 """Here is how to sign that computer out from where you are:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the computer you left it on, then select **Sign out**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "My Google Account is still signed in on a hotel business center computer. I'm back in my room and can't go back down there. I only want that one computer signed out, and I want to keep using my phone and laptop as they are. What do I do?",
                 """You can sign out only that computer:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the hotel computer in the list, then select **Sign out**.

This ends that one device's access to your account. Only choose the hotel computer in the list.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "How do I sign my Google Account out of a shared computer I used earlier?",
                 """You can do it from your account page:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the shared computer, then select **Sign out**.""",
                 "I see the same computer name listed three times. Which one do I pick?",
                 """The same name can come from one device or from several. To be safe, sign out of all of them:

1. Select the first entry with that name, then select **Sign out**.
2. Do the same for each of the other entries with that name.""",
             ]},
        ],
    },
    {
        "task_id": "TR-196",
        "task_type": "recovery_info",
        "task": "Add a recovery phone number or email to a Google Account (computer)",
        "platform": "Google Account",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Google Account Help: Add or update your recovery phone or email", "url": "https://support.google.com/accounts/answer/183723"},
        "source_notes": """Recovery phone: 1 Go to your Google Account at myaccount.google.com. 2 Click Security & sign-in. 3 Under "How you sign in to Google," click Recovery phone (you might need to sign in). 4 To add a number, follow the on-screen steps. To change a number click Edit next to it; to remove click Delete next to it, then follow the on-screen steps.
Recovery email: same steps 1-2, then under "How you sign in to Google" click Recovery email (you might need to sign in). To add an address, follow the on-screen steps. Edit / Delete next to it to change or remove.
Conditions: not all recovery options are available for every region, account, or device. Work, school or group accounts may not support these steps; ask your administrator. You can't add recovery info while locked out or in the account recovery process. Use a phone that receives texts, belongs only to you, and that you use and carry regularly. Don't use a Google Voice number (may not receive the verification code). Choose a recovery email you use regularly, but not the one you sign in with.
Page does not describe specific verification prompts; only says follow on-screen steps. Phone changes can take up to 7 days to take effect. After changing, Google may send codes to the previous details for 7 days.
Troubleshooting: if you can't change recovery info, try again from a device you normally use to sign in, from a location where you normally sign in, or the following week from your current device.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "How do I add a recovery phone number to my Google Account? I'm on my computer.",
                 """Here is how to add a recovery phone number:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Follow the on-screen steps to add your number.

Use a phone that gets text messages, belongs only to you, and that you carry regularly. Do not use a Google Voice number.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "My grandson told me I should put a backup email address on my Gmail account in case I ever get locked out. I have an old email I check every day. I'm on my laptop right now. What do I click to add that as the recovery email?",
                 """Your grandson gave good advice. Here is how:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery email**. You might need to sign in again.
4. Follow the on-screen steps to add the address.

An email you check often is a good choice. It should be a different one from the email you sign in with.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I want to add a backup way to get back into my Google account in case I get locked out.",
                 "I can help with that. Would you like to add a recovery **phone number** or a recovery **email**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I want to add a backup way to get back into my Google account in case I get locked out.",
                 "I can help with that. Would you like to add a recovery **phone number** or a recovery **email**?",
                 "phone number please",
                 """Here is how to add a recovery phone number:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Follow the on-screen steps to add your number.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I forgot my Google password and I'm in the middle of the account recovery steps right now. I'd like to add a recovery phone number at the same time so this never happens again. Can I do that now?",
                 """Not right now. Google does not let you add recovery info while you are locked out or in the account recovery process.

Once you are back in your account, you can add it:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**.
4. Follow the on-screen steps to add your number.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I'm on my PC and want to change the recovery phone number on my Google Account to my new number.",
                 """Here is how to change it:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Select **Edit** next to the number.
5. Follow the on-screen steps.""",
                 "It won't let me change it. I get stuck and it just doesn't go through.",
                 """Try one of these:

1. Try again from a device you normally use to sign in.
2. Or try from a place where you normally sign in.
3. Or wait and try again next week from the device you are using now.""",
             ]},
        ],
    },
    {
        "task_id": "TR-197",
        "task_type": "free_storage",
        "task": "Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup)",
        "platform": "Google Account (Drive, Gmail, Photos)",
        "category": "online_services",
        "sensitive": False,
        "source": {"title": "Google One Help: Clean up & fix issues with your Google storage", "url": "https://support.google.com/googleone/answer/9776477"},
        "source_notes": """A. Storage Manager (computer): 1 Go to one.google.com and click Storage. 2 Select Clean up space. 3 Under "Clean up suggested items" or "Clean up by service," choose a category or service. 4 Select the files to delete (sort, filter, layout controls at top if they appear). 5 For Google Photos, click Download first if you want local copies. 6 Click Delete at the top right. For Photos, click Move to trash. 7 Read the consent wording and check the box to continue. 8 Click Permanently delete. For Photos, click Move to trash.
Storage totals can take 48-72 hours to update after a large deletion. If still at quota after 48-72 hours, auto-backup may be refilling the space; check Google Photos backup settings.
B. Google One app (Android): 1 Open the Google One app and tap Storage, then Free up account storage. 2 Under "Clean up other items," tap WhatsApp. 3 Under the backup you want to remove, tap Delete backup. Deleting a backup does not turn off future backups.
Storage Manager shows usage across Photos, Drive, Gmail, other services at one.google.com/storage/management. Page gives no separate Drive or Gmail cleanup steps. Page does not state a trash retention period. When storage is full: Gmail cannot send or receive, Drive cannot sync or upload, Photos cannot back up. Some files don't count against storage. Family members share storage by default. Workspace admins control quotas for Workspace accounts.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Google Account (Drive, Gmail, Photos)",
             "messages": [
                 "My Google storage is full and my Gmail stopped getting new mail. How do I free up space? I'm on my computer.",
                 """You can clear space with the Storage Manager:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up suggested items** or **Clean up by service**, choose a category or service.
4. Select the files you want to delete.
5. Click **Delete** at the top right.
6. Read the wording, then check the box to continue.
7. Click **Permanently delete**.

The storage total can take 48 to 72 hours to update after a big deletion.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Google Account (Drive, Gmail, Photos)",
             "messages": [
                 "I have an Android phone and the Google One app. It says my storage is almost full and I think it's because of my WhatsApp backup, my daughter said something about that. Where do I go in the app to get rid of the old WhatsApp backup?",
                 """Here is how to remove it in the Google One app:

1. Open the **Google One** app and tap **Storage**, then tap **Free up account storage**.
2. Under **Clean up other items**, tap **WhatsApp**.
3. Under the backup you want to remove, tap **Delete backup**.

Deleting a backup does not turn off future backups.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "Google says my storage is full. What should I do?",
                 "I can help with that. Are you using a **computer**, or the Google One app on an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Google Account (Drive, Gmail, Photos)",
             "messages": [
                 "Google says my storage is full. What should I do?",
                 "I can help with that. Are you using a **computer**, or the Google One app on an **Android** phone?",
                 "I'm on a computer",
                 """Here is how to clear space on a computer:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up suggested items** or **Clean up by service**, choose a category or service.
4. Select the files you want to delete.
5. Click **Delete** at the top right.
6. Read the wording, then check the box to continue.
7. Click **Permanently delete**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Account (Drive, Gmail, Photos)",
             "messages": [
                 "Most of my storage is old photos in Google Photos. I'm on my computer and I don't want to lose any of them, I'd like copies on my own computer first. How do I free up space?",
                 """You can save copies first, then clear the space:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up by service**, choose **Google Photos**.
4. Select the photos you want to remove.
5. Click **Download** to keep copies on your computer.
6. Click **Delete** at the top right, then click **Move to trash**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Account (Drive, Gmail, Photos)",
             "messages": [
                 "My Google account storage is full. I'm on my computer. How do I free some up?",
                 """Use the Storage Manager:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up suggested items** or **Clean up by service**, choose a category or service.
4. Select the files you want to delete.
5. Click **Delete** at the top right.
6. Read the wording, then check the box to continue.
7. Click **Permanently delete**.""",
                 "I deleted a lot of stuff but it still says my storage is full.",
                 """The total can take 48 to 72 hours to update after a large deletion, so please wait that long first. If it is still full after that, your photo backup may be filling the space again. Check your **Google Photos** backup settings.""",
             ]},
        ],
    },
    {
        "task_id": "TR-198",
        "task_type": "maps_directions",
        "task": "Get directions on a computer",
        "platform": "Google Maps (computer)",
        "category": "online_services",
        "sensitive": False,
        "source": {"title": "Google Maps Help: Get directions and show routes", "url": "https://support.google.com/maps/answer/144339"},
        "source_notes": """Computer: 1 Open Google Maps in your browser. Click Directions. 2 Enter a starting point and destination by clicking the map, typing an address, or adding a place name. 3 Choose a mode: Driving, Transit, or Walking.
Driving: routes built for cars. Transit: only where the local transit agency has added route info to Google Maps; transit doesn't support multiple stops. Walking: step-by-step walking directions.
What you see: best route in blue, other routes gray, each route shows estimated travel time (select another route on the map to choose it). Under the route click Details to see steps; Expand for more detail.
Avoid tolls or highways: after entering your route, click Options, then check Tolls or Highways under "Avoid tolls & highways."
Departure or arrival time: after getting directions, click Leave now, then select Depart at or Arrive by. Only works with one destination.
Add stops: click Add destination below your destinations (up to 9 stops including final destination).
Troubleshooting: no transit option means the city's transit agency may not have added route info yet.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Google Maps (computer)",
             "messages": [
                 "How do I get driving directions on Google Maps on my computer?",
                 """Here is how to get driving directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter a starting point and a destination. You can type an address, type a place name, or click on the map.
3. Choose **Driving**.

The best route shows in blue, and other routes show in gray. Under the route, click **Details** to see the steps.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Google Maps (computer)",
             "messages": [
                 "I'm going to walk to my sister's house on Saturday and I want to print out the route first. I'm at my desktop computer in the browser, on Google Maps. How do I get the walking directions from my house to hers?",
                 """Here is how to get walking directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your house as the starting point and your sister's address as the destination.
3. Choose **Walking**.

Under the route, click **Details** to see the step by step directions.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i get directions to the dentist office on google maps",
                 "I can help with that. Are you using Google Maps on a **computer**, or on a **phone or tablet**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Google Maps (computer)",
             "messages": [
                 "how do i get directions to the dentist office on google maps",
                 "I can help with that. Are you using Google Maps on a **computer**, or on a **phone or tablet**?",
                 "my computer",
                 """Here is how to get directions on a computer:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your starting point, then type the dentist's office name or address as the destination.
3. Choose **Driving**, **Transit**, or **Walking**.

Under the route, click **Details** to see the steps.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Maps (computer)",
             "messages": [
                 "I'm planning a drive from my computer using Google Maps in my browser. I really don't want to pay any tolls on the way. How do I get driving directions that avoid them?",
                 """Here is how to get driving directions without tolls:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter a starting point and a destination.
3. Choose **Driving**.
4. Click **Options**.
5. Under **Avoid tolls & highways**, check **Tolls**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Maps (computer)",
             "messages": [
                 "I'd like bus directions to the farmers market on Google Maps on my computer.",
                 """Here is how to get bus directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your starting point and the farmers market as the destination.
3. Choose **Transit**.""",
                 "I don't see any bus or transit option for my town.",
                 """Transit only shows where your city's transit agency has added its route information to Google Maps. Your agency may not have added it yet. You can still choose **Driving** or **Walking** from the same screen to get directions.""",
             ]},
        ],
    },
]
