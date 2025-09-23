class PulseMeshRouter:
    def __init__(self):
        self.peers = []  # list of (host, port) for future routing

    def broadcast(self, pulse: dict):
        # Stub: simulate sending core_brain to peer cores
        print(f"Broadcasting {pulse['type']} to mesh peers: {self.peers}")


    async def start_nats_listener(self):
        async def heartbeat_handler(msg):
            data = __import__('json').loads(msg.data.decode())
            peer_id = data.get("sovereign_id")
            self.peer_registry.update(peer_id, data.get("timestamp"))
            print(f"Heartbeat received from {peer_id}")
            self.pulse_queue.enqueue_inbound(data)

        await self.pulse_broadcaster.nats.subscribe("pulse.heartbeat", heartbeat_handler)
