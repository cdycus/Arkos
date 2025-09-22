from fastapi import FastAPI, Request
import uvicorn
import logging

if __name__ == '__main__':
    import spine.router as router

if __name__ == '__main__':
    import spine.ledger.ledger as ledger

#from spine.router import inject_pulse
#from spine.ledger.ledger import PulseLedger

app = FastAPI()
#ledger.PulseLedger = PulseLedger()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("skippy-api")


@app.get("/")
async def welcome():
    return {"status": "ok", "message": "Skippy Pulse API is healthy"}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Skippy Pulse API is healthy"}

@app.post("/pulse/inject")
async def pulse_inject(request: Request):
    payload = await request.json()
    if router.inject_pulse(payload):
        return {"status": "ok"}
    else:
        return {"status": "error", "reason": "failed to inject"}

@app.post("/pulse/emit")
async def pulse_emit(request: Request):
    """Emit a new local core_brain and optionally broadcast it to peers."""
    pulse = await request.json()
    ledger.append(pulse, broadcast=True)
    return {"status": "emitted", "mind": pulse}


#if __name__ == "__main__":
#    uvicorn.run("api:app", host="0.0.0.0", fport=12003)