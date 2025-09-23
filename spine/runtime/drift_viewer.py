import json
import os

def view_alignment_trend(trace_path="data/foresight_trace.jsonl", window=10):
    if not os.path.exists(trace_path):
        print("No trace found.")
        return
    with open(trace_path) as f:
        lines = f.readlines()[-window:]
    scores = []
    for line in lines:
        try:
            entry = json.loads(line)
            scores.append(entry["result"]["alignment"])
        except:
            continue
    print("📉 Recent Alignment Scores:")
    for i, score in enumerate(scores):
        print(f"[{i}] {round(score, 3)}")

if __name__ == "__main__":
    view_alignment_trend()
