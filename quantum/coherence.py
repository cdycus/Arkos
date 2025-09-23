from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CoherenceChecker:
    def check(self, future, state):
        if not state.get("vector") or not isinstance(state["vector"], list):
            return 0.5
        description = future["description"].lower()
        keywords = ["scale", "optimize", "wait", "monitor", "alert", "log"]
        future_vector = [1.0 if k in description else 0.0 for k in keywords]
        state_vector = np.array(state["vector"]).reshape(1, -1)
        future_vector = np.array(future_vector).reshape(1, -1)
        similarity = cosine_similarity(state_vector, future_vector)[0][0]
        return round(similarity, 2)
