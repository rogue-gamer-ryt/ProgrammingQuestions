"""
The lists may each or both have a cycle. If such a node exists, return a node that appears first 
when traversing the lists. This node may not be unique-if one node ends in a cycle, the first 
cycle node encountered when traversing it may be different from the first cycle node encountered 
when traversing the second list, even though the cycle is the same. In such cases, 
you may retum either of the two nodes.
"""

# The problem can have three cases
# 1. Neither of the lists are cyclic -> Check for intersecting nodes for a non-cyclic list
# 2. If one is cyclic and other is not -> They cannot overlap. Return None
# 3. If both are cyclic -> Cycles must be identical
#   a. The paths to the cycle merge before the cycle -> There is a unique first node that is common
#   b. The paths reaches cycle at different nodes -> We can get the first node of the cycle for both the lists

class ListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

def has_cycle(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None

def overlapping_no_cycle_lists(L1, L2):
    # Check the lengths of both the lists
    # Use the longest list value and get the difference between their lengths
    # Let one pointer traverse till the difference
    # Get another pointer to start from the shorter list and now let both pointers move together
    # When both pointers reach a common node that is the intersection. If either becomes None then 
    # no intersection
    def length(L):
        length = 0
        while L:
            L = L.next
            length += 1
        return length
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L2, L1 = L1, L2
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next

    return L1

def distance(a, b):
    dis = 0
    while a is not b:
        a = a.next
        dis += 1
    return dis


def overlapping_lists_with_cycles(L1, L2):
    # Store the start of cycle if any
    root1, root2 = has_cycle(L1), has_cycle(L2)

    if not root1 and not root2:
        return overlapping_no_cycle_lists(L1, L2)
    elif (root1 and not root2) or (not root1 and root2):
        # No intersection if only one cycle
        return None
    
    # To check if there are any disjoint cycles. 
    # Before reaching the end of root2 it should reach root1 if it exits in the same cycle
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break
    
    # L1 and L2 do not end in the same cycle
    if temp is not root1:
        return None

    # L1 and L2 end in same cycle, locate the overlapping node if they 
    # first overlap before cycle starts
    stem1_length, stemp2_length = distance(L1, root1), distance(L1, root2)
    if stem1_length > stemp2_length:
        L2, L1 = L1, L2
        root1, root2 = root2, root1
    for _ in range(abs(stem1_length - stem2_length)):
        L2 = L2.next
    
    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2 = L1.next, L2.next
    
    # If L1 == L2 before reaching root1, it means overlap first occurs before the cycle
    # starts; otherwise the first overlapping node is not unique, we can return any node
    # on the cycle

    return L1 if L1 is L2 else root1
    
    
    