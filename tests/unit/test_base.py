import unittest
import base

class TestBase(unittest.TestCase):
    def test_should_emit(self):
        try:
            base.should_emit()
        except Exception:
            self.fail("Function should_emit raised an unexpected exception")

    def test_emit(self):
        try:
            base.emit()
        except Exception:
            self.fail("Function emit raised an unexpected exception")

    def test_PulseUnit_instantiation(self):
        try:
            instance = base.PulseUnit()
        except Exception:
            self.fail("Class PulseUnit failed to instantiate")


if __name__ == "__main__":
    unittest.main()