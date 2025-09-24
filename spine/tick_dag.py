# tick_dag.py

TICK_DAG = {
    "memory_tick": [],
    "belief_tick": ["memory_tick"],
    "foresight_tick": ["belief_tick"],
    "ethics_tick": ["foresight_tick"],
    "governance_tick": ["ethics_tick"]
}

def get_dependencies(tick_name):
    return TICK_DAG.get(tick_name, [])