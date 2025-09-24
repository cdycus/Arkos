import unittest
import pulse_broadcast_validator

class TestPulseBroadcastValidator(unittest.TestCase):
    def test_load_schema(self):
        try:
            pulse_broadcast_validator.load_schema()
        except Exception:
            self.fail("Function load_schema raised an unexpected exception")

    def test_validate_pulse(self):
        try:
            pulse_broadcast_validator.validate_pulse()
        except Exception:
            self.fail("Function validate_pulse raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()