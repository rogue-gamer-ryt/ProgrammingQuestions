"""
Write a program that takes as input a singly linked list of integers in sorted order, and removes
duplicates from it. The list should be sorted.
"""
class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

# Remove all the successive nodes with the same value as the current node

def remove_duplicates(L):
    it = L
    while it:
        # Uses next_distinct to find the next distinct value
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L