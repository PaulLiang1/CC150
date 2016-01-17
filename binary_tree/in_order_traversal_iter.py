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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        result = list()

        if root is None:
            return result

        queue = deque()
        node = root

        while node is not None or len(queue) > 0:

            while node is not None:
                queue.appendleft(node)
                node = node.left

            node = queue.popleft()
            result.append(node.val)
            node = node.right

        return result
            
