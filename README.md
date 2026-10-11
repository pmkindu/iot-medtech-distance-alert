# IoT MedTech Distance Alert System 🩺📏

Professional-grade, containerized IoT MedTech Telemetry API with automated BDD testing and CI/CD orchestration.

---

## 🛠️ Hardware Setup & Wiring

The following circuit diagram shows the hardware configuration of the MedTech distance monitoring prototype:

![Hardware Schematic](hardware_schema.png)

### Components:
- **Microcontroller:** Arduino Uno 
- **Sensor:** HC-SR04 Ultrasonic Sensor (distance measurement)
- **Alert Signaling:** Red LED & Green LED (with current-limiting resistors)
- **Breadboard & Jumper Wires**

### Pinout Mapping:
| Component | Sensor / Component Pin | Arduino Pin | Function |
| :--- | :--- | :--- | :--- |
| **HC-SR04 Sensor** | VCC | `5V` | Power Supply |
| | TRIG | Digital Pin | Trigger Signal (pulse start) |
| | ECHO | Digital Pin | Echo Signal (travel time measurement) |
| | GND | `GND` | Ground |
| **LEDs & Resistors** | Red LED (Warning) | Digital Pin (PWM) | Alert signal for unsafe distance / proximity |
| | Green LED (Status) | Digital Pin (PWM) | Normal operation / status indicator |

---

## 🏗️ Architecture Overview

- **Backend API:** FastAPI (Python 3.10+)
- **Hardware Abstraction Layer (HAL):** Supports physical `HARDWARE` serial inputs and automated `MOCK` telemetry mode.
- **Test Automation:** Behavior-Driven Development (BDD) via Behave (Gherkin syntax) & Pytest.
- **Orchestration:** Docker & Docker Compose.
- **CI/CD:** GitHub Actions automated test runner.

---

## 🚀 Running Locally with Docker Compose

```bash
docker compose up --build --exit-code-from bdd-test-runner
```
---
## 📁 Project Structure

```text
iot-medtech-distance-alert/
├── 📂 .github/
│   └── 📂 workflows/             # GitHub Actions CI/CD pipeline definition
├── 📂 features/                  # Gherkin feature files & Behave step definitions
├── 📂 firmware/                  # Embedded Arduino/C++ sensor logic
├── 🖼️ hardware_schema.png         # Hardware circuit diagram (Arduino Uno & HC-SR04)
├── 📄 Dockerfile                 # Multi-stage container build definition
├── 📄 docker-compose.yml         # Multi-container service orchestration
├── 📄 main.py                    # FastAPI application entry point
├── 📄 requirements.txt           # Python dependencies
└── 📄 sensor_reader.py           # HAL layer for serial telemetry & mocking
```