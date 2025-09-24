import unittest
import pulse_state_of_being

class TestPulseStateOfBeing(unittest.TestCase):
    def test_create_state_pulse(self):
        try:
            pulse_state_of_being.create_state_pulse()
        except Exception:
            self.fail("Function create_state_pulse raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()