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
    @return: An integer
    """
    def maxDepth(self, root):

        if not root:
            return 0

        queue = deque()
        queue.append((root, 0))
        max_depth = 0

        while len(queue) > 0:
            node, depth = queue.popleft()

            if depth > max_depth:
                max_depth = depth

            if node is None:
                continue

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return max_depth
