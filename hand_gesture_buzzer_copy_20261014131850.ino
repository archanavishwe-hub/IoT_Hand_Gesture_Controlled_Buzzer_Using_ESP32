#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "vivo Y19s 5G";
const char* password = "11112006";

#define BUZZER_PIN 13

WebServer server(80);

void buzzerOn() {
  digitalWrite(BUZZER_PIN, HIGH);
  server.send(200, "text/plain", "BUZZER ON");
}

void buzzerOff() {
  digitalWrite(BUZZER_PIN, LOW);
  server.send(200, "text/plain", "BUZZER OFF");
}

void setup() {

  Serial.begin(115200);

  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected!");

  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/buzzer/on", buzzerOn);
  server.on("/buzzer/off", buzzerOff);

  server.begin();

  Serial.println("Server Started");
}

void loop() {
  server.handleClient();
}