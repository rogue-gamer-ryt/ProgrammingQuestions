"""
Given two nodes in a binary tree, design an algorithm that computes their Least Common Ancestor. 
Assume that each node has a parent pointer.
"""

# If both the nodes are at the same depth, we traverse UP using the parent and stop 
# when we find the same node
# If not, we bring both the nodes at the same depth by traversing the node below upto
# the same height

# Time complexity - O(h)
# Space complexity - O(1)
def lca(tree, node0, node1):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth
    
    depth0 = get_depth(node0)
    depth1 = get_depth(node1)

    # Making node0 as the deeper node, to reduce code lines
    if depth0 < depth1:
        node0, node1 = node1, node0
    
    depth_diff = abs(depth0 - depth1)
    while depth_diff:
        depth_diff -= 1
        node0  = node0.parent
    
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0
