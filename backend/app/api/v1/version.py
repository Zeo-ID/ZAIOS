from fastapi import APIRouter

router = APIRouter(tags=["System"])

@router.get("/version")
def version():
    return {
        "name": "ZAIOS Pro",
        "version": "0.1.0",
        "api": "v1"
    }

