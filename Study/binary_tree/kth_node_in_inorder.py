"""
Write a program that efficiently computes the kth node appearing in an inorder traversal. Assume
that each node stores the number of nodes in the subtree rooted at that node.
"""
# Use the information of number of nodes in the subtree
# Since it is inorder (left -> root -> right) if there are 7 nodes in left subtree and you are
# asked to find the 10th node in inorder traversal (k=10) then you know the node is not present
# in the left sub tree entirely cause 7 < 10 (L < k). The element should e (k - L)th node if
# we skip the left subtree entirely

# Time complexity - O(h)
# Space complexity - O(1)
def find_kth_node_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k: #kth node would be in the right subtree
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1: # kth is the iter itself
            return tree
        else: # It is in the left subtree
            tree = tree.left
    return None 

