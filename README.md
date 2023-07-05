# Camisa inteligente
## Objetivo del proyecto
El objetivo principal de este proyecto es diseñar y desarrollar un dispositivo que pueda integrarse fácilmente a una prenda de vestir como una camiseta, con el propósito de ayudar a las personas con problemas visuales.

El dispositivo consiste como una solución deseñada para ser incorporada a un prensa de vestir. Esto permitirá que las personas con problemas visuales puedan llevar el dispositivo con sigo en todo momento. El dispositivo integrado de la prenda estará equipado con las funciones de detección de obstáculos, detección de temperatura y humedad por medio de un entorno intuitivo.
## Integrantes
- Luis Gustavo García Carrillo
- Diego Torres Pérez
- Karla Denisse Aguilar Castillo
- Fatima Natalia Ruiz Rivera

## Beneficiario
Ma. Angelica Castillo Sánchez

# Hardware
| No. | Componente | Descripción | Imagen | Costo | Cantidad | 
|-----|------------|-------------|--------|-------|----------|
|1|Raspberry Pi 4| Computador de placa única (SBC, por sus siglas en inglés) desarrollado por la Fundación Raspberry Pi. Se trata de la cuarta generación de la serie de dispositivos Raspberry Pi, y ha sido diseñado para ser una plataforma versátil y de bajo costo para una amplia gama de aplicaciones.|<img src="https://m.media-amazon.com/images/I/41cn6diLE0L.jpg" width="200px">|$2500.00|1| 
|2|ESP32 LVGL|Es una combinación del microcontrolador ESP32 y la biblioteca gráfica LVGL. El ESP32 es un microcontrolador de bajo consumo de energía y alto rendimiento desarrollado por Espressif Systems. LVGL es una biblioteca gráfica de código abierto diseñada para crear interfaces de usuario interactivas y atractivas en sistemas embebidos.|<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/e9bc176f-d8a6-4b13-ada8-a6d88dc48c10" width="200px">|$168.53|1| 
|3|ESP32Cam|Variante específica del ESP32 que incluye una cámara integrada. Combina las capacidades del ESP32 con la capacidad de capturar imágenes y vídeos en tiempo real.|<img src="https://hetpro-store.com/images/detailed/17/ESP32-CAM-imagen2.jpg" width="200px">|$172.47|1|
|4|Sensor temperatura y humedad|Dispositivo que se utiliza para medir y monitorizar la temperatura y la humedad en un entorno determinado. Estos sensores son ampliamente utilizados en aplicaciones como sistemas de climatización, invernaderos, estaciones meteorológicas, sistemas de control ambiental, entre otros.|<img src="https://m.media-amazon.com/images/I/415HFTvEImL._AC_SX679_.jpg" width="200px">|$69.00|1| 
|5|Buzzer|Es un dispositivo electromecánico que produce un sonido o zumbido cuando se le aplica una corriente eléctrica. Los buzzers se utilizan en una amplia variedad de aplicaciones, desde alarmas y señales audibles hasta indicadores sonoros en dispositivos electrónicos.|<img src="https://vystronic.com/wp-content/uploads/2020/10/piezo-buzzer-324x324.jpg" width="200px">|$50.00|1|
|6|Sensor de distancia|Dispositivo electrónico que se utiliza para medir la distancia entre el sensor y un objeto o superficie cercana. Estos sensores son ampliamente utilizados en una variedad de aplicaciones, como sistemas de navegación, robótica, automatización industrial, sistemas de seguridad y detección de objetos.|<img src="https://www.makercreativo.com/store/wp-content/uploads/2017/06/Sensor_ultrasonico_HCSR04_1.jpg" width="200px">|$80.00|1|
|7|Camisa|Prenda que el usuario pueda usar e implementar los dispositivos de apoyo para el usaurio. La comisa contará con averturas en la parte del pecho y la muñeca con el proposito de agregar y quitar a disposición del usuario|<img src="https://ropalaboralonzor.com/5156-large_default/camiseta-manga-larga-unisex-arrow.jpg" width="200px">|$250.00|1|
|8|Sensor de pulso cardíaco|Un sensor de distancia es un dispositivo electrónico que se utiliza para medir la distancia entre el sensor y un objeto o superficie cercana. Estos sensores son ampliamente utilizados en una variedad de aplicaciones, como sistemas de navegación, robótica, automatización industrial, sistemas de seguridad y detección de objetos.|<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/b3e1ecca-dcb6-49aa-b25b-6387c3566d5e" width="200px">|$150.83|1|
|9|Pulsador|Dispositivo simple y comúnmente utilizado en electrónica para activar o desactivar una función o realizar una acción específica cuando se presiona. Consiste en un interruptor momentáneo que se cierra cuando se aplica presión y se abre cuando se deja de presionar.|<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/f0fee56c-7416-413b-9c3c-3da9caa76004" width="200px">|$89.00|1|

## Tabla de Software utilizado
<div align="center">
  
| ID | Software | Versión | Tipo |
|----|----------|---------|------|
| 01 | Fritzing | 0.9.3 | Diseño de circuitos (licencia libre) |
| 02 | Tinkerd Card | N/A | Diseño 3D, electrónica y codificación(licencia libre) |
| 03 | Micro Python | 3.11.3 | Lenguaje de programación (licencia libre) |
| 04 | Github | N/A | Plataforma de alojamiento (licencia libre) |
| 05 | PySerial | 3.4 | Librería para el sensor de pulso cardiaco (licencia libre) |
| 06 | Adafruit CircuitPython | 4.0 | Librería para el sensor de temperatura y humedad del cuerpo humano |  
| 07 | RPi.GPIO | 0022 | Librería para sensor ultrasonico (licencia libre) |

</div>

## Tabla de historias de usuario
| Id | Historia de usuario | Prioridad | Estimación | Como probarlo | Responsable |Sprint |
|----|---------------------|-----------|------------|---------------|-------------|-------|
|  HU01  | Yo como persona con problemas de visión, requiero saber la distancia a la que están los objetos cercanos para tenerme precaución al moverme en mi entorno. | Debe | 2 | El usuario tendrá conocimiento de si un objeto se encuentra cerca de él por medio de un sensor infra rojo. | Denisse  | Sprint 1 |
|  HU02  | Yo como persona con limitaciones visuales, requiero tener un apoyo sensorial para que me sirva de ayuda al momento de estar en contacto cercano con otros objetos. | Debe | 1 | El usuario tendrá conocimiento de si un objeto se encuentra cerca de él por medio de un sonido transmitido por un zumbador, que vibrara a medida que el usuario más se aproxime a algun objeto con el cual este proximo a chocar | Fatima | Sprint 1 |
|  HU03  | Yo como persona con dificultades visuales, requiero de una cámara que trasmita la imagen a la pantalla, para poder ver lo que esta lejos de mi y evitar posibles accidentes. | Puede | 5 | El usuario podrá observar los objetos que no logra visualizar nítidamente por medio de un dispositivo que le transmita la imagen a la pantalla. | Diego | Sprint 2 |
|  HU04  | Yo como persona con problemas visuales y de salud, requiero poder detectar cuando es ta oscureciendo para ello nesecito un sensor de luz ambiental para el caso de que este osureciendo mas alla de lo que mi vista puede percibir | Debe | 3 | El usuario podrá medir la humedad por medio de un sensor y este dato podrá ser visualizado en la pantalla del dispositivo. | Denisse | Sprint 1 |
|  HU05  | Yo como persona con problemas de visión y de salud, requiero que la camisa integre un sensor que sea capaz de medir mi temperatura corporal para llevar un monitoreo de la misma. | Debe | 3 | El usuario podrá medir la temperatura por medio de un sensor y este dato podrá ser visualizado en la pantalla del dispositivo. | Luis Gustavo|sprint 2 |
|  HU06  | Yo como persona con dificultades visuales y de salud, requiero que la camisa pueda monitorear las pulsaciones de mi corazón para llevar un monitoreo de mi ritmo cardíaco. | Puede | 3 | El sensor será integrado en una camisa que le permita tener mejor acceso y control sobre su ritmo cardíaco, al procesar los datos recibidos del pulsómetro. | Fatima | Sprint 2|
|  HU07  | Yo como persona con limitaciones visuales, requiero una interfaz amigable para manejar intuitivamente el dispositivo. | Podria hacerse | 5 | Se podrá manejar el estado de su cuerpo y acciones del dispositivo desde una pantalla ESP32. |Luis Gustavo| Sprint 2 |
|  HU08  | Yo como persona con problemas de visión, requiero poder detener el sonido de alerta para que no llegue a ser molesto.| Debe | 1 | Se podrá detener la alerta de un objeto cercano por medio de un botón integrado en el dispositivo de la muñeca. | Diego | sprint 1 |


## Prototipo en dibujo
<div align="center">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/86625096/728ac81f-14f9-4b43-a1b9-748ddd3be6f5" width="500px">
</div>

## -----Prototipo en Fitzing Circuito y PCB del Prototipo componentes Pecho
<div align="center">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/90db7be4-1631-4bbb-a28c-d960ddf96319" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/48e6a6db-3f4e-4f5a-bce8-8d065e2c7e91" width="500px">
</div>

## Prototipo 3D Pecho
<div align="center">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/0fbade4d-0faf-4fad-95a1-f3592e3ecf94" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/1a9fcdf4-7bf6-445c-aabc-59563e8f4487" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/9af0d137-4570-447f-b33d-e817db207864" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/fc1a56fd-8b1f-48b2-b4b7-83124d40c12d" width="500px">
</div>
  
## -----Prototipo en Fitzing Circuito y PCB del Prototipo componentes Mano
<div align="center">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/c2a203fc-805f-46ad-bd42-0a952b2cc83c" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/95ce5c06-46f2-4b61-8d0f-9dc48c0aa510" width="500px">
</div>

## Prototipo 3D Mano
<div align="center">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/274dbb32-d2f2-4ebe-af47-ad778b5c8419" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/d1dced08-4d4a-4536-bbee-1fe16bf0daeb" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/31353217-ff58-4919-96a7-117c39e1daa0" width="500px">
  <img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/6dc639d3-4a72-4cef-a499-fc61fcc50229" width="500px">
</div>
