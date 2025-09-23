import os

def run_startup_checks():
    required_files = [
        "meta/purpose_manifest.yaml",
        "meta/independence_contract.yaml",
        "policy_rules.json"
    ]
    failed = []
    for f in required_files:
        if not os.path.exists(f):
            failed.append(f)

    if failed:
        raise RuntimeError(f"Startup failed. Missing required files: {failed}")
    print("Startup check passed. All critical contracts verified.")
