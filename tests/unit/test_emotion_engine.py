import unittest
import emotion_engine

class TestEmotionEngine(unittest.TestCase):
    def test_update(self):
        try:
            emotion_engine.update()
        except Exception:
            self.fail("Function update raised an unexpected exception")

    def test_get_emotion_vector(self):
        try:
            emotion_engine.get_emotion_vector()
        except Exception:
            self.fail("Function get_emotion_vector raised an unexpected exception")

    def test_predict_emotion(self):
        try:
            emotion_engine.predict_emotion()
        except Exception:
            self.fail("Function predict_emotion raised an unexpected exception")

    def test_EmotionEngine_instantiation(self):
        try:
            instance = emotion_engine.EmotionEngine()
        except Exception:
            self.fail("Class EmotionEngine failed to instantiate")

    def test_EmotionModel_instantiation(self):
        try:
            instance = emotion_engine.EmotionModel()
        except Exception:
            self.fail("Class EmotionModel failed to instantiate")


if __name__ == "__main__":
    unittest.main()