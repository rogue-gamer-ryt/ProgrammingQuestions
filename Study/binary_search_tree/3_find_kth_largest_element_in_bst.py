"""
Write a program that takes as input a BST and an integer k, and retums the k largest elements in the
BST in decreasing order.
"""

# Time O(h + k)
def find_k_largest_in_bst_tree(tree, k):
    def find_k_largest_in_bst_helper(tree):
        # Perform reverse inorder traversal
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements
