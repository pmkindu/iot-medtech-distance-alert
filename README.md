Professional-grade, containerized IoT MedTech Telemetry API with automated BDD testing and CI/CD orchestration.

## Architecture Overview
- **Backend API:** FastAPI (Python 3.10+)
- **Hardware Abstraction Layer (HAL):** Supports physical `HARDWARE` serial inputs and automated `MOCK` telemetry mode.
- **Test Automation:** Behavior-Driven Development (BDD) via Behave (Gherkin syntax) & Pytest.
- **Orchestration:** Docker & Docker Compose.
- **CI/CD:** GitHub Actions automated test runner.

## Running Locally with Docker Compose
```bash
docker compose up --build --exit-code-from bdd-test-runner
├── .github/workflows/   # GitHub Actions CI/CD pipeline definition
├── features/            # Gherkin feature files & Behave step definitions
├── firmware/            # Embedded Arduino/C++ sensor logic
├── main.py              # FastAPI application entry point
├── sensor_reader.py     # HAL layer for serial telemetry & mocking
├── Dockerfile           # Multi-stage container build definition
└── docker-compose.yml   # Multi-container service orchestration
EOF