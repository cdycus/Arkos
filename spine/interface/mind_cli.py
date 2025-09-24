import argparse
import json
from skippy_mind_entry import receive_input

def main():
    parser = argparse.ArgumentParser(description="Talk to Skippy's Mind")
    parser.add_argument("mode", choices=["reflect", "state", "expression", "intent"], help="Which cognitive mode to trigger")
    parser.add_argument("--context", type=str, help="JSON string of context data")

    args = parser.parse_args()
    context = json.loads(args.context) if args.context else {}

    payload = {
        "mode": args.mode,
        "context": context
    }

    response = receive_input(payload)
    print("\n🧠 Skippy Response:")
    print(json.dumps(response, indent=2))

    with open("data/mind_entry_log.jsonl", "a") as log:
        log.write(json.dumps({"cli_input": payload, "response": response}) + "\n")

if __name__ == "__main__":
    main()
