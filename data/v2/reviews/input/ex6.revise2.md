# Revision list: batch ex6, after review round 2 (19 examples)

Edit ONLY these examples in data/v2/specs/ex6.py, then rebuild.

## tr077-d
- reasons: The reply describes the Settings control as an icon, which the Pixel help page does not say. The rest of the steps match the page.
- fix requested: In the paragraph starting 'If nothing appears', change 'tap the **Settings** icon in Camera' to 'tap **Settings** in Camera'. Keep 'tap **More settings**' and 'make sure **Camera scan suggestions** is on' unchanged. Source: https://support.google.com/pixelphone/answer/16561572?hl=en
- unsupported claims: 'tap the **Settings** icon in Camera' -> the Pixel page says only: Tap "Settings". It does not describe an icon, so the word 'icon' is unsupported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en ; https://support.google.com/pixelphone/answer/16561572?hl=en

## tr078-a
- reasons: The opening gives a specific setup time that the page does not give. The steps and the Lock Screen claim match the page.
- fix requested: Delete the sentence 'It takes about five minutes.' from the first paragraph. Keep the rest unchanged. Source: https://support.apple.com/en-us/105072
- unsupported claims: 'It takes about five minutes.' -> the page gives no setup duration.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105072

## tr078-d
- reasons: The reply gives a specific setup time that the page does not give. The steps match the page.
- fix requested: In the first paragraph of the final reply, delete the sentence 'It takes about five minutes.' Keep the rest unchanged. Source: https://support.apple.com/en-us/105072
- unsupported claims: 'It takes about five minutes.' -> the page gives no setup duration.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105072

## tr081-a
- reasons: Option 2, step 3 gives a label that does not match the page. The page's label is 'All notifications'. Otherwise the steps match the source.
- fix requested: In Option 2, step 3, change 'Turn off notifications.' to 'Turn off **All notifications**.' Source: https://support.google.com/android/answer/9079661?hl=en
- unsupported claims: 'Turn off notifications.' (Option 2, step 3) -> the page's on-screen label is 'All notifications', not 'notifications'. The reply does not use the exact label.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9079661?hl=en

## tr081-d
- reasons: Option 2, step 3 gives a label that does not match the page. The page's label is 'All notifications'. Otherwise the steps match the source.
- fix requested: In Option 2, step 3, change 'Turn off notifications.' to 'Turn off **All notifications**.' Source: https://support.google.com/android/answer/9079661?hl=en
- unsupported claims: 'Turn off notifications.' (Option 2, step 3) -> the page's on-screen label is 'All notifications', not 'notifications'. The reply does not use the exact label.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9079661?hl=en

## tr082-a
- reasons: The mouse step names the Zoom controls with symbols the page does not show. The page's on-screen labels are 'Zoom in' and 'Zoom out', so the user may not find the matching controls.
- fix requested: In the 'With the mouse' step 2, change 'Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.' to 'Next to **Zoom**, click **Zoom in** to make the page bigger. Click **Zoom out** to make it smaller.' Leave the keyboard shortcuts unchanged, since the page gives Ctrl and + and Ctrl and -. Source: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop
- unsupported claims: 'click **+** to make the page bigger. Click **-** to make it smaller' -> the page labels these controls 'Zoom in' and 'Zoom out' and does not describe them as plus or minus symbols. Only the keyboard shortcuts use + and -.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr082-d
- reasons: The mouse step names the Zoom controls with symbols the page does not show. The page's on-screen labels are 'Zoom in' and 'Zoom out', so the user may not find the matching controls.
- fix requested: In the 'With the mouse' step 2, change 'Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.' to 'Next to **Zoom**, click **Zoom in** to make the page bigger. Click **Zoom out** to make it smaller.' Leave the keyboard shortcuts unchanged, since the page gives Ctrl and + and Ctrl and -. Source: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop
- unsupported claims: 'click **+** to make the page bigger. Click **-** to make it smaller' -> the page labels these controls 'Zoom in' and 'Zoom out' and does not describe them as plus or minus symbols. Only the keyboard shortcuts use + and -.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr083-a
- reasons: The opening sentence states where downloads are saved, which the page does not say. The steps themselves match the page.
- fix requested: Replace the first sentence 'Files you download usually go to your **Downloads** folder. Here's how to find it.' with 'Here's how to open your **Downloads** folder.' Keep the three steps and the Pin to Quick access fallback unchanged. Source: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8
- unsupported claims: 'Files you download usually go to your **Downloads** folder.' -> the page does not say that downloaded files are saved to Downloads by default. It only lists Downloads among the known folders.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr083-c
- reasons: The opening sentence says where the insurance card was saved, which the page does not support. The steps match the page.
- fix requested: Replace the first sentence 'It's most likely in your **Downloads** folder. Here's how to find it.' with 'Here's how to open your **Downloads** folder.' Keep the three steps and the Pin to Quick access fallback unchanged. Source: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8
- unsupported claims: 'It's most likely in your **Downloads** folder.' -> the page does not say that downloaded files are saved to Downloads. It only lists Downloads among the known folders.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr083-d
- reasons: The opening sentence says where downloads are saved, which the page does not say. The steps match the page.
- fix requested: Replace the first sentence 'Files you download usually go to your **Downloads** folder. Here's how to find it.' with 'Here's how to open your **Downloads** folder.' Keep the three steps and the Pin to Quick access fallback unchanged. Source: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8
- unsupported claims: 'Files you download usually go to your **Downloads** folder.' -> the page does not say that downloaded files are saved to Downloads by default. It only lists Downloads among the known folders.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr084-a
- reasons: Steps 4 and 5 use bold words as if they were on-screen labels, but the page does not name those controls. The user may not find a control called Size or Color.
- fix requested: In steps 4 and 5, remove the bold formatting from **size** and **color**, and say 'Change the size of the mouse pointer to make it bigger.' and 'You can also change the color of the mouse pointer so it stands out more.' Do not name a control. Source: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see
- unsupported claims: 'Change the **size**' and 'change the pointer's **color**' (steps 4 and 5) -> the page says only 'changing the color and size of the mouse pointer' and does not name these as on-screen controls. Bold type presents them as labels the user will see, and the page does not confirm that.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

## tr084-d
- reasons: Steps 4 and 5 use bold words as if they were on-screen labels, but the page does not name those controls. The user may not find a control called Size or Color.
- fix requested: In steps 4 and 5, remove the bold formatting from **size** and **color**, and say 'Change the size of the mouse pointer to make it bigger.' and 'You can also change the color of the mouse pointer so it stands out more.' Do not name a control. Source: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see
- unsupported claims: 'Change the **size**' and 'change the pointer's **color**' (steps 4 and 5) -> the page says only 'changing the color and size of the mouse pointer' and does not name these as on-screen controls. Bold type presents them as labels the user will see, and the page does not confirm that.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

## tr085-a
- reasons: The opening gives a specific setup time that the page does not give. The steps, the second-step description, and the code and call warnings match the page.
- fix requested: Delete the sentence 'Setting it up takes about five minutes.' from the first paragraph. Keep the rest unchanged. Sources: https://support.google.com/accounts/answer/185839?hl=en and https://support.google.com/accounts/answer/7682439?hl=en
- unsupported claims: 'Setting it up takes about five minutes.' -> the page gives no setup duration.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

## tr085-d
- reasons: The reply gives a specific setup time that the page does not give. The steps and warnings match the page. Earlier-turn style note, only because the decision is revise: the first assistant turn asks two questions in one message ('Which email do you use...? And are you on a computer or a phone?'). It is not scored.
- fix requested: Delete the sentence 'Setting it up takes about five minutes.' from the final reply. Keep the rest unchanged. Sources: https://support.google.com/accounts/answer/185839?hl=en and https://support.google.com/accounts/answer/7682439?hl=en
- unsupported claims: 'Setting it up takes about five minutes.' -> the page gives no setup duration.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

## tr086-a
- reasons: One warning sign names 'locked', which the page does not say. The rest of the warnings, the steps, and the reporting addresses match the page.
- fix requested: In the Warning signs list, change 'It says your account is **locked** or has a **problem**.' to 'It says there is a **problem** with your account.' Keep the other warnings and the 'What to do' steps unchanged. Source: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams
- unsupported claims: 'It says your account is **locked** or has a **problem**.' -> the page says scammers claim 'there's a problem with your account or your payment information'. It does not mention a locked account.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr086-d
- reasons: One warning sign names 'locked', which the page does not say. The rest of the warnings, the steps, and the reporting addresses match the page.
- fix requested: In the Warning signs list, change 'It says your account is **locked** or has a **problem**.' to 'It says there is a **problem** with your account.' Keep the other warnings and the 'What to do' steps unchanged. Source: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams
- unsupported claims: 'It says your account is **locked** or has a **problem**.' -> the page says scammers claim 'there's a problem with your account or your payment information'. It does not mention a locked account.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr087-a
- reasons: Two factual details are not on the page: a claim that most phones have the report option in the messaging app, and an explanation that 7726 spells SPAM on a keypad. The steps and the FTC address match the page.
- fix requested: In step 1, change 'Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.' to 'Look for the option to report **junk** or **spam**.' In step 2, delete '(it spells SPAM on the keypad)'. Keep everything else unchanged. Source: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages
- unsupported claims: 'Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.' -> the page says only 'Look for the option to report junk or spam' and that a phone 'may have' a filter option. It does not say most phones have this. | '(it spells SPAM on the keypad)' -> the page says 'forward it to 7726 (SPAM)' and does not say the number spells SPAM on a keypad.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr087-c
- reasons: Two factual details are not on the page: a claim that most phones have the report option in the messaging app, and an explanation that 7726 spells SPAM on a keypad. The steps and the FTC address match the page.
- fix requested: In step 1, change 'Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.' to 'Look for the option to report **junk** or **spam**.' In step 2, delete '(it spells SPAM on the keypad)'. Keep everything else unchanged. Source: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages
- unsupported claims: 'Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.' -> the page says only 'Look for the option to report junk or spam' and that a phone 'may have' a filter option. It does not say most phones have this. | '(it spells SPAM on the keypad)' -> the page says 'forward it to 7726 (SPAM)' and does not say the number spells SPAM on a keypad.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr087-d
- reasons: Two factual details are not on the page: a claim that most phones have the report option in the messaging app, and an explanation that 7726 spells SPAM on a keypad. The steps and the FTC address match the page.
- fix requested: In step 1, change 'Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.' to 'Look for the option to report **junk** or **spam**.' In step 2, delete '(it spells SPAM on the keypad)'. Keep everything else unchanged. Source: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages
- unsupported claims: 'Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.' -> the page says only 'Look for the option to report junk or spam' and that a phone 'may have' a filter option. It does not say most phones have this. | '(it spells SPAM on the keypad)' -> the page says 'forward it to 7726 (SPAM)' and does not say the number spells SPAM on a keypad.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages
