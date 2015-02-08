class Tree:
    """Abstract base class representing a tree structure"""

    #------------nested Position class-----------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return true if other does not represent the same location"""
            return not (self == other)      #opposite of __eq__

    #------abstract methods that concrete subclass must support----
    def root(self):
        """Return Position representing the tree's root(or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent(or None)"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return number of children that Position p has"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate iteration of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in a tree"""
        raise NotImplementedError('must be implemented by subcalls')

    #-------concrete methods implemented in this class -----
    def is_root(self, p):
        """Return True is Position p represents the root of tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True is Position p does not have children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True is the tree is empty"""
        return len(self) == 0

    def preorer(self):
      if not self.is_empty():
        for p in self._subtree_preorder(self.root()):
          yield p

    def _subtree_preorder():
      yield p
      for c in self.children(p):
        for other in self._subtree_preorder(c):
          yield other

        

