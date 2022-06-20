"""
Write a program that takes the head of a singly linked list and retums null if there does not exist a
cycle, and the node at the start of the cycle, if a cycle is present, (You do not know the length of the
list in advance.)
"""
class ListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

# Time comlexity - O(F) + O(C) => O(n) - O(F)
# Where F is number of nodes to the start of cycle
# C is the number of nodes on the cycle
# n is the total number of nodes
def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Cycle exits
            cycle_len_advanced_iter = head
            # Get another pointer which would be cycle_len ahead
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # Both iterators advance in together (cycle_len_advanced_iter and it)
            # If both are the same then we know the start of the cycle
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            # Iter is the start of cycle
            return it
    return None
