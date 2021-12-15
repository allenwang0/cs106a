#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def key_slug(key):
    """
    Given a key string, return the len-26 slug list for it.
    >>> key_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> key_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> key_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> key_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    slug = []
    for ch in key:
        low = ch.lower()
        if low.isalpha() and low not in slug:
            slug.append(low)
    for ch in ALPHABET:
        if ch not in slug:
            slug.append(ch)
    return slug


def encrypt_char(source, slug, char):
    """
    Given source and slug lists,
    if char is in source return
    its encrypted form, otherwise
    return it unchanged.
    # Using 'z' slug for testing.
    # Can set a var within a Doctest like this.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> encrypt_char(ALPHABET, slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, slug, 'd')
    'c'
    >>> encrypt_char(ALPHABET, slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, slug, '\\n')
    '\\n'
    """
    result = ''
    low = char.lower()
    if low in source:
        posit = source.index(low)
        if char.islower():
            result = slug[posit]
        if char.isupper():
            result = slug[posit].upper()
        return result
    if low not in source:
        return char


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> encrypt_str(ALPHABET, slug, 'And like a thunderbolt he falls.\\n')
    'Zmc khjd z sgtmcdqanks gd ezkkr.\\n'
    """
    result = ''
    for ch in s:
        result += encrypt_char(source, slug, ch)
    return result


def decrypt_str(source, slug, s):
    """
    Given source and slug lists, and encrypted string s,
    return the decrypted form of s.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> decrypt_str(ALPHABET, slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.\\n')
    'And like a thunderbolt he falls.\\n'
    """
    return encrypt_str(slug, source, s)



def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    with open(filename, 'r') as f:
        for line in f:
            slug = key_slug(key)
            result = ''
            for ch in line:
                result += encrypt_str(ALPHABET, slug, ch)
            print(result)


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    with open(filename, 'r') as f:
        for line in f:
            slug = key_slug(key)
            result = ''
            for ch in line:
                result += decrypt_str(ALPHABET, slug, ch)
            print(result)


def main():
    args = sys.argv[1:]
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    if len(args) == 3 and args[0] == '-encrypt':
        encrypt_file(args[2], args[1])
    if len(args) == 3 and args[0] == '-decrypt':
        decrypt_file(args[2], args[1])


# Python boilerplate.
if __name__ == '__main__':
    main()
