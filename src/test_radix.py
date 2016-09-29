# -*- coding: utf-8 -*-
"""File tests our radix sort."""
from __future__ import unicode_literals
import pytest


def test_radix_no_input():
    """Test radix sort with no input."""
    from radix import radix_sort
    with pytest.raises(TypeError):
        radix_sort()


def test_radix_not_list_input():
    """Test radix sort without a list input."""
    from radix import radix_sort
    with pytest.raises(TypeError) as message:
        radix_sort("I'm a string")
    assert "Radix sort only accepts inputs inside a Python list." in str(message)


def test_radix_list_not_ints():
    """Test radix sort with a list that isn't full of ints."""
    from radix import radix_sort
    test_list = [7, 4, "taco", "burrito", 5, 9, "horsie"]
    with pytest.raises(TypeError) as message:
        radix_sort(test_list)
    assert "All the items in your list must be integers." in str(message)


def test_radix_correct_short_input():
    from radix import radix_sort
    test_list = [5, 4, 47, 3, 22]
    output = test_list[:]
    assert radix_sort(test_list) == sorted(output)


def test_radix_correct_input_already_ordered():
    from radix import radix_sort
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert radix_sort(test_list) == test_list


def test_radix_correct_input_unordered():
    from radix import radix_sort
    test_list = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    output = test_list[:]
    assert radix_sort(test_list) == sorted(output)


def test_radix_correct_input_long_random():
    from radix import radix_sort
    pass
