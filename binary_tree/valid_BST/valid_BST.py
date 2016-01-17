"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# http://www.lintcode.com/en/problem/validate-binary-search-tree/
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        isValid, _, _ = self.isValidBSTHelper(root)
        return isValid

    def isValidBSTHelper(self, root):
        if root is None:
            return True, None, None

        left_is_BST, _, left_max = self.isValidBSTHelper(root.left)
        _left_max = left_max or (root.val - 1)

        right_is_BST, right_min, _ = self.isValidBSTHelper(root.right)
        _right_min = right_min or (root.val + 1)

        tree_is_BST = left_is_BST and right_is_BST and (_left_max < root.val < _right_min)
        min_val = min([x for x in [root.val, left_max, right_min] if x is not None])
        max_val = max(root.val, left_max, right_min)

        return tree_is_BST, min_val, max_val
