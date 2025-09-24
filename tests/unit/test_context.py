import unittest
import context

class TestContext(unittest.TestCase):
    def test_QuantumContext_instantiation(self):
        try:
            instance = context.QuantumContext()
        except Exception:
            self.fail("Class QuantumContext failed to instantiate")


if __name__ == "__main__":
    unittest.main()