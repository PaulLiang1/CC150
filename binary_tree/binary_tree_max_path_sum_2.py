"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
# http://www.lintcode.com/en/problem/binary-tree-maximum-path-sum-ii/

class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):

        if root is None:
            return 0

        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)

        return max(
            left,
            right
        ) + root.val
