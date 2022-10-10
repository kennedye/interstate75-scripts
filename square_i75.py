"""
sample.py
very basic interstate75 code
not for individual resale
"""
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
from rainbowio import colorwheel

from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect

import time

# get rid of any pre-existing display
displayio.release_displays()

# interstate75 32x32 or 64x32
# bit_depth can be 1 to 6
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=4,
    rgb_pins=[board.R0, board.G0, board.B0, board.R1, board.G1, board.B1],
    addr_pins=[board.ROW_A, board.ROW_B, board.ROW_C, board.ROW_D],
    clock_pin=board.CLK, latch_pin=board.LAT, output_enable_pin=board.OE)

# interstate75 64x64
# matrix = rgbmatrix.RGBMatrix(
#     width=64, height=64, bit_depth=6,
#     rgb_pins=[board.R0, board.G0, board.B0, board.R1, board.G1, board.B1],
#     addr_pins=[board.ROW_A, board.ROW_B, board.ROW_C, board.ROW_D, board.ROW_E],
#     clock_pin=board.CLK, latch_pin=board.LAT, output_enable_pin=board.OE)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

height = width = 20
hb = wb = 0
he = height - 1
we = width - 1

g = displayio.Group()
display.show(g)

def make_rect(color):
    palette1 = displayio.Palette(3)
    palette1[0]=(color[0], color[1], color[2])
    palette1[1]=(int(color[0]*0.1), int(color[1]*0.1), int(color[2]*0.1))
    palette1[2]=(0, 0, 0)
    bitmap1 = displayio.Bitmap(20, 20, 3)
    # bitmap1 = Rect(0, 0, 20, 20, fill=palette1[0])

    bitmap1[wb + 1, hb] = 1
    bitmap1[we - 1, hb] = 1
    bitmap1[wb, hb + 1] = 1
    bitmap1[we, hb + 1] = 1
    bitmap1[wb, he - 1] = 1
    bitmap1[we, he - 1] = 1
    bitmap1[wb + 1, he] = 1
    bitmap1[we - 1, he] = 1

    bitmap1[wb, hb] = 2
    bitmap1[wb, he] = 2
    bitmap1[we, hb] = 2
    bitmap1[we, he] = 2

    return displayio.TileGrid(bitmap1, pixel_shader=palette1)

color1 = (255, 165, 0)
color2 = (173, 216, 230)
color3 = (0, 255, 0)

tile_grid1 = make_rect(color1)
g1 = displayio.Group()
g1.append(tile_grid1)

g1.x = 0
g1.y = 0

tile_grid2 = make_rect(color2)
g2 = displayio.Group()
g2.append(tile_grid2)

g2.x = 21
g1.y = 0

tile_grid3 = make_rect(color3)
g3 = displayio.Group()
g3.append(tile_grid3)

g3.x = 42
g3.y = 0

g.append(g1)
g.append(g2)
g.append(g3)

time.sleep(2)

def move_down(rect):
    for i in range(10):
        time.sleep(0.025)
        rect.y = i

def move_up(rect):
    for i in range(9, -1, -1):
        time.sleep(0.025)
        rect.y = i

while True:  
    move_down(g1)
    move_down(g2)
    move_down(g3)
    move_up(g1)
    move_up(g2)
    move_up(g3)
    
# while True:
#     pass
# time.sleep(10)