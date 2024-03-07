
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
from collections import deque
​
def tree_includes(root, target):
  if root is None:
    return False
  
  queue = deque([root])
  while queue:
    curr = queue.popleft()
    if target == curr.val:
      return True
    else:
      if curr.right:
        queue.append(curr.right)
      if curr.left:
        queue.append(curr.left)
  
  return False
    if target == curr.val: