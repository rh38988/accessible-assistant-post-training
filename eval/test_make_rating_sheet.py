"""CPU-only checks for blinded rating artifacts; never score or generate replies.

Run: .\.venv\Scripts\python.exe -B -m unittest discover -s eval -p "test_*.py" -v
"""
import copy
import csv
import hashlib
import io
import json
import random
import tempfile
import unittest
import zipfile
from collections import Counter
from pathlib import Path
from unittest.mock import patch

from openpyxl import load_workbook

from eval import make_rating_sheet as rating


class RatingSheetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenario_path = rating.REPO / "eval/scenarios/eval_v1.jsonl"
        cls.outputs_dir = rating.REPO / "eval/outputs"
        cls.scenarios = rating.load_scenarios(cls.scenario_path)
        cls.outputs = rating.load_outputs(cls.outputs_dir)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def generate(self, name="ratings", seed=42):
        return rating.generate(self.scenario_path, self.outputs_dir, self.root / name, seed)

    def workbook(self, path):
        wb = load_workbook(path)
        self.addCleanup(wb.close)
        return wb

    def test_45_rows_identical_raters_and_matching_private_key_ids(self):
        first, second, key_path = self.generate()
        self.assertTrue(first.read_bytes() == second.read_bytes())
        wb = self.workbook(first)
        ws = wb["Ratings"]
        self.assertEqual(ws.max_row - 1, 45)
        self.assertEqual(tuple(c.value for c in ws[1]), rating.HEADERS)
        items = [dict(zip(rating.HEADERS, row)) for row in ws.iter_rows(min_row=2, values_only=True)]
        with key_path.open(encoding="utf-8", newline="") as stream:
            key = list(csv.DictReader(stream))
        self.assertEqual(len(key), 45)
        self.assertEqual(len({r["item_id"] for r in items}), 45)
        self.assertTrue({r["item_id"] for r in items} == {r["item_id"] for r in key})
        self.assertEqual(Counter(r["scenario_id"] for r in items),
                         Counter({s["id"]: 3 for s in self.scenarios}))
        lookup = {r["item_id"]: r for r in key}
        scenarios = {s["id"]: s for s in self.scenarios}
        outputs = {c: {r["scenario_id"]: r for r in rows} for c, rows in self.outputs.items()}
        for item in items:
            private = lookup[item["item_id"]]
            self.assertTrue(item["scenario_id"] == private["scenario_id"])
            self.assertTrue(item["candidate"] == private["candidate"])
            # Boolean assertions keep private mappings out of failure output.
            expected = outputs[private["condition"]][item["scenario_id"]]["response"]
            self.assertTrue(item["response"] == expected)
            sc = scenarios[item["scenario_id"]]
            self.assertEqual(item["prompt"], "\n\n".join(
                f"{t['role'].upper()}: {t['content']}" for t in sc["prompt"]))
            for field in ("clarification_required", "risk_level", "source_url", "task_family"):
                self.assertEqual(item[field], sc[field])
            self.assertEqual(item["expected_elements"], "\n".join(sc["expected_elements"]))
            self.assertEqual(item["word_count"], len(item["response"].split()))
            self.assertTrue(all(item[field] is None for field in (*rating.SCORES, *rating.CHECKS, "notes")))
        for sc in self.scenarios:
            group = [row for row in key if row["scenario_id"] == sc["id"]]
            self.assertTrue({r["candidate"] for r in group} == set(rating.CANDIDATES))
            self.assertTrue({r["condition"] for r in group} == set(rating.CONDITIONS))

    def test_seed_42_is_deterministic_independent_per_scenario_and_shuffles_rows(self):
        first, key = rating.build_items(self.scenarios, self.outputs)
        again, again_key = rating.build_items(self.scenarios, self.outputs, 42)
        self.assertTrue(first == again and key == again_key)
        reversed_outputs = {c: list(reversed(rows)) for c, rows in self.outputs.items()}
        reordered, reordered_key = rating.build_items(list(reversed(self.scenarios)), reversed_outputs, 42)
        self.assertTrue(first == reordered and key == reordered_key)
        changed, changed_key = rating.build_items(self.scenarios, self.outputs, 43)
        self.assertTrue(first != changed and key != changed_key)
        rng = random.Random(42)
        expected = []
        permutations = set()
        for sc in sorted(self.scenarios, key=lambda sc: sc["id"]):
            conditions = list(rating.CONDITIONS)
            rng.shuffle(conditions)
            permutations.add(tuple(conditions))
            expected.extend((sc["id"], label, condition)
                            for label, condition in zip(rating.CANDIDATES, conditions))
        self.assertTrue([(k["scenario_id"], k["candidate"], k["condition"]) for k in key] == expected)
        self.assertGreater(len(permutations), 1)
        ordered_ids = [k["item_id"] for k in key]
        rng.shuffle(ordered_ids)
        self.assertEqual([item["item_id"] for item in first], ordered_ids)
        self.assertTrue(ordered_ids != [k["item_id"] for k in key])
        a = self.workbook(self.generate("first")[0])
        b = self.workbook(self.generate("second")[0])
        self.assertTrue(list(a["Ratings"].values) == list(b["Ratings"].values))

    def test_no_condition_leakage_in_cells_metadata_or_hidden_parts(self):
        outputs = copy.deepcopy(self.outputs)
        for rows in outputs.values():
            for row in rows:
                row["adapter"] = "PRIVATE_ADAPTER_METADATA_DO_NOT_EXPORT"
                row["response"] = "A candidate answer without identity metadata."
        items, _ = rating.build_items(self.scenarios, outputs)
        wb = rating.make_workbook(items, rating.REPO / "eval/rubric_v1.md")
        path = self.root / "anonymous.xlsx"
        wb.save(path)
        wb.close()
        loaded = self.workbook(path)
        self.assertEqual(loaded.sheetnames, ["Ratings", "Rubric"])
        self.assertFalse(loaded.defined_names)
        self.assertFalse(loaded.properties.creator)
        self.assertFalse(loaded.properties.lastModifiedBy)
        for ws in loaded:
            self.assertEqual(ws.sheet_state, "visible")
            for row in ws:
                for cell in row:
                    self.assertIsNone(cell.comment)
                    self.assertIsNone(cell.hyperlink)
                    self.assertNotEqual(cell.data_type, "f")
        self.assertTrue(all(set(item) == set(rating.HEADERS) for item in items))
        self.assertFalse(set(rating.HEADERS) & {"condition", "adapter", "model", "output_file"})
        with zipfile.ZipFile(path) as archive:
            for name in archive.namelist():
                data = archive.read(name)
                for marker in (b"PRIVATE_ADAPTER_METADATA", b"eval_v1-original.jsonl",
                               b"eval_v1-prompt.jsonl", b"eval_v1-sft.jsonl", b"key.csv"):
                    self.assertNotIn(marker, data)
                self.assertNotIn("hidden", name.lower())

    def test_exact_rubric_and_score_check_choices_and_applicability(self):
        first, _, _ = self.generate()
        wb = self.workbook(first)
        expected = (rating.REPO / "eval/rubric_v1.md").read_text(encoding="utf-8").splitlines()
        actual = [row[0] or "" for row in wb["Rubric"].iter_rows(values_only=True)]
        self.assertEqual(actual[:len(expected)], expected)
        ws = wb["Ratings"]
        validations = ws.data_validations.dataValidation
        self.assertEqual(len(validations), 7)
        for field, formula in [(f, '"0,1,2,NA"') for f in rating.SCORES] + [
            ("clarification_behavior", '"appropriate,guessed,over-asked"'),
            ("unsafe_advice", '"yes,no"'), ("language_match", '"yes,no"')
        ]:
            col = rating.HEADERS.index(field) + 1
            for row in range(2, 47):
                item = dict(zip(rating.HEADERS, (c.value for c in ws[row])))
                applicable = (field != "unsafe_advice" or item["risk_level"] in {"medium", "high"})
                applicable &= field != "language_match" or item["language"] == "zh-TW"
                rules = [rule for rule in validations if ws.cell(row, col).coordinate in rule]
                self.assertEqual(len(rules), int(applicable))
                if rules:
                    self.assertEqual(rules[0].formula1, formula)
                    self.assertTrue(rules[0].allow_blank)

    def test_rejects_incomplete_duplicate_mismatched_or_empty_outputs(self):
        for case in ("missing", "duplicate", "unknown", "condition", "empty"):
            outputs = copy.deepcopy(self.outputs)
            rows = outputs["original"]
            if case == "missing":
                rows.pop()
            elif case == "duplicate":
                rows[-1] = copy.deepcopy(rows[0])
            elif case == "unknown":
                rows[0]["scenario_id"] = "UNKNOWN"
            elif case == "condition":
                rows[0]["condition"] = "other"
            else:
                rows[0]["response"] = " "
            with self.subTest(case=case), self.assertRaises(ValueError):
                rating.build_items(self.scenarios, outputs)

    def test_only_three_named_files_are_read(self):
        directory = self.root / "outputs"
        directory.mkdir()
        for condition, rows in self.outputs.items():
            (directory / f"eval_v1-{condition}.jsonl").write_text(
                "\n".join(json.dumps(row) for row in rows), encoding="utf-8")
        (directory / "unrelated.jsonl").write_text("not JSON", encoding="utf-8")
        self.assertTrue(rating.load_outputs(directory) == self.outputs)

    def test_inputs_unchanged_existing_ratings_protected_and_cli_keeps_key_private(self):
        sources = [self.scenario_path, rating.REPO / "eval/rubric_v1.md"] + [
            self.outputs_dir / f"eval_v1-{condition}.jsonl" for condition in rating.CONDITIONS]
        before = {path: hashlib.sha256(path.read_bytes()).digest() for path in sources}
        with patch("sys.stdout", new_callable=io.StringIO) as stdout:
            rating.main(["--ratings-dir", str(self.root / "cli"), "--seed", "42"])
        self.assertNotIn("original", stdout.getvalue())
        self.assertNotIn("sft", stdout.getvalue())
        self.assertTrue(before == {path: hashlib.sha256(path.read_bytes()).digest() for path in sources})
        artifacts = [self.root / "cli" / name for name in rating.FILENAMES]
        hashes = [hashlib.sha256(path.read_bytes()).digest() for path in artifacts]
        with self.assertRaises(ValueError):
            self.generate("cli")
        self.assertTrue(hashes == [hashlib.sha256(path.read_bytes()).digest() for path in artifacts])

    def test_formula_like_response_is_preserved_as_text(self):
        items, _ = rating.build_items(self.scenarios, self.outputs)
        items[0]["response"] = '=HYPERLINK("https://example.invalid", "text")'
        wb = rating.make_workbook(items, rating.REPO / "eval/rubric_v1.md")
        path = self.root / "literal.xlsx"
        wb.save(path)
        wb.close()
        loaded = self.workbook(path)
        cell = loaded["Ratings"].cell(2, rating.HEADERS.index("response") + 1)
        self.assertEqual(cell.value, items[0]["response"])
        self.assertEqual(cell.data_type, "s")


if __name__ == "__main__":
    unittest.main()
