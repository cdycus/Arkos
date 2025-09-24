import unittest
import meta_insight_log

class TestMetaInsightLog(unittest.TestCase):
    def test_load(self):
        try:
            meta_insight_log.load()
        except Exception:
            self.fail("Function load raised an unexpected exception")

    def test_record(self):
        try:
            meta_insight_log.record()
        except Exception:
            self.fail("Function record raised an unexpected exception")

    def test_save(self):
        try:
            meta_insight_log.save()
        except Exception:
            self.fail("Function save raised an unexpected exception")

    def test_MetaInsightLog_instantiation(self):
        try:
            instance = meta_insight_log.MetaInsightLog()
        except Exception:
            self.fail("Class MetaInsightLog failed to instantiate")


if __name__ == "__main__":
    unittest.main()