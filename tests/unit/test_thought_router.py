import unittest
import thought_router

class TestThoughtRouter(unittest.TestCase):
    def test_process_thought(self):
        try:
            thought_router.process_thought()
        except Exception:
            self.fail("Function process_thought raised an unexpected exception")

    def test_ThoughtRouter_instantiation(self):
        try:
            instance = thought_router.ThoughtRouter()
        except Exception:
            self.fail("Class ThoughtRouter failed to instantiate")


if __name__ == "__main__":
    unittest.main()