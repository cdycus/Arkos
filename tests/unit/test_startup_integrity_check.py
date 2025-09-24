import unittest
from startup_integrity_check import run_integrity_check

class TestStartupIntegrityCheck(unittest.TestCase):
    def test_integrity_check_runs(self):
        result = run_integrity_check()
        self.assertTrue("success" in result or "failed" in result)