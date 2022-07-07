"""
Suppose you are given the sequence in which keys are visited in an inorder traversal of a BST, and
all keys are distinct. Can you reconstruct the BST from the sequence? If so, write a program to do
so. Solve the same problem for preorder and postorder traversal sequences.
"""

# It is not possible to construct a tree from only inorder traversal
# Since [1,2,3] can have 5 distinct BSTs
# But it is possible for preorder traversal. In pre order we can split the array into three parts
# Example: [43,23,37,29,31,41,47,53]
# [43 | 23,37,29,31,41 | 47,53]
# root - 43 , left subtree (all elements less than 43) - [23,37,29,31,41], right subtree (all elements
# greate than 43) - [47, 53]
# The left subtree is itself the preorder traversal for left subtree and similarly right subtree is

# Time: worst - O(n**2) best - O(n) balanced BST - O(nlogn)
def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None
    
    transition_point = next((i for i, a in enumerate(preorder_sequence)
                            if a> preorder_sequence[0]), len(preorder_sequence))
    
    retrun BSTNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:])
    )

# Time O(n)
def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_seqeunce):
            return None
        
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1

        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)

        return BSTNode(root, left_subtree, right_subtree)
    
    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))

