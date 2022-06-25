"""
For this Problem, assume that each binary tree node has a extra field, call it level-nex! that holds a
binary tree node (this field is distinct from the fields for the left and right children). The level-next
field will be used to compute a map from nodes to their right siblings. The input is assumed to be
perfect binary tree.

Write a program that takes a perfect binary tree, and sets each node's level-next field to the node on
its right, if one exists.
"""

# Right sibling of a left child would be the right child of its parents
# Right sibling of a right child would be the left child of its parents right sibling

# Time complexity - O(n)
# Space complexity - O(h)
def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            # Populate left child's next field
            start_node.left.next = start_node.right
            # populate right child's next field
            start_node.right.next = start_node.next and start_node.next.left

            start_node = start_node.next
        
    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left
