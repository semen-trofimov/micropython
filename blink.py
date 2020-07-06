from machine import Pin
from time import sleep
led_red = Pin(21, Pin.OUT)
led_green = Pin(13, Pin.OUT)
led_blue = Pin(12, Pin.OUT)
delay = 0.5
while True:
  led_red.value(1)
  sleep(delay)
  led_red.value(0)
  sleep(delay)
  led_blue.value(1)
  sleep(delay)
  led_blue.value(0)
  sleep(delay)
