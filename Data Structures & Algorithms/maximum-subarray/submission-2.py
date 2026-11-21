class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = float("-inf")
        for num in nums:
            s += num
            res = max(res, s)
            if s < 0:
                s = 0
        
        return res