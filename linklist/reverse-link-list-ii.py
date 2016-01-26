"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):

        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        for i in xrange(m - 1):
            head = head.next

        # head at m - 1
        pre_m_nd = head
        m_nd = head.next
        n_nd = m_nd
        post_n_nd = m_nd.next

        for i in xrange(m, n):
            temp = post_n_nd.next
            post_n_nd.next = n_nd
            n_nd = post_n_nd
            post_n_nd = temp

        pre_m_nd.next = n_nd
        m_nd.next = post_n_nd

        return dummy.next



            
