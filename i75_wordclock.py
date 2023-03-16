# SPDX-FileCopyrightText: 2020 John Park for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Metro Matrix Clock
# Runs on Airlift Metro M4 with 64x32 RGB Matrix display & shield

import time
# import rtc
import board
import displayio
import terminalio
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
# from adafruit_matrixportal.network import Network
# from adafruit_matrixportal.matrix import Matrix
import framebufferio  # pylint: disable=import-error
import rgbmatrix  # pylint: disable=import-error
import adafruit_ds3231


BLINK = False
DEBUG = False

# Get wifi details and more from a secrets.py file
# try:
#     from secrets import secrets
# except ImportError:
#     print("WiFi secrets are kept in secrets.py, please add them there!")
#     raise
# print("    Metro Minimal Clock")
# print("Time will be set for {}".format(secrets["timezone"]))
i2c = board.I2C()
ds3231 = adafruit_ds3231.DS3231(i2c)

# the_rtc = rtc.RTC()

# --- Display setup ---
# matrix = Matrix()
# display = matrix.display
# network = Network(status_neopixel=board.NEOPIXEL, debug=False)
displayio.release_displays()

# interstate75 64x32
matrix = rgbmatrix.RGBMatrix(
    width=64,
    height=32,
    bit_depth=6,
    rgb_pins=[board.R0, board.G0, board.B0, board.R1, board.G1, board.B1],
    addr_pins=[board.ROW_A, board.ROW_B, board.ROW_C, board.ROW_D],
    clock_pin=board.CLK,
    latch_pin=board.LAT,
    output_enable_pin=board.OE,
)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

# --- Drawing setup ---
group = displayio.Group()  # Create a Group
bitmap = displayio.Bitmap(64, 32, 6)  # Create a bitmap object,width, height, bit depth
color = displayio.Palette(8)  # Create a color palette
color[0] = 0x000000  # black background
color[1] = 0x0000ff
color[2] = 0x006fff
color[3] = 0x009bff
color[4] = 0x00baff
color[5] = 0x00d5d8
color[6] = 0x00ed80
color[7] = 0x00ff00

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)
group.append(tile_grid)  # Add the TileGrid to the Group
display.show(group)

font = terminalio.FONT
#     font = bitmap_font.load_font("/DePixelHalbfett.bdf")


clock_label = Label(font)
clock_label_minute = Label(font)
clock_label_when = Label(font)
clock_label_hour = Label(font)

def calculate_minute(min_val: int) -> tuple:
    """turn a minute value into a time string

    Args:
        min_val (int): the current minute value

    Returns:
        tuple: the equivalent time string, past/to wording, and whether to add one to the hour
    """
    # hat tip to https://github.com/andydoro/WordClock-NeoMatrix8x8 for the idea & code
    # there's probably a more Pythonic way to do this, but eff it, it works
    if min_val < 5:
        min_string = ""
        past_to = ""
        hour_adjust = 0
    if min_val >= 5 and min_val < 10:
        min_string = "five"
        past_to = "past"
        hour_adjust = 0
    if min_val >= 10 and min_val < 15:
        min_string = "ten"
        past_to = "past"
        hour_adjust = 0
    if min_val >= 15 and min_val < 20:
        min_string = "quarter"
        past_to = "past"
        hour_adjust = 0
    if min_val >= 20 and min_val < 25:
        min_string = "twenty"
        past_to = "past"
        hour_adjust = 0
    if min_val >= 25 and min_val < 30:
        min_string = "twenty-five"
        past_to = "past"
        hour_adjust = 0
    if min_val >= 30 and min_val < 35:
        min_string = "half"
        past_to = "past"
        hour_adjust = 0
    if min_val >= 35 and min_val < 40:
        min_string = "twenty-five"
        past_to = "to"
        hour_adjust = 1
    if min_val >= 40 and min_val < 45:
        min_string = "twenty"
        past_to = "to"
        hour_adjust = 1
    if min_val >= 45 and min_val < 50:
        min_string = "quarter"
        past_to = "to"
        hour_adjust = 1
    if min_val >= 50 and min_val < 55:
        min_string = "ten"
        past_to = "to"
        hour_adjust = 1
    if min_val >= 55 and min_val < 60:
        min_string = "five"
        past_to = "to"
        hour_adjust = 1
    return min_string, past_to, hour_adjust


def calculate_hour(hr_val: int) -> str:
    """turn an hour into its numeric equivalent without importing num2word

    Args:
        hr_val (int): the current hour value

    Returns:
        str: the equivalent word
    """
    # "borrowed" from:
    # https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-without-using-num2word-library
    n2w = {
        0: "midnight",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "noon",
    }
    return n2w[hr_val]



def update_time():

    today = ds3231.datetime
    if today.tm_hour >= 18 or today.tm_hour <= 6:  # evening hours to morning
        clock_label_minute.color = color[1]
        clock_label_when.color = color[1]
        clock_label_hour.color = color[1]
    elif today.tm_hour == 7 or today.tm_hour == 17:
        clock_label_minute.color = color[2]
        clock_label_when.color = color[2]
        clock_label_hour.color = color[2]
    elif today.tm_hour == 8 or today.tm_hour == 16:
        clock_label_minute.color = color[3]
        clock_label_when.color = color[3]
        clock_label_hour.color = color[3]
    elif today.tm_hour == 9 or today.tm_hour == 15:
        clock_label_minute.color = color[4]
        clock_label_when.color = color[4]
        clock_label_hour.color = color[4]
    elif today.tm_hour == 10 or today.tm_hour == 14:
        clock_label_minute.color = color[5]
        clock_label_when.color = color[5]
        clock_label_hour.color = color[5]
    elif today.tm_hour == 11 or today.tm_hour == 13:
        clock_label_minute.color = color[6]
        clock_label_when.color = color[6]
        clock_label_hour.color = color[6]
    else:
        clock_label_minute.color = color[7]
        clock_label_when.color = color[7]
        clock_label_hour.color = color[7]

    twelve_hour = today.tm_hour - 12 if today.tm_hour > 12 else today.tm_hour

    (minute_word, when, next_hour) = calculate_minute(today.tm_min)
    our_hour = twelve_hour + next_hour
    our_hour = 1 if our_hour == 13 else our_hour
    hour_word = calculate_hour(our_hour)

    clock_label_minute.text = "{minute_word}".format(
        minute_word=minute_word
    )
    clock_label_when.text = "{when}".format(
        when=when
    )
    clock_label_hour.text = "{hour_word}".format(
        hour_word=hour_word
    )
    bbx_minute, bby_minute, bbwidth_minute, bbh_minute = clock_label_minute.bounding_box
    bbx_when, bby_when, bbwidth_when, bbh_when = clock_label_when.bounding_box
    bbx_hour, bby_hour, bbwidth_hour, bbh_hour = clock_label_hour.bounding_box
    # Center the label
    clock_label_minute.x = round(display.width / 2 - bbwidth_minute / 2)
    clock_label_minute.y = 4
    clock_label_when.x = round(display.width / 2 - bbwidth_when / 2)
    clock_label_when.y = 15
    clock_label_hour.x = round(display.width / 2 - bbwidth_hour / 2)
    clock_label_hour.y = 26
#     if DEBUG:
#         print("Label bounding box: {},{},{},{}".format(bbx, bby, bbwidth, bbh))
#         print("Label x: {} y: {}".format(clock_label.x, clock_label.y))


last_check = None
update_time()  # Display whatever time is on the board
# group.append(clock_label)  # add the clock label to the group
group.append(clock_label_minute)  # add the clock label to the group
group.append(clock_label_when)  # add the clock label to the group
group.append(clock_label_hour)  # add the clock label to the group

while True:
    if last_check is None or time.monotonic() > last_check + 3600:
        try:
            update_time()  # Make sure a colon is displayed while updating
#             network.get_local_time()  # Synchronize Board's clock to Internet
            last_check = time.monotonic()
        except RuntimeError as e:
            print("Some error occured, retrying! -", e)

    update_time()
    time.sleep(1)
