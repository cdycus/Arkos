import unittest
import audit_engine

class TestAuditEngine(unittest.TestCase):
    def test_audit_foresight(self):
        try:
            audit_engine.audit_foresight()
        except Exception:
            self.fail("Function audit_foresight raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()