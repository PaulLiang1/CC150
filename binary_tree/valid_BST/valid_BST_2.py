
import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        is_BST, _, _ = self.isValidBSTHelper(root)
        return is_BST

    def isValidBSTHelper(self, root):
        if root is None:
            # return is_BST, min_val, max_val
            return True, sys.maxint, -sys.maxint

        left_is_BST, left_min, left_max = self.isValidBSTHelper(root.left)
        right_is_BST, right_min, right_max = self.isValidBSTHelper(root.right)

        if ( left_is_BST is False or right_is_BST is False):
            return False, 0, 0

        if not left_max < root.val:
            return False, 0, 0

        if not root.val < right_min:
            return False, 0, 0

        return True, \
               min([x for x in [root.val, left_min] if x is not None]), \
               max(root.val, right_max)
