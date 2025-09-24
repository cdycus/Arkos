import unittest
import memory_semantics

class TestMemorySemantics(unittest.TestCase):
    def test_compute_similarity_matrix(self):
        try:
            memory_semantics.compute_similarity_matrix()
        except Exception:
            self.fail("Function compute_similarity_matrix raised an unexpected exception")

    def test_cluster_beliefs(self):
        try:
            memory_semantics.cluster_beliefs()
        except Exception:
            self.fail("Function cluster_beliefs raised an unexpected exception")

    def test_link_beliefs_to_actions(self):
        try:
            memory_semantics.link_beliefs_to_actions()
        except Exception:
            self.fail("Function link_beliefs_to_actions raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()