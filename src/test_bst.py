# -*- coding: utf-8 -*-
"""File tests a binary search tree data structure."""
from __future__ import unicode_literals

from collections import namedtuple
import pytest
import random
import string

INT_CASES = [random.sample(range(1000),
             random.randrange(2, 100)) for n in range(10)
             ]

STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]

TEST_CASES = INT_CASES + STR_CASES

MyBSTFix = namedtuple(
    'BSTFixture',
    ('bin_tree', 'input_val', 'error_gen', 'length', 'sorted_list')
)
RANDOM_DELETE_SAMPLE = [random.sample(range(-1000, 5000),
                        50) for n in range(20)]


def _random_generator():
    """from a random constant, make a generator for random test values"""
    for sequence in RANDOM_DELETE_SAMPLE:
        for item in sequence:
            yield (item, sequence)


def _bst_tree_checker(node):
    """helper method to check tree for correctness"""
    if node is None:
        return True
    if node.left and node.left.val > node.val:
        return False
    if node.right and node.right.val < node.val:
        return False
    return all([_bst_tree_checker(node.left), _bst_tree_checker(node.right)])


@pytest.fixture(scope='function', params=TEST_CASES)
def full_bst(request):
    '''Return a full bst for testing'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    length = len(request.param)
    sorted_list = sorted(request.param)
    for val in request.param:
        bin_tree.insert(val)
    if request.param or isinstance(request.param[0], int):
        input_val = 999
        error_gen = 'STRING!'
    else:
        input_val = 'STRING!!'
        error_gen - 999
    return MyBSTFix(bin_tree, input_val, error_gen, length, sorted_list)


@pytest.fixture(scope='function', params=[1, 5, 9, 15, 25, 'a', 'd', 'q'])
def empty_bst(request):
    '''Return an empty bst'''
    from bst import BinarySearchTree
    bin_tree = BinarySearchTree()
    return MyBSTFix(bin_tree, request.param, None, None, None)


def test_bst_init_node(empty_bst):
    """test that Node inits w/ val"""
    from bst import Node
    a = Node(empty_bst.input_val)
    assert empty_bst.input_val == a.val


def test_bst_init_node_has_left(empty_bst):
    """test Node picks up arguments and has_left_child == that input"""
    from bst import Node
    a = Node(empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val
             )
    assert a.has_left_child() == empty_bst.input_val


def test_bst_init_node_has_right(empty_bst):
    """test Node picks up arguments and has_right_child == that input"""
    from bst import Node
    a = Node(empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val,
             empty_bst.input_val
             )
    assert a.has_right_child() == empty_bst.input_val


def _test_bst_init_empty_tree(empty_bst):
    """test that empty tree has no root"""
    assert empty_bst.bin_tree.root is None


def test_bst_init_bin_tree():
    """test that tree initialized w/ val gets that val at the root"""
    from bst import BinarySearchTree
    a = BinarySearchTree(1)
    assert a.root.val == 1


def test_bst_insert(empty_bst):
    """test that insert function works on empty bst"""
    empty_bst.bin_tree.insert(empty_bst.input_val)
    assert empty_bst.bin_tree.root.val == empty_bst.input_val


def test_bst_insert_with_existing_node_right(empty_bst):
    """test that insert works with existing node, larger value goes to the
    right"""
    empty_bst.bin_tree.insert(empty_bst.input_val)
    empty_bst.bin_tree.insert(empty_bst.input_val * 2)
    assert empty_bst.bin_tree.root.right


def test_bst_insert_with_existing_node(empty_bst):
    """that that insert works with existing node, smaller value goes to the
    left"""
    empty_bst.bin_tree.insert(empty_bst.input_val * 2)
    empty_bst.bin_tree.insert(empty_bst.input_val)
    assert empty_bst.bin_tree.root.left


def test_bst_find_node_with_one_node_in_tree(empty_bst):
    """test find node with only one node in the tree"""
    empty_bst.bin_tree.insert(empty_bst.input_val)
    result = empty_bst.bin_tree.find_node(empty_bst.input_val)
    assert result.val == empty_bst.input_val


def test_bst_find_node_with_two_node_in_tree(empty_bst):
    """test find node with two nodes in the tree"""
    empty_bst.bin_tree.insert(empty_bst.input_val)
    empty_bst.bin_tree.insert(empty_bst.input_val * 2)
    result = empty_bst.bin_tree.find_node(empty_bst.input_val * 2)
    assert result.val == empty_bst.input_val * 2


def test_bst_find_node_with_three_node_in_tree(empty_bst):
    """test find node with three nodes in the tree"""
    empty_bst.bin_tree.insert(empty_bst.input_val * 10)
    empty_bst.bin_tree.insert(empty_bst.input_val)
    empty_bst.bin_tree.insert(empty_bst.input_val * 5)
    result = empty_bst.bin_tree.find_node(empty_bst.input_val)
    assert result.val == empty_bst.input_val


def test_bst_left_setter_child():
    """test that left child setter works"""
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    assert node1.left.val == node2.val


def test_bst_left_setter_parent():
    """test that left child setter sets parent"""
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    assert node2.parent.val == node1.val


def test_bst_right_setter_child():
    """test rigth child setter works"""
    from bst import Node
    node1 = Node(7)
    node2 = Node(9)
    node1.right = node2
    assert node1.right.val == node2.val


def test_bst_right_setter_parent():
    """test that right child setter sets parent"""
    from bst import Node
    node1 = Node(7)
    node2 = Node(9)
    node1.right = node2
    assert node2.parent.val == node1.val


def test_bst_del_left_child():
    """test deleter on left child"""
    from bst import Node
    node1 = Node(9)
    node2 = Node(7)
    node1.left = node2
    del node1.left
    assert node1.left is None


def test_bst_del_left_child_error():
    """test deleter on left child is None when it should be"""
    from bst import Node
    node1 = Node(9)
    del node1.left
    assert node1.left is None


def test_bst_del_right_child():
    """test deleter on right child"""
    from bst import Node
    node1 = Node(7)
    node2 = Node(9)
    node1.right = node2
    del node1.right
    assert node1.right is None


def test_bst_del_right_child_error():
    """test deleted on right child is None when it should be"""
    from bst import Node
    node1 = Node(9)
    del node1.right
    assert node1.right is None


def test_bst_parent_setter_child_parent():
    """test parent setter works properly"""
    from bst import Node
    node1 = Node(1)
    node2 = Node(2)
    node2.parent = node1
    assert node1.val == node2.parent.val


def test_bst_parent_setter_parent_child_right():
    """test that parent setter sets child right properly"""
    from bst import Node
    node1 = Node(1)
    node2 = Node(2)
    node2.parent = node1
    assert node1.right.val == node2.val


def test_bst_parent_setter_parent_child_left():
    """test that parent setter sets child left properly"""
    from bst import Node
    node1 = Node(2)
    node2 = Node(1)
    node2.parent = node1
    assert node1.left.val == node2.val


def test_bst_in_order_traversal(full_bst):
    """test in order traversal output"""
    results = full_bst.bin_tree.in_order(full_bst.bin_tree.root)
    assert list(results) == full_bst.sorted_list


def test_bst_in_order_traversal_empty_tree(empty_bst):
    """test in order traversal on empty tree"""
    with pytest.raises(IndexError):
        empty_bst.bin_tree.in_order(empty_bst.bin_tree.root)


def test_bst_pre_order_traversal(empty_bst):
    """test pre order traversal output"""
    results = [10, 5, 3, 7, 15, 13, 17]
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    assert list(tree.pre_order()) == results


def test_bst_pre_order_traversal_empty_tree(empty_bst):
    """test pre order traversal on empty tree"""
    with pytest.raises(IndexError):
        empty_bst.bin_tree.pre_order()


def test_bst_post_order_traversal(empty_bst):
    """test post order traversal output"""
    results = [3, 7, 5, 13, 17, 15, 10]
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    assert list(tree.post_order()) == results


def test_bst_post_order_traversal_empty_tree(empty_bst):
    """test post order traversal on empty tree"""
    with pytest.raises(IndexError):
        empty_bst.bin_tree.post_order()


def test_bst_contains_true(full_bst):
    """test that tree contains returns true when it should"""
    tree = full_bst.bin_tree
    result = tree.contains(full_bst.sorted_list[1])
    assert result


def test_bst_contains_false(empty_bst):
    """test contains is false when it should be"""
    tree = empty_bst.bin_tree
    result = tree.contains(1000)
    assert not result


def test_bst_depth(empty_bst):
    """test the depth function returns correct value"""
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = tree.depth()
    assert result == 3


def test_bst_empty_tree_depth(empty_bst):
    """test empty tree depth"""
    result = empty_bst.bin_tree.depth()
    assert result == 0


def test_bst_balance_balanced(empty_bst):
    """test balance on balanced tree"""
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = tree.balance()
    assert result == 0


def test_bst_balance_negative(empty_bst):
    """test balance negative"""
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = tree.balance()
    assert result == -1


def test_bst_balance_positive(empty_bst):
    """test balance positive"""
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(2)
    result = tree.balance()
    assert result == 1


def test_bst_balance_empty():
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    assert tree.balance() == 0


def test_bst_breadth_first(empty_bst):
    """test breadth-first traversal output"""
    tree = empty_bst.bin_tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    tree.insert(17)
    result = [10, 5, 15, 3, 7, 13, 17]
    assert list(tree.breadth_first()) == result


def test_bst_breadth_first_empty_tree(empty_bst):
    """test breadth-first on an empty tree"""
    tree = empty_bst.bin_tree
    with pytest.raises(IndexError):
        next(tree.breadth_first())


def test_bst_delete_from_empty():
    """test the delete method against an empty bst"""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    result = tree.delete(7)
    assert result is None


def test_bst_delete_one():
    """test that delete removes the only node in the tree if only one"""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    tree.insert(7)
    tree.delete(7)
    assert tree.size() == 0


def test_bst_delete_from_five():
    """test delete with five nodes"""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(20)
    tree.insert(13)
    tree.delete(13)
    assert tree.find_node(13) is False
    assert tree.size() == 4


def test_bst_delete_from_range():
    """test specific node is removed when range is inserted"""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    rng = range(0, 50)
    for num in rng:
        tree.insert(num)
    tree.delete(20)
    assert tree.find_node(20) is False
    assert tree.size() == 49


def test_bst_big_tree_correct():
    """this test randomly generates a large tree of random values
    and checks it for correctness"""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    rndm = [random.sample(range(1000),
            random.randrange(2, 100)) for n in range(10)]
    for lst in rndm:
        for val in lst:
            tree.insert(val)
    assert _bst_tree_checker(tree.root)


def test_bst_big_tree_deletion():
    """this test randomly generates a large tree and deletes a value out of
    it, then checks the tree for correctness."""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    rndm = [random.sample(range(1000),
            random.randrange(2, 100)) for n in range(10)]
    for lst in rndm:
        for val in lst:
            tree.insert(val)
    tree.insert(27)
    tree.insert(453)
    tree.delete(27)
    tree.delete(453)
    assert _bst_tree_checker(tree.root)


@pytest.mark.parametrize('to_delete, sequence', _random_generator())
def test_bst_big_tree_deletion_two(to_delete, sequence):
    """this test randomly generates a large tree and deletes a value out of
    it, then checks the tree for correctness."""
    from bst import BinarySearchTree
    tree = BinarySearchTree()
    for item in sequence:
        tree.insert(item)
    tree.delete(to_delete)
    assert _bst_tree_checker(tree.root)
