"""
Many different binary trees have the same preorder traversal sequence.
In this problem, the preorder traversal computation is modified to mark where a left or right
child is empty.

Design an algorithm for reconstructing a binary tree from a preorder traversal visit sequence that
uses null to mark empty children.
"""

# Time complexity - O(n)
# Space complexity - O(1)
def reconstruct_preorder(preorder):
    def reconstruct_preorder_helper(preorder_iter):
        subtree_key = next(preorder_iter) # updated the preorder_iter to its next value

        if not subtree_key:
            return None
        left_subtree = reconstruct_preorder_helper(preorder_iter)
        right_subtree = reconstruct_preorder_helper(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct_preorder_helper(iter(preorder))
