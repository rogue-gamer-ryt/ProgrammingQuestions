"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Link: https://leetcode.com/problems/distinct-subsequences/
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s, t = " " + s, " " + t
        dp = [[0 for _ in range(len(t))] for _ in range(len(s))]

        for r in range(len(s)):
            dp[r][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

