"""
Any two nodes in a binary tree have a common ancestor, namely the root. The lowest common
ancestor (LCA) of any two nodes in a binary tree is the node furthest from the root that is an ancestor
of both nodes.

Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not
have a parent field.
"""
import collections


# Traverse the tree and return the count of nodes found which matches the nodes
# to search
# If reached end, return 0 and None

# Time Complexity - O(n)
# Space Complexity - O(h)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def lca(tree, node0, node1):
    Status = collections.namedtuple('Status', ('num_of_nodes_found', 'ancestor'))

    def lca_helper(tree: TreeNode, node0: TreeNode, node1: TreeNode):
        if not tree:
            return Status(0, None)
        
        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_of_nodes_found == 2:
            return left_result
        right_result = lca_helper(tree.left, node0, node1)
        if right_result.num_of_nodes_found == 2:
            return right_result
                
        num_of_nodes_found = (
            left_result.num_of_nodes_found
            + right_result.num_of_nodes_found
            + int(tree is node0)
            + int(tree is node1)
        )

        return Status(num_of_nodes_found, tree if num_of_nodes_found == 2 else None)

    return lca_helper(tree, node0, node1).ancestor

