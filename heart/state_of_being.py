from emotion_engine import EmotionEngine
from attitude_model import AttitudeModel

class StateOfBeing:
    def __init__(self):
        self.emotion_engine = EmotionEngine()
        self.attitude_model = AttitudeModel()

    def update(self, event, foresight_result=None):
        self.emotion_engine.update(event)
        if foresight_result:
            self.attitude_model.update(foresight_result)

    def get_state_vector(self):
        return {
            "emotion_vector": self.emotion_engine.get_emotion_vector(),
            "attitude": self.attitude_model.get_attitude()
        }
