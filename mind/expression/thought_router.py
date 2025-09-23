from quantum.wavefunction import collapse_future
from memory.memory_log import log_memory
from intents import Intent

class ThoughtRouter:
    def __init__(self, state_manager, dispatcher):
        self.state_manager = state_manager
        self.dispatcher = dispatcher

    def process_thought(self, context, future_options):
        # collapse the best future
        selected = collapse_future(context, future_options[0])
        memory = log_memory(context, selected)
        intent = Intent(
            action=selected["description"],
            target="spine",
            confidence=selected.get("confidence", 0.5),
            metadata={"memory_id": memory["id"]}
        )
        self.dispatcher.dispatch(intent)
