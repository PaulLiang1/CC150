"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        check_none_list = [root, A, B]

        # boundary check
        if any(map(lambda x: x is None, check_none_list)):
            return None

        visited = set()
        visited.add(root)

        A_ptr = A
        while A_ptr is not None and A_ptr != root:
            visited.add(A_ptr)
            A_ptr = A_ptr.parent

        B_ptr = B
        while B_ptr is not None and B_ptr != root:
            if B_ptr in visited:
                return B_ptr
            B_ptr = B_ptr.parent

        return root
    
