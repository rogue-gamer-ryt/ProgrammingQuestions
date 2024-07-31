"""
Given a string s, partition s such that every  substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Link: https://leetcode.com/problems/palindrome-partitioning/
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(pos):
            if pos >= len(s):
                res.append(subset.copy())
                return
            for i in range(pos, len(s)):
                if self.isPali(s, pos, i):
                    subset.append(s[pos : i + 1])
                    dfs(i + 1)
                    subset.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True