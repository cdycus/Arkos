import unittest
import expression_reflection

class TestExpressionReflection(unittest.TestCase):
    def test_build_reflection(self):
        try:
            expression_reflection.build_reflection()
        except Exception:
            self.fail("Function build_reflection raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()