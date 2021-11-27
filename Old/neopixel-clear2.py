import machine, neopixel

n = 10
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)
for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
