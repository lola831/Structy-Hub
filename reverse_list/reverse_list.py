# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None


def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
  

