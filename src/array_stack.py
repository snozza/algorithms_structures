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

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename,'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()

def is_matched_html(raw):
    """Return true if all HTML tags are properly matched, else False"""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1 :
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()
