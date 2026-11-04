class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {}
        closeToOpen[')'] = '('
        closeToOpen[']'] = '['
        closeToOpen['}'] = '{'
        stack = []
        for c in s:
            if c in closeToOpen:
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0