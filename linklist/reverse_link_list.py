"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):

        if head is None:
            return None

        if head.next is None:
            return head

        if head.next.next is None:
            ptr = head.next
            ptr.next = head
            head.next = None
            return ptr

        prev_ptr = head
        ptr = head.next

        while ptr is not None:
            next_ptr = ptr.next
            ptr.next = prev_ptr

            prev_ptr = ptr
            ptr = next_ptr

        head.next = None
        head = prev_ptr
        return head
