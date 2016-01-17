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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        ret = list()

        if root is None:
            return ret

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        ret += left
        ret += right
        ret.append(root.val)

        return ret
        
