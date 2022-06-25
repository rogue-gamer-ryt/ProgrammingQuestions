"""
Consider a binary tree in which each node contains a binary digit. A root-to-leaf path can be
associated with a binary number-the MSB is at the root

Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf
paths
"""

# Time Complexity - O(n)
# Space Complexity - O(h)
def sum_root_to_leaf(tree, partial-path_sum=0):
    if not tree:
        return 0
    
    partial_path_sum  = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right: # Leaf node
        return partial_path_sum
    
    # non leaf
    return (sum_root_to_leaf(tree.left, partial_path_sum)
     + sum_root_to_leaf(tree.right, partial_sum))