"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# http://www.lintcode.com/en/problem/balanced-binary-tree/

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        is_balanced, _ = self.isBalancedHelper(root)
        return is_balanced

    def isBalancedHelper(self, root):

        if root is None:
            # Return is_balanced, tree_height
            return True, 0

        left_balanced, left_height = self.isBalancedHelper(root.left)
        right_balanced, right_height = self.isBalancedHelper(root.right)

        if left_balanced is False or right_balanced is False:
            return False, 0

        if abs(left_height - right_height) > 1:
            return False, 0

        return True, \
               max(left_height, right_height) + 1
