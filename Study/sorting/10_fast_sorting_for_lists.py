"""
Implement a routine which sorts lists efficiently. It should be a stable sort, i.e., the relative positions
of equal elements must remain unchanged.
"""

# Time - O(n**2)
def insertion_sort(L):
    dummy_head = ListNode(0, L)
    while L and L.next:
        if L.data > L.next.data:
            target, pre = L.next, dummy_head
            while pre.next.data < target.data:
                pre = pre.next
            temp, pre.next, L.next = pre.next, target, target.next
            target.next = temp
        else:
            L = L.next
    return dummy_head.next

# Using mergesort
# Time  - O(nlogn) | Space - (logn)
def stable_sort_list(L):
    # Base cases: L is empty or single node, nothing to do
    if not L or not L.next:
        return L
    
    # Find midpoint of L 
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        slow, fast = slow.next, fast.next.next
    pre_slow.next = None # Splitting the lists into two
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))

def merge_two_sorted_lists(L1, L2):
    tail = dummy_head = ListNode(0)
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L1.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next
