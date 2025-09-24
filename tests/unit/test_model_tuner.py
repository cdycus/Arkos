import unittest
import model_tuner

class TestModelTuner(unittest.TestCase):
    def test_tune(self):
        try:
            model_tuner.tune()
        except Exception:
            self.fail("Function tune raised an unexpected exception")

    def test_ModelTuner_instantiation(self):
        try:
            instance = model_tuner.ModelTuner()
        except Exception:
            self.fail("Class ModelTuner failed to instantiate")


if __name__ == "__main__":
    unittest.main()