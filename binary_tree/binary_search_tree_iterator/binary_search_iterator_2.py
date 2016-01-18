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
        self.node = root

        if root is None:
            return

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.node is not None or len(self.queue) > 0

    #@return: return next node
    def next(self):
        ret = None

        if self.hasNext():
            while self.node is not None:
                self.queue.appendleft(self.node)
                self.node = self.node.left

            self.node = self.queue.popleft()
            ret = self.node
            self.node = self.node.right

        return ret

        
