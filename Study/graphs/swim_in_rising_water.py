"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim
infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square
(0, 0).

Example 1:

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Link: https://leetcode.com/problems/swim-in-rising-water/

"""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit.add((0, 0))
        while minHeap:
            currHeight, r, c = heapq.heappop(minHeap)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return currHeight

            for dr, dc in directions:

                row, col = r + dr, c + dc
                if (row, col) in visit or row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                    continue
                visit.add((row, col))
                heapq.heappush(minHeap, (max(grid[row][col], currHeight), row, col))
