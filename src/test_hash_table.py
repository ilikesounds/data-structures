
# -*- coding utf-8 -*-

import pytest
from hash_table import simple_hash, bp_hash, HashTable

HASH_FUNCTIONS = [simple_hash, bp_hash]
STRING_HASH = ['s', 'bp']

# @pytest.mark.parametrize('s', HASH_FUNCTIONS)


@pytest.mark.parametrize('hash_func', HASH_FUNCTIONS)
def test_hash_func_returns_int(hash_func):
    integer = hash_func('string', 1024)
    assert isinstance(integer, int)


def test_hash_table_init():
    """Test hash table initializes correctly."""
    ht = HashTable()
    assert isinstance(ht, HashTable)


def test_hash_table_init_buckets():
    """Test hash table creates correct number of buckets."""
    ht = HashTable()
    assert len(ht._buckets) == 1024


def test_hash_table_init_hash_method_error():
    """Test to ensure error is raised when attempting to use an unregistered
    hash function.
    """
    with pytest.raises(TypeError):
        HashTable(0)
