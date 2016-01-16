"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):

        if root is None:
            return list()

        queue = deque()
        queue.append(root)

        ret = list()

        while len(queue) > 0:
            node = queue.popleft()

            if node is None:
                continue

            ret.append(node.val)
            queue.appendleft(node.right)
            queue.appendleft(node.left)

        return ret
