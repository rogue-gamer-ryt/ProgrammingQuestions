"""
Write a pro$am that takes as input a BST and a value, and retums the first key that would appear
in an inorder traversal which is greater than the input value.
"""

# Time - O(h) | Space O(1)
def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right
    return first_so_far
