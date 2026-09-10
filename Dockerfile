FROM python:3.10-slim

WORKDIR /app

# System-Abhängigkeiten installieren (curl für Healthchecks)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY . .

# Server-Port freigeben
EXPOSE 8000

# FastAPI Server starten
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]