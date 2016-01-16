"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
from collections import deque

class Solution:

    def pre_order(self, root):
        ret = list()

        if root is None:
            return ret

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()

            if node is None:
                ret.append('#')
                continue

            ret.append(node.val)
            queue.appendleft(node.right)
            queue.appendleft(node.left)

        return ret

    # to pre-order traversal,
    # only to visit right node first
    def inverse_pre_order(self, root):
        ret = list()

        if root is None:
            return ret

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()

            if node is None:
                ret.append('#')
                continue

            ret.append(node.val)
            queue.appendleft(node.left)
            queue.appendleft(node.right)

        return ret

    def isSymmetric(self, root):

        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None or root.right is None:
            return False

        left_traversal = self.pre_order(root.left)
        right_traversal = self.inverse_pre_order(root.right)

        return left_traversal == right_traversal
        
