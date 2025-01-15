from fastapi import APIRouter

from .schemas import Health

router = APIRouter(tags=["Healthcheck"])


@router.get("/", response_model=Health)
async def check_health() -> Health:
    return Health(status="OK")
