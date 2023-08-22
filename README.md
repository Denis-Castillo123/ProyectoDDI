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
Jesús Fernando Gonzalez Pedroza

# Hardware
| No. | Componente | Descripción | Imagen | Costo | Cantidad | 
|-----|------------|-------------|--------|-------|----------|
|01|Raspberry Pi 4| Computador de placa única (SBC, por sus siglas en inglés) desarrollado por la Fundación Raspberry Pi. Se trata de la cuarta generación de la serie de dispositivos Raspberry Pi, y ha sido diseñado para ser una plataforma versátil y de bajo costo para una amplia gama de aplicaciones.|<img src="https://m.media-amazon.com/images/I/41cn6diLE0L.jpg" width="200px">|$2500.00|1| 
|02|ESP32 WT32-SC01 PLUS|Placa de Desarrollo ESP32 con Pantalla LCD Multitáctil Capacitiva de 3,5 Pulgadas 320X480, BT Integrado, WifiMódulo de ESP32-WROVER-B.|<img src="https://ae01.alicdn.com/kf/S8d759761060d44f990b242c735caad83f/Placa-de-desarrollo-ESP32-WT32-SC01-PLUS-pantalla-LCD-multit-ctil-capacitiva-de-3-5-pulgadas.jpg_220x220.jpg_.webp" width="200px">|$479.46|1| 
|03|ESP32|Es un microcontrolador de bajo costo y bajo consumo de energía, diseñado para aplicaciones de IoT, con conectividad Wi-Fi y Bluetooth, y una amplia variedad de interfaces periféricas.|<img src="https://http2.mlstatic.com/D_NQ_NP_709003-MLM70483877556_072023-O.webp" width="200px">|$212.00|3|
|04|Sensor de Temperatura LM35|Dispositivo que se utiliza para medir y monitorizar la temperatura en un entorno determinado. Estos sensores son ampliamente utilizados para medir la temperatura del cuerpo humano.|<img src="https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcSRLWIuVPcelt85e4Cr4PKIaefxSI0-4VrJrIsxTP7-OS7kKn2HKaFk0Yn1bO5U4G2_t_MPs4Q0Y7nsI3eCrc0JXIrtSoaF" width="200px">|$45.00|1| 
|05|Sensor de distancia laser|sensor de distancia láser que utiliza tecnología Time-of-Flight (ToF) para medir la distancia con alta precisión. Se puede conectar a una placa Arduino a través del protocolo de comunicación I2C y proporciona una distancia de medición de hasta 2 metros. Este sensor es ideal para proyectos de robótica, automatización y detección de objetos.|<img src="https://http2.mlstatic.com/D_NQ_NP_872239-MLM44261999694_122020-O.webp" width="200px">|$116.90|1|
|06|Camisa|Prenda que el usuario pueda usar e implementar los dispositivos de apoyo para el usaurio. La comisa contará con averturas en la parte del pecho y la muñeca con el proposito de agregar y quitar a disposición del usuario|<img src="https://ropalaboralonzor.com/5156-large_default/camiseta-manga-larga-unisex-arrow.jpg" width="200px">|$250.00|1|
|07|Sensor de pulso cardíaco|Un sensor de distancia es un dispositivo electrónico que se utiliza para medir la distancia entre el sensor y un objeto o superficie cercana. Estos sensores son ampliamente utilizados en una variedad de aplicaciones, como sistemas de navegación, robótica, automatización industrial, sistemas de seguridad y detección de objetos.|<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/b3e1ecca-dcb6-49aa-b25b-6387c3566d5e" width="200px">|$150.83|1|
|08|Bocina de laptop|Dispositivo simple y comúnmente utilizado en electrónica para activar o desactivar una función o realizar una acción específica cuando se presiona. Consiste en un interruptor momentáneo que se cierra cuando se aplica presión y se abre cuando se deja de presionar.|<img src="https://i.ebayimg.com/images/g/2tgAAOSwlUlkl4wY/s-l1600.jpg" width="200px">|$500.00|1|
|09|Sensor con acelerómetro y giroscopio|Mide la aceleración y la velocidad angular de un objeto en movimiento. Se utiliza en diferentes aplicaciones, como en dispositivos móviles para detectar movimientos y orientación, en sistemas de navegación inercial, en robots y vehículos autónomos.|<img src="https://www.steren.com.mx/media/catalog/product/cache/b69086f136192bea7a4d681a8eaf533d/image/216213368/sensor-con-acelerometro-y-giroscopio.jpg" width="200px">|$99.00|1|
|10|Relevador|Es un dispositivo electrónico que permite controlar la conexión o desconexión de un circuito eléctrico mediante una señal de entrada. Este modelo en particular tiene un canal y puede manejar corrientes de hasta 10 amperios con una alimentación de 5 voltios.|<img src="https://m.media-amazon.com/images/I/41wg3LsMFNL.jpg" width="200px">|$55.00|1|
|11|Foco|fuente de iluminación diseñada para ser amigable con el medio ambiente, utilizando tecnologías de iluminación eficientes en términos de energía y materiales reciclados.|<img src="https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcS2-CyANXPRzu8T5jzr_u_0McQwyTw9K8gDQSh3Sip0usMBCJ_xG64mjcVQ7AP2FcBvOP2SLhHdRdlGrQ_pOLBAe4Du1K1bsO0Zv7-QoToY4ls0QpHRuonU" width="200px">|$56.00|1|

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
|  HU01  | Yo como persona con problemas de visión, requiero conocer la distancia a la que están los objetos cercanos para tener precaución al moverme en mi entorno. | Debe | 2 | El dispositivo detecta un objeto cercano por medio de un sensor laser, estos datos se almacenarán en la base de datos, de igual manera se mostrarán en la pantalla la distancia a la que se encuentra un objeto, para en dado caso de que la visibilidad del usuario le impida percibir la distan cia por sí mismo. | Denisse  | Sprint 2 |
|  HU02  | Yo como persona con limitaciones visuales, requiero tener un apoyo sensorial, que me sirva de ayuda al momento de estar en contacto cercano con otros objetos. | Debe | 1 | Una vez que el sensor de laser detecta una distancia muy próxima a los objetos, la bocina emitirá un sonido en el pecho del usuario indicándole que está en peligro de chocar de frente con algún objeto. | Fatima | Sprint 2 |
|  HU03  | Yo como persona con dificultades visuales y de salud, requiero que la camisa pueda monitorear las pulsaciones de mi corazón para llevar un monitoreo de mi ritmo cardíaco| Puede | 3 | El sensor de ritmo cardiaco detectará el pulso del usuario y las almacenará en la base de datos. | Fatima | Sprint 1 |
|  HU04  | Yo como persona con limitaciones visuales, requiero una interfaz amigable para manejar intuitivamente el dispositivo del antebrazo. | Podria hacerse | 5 | Se podrá visualizar el estado físico/salud del usuario por medio de mensajes en la pantalla integrada del dispositivo en el antebrazo. |Luis Gustavo| Sprint 1 |
|  HU05 | Yo como persona con problemas de visuales, requiero un medio para encender la luz de la habitación desde el dispositivo.| Debe | 1 | Se pod´ra encender y apagar el foco de la habitación del usuario por medio de la pantalla. | Diego | Sprint 2 |
|  HU06  | Yo como persona con problemas de visuales, requiero que un componente que sea capaz de medir cuando estoy acelerando o caminando demasiado rápido.| Debe | 5 | Se podrá visualizar la medición de la caminata del usuario por medio de mensajes en la pantalla integrada en el dispositivo del antebrazo. | Diego | Sprint 2 |
|  HU07 | Yo como persona con problemas de visuales, requiero que tener un medio visual donde se vea reflejada la temperatura ambiental| Debe | 5 | Se podrá visualizar la medición de la temperatura del ambiente por medio de mensajes en la pantalla integrada en el dispositivo del antebrazo. | Denisse| Sprint 2 |
|  HU08 | Yo como persona con problemas de visuales, requiero que tener un medio visual donde se vea reflejado el ritmo cardiaco.| Debe | 5 | Se podrá visualizar la medición del ritmo cardiaco por medio de mensajes en la pantalla integrada en el dispositivo del antebrazo. | Luis Gustavo | Sprint 2 |


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

# Evidenicas de la ejecución sprint 1
## Implementación de la base de datos en node-red
<div align="center">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/bfa15343-02c2-48f0-99ff-7ba085f506f5" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/55650800-b2d6-445a-9fbb-f54c8a34de4a" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/e89adf21-4740-405c-9441-7d23572b6830" width="500px">
</div>

## Lecturas de en consola de la pantalla ESP32
<div align="center">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/86983c5b-c862-49f7-b52b-e8e2cc74d4e0" width="500px">
</div>
##Captando los valores de los sensores
<div align="center">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/d088ded0-81ed-4b0d-931a-9da96bc30b4b" width="500px">
</div>

## Mostrando los valores en la pantalla
<div align="center">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/80dbcc97-81f4-4880-8d2c-355e2520a1b6" width="500px">
</div>

## VIDEO DEMOSTRATIVO DEL SPRINT 1
https://drive.google.com/file/d/1PbnqZgavAxOrBTrMRkKC7mu2j_codPKj/view?usp=drivesdk

# Evidenicas de la ejecución sprint 2
## Diseño en 3D de las carcasas 
<div align="center">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/90869371/f63620fb-fe46-4a99-8719-5669f8bbfab7" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/90869371/ae8c2bc0-e7fa-4502-a193-c99ff9c5df31" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/90869371/e1f39e4e-5d2a-429c-b8af-58b23322e56d" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/90869371/9f94ff6b-b387-4957-b6e0-4466fc06d59f" width="500px">
</div>

## Imagenes del dispositivo en ejecución 
<div align="center">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/90869371/142c7c65-724a-46e4-814e-7c1ba408dcd1" width="200px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/90869371/d90ecdcc-eb7e-44c8-82bc-9b5f81cceb2d" width="500px">
</div>


## Despliegue de Monitoreo y Control desde Dashboard 

## Implementación de Sensores y Actuadores

## Comunicación MQTT entre Dispositivos

## Uso de Base de Datos

## VIDEO DEL SPRINT 2
### Video del beneficiario
https://drive.google.com/file/d/1cfEnb1IhoRyG9T4VkEn3uEBwskRIydiF/view?usp=drive_link
### Video demostrativo
https://drive.google.com/file/d/1chnvIdxckCr2v5xHA4EuY7Q-IPKVBz1k/view?usp=drive_link

