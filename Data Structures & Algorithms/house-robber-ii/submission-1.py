class Solution:
    def rob(self, nums: List[int]) -> int:
        # since we cant rob the first and last house 
        # we run house robber 1 solution twice 
        # one run we skip first house to be able to include last house
        # one run we skip last house to be able to include first house
        # then pick max
        # the flags approach is booboo
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
            