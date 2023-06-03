# Camisa inteligente
## Objetivo del proyecto
Apoyar a personas con problemas visuales a mejorar su estilo de vida, a través de de un dspositivo integrado en una prenda que pueda usar en su dia a dia.
## Integrantes
- Luis Gustavo García Carrillo
- Diego Torres Pérez
- Karla Denisse Aguilar Castillo
- Fatima Natalia Ruiz Rivera

# Hardware
| No. | Componente | Descripción | Imagen | Costo | Cantidad |
|-----|------------|-------------|--------|-------|----------|
|1|Raspberry Pi 4|Microcompurador reciente|<img src="https://m.media-amazon.com/images/I/41cn6diLE0L.jpg" width="200px">|$2500.00|1| 
|2|ESP32 LVGL|ESP32 con pantalla táctial integrada|<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/e9bc176f-d8a6-4b13-ada8-a6d88dc48c10" width="200px">|$168.53|1| 
|3|ESP32Cam|ESP32 con Camára integrada|<img src="https://hetpro-store.com/images/detailed/17/ESP32-CAM-imagen2.jpg" width="200px">|$172.47|1|
|4|Sensor temperatura y humedad|Sensor con doble funcionalidad para medir la temperatura y la humedad del cuerpo|<img src="https://m.media-amazon.com/images/I/415HFTvEImL._AC_SX679_.jpg" width="200px">|$69.00|1| 
|5|Buzzer|Actuador para alertar al usuario|<img src="https://vystronic.com/wp-content/uploads/2020/10/piezo-buzzer-324x324.jpg" width="200px">|$50.00|1|
|6|Sensor de distancia| Sensor para medir la distancia de los objetos|<img src="https://www.makercreativo.com/store/wp-content/uploads/2017/06/Sensor_ultrasonico_HCSR04_1.jpg" width="200px">|$80.00|1|
|7|Camisa|Prenda que el usuario pueda usar|<img src="https://ropalaboralonzor.com/5156-large_default/camiseta-manga-larga-unisex-arrow.jpg" width="200px">|$250.00|1|
|8|Sensor de pulso cardiaco|Sensor para medir el ritmo cardiaco del usuario|<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/b3e1ecca-dcb6-49aa-b25b-6387c3566d5e" width="200px">|$150.83|1|
|9|Botón | Botón para detener el Buzzer |<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/87044529/f0fee56c-7416-413b-9c3c-3da9caa76004" width="200px">|$89.00|1|

## Tabla de Software utilizado
| Id | Software | Version | Tipo |
|----|----------|---------|------|
| 01 | Fritzing | 0.9.3 | Diseño de circuitos |
| 02 | Tinkerd Card | N/A | diseño 3D, electrónica y codificación|
| 03 | Micro Python | 3.11.3 | lenguaje de programación |
| 04 | Github | N/A | plataforma de alojamiento |

## Tabla de historias de usuario
| Id | Historia de usuario | Prioridad | Estimación | Como probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
|  HU01  | Yo como usuario requiero saber la distancia a la que están los objetos cercanos para tener precaución al moverme en mi entorno. | Debe | 1 semana | El usuario tendrá conocimiento de si un objeto se encuentra cerca de el por me dio de un sensor ultrasonico. |  |
|  HU02  | Yo como usuario requiero tener un apoyo auditivo para que me sirva de apoyo al momento de estar en contacto cercado de objetos. | Debe | 1 semana | El usuario tendrá conocimiento de si un objeto se encuentra cerca de el por me dio de un sonido transmitido por el buzzer que sonará más rápido cuando el usuario más se aproxime. | |
|  HU03  | Yo como usuario, requiero de una cámara que trasmita a la pantalla, para poder ver lo que esta lejos de mi y evitar posibles accidentes | Puede | 1 semana | El usuario podrá observar los objetos que no logra visualizar por medio de un dispositivo que le transmite la imagen y le permite su entorno más cerca. |  |
|  HU04  | Yo como usuario requiero poder medir la humedad de mi persona para tener una correcto monitoreo. | Debe | 1 semana | El usuario podrá medir la humedad por medio de un sensor y este datos podrá ser visualizado en la pantalla del dispositivo. | |
|  HU05  | Yo como usuario requiero que la camisa sea capaz de medir mi temperatura corporal para llevar un control de esta. | Debe | 1 semana | El usuario podrá medir la temperatura por medio de un sensor y este dato podrá ser visualizado en la pantalla del dispositivo. | |
|  HU06  | Yo como usuario requiero que la camisa pueda monitorear las pulsaciones de mi corazón para llevar un monitoreo de mi ritmo cardiaco. | Puede | 1 semana | Todo el mecanismo será implementado en una camisa que le permita tener mejor acceso y control sobre sus estados. | |
|  HU07  | Yo como usuario requiero una interfaz amigable, para manejar correctamente el dispositivo . | Podria hacerse | 1 semana | Se podrá manejar el estado de su cuerpo y acciones del dispositivo desde una pantalla ESP32. | |
|  HU08  | Yo como usuario requiero poder detener el sonido de alerta para que llegue a ser molesto | Debe | 1 semana | Se podrá detener la alerta del un objeto cerca por medio de un botón integrado en el dispositivo de la muñeca. | |

## Prototipo en dibujo
- Coloca la fotografia de tu prototipo dibujado a lapiz

## -----Prototipo en Fitzing Circuito y PCB del Prototipo componentes Pecho
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/90db7be4-1631-4bbb-a28c-d960ddf96319" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/48e6a6db-3f4e-4f5a-bce8-8d065e2c7e91" width="500px">

## Prototipo 3D Pecho
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/0fbade4d-0faf-4fad-95a1-f3592e3ecf94" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/1a9fcdf4-7bf6-445c-aabc-59563e8f4487" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/9af0d137-4570-447f-b33d-e817db207864" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/fc1a56fd-8b1f-48b2-b4b7-83124d40c12d" width="500px">

## -----Prototipo en Fitzing Circuito y PCB del Prototipo componentes Mano
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/c2a203fc-805f-46ad-bd42-0a952b2cc83c" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/95ce5c06-46f2-4b61-8d0f-9dc48c0aa510" width="500px">

## Prototipo 3D Mano
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/274dbb32-d2f2-4ebe-af47-ad778b5c8419" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/d1dced08-4d4a-4536-bbee-1fe16bf0daeb" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/31353217-ff58-4919-96a7-117c39e1daa0" width="500px">
<img src="https://github.com/Denis-Castillo123/ProyectoDDI/assets/98179865/6dc639d3-4a72-4cef-a499-fc61fcc50229" width="500px">







