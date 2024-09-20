"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally
or move outside the boundary (i.e., wrap-around is not allowed).



Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]
            # res = 1
            res = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c]),
            )
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
