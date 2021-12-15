#!/usr/bin/env python3

import random
import sys

"""
Stanford CS106A Mimic Project.
"""


# --- Define your functions here ---


def bigrams(filename):
    """
    Given a text file, returns a dictionary with the words as the keys and their following words as the values.
    >>> bigrams('test-roses.txt')
    {'': ['Roses'], 'Roses': ['are'], 'are': ['red', 'blue.'], 'red': ['violets'], 'violets': ['are']}
    >>> bigrams('test-tiny.txt')
    {'': ['a'], 'a': ['b', 'c.'], 'b': ['a']}
    """
    with open(filename, 'r') as f:
        text = f.read()       # reads entire file into 1 string
        words = text.split()  # as above, use split()
        dictionary = {}
        previous = ''
        for word in words:
            if previous not in dictionary:
                dictionary[previous] = []
            dictionary[previous].append(word)
            previous = word
    return dictionary


def random_choice(dictionary, word):
    """
    Given a word, returns a random word that follows it.
    """
    import random
    random_word = random.choice(dictionary[word])
    return random_word


def print_dict(filename, limit_num):
    """
    Given a filename, returns a string of randomly selected words following each word until the limit number is reached.
    """
    count = 0
    word = ''
    dictionary = bigrams(filename)
    story = ''
    while count <= int(limit_num) or (count >= int(limit_num) and not word.endswith('.' or ',')):
        print_word = random_choice(dictionary, word)
        story += print_word + ' '
        word = print_word
        if word not in dictionary:
            word = ''
        count += 1
    print(story)


def main():
    args = sys.argv[1:]
    # Two possible command-line forms:
    # filename
    # filename limit_num
    limit_num = 25  # default minimum value
    filename = args[0]
    if len(args) == 1:
        print_dict(filename, limit_num)
    if len(args) == 2:
        limit_num = args[1]
        print_dict(filename, args[1])


if __name__ == '__main__':
    main()

