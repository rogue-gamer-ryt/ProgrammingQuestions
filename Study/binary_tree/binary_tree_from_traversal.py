"""
Given an inorder traversal sequence and a preorder traversal sequence of a binary tree write a
program to reconstruct the tree. Assume each node has a unique key.
"""
# Use the preorder to get the root node
# Split the inorder into left subtree an right subtree
# Further split them by taking the individual subtree info from preorder

def binary_tree_from_preorder_inorder(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end]
    def helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        
        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start

        left_subtree = helper(
            preorder_start + 1, 
            preorder_start + 1 + left_subtree_size, 
            inorder_start, 
            root_inorder_idx
            )
        
        right_subtree = helper(
            preorder_start + 1 + left_subtree_size, 
            preorder_end, 
            root_inorder_idx + 1, 
            inorder_end
            )

        return BinaryTreeNode(
            preorder[preorder_start],
            # get the left subtree
            left_subtree,
            # Get the right subtree
            right_subtree
        )
    
    return helper(0, len(preorder), 0, len(inorder))

