class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ n for i in range(len(nums))]
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    dp[i] = min(dp[i], dp[i+j])
            dp[i] += 1
        return dp[0]