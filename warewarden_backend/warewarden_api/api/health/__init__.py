from fastapi import APIRouter

from .views import router as health_router

router = APIRouter()
router.include_router(router=health_router)
