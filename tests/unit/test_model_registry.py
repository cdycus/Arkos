import unittest
import model_registry

class TestModelRegistry(unittest.TestCase):
    def test_load(self):
        try:
            model_registry.load()
        except Exception:
            self.fail("Function load raised an unexpected exception")

    def test_register(self):
        try:
            model_registry.register()
        except Exception:
            self.fail("Function register raised an unexpected exception")

    def test_save(self):
        try:
            model_registry.save()
        except Exception:
            self.fail("Function save raised an unexpected exception")

    def test_is_trusted(self):
        try:
            model_registry.is_trusted()
        except Exception:
            self.fail("Function is_trusted raised an unexpected exception")

    def test_ModelRegistry_instantiation(self):
        try:
            instance = model_registry.ModelRegistry()
        except Exception:
            self.fail("Class ModelRegistry failed to instantiate")


if __name__ == "__main__":
    unittest.main()