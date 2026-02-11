from fastapi import APIRouter
from app.models.sensor_models import SensorPayload
from app.services.alert_service import evaluate_alerts
from app.services.prediction_service import predict_congestion

router = APIRouter()

@router.post("/ingest")
def ingest_sensor_data(payload: SensorPayload):
    alerts = evaluate_alerts(payload)
    congestion_level = predict_congestion(payload)

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
