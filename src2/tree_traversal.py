#pre-order traversal
"""to be added to a tree class"""

def preorer(self):

  if not self.is_empty():
    for p in self._subtree_preorder(self.root()):
      yield p

def _subtree_preorder():
  yield p
  for c in self.children(p):
    for other in self._subtree_preorder(c):
      yield other

