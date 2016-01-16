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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        ret = list()

        if root is None:
            return ret

        ret.append(root.val)
        ret += self.preorderTraversal(root.left)
        ret += self.preorderTraversal(root.right)

        return ret
        
