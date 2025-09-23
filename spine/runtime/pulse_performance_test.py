import time, json

def run_test(num=100):
    start = time.time()
    for i in range(num):
        pulse = {
            "type": "test_pulse",
            "pulse_id": f"test_{i}",
            "timestamp": time.time(),
            "confidence": 0.5
        }
        _ = json.dumps(pulse)
    end = time.time()
    print(f"Emitted {num} pulses in {round(end - start, 2)} seconds")

if __name__ == "__main__":
    run_test()
