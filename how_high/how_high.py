a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


how_high(a) # -> 2
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g


how_high(a) # -> 3
a = Node('a')
c = Node('c')


a.right = c


#      a
#       \
#        c


how_high(a) # -> 1
a = Node('a')


#      a


how_high(a) # -> 0
how_high(None) # -> -1
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None




a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g


def how_high(node):
  if node is None:
    return -1


  left_height = how_high(node.left)
  right_height = how_high(node.right)
  print(left_height)


  return 1 + max(left_height, right_height)


how_high(a) # -> 3