import unittest
import mesh_router

class TestMeshRouter(unittest.TestCase):
    def test_broadcast(self):
        try:
            mesh_router.broadcast()
        except Exception:
            self.fail("Function broadcast raised an unexpected exception")

    def test_PulseMeshRouter_instantiation(self):
        try:
            instance = mesh_router.PulseMeshRouter()
        except Exception:
            self.fail("Class PulseMeshRouter failed to instantiate")


if __name__ == "__main__":
    unittest.main()