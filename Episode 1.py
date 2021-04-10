
#First Code to on LED
from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()

#Second code to blink LED

from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
