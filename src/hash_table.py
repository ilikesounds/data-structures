# -*- coding: utf-8 -*-
"""
    This module will implement a hash_table on a string input

    This implementation of the hash table was derived from the examples found
    below:

    http://www.laurentluce.com/posts/python-dictionary-implementation/
    http://www.partow.net/programming/hashfunctions/

    Help with correctly selecting the hash function and using bytearray
    came from:

    http://www.github.com/crashtack
"""


def bp_hash(key, size):
    hash_value = 0
    for i in range(len(key)):
        hash_value = (hash_value << 7 ^ ord(key[i])) % size
    return hash_value


def simple_hash(key, size):
    key = bytearray(key.encode())
    hash_value = 0
    for i in key:
        hash_value += i % size
    return hash_value
