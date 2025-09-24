import unittest
import pulse_expression_intent

class TestPulseExpressionIntent(unittest.TestCase):
    def test_build_expression_intent(self):
        try:
            pulse_expression_intent.build_expression_intent()
        except Exception:
            self.fail("Function build_expression_intent raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()