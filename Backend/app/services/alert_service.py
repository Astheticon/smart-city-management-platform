from datetime import datetime
from typing import List

from app.models.sensor_models import SensorPayload
from app.models.alert_models import Alert


def evaluate_alerts(payload: SensorPayload) -> List[Alert]:
    alerts: List[Alert] = []
    now = datetime.utcnow()

    # 🚦 Traffic Alerts (HIGH priority)
    if payload.traffic.traffic_density >= 85:
        alerts.append(Alert(
            alert_type="TRAFFIC",
            priority="HIGH",
            message="Critical traffic congestion detected",
            value=payload.traffic.traffic_density,
            timestamp=now
        ))
    elif payload.traffic.traffic_density >= 70:
        alerts.append(Alert(
            alert_type="TRAFFIC",
            priority="HIGH",
            message="High traffic congestion detected",
            value=payload.traffic.traffic_density,
            timestamp=now
        ))

    # 🌫️ AQI Alerts (HIGH priority)
    if payload.environment.aqi > 400:
        alerts.append(Alert(
            alert_type="AQI",
            priority="HIGH",
            message="Severe air quality detected",
            value=payload.environment.aqi,
            timestamp=now
        ))
    elif payload.environment.aqi > 150:
        alerts.append(Alert(
            alert_type="AQI",
            priority="HIGH",
            message="Poor air quality detected",
            value=payload.environment.aqi,
            timestamp=now
        ))

    # 🌡️ Temperature Alerts (HIGH priority)
    if payload.environment.temperature > 40:
        alerts.append(Alert(
            alert_type="TEMPERATURE",
            priority="HIGH",
            message="High temperature warning",
            value=payload.environment.temperature,
            timestamp=now
        ))

    # 💧 Humidity Alerts (LOW priority)
    if payload.environment.humidity < 30:
        alerts.append(Alert(
            alert_type="HUMIDITY",
            priority="LOW",
            message="Low humidity detected",
            value=payload.environment.humidity,
            timestamp=now
        ))
    elif payload.environment.humidity > 70:
        alerts.append(Alert(
            alert_type="HUMIDITY",
            priority="LOW",
            message="High humidity detected",
            value=payload.environment.humidity,
            timestamp=now
        ))

    return alerts
