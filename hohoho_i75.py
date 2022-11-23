"""
hohoho_i75.py
xmas tree!
"""
import time
import random
import board  # pylint: disable=import-error
import displayio  # pylint: disable=import-error
import framebufferio  # pylint: disable=import-error
import rgbmatrix  # pylint: disable=import-error
from ulab import numpy as np # pylint: disable=import-error


def make_tree() -> displayio.TileGrid:
    """
    create the standard tree
    """

    base_tree = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 1, 1, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 3, 3, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 1, 1, 4, 1, 1, 4, 1, 1, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 4, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 3, 4, 4, 3, 4, 4, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 0, 0, 0, 0],
            [0, 0, 1, 2, 2, 2, 2, 3, 1, 3, 4, 4, 4, 1, 4, 4, 4, 1, 1, 4, 4, 4, 1, 4, 1, 4, 3, 3, 1, 0, 0, 0],
            [0, 0, 1, 2, 2, 2, 1, 1, 0, 1, 4, 1, 1, 5, 1, 4, 1, 5, 5, 1, 4, 1, 0, 1, 0, 1, 3, 3, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 6, 5, 5, 1, 5, 5, 5, 6, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 5, 5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 5, 5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 5, 5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], dtype=np.uint8
    )
    tree_size = base_tree.shape # should be (32, 40)

    palette1 = displayio.Palette(7)
    palette1[0] = (0, 0, 0)  # black
    palette1[1] = (127, 127, 127)  # gray
    palette1[2] = (0, 32, 0)  # dark green
    palette1[3] = (0, 96, 0)  # less dark green
    palette1[4] = (0, 255, 0)  # green
    palette1[5] = (92, 64, 51)  # light brown
    palette1[6] = (181, 101, 29)  # dark brown

    bitmap1 = displayio.Bitmap(tree_size[0], tree_size[1], 7)

    for i in range(tree_size[0]):
        for j in range(tree_size[1]):
            bitmap1[i, j] = base_tree[i, j]

    return displayio.TileGrid(bitmap1, pixel_shader=palette1)

def make_lights() -> displayio.TileGrid:
    """
    light random pixels on an overlay tile to emulate lights
    """
    palette1 = displayio.Palette(3)
    palette1[0] = (255, 0, 0) # red
    palette1[1] = (255, 255, 0) # yellow
    palette1[2] = (0, 0, 255) # blue

    # set some points on the tree to random colors
    bitmap1 = displayio.Bitmap(1, 1, 3)
    bitmap1[0, 0] = random.randint(0, 2)
    return displayio.TileGrid(bitmap1, pixel_shader=palette1)

# def move_down(rect: displayio.Group()) -> None:
#     """
#     move a rectangle's Group down (todo: add gravity?)
#     """
#     for i in range(10):
#         time.sleep(0.025)
#         rect.y = i


# def move_up(rect: displayio.Group()) -> None:
#     """
#     move a rectangle's Group up (todo: add gravity?)
#     """
#     for i in range(9, -1, -1):
#         time.sleep(0.025)
#         rect.y = i


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

    tree_grid = make_tree()
    tree_group = displayio.Group()
    tree_group.append(tree_grid)

    tree_group.x = 0
    tree_group.y = 0

    group_main.append(tree_group)

    time.sleep(3)

    lights = [
        (9, 16),
        (13, 14),
        (15, 18),
        (18, 11),
        (19, 16),
        (20, 19),
        (22, 14),
        (25, 9),
        (26, 17),
        (28, 12),
        (29, 7),
        (29, 22),
        (30, 19),
        (32, 11),
        (32, 21)
    ]
    while True:
        for i, _ in enumerate(lights):
            light_grid = make_lights()
            light_group = displayio.Group()
            light_group.append(light_grid)
            light_group.x = lights[i][0]
            light_group.y = lights[i][1]
            group_main.append(light_group)
        time.sleep(1)
        for i, _ in enumerate(lights):
            group_main.pop()


if __name__ == "__main__":
    main()
