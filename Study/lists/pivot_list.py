"""
For any integer k, the pivot of a list of integers with respect to k is that list with its nodes reordered so
that all nodes containing keys less than k appear before nodes containing k, and all nodes containing
keys greater than k appear after the nodes containing k

Implement a function which takes as input a singly linked list and an integer k and performs a pivot
of the list with respect to k. The relative ordering of nodes that appear before k, and after k, must
remain unchanged; the same must hold for nodes holding keys equal to k.
"""

# Create three inplace partitions in the orginal list
# 1. Smaller than
# 2. Equal
# 3. Greater than
# In the end we combine them (point a tail of one part to head of another part)

class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

# Time complexity: O(n)
# Space complexity: O(1)
def list_pivoting(L, x):
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    # Populate them
    while L:
        if L.data < x:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data = x:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else:
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next
    
    # Combine the three
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next

    return less_head.next

