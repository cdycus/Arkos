class QuantumContext:
    def __init__(self, thought, state):
        self.thought = thought
        self.state = state
        self.possible_futures = []
        self.selected = None
        self.collapsed = False
