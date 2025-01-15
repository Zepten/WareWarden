from fastapi import APIRouter

from .v1 import router as api_v1_router
from .health import router as health_router

from core.config import settings

router = APIRouter()
router.include_router(router=api_v1_router, prefix=settings.api.v1.prefix)
router.include_router(router=health_router, prefix=settings.api.health)


@router.get("/", tags=["API root"])
async def root():
    return {
        "message": "WareWarden API",
    }
