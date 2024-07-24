"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Link: https://leetcode.com/problems/same-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(t1, t2):
            if not t1 and not t2:
                return True

            if t1 and t2 and t1.val == t2.val:
                return dfs(t1.left, t2.left) and dfs(t1.right, t2.right)
            return False

        return dfs(p, q)