import unittest
import error_router

class TestErrorRouter(unittest.TestCase):
    def test_handle(self):
        try:
            error_router.handle()
        except Exception:
            self.fail("Function handle raised an unexpected exception")

    def test_classify(self):
        try:
            error_router.classify()
        except Exception:
            self.fail("Function classify raised an unexpected exception")

    def test_ErrorRouter_instantiation(self):
        try:
            instance = error_router.ErrorRouter()
        except Exception:
            self.fail("Class ErrorRouter failed to instantiate")

    def test_ErrorClassifier_instantiation(self):
        try:
            instance = error_router.ErrorClassifier()
        except Exception:
            self.fail("Class ErrorClassifier failed to instantiate")


if __name__ == "__main__":
    unittest.main()