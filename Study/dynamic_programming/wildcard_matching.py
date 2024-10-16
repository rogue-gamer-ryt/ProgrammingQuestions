"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Link: https://leetcode.com/problems/wildcard-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prevRow = [False] * (len(p) + 1)
        currRow = [False] * (len(p) + 1)

        prevRow[0] = True
        for col in range(1, len(p) + 1):
            prevRow[col] = prevRow[col - 1] if p[col - 1] == "*" else False

        for r in range(1, len(s) + 1):
            for c in range(1, len(p) + 1):
                if s[r - 1] == p[c - 1] or p[c - 1] == "?":
                    currRow[c] = prevRow[c - 1]

                elif p[c - 1] == "*":
                    currRow[c] = prevRow[c] or currRow[c - 1]

                else:
                    currRow[c] = False
            # print(prevRow, currRow)
            prevRow = currRow.copy()
            currRow[0] = False

        return prevRow[-1]