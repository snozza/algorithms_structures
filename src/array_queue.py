class ArrayQueue:
    """FIFO queue using pythong list"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return but do not remove element at front of queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None #help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer