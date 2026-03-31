class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        m = -1

        while l<r:
            h = min(heights[l], heights[r])
            cur = h * (r-l)
            m = max(cur, m)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return m