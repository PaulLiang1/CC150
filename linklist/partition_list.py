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
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):

        if head is None or head.next is None:
            return head

        before = after = None
        before_ptr = after_ptr = None
        ptr = head

        while ptr is not None:

            if ptr.val < x:
                if before is None:
                    before_ptr = ptr
                    before = ptr
                else:
                    before_ptr.next = ptr
                    before_ptr = ptr

            else:
                if after is None:
                    after_ptr = ptr
                    after = ptr
                else:
                    after_ptr.next = ptr
                    after_ptr = ptr
            ptr = ptr.next

        if before is None:
            after_ptr.next = None
            return after
        elif after is None:
            before_ptr.next = None
            return before
        else:
            before_ptr.next = after
            after_ptr.next = None
            return before
        
