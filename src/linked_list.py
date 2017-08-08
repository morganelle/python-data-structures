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


















































# class Node(object):  # pragma: no cover
#     """Set properties and methods for LinkedList class."""

#     def __init__(self, val, next_node=None):
#         """."""
#         self.val = val
#         self.next_node = next_node

# class LinkedList(object):
#     """Set properties and methods for LinkedList class."""

#     def __init__(self, inbound_data=None):
#         """Initialize LinkedList object."""
#         self.head = None
#         self._length = 0
#         if type(inbound_data) in [list, tuple, str]:
#             for item in inbound_data:
#                 self.push(item)
#         elif inbound_data is not None:
#             raise TypeError('Try again with a list, tuple, or string.')

#     def push(self, val):
#         """Create a new node."""
#         if val is None:
#             raise ValueError('You must give a value.')
#         new_node = Node(val, self.head)
#         self.head = new_node
#         self._length += 1

#     def pop(self):
#         """Remove node from LinkedList."""
#         current_node = self.head
#         if current_node is None:
#             raise IndexError('Nothing to pop.')
#         self._length -= 1
#         self.head = current_node.next_node
#         return current_node.val

#     def size(self):
#         """Return the size of a linked list."""
#         return self._length

#     def search(self, val):
#         """Return a node for a given value."""
#         current_node = self.head
#         while current_node:
#             if val == current_node.val:
#                 return current_node
#             current_node = current_node.next_node
#         return None

#     def remove(self, node):
#         """Remove a node from the linked list."""
#         current_node = self.head
#         previous_node = None
#         while current_node != node:
#             previous_node = current_node
#             current_node = current_node.next_node
#             if current_node is None:
#                 raise ValueError('Node not in linked list.')
#         if previous_node is None:
#             self.head = current_node.next_node
#         else:
#             previous_node.next_node = current_node.next_node
#         current_node.next_node = None
#         self._length -= 1

#     def display(self):
#         """Return string representing LinkedList as Python tuple."""
#         display_string = u''
#         current_node = self.head
#         while current_node:
#                 display_string = '{} {}'.format(current_node.val,
#                                                 display_string)
#                 current_node = current_node.next_node
#         display_string = display_string.strip().replace(' ', ', ')
#         display_string = '({})'.format(display_string)
#         return display_string

#     def __len__(self):
#         """Return the size of a linked list, overwriting len method."""
#         return self._length

#     def __repr__(self):
#         """Print the what is returned by display."""
#         return self.display()
