"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthList = []

        def findKthSmallest(node):
            if node and len(kthList) < k:
                findKthSmallest(node.left)
                if len(kthList) < k:
                    kthList.append(node.val)
                    findKthSmallest(node.right)
        findKthSmallest(root)
        return kthList[-1]