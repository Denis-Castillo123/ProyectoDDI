from machine import Pin, ADC, PWM
import network
from umqtt.simple import MQTTClient
import time
import utime

#Hacemos las configuraciones de MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
#Nombre tpico fotorres
MQTT_TOPIC_3 = "hasp/plate/command/p2b14.text"
#Nombre topico pulso
MQTT_TOPIC_4 = "hasp/plate/command/p1b16.text"
MQTT_PORT = 1883
sta_if = network.WLAN(network.STA_IF)

# funcion para conectar a la red wifi
def wifi_connect():
    print("Conectando ...", end = "")
    sta_if.active(True)
    sta_if.connect('HUAWEI Y9a','9960abcd')

    while not sta_if.isconnected():
        print(".", end = "")
        time.sleep(0.3)
    print("Wifi conectado!")

# Funcion de publicador de MQTT
def publishLuz(luz):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            print("[OK]")
            client.publish(MQTT_TOPIC_3,str(luz))
            print("Publicando luz: ",luz )
        else:
            wifi_connect()
    except:
        print("Reconectando...")

# Funcion de publicador de MQTT
def publishBPM(bpm):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            print("[OK]")
            client.publish(MQTT_TOPIC_4,bpm)
            print("Publicando valor de pulsometro: ",bpm )
        else:
            wifi_connect()
    except:
        print("Reconectando...")
        
# Programa principal
wifi_connect()

# Variables fotoresistencia
fotoresistencia = 4
azul = 18
verde = 21
rojo = 19

led_rojo = Pin(rojo, Pin.OUT)
led_verde = Pin(verde, Pin.OUT)
led_azul = Pin(azul, Pin.OUT)
fotoresistencia = Pin(fotoresistencia, Pin.IN)

# Variables para el sonido del piezo
piezo_pin = PWM(Pin(5))  # Cambia el número del pin por el que estés usando
frequency = 1000  # Frecuencia en Hz
duration = 700   # Duración del sonido en milisegundos

def play_piezo(frequency, duration):
    piezo_pin.freq(frequency)
    piezo_pin.duty(512)  # Valor de duty cycle para encender el piezo (puede variar según la placa)
    utime.sleep_ms(duration)
    piezo_pin.duty(0)    # Apaga el piezo

try:
    piezo_pin.duty(0)  # Apagar el piezo al inicio
    while True:
        promediobmp = 0
        for i in range(30):
            # Leer el valor de la fotoresistencia
            luz = fotoresistencia.value()
            # Encender o apagar los LEDs según la luz
            if luz:
                led_rojo.on()
                led_verde.off()
                led_azul.off()
            else:
                led_rojo.off()
                led_verde.on()
                led_azul.off()

            pin_adc = Pin(32)  # Cambiar el número de pin según la configuración física
            adc = ADC(pin_adc)
            MAX_HISTORY = 250

            history = []
            contador_pulsos = 0
            tiempo_inicio = time.ticks_ms()

            duracion_medicion = 1
            while time.ticks_ms() - tiempo_inicio < duracion_medicion * 1000:
                v = adc.read()

                history.append(v)
                history = history[-MAX_HISTORY:]

                minima, maxima = min(history), max(history)

                threshold_on = (minima + maxima * 3) // 4
                threshold_off = (minima + maxima) // 2

                if v > threshold_on:
                    contador_pulsos += 1

                if v < threshold_off:
                    contador_pulsos += 1
                time.sleep_ms(10)
            
            promediobmp = promediobmp + contador_pulsos
            publishLuz(str(luz))
            
        bpm_avg = promediobmp / 30
        print("bmp:", bpm_avg)
        
        if bpm_avg < 70:
            play_piezo(frequency, duration)
            print("Reproduciendo sonido debido a BPM menor a 60")
        else:
            piezo_pin.duty(0)  # Apagar el piezo si bpm_avg es mayor o igual a 60
            
        publishBPM(str(round(bpm_avg, 2)))
except KeyboardInterrupt:
    led_rojo.off()
    led_verde.off()
    led_azul.off()
    piezo_pin.duty(0)
