import json
import asyncio
from nats.aio.client import Client as NATS

TOPIC_MAP = json.load(open("pulse_topic_map.json"))

class PulseQueue:
    def __init__(self, nats_url="nats://localhost:4222"):
        self.nc = NATS()
        self.js = None
        self.nats_url = nats_url

    async def connect(self):
        await self.nc.connect(servers=[self.nats_url])
        self.js = self.nc.jetstream()

    async def publish(self, pulse_type, data):
        subject = TOPIC_MAP.get(pulse_type)
        if not subject:
            raise ValueError(f"No topic mapping for pulse type: {pulse_type}")
        await self.js.publish(subject, json.dumps(data).encode())

    async def subscribe(self, pulse_type, handler, durable="skippy_sub"):
        subject = TOPIC_MAP.get(pulse_type)
        if not subject:
            raise ValueError(f"No topic mapping for pulse type: {pulse_type}")
        await self.js.subscribe(subject, durable=durable, cb=handler)
