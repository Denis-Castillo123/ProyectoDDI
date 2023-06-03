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
|2|esp32|Pantalla pequeña|<img src="https://http2.mlstatic.com/D_NQ_NP_839782-CBT69011055664_042023-O.webp" width="200px">| $ | 1 |
|3|esp32cam|Camara portatil|<img src="https://www.makielectronic.com/fotos/grandes/esp32-cam.jpg" width="200px">| $ | 1 |
|4|Sensor temperatura y humedad|Sensor con doble funcionalidad para medir la temperatura y la humedad del cuerpo|<img src="https://www.automatismos-mdq.com.ar/blog/wp-content/uploads/2020/11/sensor-yl-38.jpg" width="200px">| $ | 1 |
|5|Buzzer|Actuador para alertar al usuario|<img src="https://www.flyrobo.in/image/cache/catalog/product2/3.5-5.5v-standard-active-buzzer-module-for-arduino-1024x1024.JPG" width="200px">| $ | 1 |
|6| Sensor ultrasonico| Sensor para medir la distancia de los objetos | <img src="https://www.steren.com.mx/media/catalog/product/cache/b69086f136192bea7a4d681a8eaf533d/image/1945948ab/sensor-ultrasonico.jpg" width="200px">  | $ | 1 | 
|7|Camisa|Prenda que el usuario pueda usar| <img src="https://ropalaboralonzor.com/5156-large_default/camiseta-manga-larga-unisex-arrow.jpg" width="200px"> | $ | 1 |
|8|Sensor de pulso cardiaco|Sensor para medir el ritmo cardiaco del usuario| <img src="https://cdn.shopify.com/s/files/1/0549/1166/4241/products/imagen_2022-12-29_105454198.png?v=1672332896" width="200px"> | $ | 1 |
|9|Botón | Botón para detener el Buzzer | <img src="https://megatronica.cc/wp-content/uploads/2022/04/PULSADOR-PEQUENIO-4-PINES-9.jpg" width="200px"> | $ | 1 |

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
|  HU01  | Yo como usuario requiero saber la distancia a la que están los objetos cercanos para tener precaución al moverme en mi entorno. | Debe, Puede, Podría hacerse, NO | 1 semana | El usuario tendrá conocimiento de si un objeto se encuentra cerca de el por me dio de un sensor ultrasonico. |  |
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







