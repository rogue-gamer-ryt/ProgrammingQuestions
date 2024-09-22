"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Link: https://leetcode.com/problems/edit-distance/
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf') for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(dp)):
            dp[i][-1] = len(word1) - i

        for j in range(len(dp[0])):
            dp[-1][j] = len(word2) - j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],
                        dp[i + 1][j + 1],
                        dp[i][j + 1],
                    )
        return dp[0][0]