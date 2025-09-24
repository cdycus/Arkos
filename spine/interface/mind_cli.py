
import argparse
from pprint import pprint
from memory.trait_tracker import infer_traits
from memory.reflection_hook import reflect_on_behavior
from mind.intent.planner import generate_action_plan
from mind.expression.plan_executor import execute_plan
from mind.intent.proactive_generator import generate_proactive_intent
from spine.meta.state_backup import archive_state
from spine.meta.skippy_self_check import update_skippy_state

parser = argparse.ArgumentParser(description='🧠 Skippy CLI - Sovereign Mind Debug Shell')
parser.add_argument('--state', action='store_true', help='Show Skippy cognitive state')
parser.add_argument('--trait', action='store_true', help='Show synthetic trait')
parser.add_argument('--reflect', action='store_true', help='Run behavioral reflection')
parser.add_argument('--intent', action='store_true', help='Generate proactive intent')
parser.add_argument('--plan', action='store_true', help='Generate action plan')
parser.add_argument('--exec', action='store_true', help='Execute full plan')
parser.add_argument('--backup', action='store_true', help='Run memory backup')

args = parser.parse_args()

if args.state:
    pprint(update_skippy_state())

if args.trait:
    pprint(infer_traits())

if args.reflect:
    pprint(reflect_on_behavior())

if args.intent:
    print("Intent:", generate_proactive_intent())

if args.plan:
    pprint(generate_action_plan())

if args.exec:
    steps = execute_plan()
    pprint(steps)

if args.backup:
    archive_state()


parser.add_argument('--history', choices=['plans', 'traits', 'experiences'], help='View history logs')
parser.add_argument('--examples', action='store_true', help='Show usage examples')

if args.examples:
    print("""\n🧪 Skippy CLI Examples:
  --state           Show Skippy's current cognitive snapshot
  --trait           View inferred synthetic trait
  --reflect         See behavioral reflection bias and summary
  --intent          Generate a single proactive intent
  --plan            Generate a full action plan
  --exec            Execute a plan and show signed output
  --backup          Save a snapshot of Skippy's memory
  --history plans   View recent autonomous plans
  --history traits  View trait history over time
  --history experiences  Show past experiences logged

""")

if args.history == "plans":
    with open("spine/meta/plan_history.jsonl") as f:
        for line in f.readlines()[-5:]:
            print(line.strip())

if args.history == "traits":
    with open("spine/meta/trait_history.jsonl") as f:
        for line in f.readlines()[-5:]:
            print(line.strip())

if args.history == "experiences":
    with open("memory/experience_store.jsonl") as f:
        for line in f.readlines()[-5:]:
            print(line.strip())


parser.add_argument('--history', choices=['plan', 'trait', 'intent'], help='Show history of specified type')

if args.history:
    if args.history == 'plan':
        with open("spine/meta/plan_history.jsonl") as f:
            lines = f.readlines()[-5:]
            print("\n".join(lines))
    elif args.history == 'trait':
        with open("spine/meta/trait_history.jsonl") as f:
            lines = f.readlines()[-5:]
            print("\n".join(lines))
    elif args.history == 'intent':
        with open("memory/experience_store.jsonl") as f:
            lines = f.readlines()[-5:]
            print("\n".join(lines))

import time
import sys

HISTORY_LOG = "spine/meta/cli_history.log"

def log_cli_command(args):
    timestamp = datetime.utcnow().isoformat()
    with open(HISTORY_LOG, "a") as log:
        log.write(f"{timestamp} CLI: {' '.join(sys.argv)}\n")

log_cli_command(sys.argv)

if args.watch:
    target = args.watch
    try:
        while True:
            print("🔁 [WATCH]", target)
            if target == "state":
                pprint(update_skippy_state())
            elif target == "trait":
                pprint(infer_traits())
            elif target == "reflect":
                pprint(reflect_on_behavior())
            elif target == "plan":
                pprint(generate_action_plan())
            elif target == "exec":
                pprint(execute_plan())
            print("⏳ Refresh in 10s...\n")
            time.sleep(10)
    except KeyboardInterrupt:
        print("👋 Exiting watch mode.")
