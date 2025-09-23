class StateManager:
    def __init__(self):
        self.attention_weights = {}

    def update_attention(self, pulse_type):
        self.attention_weights[pulse_type] = self.attention_weights.get(pulse_type, 0) + 0.1

    def decay_attention(self):
        for k in self.attention_weights:
            self.attention_weights[k] *= 0.9
