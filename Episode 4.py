from machine import Pin
import utime

buzzer = Pin(16, Pin.OUT)
sensor = Pin(15, Pin.IN)
buzzer.value(0)
while True:
    if sensor.value()==0:
        buzzer.value(1)
    else:
        buzzer.value(0)
