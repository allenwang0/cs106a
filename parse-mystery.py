#!/usr/bin/env python3

"""
Stanford CS106A Parse Mystery Project
"""

import sys

# Next line depends on Pillow package
from simpleimage import SimpleImage


def parse_binary(s):
    """
    >>> parse_binary('xx101xx112x010')
    ['101', '112', '010']
    >>> parse_binary('xx0002xx')
    ['0002']
    >>> parse_binary('xx2000xx')
    ['000']

    """
    search = 0
    words = []
    while True:
        begin = search
        while begin < len(s) and not (s[begin] == '0' or s[begin] == '1'):
            begin += 1
        if begin >= len(s):
            break
        end = begin + 1
        while end < len(s) and (s[end] == '0' or s[end] == '1'):
            end += 1
        if end < len(s) and s[end] == '2':
            end += 1
        word = s[begin:end]
        words.append(word)
        search = end
    return words

def reverse(s):
    """
    Given a string including a dollar sign, parse ints out of it,
    returning the int values in reverse order
    >>> reverse('5')
    '5'
    >>> reverse('12345')
    '54321'
    >>> reverse('12349580018234918273')
    '37281943281008594321'
    """
    return s[len(s)::-1]


def parse_line(s):
    """
    Given a string s, parse the ints out of it and
    return them as a list of int values.
    # 3 tiny cases provided to start
    >>> parse_line('1')
    [1]
    >>> parse_line('1$')
    [1]
    >>> parse_line('12$')
    [21]
    >>> parse_line('4567^')
    []
    >>> parse_line('493!345$789^')
    [493, 543]
    >>> parse_line('800!)176^b006$(46$*#63Z*16$*06$z5^')
    [800, 600, 64, 63, 61, 60]
    >>> parse_line('47$ 42^ 18$bj55')
    [74, 81, 55]
    >>> parse_line('166^a56')
    [56]
    """
    search = 0
    number_list = []
    num_normal = ''
    num_dollar = ''
    while True:
        begin = search
        while begin < len(s) and not s[begin].isdigit():
            begin += 1
        if begin >= len(s):
            break
        end = begin + 1
        while end < len(s) and s[end].isdigit():
            end += 1
        num_normal = s[begin:end]
        if end < len(s):
            if s[end] != '$' and s[end] != '^':
                number_list.append(int(num_normal))
            if s[end] == '$':
                num_dollar = reverse(num_normal)
                number_list.append(int(num_dollar))
            if s[end] == '^':
                pass
        else:
            number_list.append(int(num_normal))
        search = end + 1
    return number_list


def parse_file(filename):
    """
    Given filename, parse out and return a list of all that file's
    int values.
    (test provided)
    >>> parse_file('3lines.txt')
    [800, 600, 64, 63, 61, 60, 74, 81, 55, 56]
    """
    numb_list = []
    with open(filename, 'r') as f:
        for line in f:
            result = parse_line(line)
            numb_list.extend(result)
    return numb_list


def solve_mystery(filename):
    """Solve the mystery as described in the handout."""

    # SimpleImage boilerplate provided as a starting point
    numbers = parse_file(filename)
    width = numbers[0]  # correct values needed here
    height = numbers[1]
    list_index = 2
    image = SimpleImage.blank(width, height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            # manipulate pixel in here
            pixel.red = numbers[list_index]
            pixel.blue = pixel.red
            pixel.green = pixel.red
            list_index += 1
    # This displays image on screen
    image.show()


def main():
    # (provided code)
    # Command lines:
    # 1. -nums file.txt -> prints numbers
    # 2. file.txt -> shows image solution
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-nums':
        nums = parse_file(args[1])
        print(nums)
    if len(args) == 1:
        solve_mystery(args[0])


if __name__ == '__main__':
    main()
