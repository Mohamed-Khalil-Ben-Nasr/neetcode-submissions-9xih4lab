class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = max(nums)

        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMin
            curMin = min(curMax * num, curMin * num, num)
            curMax = max(curMax * num, tmp * num, num)
            res = max(res, curMin, curMax)
        return res