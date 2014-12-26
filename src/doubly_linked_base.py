class _DoublyLinkedBase:    

    class _Node:

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        #delete nonsentinel node from list and return element
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size += 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on doubly linked list"""

    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._delete_node(self._trailer._prev)

class PositionalList(_DoublyLinkedBase):
    """sequential container of elements allowing positional access"""
    class Position:
        """An abstraction representing location of single element"""
        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other does not represent the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True is other does not represent the same location"""
            return not(self == other)

    #-------------utility methods---------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #--------------accessors----------------
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return Position just before Position p"""
        node = self._validate(p)
        return self._make_position(node._prev)



