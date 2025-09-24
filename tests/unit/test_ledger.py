import unittest
import ledger

class TestLedger(unittest.TestCase):
    def test_append(self):
        try:
            ledger.append()
        except Exception:
            self.fail("Function append raised an unexpected exception")

    def test_verify(self):
        try:
            ledger.verify()
        except Exception:
            self.fail("Function verify raised an unexpected exception")

    def test_PulseLedger_instantiation(self):
        try:
            instance = ledger.PulseLedger()
        except Exception:
            self.fail("Class PulseLedger failed to instantiate")


if __name__ == "__main__":
    unittest.main()