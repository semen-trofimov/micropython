from machine import UART
from time import sleep
uart = UART(1, 9600)       # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

sleep(30)

while True:
    uart.write('abc')   # write the 3 characters
    sleep(1)