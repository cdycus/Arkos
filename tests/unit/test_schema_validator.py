import unittest
import schema_validator

class TestSchemaValidator(unittest.TestCase):
    def test_load_and_validate_json(self):
        try:
            schema_validator.load_and_validate_json()
        except Exception:
            self.fail("Function load_and_validate_json raised an unexpected exception")


if __name__ == "__main__":
    unittest.main()