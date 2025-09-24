import unittest
import pulse_priority_queue

class TestPulsePriorityQueue(unittest.TestCase):
    def test_enqueue(self):
        try:
            pulse_priority_queue.enqueue()
        except Exception:
            self.fail("Function enqueue raised an unexpected exception")

    def test_dequeue(self):
        try:
            pulse_priority_queue.dequeue()
        except Exception:
            self.fail("Function dequeue raised an unexpected exception")

    def test_is_empty(self):
        try:
            pulse_priority_queue.is_empty()
        except Exception:
            self.fail("Function is_empty raised an unexpected exception")

    def test_PulsePriorityQueue_instantiation(self):
        try:
            instance = pulse_priority_queue.PulsePriorityQueue()
        except Exception:
            self.fail("Class PulsePriorityQueue failed to instantiate")


if __name__ == "__main__":
    unittest.main()