from ..src/doubly_linked_base import _DoublyLinkedBase

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

print(insertion_sort([3, 4, 9, 2]))