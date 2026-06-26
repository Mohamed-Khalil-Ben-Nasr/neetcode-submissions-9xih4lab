class Solution:
    def trap(self, heights: List[int]) -> int:
        # the invariant of the loop is:
        # whichever side you process, the other side's max is 
        # >= the current side's max 
        # => so we are always computing the correct limiting side wall
        l, r = 0, len(heights)-1
        maxLeft = heights[0]
        maxRight = heights[len(heights)-1]
        res = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                water = maxLeft - heights[l]
                res += water if water > 0 else 0
                maxLeft = max(maxLeft, heights[l])
            else:
                r -= 1
                water = maxRight - heights[r]
                res += water if water > 0 else 0
                maxRight = max(maxRight, heights[r])
        return res
