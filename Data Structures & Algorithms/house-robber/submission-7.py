class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i] 
            
            if i >= len(nums):
                return 0
            
            rob = nums[i] + dfs(i+2)
            dontRob = dfs(i+1)
            dp[i] = max(rob, dontRob)
            return dp[i]

        return dfs(0)
