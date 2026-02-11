from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class TrafficData(BaseModel):
    vehicle_count: int
    traffic_density: float


class EnvironmentData(BaseModel):
    aqi: float
    temperature: float
    humidity: float


class SensorPayload(BaseModel):
    source: Literal["simulator", "hardware"]
    timestamp: datetime
    traffic: TrafficData
    environment: EnvironmentData
