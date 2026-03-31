class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = nums[0]
        curPro = 1
        for num in nums:
            tmp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(tmp * num, curMin * num, num)
            res = max(curMax, res)

        return res