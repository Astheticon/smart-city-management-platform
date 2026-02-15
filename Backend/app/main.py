from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.ingest import router as ingest_router
from app.routes import analytics

from fastapi.middleware.cors import CORSMiddleware


from app.database.db import engine
from app.database import models as db_models

app = FastAPI(
    title="Smart City Management Platform",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_models.Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(ingest_router)
app.include_router(analytics.router)
