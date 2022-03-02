#!/bin/bash
esptool.py --chip esp32 --port /dev/ttyUSB1 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB1 --baud 460800 write_flash -z 0x1000 esp32-20210902-v1.17.bin
