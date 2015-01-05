from doubly_linked_base import PositionalList
from favourites_list import FavouritesList

class FavouritesListMTF(FavouritesList):
    """List of elements ordered with move-to-front heuristic"""

    #override _move_up to provide move-to-front heuristic
    def _move_up(self, p):
        """Move accessed item at Position p to front of list"""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        """Generate sequence of top k elements in terms of access count"""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        #make copy of original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        #repeatedly find, report, remove element with largest count
        for j in range(k):
            #find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            #we have found the element with highest count
            yield highPos.element()._value #report to user
            temp.delete(highPos) #remove from tempList