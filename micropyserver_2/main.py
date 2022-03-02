from micropyserver import MicroPyServer
from machine import Pin
import esp
import network
from time import sleep

''' Код подключения к WiFi '''
wlan_id = "ananas"
wlan_pass = "t9indigo"

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
''' start server '''
server.start()