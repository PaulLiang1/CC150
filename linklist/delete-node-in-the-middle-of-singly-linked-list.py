"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):

        if node is None:
            return

        if node.next is None:
            # can't delete if it's last node
            return

        node.val = node.next.val
        if node.next.next is not None:
            node.next = node.next.next
        else:
            node.next = None
        return
