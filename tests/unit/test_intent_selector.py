import unittest
import intent_selector

class TestIntentSelector(unittest.TestCase):
    def test_select_intent(self):
        try:
            intent_selector.select_intent()
        except Exception:
            self.fail("Function select_intent raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()