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
            while walk != L.first() and L.before(walk).element() > value:
                walk = L.before(walk)
            L.delete(pivot)
            L.add_before(walk, value)


theList = PositionalList()
a = theList.add_first('4')
b = theList.add_after(a, '2')
c = theList.add_after(b, '1')
print(insertion_sort(theList))
for node in theList:
    print(node)