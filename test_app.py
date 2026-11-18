import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class CommandTests(unittest.TestCase):
    def test_workflow(self):
        cases = [
          [
            [
              "invoices.csv"
            ],
            0,
            "Records for review: 3"
          ],
          [
            [
              "invoices.csv"
            ],
            0,
            "duplicate vendor and invoice"
          ]
        ]
        with tempfile.TemporaryDirectory() as folder:
            for name in ["invoices.csv"]:
                shutil.copy(ROOT / name, folder)
            for args, code, expected in cases:
                with self.subTest(args=args):
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "app.py"), *args], cwd=folder,
                        capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, code, result.stderr)
                    if expected:
                        self.assertIn(expected, result.stdout + result.stderr)
                    else:
                        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
