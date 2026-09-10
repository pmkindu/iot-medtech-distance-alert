#define TRIG_PIN 9
#define ECHO_PIN 10
#define LED_GREEN 2
#define LED_RED 3

// Schwellenwert in Zentimetern für die Sicherheitszone
const int WARNING_THRESHOLD_CM = 10;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
}

void loop() {
  // Ultraschall-Impuls senden
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Signallaufzeit messen
  long duration = pulseIn(ECHO_PIN, HIGH);
  // Distanz berechnen (Schallgeschwindigkeit in Luft ~ 0.034 cm/us)
  int distance = duration * 0.034 / 2;

  String status = "SAFE";
  
  if (distance > 0 && distance < WARNING_THRESHOLD_CM) {
    status = "WARNING";
    digitalWrite(LED_RED, HIGH);
    digitalWrite(LED_GREEN, LOW);
  } else {
    digitalWrite(LED_GREEN, HIGH);
    digitalWrite(LED_RED, LOW);
  }

  // Strukturierte Telemetrie als JSON über Serial senden
  Serial.print("{\"distance_cm\": ");
  Serial.print(distance);
  Serial.print(", \"status\": \"");
  Serial.print(status);
  Serial.println("\"}");

  delay(500); // 2 Hz Messfrequenz
}