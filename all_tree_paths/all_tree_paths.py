class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def all_tree_paths(root):
  if root is None:
    print("in None")
    return []


  if root.left is None and root.right is None:
    print("in last node")
    return [[root.val]]


  paths = []


  left_sub_path = all_tree_paths(root.left)
  print("left sub path: ", left_sub_path)
  for sub_path in left_sub_path:
    print("sub_path: ", sub_path)
    paths.append([root.val, *sub_path])
    


  right_sub_paths = all_tree_paths(root.right)
  for sub_path in right_sub_paths:
    paths.append([root.val, *sub_path])


  return paths


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


all_tree_paths(a) # ->


  