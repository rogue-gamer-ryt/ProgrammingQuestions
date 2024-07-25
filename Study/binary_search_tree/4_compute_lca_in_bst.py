"""
Design an algorithm that takes as input a BST and two nodes, and retums the LCA of the two
nodes.
"""


# Time - O(h)
def find_LCA(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        # keep searching as tree is outside [s, b]
        while tree.data < s.data:
            tree = tree.right  # LCA must be in tree's right child
        while tree.data > b.data:
            tree = tree.left  # LCA must be in tree's left child

    # Now, s.data <= tree.data and tree.data <= b.data
    return tree
