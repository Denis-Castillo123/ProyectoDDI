from machine import Pin, ADC
import network
from umqtt.simple import MQTTClient
from time import sleep, time

#Hacemos las configuraciones de MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_3 = "utng/equipo1/fotorres"
MQTT_TOPIC_4 = "utng/equipo1/pulsometro"
MQTT_PORT = 1883
sta_if = network.WLAN(network.STA_IF)

#Limites del pulsometro
MAX_HISTORY = 200
TOTAL_BEATS = 30

#Calcular el BPM (ritmo normal en reposo es de 60 a 100 pulsaciones por minuto.)
def calculate_bpm(beats):
    if beats:
        beat_time = beats[-1] - beats[0]
        if beat_time:
            print("BPM: " + str((len(beats) / (beat_time)) * 60))
            return (len(beats) / (beat_time)) * 60

           
# funcion para conectar a la red wifi
def wifi_connect():
    print("Conectando ...", end = "")
    sta_if.active(True)
    sta_if.connect('HUAWEI Y9a','9960abcd')

    while not sta_if.isconnected():
        print(".", end = "")
        sleep(0.3)
    print("Wifi conectado!")

# Funcion de publicador de MQTT
def publish(luz, bpm):
    try:
        if(sta_if.isconnected()):
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user = MQTT_USER, password = MQTT_PASSWORD, keepalive=30)
            client.connect()
            print("[OK]")
            #client.publish(MQTT_TOPIC_3, valor)
            #print("Publicando: " + valor)
            client.publish(MQTT_TOPIC_3,str(luz))
            print("Publicando luz: ",luz )
            client.publish(MQTT_TOPIC_4,bpm)
            print("Publicando valor de pulsometro: ",bpm )
            sleep(5)
        else:
            wifi_connect()
    except:
        print("Reconectando...")
        
# Programa principal
wifi_connect()

#Variables fotoressitencia
fotoresistencia = 15
azul= 18
verde=21
rojo=19

led_rojo = Pin(rojo, Pin.OUT)
led_verde = Pin(verde, Pin.OUT)
led_azul = Pin(azul, Pin.OUT)
fotoresistencia = Pin(fotoresistencia, Pin.IN)

#Variables pulsometro
adc = ADC(Pin(32))  # Utilizando el pin 32 (ADC1_CH0) como entrada analógica
adc.atten(ADC.ATTN_11DB)  # Configurar atenuación de voltaje si es necesario
# Maintain a log of previous values to
# determine min, max and threshold.
history = []
beats = []
beat = False
bpm = None

try:
    while True:
        # Leer el valor de la fotoresistencia
        luz = fotoresistencia.value()
        
        # Leer el valor del pulsometro
        pulso = adc.read()
        
        # Encender o apagar los LEDs según la luz
        if luz:
            led_rojo.on()
            led_verde.off()
            led_azul.off()
        else:
            led_rojo.off()
            led_verde.on()
            led_azul.off()    
        
        history.append(pulso)
        # Get the tail, up to MAX_HISTORY length
        history = history[-MAX_HISTORY:]
        minima, maxima = min(history), max(history)

        threshold_on = (minima + maxima * 3) // 4   # 3/4
        threshold_off = (minima + maxima) // 2      # 1/2

        if pulso > threshold_on and beat == False:
            beat = True
            beats.append(time())
            # Truncate beats queue to max
            beats = beats[-TOTAL_BEATS:]
            bpm = calculate_bpm(beats)

        if pulso < threshold_off and beat == True:
            beat = False
        #bpm = "Recalculando"
        
        
        #valoresfp = str(luz) + "?" + vBPM
    
        publish(str(luz), "Calculando" if bpm == None else str(round(bpm,2)))
        #Imprimir valores en consola
        print("Valor de la fotoresistencia: ", luz)
        print("Valor de BMP: ", "Calculando" if bpm == None else str(round(bpm,2)))

except KeyboardInterrupt:
    # Apagar los LEDs al interrumpir el programa
    led_rojo.off()
    led_verde.off()
    led_azul.off()