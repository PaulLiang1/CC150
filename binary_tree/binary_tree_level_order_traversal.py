"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        result = list()

        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            sub_result = list()

            for i in xrange(len(queue)):
                node = queue.popleft()
                sub_result.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(sub_result)
        return result
