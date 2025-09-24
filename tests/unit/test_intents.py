import unittest
import intents

class TestIntents(unittest.TestCase):
    def test_to_dict(self):
        try:
            intents.to_dict()
        except Exception:
            self.fail("Function to_dict raised an unexpected exception")

    def test_Intent_instantiation(self):
        try:
            instance = intents.Intent()
        except Exception:
            self.fail("Class Intent failed to instantiate")


if __name__ == "__main__":
    unittest.main()