import unittest
import abstraction

class TestAbstraction(unittest.TestCase):
    def test_load_memories(self):
        try:
            abstraction.load_memories()
        except Exception:
            self.fail("Function load_memories raised an unexpected exception")

    def test_cluster_memories(self):
        try:
            abstraction.cluster_memories()
        except Exception:
            self.fail("Function cluster_memories raised an unexpected exception")

    def test_summarize_cluster(self):
        try:
            abstraction.summarize_cluster()
        except Exception:
            self.fail("Function summarize_cluster raised an unexpected exception")

    def test_save_abstractions(self):
        try:
            abstraction.save_abstractions()
        except Exception:
            self.fail("Function save_abstractions raised an unexpected exception")

    def test_run(self):
        try:
            abstraction.run()
        except Exception:
            self.fail("Function run raised an unexpected exception")

    def test_MemoryAbstractionEngine_instantiation(self):
        try:
            instance = abstraction.MemoryAbstractionEngine()
        except Exception:
            self.fail("Class MemoryAbstractionEngine failed to instantiate")


if __name__ == "__main__":
    unittest.main()