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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        seen = dict()
        ptr = head

        i = 0

        while ptr is not None:

            if ptr not in seen:
                seen[ptr] = i
            else:
                return ptr

            ptr = ptr.next
            i += 0

        return None
