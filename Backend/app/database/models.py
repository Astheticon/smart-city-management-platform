from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database.db import Base


class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String)
    timestamp = Column(DateTime)

    vehicle_count = Column(Integer)
    traffic_density = Column(Float)

    aqi = Column(Integer)
    temperature = Column(Float)
    humidity = Column(Float)


class AlertDB(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    alert_type = Column(String)
    priority = Column(String)
    message = Column(String)
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
