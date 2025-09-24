import unittest
import attitude_model

class TestAttitudeModel(unittest.TestCase):
    def test_update(self):
        try:
            attitude_model.update()
        except Exception:
            self.fail("Function update raised an unexpected exception")

    def test_get_attitude(self):
        try:
            attitude_model.get_attitude()
        except Exception:
            self.fail("Function get_attitude raised an unexpected exception")

    def test_update_state(self):
        try:
            attitude_model.update_state()
        except Exception:
            self.fail("Function update_state raised an unexpected exception")

    def test_AttitudeModel_instantiation(self):
        try:
            instance = attitude_model.AttitudeModel()
        except Exception:
            self.fail("Class AttitudeModel failed to instantiate")

    def test_AttitudeBayes_instantiation(self):
        try:
            instance = attitude_model.AttitudeBayes()
        except Exception:
            self.fail("Class AttitudeBayes failed to instantiate")


if __name__ == "__main__":
    unittest.main()