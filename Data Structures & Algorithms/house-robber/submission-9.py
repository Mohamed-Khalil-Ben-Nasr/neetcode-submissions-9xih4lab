class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
            
        dp = [0 for i in range(len(nums))]
        dp[len(nums)-1] = nums[len(nums)-1]
        dp[len(nums)-2] = max(nums[len(nums)-2], nums[-1])
        for i in range(len(nums)-3, -1, -1):
            dp[i] = max(dp[i+1], nums[i]+dp[i+2])
        
        return dp[0]