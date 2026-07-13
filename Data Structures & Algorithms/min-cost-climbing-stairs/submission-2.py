class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # constraint: 2 <= cost.length <= 100
        two = cost[len(cost)-1]
        one = cost[len(cost)-2]
        for i in range(len(cost)-3, -1, -1):
            new = min(one, two) + cost[i]
            two = one
            one = new

        return min(one, two)


