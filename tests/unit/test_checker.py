import unittest
import checker

class TestChecker(unittest.TestCase):
    def test_load_registry(self):
        try:
            checker.load_registry()
        except Exception:
            self.fail("Function load_registry raised an unexpected exception")

    def test_save_quarantine(self):
        try:
            checker.save_quarantine()
        except Exception:
            self.fail("Function save_quarantine raised an unexpected exception")

    def test_check_services(self):
        try:
            checker.check_services()
        except Exception:
            self.fail("Function check_services raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()