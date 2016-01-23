"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):

        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next

        ptr = head
        while l1 is not None and l2 is not None:

            if l1.val > l2.val:
                ptr.next = l2
                l2 = l2.next
            else:
                ptr.next = l1
                l1 = l1.next
            ptr = ptr.next

        if l1 is not None:
            ptr.next = l1

        if l2 is not None:
            ptr.next = l2

        return head
        
