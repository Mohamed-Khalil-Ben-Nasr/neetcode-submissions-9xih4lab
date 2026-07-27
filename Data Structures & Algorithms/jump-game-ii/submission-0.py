class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            # cache hit
            if i in dp:
                return dp[i]
            
            # success 
            if i >= len(nums)-1:
                return 0
            
            dp[i] = len(nums)+1
            for j in range(1, nums[i]+1):
                dp[i] = min(dp[i], dfs(i+j))
            dp[i] += 1
            return dp[i]
        
        return dfs(0)




