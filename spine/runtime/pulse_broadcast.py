class PulseBroadcaster:
    def __init__(self, nats_client):
        self.nats = nats_client

    async def broadcast(self, subject, pulse):
        await self.nats.publish(subject, pulse)

    async def broadcast_heartbeat(self, pulse):
        await self.broadcast("pulse.heartbeat", pulse)

    async def broadcast_result(self, pulse):
        await self.broadcast("pulse.foresight_result", pulse)
