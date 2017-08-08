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
        self._rdepth = 0
        self._ldepth = 0
        if iter_init is not None:
            if type(iter_init) not in [list, tuple]:
                raise TypeError('Please enter a list or tuple.')
            for num in iter_init:
                self.insert(num)

    def insert(self, data):
        """Insert a new node into the tree."""
        new_node = Node(data)
        current_depth = 1
        if not self._root:
            self._root = new_node
        else:
            current_node = self._root
            while data is not current_node._data:
                current_depth += 1
                if data > current_node._data:
                    if current_node._rchild:
                        current_node = current_node._rchild
                    else:
                        current_node._rchild = new_node
                        new_node._parent = current_node
                        break
                elif data < current_node._data:
                    if current_node._lchild:
                        current_node = current_node._lchild
                    else:
                        current_node._lchild = new_node
                        new_node._parent = current_node
                        break
                else:
                    return
        self._size += 1
        self._update_depths(data, current_depth)

    def _update_depths(self, data, current_depth):
        """Update left or right depth if needed."""
        if data > self._root._data:
            if current_depth > self._rdepth:
                self._rdepth = current_depth
        elif data < self._root._data:
            if current_depth > self._ldepth:
                self._ldepth = current_depth
        else:
            self._rdepth, self._ldepth = 1, 1

    def search(self, data):
        """Return node containing a data."""
        if type(data) in [int, float]:
            current_node = self._root
            while current_node:
                if data > current_node._data:
                    if current_node._rchild:
                        current_node = current_node._rchild
                    else:
                        return
                elif data < current_node._data:
                    if current_node._lchild:
                        current_node = current_node._lchild
                    else:
                        return
                else:
                    return current_node
        return

    def contains(self, data):
        """Return boolean indicating whether data is in tree."""
        return True if self.search(data) else False

    def size(self):
        """Return size of tree."""
        return self._size

    def depth(self):
        """Return depth of tree."""
        return self._ldepth if self._ldepth > self._rdepth else self._rdepth

    def balance(self):
        """Return balance of tree."""
        return self._rdepth - self._ldepth

    def pre_order_traversal(self):
        """Yield node data in pre-order."""
        for node_data in self._pre_order(self._root):
            yield node_data

    def _pre_order(self, current_node):
        """."""
        yield current_node._data
        if current_node._lchild:
            for node_data in self._pre_order(current_node._lchild):
                yield node_data
        if current_node._rchild:
            for node_data in self._pre_order(current_node._rchild):
                yield node_data
