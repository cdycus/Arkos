import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ResonanceEvaluator:
    def match(self, future, state_of_being):
        emotion_vector = state_of_being.get("emotion_vector")
        attitude_vector = state_of_being.get("attitude_vector")
        if not emotion_vector or not attitude_vector:
            return 0.5
        keywords = ["scale", "optimize", "wait", "log", "alert", "deploy"]
        future_vector = [1.0 if k in future["description"].lower() else 0.0 for k in keywords]
        future_vector = np.array(future_vector).reshape(1, -1)
        emotion_sim = cosine_similarity(np.array(emotion_vector).reshape(1, -1), future_vector)[0][0]
        attitude_sim = cosine_similarity(np.array(attitude_vector).reshape(1, -1), future_vector)[0][0]
        resonance_score = (0.7 * emotion_sim + 0.3 * attitude_sim)
        return round(resonance_score, 2)
