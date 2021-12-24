from machine import UART
from time import sleep
uart = UART(2, 9600)       # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

sleep(30)

while True:
    uart.write('abc')   # write the 3 characters
    sleep(1)