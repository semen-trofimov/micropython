import machine, neopixel

n = 10
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)

np[0] = (0,0,0)
np[1] = (0,0,0)
np[3] = (0,0,0)
np[4] = (0,0,0)
np[5] = (0,0,0)
np[6] = (0,0,0)
np[7] = (0,0,0)
np[8] = (0,0,0)
np[9] = (0,0,0)
np.write()
