import unittest
import foresight_audit

class TestForesightAudit(unittest.TestCase):
    def test_run_audit(self):
        try:
            foresight_audit.run_audit()
        except Exception:
            self.fail("Function run_audit raised an unexpected exception")

    def test_predict_drift(self):
        try:
            foresight_audit.predict_drift()
        except Exception:
            self.fail("Function predict_drift raised an unexpected exception")

    def test_ForesightAudit_instantiation(self):
        try:
            instance = foresight_audit.ForesightAudit()
        except Exception:
            self.fail("Class ForesightAudit failed to instantiate")

    def test_DriftPredictor_instantiation(self):
        try:
            instance = foresight_audit.DriftPredictor()
        except Exception:
            self.fail("Class DriftPredictor failed to instantiate")


if __name__ == "__main__":
    unittest.main()