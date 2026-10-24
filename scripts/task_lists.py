"""Training and eval task lists, split by TASK TYPE.

A task type (e.g. "text_size") belongs to exactly one split. Every platform
and language version of that type stays in the same split, so the eval set
never tests a task the model was trained on, even on a different phone.

Run to regenerate the CSVs and check the split:
    python scripts/task_lists.py
Outputs:
    data/tasks/train_tasks.csv
    eval/tasks/eval_tasks.csv
"""
import csv
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

C, O, T = "communication", "online_services", "technical_support"

# (task_type, task description, platform, category, language, sensitive, pilot example id or "")
TRAIN = [
    # ---- tasks already covered by pilot v1 ----
    ("text_size", "Make text bigger", "Samsung Galaxy", T, "en", False, "pilot-001"),
    ("ring_volume", "Turn up ring volume (device unknown)", "unknown", T, "en", False, "pilot-002"),
    ("send_photo_text", "Send a photo by text message", "Android (Google Messages)", C, "en", False, "pilot-003"),
    ("screenshot", "Take a screenshot", "iPhone", T, "en", False, "pilot-004"),
    ("email_not_working", "Email stopped working (details unknown)", "unknown", C, "en", False, "pilot-005"),
    ("printer_not_printing", "Printer will not print", "unknown", T, "en", False, "pilot-006"),
    ("wifi_connect", "Connect to a Wi-Fi network", "iPhone", T, "en", False, "pilot-007"),
    ("display_scale", "Make everything on screen bigger", "Windows 11", T, "en", False, "pilot-008"),
    ("internet_not_working", "Internet not working (message cut off)", "unknown", T, "en", False, "pilot-009"),
    ("account_password_reset", "Reset forgotten Apple Account password", "iPhone", O, "en", True, "pilot-010"),
    ("software_update", "Install a software update", "iPhone", T, "en", False, "pilot-011"),
    ("email_attach", "Attach a photo to an email", "Gmail (computer)", C, "en", False, "pilot-012"),
    ("backup_photos", "Back up photos", "iPhone (iCloud Photos)", T, "en", False, "pilot-013"),
    ("family_emergency_scam", "Caller claims to be grandchild needing gift cards", "any", O, "en", True, "pilot-014"),
    ("verification_code_scam", "Stranger asks for a verification code", "any", O, "en", True, "pilot-015"),
    ("online_payment_safety", "Is it safe to pay online?", "any", O, "en", True, "pilot-016"),
    ("social_media_privacy", "Stop strangers seeing Facebook posts", "Facebook", C, "en", True, "pilot-017"),
    ("send_photo_chat", "Send a photo in LINE", "LINE", C, "zh-TW", False, "pilot-018"),
    ("package_text_scam", "Package delivery text with a link", "any", O, "zh-TW", True, "pilot-019"),
    ("add_contact", "Add grandchild as a LINE friend", "LINE", C, "zh-TW", False, "pilot-020"),
    # ---- new tasks ----
    ("text_size", "Make text bigger", "iPhone", T, "en", False, ""),
    ("text_size", "Make text bigger", "Android (Pixel)", T, "en", False, ""),
    ("text_size", "Make chat text bigger in LINE", "LINE", C, "zh-TW", False, ""),
    ("ring_volume", "Turn up ringer volume", "iPhone", T, "en", False, ""),
    ("ring_volume", "Turn up ring volume", "Android", T, "en", False, ""),
    ("wifi_calling", "Turn on Wi-Fi Calling", "iPhone", C, "en", False, ""),
    ("screenshot", "Take a screenshot", "Android", T, "en", False, ""),
    ("screenshot", "Take a screenshot", "Windows 11", T, "en", False, ""),
    ("add_contact", "Add a LINE friend with a QR code", "LINE", C, "zh-TW", False, ""),
    ("wifi_connect", "Connect to a Wi-Fi network", "Android", T, "en", False, ""),
    ("wifi_connect", "Connect to a Wi-Fi network", "Windows 11", T, "en", False, ""),
    ("app_notifications_off", "Turn off notifications for a LINE chat", "LINE", C, "zh-TW", False, ""),
    ("software_update", "Install a software update", "Android", T, "en", False, ""),
    ("software_update", "Install Windows updates", "Windows 11", T, "en", False, ""),
    ("backup_photos", "Back up photos", "Android (Google Photos)", T, "en", False, ""),
    ("add_printer", "Add a printer", "Windows 11", T, "en", False, ""),
    ("email_attach", "Attach a photo to an email", "Gmail app (phone)", C, "en", False, ""),
    ("account_password_reset", "Reset forgotten Google Account password", "Google Account", O, "en", True, ""),
    ("family_emergency_scam", "Call that sounds like a family member's voice asking for money", "any", O, "en", True, ""),
    ("package_text_scam", "Text says package could not be delivered", "any", O, "en", True, ""),
    ("gift_card_scam", "Someone asks to be paid with gift cards", "any", O, "en", True, ""),
    ("family_sharing", "Set up Family Sharing", "iPhone", T, "en", False, ""),
    ("add_contact", "Add a contact", "Android", C, "en", False, ""),
    ("add_contact", "Add a LINE friend by phone number", "LINE", C, "zh-TW", False, ""),
    ("block_number", "Block a phone number", "iPhone", C, "en", False, ""),
    ("block_number", "Block a phone number", "Android", C, "en", False, ""),
    ("block_number", "Block someone in LINE", "LINE", C, "zh-TW", False, ""),
    ("silence_unknown_callers", "Silence calls from unknown numbers", "iPhone", C, "en", False, ""),
    ("spam_call_filter", "Filter spam calls", "Android (Pixel)", C, "en", False, ""),
    ("battery_health", "Check battery health", "iPhone", T, "en", False, ""),
    ("group_text", "Start a group text", "iPhone", C, "en", False, ""),
    ("browser_zoom", "Make every web page bigger by default", "Chrome (computer)", T, "en", False, ""),
    ("group_text", "Create a LINE group", "LINE", C, "zh-TW", False, ""),
    ("share_location", "Share location with family", "iPhone (Find My)", C, "en", True, ""),
    ("share_location", "Share location with family", "Android (Google Maps)", C, "en", True, ""),
    ("install_app", "Install an app", "iPhone", T, "en", False, ""),
    ("install_app", "Install an app", "Android", T, "en", False, ""),
    ("delete_app", "Delete an app", "iPhone", T, "en", False, ""),
    ("delete_app", "Delete an app", "Android", T, "en", False, ""),
    ("delete_app", "Uninstall a program", "Windows 11", T, "en", False, ""),
    ("free_storage", "Free up storage space", "iPhone", T, "en", False, ""),
    ("free_storage", "Free up storage space", "Android", T, "en", False, ""),
    ("flashlight", "Turn on the flashlight", "iPhone", T, "en", False, ""),
    ("flashlight", "Turn on the flashlight", "Android", T, "en", False, ""),
    ("account_security", "Protect a LINE account from being stolen", "LINE", O, "zh-TW", True, ""),
    ("alarm", "Set an alarm", "iPhone", T, "en", False, ""),
    ("alarm", "Set an alarm", "Android (Clock)", T, "en", False, ""),
    ("hearing_bluetooth", "Pair hearing aids or Bluetooth headphones", "iPhone", T, "en", False, ""),
    ("hearing_bluetooth", "Pair Bluetooth headphones", "Android", T, "en", False, ""),
    ("battery_saver", "Turn on battery saving mode", "iPhone", T, "en", False, ""),
    ("battery_saver", "Turn on battery saving mode", "Android", T, "en", False, ""),
    ("software_update", "Update apps", "iPhone (App Store)", T, "en", False, ""),
    ("magnifier", "Zoom in on the screen", "Android", T, "en", False, ""),
    ("find_lost_phone", "Find a lost phone", "iPhone (Find My)", T, "en", True, ""),
    ("find_lost_phone", "Find a lost phone", "Android", T, "en", True, ""),
    ("scan_qr", "Scan a QR code", "iPhone", T, "en", False, ""),
    ("scan_qr", "Scan a QR code", "Android", T, "en", False, ""),
    ("emergency_info", "Set up emergency medical info", "iPhone (Medical ID)", T, "en", True, ""),
    ("emergency_info", "Add emergency information", "Android", T, "en", True, ""),
    ("app_notifications_off", "Turn off notifications from an app", "iPhone", T, "en", False, ""),
    ("app_notifications_off", "Turn off notifications from an app", "Android", T, "en", False, ""),
    ("browser_zoom", "Make a web page bigger", "Chrome (computer)", T, "en", False, ""),
    ("find_downloads", "Find a downloaded file", "Windows 11", T, "en", False, ""),
    ("mouse_pointer_size", "Make the mouse pointer bigger", "Windows 11", T, "en", False, ""),
    ("two_step_verification", "Turn on 2-Step Verification", "Google Account", O, "en", True, ""),
    ("phishing_email", "Is this email asking me to log in real?", "email", O, "en", True, ""),
    ("report_spam_text", "Report a spam text message", "phone", O, "en", True, ""),
    ("romance_scam", "Online friend asks for money", "any", O, "en", True, ""),
    ("government_impersonation", "Caller claims to be from Social Security", "phone", O, "en", True, ""),
    ("strong_passwords", "Make a strong password", "any", O, "en", True, ""),
    ("maps_directions", "Get directions", "Google Maps (phone)", O, "en", False, ""),
    ("report_scam", "Check whether a LINE ID or website is a known scam", "165", O, "zh-TW", True, ""),
    ("join_video_meeting", "Join a Zoom meeting from a link", "Zoom", C, "en", False, ""),
    ("video_captions", "Turn on captions", "YouTube", T, "en", False, ""),
    ("backup_phone", "Back up the whole phone", "iPhone (iCloud Backup)", T, "en", False, ""),
    ("stolen_device_protection", "Turn on Stolen Device Protection", "iPhone", T, "en", True, ""),
    ("live_captions", "Turn on live captions", "Android", T, "en", False, ""),
    ("text_size", "Make text bigger", "Windows 11", T, "en", False, ""),
    ("phone_not_charging", "iPhone stops charging at 80%", "iPhone", T, "en", False, ""),
    ("voice_message", "Send a voice message in LINE", "LINE", C, "zh-TW", False, ""),
    ("ring_volume", "Phone only vibrates, does not ring", "iPhone", T, "en", False, ""),
    ("read_aloud", "Have the phone read the screen aloud", "Android", T, "en", False, ""),
    ("reminders", "Set a reminder", "iPhone", T, "en", False, ""),
    ("bookmark_site", "Bookmark a website", "Chrome (computer)", T, "en", False, ""),
    ("unsubscribe_email", "Unsubscribe from emails", "Gmail", C, "en", False, ""),
    ("recover_deleted_email", "Get back a deleted email", "Gmail", C, "en", False, ""),
    ("mark_spam_email", "Mark an email as spam", "Gmail", C, "en", True, ""),
    ("rotation_lock", "Stop the screen from turning sideways", "iPhone", T, "en", False, ""),
    ("rotation_lock", "Stop the screen from turning sideways", "Android", T, "en", False, ""),
    ("force_restart", "Restart a frozen iPhone", "iPhone", T, "en", False, ""),
    ("phone_not_charging", "Phone is not charging", "iPhone", T, "en", False, ""),
    ("impersonation_borrow_money", "Friend's LINE account asks to borrow money", "LINE", O, "zh-TW", True, ""),
    ("investment_scam", "Investment group promises high returns", "any", O, "zh-TW", True, ""),
    ("online_shopping_scam", "Cheap item from an online seller", "any", O, "zh-TW", True, ""),
    ("government_impersonation", "Caller claims to be police or prosecutor", "phone", O, "zh-TW", True, ""),
    ("report_scam", "Report a scam", "any", O, "zh-TW", True, ""),
]

# Eval: task types that never appear in TRAIN. Platform is a suggestion;
# the Evaluation Lead writes the actual scenarios (with notes_for_raters).
EVAL = [
    ("video_call", "Make a video call", "iPhone (FaceTime)", C, "en", False),
    ("video_call", "Make a video call", "Android (Google Meet)", C, "en", False),
    ("video_call", "Make a video call", "WhatsApp", C, "en", False),
    ("video_call", "Make a LINE video call", "LINE", C, "zh-TW", False),
    ("tech_support_scam", "Caller says computer has a virus", "phone", O, "en", True),
    ("tech_support_scam", "Pop-up says computer is infected, call a number", "computer", O, "en", True),
    ("bill_payment", "Pay a utility bill online", "unknown", O, "en", True),
    ("bill_payment", "Pay the electricity bill with a phone", "unknown", O, "zh-TW", True),
    ("dark_mode", "Turn on dark mode", "iPhone", T, "en", False),
    ("dark_mode", "Turn on dark mode", "Android", T, "en", False),
    ("dark_mode", "Turn on dark mode", "iPhone", T, "zh-TW", False),
    ("wallpaper", "Change the wallpaper", "iPhone", T, "en", False),
    ("wallpaper", "Change the wallpaper", "Android", T, "en", False),
    ("do_not_disturb", "Turn on Do Not Disturb", "iPhone", T, "en", False),
    ("do_not_disturb", "Turn on Do Not Disturb", "Android", T, "en", False),
    ("ringtone_change", "Change the ringtone", "iPhone", T, "en", False),
    ("ringtone_change", "Change the ringtone", "Android", T, "en", False),
    ("transfer_photos_computer", "Move photos from phone to computer", "iPhone to Windows", T, "en", False),
    ("transfer_photos_computer", "Move photos from phone to computer", "Android to Windows", T, "en", False),
    ("print_from_phone", "Print from a phone", "iPhone", T, "en", False),
    ("print_from_phone", "Print from a phone", "Android", T, "en", False),
    ("email_forward", "Forward an email", "Gmail (computer)", C, "en", False),
    ("email_forward", "Forward an email", "Gmail app (phone)", C, "en", False),
    ("email_cc", "Send one email to several people", "Gmail (computer)", C, "en", False),
    ("email_cc", "Reply to everyone on an email", "Outlook", C, "en", False),
    ("email_signature", "Add a signature to emails", "Gmail", C, "en", False),
    ("calendar_event", "Add an appointment to the calendar", "iPhone (Calendar)", T, "en", False),
    ("calendar_event", "Add an appointment to the calendar", "Google Calendar", T, "en", False),
    ("calendar_event", "Add an appointment to the calendar", "iPhone", T, "zh-TW", False),
    ("telehealth_visit", "Join a video doctor's appointment from a link", "unknown", C, "en", True),
    ("ride_hail", "Request a ride", "Uber", O, "en", True),
    ("ride_hail", "Call a taxi with an app", "Taiwan taxi app", O, "zh-TW", True),
    ("grocery_delivery", "Order groceries for delivery", "unknown", O, "en", True),
    ("mobile_check_deposit", "Deposit a check with a phone", "bank app", O, "en", True),
    ("p2p_payment", "Send money to a family member", "Zelle", O, "en", True),
    ("p2p_payment_scam", "Stranger sent money by mistake and asks for it back", "payment app", O, "en", True),
    ("medicare_scam", "Caller offers a new Medicare card", "phone", O, "en", True),
    ("prize_scam", "Message says I won a prize but must pay a fee", "any", O, "en", True),
    ("prize_scam", "Message says I won a prize", "any", O, "zh-TW", True),
    ("charity_scam", "Caller asks for a donation after a disaster", "phone", O, "en", True),
    ("utility_shutoff_scam", "Caller says power will be shut off today", "phone", O, "en", True),
    ("company_impersonation", "Call about a suspicious Amazon order", "phone", O, "en", True),
    ("subscription_renewal_scam", "Email about an antivirus renewal charge", "email", O, "en", True),
    ("installment_cancel_scam", "Caller says an online order was set to installments by mistake", "phone", O, "zh-TW", True),
    ("telecom_impersonation", "Caller claims to be phone company customer service", "phone", O, "zh-TW", True),
    ("bank_impersonation", "Caller claims to be the bank fraud department", "phone", O, "zh-TW", True),
    ("dictation", "Type by talking instead of typing", "iPhone", T, "en", False),
    ("dictation", "Type by talking instead of typing", "Android (Gboard)", T, "en", False),
    ("dictation", "Use voice input", "Android", T, "zh-TW", False),
    ("voice_assistant", "Call someone with Siri", "iPhone", C, "en", False),
    ("voice_assistant", "Ask Google Assistant to call someone", "Android", C, "en", False),
    ("emoji", "Send an emoji", "iPhone", C, "en", False),
    ("emoji", "Send an emoji", "Android", C, "en", False),
    ("autocorrect", "Turn off autocorrect", "iPhone", T, "en", False),
    ("take_video", "Record a video", "iPhone", T, "en", False),
    ("take_video", "Record a video", "Android", T, "en", False),
    ("take_video", "Take a photo or video", "Android", T, "zh-TW", False),
    ("recover_deleted_photos", "Get back a deleted photo", "iPhone", T, "en", False),
    ("recover_deleted_photos", "Get back a deleted photo", "Google Photos", T, "en", False),
    ("recover_deleted_photos", "Get back a deleted photo", "iPhone", T, "zh-TW", False),
    ("nearby_share", "Share a photo with a nearby phone", "iPhone (AirDrop)", C, "en", False),
    ("nearby_share", "Share a photo with a nearby phone", "Android (Quick Share)", C, "en", False),
    ("cast_to_tv", "Show a phone video on the TV", "YouTube (Chromecast)", T, "en", False),
    ("cast_to_tv", "Show iPhone screen on the TV", "AirPlay", T, "en", False),
    ("smart_tv_app", "Open YouTube on the TV", "unknown", T, "en", False),
    ("cancel_subscription", "Cancel a subscription", "iPhone", O, "en", True),
    ("cancel_subscription", "Cancel a subscription", "Google Play", O, "en", True),
    ("change_wifi_password", "Change the Wi-Fi password", "unknown router", T, "en", True),
    ("computer_restart", "Restart or shut down the computer", "Windows 11", T, "en", False),
    ("pin_taskbar", "Keep an app on the taskbar", "Windows 11", T, "en", False),
    ("high_contrast", "Turn on high contrast colors", "Windows 11", T, "en", False),
    ("no_sound", "Computer has no sound", "Windows 11", T, "en", False),
    ("webcam_not_working", "Camera not working on the computer", "Windows 11", T, "en", False),
    ("force_quit_app", "Close an app that's stuck", "Mac", T, "en", False),
    ("find_file_search", "Find a file by searching", "Mac (Spotlight)", T, "en", False),
    ("find_file_search", "Find a file by searching", "Windows 11", T, "en", False),
    ("night_light", "Make the screen easier on the eyes at night", "iPhone (Night Shift)", T, "en", False),
    ("night_light", "Make the screen easier on the eyes at night", "Android", T, "en", False),
    ("favorite_contacts", "Add a contact to favorites", "iPhone", C, "en", False),
    ("favorite_contacts", "Add a contact to favorites", "Android", C, "en", False),
    ("screen_timeout", "Keep the screen on longer", "iPhone", T, "en", False),
    ("screen_timeout", "Keep the screen on longer", "Android", T, "en", False),
    ("screen_lock_change", "Change the phone passcode", "iPhone", T, "en", True),
    ("screen_lock_change", "Change the screen lock", "Android", T, "en", True),
    ("airplane_mode", "Turn on airplane mode", "iPhone", T, "en", False),
    ("airplane_mode", "Turn on airplane mode", "Android", T, "en", False),
    ("airplane_mode", "Turn on airplane mode", "Android", T, "zh-TW", False),
    ("hotspot", "Share phone internet with a laptop", "iPhone", T, "en", False),
    ("hotspot", "Share phone internet with a laptop", "Android", T, "en", False),
    ("browser_history", "Find a website visited earlier", "Chrome (computer)", T, "en", False),
    ("clear_browser_data", "Clear browsing data", "Chrome (computer)", T, "en", True),
    ("open_pdf", "Open a PDF attachment", "phone", T, "en", False),
    ("meeting_controls", "Mute and unmute in a Zoom meeting", "Zoom", C, "en", False),
    ("youtube_search", "Find and play a video", "YouTube app", T, "en", False),
    ("library_ebooks", "Borrow an e-book from the library", "Libby", O, "en", False),
    ("weather_app", "Check the weather for another city", "unknown", T, "en", False),
    ("unsend_message", "Unsend a LINE message", "LINE", C, "zh-TW", False),
    ("photo_album_share", "Share a LINE album with family", "LINE", C, "zh-TW", False),
    ("pin_chat", "Pin a chat to the top", "LINE", C, "zh-TW", False),
    ("train_ticket", "Book a high-speed rail ticket", "THSR app", O, "zh-TW", True),
    ("health_records_app", "Check recent clinic visits in the NHI app", "NHI Express", O, "zh-TW", True),
    ("mobile_payment_link", "Link a card to mobile payment", "unknown", O, "zh-TW", True),
    ("micropayment_off", "Turn off carrier micropayments", "telecom", O, "zh-TW", True),
    ("camera_translate", "Translate a sign with the camera", "Google Translate", T, "zh-TW", False),
    ("job_scam", "Online job offer asks for a deposit", "any", O, "zh-TW", True),
    ("translate_text", "Translate a message into English", "Google Translate", T, "en", False),
    ("contact_photo", "Add a photo to a contact", "iPhone", C, "en", False),
    ("keyboard_vibration", "Turn off keyboard sounds", "iPhone", T, "en", False),
    ("keyboard_vibration", "Turn off keyboard sounds", "Android (Gboard)", T, "en", False),
    ("cellular_data", "Turn off mobile data for an app", "iPhone", T, "en", False),
    ("contact_share", "Send someone's contact card", "iPhone", C, "en", False),
    ("message_search", "Find an old text message", "iPhone", C, "en", False),
    ("message_search", "Find an old text message", "Android (Google Messages)", C, "en", False),
    ("delete_messages", "Delete a text conversation", "iPhone", C, "en", False),
    ("delete_messages", "Delete a text conversation", "Android (Google Messages)", C, "en", False),
    ("call_history", "See missed calls", "iPhone", C, "en", False),
    ("call_history", "See missed calls", "Android", C, "en", False),
    ("speakerphone", "Put a call on speaker", "iPhone", C, "en", False),
    ("speakerphone", "Put a call on speaker", "Android", C, "en", False),
    ("speakerphone", "Put a call on speaker", "iPhone", C, "zh-TW", False),
    ("conference_call", "Add a second person to a call", "iPhone", C, "en", False),
    ("photo_edit_crop", "Crop a photo", "iPhone", T, "en", False),
    ("photo_edit_crop", "Crop a photo", "Google Photos", T, "en", False),
    ("photo_album", "Make a photo album", "iPhone", T, "en", False),
    ("qr_payment_scam", "QR code on a parking meter asks for payment", "any", O, "en", True),
    ("fake_shopping_site", "Website with prices that seem too good", "any", O, "en", True),
    ("account_hacked", "Email account seems hacked", "email", O, "en", True),
    ("health_product_scam", "Ad says a health product cures illness", "any", O, "zh-TW", True),
    ("social_friend_request", "Friend request from someone already a friend", "Facebook", O, "en", True),
    ("data_breach_notice", "Letter says my information was in a data breach", "any", O, "en", True),
    ("credit_freeze", "Freeze credit", "credit bureaus", O, "en", True),
    ("robocall_register", "Stop telemarketing calls", "phone", O, "en", False),
    ("own_phone_number", "Find my own phone number", "iPhone", C, "en", False),
    ("email_new_account", "Create an email account", "Gmail", O, "en", True),
    ("video_call", "Make a group video call", "iPhone (FaceTime)", C, "en", False),
    ("meeting_controls", "Turn on the camera in a Zoom meeting", "Zoom", C, "en", False),
    ("app_permissions", "Stop an app from using my location", "iPhone", T, "en", True),
    ("voice_memo", "Record a voice memo", "iPhone", T, "en", False),
    ("new_phone_transfer", "Move everything to a new phone", "iPhone to iPhone", T, "en", False),
    ("new_phone_transfer", "Move everything to a new phone", "Android to Android", T, "en", False),
    ("restart_router", "Restart the internet router", "unknown", T, "en", False),
    ("smart_speaker", "Set a timer with a smart speaker", "unknown", T, "en", False),
    ("e_ticket_wallet", "Add a boarding pass to the phone wallet", "iPhone (Wallet)", O, "en", False),
    ("pharmacy_app", "Refill a prescription in a pharmacy app", "unknown", O, "en", True),
    ("patient_portal", "Message the doctor through a patient portal", "unknown", O, "en", True),
    ("video_doorbell", "See who is at the door on the phone", "unknown", T, "en", True),
    ("hearing_live_listen", "Use the iPhone as a microphone for hearing", "iPhone (Live Listen)", T, "en", False),
    ("emergency_sos", "Call emergency services quickly", "iPhone", T, "en", True),
    ("emergency_sos", "Call emergency services quickly", "Android", T, "en", True),
    ("fall_detection", "Turn on fall detection", "Apple Watch", T, "en", True),
]


def main():
    train_types = {t[0] for t in TRAIN}
    eval_types = {t[0] for t in EVAL}
    overlap = train_types & eval_types
    assert not overlap, f"Task types in both splits: {sorted(overlap)}"

    out_train = REPO / "data/tasks/train_tasks.csv"
    out_eval = REPO / "eval/tasks/eval_tasks.csv"
    out_train.parent.mkdir(parents=True, exist_ok=True)
    out_eval.parent.mkdir(parents=True, exist_ok=True)

    with open(out_train, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["task_id", "task_type", "task", "platform", "category", "language", "sensitive", "pilot_example"])
        for i, (ty, task, plat, cat, lang, sens, pilot) in enumerate(TRAIN, start=1):
            w.writerow([f"TR-{i:03d}", ty, task, plat, cat, lang, sens, pilot])

    with open(out_eval, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["task_id", "task_type", "task", "platform", "category", "language", "sensitive"])
        for i, row in enumerate(EVAL, start=1):
            w.writerow([f"EV-{i:03d}", *row])

    for name, rows in (("train", TRAIN), ("eval", EVAL)):
        n = len(rows)
        langs = Counter(r[4] for r in rows)
        cats = Counter(r[3] for r in rows)
        sens = sum(r[5] for r in rows)
        types = len({r[0] for r in rows})
        print(f"{name}: {n} tasks, {types} types, zh-TW {langs['zh-TW']} ({langs['zh-TW']/n:.0%}), "
              f"sensitive {sens}, categories {dict(cats)}")
    print("No task type appears in both splits.")


if __name__ == "__main__":
    main()
