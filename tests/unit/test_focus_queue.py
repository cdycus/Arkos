import unittest
import focus_queue

class TestFocusQueue(unittest.TestCase):
    def test_add(self):
        try:
            focus_queue.add()
        except Exception:
            self.fail("Function add raised an unexpected exception")

    def test_top(self):
        try:
            focus_queue.top()
        except Exception:
            self.fail("Function top raised an unexpected exception")

    def test_snapshot(self):
        try:
            focus_queue.snapshot()
        except Exception:
            self.fail("Function snapshot raised an unexpected exception")

    def test_FocusQueue_instantiation(self):
        try:
            instance = focus_queue.FocusQueue()
        except Exception:
            self.fail("Class FocusQueue failed to instantiate")


if __name__ == "__main__":
    unittest.main()