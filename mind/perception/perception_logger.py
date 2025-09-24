import json
import os

def log_perception(data, input_type):
    folder = "data"
    os.makedirs(folder, exist_ok=True)
    file_map = {
        "video": "visual_input_log.jsonl",
        "audio": "audio_input_log.jsonl"
    }
    path = os.path.join(folder, file_map.get(input_type, "general_input_log.jsonl"))
    with open(path, "a") as f:
        f.write(json.dumps(data) + "\n")
