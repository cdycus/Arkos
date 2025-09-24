import unittest
import pulse_broadcast

class TestPulseBroadcast(unittest.TestCase):
    def test_PulseBroadcaster_instantiation(self):
        try:
            instance = pulse_broadcast.PulseBroadcaster()
        except Exception:
            self.fail("Class PulseBroadcaster failed to instantiate")


if __name__ == "__main__":
    unittest.main()