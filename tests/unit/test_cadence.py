import unittest
import cadence

class TestCadence(unittest.TestCase):
    def test_update_entropy(self):
        try:
            cadence.update_entropy()
        except Exception:
            self.fail("Function update_entropy raised an unexpected exception")

    def test_get_interval(self):
        try:
            cadence.get_interval()
        except Exception:
            self.fail("Function get_interval raised an unexpected exception")

    def test_PulseCadence_instantiation(self):
        try:
            instance = cadence.PulseCadence()
        except Exception:
            self.fail("Class PulseCadence failed to instantiate")


if __name__ == "__main__":
    unittest.main()