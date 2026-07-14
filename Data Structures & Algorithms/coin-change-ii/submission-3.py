class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, cur):
            if (i, cur) in dp:
                return dp[(i, cur)]

            if i >= len(coins) or cur > amount:
                return 0

            if cur == amount:
                return 1
            
            dp[(i,cur)] = dfs(i+1, cur) + dfs(i, cur+coins[i])
            return dp[(i,cur)]
        
        return dfs(0, 0)