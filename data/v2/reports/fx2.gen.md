# fx2 generation report

Sources used (all fetched and read):
- TR-014: https://www.ftc.gov/node/54353
- TR-015: https://consumer.ftc.gov/node/84809
- TR-016: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay
- TR-017: SKIPPED. https://www.facebook.com/help/120939471321735 (and the m. version) returned robots_disallowed; only archived copies exist, which I did not use. No new examples; the pilot-017 stays alone (needs a backup topic or another source).
- TR-021: https://support.apple.com/en-us/102453
- TR-022: https://support.google.com/accessibility/android/answer/11183305?hl=en
- TR-024: https://support.apple.com/en-us/105103 (also https://support.apple.com/en-us/118444)
- TR-025: https://support.google.com/android/answer/9082609?hl=en
- TR-026: https://support.apple.com/en-us/108066
- TR-027: https://support.google.com/android/answer/9075928?hl=en
- TR-028: https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots
- TR-030: https://support.google.com/android/answer/9075847?hl=en
- TR-031: https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows

Topics replaced by backups: none.

Design notes:
- TR-016: pilot is missing_info, so I wrote d (followup using the pilot's exact opening and question), c, e, r (already_acted), g (prevention). No a or f.
- TR-014/015: the sources give no recovery advice for people who already paid (014) or only "contact your bank directly" (015); the r replies say so and give only source advice.

Not fully sure the page supports:
- TR-014 f: "Reassure her" has no direct source line (tone only).
- TR-021 e: Larger Text path is supported; the page does not say the standard slider has an end limit.
- TR-022 e: page says the Font Size tile is added to Quick Settings automatically after changing font size in Settings; I assumed that moving the slider triggers it.
- TR-024 r: which switch/Action button applies depends on model; the page does not say which direction to flip the switch, so I only say flip it until orange is not showing.
- TR-026 r: "make sure software is up to date" is the page's wording; the page gives no update steps.
- TR-030 r: that a missing network may be hidden is an inference; the page only says to wait for the list to reload, and separately describes Add network.

Existing examples the sources show as wrong or unsupported:
- pilot-014: points to ReportFraud.ftc.gov, but the cited FTC page says www.ftc.gov/complaint. Also "hang up if they call back" and "gift cards are almost impossible to get back" are not on the page.
- tr024-a, tr024-c, tr024-d: say the Sounds & Haptics > Ringtone and Alerts slider sets ringer volume. Apple's page 118444 frames that slider as alarm volume (with Change with Buttons); 105103 does not describe it as ringer volume.
- tr025-a, tr025-d: say tap the "More" icon in the volume panel; the page says "Menu" icon.
- tr025-d: includes a Samsung note, but the source is Android Help (Pixel style); not shown to apply to Samsung.
