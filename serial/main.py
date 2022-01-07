from machine import Pin, UART
from time import sleep

uart = UART(2, 115200)
uart.init (115200, bits=8, parity=None, stop=1)

while True:
    uart.write('hello')
    sleep(1)
