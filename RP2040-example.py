#note: sh1107.py need to be copied to the "Lib" folder on the rapsberry Pico board
#note2: If using Adafruit SH1107 board. The RST Pin on it need to be connected to 3.3v

from machine import I2C, Pin
from utime import sleep
from sh1107 import SH1107_I2C

i2c = I2C(id=1, sda=Pin(14), scl=Pin(15)) #Raspberry Pico and Pico W need the ID of the I2C BUS
display = SH1107_I2C(128, 64, i2c)

while True:
    display.text("Hello, World!", 0, 0, 1)
    display.show()
    sleep(2)
