from machine import Pin, I2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(15), sda=Pin(4),freq=400000)

# ESP8266 Pin assignment
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

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
oled.fill(0)
oled.text('HELLO FROM PYTHON!!!', 0, 0)
oled.text('HELLO FROM PYTHON!!!', 0, 10)
oled.text('HELLO FROM PYTHON!!!', 0, 20)
oled.text('HELLO FROM PYTHON!!!', 0, 30)
oled.text('HELLO FROM PYTHON!!!', 0, 40)
oled.text('HELLO FROM PYTHON!!!', 0, 50)
       
oled.show()