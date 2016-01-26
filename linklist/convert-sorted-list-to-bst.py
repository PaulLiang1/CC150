"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """

    def findMiddle(self, head):
        pre_slow = slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            pre_slow = slow
            slow = slow.next

        return pre_slow, slow

    def sortedListToBST(self, head):

        if head is None:
            return None

        pre_middle, middle = self.findMiddle(head)
        middleNode = TreeNode(middle.val)

        rightNode = self.sortedListToBST(middle.next)
        pre_middle.next = None

        if head != middle:
            leftNode = self.sortedListToBST(head)
        else:
            leftNode = None

        middleNode.left = leftNode
        middleNode.right = rightNode

        return middleNode
