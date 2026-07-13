class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost))]
        # constraint: 2 <= cost.length <= 100
        dp[len(cost)-1] = cost[len(cost)-1]
        dp[len(cost)-2] = cost[len(cost)-2]
        for i in range(len(cost)-3, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        return min(dp[0], dp[1])


