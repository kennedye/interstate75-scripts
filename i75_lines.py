# pylint: disable=line-too-long,import-error,unused-import,too-many-locals,invalid-name,unused-variable,too-many-statements,invalid-envvar-default
"""
mp_lines.py
a rainbow of lines
"""
import time
import os
import sys
import board
import busio
import displayio
import framebufferio
import rgbmatrix
import terminalio
from rainbowio import colorwheel
from digitalio import DigitalInOut
import neopixel
import adafruit_ds3231  # RTC
import adafruit_fancyled.adafruit_fancyled as fancy
from led_panel import LedPanel

# try:
#     from _secrets import af_secrets as secrets
# except ImportError:
#     print("WiFi secrets are kept in secrets.py, please add them there!")
#     raise


def compatibility_check():
    """
    basic checks to make sure the board and version are correct
    """
    board_type = os.uname().machine
    if "Pimoroni Interstate 75" not in board_type:
        print(f"unsupported board type: {board_type}")
        print("this code is designed to run on Pimoroni Interstate 75")
        sys.exit(1)
    cp_info = sys.implementation
    if cp_info.version[0] < 8:
        print(f"unsupported CircuitPython major version: {cp_info.version[0]}")
        print("this code is designed to run on CircuitPython 8.0 or later")
        sys.exit(1)


def make_palette_rgb():
    """
    build a rainbow palette
    of gamma-corrected values
    this should probably be a class
    so it can go in a separate file
    """
    palette = [None] * 48

    # red to orange
    palette[0] = (255, 0, 0)
    palette[1] = (255, 56, 0)
    palette[2] = (255, 81, 0)
    palette[3] = (255, 102, 0)
    palette[4] = (255, 119, 0)
    palette[5] = (255, 136, 0)
    palette[6] = (255, 151, 0)
    palette[7] = (255, 165, 0)
    
    # orange to yellow
    palette[8] = (255, 165, 0)
    palette[9] = (255, 177, 0)
    palette[10] = (255, 190, 0)
    palette[11] = (255, 203, 0)
    palette[12] = (255, 216, 0)
    palette[13] = (255, 229, 0)
    palette[14] = (255, 242, 0)
    palette[15] = (255, 255, 0)
    
    # yellow to green
    palette[16] = (255, 255, 0)
    palette[17] = (235, 255, 0)
    palette[18] = (213, 255, 0)
    palette[19] = (190, 255, 0)
    palette[20] = (164, 255, 0)
    palette[21] = (133, 255, 0)
    palette[22] = (94, 255, 0)
    palette[23] = (0, 255, 0)
    
    # green to blue
    palette[24] = (0, 255, 0)
    palette[25] = (0, 240, 115)
    palette[26] = (0, 220, 192)
    palette[27] = (0, 198, 255)
    palette[28] = (0, 174, 255)
    palette[29] = (0, 144, 255)
    palette[30] = (0, 102, 255)
    palette[31] = (0, 0, 255)

    # blue to purple
    palette[32] = (0, 0, 255)
    palette[33] = (63, 0, 253)
    palette[34] = (89, 0, 250)
    palette[35] = (108, 3, 248)
    palette[36] = (123, 10, 246)
    palette[37] = (137, 17, 244)
    palette[38] = (149, 25, 242)
    palette[39] = (160, 32, 240)
    
    # purple to red
    palette[40] = (160, 32, 240)
    palette[41] = (205, 0, 211)
    palette[42] = (236, 0, 179)
    palette[43] = (255, 0, 145)
    palette[44] = (255, 0, 112)
    palette[45] = (255, 0, 79)
    palette[46] = (255, 0, 47)
    palette[47] = (255, 0, 0)

    for i in range(len(palette)):
        r, g, b = palette[i]
        gc = fancy.gamma_adjust(fancy.CRGB(r, g, b), gamma_value=1.8)
        palette[i] = gc.pack()
    
    gamma_palette = displayio.Palette(48)
    for i in range(len(gamma_palette)):
        gamma_palette[i] = palette[i]

    return gamma_palette


def main():
    """
    they call it main.
    """

    # is it safe
    compatibility_check()

    # get rid of any pre-existing display
    displayio.release_displays()

    panel = LedPanel()
    panel_auto_refresh = (os.getenv("panel_auto_refresh") == "True", "True")  # or False if refreshing the display manually
    display = framebufferio.FramebufferDisplay(panel.matrix, auto_refresh=panel_auto_refresh)

    master_group = displayio.Group()

    display.show(master_group)

    i2c = board.I2C()  # read for accelerometer and RTC

    # RTC - https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/circuitpython
    ds3231 = adafruit_ds3231.DS3231(i2c)
    current_time = ds3231.datetime  # struct_time

    bitmap = [None] * panel.matrix.width
    tile_grid = [None] * panel.matrix.width
    palette = make_palette_rgb()
    for i in range(0, panel.matrix.width):
        bitmap[i] = displayio.Bitmap(1, panel.matrix.height, 48)
        for x in range(0, panel.matrix.height):
            bitmap[i][0,x] = i
        tile_grid[i] = displayio.TileGrid(bitmap[i], pixel_shader=palette)
        tile_grid[i].x = i
        master_group.append(tile_grid[i])

    i = 0
    while True:
        i += 1
        if i > 47:
            i = 0
        for x in range(0, panel.matrix.height):
            for y in range(0, panel.matrix.width):
                bitmap[y][x] = i


if __name__ == "__main__":
    main()
