from dispatcher import Dispatcher
from state_manager import StateManager
from thought_router import ThoughtRouter

def test_process_thought():
    dispatcher = Dispatcher(test_mode=True)
    state_manager = StateManager()
    router = ThoughtRouter(state_manager, dispatcher)

    context = {"thought": "Simulated Event"}
    futures = [
        {"description": "act now", "confidence": 0.9},
        {"description": "wait", "confidence": 0.5}
    ]
    router.process_thought(context, futures)
