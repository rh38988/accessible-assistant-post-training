"""CPU-only regression checks; never load a tokenizer/model or generate replies.

Run: python -B -m unittest discover -s eval -p "test_*.py" -v
"""
import copy
import io
import json
import subprocess
import sys
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch

from eval import generate
from scripts.validate_data import check_record


class GenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = generate.load_jsonl(generate.REPO / "eval/scenarios/eval_v1.jsonl")
        cls.system_prompt = (generate.REPO / "eval/prompts/system_prompt.txt").read_text(
            encoding="utf-8"
        ).strip()

    def args(self, condition, *extra):
        argv = ["--condition", condition, "--dry-run"]
        if condition == "sft":
            argv += ["--adapter", "checkpoints/test-pilot"]
        return generate.parse_args(argv + list(extra))

    def test_native_scenarios_and_multiturn_context_preserved_for_every_condition(self):
        before = copy.deepcopy(self.scenarios)
        self.assertEqual(len(self.scenarios), 15)
        self.assertEqual(
            [s["id"] for s in self.scenarios if len(s["prompt"]) > 1],
            ["EVAL-PHONE-004", "EVAL-SAFE-001"],
        )
        for condition in generate.CONDITIONS:
            for sc in self.scenarios:
                with self.subTest(condition=condition, scenario=sc["id"]):
                    messages = generate.build_messages(sc, condition, self.system_prompt)
                    expected = copy.deepcopy(sc["prompt"])
                    if condition == "prompt":
                        expected.insert(0, {"role": "system", "content": self.system_prompt})
                    self.assertEqual(messages, expected)
                    self.assertTrue(all(set(m) == {"role", "content"} for m in messages))
        self.assertEqual(self.scenarios, before)

    def test_evaluation_metadata_never_changes_model_messages(self):
        scenario = copy.deepcopy(self.scenarios[0])
        changed = copy.deepcopy(scenario)
        for key in changed:
            if key != "prompt":
                changed[key] = "PRIVATE_EVALUATION_METADATA_" + key
        changed["unexpected_metadata"] = "PRIVATE_EVALUATION_METADATA_extra"
        for condition in generate.CONDITIONS:
            with self.subTest(condition=condition):
                actual = generate.build_messages(changed, condition, self.system_prompt)
                self.assertEqual(
                    actual, generate.build_messages(scenario, condition, self.system_prompt)
                )
                self.assertNotIn("PRIVATE_EVALUATION_METADATA", json.dumps(actual))

    def test_built_messages_do_not_alias_dataset(self):
        scenario = copy.deepcopy(self.scenarios[0])
        messages = generate.build_messages(scenario, "original")
        messages[0]["content"] = "changed locally"
        self.assertEqual(scenario, self.scenarios[0])

    def test_only_prompt_condition_reads_accessibility_prompt(self):
        for condition in ("original", "sft"):
            args = self.args(condition, "--system-prompt", "nonexistent-system-prompt.txt")
            built = generate.build_all(args)
            self.assertEqual([sid for sid, _ in built], [s["id"] for s in self.scenarios])
            self.assertEqual([m for _, m in built], [s["prompt"] for s in self.scenarios])
        with self.assertRaises(ValueError):
            generate.build_messages(self.scenarios[0], "prompt", "   ")

    def test_shared_greedy_response_budget(self):
        for condition in generate.CONDITIONS:
            with self.subTest(condition=condition):
                args = self.args(condition)
                self.assertEqual(generate.generation_kwargs(args.max_new_tokens),
                                 {"max_new_tokens": 768, "do_sample": False})
                args = self.args(condition, "--max-new-tokens", "256")
                self.assertEqual(generate.generation_kwargs(args.max_new_tokens),
                                 {"max_new_tokens": 256, "do_sample": False})

    def test_response_jsonl_contract_and_adapter_identity(self):
        for condition in generate.CONDITIONS:
            with self.subTest(condition=condition):
                rows = [generate.response_record(s["id"], condition, "checkpoints/pilot", "reply")
                        for s in self.scenarios]
                decoded = [json.loads(line) for line in "\n".join(
                    json.dumps(row) for row in rows
                ).splitlines()]
                self.assertEqual([r["scenario_id"] for r in decoded],
                                 [s["id"] for s in self.scenarios])
                for row in decoded:
                    self.assertEqual(set(row), {"scenario_id", "condition", "adapter", "response"})
                    self.assertEqual(row["condition"], condition)
                    self.assertEqual(row["adapter"],
                                     "checkpoints/pilot" if condition == "sft" else None)
                    self.assertEqual(row["response"], "reply")

    def test_cli_rejects_ambiguous_adapter_and_invalid_generation_arguments(self):
        invalid = [
            ["--condition", "sft", "--dry-run"],
            ["--condition", "original", "--adapter", "pilot", "--dry-run"],
            ["--condition", "prompt", "--adapter", "pilot", "--dry-run"],
            ["--condition", "original"],
            ["--condition", "original", "--dry-run", "--max-new-tokens", "0"],
        ]
        for argv in invalid:
            with self.subTest(argv=argv), patch("sys.stderr", new_callable=io.StringIO):
                with self.assertRaises(SystemExit) as exc:
                    generate.parse_args(argv)
                self.assertEqual(exc.exception.code, 2)

    def test_dry_run_cli_builds_every_scenario_without_heavy_imports_or_output(self):
        # Fail even if heavy packages are installed: dry-run must never import them.
        bootstrap = """
import builtins, runpy, sys
original_import = builtins.__import__
def guarded_import(name, *args, **kwargs):
    if name.split('.')[0] in {'torch', 'transformers', 'peft', 'retrieval'} or 'schema_v1_adapter' in name:
        raise AssertionError('Forbidden dry-run import: ' + name)
    return original_import(name, *args, **kwargs)
builtins.__import__ = guarded_import
sys.argv = ['eval/generate.py'] + sys.argv[1:]
runpy.run_path('eval/generate.py', run_name='__main__')
"""
        for condition in generate.CONDITIONS:
            out = generate.REPO / "eval/outputs" / ("dry-run-" + uuid.uuid4().hex) / "out.jsonl"
            with self.subTest(condition=condition):
                argv = [sys.executable, "-B", "-c", bootstrap, "--condition", condition,
                        "--dry-run", "--out", str(out), "--max-new-tokens", "768"]
                if condition == "sft":
                    argv += ["--adapter", "checkpoints/test-pilot"]
                result = subprocess.run(argv, cwd=generate.REPO, capture_output=True,
                                        text=True, encoding="utf-8", timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                records = [json.loads(line) for line in result.stdout.splitlines()]
                self.assertEqual([r["scenario_id"] for r in records],
                                 [s["id"] for s in self.scenarios])
                for record, scenario in zip(records, self.scenarios):
                    expected = generate.build_messages(scenario, condition, self.system_prompt)
                    self.assertEqual(record["messages"], expected)
                    self.assertEqual(record["roles"], [m["role"] for m in expected])
                    self.assertEqual(record["message_count"], len(expected))
                    self.assertEqual(record["condition"], condition)
                    self.assertEqual(record["adapter"],
                                     "checkpoints/test-pilot" if condition == "sft" else None)
                    self.assertIs(record["do_sample"], False)
                    self.assertEqual(record["max_new_tokens"], 768)
                    self.assertNotIn("expected_elements", record)
                    self.assertNotIn("source_url", record)
                    self.assertNotIn("risk_level", record)
                self.assertFalse(out.parent.exists())

    def test_dry_run_needs_no_output_argument(self):
        with patch("sys.stdout", new_callable=io.StringIO) as stdout:
            generate.main(["--condition", "original", "--dry-run"])
        self.assertEqual(len(stdout.getvalue().splitlines()), 15)

    def test_loader_rejects_duplicate_ids_and_legacy_turns(self):
        scenario = self.scenarios[0]
        legacy = copy.deepcopy(scenario)
        legacy["turns"] = legacy.pop("prompt")
        cases = [
            (json.dumps(scenario) + "\n" + json.dumps(scenario), "duplicate id"),
            (json.dumps(legacy), "missing fields ['prompt']"),
            ("[]", "record must be a JSON object"),
            ("{invalid", "invalid JSON"),
            ("", "no scenarios"),
        ]
        for text, message in cases:
            with self.subTest(text=text[:40]), patch("builtins.open", return_value=io.StringIO(text)):
                with self.assertRaises(ValueError) as exc:
                    generate.load_jsonl("scenarios.jsonl")
                self.assertIn(message, str(exc.exception))

    def test_schema_v1_rejects_invalid_prompt_and_metadata_shapes(self):
        changes = [
            ("prompt", []),
            ("prompt", [None]),
            ("prompt", [{"role": "system", "content": "metadata"}]),
            ("prompt", [{"role": "user", "content": "hello", "source_url": "metadata"}]),
            ("prompt", [{"role": "user", "content": "hello"},
                        {"role": "assistant", "content": "not a final user turn"}]),
            ("prompt", [{"role": "user", "content": "   "}]),
            ("clarification_required", "false"),
            ("expected_elements", "an answer"),
            ("source_url", "not-a-url"),
            ("risk_level", "unknown"),
            ("id", ""),
        ]
        for field, value in changes:
            with self.subTest(field=field, value=value):
                scenario = copy.deepcopy(self.scenarios[0])
                scenario[field] = value
                errors = []
                check_record(scenario, "scenario", errors, "fixture")
                self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
