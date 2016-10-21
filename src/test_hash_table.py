# -*- coding utf-8 -*-

from collections import namedtuple
import pytest
from hash_table import HashTable


HTFix = namedtuple(
    'HTFixture',
    ('table', 'word')
)


@pytest.fixture(scope='function',)
def ht(request):
    '''fixture for hash table tests'''
    from hash_table import HashTable
    dict_size = 260000
    table = HashTable(dict_size)
    dictionary = '/usr/share/dict/words'
    f = open(dictionary, 'r')
    for item in f:
        if isinstance(item, bytes):
            item = item.decode('utf-8')
        word = item.rstrip('\n')
        table.set(word, word)
    f.close()

    return HTFix(table, word)


def test_simple_hash_func_returns_int():
    from hash_table import simple_hash
    integer = simple_hash('string', 1024)
    assert isinstance(integer, int)


def test_bp_hash_func_returns_int():
    from hash_table import bp_hash
    integer = bp_hash('string', 1024)
    assert isinstance(integer, int)


def test_hash_table_init():
    """Test hash table initializes correctly."""
    ht = HashTable(1024)
    assert isinstance(ht, HashTable)


def test_hash_table_init_buckets():
    """Test hash table creates correct number of buckets."""
    ht = HashTable(1024)
    assert len(ht._buckets) == 1024


def test_hash_table_init_hash_method_error():
    """Test to ensure error is raised when attempting to use an unregistered
    hash function.
    """
    with pytest.raises(TypeError):
        HashTable({})


def test_hash_table_hash_method():
    """Test to ensure hash table intializes with simple_hash function"""
    # ht = HashTable(1024)
    # assert ht.hash_func == simple_hash


def test_hash_table_set_error():
    """Test to ensure KeyError is raised from by a non-string input"""
    ht = HashTable(1024)
    import pdb; pdb.set_trace()
    with pytest.raises(TypeError):
        ht.set(1, 2)


# @pytest.mark.parametrize('hash_func', HASH_FUNCTIONS)
def test_hash_word_list(ht):
    """
    Full test of hash table with user dictionary
    """
    assert ht.table.get(ht.word) == ht.word
