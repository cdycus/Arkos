import unittest
import expression_planner

class TestExpressionPlanner(unittest.TestCase):
    def test_select_expression_type(self):
        try:
            expression_planner.select_expression_type()
        except Exception:
            self.fail("Function select_expression_type raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()