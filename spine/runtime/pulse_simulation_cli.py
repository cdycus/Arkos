import json, time

def replay_log(path="data/foresight_trace.jsonl"):
    try:
        with open(path) as f:
            for line in f:
                entry = json.loads(line)
                print(f"🔁 Replay Foresight: {entry['class']} => {entry['result']['decision']} | Confidence: {entry['result']['confidence']}")
                time.sleep(0.5)
    except Exception as e:
        print(f"Error reading: {e}")

if __name__ == "__main__":
    replay_log()
