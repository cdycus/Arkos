import unittest
import escalation_log

class TestEscalationLog(unittest.TestCase):
    def test_load(self):
        try:
            escalation_log.load()
        except Exception:
            self.fail("Function load raised an unexpected exception")

    def test_record(self):
        try:
            escalation_log.record()
        except Exception:
            self.fail("Function record raised an unexpected exception")

    def test_save(self):
        try:
            escalation_log.save()
        except Exception:
            self.fail("Function save raised an unexpected exception")

    def test_EscalationLog_instantiation(self):
        try:
            instance = escalation_log.EscalationLog()
        except Exception:
            self.fail("Class EscalationLog failed to instantiate")


if __name__ == "__main__":
    unittest.main()