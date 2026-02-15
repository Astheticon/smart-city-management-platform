from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import SensorData, AlertDB

router = APIRouter()


@router.get("/latest")
def get_latest():
    db: Session = SessionLocal()

    latest_record = (
        db.query(SensorData)
        .order_by(SensorData.id.desc())
        .first()
    )

    db.close()

    if not latest_record:
        return {"message": "No data available"}

    return latest_record


@router.get("/history")
def get_history(limit: int = Query(10, ge=1)):
    db: Session = SessionLocal()

    records = (
        db.query(SensorData)
        .order_by(SensorData.id.desc())
        .limit(limit)
        .all()
    )

    db.close()
    return records


@router.get("/alerts")
def get_alerts(limit: int = Query(10, ge=1)):
    db: Session = SessionLocal()

    alerts = (
        db.query(AlertDB)
        .order_by(AlertDB.id.desc())
        .limit(limit)
        .all()
    )

    db.close()
    return alerts
