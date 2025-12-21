from fastapi import APIRouter
from .health import router as health_router
from .version import router as version_router

router = APIRouter()
router.include_router(health_router)
router.include_router(version_router)
