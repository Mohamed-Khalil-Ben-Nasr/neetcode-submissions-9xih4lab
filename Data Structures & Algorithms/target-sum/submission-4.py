class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = 0
        for num in nums:
            totalSum += num
        dp = [ [0 for j in range(2 * totalSum + 1)] for i in range(len(nums)+1)]
        if target > totalSum:
            return 0
        offset = totalSum
        dp[len(nums)][target + offset] = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(2 * totalSum, -1, -1):
                add = 0
                if (j + nums[i]) < len(dp[0]):
                    add = dp[i+1][j + nums[i]]
                substract = 0
                if (j - nums[i]) >= 0:
                    substract = dp[i+1][j-nums[i]]
                dp[i][j] = add + substract
        return dp[0][0+offset]
        
