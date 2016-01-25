"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None

        node = self.mergeKListsHelper(lists, 0, len(lists) - 1)
        return node

    def mergeKListsHelper(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = start + (end - start) / 2
        left = self.mergeKListsHelper(lists, start, mid)
        right = self.mergeKListsHelper(lists, mid + 1, end)
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        ptr = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                ptr.next = list1
                ptr = ptr.next
                list1 = list1.next
            else:
                ptr.next = list2
                ptr = ptr.next
                list2 = list2.next

        if list1 is not None:
            ptr.next = list1

        if list2 is not None:
            ptr.next = list2

        return dummy.next
