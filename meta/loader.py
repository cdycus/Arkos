
import json
import os

def load_policy_rules():
    path = os.path.join(os.path.dirname(__file__), '../../policy_rules.json')
    if not os.path.exists(path):
        raise FileNotFoundError("Policy rules not found.")
    with open(path, 'r') as file:
        return json.load(file)
