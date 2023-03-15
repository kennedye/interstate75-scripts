# pylint: disable=line-too-long,import-error,unused-import,too-many-locals,invalid-name,unused-variable,too-many-statements,invalid-envvar-default,consider-using-f-string
"""
i75_simpleclock.py
just the text ma'am
"""
import time
import os
import sys
import random
import board
import busio
import displayio
import framebufferio
import rgbmatrix
import terminalio
from rainbowio import colorwheel
import neopixel
import adafruit_ds3231  # RTC
from led_panel import LedPanel
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

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

    # font = bitmap_font.load_font("/fonts/5x7.pcf")
    font = terminalio.FONT
    text_label = label.Label(font)
    text_label.x = 1
    text_label.y = 12
    text_label.color=(255,0,255)
    text_label.anchored_position = (0, 0)
    text_label.text="{hours:02d}{minutes:02d}{seconds:02d}".format(hours=current_time[3], minutes=current_time[4], seconds=current_time[5])
    master_group.append(text_label)
    print(text_label.bounding_box)
    while True:
        current_time = ds3231.datetime
        text_label.text="{hours:02d}{minutes:02d}{seconds:02d}".format(hours=current_time[3], minutes=current_time[4], seconds=current_time[5])
        text_label.color=(random.randint(32,255),random.randint(32,255),random.randint(32,255))
        time.sleep(1)

if __name__ == "__main__":
    main()
