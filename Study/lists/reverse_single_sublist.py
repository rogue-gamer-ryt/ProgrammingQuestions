"""
Write a program which takes a singly linked list L and two integers s and f as arguments, and
reverses the order of the nodes from the sth node to fth node, inclusive. The numbering begins at
1., i.e., the head node is the first node. Do not allocate additional nodes
"""

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def reverse_sublist(L, start, finish):
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    #  if s = 2 and f = 5 (2nd and 5th Nodes)
    
    # ListNode(data=0, next_node=L) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    
    dummy_head = sublist_head = ListNode(data=0, next_node=L)
    for _ in range(1, start):
        sublist_head = sublist_head.next
    # sublist_head = ListNode(1)

    # Reverse the sublist
    sublist_iter = sublist_head.next # sublist_iter = ListNode(2)

    for _ in range(finish - start): # Number of loops - 3
        temp = sublist_iter.next   # first value of temp -> ListNode(3)
        # First iteration - temp = 3, sublist_iter = 2, sublist_head = 1
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
        # After this - temp.next = 2, sublist_iter.next = 2, sublist_head.next = 2


    return dummy_head.next
