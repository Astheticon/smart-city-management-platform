import time
import random
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000/ingest"


def generate_sensor_data():
    return {
        "source": "simulator",
        "timestamp": datetime.utcnow().isoformat(),
        "traffic": {
            "vehicle_count": random.randint(20, 200),
            "traffic_density": random.randint(10, 95)
        },
        "environment": {
            "aqi": random.randint(50, 350),
            "temperature": random.randint(25, 45),
            "humidity": random.randint(20, 80)
        }
    }


def send_data():
    payload = generate_sensor_data()
    try:
        response = requests.post(API_URL, json=payload)
        print("Sent:", payload)
        print("Response:", response.json())
    except Exception as e:
        print("Error sending data:", e)


if __name__ == "__main__":
    print("Starting IoT data simulator...")
    while True:
        send_data()
        time.sleep(5)