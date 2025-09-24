import unittest
import observer

class TestObserver(unittest.TestCase):
    def test_get_focus_bias(self):
        try:
            observer.get_focus_bias()
        except Exception:
            self.fail("Function get_focus_bias raised an unexpected exception")

    def test_ObserverTracker_instantiation(self):
        try:
            instance = observer.ObserverTracker()
        except Exception:
            self.fail("Class ObserverTracker failed to instantiate")


if __name__ == "__main__":
    unittest.main()