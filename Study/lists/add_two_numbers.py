"""
A singly linked list whose nodes contain digits can be viewed as an integer, with the least significant
digit coming first. Such a representation can be used to represent unbounded integers. This problem
is concerned with adding integers represented in this fashion,

Write a program which takes two singly linked lists of digits, and returns the list corresponding to
the sum of the integers they represent. The least significant digit comes first.
"""

class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

# Add digit by digit and store the carryforward.
# Compute till there is no input and no carryforward

# Time Complexity: O(n + m)
# Space Complexity: O(max(n, m))
def add_two_numbers(L1, L2):
    place_iter = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        place_iter.next = ListNode(data=val % 10)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter, carry = place_iter.next, val // 10
    return dummy_head.next