
from memory.experience_log import log_experience, load_recent_experiences
from memory.reflection_hook import reflect_on_behavior

def test_memory_logging_and_reflection():
    log_experience("try_feature_x", "curious", "negative")
    log_experience("try_feature_x", "neutral", "negative")
    log_experience("try_feature_y", "hopeful", "positive")
    experiences = load_recent_experiences()
    assert len(experiences) >= 3

    reflection = reflect_on_behavior()
    assert 'bias_avoid_intent' in reflection
    print("✔ Memory loop reflects on behavior correctly:", reflection)
