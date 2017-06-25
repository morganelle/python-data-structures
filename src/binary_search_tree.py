"""Python implementation of a binary search tree."""


class Node(object):
    """Node with data and left/right children."""

    def __init__(self, data=None):
        """Init a node."""
        self._data = data
        self._lchild = None
        self._rchild = None
        self._parent = None


class BinarySearchTree(object):
    """Binary search tree attributes and methods."""

    def __init__(self, iterable=None):
        """Init a binary search tree."""
        print(iterable)
        self._root = None
        self._size = 0
        self._depth = 0
        self._rightbal = 0
        self._leftbal = 0
        if type(iterable) in [list, tuple]:
            for item in iterable:
                self.insert(item)
        elif iterable is not None:
            raise TypeError('This tree accepts numbers only.')

    def insert(self, val):
        """."""
        if type(val) not in [int, float]:
            raise TypeError('This tree accepts numbers only.')
        if self._size == 0:
            self._root = Node(val)
            self._size += 1
            self._depth = 1
        current_node = self._root
        current_depth = 1
        new_node = Node(val)
        while val is not current_node._data:
            current_depth += 1
            if val < current_node._data:
                if current_node._lchild:
                    current_node = current_node._lchild
                else:
                    current_node._lchild = new_node
                    new_node._parent = current_node
                    self._size += 1
                    if current_depth > self._depth:
                        self._depth = current_depth
                        self._increment_balance(val)
                    break
            elif val > current_node._data:
                if current_node._rchild:
                    current_node = current_node._rchild
                else:
                    current_node._rchild = new_node
                    new_node._parent = current_node
                    self._size += 1
                    if current_depth > self._depth:
                        self._depth = current_depth
                        self._increment_balance(val)
                    break

    def _increment_balance(self, val):
        """."""
        if val > self._root._data:
            self._rightbal += 1
        elif val < self._root._data:
            self._leftbal += 1

    def balance(self):
        """."""
        return self._rightbal - self._leftbal

    def depth(self):
        """."""
        return self._depth

    def size(self):
        """."""
        return self._size

    def contains(self, val):
        """."""
        if self.search(val):
            return True
        return False

    def search(self, val):
        """."""
        current_node = self._root
        while current_node is not None:
            if val < current_node._data:
                if current_node._lchild:
                    current_node = current_node._lchild
                else:
                    break
            elif val > current_node._data:
                if current_node._rchild:
                    current_node = current_node._rchild
                else:
                    break
            else:
                return current_node

    def breadth_first(self):
        """Return a generator that returns the values breadth-first."""
        to_visit = [self._root]
        while len(to_visit):
            current_node = to_visit[0]
            if current_node._lchild:
                to_visit.append(current_node._lchild)
            if current_node._rchild:
                to_visit.append(current_node._rchild)
            to_visit.remove(current_node)
            yield current_node._data

    def pre_order(self):
        """Return a generator that returns the values pre-order."""
        visited = []
        current = self._root
        while len(visited) <= self.size():
            if current._data not in visited:
                visited.append(current._data)
                yield current._data
            if current._lchild is not None and current._lchild._data not in visited:
                current = current._lchild
            elif current._rchild is not None and current._rchild._data not in visited:
                current = current._rchild
            else:
                current = current._parent
