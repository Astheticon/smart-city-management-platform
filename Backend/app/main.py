from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.ingest import router as ingest_router

app = FastAPI(
    title="Smart City Management Platform",
    version="1.0"
)

app.include_router(health_router)
app.include_router(ingest_router)
