from intents import Intent

def test_intent_structure():
    i = Intent("do_something", "core", 0.88)
    assert isinstance(i.to_dict(), dict)
    assert i.to_dict()["action"] == "do_something"
