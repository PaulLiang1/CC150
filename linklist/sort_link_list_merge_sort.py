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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):

        if head is None or head.next is None:
            return head

        mid = self.findmid(head)

        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.merge(left, right)

    def findmid(self, node):
        fast_ptr = node
        slow_ptr = node

        i = 0
        while fast_ptr is not None:
            fast_ptr = fast_ptr.next
            if i % 2 == 0 and i != 0:
                slow_ptr = slow_ptr.next
        return slow_ptr

    def merge(self, list1, list2):
        dummy = ListNode(0)
        ptr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                ptr = list1
                list1 = list1.next
            else:
                ptr.next = list2
                ptr = list2
                list2 = list2.next

        if list1:
            ptr.next = list1
        if list2:
            ptr.next = list2

        return dummy.next
