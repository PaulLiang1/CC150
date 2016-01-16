# http://www.lintcode.com/en/problem/identical-binary-tree/
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
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):

        # boundary check
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False

        queue = deque()
        queue.append((a, b))

        while len(queue) > 0:
            a_node, b_node = queue.popleft()

            if a_node is None and b_node is None:
                continue

            if any(map(lambda x: x is None, [a_node, b_node])):
                return False

            if a_node.val != b_node.val:
                return False

            queue.append((a_node.left, b_node.left))
            queue.append((a_node.right, b_node.right))

        return True
