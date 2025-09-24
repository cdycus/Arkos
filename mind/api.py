
from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/pulse")
def pulse():
    return {"pulse": f"alive-{int(time.time())}"}
