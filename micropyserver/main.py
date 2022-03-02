from micropyserver import MicroPyServer
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

def show_message(request):
    ''' request handler '''
    server.send("HELLO WORLD!")

server = MicroPyServer()
''' add request handler '''
server.add_route("/", show_message)
''' start server '''
server.start()