import unittest
import startup_integrity_check

class TestStartupIntegrityCheck(unittest.TestCase):
    def test_run_startup_checks(self):
        try:
            startup_integrity_check.run_startup_checks()
        except Exception:
            self.fail("Function run_startup_checks raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()