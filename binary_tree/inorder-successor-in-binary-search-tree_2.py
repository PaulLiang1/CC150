# https://leetcode.com/discuss/59787/share-my-java-recursive-solution
class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):

        if root is None or p is None:
            return None

        # p in right tree
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        # p in left tree
        else:
            left = self.inorderSuccessor(root.left, p)
            if left is not None:
                return left
            return root
