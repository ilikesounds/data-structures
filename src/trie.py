# -*- coding: utf-8 -*-
"""The following code implements a trie tree in python."""

END = '$'


class Trie(object):
    """Implement Trie tree class with supporting methods."""

    def __init__(self):
        """Initializes an empty Trie tree."""
        self.tokens = {}

    def insert(self, token):
        """Inserts a new token into our trie tree."""
        tokens = self.tokens
        if not isinstance(token, str):
            raise TypeError("Input must be a string.")
        if END in token:
            raise ValueError("Input must not contain $ character.")
        for char in token:
            tokens = tokens.setdefault(char, {})
        tokens[END] = True

    def contains(self, token):
        """Returns true if token is in trie, false if not."""
        if not isinstance(token, str):
            raise TypeError("Input must be a string.")
        if END in token:
            raise ValueError("Input must not contain $ character.")
        tokens = self.tokens
        for char in token:
            if char not in tokens:
                return False
            tokens = tokens[char]
        return tokens.get(END, False)

    def traversal(self, start):
        """Performs a depth-first traversal of our trie beginning at the
        string we specify as start"""
        if not isinstance(start, str):
            raise TypeError("Input must be a string.")
        if END in start:
            raise ValueError("Input must not contain $ character.")
        tokens = self.tokens
        for char in start:
            if char in tokens:
                tokens = tokens[char]
        stepping_list = []
        stepping_list.append((tokens, ""))
        while stepping_list:
            next_chars, word = stepping_list.pop()
            if END in tokens:
                yield start + word
            for char in next_chars:
                if char is not END:
                    stepping_list.append((next_chars[char], start + char))
