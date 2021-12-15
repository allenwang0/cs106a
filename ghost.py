#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    >>> pix_dist2((40, 50, 60), (60, 70, 80))
    1200
    >>> pix_dist2((40, 50, 60), (40, 50, 60))
    0
    >>> pix_dist2((10, 200, 10), (5, 5, 5))
    38075
    """
    return (pix1[0]-pix2[0]) ** 2 + (pix1[1]-pix2[1]) ** 2 + (pix1[2]-pix2[2]) ** 2


def average_pix(pixs):
    """
    Given a list of 3 or more pix, returns the average pix.
    >>> average_pix([(1, 1, 1), (2, 2, 2), (3, 3, 3)])
    (2, 2, 2)
    >>> average_pix([(30, 30, 30), (50, 50, 50), (100, 100, 100)])
    (60, 60, 60)
    """
    pix_r = 0
    for pix in pixs:
        pix_r += pix[0]
    pix_g = 0
    for pix in pixs:
        pix_g += pix[1]
    pix_b = 0
    for pix in pixs:
        pix_b += pix[2]
    return (pix_r//len(pixs), pix_g//len(pixs), pix_b//len(pixs))


def best_pix(pixs):
    """
    Given a list of 3 or more pix, returns the best pix.
    >>> best_pix([(1,1,1), (1, 1, 1), (28, 28, 28)])
    (1, 1, 1)
    >>> best_pix([(5, 5, 5), (6, 6, 6), (29, 29, 29)])
    (6, 6, 6)
    """
    return min(pixs, key=lambda pix: pix_dist2(pix, average_pix(pixs)))


def solve(images):
    """
    Given a list of image objects, compute and show
    a Ghost solution image based on these images.
    There will be at least 3 images and they will all be
    the same size.
    """

    solution = SimpleImage.blank(images[0].width, images[0].height)
    for y in range(images[0].height):
        for x in range(images[0].width):
            pixs = []
            for image in images:
                pixel = image.get_pix(x, y)
                pixs.append(pixel)
            best = best_pix(pixs)
            solution.set_pix(x, y, best)
    solution.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    if len(args) == 1:
        images = load_images(args[0])
        solve(images)


if __name__ == '__main__':
    main()
