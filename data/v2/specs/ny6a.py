TASKS = [
    {
        "task_id": "TR-186",
        "task_type": "bookmark_site",
        "task": "Save a website as a favorite",
        "platform": "Microsoft Edge (computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Add a site to my favorites in Microsoft Edge", "url": "https://support.microsoft.com/en-us/microsoft-edge/add-a-site-to-my-favorites-in-microsoft-edge-ed39f9ef-0b77-86c5-5cc5-ccf8d33350c7"},
        "source_notes": """Method 1 (address bar): 1 Open Microsoft Edge and go to the site. 2 Select the "Add this page to favorites" button in the address bar. 3 If you want, rename the favorite or choose a different folder. Then select Done.
Method 2 (menu): 1 Open Edge and go to the site. 2 Select Settings and more, then Favorites. 3 Select More options, then choose either "Add this page to favorites" (saves the current page) or "Add open pages to favorites" (saves all open pages).
Not covered: keyboard shortcuts, favorites bar, how to find favorites later, troubleshooting.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "How do I save a website as a favorite in Edge on my computer?",
                 """Here is how to save the page you are on as a favorite in Microsoft Edge:

1. Open Microsoft Edge and go to the website.
2. Select the **Add this page to favorites** button in the address bar.
3. If you like, type a new name or choose a different folder.
4. Select **Done**.

If you do not see that button in the address bar, select **Settings and more**, then **Favorites**, then **More options**, then **Add this page to favorites**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "My grandson put Microsoft Edge on my Windows laptop and every morning I type in the address of my crossword site by hand. It is open on the screen right now. I only ever use the three dots menu at the top because I don't trust the little buttons. Is there a way to save this site as a favorite from that menu?",
                 """Yes. You can do it from the menu, since the crossword page is already open:

1. Select **Settings and more**.
2. Select **Favorites**.
3. Select **More options**.
4. Select **Add this page to favorites**.

That saves only the page you are on.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I want to save a website so I can get back to it fast without typing it in again.",
                 "I can help with that. Which browser are you using: **Microsoft Edge**, **Chrome**, or something else?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "I want to save a website so I can get back to it fast without typing it in again.",
                 "I can help with that. Which browser are you using: **Microsoft Edge**, **Chrome**, or something else?",
                 "Edge, on my laptop",
                 """Thanks. In Microsoft Edge, saving a site as a favorite takes a few clicks:

1. Go to the website you want to keep.
2. Select the **Add this page to favorites** button in the address bar.
3. If you want, change the name or pick a different folder.
4. Select **Done**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "I have about eight tabs open in Edge on my computer for my daughter's wedding planning, but I only want to save the one I'm looking at right now, the florist's page. I don't want all eight saved as favorites. How do I do just the one?",
                 """You can save just the florist's page. Make sure that page is the one showing, then:

1. Select **Settings and more**.
2. Select **Favorites**.
3. Select **More options**.
4. Select **Add this page to favorites**.

Do not choose **Add open pages to favorites**. That one saves all your open pages.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "Please show me how to add a favorite in Microsoft Edge on my computer.",
                 """Sure. Here is how:

1. Open Microsoft Edge and go to the site.
2. Select the **Add this page to favorites** button in the address bar.
3. If you want, rename it or choose a different folder.
4. Select **Done**.""",
                 "I looked in the address bar and I don't see any button like that.",
                 """No problem. You can use the menu instead:

1. Select **Settings and more**.
2. Select **Favorites**.
3. Select **More options**.
4. Select **Add this page to favorites**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-187",
        "task_type": "bookmark_site",
        "task": "Bookmark a website in Chrome on the phone",
        "platform": "Chrome (Android)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chrome Help: Create, find and edit bookmarks in Chrome (Android phone section)", "url": "https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Add a bookmark (phone): 1 Open Chrome and go to the page. 2 To the right of the address bar, tap More (three-dot icon), then tap "Add to bookmarks" (icon labeled "Bookmark this page").
Find a bookmark later: 1 Open Chrome. 2 At the top right tap More, then Bookmarks (star icon). Condition: if the address bar is at the bottom, swipe up on the address bar and tap Bookmarks. 3 Tap a folder (recently opened folders first; Back arrow at top left for other folders). 4 Tap the bookmark. Tip: "Search your bookmarks" bar at the top.
Other: Edit via More > Edit next to a bookmark; Delete via More > Delete (permanent, cannot be undone); Move via More > "Move to...", pick folder, "Move here".
Not mentioned: a "Mobile bookmarks" folder.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (Android)",
             "messages": [
                 "How do I bookmark a website in Chrome on my Android phone?",
                 """Here is how to bookmark a page in Chrome on your Android phone:

1. Open Chrome and go to the page you want to save.
2. Next to the address bar, tap **More** (the three dots).
3. Tap **Add to bookmarks**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (Android)",
             "messages": [
                 "I have a Google Pixel phone and I use Chrome for the weather site every single day. My neighbor said I can save it so I don't have to search for it every time. I have the weather site open right now. How do I save it, and then how would I open it again tomorrow?",
                 """You can bookmark it now and open it from your bookmarks tomorrow.

To save it:
1. With the weather site open, tap **More** (the three dots) next to the address bar.
2. Tap **Add to bookmarks**.

To open it again:
1. Open Chrome.
2. Tap **More** at the top right.
3. Tap **Bookmarks**.
4. Tap the bookmark.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i want to save a website on my phone so i dont lose it. i use chrome",
                 "I can help with that. Is your phone an **Android** phone or an **iPhone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (Android)",
             "messages": [
                 "i want to save a website on my phone so i dont lose it. i use chrome",
                 "I can help with that. Is your phone an **Android** phone or an **iPhone**?",
                 "android, a samsung",
                 """Thanks. To bookmark a site in Chrome on your Android phone:

1. Open Chrome and go to the website.
2. Tap **More** (the three dots) next to the address bar.
3. Tap **Add to bookmarks**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (Android)",
             "messages": [
                 "On my Android phone the Chrome address bar is at the bottom of the screen, not the top. My son changed something. I want to bookmark a recipe page I'm on and then find it again later. Where do I tap?",
                 """You can do both with the bar at the bottom.

To save the recipe:
1. Tap **More** (the three dots) next to the address bar.
2. Tap **Add to bookmarks**.

To find it later:
1. Open Chrome.
2. Swipe up on the address bar.
3. Tap **Bookmarks**.
4. Tap a folder, then tap the bookmark.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (Android)",
             "messages": [
                 "Can you tell me how to bookmark a page in Chrome on my Android phone?",
                 """Yes. Here is how:

1. Open Chrome and go to the page.
2. Tap **More** (the three dots) next to the address bar.
3. Tap **Add to bookmarks**.""",
                 "ok I did that. but now how do I get back to it? I can't find where it went",
                 """Your bookmark is saved. To open it:

1. Open Chrome.
2. At the top right, tap **More**, then tap **Bookmarks**.
3. Tap a folder. Recently opened folders show first.
4. Tap the bookmark.

If your address bar is at the bottom, swipe up on it and tap **Bookmarks** instead. You can also type in the **Search your bookmarks** bar at the top.""",
             ]},
        ],
    },
    {
        "task_id": "TR-188",
        "task_type": "browser_zoom",
        "task": "Make web pages bigger",
        "platform": "Microsoft Edge (computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Accessibility features in Microsoft Edge", "url": "https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a"},
        "source_notes": """Zoom a single page: Select Settings and more (three-dot menu), then choose Zoom in (+) or Zoom out (-). The menu also has Full screen.
Keyboard: Ctrl and Plus (+) zooms in by 25%; Ctrl and Minus (-) zooms out by 25%; Ctrl and 0 resets to default zoom level; Ctrl and scroll wheel up/down zooms in/out; F11 toggles full screen.
Default zoom for all websites: Select Settings and more (or press Alt and F), select Settings, then Accessibility. Under Visibility, choose a level from the Page zoom drop-down. Zoom levels for specific sites: select Zoom levels on that page.
No menu path given for reset; Ctrl and 0 resets. No Mac steps on the page.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "The writing on websites is too small in Edge on my computer. How do I make it bigger?",
                 """You can zoom in on the page you are looking at:

1. Select **Settings and more** (the three dots menu).
2. Select **Zoom in** (the plus sign).
3. Select **Zoom in** again until the page is the size you like.

You can also hold the **Ctrl** key and press the **plus sign** key.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "My eyes aren't what they used to be and I read the news on my Windows computer using Microsoft Edge. The words are tiny. My husband mentioned there is a way to do it from the keyboard without going into any menus, and I would rather learn that. I have a mouse with a wheel on it too if that helps.",
                 """Yes, there are two quick ways. With the news page open:

1. Hold down the **Ctrl** key.
2. Press the **plus sign** key. Each press makes the page bigger.

Or, with the mouse:
1. Hold down the **Ctrl** key.
2. Roll the mouse wheel up to make the page bigger. Roll it down to make it smaller.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "Everything on the websites I visit looks so tiny. Can you make the pages bigger?",
                 "I can help with that. Which web browser are you using: **Edge**, **Chrome**, or something else?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "Everything on the websites I visit looks so tiny. Can you make the pages bigger?",
                 "I can help with that. Which web browser are you using: **Edge**, **Chrome**, or something else?",
                 "Edge on my computer",
                 """Thanks. To make the page you are on bigger in Edge:

1. Select **Settings and more** (the three dots menu).
2. Select **Zoom in** (the plus sign).
3. Select **Zoom in** again until the page is big enough.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "I use Microsoft Edge on my computer and I keep making each website bigger one at a time. That is a lot of work. Can I set it once so that every website is bigger from now on, without doing it for each page?",
                 """Yes. You can set one zoom level for all websites:

1. Select **Settings and more** (the three dots menu).
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Visibility**, open the **Page zoom** drop-down.
5. Choose the zoom level you want.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Microsoft Edge (computer)",
             "messages": [
                 "How can I make a web page bigger in Edge on my computer?",
                 """Here is how to zoom in:

1. Select **Settings and more** (the three dots menu).
2. Select **Zoom in** (the plus sign).
3. Select **Zoom in** again until the page is the size you like.""",
                 "I pressed it too many times and now the page is huge. How do I put it back to normal?",
                 """You can put it back in one step. Hold down the **Ctrl** key and press the **0** key. That resets the page to the default size.

Or you can go back to **Settings and more** and select **Zoom out** (the minus sign) until it looks right.""",
             ]},
        ],
    },
    {
        "task_id": "TR-189",
        "task_type": "popups",
        "task": "Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default)",
        "platform": "Chrome (computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chrome Help: Block or allow pop-ups in Chrome", "url": "https://support.google.com/chrome/answer/95472"},
        "source_notes": """Default: "By default, Google Chrome blocks pop-ups from automatically showing up on your screen." When one is blocked, the address bar shows "Pop-up blocked".
Change the default (computer): More (top right) > Settings > Privacy and security > Site Settings > Pop-ups and redirects > "Choose the option that you want as your default setting" (option labels not named on the page).
Allow pop-ups for one site: go to the page where blocked, click "Pop-up blocked" in address bar, click the link for the pop-up, select "Always allow pop-ups and redirects from [site]", click Done.
Block pop-ups for one site: 1 More > Settings. 2 Privacy and security. 3 Site Settings. 4 Pop-ups and redirects. 5 Under "Allowed to send pop-ups and use redirects", find the site. 6 To the right of the site, click More, then Block.
To block a site not listed: click Add next to "Not allowed to send pop-ups or use redirects", enter the address, click Add. Whole domain pattern [*.]example.com.
Troubleshooting: still seeing pop-ups: site may have notification permission; go to the site, click View site information, set Notifications to Block. Pop-ups everywhere: computer may have malware (see help article "Remove unwanted ads, pop-ups & malware"). Chrome device at work or school: you can't change this yourself; network administrator manages the pop-up blocker.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "A website keeps letting pop-ups through in Chrome on my computer. How do I block pop-ups for that site? I can see it in the allowed list.",
                 """Here is how to block pop-ups from a site that is in the allowed list:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**.
3. Click **Site Settings**.
4. Click **Pop-ups and redirects**.
5. Under **Allowed to send pop-ups and use redirects**, find the site.
6. To the right of the site, click **More**, then **Block**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I'm on a Windows computer with Chrome. Whenever I visit a certain coupon website, little windows pop up all over and I have to close each one. I looked in the pop-ups settings and the site is not listed anywhere. I would like Chrome to block it. I know the address of the site. What do I do?",
                 """Since the site is not on any list, you can add it to the blocked list:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**.
3. Click **Site Settings**.
4. Click **Pop-ups and redirects**.
5. Next to **Not allowed to send pop-ups or use redirects**, click **Add**.
6. Type the address of the coupon site.
7. Click **Add**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "A shopping site keeps throwing pop-ups at me. Can you help me block them?",
                 "I can help with that. Are you using Chrome on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "A shopping site keeps throwing pop-ups at me. Can you help me block them?",
                 "I can help with that. Are you using Chrome on a **computer** or on a **phone**?",
                 "chrome on my computer",
                 """Chrome blocks pop-ups on its own, but you can block this site on purpose. If the site is in the allowed list:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Pop-ups and redirects**.
4. Under **Allowed to send pop-ups and use redirects**, find the shopping site.
5. To the right of it, click **More**, then **Block**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I volunteer at a library and use their Chrome computer. It is a Chrome device that the library's network manager looks after. Pop-ups keep showing up and I want to block them in Chrome's settings myself. Can I do that?",
                 """On a Chrome device that is managed for work or school, you can't change this yourself. The network administrator manages the pop-up blocker. Please ask the library's network manager to change it for you.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "How do I block a site from sending me pop-ups in Chrome on my computer? It is in my allowed list.",
                 """Here is how:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Pop-ups and redirects**.
4. Under **Allowed to send pop-ups and use redirects**, find the site.
5. To the right of the site, click **More**, then **Block**.""",
                 "I did all that but that same site is still showing me pop-ups.",
                 """The site may have permission to send notifications. Try this:

1. Go to that site.
2. Click **View site information** in the address bar.
3. Find **Notifications** and set it to **Block**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-190",
        "task_type": "default_browser",
        "task": "Make Chrome the default browser",
        "platform": "Chrome (Windows computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chrome Help: Make Chrome your default browser (computer section)", "url": "https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop"},
        "source_notes": """Before: if Chrome is not installed, download and install it first.
Windows 11: 1 Click Start. 2 Open Settings, then Apps, then Default apps. 3 Under "Set defaults for applications", type Chrome in the search box. 4 Select Google Chrome. 5 At the top, click Set default next to "Make Google Chrome your default browser."
Windows 10: 1 Click Start. 2 Open Settings. 3 Open default apps: original version: System, then Default apps; Creators Update: Apps, then Default apps. 4 At the bottom, under "Web browser", click your current browser. 5 In the "Choose an app" window, select Google Chrome.
Windows 11 shows a Google Chrome settings page with the Set default button at the top plus a "Set default file types or link types" list. Windows 10 shows a list of default browsers then a "Choose an app" pop-up listing Chrome. Windows 10 has no search box or Set default button.
Troubleshooting: Chrome links still open elsewhere: check the "Set default file types or link types" list (Windows 11) so Chrome covers the file types you need. Chrome not in list: confirm Chrome is installed, install first. In some countries you may be asked to choose a default browser and can change anytime.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (Windows computer)",
             "messages": [
                 "How do I make Chrome my default browser on my Windows 11 computer?",
                 """Here is how to do it on Windows 11:

1. Click **Start**.
2. Open **Settings**.
3. Click **Apps**, then **Default apps**.
4. Under **Set defaults for applications**, type **Chrome** in the search box.
5. Select **Google Chrome**.
6. At the top, click **Set default** next to **Make Google Chrome your default browser**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (Windows computer)",
             "messages": [
                 "My computer is a few years old and runs Windows 10. Links in my emails always open in a different browser that came with it and I find it confusing. I have already installed Chrome and I use it for everything else. How can I make Chrome the one that opens by default? I don't see a search box in my settings, if that matters.",
                 """On Windows 10 you pick Chrome from a list instead of searching:

1. Click **Start**.
2. Open **Settings**.
3. Open **Default apps**. It is under **System** or under **Apps**, depending on your version of Windows.
4. At the bottom, under **Web browser**, click the browser that is there now.
5. In the **Choose an app** window, select **Google Chrome**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "Please make chrome my main browser so links open there",
                 "I can help with that. Is your computer a **Windows** PC or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (Windows computer)",
             "messages": [
                 "Please make chrome my main browser so links open there",
                 "I can help with that. Is your computer a **Windows** PC or a **Mac**?",
                 "windows 11",
                 """Thanks. On Windows 11:

1. Click **Start**.
2. Open **Settings**, then click **Apps**, then **Default apps**.
3. Under **Set defaults for applications**, type **Chrome** in the search box.
4. Select **Google Chrome**.
5. At the top, click **Set default** next to **Make Google Chrome your default browser**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (Windows computer)",
             "messages": [
                 "Chrome is already installed on my Windows 11 laptop, so please don't tell me to download anything. I just want Chrome to be the browser that opens when I click a link. Keep it short, my patience is thin today.",
                 """Since Chrome is already installed, here are the steps:

1. Click **Start**, then open **Settings**.
2. Click **Apps**, then **Default apps**.
3. Type **Chrome** in the search box under **Set defaults for applications**.
4. Select **Google Chrome**.
5. At the top, click **Set default**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (Windows computer)",
             "messages": [
                 "Make Chrome the default browser on Windows 11, how?",
                 """Here is how:

1. Click **Start**.
2. Open **Settings**, then click **Apps**, then **Default apps**.
3. Under **Set defaults for applications**, type **Chrome** in the search box.
4. Select **Google Chrome**.
5. At the top, click **Set default** next to **Make Google Chrome your default browser**.""",
                 "I did it but some links still open in the other browser.",
                 """On that same Google Chrome page, look at the list called **Set default file types or link types**. Check that Chrome is chosen for the types you need.""",
             ]},
        ],
    },
    {
        "task_id": "TR-191",
        "task_type": "find_downloads",
        "task": "Find a file downloaded with Chrome",
        "platform": "Chrome (computer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chrome Help: Download a file on Chrome", "url": "https://support.google.com/chrome/answer/95759?hl=en"},
        "source_notes": """Default save location (unless changed): Windows 10 and up: \\Users\\<username>\\Downloads; Mac: /Users/<username>/Downloads; Linux: /home/<username>/Downloads.
Downloads list: click the More icon at top right, then Downloads. After a download finishes, the Download tray opens at the top right, next to the address bar; recent downloads appear there too.
Open: in the Download tray click the file or the Open icon. Point to the filename to reveal more actions such as Show in Folder. On the Downloads page, click the file name to open it in the default app for that file type.
Change location: More > Settings > Downloads; click Change to pick a new default folder, or turn on "Ask where to save each file before downloading".
Troubleshooting: No Download tray: click More, then Downloads to see all downloads. File opens automatically: go to the site, open recent download history, right-click the file, uncheck "Always open files of this type". Remove: click Remove beside the file on the Downloads page; this clears Chrome's list but does not delete the file. Pause, resume, cancel: point to filename in the tray and use the controls.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I downloaded a file with Chrome on my computer but I can't find it. Where did it go?",
                 """Chrome keeps a list of your downloads. To see it:

1. Click **More** (the three dots at the top right).
2. Click **Downloads**.
3. Click the file name to open the file.

Unless the setting was changed, Chrome saves downloads in the **Downloads** folder in your user folder.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "My daughter emailed me a PDF of the family reunion schedule and I downloaded it using Chrome on my Mac computer. Now I want to look at it but I have no idea where Chrome puts things. I haven't changed any settings that I know of. Can you tell me where the file is and how I can open it from Chrome?",
                 """Since you have not changed any settings, Chrome saves it in the **Downloads** folder inside your user folder on your Mac.

To open it from Chrome:

1. Click **More** (the three dots at the top right).
2. Click **Downloads**.
3. Click the file name. It opens in your Mac's usual program for PDF files.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i downloaded something from a website and now i cant find it anywhere",
                 "I can help with that. Which browser did you use to download it: **Chrome**, **Edge**, or something else?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "i downloaded something from a website and now i cant find it anywhere",
                 "I can help with that. Which browser did you use to download it: **Chrome**, **Edge**, or something else?",
                 "chrome, on my computer",
                 """Thanks. In Chrome you can see all your downloads:

1. Click **More** (the three dots at the top right).
2. Click **Downloads**.
3. Click the file name to open the file.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I just finished a download in Chrome on my computer and there is a little box at the top right with the file in it. I don't want to open the file, I want to see which folder it is sitting in so I can move it myself. What do I click?",
                 """You can show the file's folder from that box:

1. In the box at the top right, point to the file name.
2. Click **Show in Folder** from the actions that appear.

That opens the folder where the file is saved, and you can move it from there.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "Where do I find the file I just downloaded in Chrome on my computer?",
                 """After a download finishes, Chrome opens a small download box at the top right, next to the address bar. Your file is listed there. Click the file to open it.""",
                 "I don't see any box at the top. It's not there.",
                 """That is fine. You can see all your downloads another way:

1. Click **More** (the three dots at the top right).
2. Click **Downloads**.
3. Click the file name to open the file.""",
             ]},
        ],
    },
    {
        "task_id": "TR-192",
        "task_type": "password_manager",
        "task": "Save and find passwords with Google Password Manager",
        "platform": "Chrome (computer)",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Chrome Help: Manage passwords in Chrome", "url": "https://support.google.com/chrome/answer/95606?hl=en"},
        "source_notes": """Save automatically: 1 On computer open Chrome, go to the site's sign-up or sign-in page. 2 Enter username and password, submit the form. 3 When Chrome asks to save the password, select Save. 4 To review first, select the Preview icon; if wrong, edit fields before selecting Save.
Save manually: 1 Select More (three dots top right), then Passwords and autofill, then Google Password Manager. 2 Select Add. 3 Enter website, username, password. 4 Select Save.
View/find: 1 More > Passwords and autofill > Google Password Manager. 2 Under "Passwords" select the site. 3 Select the Show password icon to reveal the password. Also passwords.google.com.
Turn saving on/off: Google Password Manager > Settings (left) > "Offer to save passwords and passkeys".
Verification: off by default. Google Password Manager > Settings, turn on Windows: "Use Windows Hello when filling passwords"; Mac: "Use your screen lock when filling passwords"; follow on-screen instructions. Then Chrome asks to verify identity before you can reveal, copy, or edit a password.
Troubleshooting: Chrome doesn't offer to save: confirm "Offer to save passwords and passkeys" is on. Previously declined a site: Google Password Manager > Settings > under "Declined sites and apps" remove the site; Chrome can then offer to save again. If signed in to Chrome, passwords save to your Google Account; if not signed in, only on the device.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "How do I have Chrome save my password on my computer, and how do I look at it later?",
                 """Here is how to save a password in Chrome:

1. Go to the website's sign-in page.
2. Type your username and password, then submit the form.
3. When Chrome asks to save the password, select **Save**.

To find it later:
1. Click **More** (the three dots at the top right).
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Under **Passwords**, select the site.
4. Select the **Show password** icon.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I keep all my website passwords written in a little notebook next to my computer and my son says Chrome can hold them for me instead. I use Chrome on my Windows computer. Chrome has never offered to save any of them. Can I type one in myself so Chrome has it, without waiting for it to ask me?",
                 """Yes, you can add a password yourself:

1. Click **More** (the three dots at the top right).
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Select **Add**.
4. Enter the website, your username, and your password.
5. Select **Save**.

Repeat these steps for each password in your notebook.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i want chrome to remember my passwords so i dont have to write them down",
                 "I can help with that. Are you using Chrome on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "i want chrome to remember my passwords so i dont have to write them down",
                 "I can help with that. Are you using Chrome on a **computer** or on a **phone**?",
                 "my computer",
                 """Thanks. Chrome can save a password when you sign in to a site:

1. Go to the site's sign-in page.
2. Enter your username and password, then submit the form.
3. When Chrome asks to save the password, select **Save**.

To see it again later:
1. Click **More** (the three dots at the top right).
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Under **Passwords**, select the site.
4. Select the **Show password** icon.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "My husband and I share one Windows computer and Chrome has my passwords saved. I don't want him to be able to just click and see them. Can I make Chrome check that it is really me before it shows a saved password?",
                 """Yes. On Windows, you can turn on a check:

1. Click **More** (the three dots at the top right).
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Select **Settings**.
4. Turn on **Use Windows Hello when filling passwords**.
5. Follow the on-screen instructions to confirm.

After that, Chrome asks you to verify who you are before it lets anyone reveal, copy, or edit a password.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "How do I get Chrome on my computer to save a password when I sign in to a website?",
                 """Here is how:

1. Go to the site's sign-in page.
2. Enter your username and password, then submit the form.
3. When Chrome asks to save the password, select **Save**.""",
                 "Chrome never asks me to save anything. I sign in and no question comes up.",
                 """Let's check the setting:

1. Click **More** (the three dots at the top right).
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Select **Settings** on the left.
4. Make sure **Offer to save passwords and passkeys** is turned on.

If you said no to that site before, find **Declined sites and apps** on the same page and remove the site. Chrome can then offer to save it again.""",
             ]},
        ],
    },
]
