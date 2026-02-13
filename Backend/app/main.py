from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.ingest import router as ingest_router

from app.database.db import engine
from app.database import models as db_models

app = FastAPI(
    title="Smart City Management Platform",
    version="1.0"
)

db_models.Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(ingest_router)
