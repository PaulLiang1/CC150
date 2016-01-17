"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""

from collections import deque

class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.queue = deque()

        if root is None:
            return

        node = root
        queue = deque()

        while node is not None or len(queue) > 0:
            while node is not None:
                queue.appendleft(node)
                node = node.left

            node = queue.popleft()
            self.queue.append(node)
            node = node.right

    #@return: True if there has next node, or false
    def hasNext(self):
        return len(self.queue) > 0

    #@return: return next node
    def next(self):
        return self.queue.popleft()
