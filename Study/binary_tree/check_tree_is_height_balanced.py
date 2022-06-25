"""
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of
its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete
binary tree. A height-balanced binary tree does not have to be perfect or complete

Write a program that takes as input the root of a binary tree and checks whether the tree is heightbalanced.
"""

# We need two things from the child nodes
# 1. Is the child node balanced
# 2. What is the height of the child node
# Checks to perform at the parent node
# a. Check if the child nodes are balanced
# b. Height difference is <= (atmost) 1
#  If true return the height and is_balanced as True for the parent's parent to check

# Time complexity - O(n)
# Space complexity - O(h) h-> height of the tree
def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
    
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        
        left_tree_result = check_balanced(tree.left)
        if not left_tree_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        right_tree_result = check_balanced(tree.right)
        if not right_tree_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        is_balanced = abs(left_tree_result.height - right_tree_result.height) <= 1
        height = max(left_tree.height, right_tree.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    
    return check_balanced(tree).balanced
