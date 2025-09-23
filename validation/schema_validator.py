import json
import os
import logging
from jsonschema import validate, ValidationError

def load_and_validate_json(file_path, schema):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        logging.error(f"Validation failed for {file_path}: {e.message}")
        raise
    return data