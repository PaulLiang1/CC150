"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):

        if root is None:
            return 0

        return max(
            self.maxDepth(root.left) + 1,
            self.maxDepth(root.right) + 1
        )
