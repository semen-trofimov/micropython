import machine, neopixel

n = 10
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)
for i in range(n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)
