#include <DHT.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* server = "http://YOUR_INFLUXDB_SERVER/write?db=iotdb";

void setup() {
    Serial.begin(115200);
    dht.begin();
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to Wi-Fi...");
    }
}

void loop() {
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    if (WiFi.status() == WL_CONNECTED) {
        WiFiClient client;
        HTTPClient http;
        String postData = "temperature_sensor temperature=" + String(temperature) + ",humidity=" + String(humidity);
        http.begin(client, server);
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");
        http.POST(postData);
        http.end();
    }

    delay(5000);
}
