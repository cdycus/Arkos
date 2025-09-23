import pytest
from intents import Intent
from dispatcher import Dispatcher

def test_dispatch_valid_intent(monkeypatch):
    monkeypatch.setattr("meta.alignment.check_alignment", lambda x: True)
    monkeypatch.setattr("spine.router.dispatch_to_spine", lambda x: x)

    dispatcher = Dispatcher(test_mode=True)
    intent = Intent("test_action", "spine", 0.95)
    dispatcher.dispatch(intent)
