"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
and postorder is the postorder traversal of the same tree, construct and return the binary tree.
"""
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
        
        def helper(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_start >= inorder_end or postorder_start >= postorder_end:
                return None
            
            root_inorder_idx = node_to_inorder_idx[postorder[postorder_end - 1]]
            left_subtree_size = root_inorder_idx - inorder_start
            
            left_subtree = helper(
                inorder_start,
                root_inorder_idx,
                postorder_start,
                postorder_start + left_subtree_size,
            )
            right_subtree = helper(
                root_inorder_idx + 1,
                inorder_end,
                postorder_start + left_subtree_size,
                postorder_end - 1
            )
            
            return TreeNode(
                postorder[postorder_end - 1],
                left_subtree,
                right_subtree
            )
        
        return helper(0, len(inorder), 0, len(postorder))
        