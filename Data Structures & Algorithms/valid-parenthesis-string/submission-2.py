class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            # real failure => stop => we cant have ) before a (
            if leftMax < 0:
                return False
            # this is just one bad guess => discard it and keep going
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

        
            