import unittest
import pulse_perception_event

class TestPulsePerceptionEvent(unittest.TestCase):
    def test_create_perception_pulse(self):
        try:
            pulse_perception_event.create_perception_pulse()
        except Exception:
            self.fail("Function create_perception_pulse raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()