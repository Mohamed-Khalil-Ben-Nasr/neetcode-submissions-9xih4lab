class Solution:
    def trap(self, heights: List[int]) -> int:
        # compute max left for each position
        # O(n)
        maxLeft = [0] * len(heights)
        for i in range(1, len(heights)):
            maxLeft[i] = max(maxLeft[i-1], heights[i-1])
        # compute max right for each position
        # O(n)
        maxRight = [0] * len(heights)
        for i in range(len(heights)-2,-1,-1):
            maxRight[i] = max(maxRight[i+1], heights[i+1])
        # compute max area of water
        # O(n)
        res = 0
        for i in range(len(heights)):
            water = min(maxRight[i], maxLeft[i]) - heights[i]
            res += water if water > 0 else 0
        return res

        