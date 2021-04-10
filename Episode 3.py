from machine import Pin
import utime

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led_r = Pin(16, Pin.OUT)
led_g = Pin(17, Pin.OUT)
led_b = Pin(15, Pin.OUT)

led_r.value(1)
led_g.value(1)
led_b.value(1)

while True:
  if button.value() == 1:
    led_r.toggle()
    utime.sleep(1)
    led_r.toggle()
   
    led_g.toggle()
    utime.sleep(1)
    led_g.toggle()
    
    led_b.toggle()
    utime.sleep(1)
    led_b.toggle()
    utime.sleep(1)
  else:
    led_r.value(1)
    led_g.value(1)
    led_b.value(1)
    
