from fastapi import APIRouter

from .pcs.views import router as pcs_router

from core.config import settings

router = APIRouter()
router.include_router(router=pcs_router, prefix=settings.api.v1.pcs)
