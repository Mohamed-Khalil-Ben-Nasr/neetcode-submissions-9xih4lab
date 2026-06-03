class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
            
        dp[1] = max(nums[1], dp[0])
        if len(nums) == 2:
            return dp[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums)-1]