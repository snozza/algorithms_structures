class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        """Return but do not remove element on top of stack
        Raise Empty exception is the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
