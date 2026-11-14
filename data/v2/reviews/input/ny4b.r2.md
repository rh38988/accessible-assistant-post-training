# Review input: batch ny4b, round 2 (7 examples)

## tr169-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
How do I connect my Chromebook to my home Wi-Fi? It needs a password.

**ASSISTANT:**
Here is how to connect:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. Then do the steps above.

## tr169-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
I am at a coffee shop with my Chromebook and they said the Wi-Fi is open, no password needed. I have never done this before and I do not want to mess anything up. How do I get on their network?

**ASSISTANT:**
It is simple. Here are the steps:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select the coffee shop's network.
5. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. If a sign-in page opens in your browser, finish it to complete the connection.

## tr169-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
how do I get on the wifi

**ASSISTANT:**
I can help with that. What device do you want to connect: a **Chromebook**, a **phone**, or a different computer?

**USER:**
my chromebook

**ASSISTANT:**
Thanks. Here is how to connect your Chromebook:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. If it asks, type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. Then do the steps above.

## tr169-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
My Chromebook keeps forgetting my Wi-Fi and I am tired of typing the password. I am connecting at my house right now. Is there a way to connect and have it reconnect by itself next time?

**ASSISTANT:**
Yes. First connect, then turn on automatic reconnecting:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.
7. Select your network again in the Wi-Fi list, then turn on **Automatically connect to this network**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**.

## tr169-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
I moved to a new apartment. Please help me get my Chromebook on the new password-protected Wi-Fi.

**ASSISTANT:**
Here is how:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**.

**USER:**
My network name is not shown because the router is set to hide its name, but I know the name and password.

**ASSISTANT:**
You can add the network by hand:

1. Select the time at the bottom right, then select **Settings**.
2. Select **Network**.
3. Select **Add connection**, then **Add Wi-Fi**.
4. Enter the network information.
5. Select **Connect**.

## tr170-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

**USER:**
How do I update my Chromebook? It is connected to Wi-Fi.

**ASSISTANT:**
Here is how:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.
5. When the download finishes, select **Restart** in the **Update device** message near the date.

**USER:**
I did that but the update never seems to download, it just sits there.

**ASSISTANT:**
Try these in order, and test after each one:

1. Turn your Chromebook off, then back on.
2. If you ever use your phone's connection, switch to Wi-Fi or Ethernet instead.
3. If it still will not download, the next step is a reset. A reset does not delete your personal files.
4. If that does not work, recovery is the last step. Recovery permanently erases everything on the drive, including downloads, so back up your files first if you can.

## tr171-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

**USER:**
Is there a keyboard shortcut for the full screen magnifier on a Chromebook?

**ASSISTANT:**
Yes. Press **Ctrl + Search + m** to magnify your whole screen. If your keyboard has a Launcher key instead of a Search key, press **Ctrl + Launcher + m**.

To make it bigger or smaller, press **Ctrl + Alt** and the brightness up or down key.

**USER:**
I pressed it and nothing happened.

**ASSISTANT:**
I am not sure why that happened. You can turn the magnifier on from Settings instead:

1. Select the time at the bottom right of the screen.
2. Select **Settings**, then **Accessibility**.
3. Under **Display**, turn on **Full screen magnifier**.
