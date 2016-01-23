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
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        prev_ptr = ptr = n_ptr = head

        for i in xrange(n):
            n_ptr = n_ptr.next

        while n_ptr is not None:
            n_ptr = n_ptr.next
            prev_ptr = ptr
            ptr = ptr.next

        # remove head:
        if head == ptr:
            if ptr.next is None:
                return None
            else:
                head = ptr.next
                return head

        # remove last nd
        elif ptr.next is None:
            prev_ptr.next = None
        # remove nd in middle
        else:
            prev_ptr.next = ptr.next

        return head
