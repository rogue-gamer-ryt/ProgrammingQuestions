"""
Write a program that takes as input a singly linked list and a nonnegative integer k, and retums the
list cyclically shifted to the right by k. See Figure 7.9 for an example of a cyclic right shift.
"""

class ListNode:
    def __init__(self, data = 0, next_node):
        self.data = data
        self.next = next


# We need to shift the lists by K 
# So the head would be at the Kth postion from the start in the new list
# That means the new head would be at the (n - k)th node in the initial list

# Time complexity: O(n)
# Space complexity: O(1)
def cyclically_right_shift_list(L, K):
    if not L:
        return L
    tail, n = L, 1
    while tail.next: # We need to be at the last element so we can connect it to the head
        n += 1
        tail = tail.next
    # If k > n. It makes sense to take a mod 
    k %= n
    if k == 0:
        return L
    
    tail.next = L # Making it cyclic
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None # Break the cycle

    return new_head
