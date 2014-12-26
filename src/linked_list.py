class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    #----------------nested _Node class-------------------
    class _Node:
        """Lightweight, nonpublic class for storing singly linked node"""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #-----------------stack methods---------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but do not remove element at top of stack
        Raise exception if stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element #top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of stack
        Raise Empty exception is the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is Empty')
        answer = self._head._element
        self._head = self._head._next #bypass the former top node
        self._size -= 1
        return answer



