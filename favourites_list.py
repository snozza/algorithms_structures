class FavouritesList:
    """List of elements ordered from most frequently accessed to least"""

    #-----------nested _Item class----------------
    class _Item:
      __slots__ = '_value', '_count'    #streamline memory usage
      def __init__(self, e):
        self._value = elements          #user's element
        self._count = 0                 #access count init zero

    #-----------nonpublic utilities---------------
    def _find_position(self, e):
      """Search for element e and return its position (or None if not found)"""
      walk = self._data.first();