class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        res = nums[0]

        for num in nums:
            if cur <= 0:
                cur = 0
            
            cur += num
            res = max(res,cur)
        
        return res