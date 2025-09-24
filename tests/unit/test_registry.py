import unittest
import registry

class TestRegistry(unittest.TestCase):
    def test_register(self):
        try:
            registry.register()
        except Exception:
            self.fail("Function register raised an unexpected exception")

    def test_get_units(self):
        try:
            registry.get_units()
        except Exception:
            self.fail("Function get_units raised an unexpected exception")

    def test_get_config(self):
        try:
            registry.get_config()
        except Exception:
            self.fail("Function get_config raised an unexpected exception")

    def test_get_active_units(self):
        try:
            registry.get_active_units()
        except Exception:
            self.fail("Function get_active_units raised an unexpected exception")

    def test_PulseRegistry_instantiation(self):
        try:
            instance = registry.PulseRegistry()
        except Exception:
            self.fail("Class PulseRegistry failed to instantiate")


if __name__ == "__main__":
    unittest.main()