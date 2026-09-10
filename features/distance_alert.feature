@medtech @telemetry
Feature: MedTech Distance Alert System Telemetry and Health Checks
  As a medical device operator
  I want to monitor telemetry data and system health
  So that patient safety boundaries are strictly enforced and monitored

  @health @smoke
  Scenario: Verify API Health Check Status
    Given the MedTech API is running
    When I send a GET request to "/health"
    Then the response status code should be 200
    And the response JSON should contain "status" as "HEALTHY"
    And the response JSON should contain key "sensor_mode"

  @api @regression
  Scenario: Read Valid Telemetry Data Structure
    Given the MedTech API is running
    When I send a GET request to "/telemetry"
    Then the response status code should be 200
    And the response JSON should contain key "distance_cm"
    And the response JSON should contain key "status"
    And the response JSON should contain key "mode"

  @boundary @safety
  Scenario Outline: Validate Distance Alert Safety Boundaries
    Given the MedTech API is running
    When the sensor reads a distance of <distance> cm
    Then the safety status in telemetry should be "<expected_status>"

    Examples:
      | distance | expected_status |
      | 5        | WARNING         |
      | 8        | WARNING         |
      | 10       | SAFE            |
      | 25       | SAFE            |