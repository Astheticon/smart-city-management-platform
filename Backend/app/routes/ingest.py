from fastapi import APIRouter

from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.database.models import SensorData, AlertDB

from app.models.sensor_models import SensorPayload
from app.services.alert_service import evaluate_alerts
from app.services.prediction_service import predict_congestion

router = APIRouter()

@router.post("/ingest")
def ingest_sensor_data(payload: SensorPayload):
    db: Session = SessionLocal()

    # Store sensor data
    sensor_record = SensorData(
        source=payload.source,
        timestamp=payload.timestamp,
        vehicle_count=payload.traffic.vehicle_count,
        traffic_density=payload.traffic.traffic_density,
        aqi=payload.environment.aqi,
        temperature=payload.environment.temperature,
        humidity=payload.environment.humidity
    )

    db.add(sensor_record)
    db.commit()

    # Generate alerts
    alerts = evaluate_alerts(payload)
    congestion_level = predict_congestion(payload)

    # Store alerts
    for alert in alerts:
        alert_record = AlertDB(
        alert_type=alert.alert_type,
        priority=alert.priority,
        message=alert.message,
        value=alert.value
    )
    db.add(alert_record)


    db.commit()
    db.close()

    return {
        "status": "success",
        "message": "Sensor data received successfully",
        "source": payload.source,
        "timestamp": payload.timestamp,
        "prediction": {
            "traffic_congestion_level": congestion_level
        },
        "alerts": alerts
    }
