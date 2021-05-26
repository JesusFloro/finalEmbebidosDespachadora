# finalEmbebidosDespachadora
Este proyecto consiste en generar una despachadora basica de bebidas (solo agua), para ello cuenta con los siguientes elementos:
* Pantalla LCD 16x2
* Convertidor a I2C para LCD
* Relevador a 5vdc (salida 3.3vdc) activo en bajo
* Puente H
* Motor Nema 17
* Raspberry Pi
* Pila Lipo de 11.1 V a 3 celdas
* Sensor infrarrojo detector de objetos
* Accesorios adicionales

En la carpeta se pueden encontrar los codigos por separado de cada uno de los componententes y 
un codigo llamado final.py, en el cual se encuentran todos los elementos juntos, de la misma manera, en la carpeta img se encuentra 
el diagrama esquematico del proyecto, el pinOut es el siguiente:

  - Para el motor Nema 17:
    out1 = 13 -> GPIO27
    out2 = 11 -> GPIO17
    out3 = 15 -> GPIO22
    out4 = 12 -> GPIO18
  - Para la bomba:
    pinBomba = 16 -> GPIO23
  - Para los sensores:
    sensorInf = 37 -> GPIO26
    sensorSup = 35 -> GPIO19
  - Para la pantalla LCD:
    SDA = SDA ->GPIO2
    SCL = SCL ->GPIO3
