from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # invariant of the stack
        # - bottom of the stack in the greatest element
        # - elements are sorted increasingly from top to bottom of stack 
        stack = []
        res = deque([])
        for i in range(len(temperatures)-1, -1, -1):
            curTemp = temperatures[i]
            # pop all elements that are smaller than currentTemp
            while stack and stack[-1][0] <= curTemp:
                stack.pop()
            if stack:
                # now top of the stack is always greater than currentTemp
                res.appendleft(stack[-1][1]-i)
            else:
                res.appendleft(0)
            print("res ", res)
            # update the stack to account for the current Temp
            # that could be a future "warmer" temp
            stack.append([curTemp, i])
            print("stack ", stack)
        return list(res)