"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Link: https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prefix = 1

        for i in range(N):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(N - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res