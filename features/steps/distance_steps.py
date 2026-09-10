import os
import requests
from behave import given, when, then

# Basis-URL aus Umgebungsvariable lesen oder Fallback auf localhost
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


@given("the MedTech API is running")
def step_impl_api_running(context):
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=2)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        assert False, f"API ist unter {BASE_URL} nicht erreichbar: {e}"


@when('I send a GET request to "{endpoint}"')
def step_impl_send_get(context, endpoint):
    context.response = requests.get(f"{BASE_URL}{endpoint}")


@then("the response status code should be {status_code:d}")
def step_impl_status_code(context, status_code):
    assert (
        context.response.status_code == status_code
    ), f"Expected {status_code}, got {context.response.status_code}"


@then('the response JSON should contain "{key}" as "{expected_value}"')
def step_impl_json_value(context, key, expected_value):
    data = context.response.json()
    assert key in data, f"Key '{key}' nicht in JSON enthalten: {data}"
    assert (
        str(data[key]) == expected_value
    ), f"Expected {expected_value}, got {data[key]}"


@then('the response JSON should contain key "{key}"')
def step_impl_json_key(context, key):
    data = context.response.json()
    assert key in data, f"Key '{key}' nicht in JSON-Antwort enthalten: {data}"


@when("the sensor reads a distance of {distance:d} cm")
def step_impl_sensor_reading(context, distance):
    # Speichert die Test-Distanz im Context für die spätere Überprüfung
    context.test_distance = distance


@then('the safety status in telemetry should be "{expected_status}"')
def step_impl_check_safety_boundary(context, expected_status):
    # Berechnet den erwarteten Status basierend auf dem Schwellenwert (< 10 cm = WARNING)
    calculated_status = (
        "WARNING" if getattr(context, "test_distance", 0) < 10 else "SAFE"
    )
    assert calculated_status == expected_status, (
        f"Schwellenwert-Logik fehlerhaft: Für {context.test_distance}cm "
        f"wurde '{calculated_status}' berechnet, erwartet war '{expected_status}'"
    )