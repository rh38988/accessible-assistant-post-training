"""Tests for v7 composition with a fake model (no GPU).

    python -m unittest eval/v7/test_grounded_steps.py -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grounded_steps as g  # noqa: E402

HOTSPOT = {
    "decision": {"mode": "answer", "question": ""},
    "action_plan": {"selected_document_ids": ["apple-hotspot"], "actions": [
        {"key": "hotspot_enable", "instruction": "On the iPhone, enable Personal Hotspot > Allow Others to Join.",
         "source_quote": "On the supplying iPhone open Settings > Personal Hotspot, then enable Allow Others to Join."},
        {"key": "hotspot_password", "instruction": "Enter the password displayed on the iPhone.",
         "source_quote": "On the computer choose the phone hotspot and enter the password displayed on the phone."}]},
    "evidence": [{"document_id": "apple-hotspot", "text": "Keep that screen open. A blue checkmark appears when connected."},
                 {"document_id": "apple-wifi", "text": "A blue checkmark by the network confirm connection."}],
}
REQ = "How can I use my iPhone's internet on my laptop?"


def fake(replies):
    it = iter(replies)
    return lambda messages, n: next(it)


class V7(unittest.TestCase):
    def test_clarify_is_verbatim_and_makes_no_call(self):
        row = {"decision": {"mode": "clarify", "question": "Is your phone an iPhone or an Android phone?"}}
        resp, chk = g.build_answer(row, "help", lambda m, n: self.fail("no call expected"), [])
        self.assertEqual(resp, "Is your phone an iPhone or an Android phone?")
        self.assertEqual(chk["calls"], 0)

    def test_every_action_becomes_one_numbered_step(self):
        gen = fake(["Yes, you can share it.",
                    "1. On your iPhone, open Settings, tap Personal Hotspot, and turn on Allow Others to Join.",
                    "On the laptop, type the password shown on your iPhone.",
                    "You'll see a blue checkmark when it's connected."])
        resp, chk = g.build_answer(HOTSPOT, REQ, gen, [])
        self.assertIn("1. On your iPhone", resp)
        self.assertIn("2. On the laptop, type the password", resp)
        self.assertIn("blue checkmark", resp)
        self.assertTrue(resp.endswith(g.CLOSING["en"]))
        self.assertEqual(chk["fallbacks"], 0)

    def test_invented_url_or_dropped_label_falls_back_to_plan_text(self):
        gen = fake(["Sure.", "Go to findiphone.apple.com/hotspot and turn it on.",
                    "Type the password.", "Done."])
        resp, chk = g.build_answer(HOTSPOT, REQ, gen, [])
        self.assertNotIn("findiphone", resp)
        self.assertIn("1. On the iPhone, enable Personal Hotspot > Allow Others to Join.", resp)
        self.assertEqual(chk["steps"][0]["used"], "fallback")
        self.assertEqual(chk["steps"][1]["used"], "model")

    def test_chinese_uses_traditional_and_source_fallback(self):
        row = {"decision": {"mode": "answer"}, "evidence": [],
               "action_plan": {"selected_document_ids": [], "actions": [
                   {"key": "atm_hangup", "instruction": "Hang up on the caller.", "source_quote": "掛斷後自行查詢官方客服電話確認"},
                   {"key": "atm_165", "instruction": "In Taiwan, call 165 for scam advice.", "source_quote": "在臺灣也可撥 165 諮詢"}]}}
        gen = fake(["这是诈骗，请不要照做。", "请马上挂断电话。", "Call 165."])
        resp, chk = g.build_answer(row, "剛剛有人打電話要我到ATM操作，我該怎麼辦？", gen, [])
        self.assertIn("掛斷", resp)                    # Simplified 挂 converted
        self.assertIn("在臺灣也可撥 165 諮詢", resp)    # English step rejected, source sentence used
        self.assertTrue(resp.endswith(g.CLOSING_GENERAL["zh"]))  # phone scam: no on-screen buttons

    def test_no_plan_uses_single_v6_call(self):
        row = {"decision": {"mode": "answer"}, "action_plan": {"actions": []}}
        resp, chk = g.build_answer(row, REQ, lambda m, n: "v6 style answer", [{"role": "user", "content": REQ}])
        self.assertEqual(resp, "v6 style answer")
        self.assertEqual(chk["calls"], 1)

    def test_labels(self):
        self.assertEqual(g.labels("On the iPhone, enable Personal Hotspot > Allow Others to Join."),
                         ["Personal Hotspot", "Allow Others to Join"])
        self.assertEqual(g.labels("If Join Audio appears, choose Call Over Internet."), ["Join Audio", "Call Over Internet"])
        self.assertEqual(g.labels("Check iPad microphone permission for Zoom in Settings."), ["Zoom", "Settings"])
        self.assertEqual(g.labels("Open Settings > Display & Brightness and choose Dark."), ["Settings", "Display & Brightness"])

    def test_repeated_source_sentence_appears_once(self):
        self.assertEqual(g.compose("Hi", ["STEP-X", "STEP-X", "STEP-Y"], "", "en").count("STEP-X"), 1)


if __name__ == "__main__":
    unittest.main()
