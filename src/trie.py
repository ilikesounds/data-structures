# -*- coding: utf-8 -*-
"""
The following code implements a trie tree in python.

Thanks to David Banks for help with the insert and contains methods:
https://github.com/crashtack/data-structures/tree/trie
"""

END = '$'


class Node(object):
    """Implements nodes for our Trie tree."""

    def __init__(self, value=None):
        """Creates an instance of our trie node class."""
        self.value = value
        self.next = []

    def __eq__(self, other):
        """Method to check and compare if a letter is next"""
        return self.value == other

    def _insert(self, word):
        """Insert a letter into letter list if there's a next value"""
        try:
            letter = Node(word[0])
        except IndexError:
            if END not in self.next:
                self.next.append(Node(END))
            return
        if letter not in self.next:
            self.next.append(letter)
        index = self.next.index(letter)
        self.next[index]._insert(word[1:])

    def _contains(self, word):
        """Check if next letter. Pass remaining word fragment to next node."""
        try:
            letter = word[0]
        except IndexError:
            if END in self.next:
                return True
            else:
                return False
        if END in self.next:
            index = self.next.index(letter)
            return self.next[index]._contains(word[1:])
        else:
            return False


class Trie(object):
    """Trie tree class with supporting methods."""

    def __init__(self):
        """Initializes an empty Trie tree."""
        self.root = Node()

    def insert(self, value):
        """Inserts a new value into our trie tree."""
        self.root._insert(value)

    def contains(self, value):
        """Returns true if value is in trie, false if not."""
        return self.root._contains(value)
