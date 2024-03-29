from micropyserver import MicroPyServer
from machine import Pin, I2C
import esp
import network
from time import sleep
import BME280

''' Код подключения к WiFi '''
wlan_id = "ananas"
wlan_pass = "t9indigo"
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if wlan.isconnected() == False:
    wlan.connect(wlan_id, wlan_pass)
    while wlan.isconnected() == False:
        sleep(1)
print('Device IP:', wlan.ifconfig()[0])

def do_on2(request):
    pin.value(1)
    server.send(" LED ON!")

def do_off2(request):
    pin.value(0)
    server.send("LED OFF!")

pin = Pin(2, Pin.OUT)

def temp(request):
    server.send(bme.temperature)

def show_message(request):
    ''' request handler '''
    server.send("HELLO WORLD!")

def show_message2(request):
    ''' request handler '''
    server.send("HELLO SEMEN!")

def show_message3(request):
    ''' request handler '''
    server.send("HELLO YOULIA! I LOVE YOU!!! I LOVE YOU!!! I LOVE YOU!!! I LOVE YOU!!! I LOVE YOU!!! I LOVE YOU!!!")

server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
server.add_route("/semen", show_message2)
server.add_route("/yla", show_message3)
server.add_route("/pin2on", do_on2)
server.add_route("/pin2off", do_off2)
server.add_route("/temp", temp)
''' start server '''
server.start()