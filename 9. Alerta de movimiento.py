from machine import Pin
from time import sleep

# Definciónd de pines
pir = Pin(19, Pin.IN)
led = Pin(2, Pin.OUT)
buzzer = Pin(5, Pin.OUT, Pin.PULL_DOWN)

def alarma(pin):
    print("Movimiento detectado!")
    led.on()
    for _ in range(5):
        buzzer.value(1)
        sleep(0.1)
        buzzer.value(0)
        sleep(0.1)
    led.off()
    

pir.irq(trigger=Pin.IRQ_RISING, handler=alarma)

while True:
    for i in range(1,11):
        print("Contador:",i)
        sleep(1)
