import machine

p17 = machine.Pin(17)

pwm = machine.PWM(p17)

pwm.freq(8000)
pwm.duty(1)