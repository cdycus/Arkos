import unittest
import runtime_status

class TestRuntimeStatus(unittest.TestCase):
    def test_update_status(self):
        try:
            runtime_status.update_status()
        except Exception:
            self.fail("Function update_status raised an unexpected exception")

    def test_snapshot(self):
        try:
            runtime_status.snapshot()
        except Exception:
            self.fail("Function snapshot raised an unexpected exception")

    def test_RuntimeStatus_instantiation(self):
        try:
            instance = runtime_status.RuntimeStatus()
        except Exception:
            self.fail("Class RuntimeStatus failed to instantiate")


if __name__ == "__main__":
    unittest.main()