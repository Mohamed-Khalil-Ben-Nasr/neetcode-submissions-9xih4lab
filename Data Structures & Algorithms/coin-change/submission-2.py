class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            dp[i] = float("inf")
            for coin in coins:
                dp[i] = min(dp[i], 1 + dfs(i - coin))
            return dp[i]

        dfs(amount)
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]