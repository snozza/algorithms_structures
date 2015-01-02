from doubly_linked_base import _DoublyLinkedBase
from doubly_linked_base import PositionalList
import inspect

def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order"""
    if len(L):
        marker = L.first()
    while marker != L.last():
        pivot = L.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != L.first() and L.before(walk).element > value:
                walk = L.before(walk)
            L.delete(pivot)
            L.add_before(walk, value)


theList = PositionalList()
theList.add_first('1');
print(theList)