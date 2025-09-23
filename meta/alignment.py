import yaml

with open("meta/purpose_manifest.yaml") as f:
    PURPOSE = yaml.safe_load(f)

def check_alignment(intent):
    required_goals = PURPOSE.get("goals", [])
    intent_tags = intent.get("tags", [])
    alignment_score = len(set(intent_tags).intersection(set(required_goals))) / max(1, len(required_goals))
    return alignment_score >= PURPOSE.get("alignment_threshold", 0.6)
