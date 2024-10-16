"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Link: https://leetcode.com/problems/regular-expression-matching/
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Add whitespace since dp would be (1 + len(s)) * (1 + len(p))
        s, p = ' ' + s, ' ' + p
        lenS, lenP = len(s), len(p)
        dp = [[False] * lenP for _ in range(lenS)]
        dp[0][0] = True

        for col in range(1, lenP):
            if p[col] == "*":
                dp[0][col] = dp[0][col - 2]

        for r in range(1, lenS):
            for c in range(1, lenP):
                if p[c] in {s[r], '.'}:
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[c] == "*":
                    dp[r][c] = dp[r][c - 2] or (dp[r - 1][c] and p[c - 1] in {s[r], '.'})
        return dp[-1][-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                # if a * is there, we can either use it or not use it
                cache[(i, j)] = ((match and dfs(i + 1, j)) or dfs(i, j + 2))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)