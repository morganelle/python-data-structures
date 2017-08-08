"""Tests for Binary Search Tree."""
import pytest
from binary_search_tree import BinarySearchTree


@pytest.fixture
def init_bst_no_root():
    """."""
    return BinarySearchTree()


@pytest.fixture
def init_bst_root():
    """."""
    return BinarySearchTree([5])


@pytest.fixture
def init_bst_right():
    """."""
    return BinarySearchTree([5, 10, 15, 20])


@pytest.fixture
def init_bst_left():
    """."""
    return BinarySearchTree([20, 15, 10, 5])


@pytest.fixture
def init_bst_list():
    """."""
    return BinarySearchTree([6, 3, 8, 5, 4, 1, 9])


@pytest.fixture
def init_bst_list_traverse():
    """."""
    return BinarySearchTree([6, 3, 7, 1, 5, 4, 9, 8])


def test_invalid_val_init():
    """."""
    with pytest.raises(TypeError):
        BinarySearchTree(1)


def test_init_no_root(init_bst_no_root):
    """."""
    assert init_bst_no_root._root is None


def test_init_one_node(init_bst_root):
    """."""
    assert init_bst_root._root._data == 5
    assert init_bst_root._root._parent is None


def test_init_many(init_bst_list):
    """."""
    assert init_bst_list._root._data == 6
    assert init_bst_list._root._lchild._data == 3
    assert init_bst_list._root._rchild._data == 8
    assert init_bst_list._root._parent is None
    assert init_bst_list.search(3)._parent._data == 6
    assert init_bst_list.search(8)._parent._data == 6


def test_init_left(init_bst_left):
    """."""
    assert init_bst_left._root._data == 20
    assert init_bst_left._root._lchild._data == 15
    assert init_bst_left._root._rchild is None
    assert init_bst_left._root._parent is None
    assert init_bst_left.search(10)._parent._data == 15
    assert init_bst_left.search(10)._lchild._data == 5
    assert init_bst_left.search(5)._parent._data == 10
    assert init_bst_left.search(5)._lchild is None


def test_init_right(init_bst_right):
    """."""
    assert init_bst_right._root._data == 5
    assert init_bst_right._root._lchild is None
    assert init_bst_right._root._rchild._data == 10
    assert init_bst_right._root._parent is None
    assert init_bst_right.search(15)._parent._data == 10
    assert init_bst_right.search(20)._parent._data == 15


def test_init_list(init_bst_list):
    """."""
    assert init_bst_list._root._data == 6
    assert init_bst_list._root._parent is None
    assert init_bst_list._root._lchild._data == 3
    assert init_bst_list._root._rchild._data == 8


def test_insert_none(init_bst_no_root):
    """."""
    assert init_bst_no_root.depth() is 0
    init_bst_no_root.insert(100)
    assert init_bst_no_root._root._data == 100
    assert init_bst_no_root._root._parent is None
    assert init_bst_no_root._root._lchild is None
    assert init_bst_no_root._root._rchild is None
    assert init_bst_no_root.depth() is 1


def test_insert_one(init_bst_root):
    """."""
    assert init_bst_root.depth() is 1
    init_bst_root.insert(1)
    assert init_bst_root._root._data == 5
    assert init_bst_root._root._parent is None
    assert init_bst_root._root._lchild._data == 1
    assert init_bst_root._root._rchild is None
    assert init_bst_root.depth() is 2


def test_insert_right_on_right(init_bst_right):
    """."""
    assert init_bst_right.depth() is 4
    init_bst_right.insert(25)
    assert init_bst_right._root._data is 5
    assert init_bst_right.search(20)._rchild._data is 25
    assert init_bst_right.search(25)._parent._data is 20
    assert init_bst_right.depth() is 5


def test_insert_left_on_right(init_bst_right):
    """."""
    init_bst_right.insert(0)
    assert init_bst_right._root._data is 5
    assert init_bst_right._root._lchild._data is 0
    assert init_bst_right.depth() is 4


def test_insert_right_on_left(init_bst_left):
    """."""
    init_bst_left.insert(25)
    assert init_bst_left._root._data is 20
    assert init_bst_left._root._rchild._data is 25
    assert init_bst_left._root._rchild._parent._data is 20
    assert init_bst_left.depth() is 4


def test_insert_left_on_left(init_bst_left):
    """."""
    assert init_bst_left.depth() is 4
    init_bst_left.insert(0)
    assert init_bst_left._root._data is 20
    assert init_bst_left._root._lchild._data is 15
    assert init_bst_left.search(0)._parent._data is 5
    assert init_bst_left.search(0)._lchild is None
    assert init_bst_left.search(0)._rchild is None
    assert init_bst_left.depth() is 5


def test_balance_empty_tree(init_bst_no_root):
    """."""
    assert init_bst_no_root.balance() is 0


def test_balance_left_tree(init_bst_left):
    """."""
    assert init_bst_left.size() == 4
    assert init_bst_left.balance() is -3


def test_balance_right_tree(init_bst_right):
    """."""
    assert init_bst_right.size() == 4
    assert init_bst_right.balance() == 3
