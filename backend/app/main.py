from fastapi import FastAPI
from app.api.v1 import router as api_v1_router

app = FastAPI(
    title="ZAIOS Pro",
    version="0.1.0",
    description="Zentralisiertes Management-System für IT, HR und Services"
)

app.include_router(api_v1_router, prefix="/api/v1")
