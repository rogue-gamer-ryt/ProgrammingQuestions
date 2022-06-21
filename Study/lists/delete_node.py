"""
Given a node in a singly linked list, deleting it in O(1) time appears impossible because its predecessor's
next field has to be updated. Surprisingly, it can be done with one small caveat-the node
to delete cannot be the last one in the list and it is easy to copy the value part of a node.
"""

class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next