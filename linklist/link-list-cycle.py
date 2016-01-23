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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        ptr_1 = head
        ptr_2 = head

        while True:
            try:
                ptr_1 = ptr_1.next
                ptr_2 = ptr_2.next.next
            except AttributeError:
                return False

            if ptr_1 == ptr_2:
                return True
