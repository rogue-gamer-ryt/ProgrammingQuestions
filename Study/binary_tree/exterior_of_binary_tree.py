"""
The exterior of a binary tree is the following sequence of nodes: the nodes from the root to
the leftmost leaf, followed by the leaves in left-to-right order, followed by the nodes from the
rightmost leaf to the root. (By leftmost (rightmost) leaf, we mean the leaf that appears first (last)
in an inorder traversal.)

Write a program that computes the exterior of a binary tree.
"""

# Time complexity - O(n)
def exterior_binary_tree(tree):
    def is_leaf(node):
        return not node.left and not node.right
    
    # Get all left boundary and leaf nodes in left subtree
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        
        return (
            ([subtree] if is_boundary or is_leaf(subtree) else [])
            + left_boundary_and_leaves(subtree.left, is_boundary)'
            # We need to add nodes from right only if there are no left nodes and it is for boundary
            + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)
        )
    
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        
        return (
            right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right)
            + right_boundary_and_leaves(subtree.right, is_boundary)
            + ([subtree] if is_boundary or is_leaf(subtree) else [])
        )

    return (
        [tree]
        + left_boundary_and_leaves(tree.left, True)
        + right_boundary_and_leaves(tree.right, True)
        if tree else []
    )