"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        ptr = head
        nptr = head

        for i in xrange(n):
            nptr = nptr.next

        while nptr is not None:
            nptr = nptr.next
            ptr = ptr.next

        return ptr
        
