import unittest
import pulse_queue

class TestPulseQueue(unittest.TestCase):
    def test_enqueue_inbound(self):
        try:
            pulse_queue.enqueue_inbound()
        except Exception:
            self.fail("Function enqueue_inbound raised an unexpected exception")

    def test_PulseQueue_instantiation(self):
        try:
            instance = pulse_queue.PulseQueue()
        except Exception:
            self.fail("Class PulseQueue failed to instantiate")


if __name__ == "__main__":
    unittest.main()