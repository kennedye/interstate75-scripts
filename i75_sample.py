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

import time

# get rid of any pre-existing display
displayio.release_displays()

# interstate75 32x32 or 64x32
# bit_depth can be 1 to 6
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=6,
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


g = displayio.Group()



display.show(g)