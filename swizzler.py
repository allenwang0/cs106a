#!/usr/bin/env python3

"""
Stanford CS106A Swizzler project
"""

import sys

# --define helper functions here--

def end(s):
    """
    This function returns the index of the third alpha character in the string
    >>> end('***Happy.')
    5
    >>> end('--birthday!')
    4
    >>> end('year-old')
    2
    >>> end('')
    False
    >>> end('a')
    False
    >>> end('amazing')
    2
    >>> end('Tennyson')
    2
    """
    for ch in s:
        if len(s) > 2 and ch.isalpha():
            return s.index(ch) + 2
    return False

def start(s):
    """
    This helper function returns the index of the second to last alpha character in the string
    >>> start('***Happy.')
    6
    >>> start('--birthday!')
    8
    >>> start('year-old')
    6
    >>> start('')
    False
    >>> start('a')
    False
    >>> start('amazing')
    5
    >>> start('Wheeeeeeeeeeeeeeeee')
    17
    """
    if len(s) < 2:
        return False
    for i in range(len(s)):
        last = len(s) - i - 2
        ch = s[len(s) - i - 1]
        if ch.isalpha():
            return last


def middle(s):
    """
    This function returns the part of the word starting with the second to last letter, which
    is end, and ends at the letter with index 2 which is the start.
    >>> middle('***Happy.')
    'pp'
    >>> middle('--birthday!')
    'adhtr'
    >>> middle('year-old')
    'lo-ra'
    >>> middle('')
    ''
    >>> middle('a')
    'a'
    >>> middle('amazing')
    'niza'
    >>> middle('Tennyson')
    'osynn'
    """
    reverse_s = s[end(s):start(s)+1]
    return reverse_s[len(s)::-1]


def swizzle(s):
    """
    Compute and return the swizzled version of string s.
    This is complicated, but can make heavy use of decomposed functions.
    No loops are required in this function.
    >>> swizzle('++Python!')
    '++Pyohtn!'
    >>> swizzle('^^^abcdefg$$$')
    '^^^abfedcg$$$'
    >>> swizzle('^ad-hoc$')
    '^adoh-c$'
    >>> swizzle('$^-@')  # 100% punctuation
    '$^-@'
    >>> swizzle('abcde')
    'abdce'
    >>> swizzle('abcd')
    'abcd'
    >>> swizzle('a')
    'a'
    """
    if not end(s):
        return s
    result = ''
    result += s[:end(s)]
    result += middle(s)
    result += s[start(s)+1:len(s)]
    return result


def swizzle_file(filename):
    """
    (provided code)
    Print out the contents of the given filename
    with each of its words swizzled.
    Works by splitting each line into "words",
    calling the swizzle() function to compute
    the swizzled version of each word for printing.
    """
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                swizzled = swizzle(word)
                print(swizzled + ' ', end='')
            print()  # print '\n' at end of each line


def main():
    """
    (provided code)
    The 1 command line argument is the file to process.
    Calls swizzle_file() with this filename to print it out.
    """
    args = sys.argv[1:]
    if len(args) == 1:
        swizzle_file(args[0])


# Python boilerplate
if __name__ == '__main__':
    main()
