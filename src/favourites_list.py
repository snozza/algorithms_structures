from doubly_linked_base import PositionalList

class FavouritesList:
    """List of elements ordered from most frequently accessed to least"""

    #-----------nested _Item class----------------
    class _Item:
      __slots__ = '_value', '_count'    #streamline memory usage
      def __init__(self, element):
        self._value = element          #user's element
        self._count = 0                 #access count init zero

    #-----------nonpublic utilities---------------
    def _find_position(self, e):
      """Search for element e and return its position (or None if not found)"""
      walk = self._data.first();
      while walk is not None and walk.element()._value != e:
        walk = self._data.after(walk)
      return walk

    def _move_up(self, p):
      """Move item at Position p earlier in the list based on access count"""
      if p != self._data.first():
        cnt = p.element()._count
        walk = self._data.before(p)
        if cnt > walk.element()._count:
          while (walk != self._data.first() and
                 cnt > self._data.before(walk).element()._count):
            walk = self._data.before(walk)
          self._data.add_before(walk, self._data.delete(p)) #delete/reinsert

    def __init__(self):
      """Create empty list of favourites"""
      self._data = PositionalList() #list of _Item instances

    def __len__(self):
      """Return number of entries on fav list"""
      return len(self._data)

    def is_empty(self):
      """Return True if list is empty."""
      return len(self._data) == 0

    def access(self, e):
      """Access element e, thereby increasing its access count"""
      p = self._find_position(e)
      if p is None:
        p = self._data.add_last(self._Item(e))
      p.element()._count += 1
      self._move_up(p) #consider moving forward

    def remove(self, e):
      """Remove element e from list of favs"""
      p = self._find_position(e)
      if p is not None:
        self._data.delete(p)

    def top(self, k):
      """Generate sequence of top k elements in terms of access count"""
      if not 1 <= k <= len(self):
        raise ValueError('Illegal value for k')
      walk = self._data.first()
      for j in range(k):
        item = walk.element()
        yield item._value
        walk = self._data.after(walk)


theList = PositionalList()
a = theList.add_first('4')
b = theList.add_after(a, '2')
c = theList.add_after(b, '1')

favList = FavouritesList()
favList.access('1')
favList.access('2')
favList.access('3')
favList.access('1')
favList.access('1')
favList.access('3')
theList = list(favList.top(3))
for thing in theList:
  print(thing)