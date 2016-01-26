"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:

    def findMiddle(self, head):
        slow = fast = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        new_head = None

        while head is not None:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp

        return new_head

    def reorderList(self, head):

        if head is None:
            return head

        mid = self.findMiddle(head)
        reverse = self.reverse(mid.next)
        mid.next = None

        head = self.merge(head, reverse)
        return head

    def merge(self, list1, list2):
        dummy = ListNode(0)
        ptr = dummy

        i = 0
        while list1 and list2:
            if i % 2 == 0:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
            i += 1

        if list1:
            ptr.next = list1
        if list2:
            ptr.next = list2

        return dummy.next
        
