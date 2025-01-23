"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on 
that cell there is a server and 0 means that it is no server. Two servers are said to communicate if 
they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
 
Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Link: https://leetcode.com/problems/count-servers-that-communicate/
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        row = defaultdict(int)
        col = defaultdict(int)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if row[r] > 1 or col[c] > 1:
                        res += 1

        return res
