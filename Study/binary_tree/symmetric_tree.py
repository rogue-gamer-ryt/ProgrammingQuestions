"""
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree
is the mirror image of the right subtree.

Write a program that checks whether a binary tree is symmetric
"""

# We can invert the right subtree and check if it matches with left sub tree recursively
# However, we can directly compare the pair of subtrees are mirror images, 
# if a pair is not we directly return False

# Time complexity - O(n)
# Space complexity - O(h)
def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        
        elif subtree_0 and subtree_1:
            return (subtree_o.data == subtree_1.data) and 
            check_symmetric(subtree_0.left, subtree_1.right) and 
            check_symmetric(subtree_0.right == subtree_1.left)
        # If one subtree is empty and other is not
        return False
    return not tree or check_symmetric(tree.left, tree.right)
