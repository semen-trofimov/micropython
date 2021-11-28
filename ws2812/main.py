import machine, neopixel, time

n = 12
p = 22
inten = 1

np = neopixel.NeoPixel(machine.Pin(p), n)

while i < 12:
    np[i] = (inten, 0, 0)
    i = i+1
    np.write()
    time.sleep(0.5)

# while i < 12:
#     i = i+1
#     while y < 12: 
#         y = y+1
#         np[i] = (inten, 0, 0)
#         time.sleep(0.5)
#         np[y] = (0, 0, 0)
#         np.write()



# np[0] = (inten, 0, 0)
# # np[1] = (0, inten, 0)
# # np[2] = (0, 0, inten)
# # np[3] = (inten, 0, 0)
# # np[4] = (0, inten, 0)
# # np[5] = (0, 0, inten)
# # np[6] = (inten, 0, 0)
# # np[7] = (0, inten, 0)
# # np[8] = (0, 0, inten)
# # np[9] = (inten, 0, 0)
# # np[10] = (0, inten, 0)
# # np[11] = (0, 0, inten)

# np.write()