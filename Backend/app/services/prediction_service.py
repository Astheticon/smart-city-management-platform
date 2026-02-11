from app.models.sensor_models import SensorPayload


def predict_congestion(payload: SensorPayload) -> str:
    density = payload.traffic.traffic_density

    if density < 40:
        return "LOW"
    elif density < 70:
        return "MEDIUM"
    else:
        return "HIGH"
