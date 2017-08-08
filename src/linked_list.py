"""Implementation of a linked list data structure."""


class Node(object):
    """Define node attributes."""

    def __init__(self, val=None):
        """."""
        self.val = val
        self.next_node = None


class LinkedList(object):
    """Define LinkedList attributes and methods."""

    def __init__(self):
        """."""
        self.head = None
        self._size = 0

    def push(self, val=None):
        """."""
        if val is None:
            raise ValueError('Please enter some data.')
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        """."""
        if self.head.data is not None:
            popped = self.head
            self.head = self.head.next_node
            return popped
        else:
            raise KeyError('No values to pop.')

    def search(self, val=None):
        """."""
        if val is None:
            raise ValueError('Please enter a value.')
        current_node = self.head
        while current_node.data:
            if current_node.data == val:
                return current_node
            current_node = current_node.next_node
        raise ValueError('No node with the given data in this linked list.')

    def remove(self, node):
        """."""
        pass

    def size(self):
        """."""
        return self._size


# push(val) will insert the value ‘val’ at the head of the list
# pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
# size() will return the length of the list
# search(val) will return the node containing ‘val’ in the list, if present, else None
# remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
# display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
# In addition to these methods above, your implementation also needs to be able to interact with these built-in Python functions:

# len(the_list) returns the size of the list
# print(the_list) returns what the display() method returns
























