"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# http://www.lintcode.com/en/problem/minimum-depth-of-binary-tree/#

import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is not None:
            left = self.minDepth(root.left)
        else:
            left = sys.maxint

        if root.right is not None:
            right = self.minDepth(root.right)
        else:
            right = sys.maxint

        return min(left, right) + 1
