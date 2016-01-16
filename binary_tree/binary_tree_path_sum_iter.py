"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):

        if root is None or target is None:
            return list()

        queue = deque()
        result = list()

        # Append init values
        queue.append((root, list()))

        while len(queue) > 0:
            node, path = queue.popleft()

            if node is None:
                continue

            # Create local copy of path
            path = path[:]
            path.append(node.val)

            if node.left is None and node.right is None:
                if sum(path) == target:
                    result.append(path)
                continue

            queue.append((node.left, path))
            queue.append((node.right, path))

        return result
