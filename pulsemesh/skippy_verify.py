import os
import sys
import importlib
import traceback
from pathlib import Path

def compile_check(py_file):
    try:
        with open(py_file, "r") as f:
            source = f.read()
        compile(source, filename=str(py_file), mode="exec")
        return True, None
    except SyntaxError as e:
        return False, f"{py_file.name}:{e.lineno} - {e.msg}"

def import_check(module_path, class_name):
    try:
        mod = importlib.import_module(module_path)
        getattr(mod, class_name)
        return True, None
    except Exception as e:
        return False, f"{module_path}.{class_name} - {str(e)}"

def main():
    base = Path(__file__).resolve().parent
    errors = []

    print("🔍 Verifying syntax...")
    for py_file in base.rglob("*.py"):
        if py_file.name == "skippy_verify.py":
            continue
        ok, err = compile_check(py_file)
        if not ok:
            errors.append(err)

    print("🔍 Verifying imports and classes...")
    checks = [
        ("core_brain.registry", "PulseRegistry"),
        ("core_brain.replay_buffer", "PulseReplayBuffer"),
        ("core_brain.cadence", "PulseCadence"),
        ("core_brain.feedback_engine", "PulseFeedbackEngine"),
        ("core_brain.meta_health", "MetaPulseHealth"),
        ("core_brain.units.base", "PulseUnit"),
    ]

    for mod, cls in checks:
        ok, err = import_check(mod, cls)
        if not ok:
            errors.append(err)

    if errors:
        print("\n❌ Verification failed with the following issues:")
        for err in errors:
            print(" -", err)
        sys.exit(1)
    else:
        print("\n✅ All checks passed. Skippy is sovereign and safe.")

if __name__ == "__main__":
    main()