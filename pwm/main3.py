import machine
import time, math

led = machine.PWM(machine.Pin(17), freq=1000)

for i in range(40):
    