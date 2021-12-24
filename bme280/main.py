# https://microcontrollerslab.com/micropython-bme280-esp32-esp8266-temperature-humidity-pressure/

from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import BME280        #importing BME280 library

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

while True:
    bme = BME280.BME280(i2c=i2c)          #BME280 object created
    temperature = bme.temperature            #reading the value of temperature
    humidity = bme.humidity                     #reading the value of humidity
    pressure = bme.pressure
    print('Temperature is: ', temperature)    #printing BME280 values
    print('Humidity is: ', humidity)
    print('Pressure is: ', pressure)
    sleep(10)           #delay of 10s                   #reading the value of pressure