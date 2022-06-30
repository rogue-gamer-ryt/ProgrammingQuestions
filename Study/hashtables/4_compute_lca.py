"""
Design an algorithm for computing the LCA of two nodes in a binary tree. The algorithm's time
complexity should depend only on the distance from the nodes to the LCA.
"""

# Everytime we visit a node we can check if that node has been already visited

# Time - O(D0 + D1) | Space - O(D0 + D1) where d is distance between a node and lca
def lca(node_0, node_1):
    iter_0, iter_1 = node_0, node_1
    nodes_on_path_to_root = set()

    while iter_0 or iter_1:
        if iter_0:
            if iter_0 in nodes_on_path_to_root:
                return iter_0
            nodes_on_path_to_root.add(iter_0)
            iter_0 = iter_0.parent
        
        if iter_1:
            if iter_1 in nodes_on_path_to_root:
                return iter_1
            nodes_on_path_to_root.add(iter_1)
            iter_1 = iter_1.parent
    raise ValueError('not in the same tree')