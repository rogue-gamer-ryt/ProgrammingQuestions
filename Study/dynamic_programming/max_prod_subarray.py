"""
Given an integer array nums, find a  subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Link: https://leetcode.com/problems/maximum-product-subarray/
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            prevCurMax = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * prevCurMax, n * curMin, n)
            res = max(res, curMax)
        return res