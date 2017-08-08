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
        new_node = Node(val)
        if self._size == 0:
            self._root = new_node
            self._depth = 1
        else:
            current_node = self._root
            current_depth = 1
            while val is not current_node._data:
                current_depth += 1
                if val < current_node._data:
                    if current_node._lchild:
                        current_node = current_node._lchild
                    else:
                        current_node._lchild = new_node
                        new_node._parent = current_node
                        self._update_depth_insert(val, current_depth)
                        break
                elif val > current_node._data:
                    if current_node._rchild:
                        current_node = current_node._rchild
                    else:
                        current_node._rchild = new_node
                        new_node._parent = current_node
                        self._update_depth_insert(val, current_depth)
                        break
        self._size += 1

    def _increment_balance_insert(self, val):
        """."""
        if val > self._root._data:
            self._rightbal += 1
        elif val < self._root._data:
            self._leftbal += 1

    def _update_depth_insert(self, val, current_depth):
        """."""
        if current_depth > self._depth:
            self._depth = current_depth
            self._increment_balance_insert(val)

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

    def in_order(self):
        """Return a generator that returns the values pre-order."""
        from stack import Stack
        current = self._root
        visited = []
        in_order = []
        stack = Stack()
        while len(stack):
            print(len(stack))
            if current._data not in visited:
                print('in if', current._data)
                stack.push(current._data)
            if current._rchild is None and current._lchild is None:
                print('in second if', current._data)
                in_order.append(current._data)
                current = current._parent
                in_order.append(current._data)
                # yield stack.pop()
            elif current._lchild in visited or current._lchild is None:
                print('in elif', current._data)
                if current._rchild is not None:
                    current = current._rchild
                else:
                    current = current._parent
                in_order.append(current._data)
                # yield stack.pop()
            print('visited', visited)
            return in_order



# def insert(self, val):
#         """Insert a new value into binary search tree."""
#         if type(val) not in [int, float]:
#             raise TypeError('This tree accepts numbers only.')
#         if self.contains(val):
#             raise ValueError('Node already in tree.')
#         new_node = Node(val)
#         if self._size == 0:
#             self._root = new_node
#             self._max_depth = 1
#             self._rbal = 1
#             self._lbal = 1
#         else:
#             current_depth = 1
#             current_node = self._root
#             while val is not current_node._data:
#                 current_depth += 1
#                 if val < current_node._data:
#                     if current_node._lkid:
#                         current_node = current_node._lkid
#                     else:
#                         current_node._lkid = new_node
#                         new_node._parent = current_node
#                         self._update_balances_and_depth(current_depth, val)
#                         break
#                 elif val > current_node._data:
#                     if current_node._rkid:
#                         current_node = current_node._rkid
#                     else:
#                         current_node._rkid = new_node
#                         new_node._parent = current_node
#                         self._update_balances_and_depth(current_depth, val)
#                         break
#         self._size += 1

#     def _update_balances_and_depth(self, current_depth, val):
#         """Increment left/right balance on insert."""
#         if current_depth > self._max_depth:
#             self._max_depth = current_depth
#         if val > self._root._data and self._rbal < current_depth:
#             self._rbal = current_depth
#         elif val < self._root._data and self._lbal < current_depth:
#             self._lbal = current_depth
