class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue  # skip the destination, already set to 1
                if r + 1 < m:
                    dp[r][c] += dp[r+1][c]
                if c + 1 < n:
                    dp[r][c] += dp[r][c+1]
        return dp[0][0]
