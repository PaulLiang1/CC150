"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        self.max_seen = -sys.maxint

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.val

        max_cross_root = sum([
            self.maxPathSumCrossRoot(root.left),
            self.maxPathSumCrossRoot(root.right),
            root.val
        ])

        self.maxPathSumSubTree(root.left),
        self.maxPathSumSubTree(root.right)

        return max(max_cross_root, self.max_seen)

    def maxPathSumSubTree(self, node):
        if node is None:
            return 0

        left = max(0, self.maxPathSumSubTree(node.left))
        right = max(0, self.maxPathSumSubTree(node.right))

        self.max_seen = max(
            self.max_seen,
            left + right + node.val
        )

        return max(left, right) + node.val

    def maxPathSumCrossRoot(self, node):
        if node is None:
            return 0

        left = self.maxPathSumCrossRoot(node.left)
        right = self.maxPathSumCrossRoot(node.right)

        return max(
            0,
            left,
            right
        ) + node.val
