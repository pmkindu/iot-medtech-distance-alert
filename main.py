import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from sensor_reader import SensorReader

app = FastAPI(title="IoT MedTech Distance Alert API", version="1.0.0")
sensor = SensorReader()

html_dashboard = """
<!DOCTYPE html>
<html>
    <head>
        <title>MedTech Live Telemetry</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background: #121212; color: white; }
            .card { display: inline-block; padding: 30px; border-radius: 12px; background: #1e1e1e; min-width: 300px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
            .distance { font-size: 60px; font-weight: bold; margin: 20px 0; }
            .status { font-size: 24px; padding: 8px 16px; border-radius: 6px; display: inline-block; font-weight: bold; }
            .SAFE { background-color: #2e7d32; color: white; }
            .WARNING { background-color: #c62828; color: white; animation: blink 1s infinite; }
            @keyframes blink { 50% { opacity: 0.5; } }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Live MedTech Telemetry</h2>
            <div id="distance" class="distance">-- cm</div>
            <div id="status" class="status SAFE">CONNECTING</div>
            <p id="mode" style="color: #aaa; margin-top: 20px;"></p>
        </div>
        <script>
            const ws = new WebSocket("ws://" + location.host + "/ws/telemetry");
            ws.onmessage = function(event) {
                const data = JSON.parse(event.data);
                document.getElementById("distance").innerText = data.distance_cm + " cm";
                
                const statusEl = document.getElementById("status");
                statusEl.innerText = data.status;
                statusEl.className = "status " + data.status;
                
                document.getElementById("mode").innerText = "Mode: " + data.mode;
            };
        </script>
    </body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    return html_dashboard

@app.get("/health")
def health_check():
    return {"status": "HEALTHY", "sensor_mode": "MOCK" if sensor.is_mock else "HARDWARE"}

@app.get("/telemetry")
def get_telemetry():
    return sensor.read_telemetry()

@app.websocket("/ws/telemetry")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = sensor.read_telemetry()
            await websocket.send_json(data)
            await asyncio.sleep(0.3)  # Sendet alle 300ms neue Daten
    except WebSocketDisconnect:
        print("Client disconnected from WebSocket")