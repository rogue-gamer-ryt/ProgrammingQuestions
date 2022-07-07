"""
Given a sorted array, the number of BSTs that can be built on the entries in the array grows
enormously with its size. Some of these trees are skewed, and are closer to lists; others are more
balanced.

How would you build a BST of minimum possible height from a sorted array?
"""

# We can make the middle element as the root and then divide the array into left subtree and right subtree

def build_min_height_bst_from_sorted_array(A):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BSTNode(
            A[mid], 
            build_min_height_bst_from_sorted_subarray(start + 1, mid),
            build_min_height_bst_from_sorted_subarray(mid + 1, end)
        )
    
    return build_min_height_bst_from_sorted_subarray(0, len(A))

