"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,
1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,
0,0,0]] Output: 6 Explanation: The answer is not 11, because the island must be connected 4-directionally.

Link: https://leetcode.com/problems/max-area-of-island/
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            area = 1
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                            0 <= r < rows and
                            0 <= c < cols and
                            (r, c) not in visit and
                            grid[r][c] == 1):
                        visit.add((r, c))
                        area += 1
                        q.append((r, c))

            return area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(area, res)
        return res