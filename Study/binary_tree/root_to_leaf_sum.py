"""
You are given a binary tree where each node is labeled with an integer. The path weight of a node in
such a tree is the sum of the integers on the unique path from the root to that node.

Write a program which takes as input an integer and a binary tree with integer node weights, and
checks if there exists a leaf whose path weight equals the given integer
"""

# Traverse the tree, check if the node value is equal to the remaining_weight if yes, return True
# If not we can traverse further in left and right and subtract the node value from remaining_weight

# Time complexity - O(n)
# Space complexity - O(h)
def has_path_sum(tree, remaining_weight):
        if not tree:
            return False
        if not tree.left and not tree.right:
            return remaining_weight == tree.data
        
        return (has_path_sum(tree.left, remaining_weight - tree.data) 
        or has_path_sum(tree.right, remaining_weight - tree.data))
        
