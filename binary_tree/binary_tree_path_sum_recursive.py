"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    def binaryTreePathSum(self, root, target):
        result = list()

        if root is None or target is None:
            return result

        self.binaryTreePathSumHelper(root, target, list(), result)
        return result

    def binaryTreePathSumHelper(self, node, target, path, result):

        if node is None:
            return

        path = path[:]
        path.append(node.val)

        if node.left is None and node.right is None:
            if sum(path) == target:
                result.append(path)

        self.binaryTreePathSumHelper(node.left, target, path, result)
        self.binaryTreePathSumHelper(node.right, target, path, result)
