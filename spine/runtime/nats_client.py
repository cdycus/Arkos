# Stub for nats_client.py


    async def subscribe(self, subject, handler):
        await self.nc.subscribe(subject, cb=handler)
