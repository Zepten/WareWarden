from fastapi import APIRouter

from .views import router as healthcheck_router

router = APIRouter()
router.include_router(router=healthcheck_router)
