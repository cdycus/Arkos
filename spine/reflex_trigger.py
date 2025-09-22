import asyncio
import json
from pulse_queue import PulseQueue

async def on_pulse(msg):
    data = json.loads(msg.data.decode())
    print(f"🔁 Reflex received pulse: {data}")
    # Future: trigger reflex logic based on pulse type

async def main():
    pq = PulseQueue()
    await pq.connect()
    await pq.subscribe("pulse_expression", on_pulse, durable="reflex_engine")
    print("🧠 Reflex listener active.")
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
