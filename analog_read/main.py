# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))       #Full range: 3.3v
pot.atten(ADC.WIDTH_12BIT)
while True:
    pot_value = pot.read()
    val = pot_value/40
    print(val)
    sleep(0.1)