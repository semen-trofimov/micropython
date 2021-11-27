from machine import Pin
from time import sleep
led_red = Pin(21, Pin.OUT)
led_green = Pin(13, Pin.OUT)
led_blue = Pin(12, Pin.OUT)
led_red.value(0)
led_green.value(0)
led_blue.value(0)
