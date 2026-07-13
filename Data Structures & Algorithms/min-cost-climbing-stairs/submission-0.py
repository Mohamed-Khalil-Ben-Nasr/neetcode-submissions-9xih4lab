class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(cost):
                return 0

            # decision tree
            dp[i] = min(dfs(i+1), dfs(i+2)) + cost[i]

            return dp[i] 
        
        return min(dfs(0), dfs(1))

        