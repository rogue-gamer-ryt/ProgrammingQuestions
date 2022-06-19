"""
Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field
your program can change in a node is its next field.
"""
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

# Time complexity - O(n + m)
def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L2 or L1
    return dummy_head.next
