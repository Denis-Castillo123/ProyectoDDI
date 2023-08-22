from machine import Pin, I2C, sleep, PWM
import network
import utime
import math
from mpu6050 import init_mpu6050, get_mpu6050_data
import time
import VL53L0X
from umqtt.simple import MQTTClient
import json

#Hacemos las configuraciones de MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_1 = "hasp/plate/command/p2b13.text"
MQTT_TOPIC_10 = "hasp/plate/command/p2b13.val"
MQTT_TOPIC_3 = "hasp/plate/command/p1b14.text"
MQTT_TOPIC_6 = "hasp/plate/command/p1b12.src"
MQTT_TOPIC_4 = "hasp/plate/command/p1b3.val"
MQTT_TOPIC_5 = "hasp/plate/command/p1b3.line_color10"
MQTT_TOPIC_7 = "hasp/plate/command/p1b15.text"
MQTT_TOPIC_2 = "utgn/equipo1/distancia"
MQTT_PORT = 1883
sta_if = network.WLAN(network.STA_IF)

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
# Configuración del bus I2C (puede variar según tu hardware)
i2c2 = I2C(scl=Pin(2), sda=Pin(4), freq=400000)
# Inicializar el sensor VL53L0X
tof = VL53L0X.VL53L0X(i2c2)
init_mpu6050(i2c)
buzzer_pin = Pin(25,Pin.OUT)
pwm_buzzer = PWM(buzzer_pin)
pwm_buzzer.deinit()
led = Pin(5,Pin.OUT)

# funcion para conectar a la red wifi
def wifi_connect():
    print("Conectando ...", end = "")
    sta_if.active(True)
    sta_if.connect('HUAWEI Y9a','9960abcd')

    while not sta_if.isconnected():
        print(".", end = "")
        utime.sleep(0.3)
    print("Wifi conectado!")

# Funcion de publicador de MQTT
def publishValor(tempValor):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            print("[OK]")
            client.publish(MQTT_TOPIC_4,str(tempValor))
            print("Publicando Valor: ",tempValor )
            utime.sleep(0.1)
        else:
            wifi_connect()
    except:
        print("Reconectando...3")
# Funcion de publicador de MQTT
def publishText(tempText):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            print("[OK]")
            client.publish(MQTT_TOPIC_3,str(tempText))
            print("Publicando Text: ",tempText )
            utime.sleep(0.1)
        else:
            wifi_connect()
    except:
        print("Reconectando...4")
#Funcion de publicador de MQTT Colore
def publishColor(tempColor):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            client.publish(MQTT_TOPIC_5,str(tempColor))
            print("Publicando Color: ",tempColor )
            utime.sleep(0.1)
        else:
            wifi_connect()
    except:
        print("Reconectando...5")


def publishDistancia(distancia):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            client.publish(MQTT_TOPIC_7,distancia)
            print("Publicando distancia: ",distancia)
            utime.sleep(0.1)
        else:
            wifi_connect()
    except:
        print("Reconectando...7")
        
def publishPasos(pasos):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            client.publish(MQTT_TOPIC_1,pasos)
            print("Publicando pasos: ",pasos)
            utime.sleep(0.1)
        else:
            wifi_connect()
    except:
        print("Reconectando...7")
 
def publishDistVal(distVal):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            
            client.publish(MQTT_TOPIC_2,str(distVal))
            print("Publicando distanciaVal: ",distVal) 
            utime.sleep(0.1)
        else:
            wifi_connect()
    except:
        print("Reconectando...7")
        

# Programa principal
wifi_connect()

# Función para reproducir un tono en una frecuencia dada y volumen dado
def play_tone(frequency, duration, volume):
    pwm_buzzer.freq(int(frequency))
    pwm_buzzer.duty(int(volume * 1023))  # El volumen se ajusta entre 0 y 1
    time.sleep(duration)
    pwm_buzzer.duty(0)
    time.sleep(0.1)

def alertSound():
    pwm_buzzer.init()
    # Definición de frecuencias para simular la palabra "cuidado"
    cuidado_melody = [
        (659, 0.2, 0.2),  # Nota C5 con volumen de 0.3
        (523, 0.3, 0.3),  # Nota C5 con volumen de 0.3
    ]
    for note in cuidado_melody:
        play_tone(note[0], note[1], note[2])
    pwm_buzzer.deinit()

def calculate_tilt_angles(accel_data):
    x, y, z = accel_data['x'], accel_data['y'], accel_data['z']
 
    tilt_x = math.atan2(y, math.sqrt(x * x + z * z)) * 180 / math.pi
    tilt_y = math.atan2(-x, math.sqrt(y * y + z * z)) * 180 / math.pi
    tilt_z = math.atan2(z, math.sqrt(x * x + y * y)) * 180 / math.pi
 
    return tilt_x, tilt_y, tilt_z
 
def complementary_filter(pitch, roll, gyro_data, dt, alpha=0.98):
    pitch += gyro_data['x'] * dt
    roll -= gyro_data['y'] * dt
 
    pitch = alpha * pitch + (1 - alpha) * math.atan2(gyro_data['y'], math.sqrt(gyro_data['x'] * gyro_data['x'] + gyro_data['z'] * gyro_data['z'])) * 180 / math.pi
    roll = alpha * roll + (1 - alpha) * math.atan2(-gyro_data['x'], math.sqrt(gyro_data['y'] * gyro_data['y'] + gyro_data['z'] * gyro_data['z'])) * 180 / math.pi
 
    return pitch, roll
 
pitch = 0
roll = 0
prev_time = utime.ticks_ms()
 # Variables para detección de pasos
threshold = 3  # Umbral para detectar picos
last_accel_z = 0
step_count = 0
colorDistamcia = "" 

while True:
    distance = tof.read()  # Leer la distancia en milímetros
    print("Distancia: {} cm".format(distance/10))
    
    if distance/10<=100:
        alertSound()
        colorDistamcia = "red"
    if distance/10>100:
        colorDistamcia = "green"
        #publishAlert("jsonl {'id':15,'obj':'msgbox','text':'¡Objeto cercano!', 'auto_close': '3000'}")
    data = get_mpu6050_data(i2c)
    curr_time = utime.ticks_ms()
    dt = (curr_time - prev_time) / 1000
 
    tilt_x, tilt_y, tilt_z = calculate_tilt_angles(data['accel'])
    
    
    prev_time = curr_time

    #print("diferencia: {:.2f}".format(tilt_z - last_accel_z))
    if tilt_z - last_accel_z > threshold:
        step_count += 1
        print("Paso detectado - Total de pasos:", step_count)
        
    last_accel_z = tilt_z
    if data['temp']>=32:
        color = "red"
    if data['temp']<=12:
        color = "blue"
    if data['temp']<32 and data['temp']>12:
        color = "green"
    #publishText("{} pasos".format(step_count), "{} cm".format(distance/10), "{:.2f}\u00B0C C".format(data['temp']),color,"{:.2f}".format(data['temp']))
    publishText("{:.2f}\u00B0C C".format(data['temp']))
    publishValor("{:.2f}".format(data['temp']))
    publishColor(color)
    publishDistancia("{} cm".format(distance/10))
    publishDistVal(round(distance/10,2))
    publishPasos("{} pasos".format(step_count))
    utime.sleep(0.1) 
    # Delay for 1 seconds
    utime.sleep(1)

