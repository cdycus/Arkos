import unittest
import pulse_dependency_graph

class TestPulseDependencyGraph(unittest.TestCase):
    def test_is_blocked(self):
        try:
            pulse_dependency_graph.is_blocked()
        except Exception:
            self.fail("Function is_blocked raised an unexpected exception")

    def test_DependencyGraph_instantiation(self):
        try:
            instance = pulse_dependency_graph.DependencyGraph()
        except Exception:
            self.fail("Class DependencyGraph failed to instantiate")


if __name__ == "__main__":
    unittest.main()