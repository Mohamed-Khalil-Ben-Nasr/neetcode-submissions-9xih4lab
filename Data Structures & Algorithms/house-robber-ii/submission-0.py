class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob1(nums):
            dp = [-1] * len(nums)
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                prev = 0
                if (i-2) >= 0:
                    prev = dp[i-2]
                dp[i] = max(nums[i] + prev, dp[i-1])
            return dp[len(nums)-1]
        
        return max(rob1(nums[:len(nums)-1]), rob1(nums[1:]))
            