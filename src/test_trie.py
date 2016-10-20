# -*- coding: utf-8 -*-
"""The following code tests our trie tree implementation."""
import pytest


def test_trie_class_init():
    """Test that the Trie class inits correctly."""
    from trie import Trie
    tree = Trie()
    assert tree.tokens == {}


def test_trie_insert_one():
    """verify that insertion of a string with 1 char works"""
    from trie import Trie
    tree = Trie()
    tree.insert('a')
    assert tree.tokens['a'] == {'$': True}


def test_trie_insert_two():
    """verify that insertion of two chars works"""
    from trie import Trie
    tree = Trie()
    tree.insert('ab')
    assert tree.tokens['a'] == {'b': {'$': True}}


def test_trie_insert_wrong_type():
    """verify that trie throws error if input not a string"""
    from trie import Trie
    tree = Trie()
    with pytest.raises(TypeError) as message:
        tree.insert(14)
    assert "Input must be a string." in str(message)


def test_trie_insert_dollarsign():
    """verify that trie throws error if $ in input"""
    from trie import Trie
    tree = Trie()
    with pytest.raises(ValueError) as message:
        tree.insert("super$trong")
    assert "Input must not contain $ character." in str(message)


def test_trie_contains_true():
    """verify that trie returns true if trie contains string we're
    looking for"""
    from trie import Trie
    tree = Trie()
    tree.insert("string")
    assert tree.contains("string")


def test_trie_contains_false():
    """verify trie returns false if trie does not contain the string we're
    looking for"""
    from trie import Trie
    tree = Trie()
    tree.insert("bob")
    assert not tree.contains("bobcat")


def test_trie_contains_partial_word():
    """verify that trie returns false if searching for part of a word when
    the full word is in the trie"""
    from trie import Trie
    tree = Trie()
    tree.insert("pythonic")
    assert not tree.contains("pyth")


def test_trie_contains_wrong_input():
    """verify trie throws error if input isn't a string"""
    from trie import Trie
    tree = Trie()
    with pytest.raises(TypeError) as message:
        tree.insert(2)
    assert "Input must be a string." in str(message)


def test_trie_contains_dollarsign():
    """verify trie throws error if input contains $"""
    from trie import Trie
    tree = Trie()
    with pytest.raises(ValueError) as message:
        tree.insert("dmoney$")
    assert "Input must not contain $ character." in str(message)


def test_trie_traverse_wrong_input():
    """verify trie throws error if input isn't a string"""
    from trie import Trie
    tree = Trie()
    with pytest.raises(TypeError) as message:
        tree.insert(287)
    assert "Input must be a string." in str(message)


def test_trie_traverse_dollarsign():
    """verify trie throws error if input contains $"""
    from trie import Trie
    tree = Trie()
    with pytest.raises(ValueError) as message:
        tree.insert("I'm$uperthanksforasking")
    assert "Input must not contain $ character." in str(message)
