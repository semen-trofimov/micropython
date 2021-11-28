from hcsr04 import HCSR04
from time import sleep
from machine import Pin, I2C
import ssd1306
from time import sleep

# hc-sr05 pins for ESP32
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
i2c = I2C(-1, scl=Pin(15), sda=Pin(4),freq=400000)


oled_width = 128
oled_height = 64
# OLED reset pin
i2c_rst = Pin(16, Pin.OUT)
# Initialize the OLED display
i2c_rst.value(0)
sleep(0.010)
i2c_rst.value(1) # must be held high after initialization
# Setup the I2C lines
i2c_scl = Pin(15, Pin.OUT, Pin.PULL_UP)
i2c_sda = Pin(4, Pin.OUT, Pin.PULL_UP)
# Create the bus object
i2c = I2C(scl=i2c_scl, sda=i2c_sda)
# Create the display object
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
# hc-sr05 pins for ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    oled.fill(0)
    print(distance)
    oled.text(distance, 0, 10)
    oled.show()
    sleep(1)