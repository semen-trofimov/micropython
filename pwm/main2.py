import machine
import time, math

pwm = machine.PWM(machine.Pin(25), freq=1000)

while True:
    for i in range(1024):
        pwm.duty(i)
        time.sleep(0.001)
    for i in range(1023, -1, -1):
        pwm.duty(i)
        time.sleep(0.001)