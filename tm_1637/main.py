import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))
from time import sleep

# all LEDS on "88:88"
tm.write([127, 255, 127, 127])
sleep(2)

# all LEDS off
tm.write([0, 0, 0, 0])
sleep(2)

# show "0123"
tm.write([63, 6, 91, 79])
sleep(2)

# show "COOL"
tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])
sleep(2)

# show "HELP"
tm.show('help')
sleep(2)

# display "dEAd", "bEEF"
tm.hex(0xdead)
sleep(2)
tm.hex(0xbeef)
sleep(2)
# show "12:59"
tm.numbers(12, 59)
sleep(2)
# show "-123"
tm.number(-123)
sleep(2)
# show temperature '24*C'
tm.temperature(24)
sleep(2)