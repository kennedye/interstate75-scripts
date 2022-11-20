"""
matrix_i75.py
matrix code-like effect
"""
import time
import random
import board # pylint: disable=import-error
import displayio # pylint: disable=import-error
import framebufferio # pylint: disable=import-error
import rgbmatrix # pylint: disable=import-error

def code_line():
    """
    generate a vertical line of pixels
    """
    palette1 = displayio.Palette(8)
    pos = 0
    for i in range(16,128,16):
        palette1[pos] = (0, i, 0)
        pos += 1
    palette1[7] = (255, 255, 255)
    bitmap1 = displayio.Bitmap(1, 8, 8)
    pos = 0
    for i in range(8):
        bitmap1[0, pos] = pos
        pos += 1
    
    return displayio.TileGrid(bitmap1, pixel_shader=palette1)


def main():
    """
    they call it main.
    """
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

    while True:
        group1 = displayio.Group()
        
        tile1 = code_line()
        group1.append(tile1)

        group1.x = random.randint(0, matrix.width)
        group1.y = -8

        g.append(group1)
        display.show(g)

        time.sleep(2)

        pos = group1.y
        for i in range(pos, matrix.height + 8):
            time.sleep(0.05)
            group1.y = i

if __name__ == "__main__":
    main()

