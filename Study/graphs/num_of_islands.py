class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()

            visited.add((r, c))
            q.append((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                (row, col) = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and
                            0 <= c < cols and
                            grid[r][c] == "1" and
                            (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and (r, c) not in visited):
                    bfs(r, c)
                    res += 1
        return res