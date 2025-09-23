import datetime

model_registry = {}

def register_model(name, version, trust_score):
    model_registry[name] = {
        "version": version,
        "trust_score": trust_score,
        "last_updated": datetime.datetime.utcnow().isoformat()
    }

def get_model_metadata(name):
    return model_registry.get(name, {})

def audit_model(name, trust_delta):
    if name in model_registry:
        model_registry[name]["trust_score"] += trust_delta
        return True
    return False
