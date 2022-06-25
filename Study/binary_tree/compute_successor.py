"""
The successor of a node in a binary tree is the node that appears immediately after the given node
in an inorder traversal.

Design an algorithm that computes the successor of a node in a binary tree. Assume that each node
stores its parent.
"""

# Inorder - left -> root -> right
# If given node has a nonempty right subtree, its successort must lie in that subtree
# If a node has nonempty right subtree, its successor is the first node visited when performing an 
# inorder traversal in that subtree.
# This node is the "left-most" node in that subtree (recursivley get child =  child.left)

# If a node doesn't have a right subtree
# - if the node is its parent's left child, the parent will be next node we visit -> successor
# - If the node is its parent's right child. We can determine the next visited node by 
# iteratively following parents, stopping when we move up from a left child

# Time complexity - O(h)
# Space complexity - O(1)
def find_successor(node):
    if node.right:
        # Successor is the leftmost element in node's right subtree
        node = node.right
        while node.left:
            node = node.left
        return node
    
    # Find the closest ancestor whose left subtree contains node
    # Will continue to move up until it finds a node which is in left subtree of their parent
    while node.parent and node.parent.right is node:
        node = node.parent
    
    
    return node.parent # A return value of None means the node doesn't have successor



