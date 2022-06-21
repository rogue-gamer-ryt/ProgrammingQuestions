"""
Write a program that tests whether a singly linked list is palindromic
"""

# Reverse the second part of the list
# Traverse both the parts together and check

class ListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

def reverse_list(L, start, finish):
    dummy_head = sublist_head = ListNode(0)
    for _ in range(start):
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next

    for _ in range(finsih - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next =
        temp.next, sublist_head.next, temp

    return dummy_head.next

# Time Complexity - O(n)
# Space Complexity - O(1)
def is_linked_list_a_palindrome(L):
    slow = fast = L
    half_length = 0
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        half_length += 1

    first_half_iter, second_half_iter = L, reverse_list(L, half_length, half_length*2)
    while first_half_iter.next and second_half_iter.next:
        if first_half_iter != second_half_iter:
            return False
        first_half_iter, second_half_iter = (first_half_iter.next,
                                            second_half_iter.next)

    return True