import unittest
import attention_score

class TestAttentionScore(unittest.TestCase):
    def test_score_attention(self):
        try:
            attention_score.score_attention()
        except Exception:
            self.fail("Function score_attention raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()