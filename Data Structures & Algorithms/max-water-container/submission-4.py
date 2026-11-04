class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while l < r:
            # r - l + 1 to count num of array elements included
            # r - l to count actual distance
            cur = (r - l) * min(heights[l], heights[r])
            res = max(res, cur)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res