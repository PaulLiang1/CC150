"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head is None:
            return None

        prev_ptr = head
        ptr = head.next

        while ptr is not None:

            if ptr.val == prev_ptr.val:
                # Keep moving to next pointer
                ptr = ptr.next
                continue

            prev_ptr.next = ptr
            prev_ptr = ptr
            ptr = ptr.next

        prev_ptr.next = None
        return head
        
