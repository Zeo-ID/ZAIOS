from fastapi import APIRouter
from .health import router as health_router
from .version import router as version_router

router = APIRouter()
router.include_router(health_router, prefix="/health", tags=["system"])
router.include_router(version_router, prefix="/version", tags=["system"])
