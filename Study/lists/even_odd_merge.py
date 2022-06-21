"""
Consider a singly linked list whose nodes are numbered starting at 0. Define the even-odd merge of
the list to be the list consisting of the even-numbered nodes followed by the odd-numbered nodes.

Write a program that computes the even-odd merge.
"""

# Store the heads of Even nodes and odd nodes separetly
# Use an indicator variable to tell us which list to append to
# Append the odd to even

class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

# Time Complexity: O(N)
# Space Complexity: O(1)
def even_odd_merge(L):
    if not L:
        return L
    
    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1 # Alternate between even and odd (0 ^ 1 = 1 and 1 ^ 1 = 1)
    
    tails[1].next = None # Since Last Odd node should be the tail
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next