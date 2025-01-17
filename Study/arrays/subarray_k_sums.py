"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Link: https://leetcode.com/problems/subarray-sum-equals-k/
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum(i, j) = prefix_sum(0, j) - prefix_sum(0, i) where j > i
        prefix_sums = { 0 : 1 }
        curr = res = 0
        for n in nums:
            curr += n 
            diff = curr - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[curr] = 1 + prefix_sums.get(curr, 0)
            
        return res