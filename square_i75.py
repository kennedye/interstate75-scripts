"""
square_i75.py
draw some rectangles
make 'em bounce
"""
import time
import board # pylint: disable=import-error
import displayio # pylint: disable=import-error
import framebufferio # pylint: disable=import-error
import rgbmatrix # pylint: disable=import-error


def make_rect(color, width, height):
    """
    create a "rounded" rectangle and return it as a single TileGrid
    """
    h_start = w_start = 0
    h_end = height - 1
    w_end = width - 1

    palette1 = displayio.Palette(3)
    palette1[0] = (color[0], color[1], color[2])
    palette1[1] = (int(color[0] * 0.1), int(color[1] * 0.1), int(color[2] * 0.1))
    palette1[2] = (0, 0, 0)
    bitmap1 = displayio.Bitmap(width, height, 3)

    bitmap1[w_start + 1, h_start] = 1
    bitmap1[w_end - 1, h_start] = 1
    bitmap1[w_start, h_start + 1] = 1
    bitmap1[w_end, h_start + 1] = 1
    bitmap1[w_start, h_end - 1] = 1
    bitmap1[w_end, h_end - 1] = 1
    bitmap1[w_start + 1, h_end] = 1
    bitmap1[w_end - 1, h_end] = 1

    bitmap1[w_start, h_start] = 2
    bitmap1[w_start, h_end] = 2
    bitmap1[w_end, h_start] = 2
    bitmap1[w_end, h_end] = 2

    return displayio.TileGrid(bitmap1, pixel_shader=palette1)


def move_down(rect):
    """
    move a rectangle's Group down (todo: add gravity?)
    """
    for i in range(10):
        time.sleep(0.025)
        rect.y = i


def move_up(rect):
    """
    move a rectangle's Group up (todo: add gravity?)
    """
    for i in range(9, -1, -1):
        time.sleep(0.025)
        rect.y = i


def main():
    """
    they call it main.
    """
    # get rid of any pre-existing display
    displayio.release_displays()

    # interstate75 64x32
    matrix = rgbmatrix.RGBMatrix(
        width=64,
        height=32,
        bit_depth=4,
        rgb_pins=[board.R0, board.G0, board.B0, board.R1, board.G1, board.B1],
        addr_pins=[board.ROW_A, board.ROW_B, board.ROW_C, board.ROW_D],
        clock_pin=board.CLK,
        latch_pin=board.LAT,
        output_enable_pin=board.OE,
    )

    display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

    group_main = displayio.Group()
    display.show(group_main)

    color1 = (255, 165, 0)
    color2 = (173, 216, 230)
    color3 = (0, 255, 0)
    width = height = 20

    tile_grid1 = make_rect(color1, width, height)
    group1 = displayio.Group()
    group1.append(tile_grid1)

    group1.x = 0
    group1.y = 0

    tile_grid2 = make_rect(color2, width, height)
    group2 = displayio.Group()
    group2.append(tile_grid2)

    group2.x = 21
    group2.y = 0

    tile_grid3 = make_rect(color3, width, height)
    group3 = displayio.Group()
    group3.append(tile_grid3)

    group3.x = 42
    group3.y = 0

    group_main.append(group1)
    group_main.append(group2)
    group_main.append(group3)

    time.sleep(2)

    while True:
        move_down(group1)
        move_down(group2)
        move_down(group3)
        move_up(group1)
        move_up(group2)
        move_up(group3)


if __name__ == "__main__":
    main()
