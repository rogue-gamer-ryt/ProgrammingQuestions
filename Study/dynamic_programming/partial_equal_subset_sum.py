"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Link: https://leetcode.com/problems/partition-equal-subset-sum/
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            newDP = dp.copy()
            for t in dp:
                if t + nums[i] == target:
                    return True
                newDP.add(t + nums[i])
            dp = newDP
        return True if target in dp else False

