"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def removeDuplicates(self, head):

        if head is None:
            return None

        if head.next is None:
            return head

        seen = set()
        prev_ptr = head
        ptr = head.next
        seen.add(head.val)

        while ptr is not None:

            if ptr.val in seen:
                ptr = ptr.next
                continue
            else:
                seen.add(ptr.val)
                prev_ptr.next = ptr
                prev_ptr = ptr
                ptr = ptr.next

        prev_ptr.next = None
        return head

        
