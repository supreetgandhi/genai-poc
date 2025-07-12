from fastapi import APIRouter, Request
from services.rpa_trigger import trigger_rpa

router = APIRouter()

@router.post("/rpa/trigger/{action}")
def rpa_trigger(action: str, param: str):
    result = trigger_rpa(action, param)
    return {"message": result}