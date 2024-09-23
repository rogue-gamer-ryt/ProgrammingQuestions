"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Link: https://leetcode.com/problems/burst-balloons/

"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        points = [1] + nums + [1]
        n = len(points)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for length in range(2, n):
            for l in range(n - length):
                r = l + length
                for i in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r] + points[l] * points[i] * points[r])
        return dp[0][n - 1]