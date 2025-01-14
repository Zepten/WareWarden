from fastapi import APIRouter, Depends, status

from .schemas import Healthcheck

router = APIRouter(tags=["Healthcheck"])

@router.get("/", response_model=Healthcheck)
async def check_health() -> Healthcheck:
    return Healthcheck(status="OK")
