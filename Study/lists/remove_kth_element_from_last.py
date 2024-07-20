"""
Given a singly linked list and an integer k, write a program to remove the kth last element from the
list. Your algorithm cannot use more than a few words of storage, regardless of the length of the
list. In particulaq, you cannot assume that it is possible to record the length of the list.

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

# Have two pointers
# Move one to k positions
# Move both together until 1st one is None
# The second one should be at the element which has to be removed

# Time complexity - O(n)
# Space complexity - O(1)
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next


    second = dummy_head.next
    while first:
        first, second = first.next, second.next
    # Second points to the K+1 th node, deletes its successor
    second.next = second.next.next
    return dummy_head.next

