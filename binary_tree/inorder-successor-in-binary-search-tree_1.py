# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# http://www.lintcode.com/en/problem/inorder-successor-in-binary-search-tree/

from collections import deque

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):

        if root is None or p is None:
            return None

        queue = deque()
        node = root
        p_found = False

        while node is not None or len(queue) > 0:

            while node is not None:
                queue.appendleft(node)
                node = node.left

            node = queue.popleft()

            if p_found is True:
                return node

            if node == p:
                p_found = True

            node = node.right

        return None
