from fastapi import APIRouter

from .pcs.views import router as pcs_router

from core.config import settings

router = APIRouter()
router.include_router(router=pcs_router, prefix=settings.api.v1.pcs)


@router.get("/", tags=["API v1 root"])
async def root():
    return {
        "message": "WareWarden API",
        "version": "0.1.0",
    }
