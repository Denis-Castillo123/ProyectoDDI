#include <WiFi.h>
#include <PubSubClient.h>
#include <vector>
#include <SPI.h>
#include <SD.h>
#include <FS.h>
#include "ESP32_SPI_9341.h"

// Información de la red WiFi
const char* ssid = "HUAWEI Y9a";
const char* password = "9960abcd";

// Información del broker MQTT
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;
const char* mqtt_user = "";
const char* mqtt_password = "";

// Cliente WiFi y Cliente MQTT
WiFiClient espClient;
PubSubClient client(espClient);

// Pantalla
#define SD_SCK 18
#define SD_MISO 19
#define SD_MOSI 23
#define SD_CS 5

#define LIGHT_ADC 34

int led_pin[3] = {17, 4, 16};

SPIClass SD_SPI;

LGFX lcd;

// Función de callback para recibir mensajes MQTT
void callback(char* topic, byte* payload, unsigned int length) {
  // Procesa el mensaje recibido
  Serial.print("Mensaje recibido: ");
  lcd.clear();
  lcd.fillScreen(TFT_WHITE);
  lcd.setTextColor(TFT_BLACK);
  /*
  for (int i = 0; i < length; i++) {
      char charNumero[2] = {(char)payload[i], '\0'};  // Convertir el carácter en una cadena
  
  int numero = atoi(charNumero);
      if (numero >=86) {
    // Rojo
      lcd.clear();
      lcd.fillScreen(TFT_RED);
      lcd.setTextColor(TFT_WHITE);
          // Inadecuado
            lcd.setTextSize(3); 
  lcd.setCursor(5, 200);
  lcd.print("Inadecuado");
  } else if (numero >= 70 && numero <=84) {

    // Amarillo
      lcd.clear();
      lcd.fillScreen(TFT_YELLOW);
      lcd.setTextColor(TFT_BLACK);
                  lcd.setTextSize(3); 
  lcd.setCursor(5, 200);
  lcd.print("Normal");
  } else if (numero >= 60 && numero <=68){

    // Azul
      lcd.clear();
      lcd.fillScreen(TFT_GREEN);
      lcd.setTextColor(TFT_BLACK);
          // Bueno
                            lcd.setTextSize(3); 
  lcd.setCursor(5, 200);
  lcd.print("Excelente");
  } else if (numero<60){

    // Verde
      lcd.clear();
    lcd.fillScreen(TFT_RED);
    lcd.setTextColor(TFT_BLACK);
        // Excelente
                          lcd.setTextSize(3); 
  lcd.setCursor(5, 200);
  lcd.print("BAJO");
  }
  }
  */
  lcd.setTextSize(3); 
  lcd.setCursor(5, 90);
  lcd.print(" Pulsaciones: \n\n   ");

  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
    lcd.print((char)payload[i]);
  }
  lcd.print(" bpm");
  Serial.println();
  
}

void setup() {
  // Pines
  pinMode(led_pin[0], OUTPUT);
  pinMode(led_pin[1], OUTPUT);
  pinMode(led_pin[2], OUTPUT);

  //Pantalla
  lcd.init();
  lcd.fillScreen(TFT_WHITE);
  lcd.setTextColor(TFT_BLACK);
  lcd.setTextSize(2);

  // Inicializa el puerto serie
  Serial.begin(115200);

  // Conéctate a la red WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conexión WiFi establecida");
  lcd.setCursor(60, 110);
  lcd.println("¡Conectado!");
  // Configura el servidor MQTT
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);

  // Conéctate al broker MQTT
  while (!client.connected()) {
    Serial.println("Conectando al broker MQTT...");
    if (client.connect("ESP32Client", mqtt_user, mqtt_password)) {
      Serial.println("Conexión MQTT establecida");
      lcd.setCursor(60, 70);
      lcd.println("MQTT!");
      client.subscribe("utng/equipo1/pulsometro");
    } else {
      Serial.print("Error de conexión MQTT, rc=");
      Serial.print(client.state());
      Serial.println(" Intentando nuevamente en 5 segundos...");
      delay(5000);
    }
  }
}

void loop() {
  // Mantén la conexión MQTT activa
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void reconnect() {
  // Reconéctate al broker MQTT
  while (!client.connected()) {
    Serial.println("Conectando al broker MQTT...");
    if (client.connect("ESP32Client", mqtt_user, mqtt_password)) {
      Serial.println("Conexión MQTT establecida");
      client.subscribe("utng/equipo1/pulsometro");
    } else {
      Serial.print("Error de conexión MQTT, rc=");
      Serial.print(client.state());
      Serial.println(" Intentando nuevamente en 5 segundos...");
      delay(5000);
    }
  }
}
