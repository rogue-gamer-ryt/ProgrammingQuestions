"""
Given two singly linked lists there may be list nodes that are common to both. (This may not be a
bug-it may be desirable from the perspective of reducing memory footprint, as in the flyweight
pattem, or maintaining a canonical form.) For example, the lists in Figure 7.6 on the following page
overlap at Node I.
Write a Program that takes two cycle-free singly linked lists, and determines if there exists a node
that is common to both lists.
"""

# There would be an overlapping nodes if both the linkedlist have the same tail node
# Compute the length of each list
# Have two pointers. One to be at 0 and other to be at the difference in the lengths
#  of both lists for whichever list is the longes

def overlapping_no_cycle_lists(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next

    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next

    return L1
