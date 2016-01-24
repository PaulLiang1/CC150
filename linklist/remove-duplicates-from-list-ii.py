"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from collections import OrderedDict

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):

        if head is None or head.next is None:
            return head

        node_counter = OrderedDict()
        ptr = head

        while ptr is not None:
            if ptr.val in node_counter:
                node_counter[ptr.val].append(ptr)
            else:
                node_counter[ptr.val] = [ptr]
            ptr = ptr.next

        head = ptr = None
        for val, nodes in node_counter.iteritems():
            if len(nodes) != 1:
                continue

            if head is None:
                head = ptr = nodes[0]
            else:
                ptr.next = nodes[0]
                ptr = ptr.next

        if ptr:
            ptr.next = None

        return head
        
