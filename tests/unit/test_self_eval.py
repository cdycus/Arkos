import unittest
import self_eval

class TestSelfEval(unittest.TestCase):
    def test_evaluate_thought_chain(self):
        try:
            self_eval.evaluate_thought_chain()
        except Exception:
            self.fail("Function evaluate_thought_chain raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()