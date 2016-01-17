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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        ret = list()

        if root is None:
            return ret

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        ret += left
        ret.append(root.val)
        ret += right

        return ret
        
