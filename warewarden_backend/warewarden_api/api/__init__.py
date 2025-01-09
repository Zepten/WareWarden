from fastapi import APIRouter

from .v1 import router as api_v1_router

from core.config import settings

router = APIRouter()
router.include_router(router=api_v1_router, prefix=settings.api.v1.prefix)


@router.get("/", tags=["API root"])
async def root():
    return {
        "message": "WareWarden API",
    }
