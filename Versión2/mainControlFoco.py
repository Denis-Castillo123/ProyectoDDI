from machine import Pin
import time
import network
from umqtt.simple import MQTTClient

relay_pin = 4  # GPIO pin number connected to the relay

# Setup the relay pin as an output
relay = Pin(relay_pin, Pin.OUT)

# WiFi configuration
WIFI_SSID = "HUAWEI Y9a"
WIFI_PASSWORD = "9960abcd"

# MQTT configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = b"hasp/plate/command/p2b14.text"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print("WiFi connected.")
    print("Network config:", sta_if.ifconfig())

def on_message(topic, message):
    print("Received MQTT message on topic:", topic)
    print("Message payload:", message)
    if topic == MQTT_TOPIC:
        if message == b"0":
            # Turn on the relay
            relay.value(0)
            print("Current Flowing")
        else:
            # Turn off the relay
            relay.value(1)
            print("Current not Flowing")

# Connect to WiFi
connect_wifi()

# Connect to MQTT broker
client = MQTTClient("", MQTT_BROKER)
client.set_callback(on_message)
client.connect()
client.subscribe(MQTT_TOPIC)

try:
    while True:
        client.wait_msg()
except KeyboardInterrupt:
    print("\nDisconnected from MQTT broker.")
    client.disconnect()
