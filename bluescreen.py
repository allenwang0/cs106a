#!/usr/bin/env python3

"""
Stanford Bluescreen Example
Shows front and back strategies

Front strategy:
$ python3 bluescreen.py monkey-500.jpg moon-600.jpg
$ python3 bluescreen.py monkey-500.jpg stanford-600.jpg

Back strategy:
$ python3 bluescreen.py monkey-500.jpg 200 stanford-600.jpg
$ python3 bluescreen.py monkey-500.jpg 50 stanford-600.jpg

"""

import sys
from simpleimage import SimpleImage


def do_front(front_filename, back_filename):
    """
    Front strategy: loop over front image,
    detect blue pixels there,
    substitute in pixels from back.
    Return changed front image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) // 3
            # front: replace blue pixels
            if pixel.green >= average * 0.999:
                back_pixel = back.get_pixel(x, y)
                pixel.red = back_pixel.red
                pixel.green = back_pixel.green
                pixel.blue = back_pixel.blue
    return image


def do_back(front_filename, shift_x, back_filename):
    """
    Back strategy: loop over image,
    detect *non-blue* pixels.
    Copy those pixels to back, shifted by shift_x.
    Return changed back image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) // 3
            # back: copy non-blue pixels to background
            if pixel.blue < average * 0.9:
                dst_x = x + shift_x
                dst_y = y
                # Only copy pixels to back if they will be in-bounds
                if back.in_bounds(dst_x, dst_y):
                    back_pixel = back.get_pixel(dst_x, dst_y)
                    back_pixel.red = pixel.red
                    back_pixel.green = pixel.green
                    back_pixel.blue = pixel.blue
    return back



def main():
    args = sys.argv[1:]

    # args:
    # front-image back-image         - do front strategy
    # front-image shift-x back-image - do back strategy

    if len(args) == 2:
        image = do_front(args[0], args[1])
        image.show()

    if len(args) == 3:
        image = do_back(args[0], int(args[1]), args[2])
        image.show()


if __name__ == '__main__':
    main()
