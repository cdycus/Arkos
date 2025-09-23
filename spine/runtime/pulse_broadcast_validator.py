from jsonschema import ValidationError
import json

def load_schema(path="spine/pulse_schema.json"):
    with open(path) as f:
        return json.load(f)

def validate_pulse(pulse):
    schema_map = load_schema()
    ptype = pulse.get("type")
    if not ptype or ptype not in schema_map:
        raise ValidationError(f"Unknown pulse type: {ptype}")
    required = schema_map[ptype]["required"]
    missing = [r for r in required if r not in pulse]
    if missing:
        raise ValidationError(f"Missing fields: {missing}")
    return True
