import sys
sys.path.append('/Users/asnead/documents/projects/algorithms_structures/src')
from linked_binary_tree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):

  def __init__(self, token, left=None, right=None):
    super().__init__()
    if not isinstance(token, str):
      raise TypeError('Token must be a string')
    self._add_root(token)
    if left is not None:
      if token not in '+-*x/':
        raise ValueError('token must be valid operator')
      self._attach(self.root(), left, right)

  def __str__(self):
    pieces = []
    self._parenthesize_recur(self.root(), pieces)
    return ''.join(pieces)

  def _parenthesize_recur(self, p, result):
    if self.is_leaf(p):
      result.append(str(p.element()))
    else:
      result.append('(')
      self._parenthesize_recur(self.left(p), result)
      result.append(p.element())
      self._parenthesize_recur(self.right(p), result)
      result.append(')')

def build_expression_tree(tokens):
  S = []
  for t in tokens:
    if t in '+-x*/':
      S.append(t)
    elif t not in '()':
      S.append(ExpressionTree(t))
    elif t == ')':
      right == S.pop()
      op = S.pop()
      left = S.pop()
      S.append(ExpressionTree(op, left, right))
  return S.pop()