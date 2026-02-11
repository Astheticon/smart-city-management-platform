from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class Alert(BaseModel):
    alert_type: Literal["TRAFFIC", "AQI", "TEMPERATURE", "HUMIDITY"]
    priority: Literal["HIGH", "LOW"]
    message: str
    value: float
    timestamp: datetime
