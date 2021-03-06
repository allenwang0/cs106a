#!/usr/bin/env python3

"""
Stanford CS106A Stripey Data Project
"""

import sys
from drawcanvas import DrawCanvas


DELTA = 127
BASE = 127


def draw_stripes(width, height, fracs, title):
    """
    Create a canvas of the given width and height.
    Draw the fracs data and title on the canvas.
    """
    x = 0
    y = 0
    num_loops = 0
    rect_width = width // len(fracs)
    rect_height = height
    canvas = DrawCanvas(width, height, title='Stripey')
    for frac in fracs:
        r = BASE + DELTA * frac
        g = BASE
        b = BASE - DELTA * frac
        canvas.fill_rect(x + num_loops * rect_width, y, x + (num_loops + 1) * rect_width, rect_height, color=(r, g, b))
        num_loops += 1
    canvas.draw_string(5, 5, title, color='white')




def read_fracs(filename):
    """
    (provided)
    Given filename, read in and return a list
    of the "fracs" data values.
    Oddity: the index-0 element is the
    string title of this data set,
    the rest of the elements are the float values.
    """
    fracs = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        # First line is title
        fracs.append(lines.pop(0))
        # Process other lines as floats
        for line in lines:
            fracs.append(float(line))
        return fracs


def main():
    # (provided)
    args = sys.argv[1:]

    # Default window size is 800 by 400
    # Optionally command line can have width height numbers to override
    width = 800
    height = 400
    if len(args) == 3:
        width = int(args[len(args) - 2])
        height = int(args[len(args) - 1])

    if len(args) >= 1:
        fracs = read_fracs(args[0])
        title = fracs.pop(0)
        draw_stripes(width, height, fracs, title)

    DrawCanvas.mainloop()


if __name__ == '__main__':
    main()
