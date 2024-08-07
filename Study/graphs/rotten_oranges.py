"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Link: https://leetcode.com/problems/rotting-oranges/
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        visit = set()
        q = collections.deque()
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges +=1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1,0], [0, 1], [0, -1], [-1, 0]]

        while q and fresh_oranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh_oranges -=1
            time += 1
        return time if fresh_oranges == 0 else -1

