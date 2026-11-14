TASKS = [
    {
        "task_id": "TR-180",
        "task_type": "date_time",
        "task": "Fix the wrong date or time",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Set time, date, and time zone settings in Windows", "url": "https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261"},
        "source_notes": """Open settings: Start, then Settings, then Time & language, then Date & time.
Automatic time: open Date & time, turn on Set time automatically.
Manual time: open Date & time, turn off Set time automatically, click Change next to Set the date and time. A Change date and time window opens. Enter the Date and Time, then click Change.
Automatic time zone: turn on Set time zone automatically.
Manual time zone: turn off Set time zone automatically, next to Time zone select the time zone from the drop-down menu.
Daylight saving: if Set time zone automatically is on, daylight saving time is set automatically. If off, turn on Adjust for daylight saving time automatically for automatic adjustment; to set manually, turn that option off and set the time yourself.
Optional: Show time and date in the System tray on/off; Show seconds in system tray clock (uses more power).
No troubleshooting (no Sync now, no greyed out notes).""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """The clock on my Windows 11 computer is showing the wrong time. How can I get it to set itself correctly?""",
                 """Windows can set the time for you. Here is how.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn on **Set time automatically**.

If the time is still wrong, check that **Set time zone automatically** is also turned on in the same screen.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """My husband says the clocks went back an hour last weekend but my Windows 11 laptop is now showing one hour off. I turned off the automatic time zone thing a while ago because it kept putting me in the wrong city. I would like it to follow the daylight saving change without me doing it by hand each time. Can you tell me what to do?""",
                 """You can turn on a setting that changes the clock for daylight saving time on its own.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn on **Adjust for daylight saving time automatically**.

Since your automatic time zone is off, this is the setting that handles the change. Your time zone stays as you chose it.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 """my computer clock is wrong again, can you help me fix it""",
                 """I can help with that. Is your computer a **Windows PC** or a **Mac**?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """my computer clock is wrong again, can you help me fix it""",
                 """I can help with that. Is your computer a **Windows PC** or a **Mac**?""",
                 """Windows 11""",
                 """Thanks. Here is how to let Windows set the time itself.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn on **Set time automatically**.

If it is still wrong, make sure **Set time zone automatically** is turned on too.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I have a Windows 11 PC and I do not want Windows to change the time by itself, I want to type in the date and time myself. Today is the right date but it shows the wrong hour. How do I type it in?""",
                 """You can set it by hand. Here is how.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn off **Set time automatically**.
5. Click **Change** next to **Set the date and time**. A **Change date and time** window opens.
6. Enter the **Date** and **Time**.
7. Click **Change**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """My Windows 11 computer has the wrong date. I want to type in the right one myself. What do I do?""",
                 """You can change it by hand.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn off **Set time automatically**.
5. Click **Change** next to **Set the date and time**.
6. Enter the **Date** and **Time**, then click **Change**.""",
                 """I opened Date & time but I can't find a Change button to click, or it won't let me click it.""",
                 """The **Change** button works only after you turn off the automatic setting.

1. On the **Date & time** screen, find **Set time automatically**.
2. Turn it off.
3. Now click **Change** next to **Set the date and time**.

A **Change date and time** window should open so you can enter the date.""",
             ]},
        ],
    },
    {
        "task_id": "TR-181",
        "task_type": "organize_files",
        "task": "Create a folder and move files into it",
        "platform": "Windows 11 (File Explorer)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Windows Learning Center: Create new folders to organize files", "url": "https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files"},
        "source_notes": """Create a folder: open File Explorer. Select Home in the upper-left corner of the window. Click the New folder icon. A new folder appears in the window, ready for a name. Rename: right-click the folder's name and enter a new one. Alternative: press Ctrl + Shift + N to create a new folder without using the menu.
Move files: select the file you want to move, drag the file into the new folder. Multiple files: select each file, then drag the group into the folder at once.
The page does not describe cut and paste. Features may vary by region.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """On my Windows 11 computer, how do I make a new folder and put a file in it?""",
                 """Here is how to make a folder and move a file into it.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon. A new folder appears, ready for a name.
4. Right-click the name of the new folder and type the name you want.
5. Select the file you want to move.
6. Drag the file into the new folder.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """My grandson set up this Windows 11 computer for me and now everything I save piles up in one big mess. I want a folder just for my recipes and then to put my recipe documents in it. I only know how to use File Explorer a little bit. Could you walk me through making the folder first and then moving them over?""",
                 """Happy to. Start with the folder.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon.
4. Right-click the name of the new folder and type **Recipes**.

Now move the recipes.

5. Select one recipe document.
6. Drag it into the new folder.

To move several at once, select each one first, then drag the group into the folder together.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 """I need to make a folder so I can put my tax papers in it""",
                 """I can help with that. Are you using a **Windows PC** or a **Mac**?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I need to make a folder so I can put my tax papers in it""",
                 """I can help with that. Are you using a **Windows PC** or a **Mac**?""",
                 """windows 11""",
                 """Here is how to make the folder and move your papers into it.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon.
4. Right-click the name of the new folder and type a name such as Taxes.
5. Select a tax file.
6. Drag it into the new folder.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I have a Windows 11 PC and about twenty vacation photos in File Explorer that I want in one new folder. I do not want to drag them one at a time because my hand shakes, so is there a way to move all of them together?""",
                 """Yes, you can select them all and move them in one drag.

1. In **File Explorer**, select **Home** in the upper-left corner.
2. Click the **New folder** icon, or press **Ctrl + Shift + N**.
3. Right-click the name of the new folder and type a name for it.
4. Select each of your photos.
5. Drag the whole group into the new folder at once.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """Windows 11 here. How do I make a new folder in File Explorer?""",
                 """Here is how.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon.

A new folder appears in the window, ready for a name.""",
                 """OK I made it but it just has a plain name and I want to call it Insurance. How do I change the name?""",
                 """You can rename it from the folder's name.

1. Right-click the name of the new folder.
2. Type **Insurance** as the new name.

Next time you can also press **Ctrl + Shift + N** to make a new folder without using the menu.""",
             ]},
        ],
    },
    {
        "task_id": "TR-182",
        "task_type": "mouse_settings",
        "task": "Change mouse settings such as speed",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Change mouse settings", "url": "https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings"},
        "source_notes": """Replaced Recycle Bin topic (the Microsoft page found only covers showing a missing Recycle Bin icon, not restoring files).
Main page: Start > Settings > Bluetooth & devices > Mouse. Additional mouse settings is under Related settings.
Primary mouse button: drop-down, choose Left or Right.
Pointer speed: move slider next to Mouse pointer speed.
Enhance pointer precision: set to On for accuracy at slow speeds.
Double-click speed: Additional mouse settings, Buttons tab, under Double-click speed adjust the Speed: slider, OK.
Scrolling (in Mouse): Roll the mouse wheel to scroll (Multiple lines at a time / One screen at a time); Lines to scroll at a time slider; Scroll inactive windows when hovering over them On; Scrolling direction (Down motion scrolls down / Down motion scrolls up).
Pointer Options tab: Display pointer trails with slider Short to Long; Hide pointer while typing; Show location of pointer when I press the CTRL key (press CTRL to see a circle around the pointer); OK.
ClickLock: Buttons tab, Turn on ClickLock, lets you drag or highlight without holding the button.
Pointer look: Start > Settings > Accessibility > Mouse pointer and touch, Mouse pointer style, Size slider.
No troubleshooting in page.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """The mouse pointer on my Windows 11 computer moves too fast and I keep overshooting. How can I slow it down?""",
                 """You can change the pointer speed with a slider.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Move the slider next to **Mouse pointer speed** to change how fast the pointer moves.

Try the mouse on the screen after each change to see if the speed feels right.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I am left handed and I have always used my mouse in my left hand, but on my new Windows 11 computer the left button does the clicking that the right button should do for me. I would like the right button to be the main one. Where is that setting?""",
                 """There is a setting for exactly that.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Open the drop-down next to **Primary mouse button**.
5. Choose **Right**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 """my mouse is too slow, how do i change it""",
                 """I can help with that. Is your computer a **Windows PC** or a **Mac**?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """my mouse is too slow, how do i change it""",
                 """I can help with that. Is your computer a **Windows PC** or a **Mac**?""",
                 """it's a windows 11 pc""",
                 """Thanks. You can change the pointer speed with a slider.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Move the slider next to **Mouse pointer speed**.

Try the pointer after each change to find a speed you like.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """On my Windows 11 PC the pointer speed is fine and so is the left button. The only thing that bothers me is that I have to click twice so fast to open a file that I often miss. Please don't change anything else, just the double click timing.""",
                 """That is a separate setting, so nothing else will change.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Under **Related settings**, click **Additional mouse settings**.
5. Click the **Buttons** tab.
6. Under **Double-click speed**, adjust the **Speed:** slider.
7. Click **OK**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """Windows 11 computer. I double click too slowly and the computer thinks I only clicked once. How do I give myself more time between the clicks?""",
                 """You can change the double-click speed.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Click **Additional mouse settings**.
5. Click the **Buttons** tab.
6. Under **Double-click speed**, adjust the **Speed:** slider.
7. Click **OK**.""",
                 """I'm on the Mouse page but I don't see anything called Additional mouse settings.""",
                 """It is a link lower down on the same **Mouse** page.

1. Scroll down the **Mouse** page until you see **Related settings**.
2. Click **Additional mouse settings** there.
3. Then continue with the **Buttons** tab as before.""",
             ]},
        ],
    },
    {
        "task_id": "TR-183",
        "task_type": "virus_scan",
        "task": "Run a virus scan with Windows Security",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Virus and threat protection in the Windows Security app", "url": "https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e"},
        "source_notes": """Also read Microsoft Support "Stay protected with the Windows Security app": to open the app, search for it in the Start menu. To scan one file or folder, right-click it in File Explorer and select Scan with Microsoft Defender; on Windows 11 you may need to choose Show more options first.
Main page: in the Windows Security app, select Virus & threat protection. You see the Current threats section.
Quick scan: under Current threats, select Start a quick scan. Faster. Scan runs and reports when finished.
Scan options (under Current threats): Quick scan; Full scan (scans every file and program, takes longer); Custom scan (only files and folders you select); Microsoft Defender Antivirus (offline scan).
Full scan: on Scan options page select Start a full scan.
Results: under Current threats see last scan time, how long it took, how many files scanned; quarantined threats appear there. If Windows Security recommends a different scan type you are notified when the quick scan finishes.
Notes: Windows Security scans automatically but you can run extra scans. Offline scan restarts the device, so save open files first; results appear in Protection history. If you accidentally allowed a threat, open Allowed threats, select the item, choose Don't allow.
Troubleshooting: if scans are not running because a compatible non-Microsoft antivirus program is installed, Microsoft Defender Antivirus turns itself off automatically; scan with that program instead.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """How do I check my Windows 11 computer for viruses with the built in security program?""",
                 """You can run a quick scan in Windows Security.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

The scan runs and reports when it finishes. You can see the last scan time and how many files were scanned in the same place.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """My Windows 11 laptop has been acting strange since I opened an email attachment last night and I am worried something got on it. I do not have time for a long scan right now, I just want the fastest check Windows can do. Which button do I press?""",
                 """The quick scan is the faster option.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

When it finishes, look under **Current threats** to see what was scanned and whether any threats were quarantined.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 """i think i have a virus, how do i scan my computer""",
                 """I can help with that. Is your computer a **Windows PC** or a **Mac**?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """i think i have a virus, how do i scan my computer""",
                 """I can help with that. Is your computer a **Windows PC** or a **Mac**?""",
                 """Windows 11""",
                 """Thanks. Windows has a scan built in.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

When it finishes, the same area shows what was scanned and any threats that were quarantined.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I have a Windows 11 PC and I want the most thorough virus check possible, even if it takes a long time. I plan to leave it running overnight. Which scan should I pick in Windows Security?""",
                 """The full scan checks everything.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Scan options**.
4. Select **Start a full scan**.

A full scan checks every file and program on your device, so it takes longer than a quick scan.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """How do I run a virus scan on my Windows 11 PC?""",
                 """Here is a quick way.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.""",
                 """It says the scans aren't running and I think I installed another antivirus program a while ago. What now?""",
                 """That is likely the reason. When a compatible antivirus program from another company is installed, Microsoft Defender Antivirus turns itself off on its own.

1. Open that other antivirus program.
2. Run the scan from there instead.""",
             ]},
        ],
    },
    {
        "task_id": "TR-184",
        "task_type": "backup_photos",
        "task": "Back up photos and folders with OneDrive",
        "platform": "Windows 11 (OneDrive)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Back up your folders with OneDrive", "url": "https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057"},
        "source_notes": """Open OneDrive settings: select the OneDrive cloud icon in the notification area, select the Help & Settings icon, then select Settings.
Select the Sync and backup tab. Select Manage backup. A folder selection dialog appears listing your important folders (Documents, Desktop, Pictures).
Turn on the toggle for each folder labeled Not backed up, then select Save changes.
Conditions: each folder must be in its default location. For Pictures, make sure Pictures, Screenshots and Camera Roll are all selected or don't exist.
Result: backed up folders are available in File Explorer under OneDrive and in the OneDrive mobile app. Desktop items follow you to other PCs running OneDrive.
Stop backup: in Manage backup turn off the toggle for the folder, then choose keep files only in OneDrive or only on your PC.
Notes: cloud-only files block the move; you see a message to download them first by setting them to Always keep on this device. Open files can't be moved; save and close them first. Files over 250GB can't sync. Path must be under 260 characters. File names can't start with a space or contain \\ : / * ? < > " |.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """How can I back up the pictures on my Windows 11 computer using OneDrive?""",
                 """You can turn on backup for your Pictures folder in OneDrive.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures**.
6. Select **Save changes**.

Your backed up folders then show up in File Explorer under OneDrive.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """My old computer died last year and I lost everything, so I never want that to happen again. I have a Windows 11 PC now with OneDrive already on it. I keep my letters in Documents and my family photos in Pictures. Please show me how to have OneDrive keep copies of both.""",
                 """OneDrive can back up both folders.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Documents** and for **Pictures**.
6. Select **Save changes**.

Your backed up folders then show up in File Explorer under OneDrive.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 """I want to make sure my photos are safe, can you help me back them up with OneDrive?""",
                 """I can help with that. Are your photos on a **Windows PC** or a **Mac**?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I want to make sure my photos are safe, can you help me back them up with OneDrive?""",
                 """I can help with that. Are your photos on a **Windows PC** or a **Mac**?""",
                 """Windows 11 PC""",
                 """Thanks. Here is how to back up your Pictures folder.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures**.
6. Select **Save changes**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """I use Windows 11 and OneDrive. I only want my photos backed up. My Desktop is full of things I do not want in the cloud and I do not want my Documents copied either. How do I back up just Pictures?""",
                 """You choose each folder with its own toggle, so you can pick only Pictures.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures** only. Leave **Desktop** and **Documents** off.
6. Select **Save changes**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 """Windows 11 PC. How do I make OneDrive back up my Pictures folder?""",
                 """Here is how.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures**.
6. Select **Save changes**.""",
                 """It gave me an error saying some of my files are online only and need to be downloaded first. What should I do?""",
                 """Those files are stored only in the cloud, which blocks the move. Set them to keep a copy on your computer first.

1. Find the online only files in your Pictures folder.
2. Set them to **Always keep on this device**.
3. Go back to **Manage backup** and try **Save changes** again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-185",
        "task_type": "account_password_reset",
        "task": "Reset a forgotten Microsoft account password",
        "platform": "Microsoft account",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Microsoft Support: Reset a forgotten Microsoft account password", "url": "https://support.microsoft.com/help/4026971"},
        "source_notes": """Step 1: if the Enter password window is still open, select Forgotten your password? Otherwise select Reset password, enter the username, select Next.
Step 2: choose how you want to receive a verification code, then select Next.
Step 3: retype the first part of the email address or the last four digits of the phone number shown. Select Get code, then check the email or phone you selected.
Step 4: paste or type the code and select Next. Type your new password and select Next again.
If no place to send a code, no access to any verification option shown, or you don't recognize the listed options: use the sign-in helper tool (https://go.microsoft.com/fwlink/?linkid=2242650 for no option or no access; https://go.microsoft.com/fwlink/?linkid=2241144 if you don't recognize the options). Support agents can't send password reset links or access and change account details.
If you can't get a code, see the article on troubleshooting verification code issues. If the steps don't work, use the sign-in helper tool. No password rules listed.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Microsoft account",
             "messages": [
                 """I forgot the password for my Microsoft account and I'm on the sign in screen. What do I do?""",
                 """You can reset it with a code that Microsoft sends you.

1. On the **Enter password** window, select **Forgotten your password?**
2. Choose how you want to get a verification code, then select **Next**.
3. Retype the first part of the email address, or the last four digits of the phone number, that is shown. Select **Get code**.
4. Check that email or phone, then type the code and select **Next**.
5. Type your new password and select **Next** again.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Microsoft account",
             "messages": [
                 """I closed the sign in box on my Microsoft account by mistake and now I don't remember my password at all. I haven't used the account in months. I do still have my phone, which I think is the number linked to the account. How can I reset the password using my phone?""",
                 """You can start the reset again and have a code sent to your phone.

1. Select **Reset password**, enter the username for your account, and select **Next**.
2. Choose the phone option to get a verification code, then select **Next**.
3. Retype the last four digits of the phone number shown, then select **Get code**.
4. Check your phone, then type the code and select **Next**.
5. Type your new password and select **Next** again.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 """i forgot my password and cant get in, please help""",
                 """I can help with that. Is this the password for your **Microsoft account**, or for something else?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Microsoft account",
             "messages": [
                 """i forgot my password and cant get in, please help""",
                 """I can help with that. Is this the password for your **Microsoft account**, or for something else?""",
                 """its my microsoft account""",
                 """Thanks. You can reset it with a code that Microsoft sends you.

1. Select **Forgotten your password?** if the **Enter password** window is open. If not, select **Reset password**, enter your username, and select **Next**.
2. Choose how to get a verification code, then select **Next**.
3. Retype the first part of the email address, or the last four digits of the phone number, shown. Select **Get code**.
4. Type the code and select **Next**.
5. Type your new password and select **Next** again.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Microsoft account",
             "messages": [
                 """I forgot my Microsoft account password. I don't want to call anyone or wait for a person to help me. Is there a way to do the whole reset myself on the computer? I can read my email.""",
                 """Yes, you can do the whole reset yourself. A support agent can't send reset links or change account details for you anyway.

1. Select **Reset password**, enter your username, and select **Next**.
2. Choose the email option for a verification code, then select **Next**.
3. Retype the first part of the email address shown, then select **Get code**.
4. Open that email, then type the code and select **Next**.
5. Type your new password and select **Next** again.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Microsoft account",
             "messages": [
                 """I forgot my Microsoft account password. How do I reset it?""",
                 """You can reset it with a code that Microsoft sends you.

1. Select **Forgotten your password?** on the **Enter password** window. If you do not see it, select **Reset password**, enter your username, and select **Next**.
2. Choose how to get a verification code, then select **Next**.
3. Retype the first part of the email address, or the last four digits of the phone number, shown. Select **Get code**.
4. Type the code and select **Next**.
5. Type your new password and select **Next** again.""",
                 """It only shows an old email address and a phone number I don't have anymore, so I can't get a code.""",
                 """Then use Microsoft's sign-in helper tool. It is meant for when you no longer have access to any of the options shown.

1. Go to https://go.microsoft.com/fwlink/?linkid=2242650
2. Follow the steps the tool gives you.

Support agents can't send reset links or change your account details, so the tool is the way forward.""",
             ]},
        ],
    },
]
