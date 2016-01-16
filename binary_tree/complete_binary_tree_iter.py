"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

from collections import deque

class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):

        if root is None:
            return True

        queue = deque()
        queue.append(root)

        result = list()

        # Do BFS
        while len(queue) > 0:
            node = queue.popleft()

            if node is None:
                result.append('#')
                continue

            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        if '#' not in result:
            return True

        non_hash_bang_found = False
        for i in xrange(len(result) - 1, -1, -1):
            if '#' == result[i] and non_hash_bang_found is True:
                return False

            if '#' != result[i]:
                non_hash_bang_found = True

        return True
