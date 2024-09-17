
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = [1 for _ in range(COLS)]
        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[c] += dp[c - 1]
        return dp[-1]