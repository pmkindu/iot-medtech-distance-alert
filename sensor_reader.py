import os
import json
import random

class SensorReader:
    def __init__(self, port=None, baudrate=9600):
        self.port = port or os.getenv("SERIAL_PORT", "MOCK")
        self.baudrate = baudrate
        self.serial_conn = None
        self.is_mock = self.port == "MOCK"

        if not self.is_mock:
            try:
                import serial
                self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            except Exception as e:
                print(f"[WARN] Serial connection failed ({e}). Falling back to MOCK mode.")
                self.is_mock = True

    def read_telemetry(self):
        if self.is_mock:
            mock_distance = random.choice([5, 12, 25, 40])
            status = "WARNING" if mock_distance < 10 else "SAFE"
            return {"distance_cm": mock_distance, "status": status, "mode": "MOCK"}

        try:
            line = self.serial_conn.readline().decode('utf-8').strip()
            if line:
                data = json.loads(line)
                data["mode"] = "HARDWARE"
                return data
        except Exception as e:
            print(f"[ERROR] Failed to read serial data: {e}")
        
        return {"distance_cm": -1, "status": "ERROR", "mode": "HARDWARE"}