class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[n] = 1
        for i in range(n-1, -1,-1):
            dp[i] += dp[i+1]
            if i + 2 < n+1:
                dp[i] += dp[i+2]
        return dp[0]