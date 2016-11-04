# -*- coding: utf-8 -*-
"""The following code tests our trie tree implementation."""


def test_trie_init():
    """
    Test that Trie Initializes.
    """
    from trie import Trie
    trie = Trie()
    assert trie.root.value is None


def test_trie_insert_one_letter():
    """
    Test that a node with a value inserts into the trie correctly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('I')
    assert 'I' in trie.root.next


def test_trie_insert_two_letter_word_first_letter():
    """
    Test that a node with a value longer than one character inserts into the
    trie and indexes properly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('by')
    assert 'b' in trie.root.next


def test_trie_insert_two_letter_word_second_letter():
    """
    Test that a node with a value longer than one character returns the second
    character proper.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('by')
    assert 'y' in trie.root.next[0].next


def test_trie_insert_two_words():
    """
    Test that a trie with two nodes of the same starting character returns the
    proper second character of the second word.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('I')
    trie.insert('It')
    assert 't' in trie.root.next[0].next


def test_trie_insert_two_words_one_root_count():
    """
    Test that only one root is created for a character.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('I')
    trie.insert('It')
    assert len(trie.root.next) == 1


def test_trie_insert_two_words_two_root_count():
    """
    Test that trie creates two roots for two different starting characters.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('It')
    trie.insert('by')
    assert len(trie.root.next) == 2


def test_trie_insert_two_words_first_root_leaf():
    """
    Test that the second character of first root returns correctly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('It')
    trie.insert('by')
    assert 't' in trie.root.next[0].next


def test_trie_insert_two_words_second_root_leaf():
    """
    Test that second character of second root returns correctly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('It')
    trie.insert('by')
    assert 'y' in trie.root.next[1].next


def test_word_stop_charcter():
    """
    Test that END is added properly to a one character root.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('I')
    assert '$' in trie.root.next[0].next


def test_contains_one_letter_word():
    """
    Test that one character root is found by _contains and returned properly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('I')
    assert trie.contains('I')


def test_contains_two_letter_word():
    """
    Test that two character root and leaf is found by _contains and returned
    properly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('It')
    assert trie.contains('It')


def test_contains_long_word():
    """
    Test that a long string inserts into the trie and is returned by _contains
    properly.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('concentration')
    assert trie.contains('concentration')


def test_contains_doesnt_contain_substring():
    """
    Test that a root is not created improperly when a multi-character string
    is entered into the trie.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('It')
    assert not trie.contains('I')


def test_contains_doesnt_contain_word():
    """
    Test that a matching root for a word not inserted into the Trie is not
    valid when searched for.
    """
    from trie import Trie
    trie = Trie()
    trie.insert('ate')
    assert not trie.contains('at')
