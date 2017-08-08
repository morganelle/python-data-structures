"""Python implementation of a numeric binary search tree."""


class Node(object):
    """Attributes of a binary search tree node."""

    def __init__(self, data):
        """Create a new node."""
        if type(data) not in [float, int]:
            raise TypeError('{} is not an int or float.'.format(data))
        self._data = data
        self._parent = None
        self._rchild = None
        self._lchild = None


class BinarySearchTree(object):
    """Attributes and methods of a binary search tree."""

    def __init__(self, iter_init=None):
        """Create a new tree."""
        self._root = None
        self._size = 0
        self._depth = 0
        if iter_init is not None:
            if type(iter_init) not in [list, tuple]:
                raise TypeError('Please enter a list or tuple.')
            for num in iter_init:
                self.insert(num)

    def insert(self, data):
        """Insert a new node into the tree."""
        new_node = Node(data)
        if not self._root:
            self._root = new_node
            self._size += 1
        else:
            current_node = self._root
            while True:
                if data > current_node._data:
                    if current_node._rchild:
                        current_node = current_node._rchild
                    else:
                        current_node._rchild = new_node
                        new_node._parent = current_node
                        self._size += 1
                        break
                elif data < current_node._data:
                    if current_node._lchild:
                        current_node = current_node._lchild
                    else:
                        current_node._lchild = new_node
                        new_node._parent = current_node
                        self._size += 1
                        break
                else:
                    raise ValueError('{} is already in the tree'.format(data))

    def size(self):
        """Return size of tree."""
        return self._size

    def depth(self):
        """Return depth of tree."""
        return self._depth()

    def contains(self, data):
        """Return boolean indicatig whether data is in tree."""

    def search(self, data):
        """Return node containing a data."""

    def balance(self):
        """Return balance of tree."""
