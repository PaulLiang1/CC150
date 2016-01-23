"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head: the head of linked list.
    # @return: a middle node of the linked list
    def middleNode(self, head):

        if head is None:
            return None

        ptr_1 = ptr_2 = head

        i = 0
        while ptr_2 is not None:
            if i % 2 == 0 and i != 0:
                ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
            i += 1

        return ptr_1
