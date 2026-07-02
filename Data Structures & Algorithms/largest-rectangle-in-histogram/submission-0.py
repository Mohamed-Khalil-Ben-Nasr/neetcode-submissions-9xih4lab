class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBounds, rightBounds = [0] * len(heights), [0] * len(heights)
        # right bounds = first shorter bar to the right 
        stack = []
        for i in range(len(heights)-1, -1 ,-1):
            # pop all current elements in the stack that >= current height
            # this is because we found a closer + shorter bar
            # so we can discard the farther + equal/longer bar
            while stack and  heights[i] <= stack[-1][0]:
                stack.pop()
            # if the stack becomes empty
            # => no element to the right of i thats shorter than current height
            # => right bound is len(heights)
            if not stack:
                rightBounds[i] = len(heights)
            else:
                rightBounds[i] = stack[-1][1]
            stack.append([heights[i], i])

        # left bounds
        stack2 = []
        for i in range(len(heights)):

            while stack2 and  heights[i] <= stack2[-1][0]:
                stack2.pop()

            if not stack2:
                leftBounds[i] = -1
            else:
                leftBounds[i] = stack2[-1][1]
            
            stack2.append([heights[i], i])
        
        res = 0
        for i in range(len(heights)):
            curArea = (rightBounds[i] - leftBounds[i] - 1) * heights[i]
            res = max(res, curArea, heights[i])
        
        return res

            
        


    


