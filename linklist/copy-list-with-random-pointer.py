# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:

    def copyRandomList(self, head):
        self.node_buffer = dict()
        return self.copyRandomListHelper(head)


    # return a deep copy of node
    def copyRandomListHelper(self, node):

        if node is None:
            return None

        if node.label in self.node_buffer:
            return self.node_buffer[node.label]

        new_node = RandomListNode(node.label)
        self.node_buffer[node.label] = new_node

        next_nd = self.copyRandomListHelper(node.next)
        new_node.next = next_nd

        random_nd = self.copyRandomListHelper(node.random)
        new_node.random = random_nd

        return new_node
