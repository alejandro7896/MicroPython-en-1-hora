from machine import Pin, ADC
from time import sleep

# Configuración del sensor de luz (LDR como sensor)
sensor = ADC(Pin(34))

sensor.width(ADC.WIDTH_12BIT) # Resolución de 12 bits (0–4095)

# LED indicador
led = Pin(19, Pin.OUT)

# Bucle principal
contador = 1

while contador <= 100:
    lectura = sensor.read()
    print("Valor:", lectura)
    
    # Si hay mucha luz, apaga el LED; si hay poca, enciéndelo
    if lectura > 1000:
        led.off()
    else:
        led.on()
    
    sleep(0.3)
    contador += 1
  
