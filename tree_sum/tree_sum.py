
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def tree_sum(root):
  if root is None:
    return 0
  
  sum = 0
  stack = [root]
  while stack:
    curr = stack.pop()
    sum = sum + curr.val
    
    if curr.left:
      stack.append(curr.left)
    if curr.right:
      stack.append(curr.right)
  
  return sum