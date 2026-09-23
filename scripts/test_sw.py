#!/usr/bin/env python3
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
SW = ROOT / "scripts" / "sw"


class ResearchThreadSelectionTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        root = Path(self.tempdir.name)
        self.bin_dir = root / "bin"
        self.bin_dir.mkdir()
        self.log_path = root / "gh.log"
        self.brief_path = root / "brief.txt"
        self.brief_path.write_text(
            textwrap.dedent(
                """\
                ## Request

                Exercise research intake.

                ## Inputs and sources

                https://example.com/

                ## Context

                Verify explicit research thread selection.

                ## Acceptance criteria

                - The issue is created with the selected milestone.

                ## Constraints and non-goals

                Do not call GitHub.
                """
            ),
            encoding="ascii",
        )
        fake_gh = self.bin_dir / "gh"
        fake_gh.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env python3
                import json
                import os
                import sys

                args = sys.argv[1:]
                with open(os.environ["GH_LOG"], "a", encoding="utf-8") as log:
                    log.write(json.dumps(args) + "\\n")

                if args[:2] == ["repo", "view"]:
                    print("smith-wiki/wiki")
                elif args[:2] == ["pr", "list"]:
                    print("[]")
                elif args[:2] == ["issue", "create"]:
                    print("https://github.com/smith-wiki/wiki/issues/999")
                elif args and args[0] == "api":
                    if "--method" in args and "POST" in args and any(
                        value.endswith("/milestones") for value in args
                    ):
                        print(json.dumps({
                            "number": 42,
                            "title": "Session thread",
                            "html_url": "https://github.com/smith-wiki/wiki/milestone/42",
                        }))
                    elif "repos/smith-wiki/wiki/milestones/42" in args:
                        print(json.dumps({
                            "number": 42,
                            "title": "Session thread",
                            "html_url": "https://github.com/smith-wiki/wiki/milestone/42",
                            "state": "open",
                        }))
                    else:
                        print("unexpected gh api invocation: " + repr(args), file=sys.stderr)
                        raise SystemExit(2)
                else:
                    print("unexpected gh invocation: " + repr(args), file=sys.stderr)
                    raise SystemExit(2)
                """
            ),
            encoding="ascii",
        )
        fake_gh.chmod(fake_gh.stat().st_mode | stat.S_IXUSR)
        self.env = os.environ.copy()
        self.env["PATH"] = f"{self.bin_dir}{os.pathsep}{self.env['PATH']}"
        self.env["GH_LOG"] = str(self.log_path)

    def run_issue(self, *selector):
        return subprocess.run(
            [
                str(SW),
                "issue",
                "--queue",
                "research",
                "SOURCE_BRIEF",
                "thread-contract",
                "Session thread",
                str(self.brief_path),
                *selector,
            ],
            cwd=ROOT,
            env=self.env,
            text=True,
            capture_output=True,
            check=False,
        )

    def gh_calls(self):
        if not self.log_path.exists():
            return []
        return [json.loads(line) for line in self.log_path.read_text().splitlines()]

    def test_thread_selector_is_required(self):
        result = self.run_issue()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("(--new-thread | THREAD)", result.stderr)
        self.assertEqual(self.gh_calls(), [])

    def test_new_thread_creation_is_explicit(self):
        result = self.run_issue("--new-thread")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.gh_calls()
        self.assertTrue(
            any("POST" in call and any(value.endswith("/milestones") for value in call) for call in calls)
        )

    def test_existing_thread_reuse_does_not_create_milestone(self):
        result = self.run_issue("42")

        self.assertEqual(result.returncode, 0, result.stderr)
        calls = self.gh_calls()
        self.assertTrue(any("repos/smith-wiki/wiki/milestones/42" in call for call in calls))
        self.assertFalse(
            any("POST" in call and any(value.endswith("/milestones") for value in call) for call in calls)
        )


if __name__ == "__main__":
    unittest.main()
