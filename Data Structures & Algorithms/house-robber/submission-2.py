class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            two = 0
            if (i - 2) >= 0:
                two = dp[i-2]
            dp[i] = max(dp[i-1], two + nums[i])
        return dp[len(nums)-1]